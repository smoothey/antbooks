# Chapter 20b: Spending tokens well

<!--
First draft, 28 Nov 2026. Ant's theme (27 Nov 23:47): "techniques for managing token useage (including caveman prompting ...) ... how prompt cacheing works, how to choose a model etc"; agreed as a chapter of its own (23:48), placed after ch 14. Store note r2antbooks notes/plans/build-the-thing/2026-11-27-theme-token-use.md.
PLACEMENT NOT AGREED: filed as 20b so it sits after ch 20 (Measuring the right thing) and before ch 21 (What it costs), the drafter's suggestion. Paragraph ids 20b-nn are provisional; renumber the file, the ids and later cross-references once Ant agrees where it goes.
Ch 20 already has the 88% caching rate and "tokens measure spend, not value"; ch 26 has routing between models; ch 4 has what context is; ch 5 (05-14) has lanes and the 85% brake. Point back; don't retell. No money figures, ours or a price list's: prices as fractions only.
Outside sources (cite the originals, not news write-ups): Anthropic's prompt caching documentation (platform.claude.com/docs/en/build-with-claude/prompt-caching, read 28 Nov 2026); JetBrains AI blog, Denis Shiryaev, "Does Speaking to Agents Like Cavemen Really Save 65% of Tokens? We Test" (July 2026, blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/). Check both again before print.
-->

<!-- p: 20b-01 | draft 2026-11-28 -->
Chapter 20 said that tokens measure spend, not value. This chapter is about spending them well. A token is a piece of a word, and it's how an AI counts its work: every word you send it, and every word it sends back, is counted in tokens. Plans and price lists are set in them, and so are the limits. So it's worth knowing where they go, and which habits waste them.
<!-- src: chapter 20, 20-05 and 20-08 (draft: tokens measure spend and pace, not value); Ant, 27 Nov 23:47 (the theme). Definition of a token: general; Anthropic's documentation counts input, output and cache use in tokens -->

<!-- p: 20b-02 | draft 2026-11-28 -->
I'm terse by nature, and it turns out that suits AI. Most of my messages are a few words long. When the AI has laid out what it's about to do, I say "crack on", or "make it so", or "proceed", and it does. When we reviewed chapter 9 of this book, a paragraph at a time, most of my replies were one word: "approve". The night I write this, a whole chapter was agreed that way in half an hour.
<!-- src: Ant, 27 Nov 23:47 ("i tend to be on the terse side anyone and we are set up so if I say "make it so", "proceed", "crack on" etc you understand the intent"); the ch 9 review in the Jimmy Hub chat, 27 Nov 21:38 to 22:07 (most replies "approve" or "approved"); store notes/interviews/build-the-thing/2026-11-27-ch9-confidences.md -->

<!-- p: 20b-03 | draft 2026-11-28 -->
A short word only works because of everything that came before it. "Crack on" isn't an instruction. It's a hand-over. The AI already has the plan, the record, the rules and the reasons, because chapter 4's store put them in front of it. What it's waiting for isn't more detail. It's my go-ahead. So the real work of a short message is done long before I type it: in the context, and in the way the AI sets up the choice. When it offers me two options and a third, "answer later", from chapter 23, my reply can be one word because the thinking is already on the screen.
<!-- src: Ant, 27 Nov 23:47 ("because you have the context already you just need the handoff"); chapter 4, 04-03c and 04-12 (agreed: what context is; the right context in one place); chapter 23 (draft: two suggested answers and "answer later") -->

<!-- p: 20b-04 | draft 2026-11-28 -->
That's also how it goes wrong. In a brand new chat with nothing behind it, "crack on" means nothing, and the AI will guess. And a short question can get a confident answer from stale context. The same night we reviewed chapter 9, I asked which chapter was the earliest with paragraphs still to agree. The answer came back as chapter 9, taken from the book's plan. It was wrong. Chapters 5 to 8 had each gained a paragraph or two that day, and the plan hadn't caught up. We only found out because I asked a second short question, how many paragraphs were written, and that one was counted from the chapters themselves. A short question is fine. The answer still has to come from the live source, not a note about it.
<!-- src: Jimmy Hub chat, 27 Nov 20:58 (Ant: "what is the earliest chapter that needs paragraphs still approving"; answer ch 9 from claude/ant-smoothey-books.md) and 23:42 ("how many paragraphs are written"; count from the chapter files found 05-14, 06-15, 07-13, 07-14, 08-14, 08-15 still drafts); the plan doc now says to check the markers, not the doc. The last two sentences are the drafter's -->

