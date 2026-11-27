# Chapter 16: What experience knows that nobody writes down

<!--
First draft, 27 Nov 2026 (Ant's pick from the content brainstorm, 17:25; working title). Sources: store r2antbooks notes/source-material/build-the-thing/2026-11-27-deploy-without-pull.md, 2026-11-25-pushing-to-merged-branches.md, 2026-11-27-draft-prs-and-version-9.md, 2026-11-26-key-off-disk.md (the key story is told in ch 14, 14-13; point to it here).
-->

<!-- p: 16-01 | draft 2026-11-27 -->
Some of the AI's mistakes aren't about what it knows. They're about what it doesn't do. An experienced person carries dozens of small habits that never get written down, because nobody thinks to. You just do them. The AI has read everything that was written down, so it has every rule and none of those habits. And it copies the silence perfectly.
<!-- src: deploy-without-pull note ("The gap between the two is a step a senior person does without thinking, so nobody writes it down, and the AI copies that silence"). Drafter's framing: Ant to agree -->

<!-- p: 16-02 | draft 2026-11-27 -->
Here's the one that caught me most recently. On the night of 26 November, we were fixing the merge page, the one I use to approve changes from my phone. Four fixes went in over about three hours, late at night. Each one ended the same way: merge it, then run the deploy script. Not one of them said to fetch the latest code first. Just after midnight, I reported that the page still wasn't working. It turned out the live page was running the fix from two changes earlier. The bug I was looking at had already been fixed, twenty-two minutes before.
<!-- src: deploy-without-pull note (four broker fixes, jimmy#1445, #1449, #1452, #1455, "in about three hours, late at night"; every "your steps" list said merge, then merge/infra/deploy.ps1, none said git pull; 27 Nov 00:01 "still isn't playing"; live broker serving #1449's panel script although #1452 had been merged 22 minutes before). jimmy#1445: https://github.com/smoothey/jimmy/pull/1445; jimmy#1452: https://github.com/smoothey/jimmy/pull/1452. "the merge page" stands in for the merge broker's panel: Ant to check -->

<!-- p: 16-03 | draft 2026-11-27 -->
The reason is simple once you see it. The merge happens on GitHub, where the code lives. The script runs from the copy on my own computer. If nobody updates that copy, the script deploys the old code, and it reports success. Nothing fails loudly. Anyone who has done this for a while pulls first without thinking. When I flagged it, I put it like this: a less experienced developer, or me when I'm tired, might not realise.
<!-- src: deploy-without-pull note ("The merge happens on GitHub. The script runs from the copy on Ant's computer. If that copy wasn't updated, the script deploys the old code and reports success. Nothing fails loudly"; Ant, 27 Nov 00:29: "you often don't tell me to git pull, a less experienced dev (or me when I'm tired) might not realise to pull the latest version of the code when running deployment scripts") -->

<!-- p: 16-04 | draft 2026-11-27 -->
The second habit is about time. I often merge a change from my phone in the middle of a conversation with a chat. The chat doesn't know. It still remembers the pull request as open from twenty minutes ago, so it carries on and adds more work to it. But the branch has gone, and the extra work quietly lands somewhere that never reaches the live site. Of one run of ninety-seven merged pull requests, three had work added after they'd been merged. One had a change pushed to it fifty-eight seconds after I merged it.
<!-- src: pushing-to-merged-branches note (Ant, 25 Nov 19:32; "Of the last 97 merged pull requests, three branches had new commits after their merge"; wall-pods-merged-land: #1327 merged 25 Nov 15:34, "pushed to it 58 seconds later"; "the push quietly makes it again, with no pull request. The work sits there and never reaches main"). jimmy#1327: https://github.com/smoothey/jimmy/pull/1327 -->

<!-- p: 16-05 | draft 2026-11-27 -->
That's a habit any developer on a team has: check whether something has changed before you build on it. The AI's picture of the world goes stale inside a single conversation, and nothing tells it so. And it gets worse the better the method works. The faster I move, the more often I'm ahead of the chat.
<!-- src: pushing-to-merged-branches note ("The AI's picture of the world goes stale inside one conversation ... nothing tells it things changed"; "The person moving faster than the AI expects ... is exactly what working this way encourages, so the failure grows with success"); chapter 11, 11-06 (draft: pull before you build) -->

<!-- p: 16-06 | draft 2026-11-27 -->
The third is about cost. While we were trying fixes on 3D Jimmy, the chat opened its pull request as ready for review and then pushed to it about ten times, one try after another. Every push started the full set of checks, including one that takes screenshots of every page of the Hub. That came to twenty-five runs and about two and a half hours of machine time, for results nobody needed until the end. Marking it as a draft, the way you would while you're still trying things, would have cost nothing. The checks already skip drafts.
<!-- src: draft-prs-and-version-9 note (jimmy#1454 "pushed to about ten times"; "Every push ran the Hub preview check (7 to 18 minutes on the runner each time) and the summary check: 25 runs, about 2.4 hours of machine time"; "The check already skips drafts. Opening the pull request as a draft would have cost nothing"; Ant, 27 Nov 14:49). jimmy#1454: https://github.com/smoothey/jimmy/pull/1454. The screenshot check is told in ch 21 -->

<!-- p: 16-07 | draft 2026-11-27 -->
And the fourth, in chapter 14, was a security key. My instinct was right, to keep it off the disk. The easy-looking way to do that quietly wrote it to the disk anyway. Knowing where that hidden copy lands is experience too.
<!-- src: chapter 14, 14-13 (draft: the key-off-disk story); key-off-disk note ("Ant's instinct (keep it off disk) was right, and the easy-looking way quietly defeated it. The assistant earns its place by knowing where the hidden copy lands") -->

<!-- p: 16-08 | draft 2026-11-27 -->
That last one cuts the other way, and it matters. There, the AI knew the habit and I didn't. Habits aren't a human thing or an AI thing. They're whatever the person, or the model, has been bitten by before. So the useful question isn't who's more experienced. It's which habits are missing from this particular piece of work, and who's going to notice.
<!-- src: drafter's synthesis from 16-02 to 16-07. Ant to agree -->

<!-- p: 16-09 | draft 2026-11-27 -->
Each time, the fix that worked wasn't a longer list of instructions. A list is just another thing to forget at midnight. The fix was to put the habit into the tools. Chats now check a pull request's state live, on GitHub, before they touch it, never from what they remember. The Hub notices work left on a branch that's already merged. And any steps that end in running a script on my computer now say to fetch the latest code first.
<!-- src: smoothey/jimmy CLAUDE.md ("Never add to a merged pull request (Ant, 25 Nov 2026, JM-533). Before pushing to an existing branch ... check its state on GitHub now, never from memory"); pushing-to-merged-branches note (the Jimmy chat's follow-up: "the Hub noticing work left on a merged branch"); lesson lesson-2026-11-26-guard-never-switched-on (the merge watch, jimmy#1361, "only notices and tells ... and stays"); Ant's standing preference, 27 Nov ("Steps that end in running a local script (e.g. deploy.ps1) should say to git pull the latest main first"); deploy-without-pull note ("The better fix is in the tool, not the instructions: a deploy script that checks it is running on the latest main"). JM-533: https://hub.smoothey.co.uk/dashboard#ref/JM-533 -->
<!-- q: SB-6 16-09: does the deploy script now check it's running on the latest code, and stop if not? If so, say so here; if not, is it worth building? -->

<!-- p: 16-10 | draft 2026-11-27 -->
There's a lesson in this for anyone who's been doing their job a long time. The habits you never wrote down are part of what you bring. They're exactly the things the AI won't have, and the things you'll notice missing first. Chapter 3 said my value had moved from writing code to vision and judgement. This is the small, daily version of the same thing: noticing the step that isn't there.
<!-- src: chapter 3 (agreed: comparative advantage; value moves to vision, architecture and design); drafter's closing. Ant to agree -->
