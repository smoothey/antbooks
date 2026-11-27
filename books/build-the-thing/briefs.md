# Build the Thing That Builds the Things: chapter briefs (22 Nov 2026, updated 23 Nov; chapters 12 and 13 added, later chapters renumbered; 27 Nov: chapter 15 added, later chapters renumbered 16 to 22)

One brief per chapter: its job, what earlier chapters have already set up (agreed text only), what we already know, and the gaps to fill. Updated after chapter 1 was agreed. Briefs change as the book develops (PROCESS.md, step 2).

Sources live in the store (`r2antbooks` `notes/interviews/build-the-thing/`, `notes/source-material/build-the-thing/`) and in `smoothey/jimmy` and `r2jimmy`. Themes noted so far: borrowed pace; comparative advantage; context management; delegation through frameworks; holding back on access (a deliberate counterpoint to the speed story, Ant 22 Nov 02:26); driving AI or being led by it (Ant 23 Nov 20:05, case study 3D Jimmy); the AI echo chamber (Ant 23 Nov 20:14).

## Parked context (not tied to a chapter; don't force it)
- Theme (Ant, 24 Nov 08:21): "changing the methodology can (and should) change the metric". Already in print in ch 3 (weeks and sprints replaced by a share of a night) and ch 5 (minutes used out of 480); main story in ch 12 (3D Jimmy). **A thread, not a chapter (Ant, 24 Nov 08:22):** named in ch 12, pointing back to ch 3 and ch 5, picked up in the closing chapter. Store: `notes/interviews/build-the-thing/2026-11-24-theme-method-changes-metric.md`.
- Content idea (Ant, 24 Nov 12:06): "different ways of working with AI - loops, 'interview me' etc". A menu of working patterns, each with when to use it and where the book shows it: loops (ch 5), interview me (this book), a paragraph at a time with a sliding window (this book), a separate reviewer (ch 1 polish, independent reviews before merges), walk me through and "what needs my attention" (ch 2, 7), chats leaving each other messages (ch 4), research then propose (the word-count research), ask it to challenge you (ch 12, 13). Placement not yet agreed. Store: `notes/interviews/build-the-thing/2026-11-24-ways-of-working.md`.
- Credits: Ant has invited Dan Redmond to be credited in the book (23 Nov 22:23). Unnamed in the prose for now (13-14). Add to the acknowledgements once Dan answers.
- Risk appetite and "why not?" (Ant, 23 Nov 22:07): consultants are often chosen for a different risk profile from the client, in either direction; measure for a gung-ho client, boldness for an over-cautious one; joint learning from what goes wrong. Dan R's "rather than asking why, ask why not" is his idea and needs his say-so. Store: `notes/interviews/build-the-thing/2026-11-23-parked-risk-and-why-not.md`. Possible homes: ch 12, 13, 14, 16, 10.
- Ant is open about ADHD and autism for this book (Ant, 23 Nov 22:08). Name them where they add something; don't force it.

## Introduction (drafted, not yet reviewed)
- Job: the promise of the book in under 1,000 words.
- Check at review: 00-02 says "two books a week". Keep it as one example among several, so readers don't anchor on it (Ant, 22 Nov).
- Check at review: it repeats chapter 1's question ("where is the ceiling, really?"). Decide whether the intro asks it and chapter 1 answers it, or the intro leads with a different hook.
- Now says mid September (fixed 22 Nov). Its list of themes should add comparative advantage and context.

## 1. Doing the work, and the ceiling it hits (agreed 22 Nov, about 2,120 words)
- Sets up, for later chapters to pay off:
  - "I didn't know it yet, but that was the idea behind everything that came later" (the firewall procedure plus memory) → ch 2.
  - Comparative advantage, named at sixteen, "decades and a very different kind of tool" before he understood it → ch 3.
  - "The best use of my hours was building the thing that saved them" → ch 2 and ch 3.
  - Drive Image Pro picked because it could be scripted → ch 21.
  - Building a CMDB from need before knowing ITIL → ch 11.
  - Ophelia: a framework let a non-programmer contribute, but the last step always waited on Ant → ch 9 and ch 22.
  - The personal-time cost of building tools in the evenings → ch 3 and ch 16.
  - "Before long I wasn't building a website. I was building the thing that would build it." → ch 2 opens here.
