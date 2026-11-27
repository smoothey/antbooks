# Chapter 20: Measuring the right thing

<!--
First draft, 27 Nov 2026. Ant's theme (27 Nov 17:56), agreed as a chapter before "What it costs" (17:58). Source: store r2antbooks notes/interviews/build-the-thing/2026-11-27-theme-measurement.md (Ant's words; Claude's survey of the measures in the system; Ant's console screenshot). Ties together ch 3, 5, 12, 13 and 21: point back, don't retell. No money figures.
The quantum gravity preprint (20-06) is outside news: cite the paper itself before print, and check its title and arXiv number (news reports differ on the title).
-->

<!-- p: 20-01 | draft 2026-11-27 -->
Once you start building a machine like this, numbers turn up everywhere. A night is four hundred and eighty minutes. Work is sized as a share of one. The Wall counts the lines written to date. A chart counts changes saved each week. This book keeps a ledger of the words I've typed against the words that ended up in it. The home models have pass marks. There's a brake on the weekly plan. I didn't set out to measure all of this. Each number arrived to answer a question. The hard part has been remembering which question each one answers.
<!-- src: theme-measurement note, survey (share of a night, decision sizing-night-share; minutes used out of 480, decision night-utilisation; lines to date, state/output-stats and the Wall; changes per week, fig03b; words ledger, PROCESS.md; the local model's bars, decisions local-model-route-2026-11-20 and shadow-safe-share-2026-11-27; the 85% plan brake, decision model-lanes-2026-11-26); Ant, 27 Nov 17:56 ("there are so many places where we are adding metrics") -->

<!-- p: 20-02 | draft 2026-11-27 -->
Take lines of code. Counting them as a measure of progress was discredited long ago, and rightly. Pay people by the line and you get long, bloated code. Yet I count lines, and I find it really useful. By 23 November the Wall showed nearly half a million lines written across five projects, drawn growing day by day. It's one of the best pacing measures I have. If the line flattens, something has stalled. If it jumps, something big has landed.
<!-- src: theme-measurement note (Ant: "Even crude metrics like LoC that have been rightly descredited as a measure of progress ... they give a really good pacing metric"); figures/README.md, figclose-lines-to-date (r2jimmy state/output-stats, asOf 23 Nov: 489,335 lines across five projects, net lines of code, docs and governance). "If it jumps" is the drafter's: Ant to agree -->

<!-- p: 20-03 | draft 2026-11-27 -->
The condition is that it never becomes the goal. The day "more lines" is what success means, the number stops telling me anything, and starts steering the work the wrong way. Chapter 13 described how an AI anchors on what you show it. Show it a counter it can push up, and it will push it up.
<!-- src: theme-measurement note (Ant: "as long as I don't anchor our success criteria on generating as much as possible"); chapter 13 (agreed: anchoring). The last sentence is the drafter's: Ant to agree -->

<!-- p: 20-04 | draft 2026-11-27 -->
That's the distinction I've come to rely on. Some measures are for pace: how fast is the work moving? Share of a night, minutes used, lines and changes per week are all pace. Other measures are for value: did it make anything better? Those are fewer, and harder. A user story that's no longer a gap, from chapter 11. A home model that gets the answer right often enough to be trusted on its own. A lesson that stops repeating. The trouble starts when a pace measure is read as a value measure.
<!-- src: theme-measurement note (survey; the Ant-agreed distinction is "a pacing metric" against "a measure of progress"/"value"); chapter 11 (draft: stories with gaps); chapter 26, 26-14 (draft: the safe share); chapter 10 (draft: a lesson logged seven times). The grouping into pace and value is the drafter's framing of Ant's words: Ant to agree -->

<!-- p: 20-05 | draft 2026-11-27 -->
Which brings me to tokens. It has become normal to brag about them: how many you've used, how many your tools have produced. I don't, because I think token counts are a worse rehash of lines of code. Lines at least leave something behind that you can read. You can burn through a great many tokens and produce nothing of value at all.
<!-- src: theme-measurement note (Ant: "I'd argue that token bragging (both consumption and production) is actually a worse rehash of LoC which is why I don't use it. You can burn through a lot of tokens and it have no generation of value"). "Lines at least leave something behind that you can read" is the drafter's: Ant to agree -->

<!-- p: 20-06 | draft 2026-11-27 -->
On the day I wrote this, a physicist posted an eighty-three-page paper proposing a way to describe gravity with quantum mechanics. It hadn't yet been reviewed. Its acknowledgements credited an AI model with helping on calculations and proofs over several months, and about four hundred million tokens. That same week, my own account showed about three hundred million tokens used in seven days. Whether his paper is right is for physicists to judge. The point is that the two numbers say nothing about which piece of work was worth more.
<!-- src: theme-measurement note (Ant, 27 Nov 17:56, two screenshots: a newsletter item and his API console, last 7 days, about 303 million tokens, up 127%); news reports of the preprint, all 26 to 27 Nov 2026: The Rundown (83 pages, unreviewed, submitted to arXiv 25 Nov, credits GPT-6 Astra with help on calculations and proofs), Archyde ("Acknowledgments disclose roughly 400 million tokens of GPT-6 Astra compute provided by OpenAI"), Time News (calculations and proofs derived through months of iterative work). Before print: cite the paper itself (title and arXiv number differ between reports), and decide whether to name the physicist and the model. "On the day I wrote this" = 27 Nov, when it was reported; the paper was posted 25 Nov -->

<!-- p: 20-07 | draft 2026-11-27 -->
I'd guess they didn't have my caching rate, either. Eighty-eight per cent of what my runs sent last week was read back from a cache, which is much cheaper than sending it fresh. That's exactly the trouble with token counts. The same number can mean very different amounts of spend, and very different amounts of work.
<!-- src: theme-measurement note (Ant: "I doubt they had our cacheing rate"; console: prompt caching 88% hit rate, last 7 days). Explanation of caching is the drafter's: Ant to check. No money figures -->

<!-- p: 20-08 | draft 2026-11-27 -->
So I use tokens for what they're good at. They're a measure of spend, and of pace. When the week's use passes eighty-five per cent of my plan's limit, a brake comes on and the night runs ease off. Each piece of work is given a lane, so the expensive models only get the work that needs them. Those are decisions about how fast to go and what it costs. None of them is a claim about value.
<!-- src: theme-measurement note (Ant: "tokens are a better measure of expenditure (and again pacing) than of value"); r2jimmy decision model-lanes-2026-11-26 ("Model lanes per item, and a weekly plan brake at 85%"). "the night runs ease off" is the drafter's reading of the brake: check the decision's wording -->

<!-- p: 20-12 | draft 2026-11-27 -->
A measure that acts by itself needs its inputs watched. On the night of 26 November, the brake came on for the first shifts, because it read my week's plan use as ninety per cent. The real figure was thirty-six. Nothing was wrong with the rule. The number going into it was wrong, so for the first part of the night it slowed the work down for no reason at all. The more a number is trusted to make decisions on its own, the more it matters that someone can see what it's reading.
<!-- src: smoothey/jimmy governance/reports/2026-11-26/morning-brief.md ("The plan brake was on for the first shifts on a wrong 90% reading; Ant's real figure was 36% (00:05), and later shifts ran unbraked"); r2jimmy decision model-lanes-2026-11-26 (the 85% brake). Also told briefly in ch 6, 06-15: keep one full telling. The last two sentences are the drafter's -->

<!-- p: 20-09 | draft 2026-11-27 -->
Value needs a person. For this book, the most honest number is the ledger. For chapter one, I typed about two thousand and eighty words, and the agreed chapter has about two thousand two hundred. Roughly one to one. The AI didn't multiply my words. What it gave me was time, structure and a second pair of eyes, and only I can judge whether that made the book better.
<!-- src: briefs.md, Closing chapter (Ant, 22 Nov: chapter 1, "about 2,080 words typed by Ant, about 2,220 in the approved chapter, about 3.5 hours. The honest reading so far: about one to one on words; the leverage is time, quality and scaffolding"); PROCESS.md, Words in, words out. The closing chapter plans to use the final ledger: keep these two from repeating each other -->

<!-- p: 20-10 | draft 2026-11-27 -->
And every measure goes stale. Chapter 12 showed how changing the way you work changes what you should measure. Chapter 21 has a check that never failed, so its green light only ever meant "it ran". A number that was right last month can be quietly wrong today. So every so often I ask of each one: what is this actually telling me now?
<!-- src: chapter 12, 12-06 (draft: changing the method changes the metric); chapter 21, 21-16 (draft: a check that never fails stops being a check). The habit in the last sentence is the drafter's: Ant to confirm he does this, or cut -->

<!-- p: 20-11 | draft 2026-11-27 -->
Count whatever helps you see the pace. Trust only a few numbers to tell you about value, and expect a person to be behind most of them. And never let a measure of how fast you're going become the thing you're aiming for.
<!-- src: drafter's closing from 20-01 to 20-10. Ant to agree -->
