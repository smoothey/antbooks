# Chapter 2: Build the thing that builds the things

<!-- p: 02-01 | agreed 2026-11-22 -->
I didn't start with a plan. From 14 September, the first day of my gardening leave, I spent the gaps between job applications in long chats with AI and reading about what other people were doing with it. None of that left a trace. The first thing that did was a repository, the folder where code and the history of every change to it live, for a series of technical study guides. I created it on 30 September, just before midnight. Every change saved to a repository carries a date, so from that night on there's a record of what I built and when.
<!-- src: review 22 Nov 01:21 (started 14 Sep, between job applications); Ant 22 Nov 02:00 (initial work in informal chats and own research); GitHub smoothey/ultimatetranscender created 2026-09-30T23:56Z, first commit 38d81a0 2026-09-30T23:51Z; CLAUDE.md (study guides never named) -->

<!-- p: 02-02 | agreed 2026-11-22 -->
Two weeks later, on 13 October, I started on Charlie's website. Charlie models as Charlie Doll, and she needed somewhere to show her work. I wanted an admin area where she could pick photos straight from the Google Drive folder that held her shoots, and a public site that showed watermarked versions. I tried a website builder first, one of the new ones where you describe what you want and AI puts it together. I used up the free credit and wasn't impressed. The same day I switched to Claude, on Azure, the cloud platform I know best.
<!-- src: GitHub smoothey/poseroll created 2026-10-13, first commit 7b58f1a 2026-10-13; r2antbooks notes/source-material/build-the-thing/2026-11-22-charlie-doll-origins.md (13 Oct: Base44 prompt, then Claude on Azure); memory, charlie-portfolio-site (Drive picker, watermarking; Base44 free credit, not impressed) -->

