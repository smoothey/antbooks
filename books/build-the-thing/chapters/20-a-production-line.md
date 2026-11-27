# Chapter 20: A production line, end to end

<!--
Never in print: the series name or the pen name (Ant, 22 Nov 01:43). Call it "a series of technical study guides I publish". No exam codes either, as they'd identify the series. Readers must not anchor on the pace: the lesson is the line, not the number (outline; Ant, 22 Nov 01:42). Figure fig16-production-line (filename kept from the old numbering) goes after 20-03.
-->

<!-- p: 20-01 | draft 2026-11-25 -->
Most of this book is about projects: things that get built, and then get better. But some work isn't a project. It's the same kind of thing, made again and again: a report every month, a newsletter every week, a release every sprint. For that kind of work, the thing that builds the things is a production line. This chapter follows one of mine from start to finish, and shows how it keeps changing.
<!-- src: outline ch 20 ("One repeating piece of work followed from idea to published product, and how the line keeps evolving"); briefs.md ch 20 ("Ends with a short checklist for any repeating output: a newsletter, client reports, releases") -->

<!-- p: 20-02 | draft 2026-11-25 -->
The example is a series of technical study guides I publish. Each one helps someone prepare for an IT certification exam. I'm not going to name them, because they aren't the point, and I'd rather you didn't fix on how many there are or how fast they come out. Your line will run at whatever pace your work needs. What's worth copying is the shape.
<!-- src: briefs.md ch 20 (in print: neither the series name nor the pen name; "Don't let readers anchor on the number ... the message is building a line that runs at whatever pace fits the work"); smoothey/antbooks CLAUDE.md ("Describe them as 'a series of technical study guides'") -->

<!-- p: 20-03 | draft 2026-11-25 -->
Every guide goes through the same seven steps. Research the exam. Plan the book. Write it, a chapter at a time. Check the facts and figures. Put everything needed to publish it into one proposed change. I approve it. It's published. The machine does every one of those steps but one. The one it doesn't do is mine.
<!-- src: figures/diagrams.py fig16-production-line (steps: Research the exam; Plan the book; Write it, chapter by chapter; Check facts and figures; One pull request to go live; I approve with one tap; Published; "the machine runs every step but one"). Not quite true today: Ant also uploads each book to the publisher himself (ultimatetranscender EDITIONS.md section 9: "Ant's part is the KDP upload and one tap to merge"). See 20-09 and q -->

<!-- p: 20-04 | draft 2026-11-25 -->
It starts with a shared source of material, built once and kept current. Every guide rests on the exam's published objectives and on the vendor's own documentation, never on blogs or memory. Rather than research those pages again for every book, the line keeps its own copy of every page the books rely on, and checks them all every night. When a page changes, it records what changed and which books cite it. So the research for a new book starts from a library, not a blank page, and an existing book can be checked against just the pages that moved.
<!-- src: smoothey/ultimatetranscender CORPUS.md ("The vendor pages the books rest on, kept current so a book is checked against what changed instead of being researched again. Agreed by Ant on 22 Oct 2026"; changes/<date>.jsonl "with the books that cite the page"); r2jimmy decision ut-nightly (22 Oct: "with a research corpus refreshed every night"); ultimatetranscender CLAUDE.md ("Facts come from the vendor's documentation, read in this session ... Never from memory, blogs, forums or course sites"). The vendors' own text is kept privately, never published (CORPUS.md: a private repo) -->

<!-- p: 20-05 | draft 2026-11-25 -->
That one decision changed the cost of keeping a book right. Technical documentation changes all the time. A feature gets renamed, a limit goes up, a service is retired. Without the shared source, every book is a snapshot that starts going stale the day it's published. With it, the line knows which sentence in which book rests on which page, and it can tell me exactly what needs checking.
<!-- src: CORPUS.md (books/<slug>.json: "The pages each section of a book rests on"; `impact`: "sections whose pages changed since checked_on"); BOOK-PREP.md step 1. "every book is a snapshot that starts going stale" is the drafter's: check -->

