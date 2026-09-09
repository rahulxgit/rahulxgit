
<div align="center">

# Rahul Kumar

**Full-stack & AI systems engineer** · NIT Raipur, B.Tech '26 · Pune, India

Building LLM infrastructure that survives production traffic, not just demos.

[Resume](https://drive.google.com/file/d/1CtBwvwxXaMn3tgoBT6EWJ9P7r4UOJkKr/view) · [Portfolio](https://rahul-portfolio-eight-eta.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/rahulxnit/) · [rahulkumarshc00@gmail.com](mailto:rahulkumarshc00@gmail.com)

</div>

---

## About

I graduate from NIT Raipur in 2026 and spent the last six months as an SDE intern at Bluestock Fintech, shipping three production apps end to end. Outside of work I build LLM infra on the side: a multi-provider gateway with automatic failover, a native MCP server for AI agents, and a token-streaming playground that had to survive 100+ tokens/sec without freezing the UI.

I solve about 500 DSA problems for fun (LeetCode rating 1,746, top 15% globally) and did well enough in a couple of national tests to put on this README: 99.41 percentile in Naukri Young Turks 2025, AIR 242 in NCAT 2026.

Looking for SDE-1, full-stack, or AI systems roles in Pune, Bengaluru, Hyderabad, Gurugram, or remote. Available immediately.


---

## Bugs I actually had to fix

**The `startTimeRef` bug in Logic Looper.** Real-time scoring and streak counters would silently drift out of sync whenever a user restarted a puzzle quickly, because the timer ref never got reinitialized. Fixed the lifecycle without triggering re-renders across all 10 puzzle boards, which was the actual hard part.

**Node's call stack couldn't handle deep folder trees in DriveClone.** Recursive directory sizing threw `RangeError: Maximum call stack size exceeded` on deeply nested folders. Rewrote it as an iterative BFS (O(V+E)) so memory stays predictable no matter how deep the tree goes.

**Health checks were burning API credits in AI Gateway.** Pinging providers with real chat completions to check if they're alive is expensive and dumb. Switched to lightweight `GET /models` probes every 5 minutes across the provider adapters, so latency data stays fresh at zero token cost.

**The UI froze under fast token streams in AI Inference Playground.** SSE updates at 100+ tokens/sec were flooding the main thread. Batched renders with `requestAnimationFrame` and wrote a small in-memory LCS diff engine to keep whitespace intact while comparing streamed tokens, and got it back to a steady 60fps.

**Recursive folder deletes were slow in DriveClone.** Deleting a folder tree meant thousands of individual `deleteOne` calls. Switched to a materialized path schema so an entire subtree deletes in one regex query instead.

---

## AI Gateway, roughly how it works

```
Client request (OpenAI-style chat format)
        │
        ▼
Express middleware (rate limiting, 50MB vision payload parsing)
        │
        ▼
Cache check ── L1 memory LRU ── hit (~10ms)
        │
        └── miss ── L2 Redis ── hit (~25ms)
                │
                └── miss
                        │
                        ▼
        Router across provider adapters
        (OpenAI, Claude, Gemini, Groq, Cerebras, Mistral...)
                │
        ┌───────┴────────┐
        │                │
   transient error   permanent error (401 / quota)
   (429 / 5xx)        mark provider degraded,
   retry next            route elsewhere
   provider
        │
        ▼
   success → write to SQLite (WAL) → stream response via SSE
```

---

## Work experience

**SDE Intern, Bluestock Fintech** — Pune (hybrid/remote), Feb 2026 to Aug 2026 · [certificate](https://drive.google.com/file/d/1BaannFUBfAZV7AhhSX1nBF8O7QHcGoJf/view?usp=sharing)

Owned three apps from architecture through deployment:

- **Logic Looper** — a daily puzzle platform with 10 games (Sudoku, Nonogram, Futoshiki, KenKen, Kakuro, Hitori, Shikaku, Bridges, Slitherlink, Daily Word). Puzzles are generated from a SHA256 hash of the calendar date, so every player worldwide gets the same board with zero server storage. Added an IndexedDB caching layer that cut backend reads by roughly 70% and got validation under 50ms, with full offline play.
- **AI Profile Picture Maker** — an open-source image pipeline using Stable Diffusion for generation, GFPGAN for face restoration, and rembg for background removal, running as Dockerized workers behind a Redis queue.
- **The Corporate Blog** — a publishing platform for internal engineering and company updates.

Also cleaned up the codebase along the way: pulled hardcoded credentials into env vars, deleted 13 dead files, and standardized the Redux Toolkit setup.

---

## Projects

**[AI Gateway](https://github.com/rahulxgit/ai-gateway)** — TypeScript, Express, Redis, SQLite (WAL)
An OpenAI-compatible router across multiple LLM provider adapters with error-classified failover (rate limits and server errors trigger fallback, auth and quota errors mark a provider degraded), two-tier caching, and background health probing. [Live](https://ai-gateway-alpha.vercel.app/) · [API](https://ai-gateway-wx35.onrender.com)

**[DriveClone + MCP Server](https://github.com/rahulxgit/driveclone)** — MERN, MongoDB, native MCP
A Google Drive clone with an actual MCP server on port 5001, so Claude Desktop (or any MCP client) can run directory operations on it directly. Iterative BFS for sizing, materialized paths for fast deletes. [API](https://driveclone-api.onrender.com)

**[Logic Looper](https://github.com/rahulxgit/logic-looper)** — React 19, Redux Toolkit, Firebase, IndexedDB
Same project as the Bluestock work above, maintained as an independent open-source repo. [Live](https://logic-looper-mu.vercel.app/)

**[AI Inference Playground](https://github.com/rahulxgit/ai-inference-playground)** — React, Vite, SSE
Benchmarks multiple LLMs side by side with live token streaming, TTFT numbers, and a custom LCS-based diff view between model outputs. [Live](https://ai-inference-playground-iota.vercel.app/)

**[Realtime Gallery](https://github.com/rahulxgit/realtime-gallery)** — React, InstantDB, TanStack Query
A collaborative photo gallery synced over WebSockets via InstantDB, with atomic multi-collection transactions so nothing ends up orphaned mid-update. [Live](https://realtime-gallery-tau.vercel.app/)

**[Mume](https://github.com/rahulxgit/mume-react-native)** — React Native, TrackPlayer
A music streaming app with headless background playback (Android foreground service, iOS AVQueuePlayer), lockscreen controls, and adaptive bitrate fallback. Uses Shopify's FlashList for scrolling performance.

**[Smart Bookmark App](https://github.com/rahulxgit/smart-bookmark-app)** — Next.js 15, Supabase
Layered cleanly (UI, hooks, services, DB) with server-side sessions and Postgres row-level security for multi-tenant isolation. [Demo](https://www.loom.com/share/71832d00480b434eb2835f2d4fd92eee)

**[Swiggy SQL Analytics](https://github.com/rahulxgit/Swiggy-Case-Study-SQL)** — PostgreSQL
Cohort retention, churn, and funnel analysis on a transactions dataset, written with CTEs and window functions.

**[Portfolio site](https://rahul-portfolio-eight-eta.vercel.app/)** — vanilla HTML/CSS/JS
No frameworks, no build step. 100/100 on Lighthouse across the board, under 100ms first contentful paint.

---

## Stack

| Area | Tools |
|---|---|
| AI / agents | MCP servers, multi-provider LLM routing, SSE token streaming, prompt engineering, Stable Diffusion |
| Backend | Node.js, Express, REST, WebSockets, JWT, Docker |
| Data | PostgreSQL, MongoDB, SQLite (WAL), Redis, InstantDB, Firebase, Supabase |
| Frontend / mobile | React, Next.js, React Native, Redux Toolkit, Zustand, TanStack Query, Tailwind |
| Languages | TypeScript, JavaScript, Python, SQL, Java, C++ |
| Tooling | Git, GitHub Actions, Jest, Postman, Vercel, Render |

---

## Numbers, for what they're worth

- LeetCode contest rating 1,746, top 15% globally, 500+ problems solved across LeetCode, Codeforces, and CodeChef → [profile](https://leetcode.com/u/S4gKOmKmsm/)
- Naukri Campus Young Turks 2025: 99.41 percentile → [certificate](https://www.naukri.com/campus/certificates/young_turks25_round_1_achievement/v0/68d9b36d7baf842bcc2d84c9)
- All India NCAT 2026: AIR 242, 55/60, 98.88 percentile → [certificate](https://www.naukri.com/campus/certificates/nc_ai_ncat_participation_may_2026/v0/6a19907a542fee52d123f8c4)
- TCS CodeVita Season 13: global rank ~8,552 out of 100,000+ → [certificate](https://drive.google.com/file/d/1jKomevh2ulQP1utY8s3Pc0fgK4KlO2ks/view?usp=sharing)
- Polaris Fellowship 2026: shortlisted for round 2 (10 residential seats nationally)
- Sponsorship & Outreach Lead, Innovation Cell, and Technical Events Coordinator, Robotics Club, at NIT Raipur, co-organized a 200+ participant hackathon

---

## Activity

<div align="center">
<img src="https://streak-stats.demolab.com/?user=rahulxgit&theme=tokyonight&hide_border=true" alt="GitHub Streak" width="48%"/>
<img src="https://leetcard.jacoblin.cool/S4gKOmKmsm?theme=tokyonight&font=Fira%20Code&ext=contest" alt="LeetCode Stats" width="48%"/>
</div>

<p align="center">
<img src="https://raw.githubusercontent.com/rahulxgit/rahulxgit/output/github-contribution-grid-snake.svg" alt="Contribution Snake" />
</p>

---

If you're working on something with real latency or reliability constraints, or just want to talk shop about LLM infra, my inbox is open.

[rahulkumarshc00@gmail.com](mailto:rahulkumarshc00@gmail.com) · [+91 7762068086](tel:+917762068086)
