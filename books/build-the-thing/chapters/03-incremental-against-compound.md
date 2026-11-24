# Chapter 3: Incremental against compound

<!-- p: 03-01 | agreed 2026-11-22 -->
There are two ways to get more done. You can add: more hours, more effort, more evenings. Or you can multiply: build things that keep working after you've stopped. For more than twenty years I mostly added. This chapter is about the difference, and why it matters more now than it ever has.
<!-- src: book thesis (Ant, 21 Nov 2026, title and outline); chapter 1, 01-06 and 01-10 (agreed) -->
<!-- rev: 'more than twenty years' (from Brussels, 2000); agreed by Ant 22 Nov 17:25 -->

<!-- p: 03-02 | agreed 2026-11-22 -->
Adding works, up to a point. Every tool I built in my own time saved hours once it existed. But much of what it saved, I'd already paid for in an evening or a weekend, and every change it needed came out of the same evenings. My progress grew in a straight line at best, and the line could never climb higher than the hours I had. That's what incremental means. It isn't slow. It's capped.
<!-- src: notes/interviews/build-the-thing/2026-11-22-career-and-own-time.md ("burning my personal time"; "still helped free up time, but at a personal cost"); chapter 1, 01-06 (agreed) -->
<!-- rev: 'much of what it saved'; agreed by Ant 22 Nov 17:26 -->

<!-- p: 03-03 | agreed 2026-11-22 -->
Compounding works differently. Some things you make keep paying out, and each one makes the next one easier to build. A rule, written down once, applies to every piece of work from then on. A tool, built once, gets used every night. A record of what happened, kept once, means nobody has to rediscover it. When I write a rule into Jimmy today, it applies to every project tonight, without me doing anything else.
<!-- src: outline ch 3 ("what compounds: rules, tools, records"); r2jimmy decision sizing-night-share (20 Oct 2026: agreed 11:50, governance merged 13:05, "live for tonight's runs", applies to every project) -->
<!-- rev: 'easier to build', 'into Jimmy'; agreed by Ant 22 Nov 17:27 -->

<!-- p: 03-04 | agreed 2026-11-22 -->
Here's a real example. On the morning of 20 October I agreed a new way of sizing work, which I'll come to later in this chapter. By lunchtime it was written into the rules, and that night every project used it. One decision, made once, changed how five projects planned their work, and it has kept doing so every night since.
<!-- src: r2jimmy decision sizing-night-share (decided 11:50, governance merged 13:05 on 20 Oct 2026; appliesTo: r2poseroll, r2jimmy, r2photoorganiser, r2transcenders, r2robroblox, w2aaah once live) -->
<!-- rev: 'five' (sixth, w2aaah, was 'once live'); agreed by Ant 22 Nov 17:27 -->

<!-- p: 03-05 | agreed 2026-11-22 -->
Effort doesn't compound. An evening spent fixing something by hand is gone once it's spent. It might help, but tomorrow starts from the same place. I've had one principle since I wrote my first scripts: it isn't enough for something to fix the problem in front of me. It should stop the problem coming back.
<!-- src: Ant, 22 Nov 17:34 ("not just asking myself if something fixes the issue, it's whether it prevents future issues too"; principle "right back to when I first made scripts"); agreed by Ant 22 Nov 17:36 -->

<!-- p: 03-05b | agreed 2026-11-22 -->
At the financial sector company, a whole team of developers built our business systems in a language called Jade. The software kept falling over at night, and I was asked to help soften the impact. I pushed back. The developers should stop it crashing in the first place. But to help in the meantime, I built a VBScript tool that watched the network connections the software used, and restarted it if they dropped. I was clear that it wasn't a fix. It was a stopgap, until they fixed the cause.
<!-- src: Ant, 22 Nov 17:34 (Jade business systems falling over at night; pushed back; VBScript tool monitoring the ports, restarting the app; "it wasn't a fix, it was a stopgap"); employer not named; agreed by Ant 22 Nov 17:36 -->

<!-- p: 03-05c | agreed 2026-11-22 -->
Three years after I'd left, I was back there as a consultant on some unrelated work. My temporary fix was still running. The crash had never been fixed. The stopgap had worked so well that the pain went away, and with it, the reason to fix the cause. It was the right instinct to build something that kept working without me. I'd just built it on the wrong side of the problem.
<!-- src: Ant, 22 Nov 17:34 (three years after leaving, contracted as a consultant for unrelated work; "temporary fix" still running; devs never fixed the source); closing reading by Claude, agreed by Ant 22 Nov 17:36 -->