<!-- p: 20b-05 | draft 2026-11-28 -->
There's a fashion for this, and it has a name: caveman prompting. The idea is to make the AI talk like a caveman, dropping the little words, the politeness and the padding, so there are fewer tokens to pay for. One popular add-on that does it claimed to cut the AI's output by about two thirds. In July, JetBrains, a company that makes tools for programmers, tested that claim properly, on eighty-six real coding tasks. With the add-on forced on every time, the saving was about eight and a half per cent, and nothing got worse. Most of what an AI produces in real work is code and commands, which the add-on leaves alone. The big saving only showed up in chatty answers.
<!-- src: JetBrains AI blog, Denis Shiryaev, July 2026 ("Advertised saving: 65%. Measured saving: 8.5%"; 86 of 87 SkillsBench tasks, Claude Code, paired; forced activation is the ceiling; no quality loss). Check the wording and figures against the post before print -->

<!-- p: 20b-06 | draft 2026-11-28 -->
I like that test, because it's chapter 20 in miniature: a striking number that didn't hold up once someone measured it on real work. And it points at the bigger truth. My short messages save a little, but that isn't really why I write them. They save my time. The tokens that matter are somewhere else.
<!-- src: chapter 20 (draft: measure on real work; pace against value); drafter's framing from Ant's 23:47 theme: Ant to agree that his terseness is about time more than tokens -->
<!-- q: is that right? Is being terse mostly about your time, or do you do it to save tokens too? -->

<!-- p: 20b-07 | draft 2026-11-28 -->
Here's where they go. Each time I send a message, the AI doesn't just get my message. It gets everything again: its instructions, the tools it can use, the files it has read, and the whole conversation so far. My "approve" might be one token. What goes with it might be a hundred thousand. So the length of my message barely matters. The length of the conversation, and how much is loaded into it, matters a lot.
<!-- src: Anthropic prompt caching documentation (a request carries tools, system and messages, in that order; input counted as cache reads, cache writes and uncached input). "A hundred thousand" is illustrative, not a measured figure: Ant to agree, or swap for a real one from the console -->

<!-- p: 20b-08 | draft 2026-11-28 -->
That would be ruinous if it were sent fresh every time. It isn't, because of prompt caching. When a request starts exactly the same way as one sent a few minutes earlier, the service can keep that opening part and read it back instead of working through it again. Reading it back costs about a tenth of sending it fresh, and less than that on some models. The first time costs a little more, to store it. The cache lasts five minutes by default, and each use resets the clock. There's an hour-long option too, which costs more to store.
<!-- src: Anthropic prompt caching documentation, read 28 Nov 2026 (caches the prefix; "Cache hits require 100 percent identical prompt segments"; cache read 0.1x base input, 0.05x on Opus 5.5 and Sonnet 5.5; 5-minute write 1.25x, 1-hour write 2x; default 5 minutes, "refreshed for no additional cost each time the cached content is used"). Prices as fractions only -->

<!-- p: 20b-09 | draft 2026-11-28 -->
The catch is in the word "exactly". The cache only matches from the start, in order: first the tools, then the instructions, then the conversation. Change something near the start, and everything after it has to be sent fresh again. So the things that never change go first, and the things that do go last. A time stamp at the top of the instructions sounds harmless. It means nothing after it ever matches.
<!-- src: Anthropic prompt caching documentation (order tools, system, messages; "a change at one level invalidates that level and everything after it"; "Put static content ... first, and varying content ... last"; a breakpoint on content that changes every request, "such as a timestamp", never hits) -->

