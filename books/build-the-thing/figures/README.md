# Figures: Build the Thing That Builds the Things

Agreed with Ant, 22 Nov 2026: about one visual per chapter, each making a point. Black and white with the cover's orange as the only accent, so they work on Kindle e-readers and in a black-and-white paperback. No real photos of people, no client names, no money figures. Every number has a source. Re-check the data figures before publishing.

Made by `charts.py` and `diagrams.py` (SVG and PNG). The admin renders come from `render-admin.py`: the real Poseroll admin code at each date, run in a headless browser with a fake sign-in and grey placeholder photos.

| File | Chapter | What it shows | Source |
| --- | --- | --- | --- |
| fig02a-admin-grew.png | 2 | The Poseroll admin on 13, 16 and 25 Oct (4, 20, 46 files) | smoothey/poseroll git history at those dates; logo replaced with a placeholder; the reveal date on the 25 Oct checklist replaced with "the reveal" (Ant, 22 Nov) |
| fig02b-how-it-grew | 2 | One problem at a time: repo, site, Jimmy, store, first night, brief and Hub, share of a night, Cockpit | chapter 2 (agreed); r2jimmy decisions; Cockpit plan docs |
| fig03a-incremental-vs-compound | 3 | A capped straight line against a curve | illustration of the chapter's idea, no data |
| fig03b-changes-per-week | 3 | Changes saved per week, 140 to 929 | git history of six repos, counted 22 Nov 2026 (SB-4) |
| figclose-lines-to-date | Not used: replaced by figwall-the-wall (Ant, 24 Nov 20:15). Kept as a fallback if the screenshot can't be cleaned | Lines written to date, stacked by project: 489,335 across five projects, 1 Oct to 22 Nov | r2jimmy state/output-stats (asOf 23 Nov 02:27), saved in figclose-lines-to-date.json; net lines of code, docs and governance; book content not counted; same as the Hub Wall (Ant, 23 Nov) |
| fig12-3d-jimmy-two-routes (planned) | 12 | 3D Jimmy two ways, side by side: Fable only, and Meshy plus Fable | Ant, 24 Nov 16:15. Renders from JM-491's work; capture late (SB-12), as both are still improving |
| figwall-the-wall (planned) | Closing chapter, beside the words ledger; replaces figclose (Ant, 24 Nov 20:15) | The Hub's Wall page, "The story so far", with projects anonymised | Ant, 24 Nov 16:15. Screenshot of hub.smoothey.co.uk/dashboard The Wall; names relabelled; no Robyn, no codes; capture late (SB-12) |
| fig04-one-truth-three-doors | 4 | The store and its three front doors | ADR 0002 |
| fig05a-minutes-per-night | 5 | Minutes used per night, 20 Oct to 21 Nov, with the 480 and 75% lines | r2jimmy decision night-utilisation (20 and 21 Oct); morning briefs in smoothey/jimmy governance/reports |
| fig03c-share-of-a-night | 3 (after 03-10) | The sizes: 1/16 to a whole night | r2jimmy decision sizing-night-share |
| fig06-a-night-hour-by-hour | 6 | The night of 18 Nov: each run's start and minutes used, two merges, the brief | smoothey/jimmy governance/schedule.md (start times); reports/2026-11-18/morning-brief.md (minutes, merges at 23:15 and 23:53) |
| fig07-needs-you | 7 | The Needs you list | mock-up: example items in the style of the real list |
| fig08-privacy-rings | 8 | Rings 0 to 3 | ADR 0003 |
| fig10-lesson-seven-times | 10 | The one-off reminder lesson, logged 19, 23, 27, 31 Oct, 12, 19, 21 Nov | r2jimmy lesson records |
| fig11-best-practice-by-accident | 11 | What I did against its formal name | DRAFT until chapter 11 is agreed |
| fig16-production-line | 20 (A production line, end to end) | Idea to published, one approval | Ultra Transcenders process, never named in print |
