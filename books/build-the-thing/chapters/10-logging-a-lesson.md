# Chapter 10: Logging a lesson isn't learning it

<!-- p: 10-01 | agreed 2026-11-28 -->
Between 19 October and 21 November, the same lesson was written down seven times. Each time it was clear, accurate and sensible. Each time it said what had gone wrong and what should change. And each time, a few days later, the same thing went wrong again.
<!-- src: r2jimmy lessons 2026-10-19-agency-test-1, 2026-10-23-agency-test-1, 2026-10-27-agency-test-1, 2026-10-31-agency-test-1, 2026-11-12-agency-test-1, 2026-11-19-agency-test-1, 2026-11-21-agency-test-1; figures/fig10-lesson-seven-times -->

<!-- p: 10-02 | agreed 2026-11-28 -->
Lessons are one of the kinds of thing the store keeps, from chapter 4: what went wrong, and what we changed. The rule is that any run that fails or only half finishes has to write one. So the system is good at writing things down. This chapter is about the gap between noticing a mistake and not making it again.
<!-- src: chapter 4, 04-05 (agreed: "Lessons record what went wrong and what we changed"); smoothey/jimmy governance/reports/2026-10-19/morning-brief.md ("Both failed or partial runs have a lesson"). "good at noticing" made "good at writing things down", Ant 28 Nov 00:30 -->

<!-- p: 10-03 | agreed 2026-11-28 -->
The mistake itself was small. Every scheduled task has an entry in a register on the Hub: what it is, when it runs, which project it's for and what it's allowed to touch. It's how I know what's running in my name, and with what access. Every evening at 20:23, the agency test from chapter 5 checks that each scheduled task is in that register. On 19 October, a chat had made one without registering it, and the test failed.
<!-- src: r2jimmy lesson 2026-10-19-agency-test-1 ("A chat made a scheduled task without registering it"); smoothey/jimmy CLAUDE.md and governance/loops/CONTRACT.md "Authority" (the Hub is the authority for every scheduled job and the access each has); chapter 5, 05-02 (agreed: agency test at 20:23). "and with what access" added, Ant 28 Nov 00:31 -->

<!-- p: 10-04 | agreed 2026-11-28 -->
The culprit was always the same kind of thing: a one-off reminder. I'd say "remind me to check this on Thursday", and the chat would set one up, straight away, and forget the register. The test caught it that evening. A lesson was written: one-off tasks made in a chat need a register entry at the same time. Then it happened on 23 October. Then 27 and 31 October, then 12, 19 and 21 November.
<!-- src: r2jimmy lessons as 10-01 (titles: "One-off scheduled tasks made in a chat need a register entry at the same time" 23 Oct; "A reminder made from a chat skipped the hub register" 27 Oct; "One-off tasks made in chat skip the hub register" 31 Oct; "One-off reminders made in a chat skip the hub register" 12 Nov; "A one-off reminder task was made without a register entry" 19 Nov; "(again)" 21 Nov). "remind me to check this on Thursday" is an illustration, not a quote; Ant agreed it as written, 28 Nov 00:39 -->

<!-- p: 10-05 | agreed 2026-11-28 -->
Every one of those lessons was right. That was the problem. Nobody needed to be told what had gone wrong; by the end, the record had said so seven times. The lesson lived in the store. The rule lived in a file about the schedule. But a chat that's just been asked to remind me about something doesn't open either of them. The thing that kept making the mistake never read the place where the lesson was kept.
<!-- src: claude/project-instructions.md, 21 Nov ("The 'register after' rule lived only in schedule.md, which a chat answering 'remind me' doesn't open"). "six times over" made "by the end, the record had said so seven times" to match 10-01, Ant 28 Nov 00:40 -->

<!-- p: 10-06 | agreed 2026-11-28 -->
It wasn't the only one. On 10 November, six runs tried the same command to reset their copy of the code, and the safety check refused it every time. Three nights later, two more did the same. And when I counted, of the 53 lessons logged in the first five weeks, only about one in four had ever been marked as applied. Writing a lesson down is cheap. Changing what happens next time is the hard part.
<!-- src: r2jimmy lessons 2026-11-10-morning-brief-1 ("Six runs tried git reset --hard on an existing clone; it is refused every time"), 2026-11-13-nightly-photo-organiser-2-1 ("Both Snappier shifts used git reset --hard"); lesson records 18 Oct to 21 Nov counted 24 Nov: 53 lessons, 14 with status applied. "and the system is very good at it" trimmed (repeats 10-02), agreed by Ant 28 Nov 00:41 -->

