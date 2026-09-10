<!-- ===================== HERO SECTION ===================== -->

<h1 align="center">Hi, I'm Rahul Kumar 👋</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3500&pause=1000&color=0E75B6&center=true&vCenter=true&width=850&lines=Full-Stack+%26+AI+Engineer;Building+MCP+Servers+%26+Multi-Provider+LLM+Gateways;Sub-50ms+State+Sync+%26+Distributed+Systems" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/rahulxnit/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://github.com/rahulxgit"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://leetcode.com/u/S4gKOmKmsm/"><img src="https://img.shields.io/badge/LeetCode-1746_Max-FFA116?style=flat-square&logo=leetcode&logoColor=black" alt="LeetCode"/></a>
  <a href="mailto:rahulkumarshc00@gmail.com"><img src="https://img.shields.io/badge/Email-rahulkumarshc00%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://rahul-portfolio-eight-eta.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-Live-000000?style=flat-square&logo=vercel&logoColor=white" alt="Portfolio"/></a>
  <a href="https://drive.google.com/file/d/1CtBwvwxXaMn3tgoBT6EWJ9P7r4UOJkKr/view"><img src="https://img.shields.io/badge/Resume-PDF-4285F4?style=flat-square&logo=google-drive&logoColor=white" alt="Resume"/></a>
</p>

---

## About Me

I build web applications, backend services, and AI tooling. I graduated with a B.Tech from NIT Raipur (Class of 2026). Most recently, I spent 6 months as an SDE intern at Bluestock Fintech in Pune. I worked on three production web apps.

- **AI and Agent Systems:** Built an LLM router supporting 23 provider adapters with automatic failover, a Model Context Protocol (MCP) server over SSE, and a token streaming playground with an LCS token diff engine.
- **Real-Time and Backend:** Built sub-50ms relational state sync using InstantDB graph sockets, client-side daily puzzle generation in IndexedDB, and mobile background audio playback in React Native.
- **Bluestock Fintech (Feb 2026 to Aug 2026, 6 months):** Shipped features and fixed critical production bugs across 3 web apps. Tracked down and fixed the `startTimeRef` timer bug in Logic Looper, and cut server reads by ~70% using IndexedDB caching.
- **Problem Solving:** Solved 500+ problems across LeetCode (Contest Peak: 1,746), Codeforces, and CodeChef. Scored 99.41%ile in Naukri Campus Young Turks 2025 and AIR 242 in NCAT 2026.

---

## Technical Problems and Trade-offs

Here are five specific engineering bugs and design decisions from recent work:

1. **The `startTimeRef` scoring desync bug (Logic Looper)**
   - *Problem:* Players lost streaks and point multipliers during daily puzzle transitions across 10 game types.
   - *Root cause:* The scoring engine initialized `startTimeRef` to zero on mount. During fast restarts or seed changes, the timer component rendered before the ref updated. This produced negative or zero elapsed time deltas.
   - *Fix:* Added an explicit synchronous initialization guard to the timer hook lifecycle and separated score updates from React render passes. Zero UI re-renders, streaks persisted accurately.

2. **Call-stack overflow on deep folder trees (DriveClone)**
   - *Problem:* Calling `get_folder_size` on directories nested 10+ levels deep threw `RangeError: Maximum call stack size exceeded` in Node.js.
   - *Root cause:* Standard recursive directory traversal pushed each nested folder frame onto the V8 stack.
   - *Fix:* Swapped recursion for an iterative Breadth-First Search (BFS) queue using an array ($O(V+E)$). This flattened stack depth to $O(1)$. Memory stays flat even on deep folder hierarchies.

3. **Multi-provider health checks without burning API credits (AI Gateway)**
   - *Problem:* Pinging 23 LLM providers (OpenAI, Claude, Gemini, DeepSeek, Groq) with completions requests cost money on idle instances and risked rate limits.
   - *Fix:* Switched health checks from completions to lightweight `GET /models` queries run every 5 minutes. Providers stay validated, latency numbers stay fresh, and API cost is zero.

