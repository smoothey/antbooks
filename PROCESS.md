# How we write a book (standard for Ant Smoothey Books)

Agreed by Ant on 21 Nov 2026 as the standard for every book that isn't an Ultra Transcenders title. We'll refine it as we go; changes are Ant's to agree.

## 1. Interview only when needed
Claude drafts from what it already has: the logs, the store, earlier interviews, decisions and notes. It interviews Ant only for detail it can't get from that context. Questions are few and specific, and say which chapter they're for.

Interview notes stay in the store (`r2antbooks` `notes/interviews/<book>/`), never in this repo.

## 2. Chapter headings and themes are agreed, then can change
The book's `outline.md` holds the agreed chapter headings and themes. Either of us can propose a change at any time: a new chapter, a merge, a move, a new theme. Nothing in the outline is frozen; it changes when Ant agrees.

## 3. Chapter reviews, a paragraph at a time
When either of us asks, we go through a chapter one paragraph at a time. For each paragraph Ant either approves it, or we agree an amendment and then it's approved.

Each step shows a sliding window, so the paragraph is read in context (Ant, 22 Nov 2026):
- the paragraph before it, for reference;
- the paragraph under review, with what's Ant's and what's Claude's wording;
- the paragraph after it, for reference.

Only the middle one is being agreed. If a change ripples into a neighbour, that neighbour is flagged and reviewed again in its turn.

## 4. Agreed paragraphs stay set
An agreed paragraph doesn't change unless:
- new context changes what it says (a fact turns out wrong, a story changes, Ant adds something), or
- a review reopens it.

Claude doesn't reword an agreed paragraph for style, and says when new context means one needs reopening.

How it's tracked: each paragraph in a chapter file has a marker on the line above it:

```
<!-- p: 01-03 | agreed 2026-11-22 -->
```

- `01-03` is chapter 1, paragraph 3. Ids stay put when paragraphs move.
- The state is `draft`, `agreed <date>` or `reopened <date>: <why>`.
- Only Ant's word moves a paragraph to `agreed`. Any change to an agreed paragraph's wording sets it back to `reopened`, with the reason.

## References
References go in the book's "Notes and further reading" section at the back, never as marks in the text (Ant, 22 Nov 2026). Notes are grouped by chapter and keyed by a short phrase. Add a chapter's notes when the chapter is written, each checked against a real source; the whole section is polished with the rest of the book.

## 5. Final polish
When the chapters are agreed, a polish reviewer reads the whole book. It may change wording, never intent.
- It writes its proposed changes chapter by chapter, in `books/<book>/polish/<chapter>.md`: each change as before, after, and why, in one line.
- Ant agrees them in bulk, chapter by chapter. He can strike any single change.
- Agreed polish changes go into the chapter. Those paragraphs stay agreed, because their intent hasn't changed.
- Anything that would change meaning isn't polish: it goes back to step 3 for that paragraph.
- The polish reviewer is a separate pass that hasn't written the draft, so the work isn't marking itself.

## Words in, words out
For each book we keep a ledger of how many words Ant typed against how many ended up in the book (Ant, 22 Nov 2026). At each chapter's approval, Claude counts Ant's messages that fed the chapter (content and direction), the approved chapter's words, the generated working text, and the time it took, and adds an entry to the store record `state/words-ledger-<book>` in `r2antbooks`. Chat replies aren't counted. The totals may feed the book's closing.

## Always
- Ant's voice, first person, plain words.
- Every fact has a source comment beside it (see CLAUDE.md).
- The never list in CLAUDE.md holds at every step, including interviews and polish.