<!-- p: 03-06 | agreed 2026-11-24 -->
There's a second idea behind all this: comparative advantage, from chapter 1. Picture a lawyer who types faster than her assistant. She still shouldn't do her own typing, because every hour she spends typing is an hour she isn't doing the work only she can do. Being best at something doesn't mean it's the best use of your time.
<!-- src: chapter 1, 01-24 (agreed); r2antbooks notes/interviews/build-the-thing/2026-11-22-early-years-and-game-theory.md (comparative advantage, Ant 00:11 to 00:13); the lawyer and typist is the standard textbook illustration, not Ant's own story -->
<!-- rev: new bridge after the Jade story; agreed by Ant 22 Nov 17:38 -->

<!-- p: 03-07 | agreed 2026-11-22 -->
For most of my career, I was the lawyer who did his own typing. Among the people I worked with I was usually the best developer, so writing the code myself felt like the obvious thing to do. Once AI could write code faster than me, that changed completely. In the world after AI, I add far more through vision, architecture and design than I ever did by typing code.
<!-- src: notes/interviews/build-the-thing/2026-11-22-early-years-and-game-theory.md ("among his peers he has mostly been the best developer"; "in the post-AI world he adds much more in vision, architecture and design"; direction, critical review, process design, reviewing PRs); chapter 2, 02-14 (agreed) -->
<!-- rev: ending in Ant's interview words (avoids repeating 02-14); agreed by Ant 22 Nov 17:39 -->

<!-- p: 03-08 | agreed 2026-11-22 -->
Most of my hands-on time now goes on checking what comes back, and that turns out to be quick. When we agreed how to measure my own time, we counted about five minutes to review and accept each piece of finished work. The AI does hours of building; I do minutes of checking. That's comparative advantage in practice, and it's also where the compounding comes from. The more the system can do without me, the more of my minutes go on the decisions that change what it does next.
<!-- src: r2jimmy decision sizing-night-share (antTime "includes reviewing and merging (about 5 min a PR)") -->
<!-- rev: bridge added, 'review and accept'; agreed by Ant 22 Nov 17:40 -->

<!-- p: 03-09 | agreed 2026-11-22 -->
There was one thing slowing all of this down, and it took me a while to see it. The AI kept planning my work as if a team of people were doing it. It sized tasks as small, medium and large, and planned in sprints: set batches of work that a team would usually expect to take a week or two. On Charlie's site, those sprints were getting done in hours, whether we worked through them together or the runs did them overnight. Before each freeze on releases, the AI would start worrying days in advance that we wouldn't have enough time. I knew from what we'd already done that we would. When we worked through things together, we smashed through the work in hours. It isn't unusual for me to get through three sprints on one project in an afternoon, while other projects in the portfolio carry on at the same time. I found myself challenging its sense of time again and again.
<!-- src: notes/interviews/build-the-thing/2026-11-21-theme-pace-anchoring.md ("AI's answers often assumed a rate of progress anchored to a human team. He has constantly had to challenge that"); r2jimmy decision sizing-night-share (replaced S/M/L sizes); introduction, 00-05 (agreed). SETTLED (paragraph agreed by Ant 22 Nov; was NEEDS ANT): "a fortnight of work it could finish in a night" is illustrative; confirm or give a real case -->
<!-- rev: rewritten from Ant 22 Nov 17:44 (Charlie Doll sprints in hours, interactive and overnight; freeze worries days ahead; 3 sprints in an afternoon alongside other projects); sprint explained; agreed by Ant 22 Nov 17:46 -->

<!-- p: 03-10 | agreed 2026-11-22 -->
So on 20 October we stopped borrowing a pace and made our own. We decided to size every piece of work as a share of a night: a sixteenth, an eighth, a quarter, a half, or a whole night. Anything bigger gets split before it's planned. A "night" isn't a time of day. It's a unit of building effort, so work done in a daytime chat counts in the same units. My own time is counted separately, in minutes, because it's the thing in shortest supply.
<!-- src: r2jimmy decision sizing-night-share (20 Oct 2026: nightShare 0, 1/16, 1/8, 1/4, 1/2, 1; split anything over one night; "a night is a unit of Claude build effort, not a time of day: daytime chat work counts in the same units"; antTime in minutes) -->
<!-- rev: agreed by Ant 22 Nov 17:47 -->

