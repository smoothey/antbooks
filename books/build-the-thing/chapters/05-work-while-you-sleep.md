# Chapter 5: Work while you sleep

<!-- p: 05-01 | agreed 2026-11-22 -->
The first night run, on 18 October, lasted less than an hour. A month later, every night has more than a dozen runs across seven projects, from before eleven in the evening until six the next morning. None of them needs my laptop on. Each one is a scheduled task in the cloud, so it runs whether I'm at my desk, asleep, or away.
<!-- src: chapter 2, 02-10 (agreed: first run 22:48 to 23:45 on 18 Oct); smoothey/jimmy governance/schedule.md (nightly runs from 22:47; window ends 06:00; "Every run is a Claude scheduled task in the cloud, so it runs whether or not the MSI laptop or Balrog is on"); readiness.md (seven projects: Charlie Doll, Snappier, Jimmy, Robyn's Roblox, Togmatic, Ultra Transcenders, Work) -->
<!-- rev: 'worked on one project' cut (ch 2 says three projects ran that night); agreed by Ant 22 Nov 19:27 -->

<!-- p: 05-02 | agreed 2026-11-22 -->
The night actually starts in the afternoon. At 16:37 a readiness check looks at every project and asks a simple question: is there something tonight's run can do without me? If a project has nothing agreed, or its code is broken, I hear about it while there's still time to fix it. At 20:23 an agency test goes further. It proves that tonight's runs can do their jobs without anyone approving anything: that each one can reach its code, read its rules and save its work. If any check fails, I know before I go to bed, not when I wake up.
<!-- src: smoothey/jimmy governance/schedule.md (16:37 readiness, 20:23 agency test); loops/readiness.md ("Makes sure every project has something its run can do tonight, so Ant can fix it before the evening if not"; unattended work; main passing CI); loops/agency-test.md ("Proves, before the night starts, that tonight's runs can do their jobs without anyone approving anything. If any check fails, Ant hears about it by 21:00"; clone, read rules, push) -->
<!-- rev: agreed by Ant 22 Nov 19:31 (as is) -->

<!-- p: 05-03 | agreed 2026-11-22 -->
Then the runs begin, one after another. Charlie's site goes first, at 22:47. The Roblox game follows just before midnight, then the camera app, the study guides and the photo organiser in the small hours, then Jimmy itself and the work projects around three in the morning. Most projects also get a second shift later in the night. The start times are deliberately odd, like 22:47 rather than 23:00, because runs set for the hour tend to start late when the service that starts them is busy.
<!-- src: smoothey/jimmy governance/schedule.md (22:47 Charlie Doll, 23:51 Robyn's Roblox, 00:07 Togmatic, 00:23 Ultra Transcenders, 00:53 Snappier, 02:53 Jimmy, 03:17 Work; second shifts; "Minutes are deliberately off the hour: runs set for :00 start late when the service is busy") -->
<!-- rev: agreed by Ant 22 Nov 19:32 -->

<!-- p: 05-04 | agreed 2026-11-22 -->
The night is a budget of 480 minutes, shared by priority. Charlie's site gets a third of it. The camera app and Jimmy get about a fifth each. The photo organiser gets about an eighth, and the Roblox game, the study guides and the work projects share what's left. A project's share is guaranteed, but it isn't a wall. When a run finishes early, the minutes it didn't use flow on to the runs that come after it, so a busy project can borrow up to three times its own share from a quiet one.
<!-- src: smoothey/jimmy governance/loops/cycles.json budget (nightMinutes 480; shares charliedoll 0.33, togmatic 0.20, jimmy 0.19, photo-organiser 0.13, robroblox 0.06, transcenders 0.05, work 0.04; "A project's share is guaranteed; minutes left by projects that finished earlier tonight may be borrowed"; borrowCeiling 3) -->
<!-- rev: 'about a fifth each'; agreed by Ant 22 Nov 19:34 -->

<!-- p: 05-05 | agreed 2026-11-22 -->
A run doesn't start by writing code. It starts by taking stock. It reads its project's progress record and backlog from the store, and brings them up to date with whatever happened since the last run: what I accepted, what I agreed, what I turned down. It acts on my decisions first. Then it spends about three quarters of an hour on a critical review of its own project, looking for what's broken, what's weak and what's missing. After that it looks at what's next, what dates could move forward, and whether the rules themselves need changing. Only after all that does it start building. That order matters. When I'm moving fast, several things may be half finished at once, and there may be problems I haven't spotted that need fixing before anything new can be built on top. Knowing exactly where things stand also stops the same work being built twice.
<!-- src: smoothey/jimmy governance/loops/nightly-common.md (1. Set up and take stock; 1a. Bring the backlog up to date, every night; 2. Act on Ant's decisions; 3. Critical review, about 45 minutes, every night; 3a. Next steps and new functionality; 3b. Dates: what can move forward; 3c. Governance review; 4. Research and planning; 5. Work in cycles) -->
<!-- rev: 'accepted'; why from Ant 22 Nov 19:37 (half-finished work at pace, unspotted problems to fix first, accurate position stops work being built twice); agreed -->

<!-- p: 05-06 | agreed 2026-11-22 -->
The building happens in cycles. Each cycle takes the next piece of agreed work, builds it, tests it and saves it, then checks whether it should carry on. Everything a night run builds goes onto a pull request: a proposed change, waiting for me to look at it and accept it. Each project is meant to send me just one a night, because every pull request costs me a tap, though a busy night can still bring two or three. The pull requests are deliberate: nothing a night run builds reaches the real thing until I've seen it.
<!-- src: nightly-common.md (5. Work in cycles until a stop rule says stop; 5b. One cycle); morning briefs (e.g. 2026-11-09: "most of what they built waits on your merges"); chapter 3, 03-08 (agreed); smoothey/jimmy governance/loops/merging.md ("Plain night runs don't merge (Ant, 3 Nov 2026)"; "One pull request a night": "Every pull request costs Ant a tap") -->
<!-- rev: new last line (control, not time); tightened to night runs, which never merge, one PR a night (merging.md); agreed by Ant 22 Nov 19:39 -->
<!-- rev: reopened and changed 22 Nov 20:09: 'is meant to ... though a busy night can still bring two or three' (18 Nov: Charlie Doll opened poseroll#453, #460, #464); agreed by Ant -->

<!-- p: 05-07 | agreed 2026-11-22 -->
Every run also has to know when to stop, and the rules for that turned out to matter as much as the rules for working. A run stops when the night's window closes, or when its minutes or its allowance of saved changes run out. It stops if the project's main code is broken and one attempt to fix it hasn't worked, or if fewer tests pass than when it started. It stops if a safety check refuses something, and it doesn't try to find a way round. And it stops when it has been going so long that it's losing track, which is the context problem from chapter 4 showing up at three in the morning.
<!-- src: smoothey/jimmy governance/loops/cycles.json stop.hard (window, budget, red-main, tests-fell, live-drift, safety: "don't retry around it", context: "the session has got long and work is slowing or going wrong"); nightly-common.md 5c; chapter 4, 04-03c (agreed) -->
<!-- rev: agreed by Ant 22 Nov 19:41 -->

<!-- p: 05-08 | agreed 2026-11-22 -->
That last one is why most projects have more than one shift. A long session fills up its context, and the work starts to slip. So instead of one run trying to last all night, a run writes a hand-over note when it stops, and a fresh shift picks it up later with a clear head: what was done, what's half done, what to do next. Charlie's site, which has the most work, now has relay shifts that can take over from each other through the night. It's the same idea as a hospital shift change, and for the same reason.
<!-- src: schedule.md (second shifts at 01:37, 02:13, 02:37, 03:22, 03:47; relay shifts 00:17 and 03:07 for Charlie Doll; late shift 04:47); nightly-common.md 5d and "Relay shifts" (Ant, 22 Nov 2026, decision night-utilisation-plan-2026-11-22: when a run stops on context after about 45 minutes with agreed work left); the hospital comparison is Claude's -->
<!-- rev: agreed by Ant 22 Nov 19:43; relay shifts agreed 22 Nov, check their track record at final check -->

<!-- p: 05-09 | agreed 2026-11-22 -->
The stop I like least is "empty": a run with minutes left and nothing it's allowed to do. For a while, it was the commonest reason a night went unused. So the rules now say a run has to prove a queue is empty before it stops. It must go through every agreed item and every idea, and say why each one can't be done tonight. And if the only thing left is a small idea that's safe to build without me, it can build that instead of stopping. An idle night has to justify itself.
<!-- src: nightly-common.md 5c ("Prove it's empty", Ant, 21 Nov 2026, decision night-fill-stronger; small ideas instead of empty, PF-118 and PF-133); morning briefs Nov 2026 (runs stopping on empty); chapter 3, 03-12 (agreed) -->
<!-- rev: agreed by Ant 22 Nov 19:43; figure fig05a goes after this paragraph -->

<!-- p: 05-10 | agreed 2026-11-22 -->
Each run leaves a trail. When it starts, it writes a heartbeat, a small file that says "I'm running". When it finishes, it replaces that with a final heartbeat and a report: what it did, how many minutes it used, why it stopped, and what it needs from me. If a run disappears without a final heartbeat, something went wrong. Telling a run that's still working from one that has quietly died turned out to be harder than it sounds, as the next chapter shows.
<!-- src: smoothey/jimmy governance/loops/CONTRACT.md (2. Start heartbeat; 3. Heartbeat: governance/status/<night>/<loop>.json replaces the start heartbeat; "the watchdog on GitHub reads"); reports in governance/reports/<night>/; r2jimmy lesson 2026-11-02-morning-brief-1 ("Seven shifts left no final heartbeat, and the brief can't tell stopped from still working") -->
<!-- rev: honest ending (2 Nov: seven shifts left no final heartbeat); sets up ch 6; agreed by Ant 22 Nov 19:45 -->

<!-- p: 05-11 | agreed 2026-11-22 -->
At 06:13 the morning brief reads all of it. It checks that every run that should have happened did, and that nothing is missing or failed. It counts the minutes used. It gathers everything that needs me into one list, with a reason for each item and an action I can take. When I wake up, that's the first thing I read. Most mornings it takes me a few minutes, and the list of things only I can decide is short.
<!-- src: schedule.md (06:13 Portfolio: morning brief, "Gathers the night, checks nothing is missing, tells Ant what to agree"); morning briefs in governance/reports (runs, utilisation, recs with why and action); chapter 2, 02-11 (agreed) -->
<!-- rev: new ending (avoids echoing 02-11), confirmed true by Ant; agreed 22 Nov 19:46 -->

<!-- p: 05-12 | agreed 2026-11-22 -->
The nights aren't the only time the work goes on. During the day, extra runs pick up queued tasks for some of the projects, paid from a separate daily allowance and started automatically when there's room. Unlike the night runs, these can accept their own work when every check passes and nothing in it is on the list that always waits for me. But the night is still where most of the building happens, because it's the time I'm least able to help, and the time the work gets in nobody's way.
<!-- src: schedule.md (07:00 to 21:30 credit runs for Jimmy, Snappier, Robyn's Roblox, Togmatic, Charlie Doll queued tasks only; "started by the backup runner"; daily allowance in cycles.json budget.credit); no money figures per the never list -->
<!-- rev: credit runs may merge when green and nothing on the hold list (merging.md); agreed by Ant 22 Nov 19:48 -->

<!-- p: 05-13 | agreed 2026-11-22 -->
My part of the night is small, but it isn't nothing. Before bed I usually check what's waiting and accept a couple of pull requests, so the night starts from the latest work. On 18 November I accepted two at 23:15 and 23:53, while Charlie's site was mid-run. In the morning I read the brief, agree or decline what it asks, and accept what's ready. Twenty minutes either side of sleep, against a night of building.
<!-- src: smoothey/jimmy governance/reports/2026-11-18/morning-brief.md (poseroll#453 merged 23:15, poseroll#460 merged 23:53); "twenty minutes either side of sleep" confirmed by Ant 22 Nov 19:52 -->
<!-- rev: agreed by Ant 22 Nov 19:52 -->
