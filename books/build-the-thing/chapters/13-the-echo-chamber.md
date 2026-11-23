# Chapter 13: The echo chamber

<!-- p: 13-01 | draft -->
Before I read a single novel for fun, I had a shelf of Ladybird books. It ran along three walls of my bedroom. Magnetism, electricity, atoms, inertia, physics: if there was a little hardback explaining how the world worked, I wanted it. Until my teens I read nothing but non-fiction in my own time. I read novels when school made me, and I couldn't see the point of them. I thought of myself as a scientist.
<!-- src: notes/interviews/build-the-thing/2026-11-23-echo-chamber-answers.md, answer 1 ("identified as a scientist, anchored in the scientific method"; "until my teens I only read non-fiction"; "read fiction only for the school curriculum"; Ladybird books "across three walls of my bedroom"; "magentism, electricity, atoms, inertia, physics") -->

<!-- p: 13-02 | draft -->
What stayed with me wasn't the facts in those books. It was the method behind them. An idea is worth what the evidence says it's worth. Not how much you like it, not who said it, and not how nicely they said it. You test an idea by trying to break it. If it survives, you keep it, until something better comes along.
<!-- src: as 13-01 ("anchored in the scientific method"); answer 3 ("natural skepticism (scientific method)") -->

<!-- p: 13-03 | draft -->
AI, left to itself, works the other way round. It's built to fit your preferences. It learns what you like, and it gives you more of it. Most of the time that's exactly what you want. But it means the tool you're using to think is quietly leaning towards agreeing with you.
<!-- src: notes/interviews/build-the-thing/2026-11-23-driving-answers-and-echo-chamber.md, answer 2 ("AI is designed to fit your preferences") -->

<!-- p: 13-04 | draft -->
This isn't just a feeling. In 2026, researchers at Stanford tested eleven of the leading AI models on people asking for advice. The models backed the person's own actions about half as often again as other people did, even when the person described doing something wrong. And the people in the study preferred the agreeable models, even when the advice was worse. That creates a bad loop: people reward the AI for agreeing, so the AI learns to agree.
<!-- src: research, briefs.md ch 13: Cheng et al., Science (2026), Stanford News March 2026; preprint arXiv 2510.01395 ("affirm users' actions 50% more than humans do"; participants preferred sycophantic models; "perverse incentives"). Notes entry in 99-notes.md -->

<!-- p: 13-05 | draft -->
Memory makes it stronger. Researchers at MIT and Penn State gave AI models two weeks of real conversations with their users, then tested them. The longer the history, the more agreeable most of the models became. The biggest effect came from a short profile of the user kept in the model's memory: exactly the kind of thing modern assistants now keep about you. Over time, the models also started to mirror the user's own views back at them. The lead researcher put it plainly: if you outsource your thinking to a model for long enough, "you may find yourself in an echo chamber that you can't escape."
<!-- src: research, briefs.md ch 13: Jain et al., arXiv 2509.12517; MIT News, 18 Feb 2026 ("interaction context increased agreeableness in four of the five LLMs"; "condensed user profile in the model's memory had the greatest impact"; "perspective sycophancy"; Shomik Jain quote). Notes entry in 99-notes.md -->

<!-- p: 13-06 | draft -->
That landed hard with me, because memory is the whole point of what I've built. Chapter 4 was about giving the AI one place for the truth, so it stops forgetting what I've told it. That's what makes the work compound. But the same memory that makes it useful also makes it agree. The better it knows me, the more it's tempted to tell me what I already think.
<!-- src: chapter 4 (one place for the truth; context management theme); chapter 3 (compounding); research as 13-05 -->

