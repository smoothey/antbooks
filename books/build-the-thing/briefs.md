# Build the Thing That Builds the Things: chapter briefs (22 Nov 2026)

One brief per chapter: its job, what earlier chapters have already set up (agreed text only), what we already know, and the gaps to fill. Updated after chapter 1 was agreed. Briefs change as the book develops (PROCESS.md, step 2).

Sources live in the store (`r2antbooks` `notes/interviews/build-the-thing/`, `notes/source-material/build-the-thing/`) and in `smoothey/jimmy` and `r2jimmy`. Themes noted so far: borrowed pace; comparative advantage; context management; delegation through frameworks.

## Introduction (drafted, not yet reviewed)
- Job: the promise of the book in under 1,000 words.
- Check at review: it repeats chapter 1's question ("where is the ceiling, really?"). Decide whether the intro asks it and chapter 1 answers it, or the intro leads with a different hook.
- Now says mid September (fixed 22 Nov). Its list of themes should add comparative advantage and context.

## 1. Doing the work, and the ceiling it hits (agreed 22 Nov, about 2,120 words)
- Sets up, for later chapters to pay off:
  - "I didn't know it yet, but that was the idea behind everything that came later" (the firewall procedure plus memory) → ch 2.
  - Comparative advantage, named at sixteen, "decades and a very different kind of tool" before he understood it → ch 3.
  - "The best use of my hours was building the thing that saved them" → ch 2 and ch 3.
  - Drive Image Pro picked because it could be scripted → ch 17.
  - Building a CMDB from need before knowing ITIL → ch 11.
  - Ophelia: a framework let a non-programmer contribute, but the last step always waited on Ant → ch 9 and ch 18.
  - The personal-time cost of building tools in the evenings → ch 3 and ch 13.
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
- Gaps: before-and-after numbers (SB-4): books a week, pull requests and lines a week, Ant's own minutes a day. Unit counts only, no money.

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
- Job: Needs you, Agree, away mode, the phone test.
- Known: decisions asks-need-ant-and-agree, agree-or-discuss, away-mode, away-is-reduced-access (about 2 hours a day, not a freeze).
- Gaps: what it was like running everything from a phone while away (1 to 13 Nov), if Ant wants that in.

## 8. Rings and brokers
- Job: privacy by where data lives; approvals for merges, spend and infrastructure.
- Known: ADR 0003, 0009, 0010, 0014. Little Ant input needed.

## 9. The people around you
- Job: what never goes in, building for people you care about, and keeping their stories theirs.
- Known: never lists; rings; Charlie happy to be in the book; the delegation theme (Ophelia then, Charlie's site admin with Jimmy now); this book's own consent checks (Charlie, Ant's mother, his wife-to-be, a former partner's detail left out).
- Gaps: needs a short interview (SB-6). Robyn only as Ant chooses.

## 10. Logging a lesson isn't learning it
- Job: why lessons repeat, and what makes one stick.
- Known: the one-off reminder lesson, logged seven times (19 Oct to 21 Nov); on the client work, banked gotchas did stop repeats; context theme (a lesson only helps if it reaches the next run).
- Gaps: Ant's view on why one stuck and the other didn't.

## 11. Best practice by accident
- Job: arriving at known good practice without setting out to.
- Known: "we'd be slower if we started with them"; Jimmy ended up like Azure DevOps without aiming to; the formal tiny-tasks team (ch 1) as contrast; the CMDB before ITIL (ch 1); pull before building; scripts split so a crash lands in the safe half; user stories after the fact.
- Gaps: few.

## 12. When the machine says no
- Job: safety checks, trust, and what stays a human's job.
- Known: refusals (19, 21, 24, 25 Oct; 21 Nov); "challenge goes both ways"; "attach repos" friction; Ant's role: direction, challenging decisions, designing processes, reviewing pull requests; client lessons (false FAILED, clean test run hiding bugs, 17 months of missed backups).
- Gaps: few.

## 13. What it costs
- Job: the real cost was work not done.
- Known: overrunning a budget never bothered Ant; idle nights did (unused budget, Actions minutes running out); stalls; personal time (ch 1). No money figures.
- Gaps: how much of the night went unused in the bad weeks (unit counts from the logs).

## 14. Start small
- Job: one loop, one record, one rule. Written fresh for the reader.
- Gaps: Ant's own advice to someone starting (SB-6).

## 15. Many projects from one hub
- Job: tiers, onboarding, saying no.
- Known: project-tiers and project-onboarding decisions; this book's own onboarding on 21 Nov (proposed, approved, repo, backlog, all in one evening) is a ready-made example.

## 16. Two books a week
- Job: the study guides as the case study.
- Known: UT decisions and plan docs: research corpus, book prep, go-live in one pull request, the Sunday upload.
- Gaps: pen name and series name in or out (Ant's call).

## 17. The right tool for each job
- Job: not everything needs the biggest model.
- Known: Drive Image Pro (ch 1) as the early example; ADR 0014, 0017, 0018; local models and small helpers.

## 18. What comes next
- Job: the Cockpit, own models, and where this goes.
- Known: Cockpit plans; own-photo-models decisions; Ophelia's last step finally closed.
- Gaps: Ant's own view of where this goes.