4. **UI thread drops below 15fps during token bursts (AI Inference Playground)**
   - *Problem:* Streaming tokens over Server-Sent Events (SSE) from fast providers like Cerebras and Groq fired state updates faster than the browser could paint.
   - *Fix:* Buffered incoming SSE chunks in memory and flushed them using `requestAnimationFrame` batching. The UI stayed locked at 60fps even under bursts of 100+ tokens/sec.

5. **$O(N)$ cascading deletes on folder trees (DriveClone)**
   - *Problem:* Deleting a top-level directory required querying and deleting hundreds of descendant folders individually. This held database connections open.
   - *Fix:* Combined an Adjacency List with a Materialized Path string (`/root/folderA/folderB`). Subtree deletion became a single regex query (`path: /^parent\/child/`). It finishes in one database roundtrip instead of recursive lookups.

---

## AI Gateway Architecture

```
   [ Client Request: POST /api/chat ]
                   │
                   ▼
       ┌────────────────────────┐
       │   AI Gateway Router    │ ◄─── In-Memory LRU (L1 Cache)
       └───────────┬────────────┘
                   │ Cache Miss
                   ▼
       ┌────────────────────────┐
       │   Redis L2 Cache       │ ◄─── Graceful Redis Fallback
       └───────────┬────────────┘
                   │ Cache Miss
                   ▼
    ┌──────────────────────────────┐
    │  Error-Classified Failover   │
    ├──────────────────────────────┤
    │ 429 Rate Limit  ──► Next Prov│
    │ 5xx Outage      ──► Next Prov│
    │ Auth / Quota    ──► Fail Fast│
    └──────────────┬───────────────┘
                   │
     ┌─────────────┼─────────────┐
     ▼             ▼             ▼
┌─────────┐   ┌─────────┐   ┌─────────┐
│ OpenAI  │   │ Claude  │   │ Gemini  │ ... (23 Providers)
└─────────┘   └─────────┘   └─────────┘
```

---

## Work Experience

