# Build the Thing That Builds the Things: outline (draft 7, 27 Nov 2026)

Agreed by Ant on 21 Nov 2026: the first 14 chapters, then all four new chapters and the appendix. 23 Nov: two more chapters added in Part 3 (12 and 13, Ant's themes); later chapters renumbered 14 to 20. 24 Nov: Ways of working with AI added in Part 4. 27 Nov: Working with AI is still work added in Part 3 (chapter 15, Ant's title); later chapters renumbered 16 to 22. 27 Nov evening: three more from the content brainstorm, 15, 16 and 18 (Ant's picks); later chapters renumbered 17 and 19 to 25. 27 Nov, 17:58: Measuring the right thing added as 19; later chapters renumbered 20 to 26. 27 Nov, 18:11: What you're actually talking to added as 15; later chapters renumbered 16 to 27. 27 Nov, 18:21: Ant unlocked the agreed chapters for a content pass across the whole book; new paragraphs in agreed chapters are drafts for him to agree, and any agreed paragraph that changes is marked reopened. Ant: chapters are coming in under length, so no padding and no squeezing to fit. Target about 45,000 to 50,000 words, about 2,500 words a chapter.

Fuller briefs per chapter (job, what's set up, known material, gaps): briefs.md.

Each chapter lists what it draws on: L = the logs (store records, run reports, decisions, ADRs), I = interviews with Ant.

## Part 1: The shift
1. **Doing the work, and the ceiling it hits.** One person, evenings, many projects. *I: the Commodore and the shop demo machines; Ophelia, the shared task tool he never had the bandwidth to grow; AzureDump, hand-maintained since 2002; "where is the ceiling really?"*
2. **Build the thing that builds the things.** The idea in one chapter, with the first night it worked. *I, plus the first run reports (18 Oct). A present for Charlie. Bridge: the client firewall work, a written procedure plus a memory before Jimmy existed (a few hours down to minutes; 22 form rows became 5 rules). The 2019 Ophelia walkthrough against 2026.*
3. **Incremental against compound.** What compounds (rules, tools, records) and what doesn't (effort). Comparative advantage: when AI writes the code, my value moves from being the best developer to vision, architecture and design. And the borrowed pace: AI plans in human-team time until you measure your own; the share-of-a-night measure. *I (Economics GCSE, 22 Nov; theme note 21 Nov), decisions sizing-night-share, night-load, night-utilisation; numbers from the Hub.*

## Part 2: The machine
4. **One place for the truth.** The store, the Hub, and why chat memory isn't enough. Is the AI stupid, or missing context? Good context management drives AI productivity. *L: ADR 0002, 0003. I: value hidden in memories the user can't see.*
5. **Work while you sleep.** Night runs, shifts, budgets as a share of a night. *L: overnight-cycles, night-load, sizing-night-share.*
6. **A night in the life.** One real night, hour by hour: from the evening run to the morning brief. Shifts, stalls, the 2am approvals. *L: run reports and morning briefs; I.*
7. **Only real asks reach you.** Needs you, Agree, away mode, the phone test. *L: asks-need-ant-and-agree, away-mode.*
8. **Rings and brokers.** Privacy by where data lives; approvals for merges, spend and infrastructure. *L: ADR 0003, 0009, 0010, 0014.*
9. **The people around you.** What never goes in; building for a partner; keeping other people's stories theirs. *L: rings, people register, never lists; I (short interview). Robyn only as Ant chooses.*

## Part 3: What it teaches you
10. **Logging a lesson isn't learning it.** The repeat lessons, and what finally fixes one. *L: lesson records; the one-off reminder lesson logged seven times, 19 Oct to 21 Nov. Contrast: on the client work, banked gotchas did stop repeat mistakes.*
11. **Best practice by accident.** Arriving at DevOps habits without setting out to. *I: "we'd be slower if we started with them"; ended up like Azure DevOps without aiming to. The tiny-tasks team against one person AI-first; "pull before building"; scripts split so a crash lands in the safe half.*
12. **Driving, or being driven?** Are you steering the AI, or following it? One evening's work on 3D Jimmy: the first version "cursed", one test anyone can apply, a rule only I knew, a tool found outside the AI. Driving isn't doing the work; it's owning the goal and the taste. *I (23 Nov), L: JM-491, jimmy#1174, #1175.*
13. **The echo chamber.** AI is built to fit your preferences, and memory makes it agree more. Anchor it on growth, not on what you already are. The scientist's habit; gold stars issued by idiots; do things for reasons. *I (23 Nov); research: Stanford in Science 2026, MIT and Penn State 2026, CJR Tow Center 2026.*
14. **When the machine says no.** Safety checks, trust, and what stays a human's job: direction, challenging decisions, designing processes, reviewing pull requests. *L: refusals in run reports and lessons; I: challenge goes both ways; "attach repos" in every chat. Client work: AI builds, human holds the keys; the false FAILED report; a clean test run that proved little; the backups nobody had noticed for 17 months.*
15. **What you're actually talking to.** Language models, intelligence and sentience, pragmatically. It sounds human, so it's easy to be fooled; productivity comes from knowing the differences and frictions. When to talk normally, and when to tailor the ask. *I (27 Nov).*
16. **What experience knows that nobody writes down.** The step a senior person does without thinking is the one the AI leaves out. Pull before deploying; draft while iterating; never push to a merged branch; keep a key off disk. The fix is in the tool, not the instructions. *L: store source notes 25 to 27 Nov.*
17. **Risk, measure and boldness.** Measure for the gung-ho, boldness for the over-cautious; how AI moves the dial; under-caution and ADHD, where it helps. *I (23 Nov, parked note; Ant's own words only).*
18. **Working with AI is still work.** Persistence and an experimental mindset: a callback to the scientific method. Try, look, adjust, try again. Revising decisions when new information turns up (respect the intent; the detail is fair game). AI driving AI, and when it goes wrong: the fix that added a third AI. *I (27 Nov): store theme notes on persistence, ADRs revised, AI driving AI. Ending waits on how the third-AI fix turns out.*
19. **Learning by building.** Using AI to learn what there was never time for: 3D, Blender, space graphics, photo models, a camera app before owning a camera. *I (26 Nov: enjoying learning through the Wall graphics); L: 3D Jimmy, Wall plans.*
20. **Measuring the right thing.** Pacing measures against value measures. Lines of code as a fair pace, if success is never "more lines"; token counts as a worse rehash of lines of code: spend and pace, not value. Ties together share of a night, minutes used, the check that never failed. *I (27 Nov); L: the measures already in the system.*
21. **What it costs.** The cost that hurt was work not done, not money spent. Stalls, minutes run out, the pull of building the system instead of the product. *I; stall lessons and night-use decisions from L. No money figures.*

## Part 4: Your turn
22. **Start small: one loop, one record, one rule.** *Written fresh.*
23. **Ways of working with AI.** A menu of patterns: loops, interview me, a paragraph at a time, a separate reviewer, walk me through, chats leaving messages, research then propose, ask it to challenge you; and one pattern tried for the first time while writing this book. *L and this book's own process; I (24 Nov).*
24. **Many projects from one hub.** Tiers, onboarding, saying no to projects. *L: project-tiers, project-onboarding.*
25. **A production line, end to end.** One repeating piece of work followed from idea to published product, and how the line keeps evolving. The study guides are the worked example, never named in print (no series name, no pen name; Ant, 22 Nov 01:43) (research corpus, book prep, go-live in one pull request, approval at one point), not the subject. The lesson is the line, not the number: readers should not anchor on two books a week. Ends with a checklist for any repeating output. *L: UT decisions and plan docs; Ant, 22 Nov 01:42.*
26. **The right tool for each job.** Not everything needs the biggest model: local models, small helpers, brokers, cheapest capacity first. *L: ADR 0014, 0017, 0018; local model decisions.*
27. **What comes next.** The Cockpit, own models, and where this goes. *L: own-photo-models, Cockpit plans; I.*

## Front and back
- A short opening story.
- A closing chapter.
- **Appendix: starter kit.** Templates a reader can copy: a contract page, a backlog record, a lesson record, a night run, a "never" list.
- A plain glossary.
- **Acknowledgements.** Dan Redmond, credited by name: Ant invited him on 23 Nov and he said yes (27 Nov). Add others as they agree.
- **Notes and further reading.** References grouped by chapter, keyed by a short phrase, with no marks in the text. Filled in as each chapter is written, polished once the book is finished (Ant, 22 Nov 16:32). File: `chapters/99-notes.md`.
- "How this book was made". Kept open until upload, to match Ant's answer to KDP's AI question (SB-10).
