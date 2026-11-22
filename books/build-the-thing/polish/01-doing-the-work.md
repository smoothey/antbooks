# Polish: Chapter 1 (proposed, not applied)
Summary: The prose is in good shape: plain, first person, with a strong voice and a clear thread from the VIC-20 to the Charlie present. Most of the proposals explain technical terms on first use (the CLAUDE.md rule), as the chapter assumes an IT reader in places. The rest fix a few unclear pronouns, number style, "learnt" and "client" consistency, and one dangling clause. Small tidy, not a wording change: there is a stray double blank line after 01-24.

## Proposed changes
1. **01-02** — Before: "GOTO was my friend." → After: "GOTO, the command that sends a program back to an earlier line, was my friend." — Why: explains a technical term the first time it appears.
2. **01-02** — Before: "My sister technically got the television it plugged into, as her present." → After: "Technically, my sister's present was the television it plugged into." — Why: shorter, and the joke lands at the end.
3. **01-25** — Before: "make my own bugs walk across the screen, with brackets for legs, and balls that bounced around it" → After: "make my own bugs, with brackets for legs, walk across the screen, and balls bounce around it" — Why: as written, the balls seem to have the brackets for legs.
4. **01-03** — Before: "Those bugs taught me" → After: "Those walking bugs taught me" — Why: in a book about programming, "bugs" on its own reads as software errors.
5. **01-18** — Before: "But it forced me to understand" → After: "It also forced me to understand" — Why: removes a second contrast straight after "though".
6. **01-19** — Before: "When I was 17," → After: "When I was seventeen," — Why: matches "six" and "sixteen" elsewhere in the chapter.
7. **01-21** — Before: "teaching NT4 and networking courses" → After: "teaching Windows NT4 and networking courses" — Why: "NT4" means nothing to a general reader without the product name.
8. **01-22** — Before: "it could be scripted." → After: "it could be scripted: run from a written list of instructions instead of by hand." — Why: explains "scripted" on first use, and it is the point of the paragraph.
9. **01-22** — Before: "Each machine got hidden partitions on its hard drive that could" → After: "Each machine's hard drive got hidden sections, called partitions, that could" — Why: explains a technical term.
10. **01-23** — Before: "They were a testing centre too, and they gave me" → After: "The company was also a testing centre, and they gave me" — Why: "They" now follows "competitors" and the DVD installs, so it is unclear who is meant.
11. **01-23** — Before: "my MCSE exams for free. On the back of how things went, they also paid for my MCSD, in Visual Basic 6." → After: "my MCSE exams, Microsoft's certification for systems engineers, for free. On the back of how things went, they also paid for my MCSD, the developer equivalent, in Visual Basic 6." — Why: explains two acronyms a general reader won't know.
12. **01-23** — Before: "But I'd learned something" → After: "But I'd learnt something" — Why: the chapter uses "learnt" elsewhere (01-24, 01-25).
13. **01-05** — Before: "a VBScript with a simple HTA front end that let me check" → After: "a script, written in VBScript, with a simple point-and-click front end that let me check" — Why: plain words for the tool. "HTA" goes because the new words describe it. Ant may prefer to keep "(an HTA)" after "front end".
14. **01-05** — Before: "we had a hard DMZ and even some air-gapped servers that nothing else could reach" → After: "we had a hard DMZ (a walled-off part of the network facing the outside world) and even some air-gapped servers, physically cut off from other networks, that nothing else could reach" — Why: explains two technical terms.
15. **01-05** — Before: "before I'd even heard of ITIL or a configuration management database." → After: "before I'd even heard of ITIL or a configuration management database, the formal ways IT departments keep track of what they run." — Why: explains the terms without adding a claim.
16. **01-26** — Before: "It wasn't the only one." → After: "That audit tool wasn't the only thing I built there." — Why: after the AzureDump detour, "one" has no clear referent.
17. **01-07** — Before: "she let me and my partner at the time share" → After: "she let my partner at the time and me share" — Why: grammar.
18. **01-08** — Before: "a message I posted for her in January 2019" → After: "a message I posted for my partner in January 2019" — Why: the nearest "she" is Ophelia, so "her" reads as the bot.
19. **01-09** — Before: "She could describe what she wanted" → After: "My partner could describe what she wanted" — Why: the same ambiguity between Ophelia and the partner.
20. **01-12** — Before: "Where it did help was in writing the scripts." → After: "Where it did help was in writing scripts." — Why: "the scripts" points back to nothing.
21. **01-13** — Before: "I was called in on one customer's firewall changes" → After: "I was called in on one client's firewall changes" — Why: the chapter says "client" everywhere else (01-12).
22. **01-13** — Before: "a place to keep what it learned about that customer" → After: "a place to keep what it learnt about that client" — Why: consistent "learnt" and "client".
23. **01-14** — Before: "It could just as easily have been PowerShell," → After: "It could just as easily have been PowerShell, Microsoft's own scripting language," — Why: explains a tool name on first use.
24. **01-14** — Before: "It was run very formally in Azure DevOps, broken" → After: "It was run very formally in Azure DevOps (Microsoft's tool for planning and tracking software work), broken" — Why: explains a tool name on first use.