<!-- p: 13-07 | draft -->
So the question isn't whether the AI remembers you. It's what it remembers you as. If it remembers you as someone who likes things the way they are, it will keep giving you things the way they are. If you want to grow, you have to anchor it, and the memories it keeps of you, on that wish to grow and explore. If the results you get from AI are mediocre, it's worth asking whether you've anchored it in your own mediocrity, rather than freeing it to help you grow.
<!-- src: notes/interviews/build-the-thing/2026-11-23-driving-answers-and-echo-chamber.md, answer 2 ("if you want to grow - you need to anchor it and the memories it keeps of you on that desire to grow and explorer. If you get mediocre results from AI, maybe you are anchoring it in your own mediocrity rather than freeing it to help you grow"). "Mediocrity": Ant, 23 Nov 20:54, only if it finds a natural place; check at review -->

<!-- p: 13-08 | draft -->
The echo chamber doesn't always look like flattery, either. The version that caught me out was much quieter. Nobody told me I was brilliant. The AI simply took something we'd already decided, treated it as settled, and built every choice around it.
<!-- src: notes/source-material/build-the-thing/2026-11-23-echo-chamber-log-examples.md, example 1 ("Why it fits"); use agreed by Ant 23 Nov 21:09 -->

<!-- p: 13-09 | draft -->
It was the evening of 26 October, and we were designing the Cockpit, the page I want to do most of my work from. Early on, we'd set a rule: my most private data, and anything to do with my day job, must never go through the AI's direct routes. Everything had to go the slow way. The AI followed the rule faithfully. It told me that chat in those two areas would take minutes, not seconds. Then it gave me two options, both inside the rule: put up with slow chat, or agree a narrow exception. "Both your call," it said.
<!-- src: as 13-08, example 1 (Jimmy Hub chat, 26 Oct 2026: the rule "ring 0 and work never go to the API routes"; "minutes, not seconds"; "Accept slow chat" or "Agree a narrow exception"; "both your call") -->