<!-- p: 10-07 | agreed 2026-11-28 -->
The fix for the reminders, on 21 November, wasn't another lesson. It was moving one sentence. Every chat in a Project, a set of chats that share one set of instructions, starts by reading them, so that's where the rule went: "Before making any scheduled task or reminder, write its Hub register entry first." Register first, then make the task. The same day, the agency test changed too. A stray one-off from the past week now gets registered by the test itself, and passes with a note. Only a recurring or older task still fails.
<!-- src: claude/project-instructions.md, "21 Nov 2026: register scheduled tasks first" (new Project line, quoted; agency-test check 9 registers a stray one-off from the last 7 days as a pass with a note; smoothey/jimmy#1076); Jimmy Hub Project instructions (live text includes the line). Agreed by Ant 28 Nov 00:44 with the tool names in brackets dropped from the quote and Project glossed -->

<!-- p: 10-08 | agreed 2026-11-28 -->
Since then, it hasn't happened again. The test passed all fourteen of its checks on the first two nights, and the mistake hasn't come back since. It's the first time the lesson changed something the next chat would actually read.
<!-- src: smoothey/jimmy governance/reports/2026-11-22/agency-test.md ("ok, 14 of 14 checks passed"), 2026-11-23/agency-test.md ("passed 14 of 14"); Ant, 28 Nov 00:59: "Its fixed now it hasn't re-occurred". Rewritten and agreed 28 Nov 00:59 -->

<!-- p: 10-09 | agreed 2026-11-28 -->
I'd seen lessons stick before. On the firewall work, the AI's traps went into its notes about that client, and it didn't fall into them again. Looking back, the difference is simple. Those notes were read at the start of every job. The lesson sat in the path of the work, not beside it.
<!-- src: chapter 4, 04-10 (agreed: notes read at the start of each session; traps banked); notes/source-material/build-the-thing/2026-11-21-client-azure-ops-ai-usage.md ("Banked gotchas ... stopped repeat mistakes across sessions"). The "difference" is the drafter's reading; Ant agreed it, 28 Nov 01:01 -->

<!-- p: 10-10 | agreed 2026-11-28 -->
It's the same question as chapter 4. Is the AI stupid, or has nobody given it the right context? A lesson kept somewhere the AI never looks is context it doesn't have. It isn't forgetting. It never knew.
<!-- src: chapter 4, 04-01 (agreed: "Is it stupid, or has nobody given it the right context?") -->

<!-- p: 10-11 | agreed 2026-11-28 -->
So a lesson isn't learnt until it changes one of three things: what the next run or chat reads before it starts, a check that catches the mistake before it does harm, or the tool itself, so the mistake can't be made at all. Writing it down is the first step, not the last.
<!-- src: drafter's synthesis of 10-05 to 10-09 (instructions: the Project line; check: agency-test check 9; tool: the safety check refusing git reset --hard). Reworded as one list and agreed by Ant, 28 Nov 01:05 -->

<!-- p: 10-12 | agreed 2026-11-28 -->
That changes the question I ask when something goes wrong twice. Not "did we write it down?" We almost always did. The question is where the next run, or the next chat, will come across it before it makes the same mistake.
<!-- src: drafter's closing line; agreed by Ant 28 Nov 01:06, then changed to the clearer wording ("come across it before it makes the same mistake", was "trip over it") at 01:07 -->
<!-- p: 10-13 | agreed 2026-11-28 -->
There's a fourth place a lesson can end up, and it's the one I'm most hopeful about. On 24 November I asked for the common troubleshooting steps to be turned into a skill: a written set of steps the AI loads when it needs them, like a checklist a new colleague would be handed. The raw material was the lessons. By then there were more than fifty of them, and when they were grouped by cause, a handful of causes covered most of them: runs that stalled or went quiet, runs refused by a safety check, a scheduled task with no register entry.
<!-- src: claude/jimmy-troubleshooting-skill.md (Ant, 24 Nov 15:59: a skill for Jimmy's common troubleshooting steps, and a process to develop it or propose new ones; "r2jimmy has 55 (18 Oct to 21 Nov)"; by cause: stalls, missing heartbeats and late reports about 10; refused by a permission or safety check about 9; a scheduled task made without a register entry 7). "like a checklist a new colleague would be handed" is the drafter's. "fifty-five" made "more than fifty" so it doesn't clash with 10-06's 53 (two counts of the same period); agreed by Ant 28 Nov 01:07 -->

<!-- p: 10-14 | draft 2026-11-27 -->
So now the lessons feed the skill. Every Sunday, a review reads them, groups them by cause, and suggests at most three changes for me to agree: a step to add or reword, a new skill when the same cause has turned up three times, a step to drop when nobody's needed it for two months. When Jimmy notices something failing on the Wall and I press Investigate, the fix starts by following that skill. A lesson used to be a note. Now it can become a step that runs.
<!-- src: claude/jimmy-troubleshooting-skill.md ("Weekly skill review: scheduled ... Sundays 10:42 London; first run 29 Nov 2026"; "raises at most three recommendations: a skill change with exact wording; a new skill when a cause shows three times; a noticing rule to change, drop or add; a skill step to remove after two months unused"; Do it now ends "Follow the jimmy-troubleshoot skill"); Ant, 24 Nov (the button called "Investigate" rather than "Do it now"). First review runs 29 Nov: report how it went before print. The last two sentences are the drafter's. Ant, 28 Nov 01:09: leave as is, and come back to it after the first run (29 Nov) to check it and add how it went; not agreed yet -->

<!-- p: 10-15 | agreed 2026-11-28 -->
Clients taught me the same thing long before AI did. When something went wrong, they didn't want a story. They preferred an honest "this didn't go to plan", as long as it came with a strong answer to why it wouldn't happen again. But the answer is the easy part. Each of those seven lessons said, in effect, that it wouldn't happen again. The skill is in genuinely making sure it doesn't.
<!-- src: Ant, 27 Nov 23:55 (store notes/plans/build-the-thing/2026-11-27-theme-learning-from-failure.md) ("Even clients prefer the honest, "Yeah, this didn't go to plan" as long as you have a strong answer to why it isn't going to happen again. The skill comes from genuinely ensuring it doesn't happen again!"); chapter 10, 10-01 and 10-04 (draft: the same lesson written seven times). New 28 Nov, placed last, after 10-14, as the chapter's close (after 10-12 it would break the link between 10-11's three places and 10-13's fourth). Agreed by Ant 28 Nov 01:11 with the first sentence changed to "Clients taught me the same thing long before AI did"; "they didn't want a story" is the drafter's, kept. No client names -->