<!-- p: 03-11 | agreed 2026-11-22 -->
Then we measured. Each night has eight hours of building time, 480 minutes. On the nights of 20 and 21 October, the runs used only about 274 and 255 of them. Nothing had run out of time. The runs had simply run out of work. Some projects emptied their lists; others hit a limit on how many changes they could put live in one go. The AI had planned for the pace it expected, and the real pace was faster.
<!-- src: r2jimmy decision night-utilisation (22 Oct 2026: "The nights of 20 and 21 Oct used about 274 and 255 of 480 minutes; runs stopped on empty queues ... or push caps, never on time"); decision night-load (22 Oct 2026, evidence) -->
<!-- rev: agreed by Ant 22 Nov 17:48 (as is) -->

<!-- p: 03-12 | agreed 2026-11-22 -->
So we changed the plan to match the evidence. On 22 October we started planning each night at about twice what we expected it to take. Runs that finish early now pull in more work by themselves, from items that are safe to do without me. And the morning brief now tells me how many of the 480 minutes were used, and warns me if a night used less than three quarters of them. An idle night became something I could see, and something we could fix.
<!-- src: r2jimmy decision night-load (22 Oct 2026: "Nights planned at about 2x nightShare; runs keep taking next items until a stop rule"); decision night-utilisation (22 Oct 2026: self-promote up to 6 of its own ideas, unattended yes only; "Morning brief reports minutes used of 480 and flags a night under 75%") -->
<!-- rev: agreed by Ant 22 Nov 17:49 -->

<!-- p: 03-13 | agreed 2026-11-22 -->
I said at the start that my guess is the AI learned its sense of time from writing made before AI. There may be more to it. It may play safe and pad its estimates, and it can't know its own speed until someone measures it. Either way, the most expensive limit is the one you don't notice you've accepted.
<!-- src: notes/interviews/build-the-thing/2026-11-21-theme-pace-anchoring.md (Ant's guess: anchored to training material from before AI; Claude's offered causes: caution, no view of its own throughput). SETTLED (paragraph agreed by Ant 22 Nov; was NEEDS ANT): the two extra causes were Claude's suggestion; keep only if Ant agrees -->
<!-- rev: shorter, nods to 00-05; Claude's two extra causes accepted by Ant 22 Nov 17:50 -->

<!-- p: 03-14 | agreed 2026-11-22 -->
Here's what the difference looked like for me. Before mid September, my side projects moved only when I had an evening free: one main tool, kept going by hand, and a list of features that never got shorter. By the third week of November, six of my project repositories had saved around 4,000 changes between them in eight weeks, and that doesn't count Jimmy itself or the game. In the week to 22 November alone there were about 900 changes, and around 240 pieces of finished work reviewed and accepted. The busiest single day, 18 November, saw 255. These are my results, not a target. What matters isn't the number. It's that the number kept rising while my own hours didn't.
<!-- src: git history of smoothey/ultimatetranscender, poseroll, photo-organiser, togmatic, ut-corpus, antbooks (all branches, counted 22 Nov 2026 17:53 UTC: 4,054 commits from 30 Sep to 22 Nov; week 16 to 22 Nov 889 to 929 depending on date used; ~242 merged pull requests that week; 255 commits on 18 Nov); smoothey/jimmy and the Roblox repo not counted; "before" from chapter 1 (01-06, agreed) and interview 1. -->
<!-- rev: numbers from git history 22 Nov; 'my own hours didn't' confirmed by Ant 22 Nov 17:55; re-count before publish (SB-4) -->

<!-- p: 03-15 | agreed 2026-11-22 -->
That's the whole difference. Incremental is adding hours to the work. Compound is adding things that add to the work: rules, tools, records, and a pace you've measured rather than borrowed. The first is capped by how much of yourself you can give. The second isn't, because each thing you add keeps working while you're asleep, as long as you've built it on the right side of the problem. The rest of this book is about the things I added, starting with the first one, the one everything else stands on: one place for the truth.
<!-- src: outline ch 3 and ch 4 ("One place for the truth"); book thesis -->
<!-- rev: Jade callback added; 'The second isn't' kept; agreed by Ant 22 Nov 17:51 -->

