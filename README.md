<!-- ===================== HERO SECTION ===================== -->

<div align="center">
  <h1>Hi there, I'm Rahul Kumar 👋</h1>

  <p align="center">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&duration=3200&pause=1000&color=0E75B6&center=true&vCenter=true&width=900&lines=Full-Stack+%26+AI+Systems+Engineer;Building+Native+MCP+Servers+%26+23-Provider+LLM+Gateways;Ex-SDE+Intern+%40+Bluestock+Fintech+(6+Months+Production);500%2B+DSA+Problems+Solved+%7C+LeetCode+1%2C746;B.Tech+Graduate+from+NIT+Raipur+(Class+of+2026)" alt="Typing SVG" />
  </p>

  <p align="center">
    <b>Full-Stack & AI Systems Engineer</b> • B.Tech from <b>National Institute of Technology, Raipur (Class of 2026)</b><br>
    <i>Production-first builder specializing in fault-tolerant AI infrastructure, native Model Context Protocol (MCP) servers, and low-latency distributed web platforms.</i>
  </p>

  <p align="center">
    <a href="https://drive.google.com/file/d/1CtBwvwxXaMn3tgoBT6EWJ9P7r4UOJkKr/view" target="_blank">
      <img src="https://img.shields.io/badge/📄_Resume_PDF-View_Verified-0A66C2?style=for-the-badge" alt="Resume PDF"/>
    </a>
    <a href="https://rahul-portfolio-eight-eta.vercel.app/" target="_blank">
      <img src="https://img.shields.io/badge/🌐_Portfolio-Live_Site-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Live Portfolio"/>
    </a>
    <a href="https://www.linkedin.com/in/rahulxnit/" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
    </a>
    <a href="mailto:rahulkumarshc00@gmail.com">
      <img src="https://img.shields.io/badge/Email-Get_in_Touch-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
    </a>
  </p>

  <p align="center">
    <a href="https://github.com/rahulxgit"><img src="https://komarev.com/ghpvc/?username=rahulxgit&label=Profile%20Views&color=0e75b6&style=flat-square" alt="Profile Views"/></a>
    <img src="https://img.shields.io/badge/Location-Pune%2C%20India-blue?style=flat-square" alt="Location"/>
    <img src="https://img.shields.io/badge/Target_Roles-SDE--1_%7C_Full--Stack_%7C_AI_Engineer-0E75B6?style=flat-square" alt="Target Roles"/>
    <img src="https://img.shields.io/badge/DSA-500%2B_Solved_(LeetCode_1746)-brightgreen?style=flat-square" alt="DSA Solved"/>
    <img src="https://img.shields.io/badge/Availability-Immediate_Joiner-success?style=flat-square" alt="Availability"/>
  </p>
</div>

---

## ⚡ Executive Summary

- 🎓 **B.Tech Graduate** from **National Institute of Technology, Raipur (NIT Raipur)**, Class of 2026.
- 💼 **Ex-SDE Intern @ Bluestock Fintech (Feb 2026 – Aug 2026 · 6 Months):** Owned architecture, implementation, debugging, and deployment across 3 production web applications. Resolved a critical scoring engine defect (`startTimeRef` zero-initialization bug) and reduced server database reads by ~70% via IndexedDB-first caching.
- 🤖 **Production AI Engineering Depth:** Built an enterprise **AI Gateway routing across 23 configured LLM provider adapters** with automated error-classified failover and dual-tier L1/L2 caching, and a **native Model Context Protocol (MCP) server** for autonomous AI agent filesystem operations.
- 🧠 **Algorithmic Rigor:** Solved **500+ DSA problems** across LeetCode, Codeforces, and CodeChef (**LeetCode Contest Rating: 1,746** · Top 15% globally). Scored **99.41 Percentile** nationwide in Naukri Campus Young Turks 2025 and **AIR 242** (98.88%ile) in All India NCAT 2026.
- 📍 **Location:** Pune, Maharashtra, India (Open to Pune, Bengaluru, Hyderabad, Gurugram, and Remote).
- 🚀 **Immediate Availability:** Actively interviewing for **SDE-1, Full-Stack Engineer, Backend Engineer, and AI Systems Engineer** roles at product companies and engineering-driven teams.

---

