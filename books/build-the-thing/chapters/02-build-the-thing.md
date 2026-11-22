# Chapter 2: Build the thing that builds the things

<!-- p: 02-01 | draft -->
The website came first. Charlie models as Charlie Doll, and she needed somewhere to show her work. I wanted an admin area where she could pick photos straight from the Google Drive folder that held her shoots, and a public site that showed watermarked versions. I started on it on 14 September, the first day of my gardening leave, in the gaps between job applications.
<!-- src: memory, charlie-portfolio-site (Drive picker, watermarking, Azure); review 22 Nov 01:21 (started 14 Sep); smoothey/jimmy CLAUDE.md (Charlie models as Charlie Doll) -->

<!-- p: 02-02 | draft -->
I tried a website builder first, one of the new ones where you describe what you want and AI puts it together. I used up the free credit and wasn't impressed. So I decided to build it properly, with Claude, on Azure, the cloud platform I know best. I still expected to write a fair amount of the code myself.
<!-- src: memory, charlie-portfolio-site (tried Base44, used the free credit, not impressed; build with Claude on Azure); interview 2 (expected to write and tweak code) -->

<!-- p: 02-03 | draft -->
[GAP: what the first few weeks of building the site were like. When did you realise you weren't writing the code?]

<!-- p: 02-04 | draft -->
The site grew quickly, and so did my ambitions for it. It became something that could one day be a product for models and photographers, which I called Poseroll. It also needed a helper inside the admin area: someone Charlie could ask how to do things. I'd built chatbots before, and most chatbots I'd used were woeful. I wanted this one to be cute and capable. So he got a name, Jimmy, after our grey cat, and a face to go with it.
<!-- src: architecture docs, 21 Oct (site built so it can become Poseroll; Jimmy inside the admin); interview 2 (persona: cute and capable; chatbots woeful); smoothey/jimmy CLAUDE.md (Jimmy is Ant and Charlie's grey cat) -->

<!-- p: 02-05 | draft -->
Then I hit the problem that changed everything. Every new conversation with the AI started from nothing. I'd explain how the site worked, what we'd decided, what not to touch, and the next day I'd explain it again. A lot of value was building up in those conversations, and almost none of it carried over. Some of it sat in the AI's memory, where I couldn't easily see it or check it. The rest just vanished.
<!-- src: interview 1b ("a lot of value sits in memories and isn't always visible to the person using the AI") -->

<!-- p: 02-06 | draft -->
I'd tried to fix this once before, at work, with Azure DevOps. This time I built a store of my own: a small service in my own Azure account where the AI could keep what it learnt and read it back next time. Decisions, notes, the list of work still to do, what had happened the night before. Almost straight away I turned it into an MCP server, which is a standard way for an AI to use outside tools. That meant any of my Claude chats could reach the store directly, read from it and write to it, without me copying anything across.
<!-- src: interview 1b (tried similar with ADO); interview 2 (memory store, almost immediately an MCP server); ADR 0002 (store in Ant's Azure); memory, jimmy (18 Oct: built in his own Azure, connected as an MCP connector) -->

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
[GAP: what it felt like to read that first brief. Was there a moment you thought "this actually works"? Were there overnight runs before 18 October, started from a chat?]

<!-- p: 02-13 | draft -->
That's the idea this book is about, and it's simple enough to fit in one sentence. Stop doing the work, and build the thing that does the work. The website was the work. The store, the rules and the runs were the thing that builds the things. Once that existed, every project I added got the same memory, the same rules and the same nights for free.

<!-- p: 02-14 | draft -->
It also changed what I did all day. It was pointless for me to write code any more. The AI wrote it faster than I could, and it could work while I slept. What it couldn't do was decide where we were going, challenge its own decisions, design the way the work should flow, or check the result. That was where I added the most value. The idea I'd met in Economics GCSE had finally caught up with me.
<!-- src: early years note (realising it's pointless to write code; value from direction, critical review, process design, reviewing PRs); chapter 1, 01-24 (agreed) -->

<!-- p: 02-15 | draft -->
By the end of October the same system was running all of my projects: Charlie's site, a photo organiser, a series of technical study guides, a game, and the system itself. It had a home page of its own, which I called the Hub, where I could see every project's progress and the short list of things only I could decide. It wasn't finished. It still isn't. But the shape was there, and it's the shape the rest of this book describes.
<!-- src: architecture docs, 21 Oct (projects table); memory, jimmy (19 Oct: progress page on the store is his source of truth); CLAUDE.md (study guides never named) -->