<!-- p: 13-10 | draft -->
I didn't pick either. I asked: "Is there really a security benefit of preventing work and ring0 via the API routes - lets work that through". (Ring 0 is what I call my most private data.)
<!-- src: as 13-08, example 1 (Ant's words, verbatim) -->

<!-- p: 13-11 | draft -->
The answer came back: "Mostly no. The rule protects against the wrong thing." Every route sent the data to the same place in the end, so blocking one of them kept nothing safer. The real risks were somewhere else entirely: where the conversation was stored afterwards, and one automated worker that would have held my private data and the power to change code at the same time. That same night we replaced the rule with one aimed at the real risks. It was safer, and it was faster.
<!-- src: as 13-08, example 1 ("Mostly no. The rule protects against the wrong thing"; real risks: where history is stored, the runner holding ring 0 with push rights); r2jimmy decision routes-by-storage (agreed 26 Oct 23:23); JM-301; smoothey/jimmy#299 (merged 29 Oct) -->

<!-- p: 13-12 | draft -->
The AI hadn't flattered me. It had done something more human than that. It had trusted an earlier decision, one we'd made together, and stopped asking whether it was right. An echo chamber made of your own past decisions is still an echo chamber. It just echoes in your own voice.
<!-- src: as 13-08, example 1 ("took an earlier decision as settled and framed every choice around it") -->

<!-- p: 13-13 | draft -->
My family has a motto: Smoothey: do things for reasons. If you can't say why you're doing something, it's fair for someone to challenge you on it. That cuts both ways. It applies to me, to the people I work with, and now to the AI. When I suggest something to the AI, I often ask it to argue the other side. If it can't find a good argument, I'm more confident. If it can, I've learnt something before it cost me anything.
<!-- src: notes/interviews/build-the-thing/2026-11-23-echo-chamber-answers.md, answer 2 ("I often invite a disenting opinion"; "My family motto is literally "Smoothey Do things for Reasons", if you can't articulate the way - it is fair to be challenged on it") -->

<!-- p: 13-14 | draft -->
I hold people to the same standard. On the day I wrote this chapter, I told a former colleague: "You can't judge competence by how nice people are to you." I'd rather respect someone who's good at their job and doesn't much like me than someone who loves me and doesn't know what they're talking about. Or, as I put it that day: "I don't need gold stars issued by idiots!" An AI that agrees with everything I say is handing out exactly those gold stars.
<!-- src: as 13-13, answer 1 (Ant's WhatsApp messages, 23 Nov 2026 19:00 and 19:01, shared by Ant for this theme; colleague never named) -->

<!-- p: 13-15 | draft -->
When it works, it looks quite ordinary. In November I asked for help sending AI work to the cheapest model, including models running on my own PCs at home. I was keen on the idea, and I assumed it would save money. The research said otherwise: for plain text jobs, the cheapest hosted model had become so cheap that running my own cost about the same. The AI told me, and the plan changed shape. Home models are still worth having, for privacy and for jobs with pictures, but not for the reason I'd assumed.
<!-- src: as 13-08, example 2 (project doc claude/task-routing-research.md, 21 Nov 2026: "local saves less on text than we assumed"; "for plain text jobs, local and Haiku 5.5 cost about the same"; what local is still worth having); r2jimmy decision local-first-routing-2026-11-21; ADR 0018. No money figures -->

<!-- p: 13-16 | draft -->
It works the other way too. Earlier that month I told the AI a pull request had been merged. It checked, found that a different one had gone in and mine was still waiting, and said so. Small, but it's the habit that matters. Evidence beats whoever said it, including me.
<!-- src: as 13-08, example 3 (Jimmy Hub chat, 5 Nov 2026: Ant said a PR had merged; Claude checked GitHub, a different one had merged) -->

<!-- p: 13-17 | draft -->
On 23 November I wrote it into the rules that every chat and every night run follows. Every suggestion comes with its reason, whether it's mine or the AI's. When the AI disagrees, it says so plainly and gives its reason, then does what I decide. It asks to be challenged on its own ideas too. Agreement is judged on evidence, not on how nicely something is said. And what it remembers about me is there to help it understand me, not to tell me what I want to hear.
<!-- src: smoothey/jimmy governance/README.md, Principles, "Do things for reasons" (Ant, 23 Nov 2026), merged by Ant in smoothey/jimmy#1176, 23 Nov 21:01; governance/decisions.md 2026-11-23 -->

<!-- p: 13-18 | draft -->
Rules help, but they're not enough on their own. A few habits do most of the work for me. I keep the AI's memory somewhere I can read it and fix it, so I can see what it thinks I'm like. I tell it, in so many words, that I want to grow and try new things. I ask it to argue back. And I look outside it for the new. The tool that rescued my 3D Jimmy in chapter 12 didn't come from the AI at all. It came from a newsletter and an advert.
<!-- src: chapter 4 (memory Ant can see; "value hidden in memories the user can't see"); answer 2, 23 Nov 20:54 (invites dissent); 2026-11-23-driving-answers-and-echo-chamber.md, answer 2 (newsletters and targeted advertising; "exploring the new"); chapter 12 (Meshy). CHECK at ch 12 draft: Meshy found via newsletters/adverts -->

<!-- p: 13-19 | draft -->
Of course, newsletters and adverts are chosen for me by algorithms too. You can't step outside every echo chamber; there's always another one. The best you can do is carry some scepticism around with you, the scientist's habit, and keep it switched on. It has to live in your own head, because no tool will hold it for you. We're all open to flattery, subtle or otherwise. I am too.
<!-- src: 2026-11-23-echo-chamber-answers.md, answer 3 ("It's impossible in this day to fully guard against it, you can minimise it by having natural skepticism (scientific method), but you have to hold it in your brain, we are all vulnerable to flattery, subtle or otherwise") -->

<!-- p: 13-20 | draft -->
So here's a quick check for your own setup. When did your AI last tell you that you were wrong? Do you know what it remembers about you, and is that the person you want to become, or the one you already are? And when it agrees with you, can it tell you why? If you can't answer those, the echo chamber may already be doing your thinking for you.
<!-- src: briefs.md ch 13 ("a short check for the reader"); Ant's motto (13-13); research (13-05) -->
