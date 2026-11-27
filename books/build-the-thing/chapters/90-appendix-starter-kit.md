# Appendix: a starter kit

<!--
First draft, 27 Nov 2026 (Ant's pick, 18:29: "Starter kit"). Outline: "Templates a reader can copy: a contract page, a backlog record, a lesson record, a night run, a 'never' list." Chapter 22 promises one template each for a record, a night run, a lesson and a never list.
Every template is a plain-words version of a real file or record in Ant's system, with names, codes, paths and products taken out (chapter 22: "Deliberately names no product"). Sources: smoothey/jimmy governance/loops/CONTRACT.md (Your night; What every run writes; Backlogs; Sizing: a share of a night; Failure, and learning from it; Standing limits); r2jimmy record kinds backlog and lesson; the antbooks project register's "never" list.
Code blocks are for the reader to copy. Ant to agree the field names and wording; polish may plain them further.
-->

<!-- p: 90-01 | draft 2026-11-27 -->
Chapter 22 promised you templates. Here they are. Each one is a simplified version of something that runs my own system every night, with my names and tools taken out. Copy them into whatever you use: a folder of text files is plenty to start with. Change the words to suit you. The shape is the part that matters.
<!-- src: chapter 22 (draft: "The appendix has a template for each one, ready to copy: a record, a night run, a lesson, and a never list"); outline, appendix -->

<!-- p: 90-02 | draft 2026-11-27 -->
**1. The contract.** One page that every run reads before it does anything. It's the rules that apply to every job, so each job's own instructions can stay short.
<!-- src: governance/loops/CONTRACT.md ("Every scheduled run in Ant's portfolio follows this file, then its own runbook"; "Runs are unattended: nobody answers questions. A run that can't do what it was tasked with has failed, even if the session ended cleanly") -->

```
THE CONTRACT (every run reads this first)

1. Nobody is watching. Don't ask questions; nobody will answer.
   If you can't do the job, say so in your report. That's a failure,
   even if nothing crashed.
2. Before you start: write a heartbeat ("I'm running", the time).
3. Read the record for your project. Read the never list.
4. Only take work that's agreed (status: next). Ideas aren't agreed.
5. Before you build an item, check it again: is anyone else on it?
   Mark it "doing" before you start, not after.
6. Never put anything live by yourself. Leave it for me to approve.
7. Before you stop: write your report, update the record,
   write a final heartbeat ("done", or "stopped" and why).
8. If something went wrong: write a lesson (template 3).
```

<!-- p: 90-03 | draft 2026-11-27 -->
**2. A backlog record.** One record for each piece of work. Keep it small. The fields that earn their place are the status, the size, and the reason it exists.
<!-- src: r2jimmy backlog records (status idea | next | doing | done | parked; a short code in "ref"); CONTRACT.md, Sizing: a share of a night (decision sizing-night-share); Dates on items (notBefore, due); Model lanes (decision model-lanes-2026-11-26) -->

```
CODE:     AB-12   (short, so you can say it out loud)
TITLE:    What it is, in one line
WHY:      What it's for, and who it's for
STATUS:   idea | next | doing | done | parked
SIZE:     a share of a night (1/16, 1/8, 1/4, 1/2, a whole night)
NOT BEFORE / DUE:  dates, or a named event ("after the launch")
NEEDS ME: yes / no   (can a run do it without you?)
DONE WHEN: how anyone can tell it's finished
```

<!-- p: 90-04 | draft 2026-11-27 -->
Size work as a share of a night, not in hours or days. You'll find out quickly how much a night really holds, and the number will be yours, not a guess borrowed from a human team. Chapter 3 tells why that matters.
<!-- src: decision sizing-night-share ("size backlogs as a share of a night, not S/M/L"); chapter 3 (agreed: the borrowed pace) -->

<!-- p: 90-05 | draft 2026-11-27 -->
**3. A lesson record.** Written whenever something goes wrong. The important field is the last one: where the change was made. A lesson isn't learnt until it changes something the next run will actually meet, as chapter 10 explains.
<!-- src: r2jimmy lesson records (fields what, why, change, status, closed how); chapter 10 (draft: a lesson isn't learnt until it changes what the next run reads, a check, or the tool) -->

```
DATE / WHICH RUN:
WHAT HAPPENED:   facts only
WHY:             the cause, as far as you know it
WHAT CHANGES:    the fix
WHERE IT CHANGED: the instructions the next run reads
                  | a check that catches it
                  | the tool itself
SEEN BEFORE?:    link the earlier lesson if this is a repeat
STATUS:          proposed | applied | not needed
```

<!-- p: 90-06 | draft 2026-11-27 -->
If a lesson's "seen before" field keeps filling in, stop writing lessons about it. Move the fix to where the next run will trip over it instead.
<!-- src: chapter 10 (draft: the same lesson logged seven times; the fix was moving one sentence) -->

<!-- p: 90-07 | draft 2026-11-27 -->
**4. A night run.** The instructions for one job. They sit on top of the contract, so they only need what's special about this job.
<!-- src: governance/loops/nightly-common.md and the project runbooks (nightly-<project>.md); CONTRACT.md, Your night; chapter 5 (agreed: stop rules, shifts, heartbeats, the morning brief) -->

```
NIGHT RUN: <project>

WHEN:        e.g. 23:00 every night
BUDGET:      e.g. 90 minutes, or a share of the night
WHAT TO DO:  take "next" items from the project's backlog,
             most important first; build, test, save each one
             as a change for me to approve
STOP WHEN:   the budget is spent | nothing agreed is left ("empty")
             | the session is getting full | something is unsafe
HAND OVER:   if you stop with work half done, leave a note
             the next shift can pick up
REPORT:      what you did, what you skipped and why,
             what needs me, and how many minutes you used
```

<!-- p: 90-08 | draft 2026-11-27 -->
Add a morning job once you have more than one run. It reads every report and gives you one page: what ran, what didn't, and only the things that really need you.
<!-- src: chapter 5 (agreed: the morning brief); chapter 7 (agreed: only real asks reach you) -->

<!-- p: 90-09 | draft 2026-11-27 -->
**5. A never list.** What must never go into the system, or come out of it. Write it before anything else, and put it where every run reads it. Mine are longer, but they all start like this.
<!-- src: the antbooks project register's "never" list; smoothey/antbooks CLAUDE.md (Never); chapter 9 (draft) -->

```
NEVER
- Passwords, keys or other secrets, anywhere: not in files,
  reports, notes or messages.
- Other people's private details or stories without their say-so.
- Money figures in anything that might be shared.
- Anything about my clients' or employer's work.
- Anything about children beyond what I choose to say.

AND NEVER, WITHOUT ME
- Put anything live.
- Spend money.
- Change who can see or do what.
```

<!-- p: 90-10 | draft 2026-11-27 -->
That's all of it: a contract, a record, a lesson, a night run and a never list. Start with one project and one run, as chapter 22 says, and add the rest when something tells you it's needed.
<!-- src: chapter 22 (draft: start small: one loop, one record, one rule) -->
