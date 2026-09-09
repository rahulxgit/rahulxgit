import os
import re
import json
import urllib.request
import datetime

def fetch_recent_activity(username="rahulxgit", max_items=5):
    url = f"https://api.github.com/users/{username}/events/public?per_page=30"
    headers = {"User-Agent": "Mozilla/5.0"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        events = json.loads(resp.read().decode("utf-8"))
    
    lines = []
    seen = set()

    for e in events:
        etype = e.get("type")
        repo_name = e.get("repo", {}).get("name", "")
        repo_url = f"https://github.com/{repo_name}"
        created_at = e.get("created_at", "")
        
        try:
            dt = datetime.datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            date_str = dt.strftime("%b %d, %Y")
        except Exception:
            date_str = ""

        # Skip automated commits or activity updater commits on this repo
        if repo_name == f"{username}/{username}":
            commits = e.get("payload", {}).get("commits") or []
            if any("chore(activity)" in (c.get("message") or "") for c in commits):
                continue

        key = (etype, repo_name, date_str)
        if key in seen:
            continue
        seen.add(key)

        date_suffix = f" ({date_str})" if date_str else ""

        if etype == "PushEvent":
            commits = e.get("payload", {}).get("commits") or []
            branch = (e.get("payload", {}).get("ref") or "main").replace("refs/heads/", "")
            if commits:
                count = len(commits)
                c_str = f"{count} commit" if count == 1 else f"{count} commits"
                msg = (commits[0].get("message") or "").split("\n")[0]
                if len(msg) > 50:
                    msg = msg[:47] + "..."
                lines.append(f"- Pushed {c_str} to [`{repo_name}`]({repo_url}): \"{msg}\"{date_suffix}")
            else:
                lines.append(f"- Pushed to `{branch}` in [`{repo_name}`]({repo_url}){date_suffix}")
        elif etype == "PullRequestEvent":
            action = e.get("payload", {}).get("action", "opened")
            pr = e.get("payload", {}).get("pull_request", {})
            pr_title = pr.get("title", "")
            pr_url = pr.get("html_url", repo_url)
            pr_num = pr.get("number", "")
            lines.append(f"- {action.capitalize()} PR [#{pr_num} {pr_title}]({pr_url}) in [`{repo_name}`]({repo_url}){date_suffix}")
        elif etype == "CreateEvent":
            ref_type = e.get("payload", {}).get("ref_type")
            if ref_type == "repository":
                lines.append(f"- Created repository [`{repo_name}`]({repo_url}){date_suffix}")
        elif etype == "WatchEvent":
            lines.append(f"- Starred [`{repo_name}`]({repo_url}){date_suffix}")
        elif etype == "ForkEvent":
            forkee = e.get("payload", {}).get("forkee", {}).get("full_name", "")
            lines.append(f"- Forked [`{repo_name}`]({repo_url}) to [`{forkee}`](https://github.com/{forkee}){date_suffix}")

        if len(lines) >= max_items:
            break

    return "\n".join(lines)

def update_readme(readme_path, activity_md):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"(<!-- RECENT_ACTIVITY:START -->)(.*?)(<!-- RECENT_ACTIVITY:END -->)"
    replacement = f"\\1\n{activity_md}\n\\3"

    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("README.md updated with latest activity.")
        else:
            print("No changes in recent activity.")
    else:
        print("Marker tags not found in README.md.")

if __name__ == "__main__":
    readme_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "README.md")
    if not os.path.exists(readme_file):
        readme_file = "README.md"
    
    activity = fetch_recent_activity()
    if activity:
        update_readme(readme_file, activity)
    else:
        print("No activity fetched.")