<!-- p: 20b-10 | draft 2026-11-28 -->
That's most of the reason for the caching rate in chapter 20. My night runs all start the same way. Each one reads the same rules, then its own project's record, then gets to work, and the rules don't change during the night. Changes to the rules happen in the daytime, and I merge them. A run that reads the same long opening as the one before it pays for most of it at the cheap rate. Nobody designed the rules for the cache. It came from wanting every run to start from the same agreed place, and the cache rewarded it.
<!-- src: chapter 20, 20-07 (draft: 88% read from cache last week); smoothey/jimmy governance/loops/nightly-common.md (1. Set up and take stock: every run reads the rules and its record first); CLAUDE.md in the Jimmy Hub project: changes that touch governance are Ant's to merge. "Nobody designed the rules for the cache" is the drafter's reading: Ant to agree -->

<!-- p: 20b-11 | draft 2026-11-28 -->
Long sessions are the other drain. Every message in a long conversation carries the whole conversation with it, so the hundredth message costs far more than the first, even when it says less. And chapter 4 explained that an AI can only hold so much at once. Near the limit, it gets worse as well as dearer: older details start to drop out. So a fresh session with a good hand-over is often both cheaper and sharper than carrying on. That's why the night shifts on Charlie's site run as a relay, each one picking up the last one's notes, as chapter 21 tells.
<!-- src: chapter 4, 04-03c (agreed: the limit on what it can hold; older details drop out); chapter 21, 21-04 and 21-05 (draft: shifts stopped on context; relay shifts with hand-overs); Anthropic prompt caching documentation (each request carries the conversation so far) -->

<!-- p: 20b-12 | draft 2026-11-28 -->
The cheapest token is the one you never need to send. Every time I re-explain something, I pay for it twice: once in tokens, and once in my own time. Write it down once, in one place, and every chat and every run can read it without me. That's the store again, and it's the same habit as being terse. Say it properly once, then say very little.
<!-- src: chapter 4, 04-12 (agreed: the right context kept in one place helps every time); Ant, 27 Nov 23:47 (context already there; just the hand-over). The closing two sentences are the drafter's -->

<!-- p: 20b-13 | draft 2026-11-28 -->
Then there's choosing a model. Chapter 26 tells how work is routed between models and my own computers. In day-to-day use the choice is simpler. The most capable models are for judgement, and for long, careful work on code. Small, quick models are for looking things up, sorting and tidying. And how hard a model thinks is a choice too. Thinking costs tokens, so a quick tidy-up doesn't need the AI to deliberate. That's what the lanes from chapter 5 are: each piece of work says which model should do it and how hard it should think, set by the chat that knows the work best.
<!-- src: chapter 26 (draft: routing; the cheapest capacity that's allowed; helper models under a stronger lead); chapter 5, 05-14 (agreed: lanes, model and effort, set item by item); r2jimmy decision model-lanes-2026-11-26 -->
<!-- q: do you ever pick a model by hand in a chat, and when? A line from you would make this paragraph yours -->

<!-- p: 20b-14 | draft 2026-11-28 -->
The output can be managed as well as the input. I don't need a page when a line will do, so I ask for the short version. Reviewing a paragraph at a time keeps every turn small: three paragraphs on the screen, one word back. And a question with suggested answers gets a reply in seconds, where an open one could take a page from either of us.
<!-- src: chapter 23 (draft: a paragraph at a time, with the one before and after; two suggested answers and "answer later"); PROCESS.md step 3. Drafter's paragraph: Ant to agree -->

<!-- p: 20b-15 | draft 2026-11-28 -->
And if all that fails, there's the brake. When the week's use passes eighty-five per cent of my plan's limit, the night runs take only light work. I'd rather never reach it. The habits in this chapter are what keep me below it, and the brake is there for the weeks they don't.
<!-- src: chapter 5, 05-14 (agreed: the 85% brake); r2jimmy decision model-lanes-2026-11-26. The wrong 90% reading is told in ch 20 (20-12): don't retell -->

<!-- p: 20b-16 | draft 2026-11-28 -->
So here's what I'd pass on. Put the effort into the context, not the message. Keep what never changes at the start, so the cache can do its job. Start fresh sessions with a good hand-over rather than letting one grow forever. Match the model, and how hard it thinks, to the job. And then say as little as you need. When everything else is right, "crack on" is all it takes.
<!-- src: summary of 20b-03 to 20b-15; Ant's words (23:47). Drafter's closing: Ant to agree -->
