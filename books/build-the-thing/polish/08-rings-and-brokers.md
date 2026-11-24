# Polish: Chapter 8 (proposed 24 Nov 2026, separate reviewer)
Summary: The hardest chapter to make plain, and it mostly is. The two questions frame it well, and the summary in 08-12 lands. The proposals fix two unclear references ("the difference", "the parts ... it"), explain "identity" in plain words, and untangle one sentence about the merge broker's key. Two items need checking before print.

## Proposed changes
1. **08-03** — Before: "That's called prompt injection, and the AI can't always tell the difference." → After: "That's called prompt injection, and the AI can't always tell a slipped-in instruction from a real one." — Why: "the difference" has nothing clear to point back to.
2. **08-06** — Before: "The merge broker has its own identity, with no access to the store at all." → After: "The merge broker has its own identity, the account it acts as, with no access to the store at all." — Why: "identity" is a technical term here, and it's its first use.
3. **08-06** — Before: "It holds the key it needs to act on GitHub in a way that lets it use the key but never copy it out." → After: "It holds the key it needs to act on GitHub, stored so that it can use the key but never copy it out." — Why: "in a way that lets it" tangles the sentence, with three "it"s close together.
4. **08-09** — Before: "As I write, the parts are built and waiting for me to switch it on." → After: "As I write, its parts are built and waiting for me to switch it on." — Why: "the parts ... it" left unclear what "it" is; "its parts" ties both to the broker.

## Needs Ant (not polish)
- 08-09: "As I write, the parts are built and waiting for me to switch it on." The source says to check at review that it's still not switched on (JM-239 was due 27 Nov). Recheck before print.
- 08-12: the source comment asks whether "separation of duties" belongs here or in chapter 11 (Best practice by accident). A structure call, not wording.
- 08-13: the source comment points to "chapter 5, 05-xx"; the line is 05-06. Not printed, but worth fixing.
