# Chapter 16: Risk, measure and boldness

<!--
First draft, 27 Nov 2026 (Ant's pick from the content brainstorm, 17:25). Source: store r2antbooks notes/interviews/build-the-thing/2026-11-23-parked-risk-and-why-not.md. Use Ant's own words only. Dan's words and his "why not?" idea are Dan's and need his say-so: not used. Anything about Dan stays out. Previous-job and client detail never named.
ADHD and autism: Ant is open about both for this book, sparingly (27 Nov 17:25: "Both, sparingly"). ADHD is named here because it explains how he handles risk.
-->

<!-- p: 16-01 | draft 2026-11-27 -->
I should say something about myself before this chapter goes any further. I have ADHD, and I'm autistic. The ADHD means I'm at times under-cautious. When I tell someone to just go ahead with a change, it's calculated, and it's considered. But my natural setting leans towards doing it, not waiting. That matters in a book about going faster, so it's fair you know it.
<!-- src: parked note (Ant, 23 Nov: "It was calculated but also considered, I am at times under-cautious - it comes from my ADHD - but I am also Autistic"; 22:08: "For this book I'm open about ADHD and autism"); content brainstorm, Ant's picks (27 Nov 17:25: "Both, sparingly"). The last sentence is the drafter's: Ant to agree. Check the book doesn't name ADHD and autism for the first time anywhere else first -->

<!-- p: 16-02 | draft 2026-11-27 -->
In my working life, risk has always been part of the job. As consultants, we're often chosen precisely because our appetite for risk is different from the people who commission us. It can be different in either direction. A gung-ho client needs measure. An over-cautious one benefits from boldness. Part of being good at the job is reading which one is in front of you.
<!-- src: parked note (Ant: "As consultants we are often chosen to have a different (in either direction) risk profile to the people commissioning us"; "A gung ho client, needs measure, an overcautious one benefits from boldness"). The last sentence is the drafter's: Ant to agree -->

<!-- p: 16-03 | draft 2026-11-27 -->
Most of the time, though, a client is handing you their risk. That's what they're paying for. We learn from what goes wrong, even if we sometimes get hauled over the coals for it. The good consultants can turn that round, and help the client see the value of learning from it together.
<!-- src: parked note (Ant: "But most commonly clients are outsourcing risk, but as consultants we learn (even if we are hauled over the coals sometimes) from what goes wrong, but good consultants can navigate that and make the client see the value of the joint learning") -->

<!-- p: 16-10 | draft 2026-11-27 -->
Dan, the former colleague from chapter 13, put the other half of it neatly. Rather than asking why, ask why not. His example was a sensible safeguard applied everywhere by default. If everything else is right, it does very little. But give me a reason you wouldn't. It's the mirror of my family's motto in chapter 13. "Do things for reasons" asks for a reason to act. "Why not?" asks for a reason not to. Between them, they catch both kinds of risk: doing something you shouldn't, and not doing something you should.
<!-- src: store notes/interviews/build-the-thing/2026-11-23-parked-risk-and-why-not.md (Dan's words: "Rather than asking why, ask why not"; his example: "a sensible default control applied everywhere; it does little if everything else is right, 'but give me a reason you wouldn't'"); store notes/interviews/build-the-thing/2026-11-27-learning-by-building-and-dan.md (Ant, 27 Nov 17:47: "Yes at why not": Dan agreed to its use); chapter 13 (agreed: "Smootheys do things for reasons").  Named in ch 13, 13-14 (Ant, 27 Nov 17:48). The last sentence is the drafter's. New id 16-10 (after 16-03) -->

<!-- p: 16-04 | draft 2026-11-27 -->
With Jimmy, I'm the client, and the AI is the consultant. So which way does it lean? Mostly towards the middle. Its safety checks are firm, as chapter 14 showed. Its estimates are cautious: it plans as though a human team were doing the work, until it's shown its own pace. Asked to choose between three options, it tends to recommend the middle one. None of that is wrong. But it means the measure and the boldness both have to come from me, and I have to know which the moment needs.
<!-- src: chapter 14 (draft: the safety check); chapter 3 (agreed: the borrowed pace, AI plans in human-team time); chapter 19 (draft: screenshot checks, the AI recommended the middle option); store 2026-11-27-screenshot-checks.md. "Mostly towards the middle" is the drafter's reading: Ant to agree -->

<!-- p: 16-05 | draft 2026-11-27 -->
Sometimes the moment needs boldness. Before Charlie's site was revealed, I decided its changes would go straight to the live site, every night, right up to a freeze before the big day. No waiting on a test copy. And I set a standing rule for every freeze since: if something can be done before the freeze at the pace we're going, it should be. Doing it after needs evidence. I was tired of being asked "before or after?" every time.
<!-- src: r2jimmy decisions build-to-live-until-freeze (22 Oct: "Charlie Doll: build straight to live until the look freeze (31 Oct)") and freeze-default-before (24 Oct: "Before the freeze by default; after a freeze needs evidence (all freezes)"); Ant, 25 Oct (standing rule for all freezes; "tired of being asked 'before or after the freeze'") -->

<!-- p: 16-06 | draft 2026-11-27 -->
Sometimes it needs measure. Chapter 14 told why I still hold some access back, even though it slows me down, and why night work goes to a pull request I merge myself. The keys to money, merges and my own Azure stay with me. Those are the places where a mistake is hard to take back, and where my own boldness is the thing I'd least want to rely on.
<!-- src: chapter 14 (draft: holding back on access; night work goes to a pull request); chapter 8 (agreed: brokers for merges, spend and infrastructure). The last clause is the drafter's: Ant to agree -->

<!-- p: 16-07 | draft 2026-11-27 -->
That's the part I find most useful. Knowing I'm at times under-cautious, I don't have to rely on catching myself in the moment. I can build the measure into the system, once, while I'm thinking clearly. A broker that asks for my face before a risky merge. A never list. A rule that a run doesn't put anything live on its own. The system supplies the caution on the nights I'd skip it.
<!-- src: chapter 8 (agreed: brokers, Face ID for the riskiest merges); chapter 9 (draft: never lists); chapter 14 (draft: a run doesn't push to main). Drafter's synthesis: Ant to agree it's how he sees it -->

<!-- p: 16-08 | draft 2026-11-27 -->
And when something does go wrong, it gets written down. Chapter 10 is about why writing it down isn't enough on its own. But it's where the joint learning starts: the AI and I both know what happened, and the next run reads it before it begins.
<!-- src: chapter 10 (draft: logging a lesson isn't learning it); parked note ("joint learning"); r2jimmy lesson records -->

<!-- p: 16-09 | draft 2026-11-27 -->
[A time boldness paid off, and a time measure saved you, in your words.]
<!-- q: SB-6 16-09: one example of each from the Jimmy work: a bold call that paid off, and a time holding back saved you -->
