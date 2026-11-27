# Chapter 18: Learning by building

<!--
First draft, 27 Nov 2026 (Ant's pick from the content brainstorm, 17:25). Sources: Ant in the Jimmy project chat, 26 Nov (late: "enjoying learning through the Wall graphics work"); project docs claude/wall-space-theme.md, claude/jimmy-9.md; r2jimmy decisions sprint-2026-11-25-pods, sprint-2026-11-25-idles-3, own-photo-models-2026-11-21, togmatic-runs-build-live-coaching-2026-11-02; Ant's notes on the camera app (Nov 2026: no camera yet; wants a Canon). The craft business named only as "a craft business I run" (Ant, 27 Nov 17:25).
Gaps for Ant at 18-07.
-->

<!-- p: 18-01 | draft 2026-11-27 -->
Some of the deepest learning I've done in the last two months started as play. The graphics on the Hub's Wall began as a bit of whimsy. They were also an excuse: a reason to learn more, and to explore areas I'd never explored properly. Late one night in November, deep in another round of them, I noticed I was enjoying it for a reason I hadn't expected. It wasn't only the result. It was what I was picking up on the way.
<!-- src: store notes/interviews/build-the-thing/2026-11-27-learning-by-building-and-dan.md (Ant, 17:43: "The Wall's space graphics started a bit of whimsey and a premise to learn more and explore areas I hadn't explored as fully"; "seriously deep learning can come from play"); Ant, Jimmy project chat, 26 Nov late (enjoying learning through the Wall graphics work). Replaces the drafter's "more new things in the last two months than in the five years before" -->

<!-- p: 18-02 | draft 2026-11-27 -->
The Wall is a page on the Hub that shows everything that's going on, as space. Each project is a planet. The computers doing the work are satellites that fly out and circle the planet they're working for. Jimmy sits in the middle, lighting them. The sky changes with the hour, like the sky over London through the day. I'd never built anything like it. I didn't know how a star field is drawn, or how light falls on a sphere, or how to make a sky change gradually rather than jump.
<!-- src: Ant, 25 Nov (space theme: projects as planets, runners as satellites flying out to circle the planet they work for, planets lit from Jimmy in the middle, the sky changing with the hour); Ant, 26 Nov (an all-day London sky colour); Ant, 27 Nov ("wants the sky to change gradually, never cut over"); project doc claude/wall-space-theme.md. The list of what he didn't know is the drafter's: Ant to check -->

<!-- p: 18-09 | draft 2026-11-27 -->
Then something I hadn't planned happened. The Wall stopped being a toy. It's becoming my main workspace, with the monitoring rolled into the same screen. When something on it needs fixing, I can start the fix from there, and it hands straight over to the Cockpit. That's now faster than doing the same job in the desktop app, and it uses far fewer tokens. A thing I built to learn on turned into the thing I work in.
<!-- src: store notes/interviews/build-the-thing/2026-11-27-learning-by-building-and-dan.md (Ant, 17:43: "in doing so the Wall is becoming my main workspace and monitoring rolled into one, using the fix functionality and integration with the cockpit is now becoming faster than doing it in Claude desktop and is much more token efficient"); Ant, 24 Nov (the Wall's "Investigate" button on Jimmy's thoughts); chapter 26 (draft: the Cockpit).  "the desktop app" (Ant, 27 Nov 17:48). New id 18-09 (after 18-02) -->

<!-- p: 18-03 | draft 2026-11-27 -->
3D Jimmy taught me more. I now know what a rig is, and why a model needs one closed skin before it will bend. I know that real-time fur is usually a trick: layers of shells drawn one over another. I know what a range-of-motion test is, because version nine has to pass one before anything pretty goes on. None of those were on my list of things to learn. I learnt them because I needed the words to steer.
<!-- src: claude/jimmy-9.md (one closed skin; Rigify's cat skeleton; "soft layered fur drawn by the web viewer (shell fur, a well-known cheap trick for real-time fur)"; the range of motion test); chapter 17 (draft: version nine). "I learnt them because I needed the words to steer" is the drafter's: Ant to agree -->

<!-- p: 18-10 | draft 2026-11-27 -->
What I learn in one place turns up in another. On the Roblox game, I learnt how to set up an MCP server: a connector that lets the AI work another program directly. We took that set-up across to the 3D work on Jimmy. Then I noticed that several chats could be using it at once and treading on each other's work, so we added a lock: one chat at a time. Next we copied the whole set-up onto my second PC. That raised the next problem. The models and files couldn't just live on one computer, and they needed keeping safe. None of it was planned. Each step came out of the one before.
<!-- src: store notes/interviews/build-the-thing/2026-11-27-learning-by-building-and-dan.md (Ant, 17:43: "Some of what I learnt from Robyn's Roblox graphics and AI fed into my 3d work"; 17:47: "the setup how to set up an MCP server, we took that and developed a lock idea when I identified I could have multiple chats interfering with each other, we then duplicated the setup on Balrog, we then realised the assets couldn't just live on one computer (and also needed to be preserved)").  The MCP server was for Blender (Ant, 27 Nov 17:48). "MCP server" explained the first time it appears; add to the glossary. PC name left out. The last two sentences are the drafter's -->

<!-- p: 18-04 | draft 2026-11-27 -->
That's how the learning happens. You ask for something. It comes back wrong. To say why it's wrong, you need a word you didn't have, and the AI gives you that word along with the fix. Chapter 12 was about steering. This is what steering teaches you. The next time, you can ask for the right thing first.
<!-- src: chapter 12 (draft: driving, or being driven; the test anyone can apply). Drafter's synthesis: Ant to agree -->

<!-- p: 18-11 | draft 2026-11-27 -->
The way I work with the tools grew up too. At first, the AI wrote the prompts and I pasted them into the image tool myself. Now it drives the image tool directly, in my browser, while I watch and step in. That's chapter 17's idea of one AI driving another. I only got there because I'd done it the slow way first, and learnt what good looked like.
<!-- src: store notes/interviews/build-the-thing/2026-11-27-learning-by-building-and-dan.md (Ant, 17:43: "We went from you giving me prompts to paste into Gemini, to you driving Gemini itself"); claude/jimmy-9.md ("Gemini in Ant's Chrome, Create image tool", 27 Nov 15:00); chapter 17, 17-07 (draft: using one AI to drive another). The last sentence is the drafter's: Ant to agree. New id 18-11 (after 18-04) -->

<!-- p: 18-05 | draft 2026-11-27 -->
Sometimes I build the tool before I've learnt the craft at all. The camera coaching app is meant to help me be a better photographer, and to act as an assistant on a shoot. I started building it before I owned a camera. I still don't. I'll pick up a Canon when I can. By then, the app will already know more about coaching than I do about photography, and I'll learn the craft with it.
<!-- src: Ant's notes on the camera app (Nov 2026: "Wants Togmatic to help him (and potentially others) be a better tog, and to work as a shoot assistant"; "Doesn't have a camera yet; wants to pick up a Canon when he can to get started"); r2jimmy decision togmatic-runs-build-live-coaching-2026-11-02 (night runs build new live coaching features every night). "I still don't" is as of 27 Nov: check before print. The last sentence is the drafter's: Ant to agree -->

<!-- p: 18-06 | draft 2026-11-27 -->
The same goes further out. We're training models of our own on my photos, which is a field I'd never have touched in my spare time, and chapter 26 says why. And a craft business I run is next in line for a website with a shop. That means learning how an online shop takes payments properly, which I've never had to know.
<!-- src: r2jimmy decision own-photo-models-2026-11-21; chapter 26, 26-09 (draft: why own photo models); Ant's notes on the craft business (Nov 2026: one of its first asks is a new website; an online shop on his Azure; would prefer Square for payments). Named only as "a craft business I run" (Ant, 27 Nov). The last sentence is the drafter's: Ant to agree -->

<!-- p: 18-07 | draft 2026-11-27 -->
Does it stick? I'm honestly not sure yet. I can ask for a closed skin and know what I'll get. I couldn't build one by hand. Maybe that doesn't matter. Most of what I learnt in my career, I learnt the same way, by needing it for a job. The difference is that the job used to have to be one I was paid for. Now it can be anything I'm curious about.
<!-- src: drafter's reading; chapter 1 (agreed: learning on the job across a career). The whole paragraph needs Ant's view: see q -->
<!-- q: SB-6 18-07: does learning this way stick for you? Is there something you've learnt through building with AI that you could now do yourself, without it? -->

<!-- p: 18-08 | draft 2026-11-27 -->
That's the ceiling again, from a different side. Every word I learn widens what I can ask for, and every new thing I can ask for is a new thing I can build. Nothing I learnt was wasted, even the parts that looked like messing about. All knowledge and experience have value. You just have to learn to recognise it. And some of the deepest learning comes from play.
<!-- src: store notes/interviews/build-the-thing/2026-11-27-learning-by-building-and-dan.md (Ant, 17:43: "All knowledge and experience have value, you just have to learn to recognise it, and seriously deep learning can come from play"); chapter 1 (agreed: "where is the ceiling, really?"). "Nothing I learnt was wasted, even the parts that looked like messing about" is the drafter's: Ant to agree. Watch for overlap with 26-12 -->