## Needs Ant (not polish)
- 01-24: The comparative advantage paragraph sits between the GCSE homework (01-18) and bridge (01-19). Those two both lead into 01-20 ("I've worked that way ever since"), so 01-24 breaks that thread and jumps decades ahead before we go back to age seventeen. Consider moving it to after 01-20, or after 01-19.
- 01-24: The plain-terms gloss ("whatever adds the most value", not "whatever you're best at") is loose. Ricardo's idea is about relative cost: doing what you give up least to do. An economist reader may quibble. Ch 3 expands on it, but the wording here is Ant's call. Also, "game changer" sits a little oddly beside "At sixteen it was just an idea that made sense".
- 01-21 / 01-22: 01-21 says he "ended up doing consultancy, and teaching", then 01-22 ends saying the time he got back "is what let me start my consultancy and teaching career". The same outcome is told twice, in a slightly circular way. Decide where it belongs.
- 01-05: "made pointless by something public and polished". Does "public" mean free and publicly available, or commercial? The right wording depends on which he means.
- 01-04 to 01-07: The story jumps from the data centre years (from 2002) to Ophelia (2019), then to the Data & AI secondment, with nothing on the years between. That's fine if intended. If not, it is a gap a reader may notice.
- 01-17: The source comment says "(mid October)", but 01-16 and the introduction now say mid September. The text gives no date, so nothing is wrong on the page. Check the comment and the timeline: the challenge started mid September, the first night ran on 18 Oct, so when did the Charlie present start?

## Narrative notes for later chapters
- "Where is the ceiling, really?" opens the introduction (00-01) and comes back almost word for word in 01-16. It works as a callback, but don't use it a third time early on.
- "Building the thing that builds/saves" appears in 00-02, 01-17 and 01-23 before ch 2, which carries it as its title. Watch for overuse.
- 00-03 "didn't start out as anything grand" and 01-17 "I didn't start with a grand plan" echo each other closely.
- Comparative advantage (01-24) and "usually the best developer" (01-11) set up ch 3's "value moves from best developer to vision and design". Ch 3 must pay these off.
- The firewall story (01-13) is called "the idea behind everything that came later". Ch 2 is its bridge, so it should build on it, not retell it.
- The Ophelia walkthrough's last line ("give Ant the nod...") is set up for the 2019 against 2026 comparison in ch 2.
- AzureDump's feature list "didn't get shorter" (01-06). A later chapter should say whether it finally did, or the reader is left hanging.
- The "loop" feeling (01-03) sets up the night runs (ch 5). "Loop" is also the system's own term later, so it needs a glossary entry.
- The team working in "tiny tasks" at the old pace (01-14, 01-15) overlaps with the borrowed pace in the introduction (00-05), ch 3 and ch 11's tiny-tasks contrast. Keep each telling distinct.
- The chapter ends with the Charlie present (mid September challenge). Ch 2 opens on the first night (18 Oct), so ch 2 should bridge the weeks between.