## 🛠️ Core Engineering Specialties & Architecture Paradigms

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  AI & AGENTIC SYSTEMS       │ Native MCP Servers • Multi-Provider Routing • SSE Streaming   │
│  DISTRIBUTED BACKEND        │ Dual-Tier Caching (L1 LRU + L2 Redis) • SQLite WAL • Docker   │
│  REAL-TIME & CLIENT-FIRST   │ WebSockets State Sync (InstantDB) • IndexedDB • Redux Toolkit │
│  CROSS-PLATFORM & MOBILE    │ React Native 0.73 • Background Audio Services • FlashList     │
│  ALGORITHMIC PERFORMANCE    │ BFS O(V+E) Directory Sizing • LCS Token Diffing • SHA256 Seed │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 💼 Production Work Experience

### 💻 Software Development Engineer Intern — **Bluestock Fintech**
*Pune, Maharashtra, India (Hybrid / Remote) • February 2026 – August 2026 (6 Months)*  
*Verification Certificate: [View Certificate](https://drive.google.com/file/d/1BaannFUBfAZV7AhhSX1nBF8O7QHcGoJf/view?usp=sharing)*

- Exercised full-lifecycle engineering ownership (architecture, development, debugging, and deployment) across **3 production applications**:
  1. **Logic Looper (Daily Puzzle Platform):**
     - Architected a client-first daily puzzle web platform featuring 10 distinct puzzle games (Sudoku, Nonogram, Futoshiki, KenKen, Kakuro, Hitori, Shikaku, Bridges, Slitherlink, and Daily Word).
     - Engineered cryptographic calendar date seeding (`SHA256(YYYY-MM-DD + seed)`) to generate identical daily puzzle boards globally with zero server database storage overhead.
     - **Critical Debugging Win:** Diagnosed and eliminated a persistent scoring engine defect caused by uninitialized timer references (`startTimeRef` zero-init bug), restoring accurate real-time scoring and persistent streaks across active user sessions.
     - Implemented an IndexedDB local caching layer that cut redundant backend reads by ~70% and guaranteed sub-50ms validation latency with complete offline playability.
  2. **AI Profile Picture Maker (Open Source Generative Platform):**
     - Engineered an asynchronous generative image pipeline utilizing **Stable Diffusion** for text-to-image synthesis, **GFPGAN** for facial enhancement, and **rembg** for automated background removal.
     - Containerized workers into Docker microservices orchestrated with Redis queues to handle burst image generation workloads without worker starvation.
  3. **The Corporate Blog (TCB):**
     - Designed and shipped a high-performance, responsive corporate publishing engine for company-wide news releases and technical engineering articles.
- **Codebase Hardening:** Decoupled hardcoded credentials into secure environment configurations, eliminated 13 dead code modules, and standardized Redux Toolkit provider trees.

---

## 🚀 Featured Engineering Projects

| Project | Core Stack | Architecture Highlights | Live & Code |
| :--- | :--- | :--- | :---: |
| **[AI Gateway](https://github.com/rahulxgit/ai-gateway)** | TypeScript 5, Express.js 4, Redis L2, SQLite WAL, Docker, Jest, React | Enterprise OpenAI-compatible chat router routing across **23 configured provider adapters** (OpenAI, Claude, Gemini, Groq, Cerebras, Mistral, DeepSeek, OpenRouter). Features intelligent error-classified failover (429/5xx vs auth/quota), dual-tier caching (L1 Memory LRU + L2 Redis), zero-token background health probing every 5 mins, vision streaming (50MB parser), and SQLite conversation persistence. | [Live Dashboard](https://ai-gateway-alpha.vercel.app/) • [API](https://ai-gateway-wx35.onrender.com) • [Code](https://github.com/rahulxgit/ai-gateway) |
| **[DriveClone + MCP Server](https://github.com/rahulxgit/driveclone)** | React 18, Node.js, Express, MongoDB Atlas, Cloudinary CDN, MCP, JWT | Production MERN cloud storage system featuring a **native Model Context Protocol (MCP) server** on port 5001 with SSE streaming, enabling AI agents (Claude Desktop) to execute directory operations autonomously. Implemented an iterative BFS directory sizing algorithm ($O(V+E)$) eliminating call-stack recursion overflow and a Materialized Path hierarchy for $O(1)$ single-regex cascading subtree deletions. | [API Endpoint](https://driveclone-api.onrender.com) • [Code](https://github.com/rahulxgit/driveclone) |
| **[Logic Looper](https://github.com/rahulxgit/logic-looper)** | React 19, TypeScript, Redux Toolkit, Firebase Auth & Firestore, IndexedDB | Client-first daily puzzle platform with 10 puzzle games. Uses cryptographic calendar date seeding (`SHA256`) for zero-server board generation. Resolved the production `startTimeRef` scoring engine defect and implemented IndexedDB caching for <50ms validation latency and offline play. | [Live App](https://logic-looper-mu.vercel.app/) • [Code](https://github.com/rahulxgit/logic-looper) |
| **[AI Inference Playground](https://github.com/rahulxgit/ai-inference-playground)** | React 18, TypeScript 5, Vite 5, Tailwind CSS, SSE, LLM APIs | Real-time multi-model LLM benchmarking suite. High-frequency token streaming visualization via Server-Sent Events (SSE) with `requestAnimationFrame` batching preventing UI thread freezes during 100+ tokens/sec bursts. Features custom in-memory Longest Common Subsequence (LCS, $O(M \times N)$) token diffing with whitespace preservation and live TTFT telemetry. | [Live Demo](https://ai-inference-playground-iota.vercel.app/) • [Code](https://github.com/rahulxgit/ai-inference-playground) |
| **[Realtime Gallery (ImageSync)](https://github.com/rahulxgit/realtime-gallery)** | React 18, Vite 5, InstantDB, TanStack Query v5, Zustand 5, Tailwind | Sub-50ms collaborative graph media platform built on InstantDB client-side relational graph database over WebSockets. Features atomic multi-collection transactions (`db.transact`) preventing orphaned state and TanStack Query v5 infinite scroll with $O(N)$ Map deduplication and smooth linking. | [Live App](https://realtime-gallery-tau.vercel.app/) • [Code](https://github.com/rahulxgit/realtime-gallery) |
| **[Mume Mobile](https://github.com/rahulxgit/mume-react-native)** | React Native 0.73, TypeScript 5, TrackPlayer 4.1, Shopify FlashList 1.6 | Cross-platform native music streaming engine. Headless background audio playback via Android Foreground Service and iOS `AVQueuePlayer` with lockscreen media controls and an adaptive bitrate fallback ladder (320kbps CD quality down to 96kbps). Shopify FlashList cell virtualization delivers 60fps scrolling with 5x lower memory footprint than FlatList. | [Code](https://github.com/rahulxgit/mume-react-native) |
| **[Smart Bookmark App](https://github.com/rahulxgit/smart-bookmark-app)** | Next.js 15 (App Router), React 19, Supabase SSR Auth, PostgreSQL RLS | Strictly layered web platform (UI -> Hooks -> Services -> DB) with server-side cookie sessions, protected route middleware, and PostgreSQL Row-Level Security (RLS) guaranteeing strict multi-tenant data isolation. | [Walkthrough](https://www.loom.com/share/71832d00480b434eb2835f2d4fd92eee) • [Code](https://github.com/rahulxgit/smart-bookmark-app) |
| **[Swiggy SQL Analytics](https://github.com/rahulxgit/Swiggy-Case-Study-SQL)** | PostgreSQL, SQL CTEs, Window Functions, Indexing | Operational analytics case study on consumer transaction datasets. Authored complex PostgreSQL analytical queries using CTEs and window functions (`DENSE_RANK`) for monthly cohort retention, churn rates, and multi-tier funnel conversion metrics. | [Code](https://github.com/rahulxgit/Swiggy-Case-Study-SQL) |
| **[Developer Portfolio Hub](https://github.com/rahulxgit/rahul-portfolio)** | Vanilla HTML5, CSS3 Custom Properties, ES6+ JavaScript, Vercel | Ultra-fast personal brand hub with zero external runtime dependencies. Achieves 100/100 Google Lighthouse scores across Performance, Accessibility, Best Practices, and SEO with <100ms First Contentful Paint. | [Live Site](https://rahul-portfolio-eight-eta.vercel.app/) • [Code](https://github.com/rahulxgit/rahul-portfolio) |

---

## 🧠 Technical Skills & Systems Toolbox

<table width="100%">
  <tr>
    <td width="20%"><b>AI & LLM Systems</b></td>
    <td>
      <img src="https://img.shields.io/badge/Model_Context_Protocol_(MCP)-10A37F?style=flat-square&logo=openai&logoColor=white"/>
      <img src="https://img.shields.io/badge/Multi--Provider_Routing-412991?style=flat-square&logo=anthropic&logoColor=white"/>
      <img src="https://img.shields.io/badge/Token_Streaming_(SSE)-FF6B6B?style=flat-square"/>
      <img src="https://img.shields.io/badge/LCS_Token_Diffing-0E75B6?style=flat-square"/>
      <img src="https://img.shields.io/badge/RAG_Pipelines-000000?style=flat-square"/>
      <img src="https://img.shields.io/badge/Vector_DBs-02569B?style=flat-square"/>
      <img src="https://img.shields.io/badge/Prompt_Engineering-3178C6?style=flat-square"/>
      <img src="https://img.shields.io/badge/Stable_Diffusion-FF9900?style=flat-square"/>
      <img src="https://img.shields.io/badge/GFPGAN-2496ED?style=flat-square"/>
    </td>
  </tr>
  <tr>
    <td width="20%"><b>Languages & Core</b></td>
    <td>
      <img src="https://img.shields.io/badge/TypeScript_5-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
      <img src="https://img.shields.io/badge/JavaScript_(ES6+)-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
      <img src="https://img.shields.io/badge/Python_3-3776AB?style=flat-square&logo=python&logoColor=white"/>
      <img src="https://img.shields.io/badge/SQL_(PostgreSQL)-4169E1?style=flat-square&logo=postgresql&logoColor=white"/>
      <img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=java&logoColor=white"/>
      <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white"/>
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td width="20%"><b>Frontend & Mobile</b></td>
    <td>
      <img src="https://img.shields.io/badge/React_19-20232A?style=flat-square&logo=react&logoColor=61DAFB"/>
      <img src="https://img.shields.io/badge/Next.js_15_(App_Router)-000000?style=flat-square&logo=next.js&logoColor=white"/>
      <img src="https://img.shields.io/badge/React_Native_0.73-20232A?style=flat-square&logo=react&logoColor=61DAFB"/>
      <img src="https://img.shields.io/badge/Redux_Toolkit-764ABC?style=flat-square&logo=redux&logoColor=white"/>
      <img src="https://img.shields.io/badge/Zustand_5-443E38?style=flat-square"/>
      <img src="https://img.shields.io/badge/Tailwind_CSS_3-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white"/>
      <img src="https://img.shields.io/badge/Shopify_FlashList-95BF47?style=flat-square&logo=shopify&logoColor=white"/>
      <img src="https://img.shields.io/badge/Vite_5-646CFF?style=flat-square&logo=vite&logoColor=white"/>
      <img src="https://img.shields.io/badge/TanStack_Query_v5-FF4154?style=flat-square"/>
    </td>
  </tr>
  <tr>
    <td width="20%"><b>Backend & Concurrency</b></td>
    <td>
      <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white"/>
      <img src="https://img.shields.io/badge/Express.js_4-000000?style=flat-square&logo=express&logoColor=white"/>
      <img src="https://img.shields.io/badge/RESTful_APIs-02569B?style=flat-square"/>
      <img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socket.io&logoColor=white"/>
      <img src="https://img.shields.io/badge/Redis_L2_Caching-DC382D?style=flat-square&logo=redis&logoColor=white"/>
      <img src="https://img.shields.io/badge/JWT_Authentication-000000?style=flat-square&logo=json-web-tokens&logoColor=white"/>
      <img src="https://img.shields.io/badge/Bcryptjs-5B5B5B?style=flat-square"/>
      <img src="https://img.shields.io/badge/Rate_Limiting-20232A?style=flat-square"/>
    </td>
  </tr>
  <tr>
    <td width="20%"><b>Databases & Storage</b></td>
    <td>
      <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"/>
      <img src="https://img.shields.io/badge/MongoDB_Atlas-47A248?style=flat-square&logo=mongodb&logoColor=white"/>
      <img src="https://img.shields.io/badge/SQLite_(WAL_Mode)-003B57?style=flat-square&logo=sqlite&logoColor=white"/>
      <img src="https://img.shields.io/badge/InstantDB_(Realtime_Graph)-10A37F?style=flat-square"/>
      <img src="https://img.shields.io/badge/Firebase_Firestore-FFCA28?style=flat-square&logo=firebase&logoColor=black"/>
      <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white"/>
      <img src="https://img.shields.io/badge/IndexedDB_(Client_Cache)-0E75B6?style=flat-square"/>
    </td>
  </tr>
  <tr>
    <td width="20%"><b>DevOps & Infrastructure</b></td>
    <td>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
      <img src="https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker&logoColor=white"/>
      <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/>
      <img src="https://img.shields.io/badge/GitHub_Actions_(CI/CD)-2088FF?style=flat-square&logo=github-actions&logoColor=white"/>
      <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white"/>
      <img src="https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black"/>
      <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white"/>
      <img src="https://img.shields.io/badge/Jest-C21325?style=flat-square&logo=jest&logoColor=white"/>
      <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"/>
    </td>
  </tr>
</table>

---

## 🏆 Competitive Programming & Verified National Achievements

<table width="100%">
  <tr>
    <td width="70%"><b>LeetCode Contest Max Rating: 1,746</b> (Top 15% Globally • 500+ Algorithmic Problems Solved across LeetCode, Codeforces, and CodeChef)</td>
    <td align="right"><a href="https://leetcode.com/u/S4gKOmKmsm/">[LeetCode Profile]</a></td>
  </tr>
  <tr>
    <td><b>Naukri Campus Young Turks 2025: 99.41 Percentile</b> (Ranked in Top 1% nationally out of hundreds of thousands of engineering participants)</td>
    <td align="right"><a href="https://www.naukri.com/campus/certificates/young_turks25_round_1_achievement/v0/68d9b36d7baf842bcc2d84c9?utm_source=certificate&utm_medium=copy&utm_campaign=68d9b36d7baf842bcc2d84c9">[Verify Certificate]</a></td>
  </tr>
  <tr>
    <td><b>All India NCAT 2026 (National Core Aptitude Test): AIR 242</b> (Score: 55/60 • 98.88 Percentile in Engineering)</td>
    <td align="right"><a href="https://www.naukri.com/campus/certificates/nc_ai_ncat_participation_may_2026/v0/6a19907a542fee52d123f8c4?utm_source=certificate&utm_medium=copy&utm_campaign=6a19907a542fee52d123f8c4">[Verify]</a> • <a href="https://www.naukri.com/campus/contests/all-india-online-aptitude-test/leaderboard">[Leaderboard]</a></td>
  </tr>
  <tr>
    <td><b>TCS CodeVita Season 13: Global Rank ~8,552</b> (International contest with 100,000+ competitors)</td>
    <td align="right"><a href="https://drive.google.com/file/d/1jKomevh2ulQP1utY8s3Pc0fgK4KlO2ks/view?usp=sharing">[Verify Certificate]</a></td>
  </tr>
  <tr>
    <td><b>Polaris Fellowship 2026: Shortlisted for Round 2</b> (Top national candidates for 10 fully-funded residential seats)</td>
    <td align="right"><i>Round 2 Shortlist</i></td>
  </tr>
  <tr>
    <td><b>Bluestock Fintech SDE Internship Certificate: 6 Months</b> (Full production ownership across 3 applications)</td>
    <td align="right"><a href="https://drive.google.com/file/d/1BaannFUBfAZV7AhhSX1nBF8O7QHcGoJf/view?usp=sharing">[Verify Certificate]</a></td>
  </tr>
  <tr>
    <td><b>Technical Leadership (NIT Raipur):</b> Co-organized national hackathon with 200+ participants as Sponsorship & Outreach Lead (Innovation Cell) and Technical Events Coordinator (Robotics Club)</td>
    <td align="right"><i>NIT Raipur</i></td>
  </tr>
</table>

---

<!-- ===================== METRICS SECTION ===================== -->
## 📊 Live Coding Telemetry & Activity

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

### 🐍 Contribution Activity Graph

<p align="center">
  <img src="https://raw.githubusercontent.com/rahulxgit/rahulxgit/output/github-contribution-grid-snake.svg" alt="Contribution Snake" />
</p>

---

## 🤝 Let's Build Together

I am actively interviewing for **Software Development Engineer (SDE-1), Full-Stack Engineer, Backend Engineer, and AI Systems Engineer** positions. If you are building high-scale distributed systems, agentic AI platforms, or products that value rock-solid engineering and low-latency performance, let's talk.

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
  <i>"Production-first engineering: build systems that withstand real-world traffic, failover gracefully, and deliver measurable business value."</i><br>
  Built by <b><a href="https://github.com/rahulxgit">Rahul Kumar</a></b>
</p>