<!-- p: 20-06 | draft 2026-11-25 -->
The plan comes next. In October the line changed how a book begins. Now it starts from the exam's own list of what it tests, copied word for word, and an outline is built from that list before any chapter is written. Every fact in the finished book carries a note, hidden from the reader, saying which page it came from. That's the same rule this book follows. Every fact has a source beside it, or it doesn't go in.
<!-- src: ultimatetranscender OUTLINE-FIRST.md ("How a new ... book is written from the exam objectives and the vendor's documentation ... First used for [a VMware exam] ... October 2026"; step 1, objectives verbatim); ultimatetranscender CLAUDE.md ("Cite the URL in src lines"); smoothey/antbooks CLAUDE.md (every fact has a source comment). Exam code and vendor left out on purpose (they'd identify the series) -->

<!-- p: 20-07 | draft 2026-11-25 -->
Then the writing, and the checks. The night runs write the chapters, a little each night, from the outline and the shared source. Separate checks look at the finished book: that the links work, that the ebook file is valid, that the print version has the right number of pages for its cover. Before a book's publishing day, a night run goes back over it, and checks only the sections whose source pages have changed since the book was last checked. It doesn't re-read the whole book. It knows where to look.
<!-- src: r2jimmy decision ut-nightly (nightly pool, 5%); ultimatetranscender BOOK-PREP.md ("The nightly run ... preps the books due in the next 14 days, nearest first"; step 1 "What changed"; step 2 "Check those sections only"; step 5 checks: link_ebook.py, EPUBCheck, check_pdf.py, page count); chapter 5, 05-03 and 05-04 (agreed: the study guides' night run and share) -->

<!-- p: 20-08 | draft 2026-11-25 -->
Then comes the step I'm proudest of, because it's so plain. Each book goes live through one pull request. Everything that has to change to publish that book, from the shop page on my website to the book's own record, goes into that one proposed change. The open ones are the list of books on their way. My part is to upload the files to the publisher, and then tap once to merge. Nobody needs me to type in a number or copy anything across. The approval happens at exactly one point, and that point is obvious.
<!-- src: ultimatetranscender EDITIONS.md section 9 ("Going live ... one PR per book, UT-28, 27 Oct 2026": "Each book goes live through one pull request, its go-live PR"; "Open go-live PRs are the list of books on their way"; "Ant's part is the KDP upload and one tap to merge; nobody needs him to type an ID"); store.json entries (the website's book pages). "the shop page on my website" paraphrases store.json and the site build: check. -->

<!-- p: 20-09 | draft 2026-11-25 -->
That one tap isn't a formality. It's the only place where a person stands between the line and the public, and I want it that way. Night runs are allowed to prepare the change, but they're never allowed to merge it or fill in the publishing details. Those wait for a daytime chat, with me there.
<!-- src: EDITIONS.md section 9, step 6 ("Unattended runs never merge a go-live PR and never fill in ASINs or ISBNs. They may open the draft"); ultimatetranscender CLAUDE.md ("Scheduled and unattended runs never use the chat or go-live exceptions"). Links forward to ch 14 (what stays a human's job) -->

<!-- p: 20-10 | draft 2026-11-25 -->
The line also learns. On 25 October, two books were uploaded from files that weren't the latest build. It shouldn't have happened. The files I uploaded weren't the ones the line had just built and checked, and nothing in the step made sure they were. Now something does. Before the line tells me a book is ready, it writes the final file to the exact folder I upload from, reads it back, and checks the details on its copyright page and its page count. Only then does it say "ready".
<!-- src: EDITIONS.md section 9, step 2.4 ("Hard check before 'ready to upload': write the interior to where Ant uploads from ... then read that file back and check the ISBN on the copyright page and the page count against the cover wrap. Only then tell Ant it is ready to upload ... (two books were both uploaded from stale builds on 25 Oct; exam codes left out here)"). Exam codes left out. "weren't the ones the line had just built and checked" is the drafter's reading of "stale builds": check -->
<!-- q: SB-6 20-10: what happened after the two stale uploads on 25 Oct? Did readers see the old files, and how was it put right? A sentence on the outcome can go after "It shouldn't have happened" -->

<!-- p: 20-11 | draft 2026-11-25 -->
That's the pattern for every change to the line. Something goes wrong once. The fix goes into the step itself, not into a note beside it. Chapter 10 explained why that matters. A production line is the best place in the world to apply that lesson, because every fix is used again on every book that follows.
<!-- src: chapter 10 (draft: a lesson isn't learnt until it changes what the next run reads, a check, or the tool); EDITIONS.md (the stale-build fix is in the step itself) -->

<!-- p: 20-12 | draft 2026-11-25 -->
And the line keeps evolving. In its first weeks, it changed where its research comes from, how a book is planned, how a book is checked before it's published, and how it goes live. None of those changes was planned in advance. Each one came from a book that taught us something.
<!-- src: CORPUS.md (22 Oct); OUTLINE-FIRST.md (October 2026); BOOK-PREP.md (before an upload, check only what changed); EDITIONS.md section 9 (one PR per book, 27 Oct); figures/diagrams.py fig16 ("The line keeps changing: each book teaches the next one") -->
<!-- q: SB-6 20-12: what's changing in the line now? (briefs.md ch 20 gap) One or two current changes would make this paragraph concrete -->

<!-- p: 20-13 | draft 2026-11-25 -->
If you have a piece of work that repeats, here's the checklist I'd use to turn it into a line. What's the shared source, and can you build it once and keep it current instead of gathering it every time? What's the plan each piece starts from, and is it written down before the work begins? Which checks can a machine run on every piece, every time? Is there exactly one place where a person approves, and is it obvious what they're approving? When something goes wrong, does the fix go into the step, so the next piece can't repeat it? And is there a steady rhythm the line can hold, without you pushing it?
<!-- src: briefs.md ch 20 patterns ("a shared source of material built once (the research corpus); one controlled release step (one pull request per book); approval at exactly one point; a steady cadence the system holds; the line itself improves over time"; "Ends with a short checklist for any repeating output"). Could be set as a list at layout: Ant's call -->

<!-- p: 20-14 | draft 2026-11-25 -->
That works for a newsletter, for a monthly client report, for software releases. I've used it for study guides. The pace isn't the point. Mine runs at a pace that suits me, and yours should run at one that suits you. What makes it a line is that it keeps going when you stop pushing it, and gets a little better every time it runs.
<!-- src: briefs.md ch 20 ("Two books a week is not the message; the message is building a line that runs at whatever pace fits the work"). No count of books or weekly figure, on purpose -->
