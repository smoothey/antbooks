# Build the Thing That Builds the Things: outline (draft 2, agreed 21 Nov 2026)

Agreed by Ant on 21 Nov 2026: the first 14 chapters, then all four new chapters and the appendix. Target about 45,000 to 50,000 words, about 2,500 words a chapter.

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
12. **When the machine says no.** Safety checks, trust, and what stays a human's job: direction, challenging decisions, designing processes, reviewing pull requests. *L: refusals in run reports and lessons; I: challenge goes both ways; "attach repos" in every chat. Client work: AI builds, human holds the keys; the false FAILED report; a clean test run that proved little; the backups nobody had noticed for 17 months.*
13. **What it costs.** The cost that hurt was work not done, not money spent. Stalls, minutes run out, the pull of building the system instead of the product. *I; stall lessons and night-use decisions from L. No money figures.*

## Part 4: Your turn
14. **Start small: one loop, one record, one rule.** *Written fresh.*
15. **Many projects from one hub.** Tiers, onboarding, saying no to projects. *L: project-tiers, project-onboarding.*
16. **A production line, end to end.** One repeating piece of work followed from idea to published product, and how the line keeps evolving. The study guides are the worked example, never named in print (no series name, no pen name; Ant, 22 Nov 01:43) (research corpus, book prep, go-live in one pull request, approval at one point), not the subject. The lesson is the line, not the number: readers should not anchor on two books a week. Ends with a checklist for any repeating output. *L: UT decisions and plan docs; Ant, 22 Nov 01:42.*
17. **The right tool for each job.** Not everything needs the biggest model: local models, small helpers, brokers, cheapest capacity first. *L: ADR 0014, 0017, 0018; local model decisions.*
18. **What comes next.** The Cockpit, own models, and where this goes. *L: own-photo-models, Cockpit plans; I.*

## Front and back
- A short opening story.
- A closing chapter.
- **Appendix: starter kit.** Templates a reader can copy: a contract page, a backlog record, a lesson record, a night run, a "never" list.
- A plain glossary.
- **Notes and further reading.** References grouped by chapter, keyed by a short phrase, with no marks in the text. Filled in as each chapter is written, polished once the book is finished (Ant, 22 Nov 16:32). File: `chapters/99-notes.md`.
- "How this book was made". Kept open until upload, to match Ant's answer to KDP's AI question (SB-10).