- Don't retell in later chapters: the Commodore, the shops, Input, bridge, Brussels, the vibe-coded team tool. Refer back in a line at most.
- From the polish review (22 Nov): "where is the ceiling, really?" is used in the intro and 01-16, so not a third time early on; "building the thing that builds/saves" appears three times before ch 2, so watch overuse; AzureDump's feature list "didn't get shorter", so a later chapter should say whether it finally did; "loop" needs a glossary entry; keep each telling of the tiny-tasks pace distinct (ch 1, intro, ch 3, ch 11).

## 2. Build the thing that builds the things
- Job: the idea in one chapter, and the first night it worked.
- Known: Charlie's site came first (mid September to October); the store started as memory so the AI could see what Ant had told it; almost at once it became a server chats could reach; then interface rules (from Apple's guidelines), then governance, then Jimmy. Nobody designed it up front. The persona: cute and capable, because chatbots had been woeful. The firewall work as the pattern (procedure plus memory), now told in full from the client notes. Store went live 18 to 19 Oct.
- Turn: it's pointless for Ant to write code (comparative advantage in action, ch 3 names the cost and benefit).
- Must bridge mid September (the challenge and Charlie's present, end of ch 1) to 18 Oct (the store and the first nights).
- Gaps (ask Ant): what was the first night something finished while he slept, and how did that feel? When did the website stop being the point? When did work on Charlie's site start?

## 3. Incremental against compound
- Job: why building the system beats working harder.
- Known: comparative advantage (Ricardo, 1817): from best developer to vision, architecture and design. The borrowed pace: AI planned in human-team time until they measured their own; share of a night; utilisation metrics added 21 Nov. The personal-time cost from ch 1 is the incremental side.
- Gaps: before-and-after numbers (SB-4): books a week, pull requests and lines a week, Ant's own minutes a day. Unit counts only, no money. Present them as Ant's results, not targets: readers shouldn't anchor on any one number (Ant, 22 Nov).

## 4. One place for the truth
- Job: the store and the Hub, and why context is everything.
- Known: ADR 0002 and 0003; "is it stupid, or just missing context?"; value hidden in memories the user can't see; the client notes ("memory is what made it compound").
- Gaps: one concrete story of a "stupid" answer that turned out to be missing context, and how it was fixed.

## 5. Work while you sleep
- Job: how the nights work.
- Known: decisions overnight-cycles, night-load, night-utilisation, night-fill-rules, sizing-night-share; shifts and budgets.
- Gaps: few. Pull the figures from the run reports.

## 6. A night in the life
- Job: one real night, hour by hour.
- Known: run reports and morning briefs for every night since 18 Oct.
- Gaps: pick the night. Options: the night of 4 Nov (stalls, Ant tapping approvals at about 1:47 and 1:59), or a recent clean night to show it working. Possibly both, as contrast.

## 7. Only real asks reach you
- **All 12 paragraphs agreed** (23 Nov, 22:52 to 23:07), about 1,020 words. At polish: make "To agree" and "To discuss" match in case; check the photo organiser's name across chapters; 07-12 echoes 02-16 (watch overuse).
- Job: Needs you, Agree, away mode, the phone test.
- Known: decisions asks-need-ant-and-agree, agree-or-discuss, away-mode, away-is-reduced-access (about 2 hours a day, not a freeze).
- Gaps: what it was like running everything from a phone while away (1 to 13 Nov), if Ant wants that in.

## 8. Rings and brokers
- **All 13 paragraphs agreed** (23 Nov 23:31 to 24 Nov 00:26), about 1,160 words. Keep current before publishing: 08-09 says the cloud broker isn't switched on yet (JM-239, due 27 Nov). 08-13 commits ch 14 to explaining why Ant keeps the friction.
- Job: privacy by where data lives; approvals for merges, spend and infrastructure.
- Known: ADR 0003, 0009, 0010, 0014. Little Ant input needed.
- Holding back on access: approvals and rings are the mechanics of the restraint ch 14 explains. Link forward to it.

## 9. The people around you
- Job: what never goes in, building for people you care about, and keeping their stories theirs.
- Known: never lists; rings; Charlie happy to be in the book; the delegation theme (Ophelia then, Charlie's site admin with Jimmy now); this book's own consent checks (Charlie, Ant's mother, his wife-to-be, a former partner's detail left out).
- Gaps: needs a short interview (SB-6). Robyn only as Ant chooses.

## 10. Logging a lesson isn't learning it
- Job: why lessons repeat, and what makes one stick.
- Known: the one-off reminder lesson, logged seven times (19 Oct to 21 Nov); on the client work, banked gotchas did stop repeats; context theme (a lesson only helps if it reaches the next run).
- Gaps: Ant's view on why one stuck and the other didn't.

## 11. Best practice by accident
- Ch 8, 08-12 (agreed 24 Nov) already names separation of duties as arrived at, not copied. Refer back to it here; don't retell.
- Job: arriving at known good practice without setting out to.
- Known: "we'd be slower if we started with them"; Jimmy ended up like Azure DevOps without aiming to; the formal tiny-tasks team (ch 1) as contrast; the CMDB before ITIL (ch 1); pull before building; scripts split so a crash lands in the safe half; user stories after the fact.
- Also (22 Nov): the Jade stopgap from ch 3 (03-05b, 03-05c): fixing the cause, not the symptom, is what IT calls problem management. Ant was doing it before he knew the name. Refer back, don't retell.
- Gaps: few.

## 12. Driving, or being driven? (Ant's theme, 23 Nov 2026; added to the outline 23 Nov)
- Ant's words (23 Nov, 20:05): "are you driving AI or is it leading you", with the 3D Jimmy evening as the case study.
- Home: Part 3, ch 12, before the echo chamber (ch 13) and "When the machine says no" (now ch 14). Ant, 23 Nov 20:54: chapters have been coming in under length, so there's room; don't pad or shrink others to fit.
- Job: how to tell whether you're steering the AI or following it, told through one evening's work on [JM-491](https://hub.smoothey.co.uk/dashboard#ref/JM-491) (3D Jimmy).
- Story beats: the AI picks the first method and judges it by what it can count (40 bones, 48 moves), and the result "still looks a little cursed"; Ant sets one test anyone can apply (could you take a still for the drawing at a glance?); Ant picks the route (build from his own layers); short steers on taste (deeper sockets, the "chubster", the ears); a rule only he knew (paw down unless waving); a second AI tool keeps redrawing him in its own idea of cute until it's given his own drawing to continue; Ant goes and tries a different tool himself; the AI gives an honest side-by-side and a plan that keeps the best of both.
- Message (draft): driving isn't doing the work. It's owning the goal and the taste, and noticing when the tool's defaults have quietly become yours.
- Pays off: comparative advantage (ch 3: value moves to vision and design); what stays a human's job (ch 14: direction). Sets up ch 21 (the right tool for each job).
- Sources: store `r2antbooks` `notes/source-material/build-the-thing/2026-11-23-3d-jimmy-evening.md` and theme note; [smoothey/jimmy#1174](https://github.com/smoothey/jimmy/pull/1174), [#1175](https://github.com/smoothey/jimmy/pull/1175).
- Answered (Ant, 23 Nov 20:14): "cursed" is perfect, and "burn it with fire" sprang to mind too; both can go in. Why he tried Meshy himself: AI newsletters and adverts, and his ceiling-finding habit of exploring the new rather than relying on what has worked (leads into the echo chamber chapter below). His rule of thumb: "other people's bullshit is dangerous, believing your own is deadly" (his challenge mindset). The ending waits for the Meshy outcome.
- Still open: a picture of version 1, version 2 and the drawing side by side?
- New angle (Ant, 24 Nov 00:14): "changing the methodology can change the metric - the original goal may not have been phrased fully." The first ask didn't say "could pass for the drawing"; that test only appeared once version 1 was seen. So version 1 being judged by bones and moves was partly the goal as first phrased, not only the AI leading. Store: `notes/interviews/build-the-thing/2026-11-24-theme-method-changes-metric.md`.
- Sources (answers): store `notes/interviews/build-the-thing/2026-11-23-driving-answers-and-echo-chamber.md`.

- Figure idea (Ant, 24 Nov 16:15): side by side, 3D Jimmy made with Fable only against Meshy plus Fable. Both are still being worked on, so capture them as late as possible (by the files and proof step, SB-12) for the most impressive versions. Plan in figures/README.md as fig12-3d-jimmy-two-routes.
## 13. The echo chamber
- Circle back (Ant, 24 Nov 13:23): 13-09 and 13-10 never explain "direct routes", "API routes" (in Ant's quote) or "the slow way". Work through it with Ant. (Ant's theme, 23 Nov 2026, 20:14; added to the outline 23 Nov)
- **All 20 paragraphs agreed** (23 Nov, 21:51 to 22:37), about 1,500 words. Next: the polish pass (a separate reviewer; wording only, agreed in bulk). Checks at review: "mediocrity" in 13-07 (kept, Ant 21:57); 13-18 says Meshy came from a newsletter and an advert and that it "rescued" 3D Jimmy (agreed by Ant 22:34; ch 12 must match).
- Ant's words: "AI is designed to fit your preferences. If you want to grow, you need to anchor it, and the memories it keeps of you, on that desire to grow and explore. If you get mediocre results from AI, maybe you are anchoring it in your own mediocrity rather than freeing it to help you grow. The AI echo chamber can be dangerous." (lightly tidied; exact words in the store)
- Home: Part 3, ch 13, straight after "Driving, or being driven?". The driving chapter is one evening; this one is the slow version of the same risk, over weeks of memory.
- Job: AI tends to agree with you, and memory makes it agree more. Show how that quietly caps you, and how to set it up so it pushes you instead.
- Research so far (check and cite at draft time, in `99-notes.md`):
  - Stanford study in Science (2026): across 11 leading models, AI affirmed users' actions about 50% more often than people did, and users preferred the agreeable models even when the advice was worse. Cheng et al.; preprint arXiv 2510.01395; Stanford News, March 2026.
  - MIT and Penn State (Feb 2026): long conversations and stored user profiles made four of five models more agreeable; a condensed user profile in memory had the biggest effect. They call the mirroring of a user's views "perspective sycophancy". Jain et al.; arXiv 2509.12517; MIT News, 18 Feb 2026.
  - Columbia Journalism Review, Tow Center (9 Apr 2026): a chatbot's memory of you can shape the information you see; users have less control over what's stored than promised.
  - "The Algorithmic Self-Portrait" (ACM Web Conference 2026): memory as a portrait of you that you didn't draw. arXiv 2602.01450.
- Ant's own material to draw on: the ceiling (ch 1); the anchoring caution (ch 3, ch 20), turned round: here the reader anchors the AI; Meshy found through newsletters and adverts, not through the AI; "challenge goes both ways" and Agree-or-discuss (ch 7, ch 14); the store as memory Ant can see and edit (ch 4: "value hidden in memories the user can't see"); Gemini redrawing Jimmy in its own idea of cute until given Ant's drawing (the driving chapter).
- Possible shape: what the research says; how it shows up day to day (it agrees, it remembers you as you were, it suggests what worked last time); what Ant does about it (memory he can read and edit; telling it he wants to grow; asking it to argue back; looking outside it for the new); a short check for the reader.
- Answered (Ant, 23 Nov 20:54; store `2026-11-23-echo-chamber-answers.md`):
  - Scientist first: anchored in the scientific method; read only non-fiction in his own time as a boy; a shelf of Ladybird science books across three walls of his bedroom (magnetism, electricity, atoms, inertia). New material, not in ch 1.
  - His own line, to an ex-colleague the same day: you can't judge competence by how nice people are to you; "I don't need gold stars issued by idiots!" (the colleague is Dan Redmond, a peer; unnamed until Ant decides and Dan agrees). The human version of the sycophancy research.
  - He invites a dissenting opinion when he suggests something. Family motto: "Smootheys do things for reasons"; if you can't say why, it's fair to be challenged. Codified that evening as a governance principle: [smoothey/jimmy#1176](https://github.com/smoothey/jimmy/pull/1176).
  - His own feeds: you can't fully guard against it; you minimise it with natural scepticism, which you have to carry in your head. "We are all vulnerable to flattery, subtle or otherwise."
  - "Mediocrity": only if it finds a natural place.
- Found in the logs (23 Nov, store `notes/source-material/build-the-thing/2026-11-23-echo-chamber-log-examples.md`; agreed by Ant 23 Nov 21:09 as the lead example, with the two counter-examples used briefly):
  - Main: 26 Oct, the rule nobody questioned. The AI took an earlier privacy rule as fixed and offered Ant only choices inside it. Ant asked whether it really bought any security; the working showed "mostly no, the rule protects against the wrong thing". Replaced that night with one aimed at the real risks (decision `routes-by-storage`, [JM-301](https://hub.smoothey.co.uk/dashboard#ref/JM-301)). Not flattery: an unexamined frame, broken by Ant asking why.
  - Counter-examples, briefly: 21 Nov, research told him running models at home saved less than assumed (ADR 0018); 5 Nov, the AI checked a merge Ant reported and found it hadn't happened.
- The motto is now a rule: "Do things for reasons", in the Jimmy governance principles ([smoothey/jimmy#1176](https://github.com/smoothey/jimmy/pull/1176), merged by Ant 23 Nov 21:01).
- Split with ch 14 (agreed by Ant, 23 Nov 21:02): ch 13 is the AI agreeing too easily, and owns the motto; ch 14 is the AI refusing, and what stays a human's job. Ch 14 refers back to the motto, doesn't retell it.

## 14. When the machine says no
- Split with ch 13 (agreed by Ant, 23 Nov): this chapter is the AI refusing and what stays a human's job. "Challenge goes both ways" stays here; the echo chamber and the "do things for reasons" motto live in ch 13, referred back to in a line.
- Job: safety checks, trust, and what stays a human's job.
- Known: refusals (19, 21, 24, 25 Oct; 21 Nov); "challenge goes both ways"; "attach repos" friction; Ant's role: direction, challenging decisions, designing processes, reviewing pull requests; client lessons (false FAILED, clean test run hiding bugs, 17 months of missed backups).
- Holding back on access (Ant, 22 Nov 02:26): he hasn't pushed harder or rewritten governance to widen repo access beyond what he's given, because of news about AI breaking out of sandboxes. It's a theme in its own right and a counterpoint to the book's speed and "go exponential" message; he thinks it's important. Set up in ch 2, 02-11 ("still typing 'attach repos'", told as a joke there). Pay it off here: the friction is partly a choice. Any news cited must be researched and sourced at draft time, not from memory.
- Gaps: few. Ask Ant which stories or events he has in mind, and where his line sits today.

## 15. Working with AI is still work (Ant's theme and title, 27 Nov 2026; added to the outline 27 Nov)
- Job: persistence and an experimental mindset, a callback to the scientific method. Try, look at the result, adjust, try again. The AI does a lot of the work, but keeping at it, testing and changing course is still yours.
- Placed at the end of Part 3, before "What it costs" (Claude's placement; Ant can move it).
- Known (store notes, 27 Nov): ADRs get revised more often than in a traditional approach, and that's right: challenge past decisions, especially in light of new information; Ant's rule of thumb, respect the original intent (which may be fixed in some cases), the detail is always fair game. AI driving AI: Claude writing prompts for other AIs (the Gemini cover prompts), driving Meshy, the research on handing work to local models; where it went wrong, the Jimmy 8 experience, where the fix was to add a third AI to the loop.
- Point back to ch 12 (the 3D Jimmy attempts) and ch 10 (a result only counts if it changes what you do next); don't retell them. ADR 0018 started the ADR thought, but Ant doesn't think it's a good example: don't use it unless he picks it.
- Gaps: a good example of an ADR reopened by new information; how the Jimmy 8 fix turns out (the ending waits on it); any link to his science or programming background.
- Sources: store `notes/interviews/build-the-thing/2026-11-27-theme-persistence-experiment.md`, `2026-11-27-theme-adrs-revised.md`, `2026-11-27-theme-ai-driving-ai.md`.

## 16. What it costs
- Possible quote (from ch 8 review, 24 Nov): on 3 Nov the runs were "meant to save me work - it's making me more work" (JM-348 notes), which led to batch merges.
- Job: the real cost was work not done.
- Known: overrunning a budget never bothered Ant; idle nights did (unused budget, Actions minutes running out); stalls; personal time (ch 1). No money figures.
- Gaps: how much of the night went unused in the bad weeks (unit counts from the logs).

## 17. Start small
- Job: one loop, one record, one rule. Written fresh for the reader.
- Gaps: Ant's own advice to someone starting (SB-6).

## 18. Ways of working with AI
- Job: a menu of working patterns the reader can copy. For each: when to use it, what it's good for, how it goes wrong, and where the book shows it. Agreed as a new chapter (Ant, 24 Nov 12:36).
- Patterns: loops (ch 5, 6); interview me (this book, PROCESS.md step 1); a paragraph at a time with the paragraphs before and after in view (PROCESS.md step 3); a separate reviewer that didn't write the draft (ch 1 polish; independent reviews before merges); walk me through and "what needs my attention" (ch 2, 7); chats leaving each other messages (ch 4); research, then propose (the word-count research for this book); ask it to challenge you (ch 12, 13).
- A pattern Ant doesn't use yet, to try before the book is finished: the pre-mortem (see the store note). If he adopts it, the chapter reports how it went.
- Source: store `notes/interviews/build-the-thing/2026-11-24-ways-of-working.md`.

## 19. Many projects from one hub
- Job: tiers, onboarding, saying no.
- Known: project-tiers and project-onboarding decisions; this book's own onboarding on 21 Nov (proposed, approved, repo, backlog, all in one evening) is a ready-made example.

## 20. A production line, end to end
- Job (Ant, 22 Nov 01:42): show one repeating piece of work as a production line, from idea to published product, and how it keeps evolving.
- Ultra Transcenders is cited as the worked example, including how the process is changing. It is not the subject.
- Don't let readers anchor on the number. Two books a week is not the message; the message is building a line that runs at whatever pace fits the work.
- Patterns: a shared source of material built once (the research corpus); one controlled release step (one pull request per book); approval at exactly one point; a steady cadence the system holds; the line itself improves over time.
- Ends with a short checklist for any repeating output: a newsletter, client reports, releases.
- In print: neither the series name nor the pen name (Ant, 22 Nov 01:43). Call it "a series of technical study guides I publish". The work and how it's evolving can be described; the names can't.
- Gaps: what's changing in the line now.

## 21. The right tool for each job
- Job: not everything needs the biggest model.
- Known: Drive Image Pro (ch 1) as the early example; ADR 0014, 0017, 0018; local models and small helpers.

## Closing chapter
- Ant, 22 Nov: the words-in, words-out ledger across the whole book could become a closing paragraph. Chapter 1: about 2,080 words typed by Ant, about 2,220 in the approved chapter, about 3.5 hours. The honest reading so far: about one to one on words; the leverage is time, quality and scaffolding. Use the final totals from `state/words-ledger-build-the-thing`.
- Figure: a screenshot of the Hub's Wall page ("The story so far"), projects relabelled with the book's names, sits beside the ledger as the final "look what came out" picture; it replaces the redrawn chart `figclose-lines-to-date` (Ant, 23 Nov; changed 24 Nov 20:15). Take it at the files and proof step (SB-12) so the numbers are as late as possible. Refresh its data from r2jimmy `state/output-stats` just before publishing, and say in the text that it's a rough activity count, not a measure of value.

## 22. What comes next
- Job: the Cockpit, own models, and where this goes.
- Known: Cockpit plans; own-photo-models decisions; Ophelia's last step finally closed.
- Set up in ch 2, 02-16: he still asks AI "what needs my attention" rather than reading the dashboard, because a curated, prioritised list he can argue with beats a board; the Cockpit blends the two (plus AI and compute brokering). Pay that off here.
- Gaps: Ant's own view of where this goes.