<!-- p: 02-03 | agreed 2026-11-22 -->
I'd expected to be writing and tweaking code. I realised straight away that I wasn't. I described what I wanted, read what came back, and said yes, no or not like that. By the end of the first day, 43 changes had been saved to the site. The next day there were 56, including the page we'd use to reveal it.
<!-- src: interview 2 (expected to write and tweak code); Ant 22 Nov (realised straight away I wasn't writing code); charlie-doll-origins note (43 commits 13 Oct; 56 commits 14 Oct incl. birthday reveal) -->

<!-- p: 02-04 | agreed 2026-11-22 -->
The site grew quickly, and so did my ambitions for it. I'd called the project Poseroll from the first day, because I could see it becoming a product for models and photographers one day. It also needed a helper inside the admin area: someone Charlie could ask how to do things. I'd built chatbots before, and most chatbots I'd used were woeful. I wanted this one to be cute and capable. So on 16 October he got a name, Jimmy, after our grey cat, and that same night a face to go with it.
<!-- src: charlie-doll-origins note (Poseroll named from day one; Jimmy first commit ffb0d3f 16 Oct 17:54, avatar same night); architecture docs, 21 Oct (site built so it can become Poseroll); interview 2 (cute and capable; chatbots woeful); smoothey/jimmy CLAUDE.md (grey cat) -->

<!-- p: 02-05 | agreed 2026-11-22 -->
Then I hit the problem that changed everything. Every new conversation with the AI started from nothing. I'd explain how the site worked, what we'd decided, what not to touch, and in every chat I'd explain it again, project after project. A lot of value was building up in those conversations, and almost none of it carried over. Some of it sat in the AI's memory, where I couldn't easily see it or check it. The rest just vanished.
<!-- src: interview 1b ("a lot of value sits in memories and isn't always visible to the person using the AI") -->

<!-- p: 02-06 | agreed 2026-11-22 -->
I'd tried to fix this once before, at work, with Azure DevOps. This time, on 18 October, I built a store of my own: a small service in my own Azure account where the AI could keep what it learnt and read it back next time. Decisions, notes, the list of work still to do, what had happened the night before. Almost straight away I turned it into an MCP server, which is a standard way for an AI to use outside tools. That meant any of my Claude chats could reach the store directly, read from it and write to it, without me copying anything across.
<!-- src: interview 1b (tried similar with ADO); interview 2 (memory store, almost immediately an MCP server); ADR 0002 (store in Ant's Azure); memory, jimmy (18 Oct: built in his own Azure, connected as an MCP connector); Jimmy Hub chat "Azure storage system for memories" 18 Oct -->

<!-- p: 02-07 | draft -->
That was the firewall lesson again, on a bigger scale. When I'd written down how the work should be done and given the AI somewhere to keep what it learnt, a job that took me hours took minutes. Now I wasn't doing it for one customer's firewall. I was doing it for everything I was building.
<!-- src: chapter 1, 01-13 (agreed); interview 1b (firewall before and after) -->

<!-- p: 02-08 | draft -->
Rules came next. I wanted every screen I built to feel the same, so I started writing down interface rules. I'd been an Apple fan once, and I borrowed the idea from Apple's interface guidelines: one written set of rules everyone follows, so you don't decide the same thing twice. The interface rules grew into rules for everything else: how work gets planned, who approves what, what must never happen. That became governance, and governance became Jimmy. Not just the cat in the admin area any more, but the system that holds the rules and runs the work.
<!-- src: interview 2, Q1 (consistent interface; Apple's interface rules; rules morphed into governance and later Jimmy) -->

<!-- p: 02-09 | draft -->
None of this was designed up front. I didn't sit down and plan a store, a set of rules and a system to run my projects. Each piece was the answer to the problem the last piece had shown up. Memory showed I needed one place for the truth. One place for the truth showed I needed rules about what went in it. Rules showed I needed something to follow them while I wasn't there.
<!-- src: interview 2 (developed organically); theme note on best practice layered on as needed -->

<!-- p: 02-10 | draft -->
On the evening of 18 October, the first scheduled run of the night began at 22:48. It worked on Charlie's site, the project I'd started all this for, and it finished at 23:45. By then nine changes were live on the site, all tested, every deployment green. There was a freeze built into the deployments for the week we'd reveal the site, so nothing could go out by accident. A privacy page explained how AI was used. And Jimmy no longer trusted chat history sent from the browser, so nobody could forge his past answers.
<!-- src: smoothey/jimmy governance/reports/2026-10-18/nightly-charliedoll.md (22:48 to 23:45; nine items live on main; deploys green; reveal freeze; privacy page; Jimmy history sealed) -->

<!-- p: 02-11 | draft -->
At 06:14 the next morning, a morning brief ran for the first time. It read every report from the night and wrote me one page. Three projects had run overnight. One had put its work live; another had its whole queue ready on a branch, waiting for me to merge. And there were 26 recommendations for me to agree, each with a reason, an action and a note on whether it could be done without me.
<!-- src: smoothey/jimmy governance/reports/2026-10-18/morning-brief.md (06:14, first run; runs table; 26 recommendations with why, action, type, size and unattended) -->

<!-- p: 02-12 | draft -->
Reading it, I realised I could genuinely be onto something. In software, DevOps is the name for the habits that take code from an idea to live and keep it running. This was the same thing, run by AI: AI DevOps, or whatever we end up calling it. I read every line. Then I went straight to Charlie's site, and to anything in Jimmy that might hold it up. Twenty-six decisions didn't daunt me, because I knew I could use AI to triage those too.
<!-- src: Ant 22 Nov 02:12 (onto something; AI DevOps "whatever we want to call it"; read it all; focused on Charlie Doll and Jimmy functionality that may hold it up; not daunted, could triage using AI) -->

<!-- p: 02-16 | draft -->
I still do. Even now, with a dashboard that shows every project, I often just ask the AI what needs my attention. The dashboard shows me everything. The question gets me a short list, in order, and I can argue with it. One I look at; the other I talk to. That's why I'm building a cockpit: one place that blends the two.
<!-- src: Ant 22 Nov 02:12 (often ask AI "What needs my attention"; curated, prioritised experience has value because it's interactive; cockpit built to create that blended experience) -->

<!-- p: 02-13 | draft -->
That's the idea this book is about, and it's simple enough to fit in one sentence. Stop doing the work, and build the thing that does the work. The website was the work. The store, the rules and the runs were the thing that builds the things. Once that existed, every project I added got the same memory, the same rules and the same nights for free.

<!-- p: 02-14 | draft -->
It also changed what I did all day. It was pointless for me to write code any more. The AI wrote it faster than I could, and it could work while I slept. What it couldn't do was decide where we were going, challenge its own decisions, design the way the work should flow, or check the result. That was where I added the most value. The idea I'd met in Economics GCSE had finally caught up with me.
<!-- src: early years note (realising it's pointless to write code; value from direction, critical review, process design, reviewing PRs); chapter 1, 01-24 (agreed) -->

<!-- p: 02-15 | draft -->
By the end of October the same system was running all of my projects: Charlie's site, a photo organiser, a series of technical study guides, a game, and the system itself. It had a home page of its own, which I called the Hub, where I could see every project's progress and the short list of things only I could decide. It wasn't finished. It still isn't. But the shape was there, and it's the shape the rest of this book describes.
<!-- src: architecture docs, 21 Oct (projects table); memory, jimmy (19 Oct: progress page on the store is his source of truth); CLAUDE.md (study guides never named) -->