### Software Development Engineer Intern, Bluestock Fintech
*Pune, India (Hybrid / Remote) | February 2026 to August 2026 (6 months)*  
*Verification Certificate:* [View Certificate](https://drive.google.com/file/d/1BaannFUBfAZV7AhhSX1nBF8O7QHcGoJf/view?usp=sharing)

Worked as an SDE intern on three production applications:

1. **Logic Looper:** Daily puzzle web app with 10 puzzle games (Sudoku, Nonogram, Futoshiki, KenKen, Kakuro, Hitori, Shikaku, Bridges, Slitherlink, Daily Word).
   - Generated daily puzzles on the client with `SHA256(YYYY-MM-DD + seed)` so every user gets the same puzzle without storing daily boards in a database.
   - Tracked down and fixed a race condition in `startTimeRef` where fast restarts wiped user streaks. The fix preserved streak counts and scoring multipliers across all games.
   - Added an IndexedDB-first caching layer that cut Firestore database reads by ~70% and kept puzzle validation under 50ms.

2. **AI Profile Picture Maker:** Production generative avatar tool.
   - Built an image processing pipeline with Stable Diffusion for generation, GFPGAN for face enhancement, and rembg for background removal.
   - Queued generation requests in Redis to handle GPU cold-starts and traffic spikes without dropped jobs.

3. **The Corporate Blog (TCB):** Company updates and technical publication site.
   - Built responsive article layouts with custom Markdown rendering, dynamic SEO tags, and optimized asset loading.

---

## Featured Projects

| Project | Stack | What It Does & Technical Details | Links |
| :--- | :--- | :--- | :--- |
| **[AI Gateway](https://github.com/rahulxgit/ai-gateway)** | TypeScript 5, Node.js, Express.js 4, Redis L2, SQLite (WAL mode), Docker, Jest, React | Multi-provider chat router supporting 23 model providers. Categorizes errors automatically: rotates to the next provider on 429 or 5xx, halts immediately on 401 or 403. Two-tier caching (in-memory LRU + Redis L2) stops duplicate API calls. Includes background health checks every 5 minutes and streaming for payloads up to 50MB. | [Live App](https://ai-gateway-alpha.vercel.app/) • [API](https://ai-gateway-wx35.onrender.com) • [Code](https://github.com/rahulxgit/ai-gateway) |
| **[Logic Looper](https://github.com/rahulxgit/logic-looper)** | React 19, TypeScript, Redux Toolkit, Firebase Auth, Firestore, IndexedDB, Tailwind CSS | Client-first puzzle platform with 10 game types. Creates daily puzzles using calendar dates and SHA256 seeds on the client. It stores zero puzzle boards on the server. Fixed a production `startTimeRef` race condition in the scoring engine. IndexedDB caching enables offline play and keeps move validation under 50ms. | [Live App](https://logic-looper-mu.vercel.app/) • [Code](https://github.com/rahulxgit/logic-looper) |
| **[DriveClone](https://github.com/rahulxgit/driveclone)** | React 18, Node.js, Express.js, MongoDB Atlas, Cloudinary CDN, MCP, JWT, Bcryptjs | Cloud drive with an integrated Model Context Protocol (MCP) server over SSE on port 5001. AI agents like Claude Desktop connect to it directly to create folders, list files, and check folder sizes. Uses an iterative BFS queue ($O(V+E)$) to prevent call-stack overflows on deep folders, and Materialized Paths for $O(1)$ subtree deletes. | [API](https://driveclone-api.onrender.com) • [Code](https://github.com/rahulxgit/driveclone) |
| **[AI Inference Playground](https://github.com/rahulxgit/ai-inference-playground)** | React 18, TypeScript 5, Vite 5, Tailwind CSS 3, Server-Sent Events (SSE) | Multi-model token streaming benchmark tool. Batches incoming SSE streams with `requestAnimationFrame` to keep the UI at 60fps during 100+ tokens/sec bursts. Includes an in-memory LCS token diff engine ($O(M \times N)$) that highlights token discrepancies while preserving whitespace. Displays live TTFT, tokens/sec, and latency stats. | [Live App](https://ai-inference-playground-iota.vercel.app/) • [Code](https://github.com/rahulxgit/ai-inference-playground) |
| **[Realtime Gallery](https://github.com/rahulxgit/realtime-gallery)** | React 18, Vite 5, InstantDB, TanStack Query v5, Zustand 5, Tailwind CSS | Collaborative image board with sub-50ms sync via InstantDB relational graph sockets. Uses atomic transactions (`db.transact`) so reaction counters and activity feeds stay in sync without orphans. Infinite scrolling uses an $O(N)$ `Map` deduplicator with smooth scroll linking to selected images. | [Live App](https://realtime-gallery-tau.vercel.app/) • [Code](https://github.com/rahulxgit/realtime-gallery) |
| **[Mume React Native](https://github.com/rahulxgit/mume-react-native)** | React Native 0.73, TypeScript 5, react-native-track-player 4.1, Shopify FlashList 1.6, Zustand 4.4 | Mobile music player with background audio playback via Android Foreground Services and iOS `AVQueuePlayer`. Adapts audio quality through a bitrate ladder (320kbps -> 160kbps -> 96kbps) during network drops. Replaced FlatList with Shopify FlashList for smooth 60fps scrolling and 5x lower memory usage. | [Code](https://github.com/rahulxgit/mume-react-native) |
| **[Smart Bookmark App](https://github.com/rahulxgit/smart-bookmark-app)** | Next.js 15 (App Router), React 19, Supabase SSR Auth, PostgreSQL RLS | Web bookmark manager with a four-tier architecture (UI -> Hooks -> Services -> DB). Uses server cookie sessions, route middleware, and PostgreSQL Row-Level Security policies to keep user records strictly separated. | [Walkthrough](https://www.loom.com/share/71832d00480b434eb2835f2d4fd92eee) • [Code](https://github.com/rahulxgit/smart-bookmark-app) |
| **[Swiggy SQL Analytics](https://github.com/rahulxgit/Swiggy-Case-Study-SQL)** | PostgreSQL, SQL CTEs, Window Functions, Indexing | Analytics study on consumer order datasets. Wrote PostgreSQL queries using CTEs and window functions (`DENSE_RANK`) to calculate monthly retention cohorts, churn rates, and checkout funnel drop-offs. | [Code](https://github.com/rahulxgit/Swiggy-Case-Study-SQL) |
| **[Developer Portfolio Hub](https://github.com/rahulxgit/rahul-portfolio)** | Vanilla HTML5, CSS3 Custom Properties, ES6+ JavaScript, Vercel | Personal portfolio site built with zero runtime dependencies. Reaches 100/100 on Google Lighthouse for Performance, Accessibility, Best Practices, and SEO. First Contentful Paint is under 100ms. | [Live Site](https://rahul-portfolio-eight-eta.vercel.app/) • [Code](https://github.com/rahulxgit/rahul-portfolio) |

---

## Technical Skills

| Layer | Tools and Technologies | Applied In |
| :--- | :--- | :--- |
| **AI and Agent Systems** | Model Context Protocol (MCP) Servers, Multi-Provider Routing, Automatic Failover, Token Streaming (SSE), LCS Token Diffing, Prompt Engineering, Stable Diffusion, GFPGAN | **AI Gateway**, **DriveClone MCP**, **AI Inference Playground** |
| **Backend and APIs** | Node.js, Express.js 4, REST APIs, Server-Sent Events (SSE), WebSockets, JWT, Rate Limiting, Helmet, Docker | **AI Gateway**, **DriveClone**, **Realtime Gallery** |
| **Databases and Caching** | PostgreSQL, MongoDB Atlas (Mongoose 8), SQLite (WAL Mode), Redis L2 (ioredis), InstantDB, IndexedDB, Supabase, Firebase Firestore | **AI Gateway**, **Logic Looper**, **DriveClone**, **Smart Bookmark** |
| **Frontend and Mobile** | React 19, Next.js 15 (App Router), React Native 0.73, Redux Toolkit, Zustand 5, Shopify FlashList 1.6, TanStack Query v5, Tailwind CSS 3, Vite 5 | **Logic Looper**, **Mume React Native**, **Realtime Gallery** |
| **Languages and Core** | TypeScript 5, JavaScript (ES6+), Python 3, SQL (PostgreSQL), Java, C++, Data Structures and Algorithms, System Design | Core problem solving across all projects |
| **DevOps and Testing** | Git, GitHub Actions, Docker, Jest, Postman, Linux, Vercel, Render, LaTeX | Build pipelines and testing across all projects |

---

## Competitive Programming and Verified Achievements

<table width="100%">
  <tr>
    <td width="70%"><b>LeetCode Contest Max Rating: 1,746</b> (Top 15% globally, 500+ problems solved across LeetCode, Codeforces, and CodeChef)</td>
    <td align="right"><a href="https://leetcode.com/u/S4gKOmKmsm/">[LeetCode Profile]</a></td>
  </tr>
  <tr>
    <td><b>Naukri Campus Young Turks 2025: 99.41 Percentile</b> (Ranked in top 1% nationwide out of hundreds of thousands of candidates)</td>
    <td align="right"><a href="https://www.naukri.com/campus/certificates/young_turks25_round_1_achievement/v0/68d9b36d7baf842bcc2d84c9?utm_source=certificate&utm_medium=copy&utm_campaign=68d9b36d7baf842bcc2d84c9">[Verify Certificate]</a></td>
  </tr>
  <tr>
    <td><b>All India NCAT 2026 (National Core Aptitude Test): AIR 242</b> (Score: 55/60, 98.88%ile in Engineering)</td>
    <td align="right"><a href="https://www.naukri.com/campus/certificates/nc_ai_ncat_participation_may_2026/v0/6a19907a542fee52d123f8c4?utm_source=certificate&utm_medium=copy&utm_campaign=6a19907a542fee52d123f8c4">[Verify]</a> • <a href="https://www.naukri.com/campus/contests/all-india-online-aptitude-test/leaderboard">[Leaderboard]</a></td>
  </tr>
  <tr>
    <td><b>TCS CodeVita Season 13: Global Rank ~8,552</b> (International contest with 100,000+ competitors)</td>
    <td align="right"><a href="https://drive.google.com/file/d/1jKomevh2ulQP1utY8s3Pc0fgK4KlO2ks/view?usp=sharing">[Verify Certificate]</a></td>
  </tr>
  <tr>
    <td><b>Polaris Fellowship 2026: Shortlisted for Round 2</b> (Selected for second stage evaluation for 10 fully-funded residential seats)</td>
    <td align="right"><i>Round 2 Shortlist</i></td>
  </tr>
  <tr>
    <td><b>Bluestock Fintech SDE Internship Certificate: 6 Months</b> (Full production ownership across 3 applications)</td>
    <td align="right"><a href="https://drive.google.com/file/d/1BaannFUBfAZV7AhhSX1nBF8O7QHcGoJf/view?usp=sharing">[Verify Certificate]</a></td>
  </tr>
  <tr>
    <td><b>Technical Leadership (NIT Raipur):</b> Co-organized national hackathon with 200+ attendees as Sponsorship & Outreach Lead (Innovation Cell) and Technical Events Coordinator (Robotics Club)</td>
    <td align="right"><i>NIT Raipur</i></td>
  </tr>
</table>

---

## Telemetry and Activity

<div align="center">
  <table border="0">
    <tr>
      <td align="center" valign="middle">
        <img src="https://streak-stats.demolab.com/?user=rahulxgit&theme=tokyonight&hide_border=true" alt="GitHub Streak" />
      </td>
      <td align="center" valign="middle">
        <img src="https://leetcard.jacoblin.cool/S4gKOmKmsm?theme=tokyonight&font=Fira%20Code&ext=contest" alt="LeetCode Stats" height="195"/>
      </td>
    </tr>
  </table>
</div>

### Recent Activity
<!-- RECENT_ACTIVITY:START -->
- Pushed to `main` in [`rahulxgit/spiderman`](https://github.com/rahulxgit/spiderman) (Sep 08, 2026)
- Pushed to `main` in [`rahulxgit/job-alert-bot`](https://github.com/rahulxgit/job-alert-bot) (Sep 09, 2026)
- Pushed to `main` in [`rahulxgit/rahulxgit`](https://github.com/rahulxgit/rahulxgit) (Sep 09, 2026)
- Pushed to `main` in [`rahulxgit/rahul-portfolio`](https://github.com/rahulxgit/rahul-portfolio) (Sep 09, 2026)
- Pushed to `main` in [`rahulxgit/mume-react-native`](https://github.com/rahulxgit/mume-react-native) (Sep 09, 2026)
<!-- RECENT_ACTIVITY:END -->

### Contribution Activity

<p align="center">
  <img src="https://raw.githubusercontent.com/rahulxgit/rahulxgit/output/github-contribution-grid-snake.svg" alt="Contribution Snake" />
</p>

---

## Contact

I am based in Pune, India, and open to SDE-1, Full-Stack, Backend, or AI engineering roles (Pune, Bengaluru, Hyderabad, Gurugram, or Remote).

<div align="center">
  <a href="https://www.linkedin.com/in/rahulxnit/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="mailto:rahulkumarshc00@gmail.com">
    <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  <a href="https://drive.google.com/file/d/1CtBwvwxXaMn3tgoBT6EWJ9P7r4UOJkKr/view">
    <img src="https://img.shields.io/badge/Resume_PDF-000000?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Resume PDF"/>
  </a>
  <a href="https://rahul-portfolio-eight-eta.vercel.app/">
    <img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/>
  </a>
  <a href="https://leetcode.com/u/S4gKOmKmsm/">
    <img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode"/>
  </a>
  <a href="https://github.com/rahulxgit">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</div>

<br>

<p align="center">
  Rahul Kumar
</p>
