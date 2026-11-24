# Chapter 8: Rings and brokers

<!-- p: 08-01 | agreed 2026-11-23 -->
A system that works for you while you sleep has to answer two questions before you can trust it. Who can see what? And who can do what? Chapter 4 promised I'd explain how I answered the first. This chapter does that, and then the second, because the second is where the real danger is.
<!-- src: chapter 4, 04-09 (agreed: "Chapter 8 goes into how that works"); ADR 0003 (rings); ADR 0009 and 0010 (powers) -->

<!-- p: 08-02 | agreed 2026-11-23 -->
Who can see what is decided by rings. Every part of the store belongs to one. Ring 0 is me alone, and it can never be shared with anyone. Ring 1 is me and people I name, like Charlie, for the things we share at home. A child in the family has a ring of her own beside it, in a separate account, shared only with her guardians and me. Ring 2 is a project, and anyone working on that project. Ring 3 is the public, and the public never touches the store at all: it only sees what's been published. My work notes sit apart again, in their own storage, reachable only through my work sign-in.
<!-- src: ADR 0003, Decision table (ring 0 Ant only, never granted; ring 1 Ant and named people, r1household; ring 2 a project's people; work w2, Ant's work identity; ring 3 public, no store access, published content only). Child ring: one neutral line, no name (Ant, 23 Nov 23:42); ADR 0003 and ADR 0015 (c1, a child, her guardians and Ant, never granted, own account) -->

<!-- p: 08-03 | agreed 2026-11-24 -->
The important part is where those lines are drawn. It would have been easy to write "never show ring 0 to anyone" into the AI's instructions and leave it there. But a rule that only lives in the instructions can be talked round. The AI reads a lot of text written by other people and other runs: notes, web pages, the descriptions on pull requests. Any of it could carry an instruction of its own, slipped in on purpose or by accident. That's called prompt injection, and the AI can't always tell a slipped-in instruction from a real one. So the rings aren't a rule the AI follows. They're a check the store makes on every request, based on who is asking, whatever the AI has been told.
<!-- src: ADR 0003, Context ("A rule that lives only in a prompt ... can be talked round by prompt injection, a confused model or a bug in a tool. The boundary has to hold whatever the model is told"); Decision ("enforced in the store's code ... checked on every request ... never in what a model is told"); ADR 0009, Context (Jimmy reads text written by runs and chats; "That text can carry instructions") -->

<!-- p: 08-04 | agreed 2026-11-24 -->
Ring 0 goes further. It lives in a separate store of its own, with its own locks, and so do my work notes. That way, one wrong setting can't open them up by mistake. The payoff is simple: an AI that has been confused or tricked still can't read anything the person it's working for can't reach. The cost is that anything showing everything at once, like my morning brief, has to ask each part separately and leave ring 0 out unless I ask for it.
<!-- src: ADR 0003, Decision ("Ring 0 is a separate storage account, and so are work compartments, so those lines are access boundaries, not naming rules"); Alternatives ("one wrong role assignment exposes ring 0"); Consequences (good: "a jailbroken or confused assistant still can't read what the caller's token can't reach"; bad: progress page and brief must query each compartment and leave ring 0 out unless the owner asks) -->

<!-- rev: 24 Nov 00:01, Ant: plainer, 'a separate store of its own, with its own locks'; agreed -->

<!-- p: 08-05 | agreed 2026-11-24 -->
Who can do what is the harder question. Three powers matter most: shipping code to a live website, changing the cloud services everything runs on, and spending money. Any of them, in the wrong hands, could do real damage while I'm asleep. And there was a trap waiting. The store, the thing that knows everything, can read every ring. If I'd also given it the power to ship code, my most private notes and the power to change live sites would have sat behind one door.
<!-- src: ADR 0009, Context ("Giving the same app the power to merge would put the most private data and the power to ship code behind one door"; merges that deploy); ADR 0010 (Azure changes); ADR 0014 (credit, spend) -->

<!-- p: 08-06 | agreed 2026-11-24 -->
So each dangerous power got its own broker: a small, separate program whose only job is to do that one thing, and only when I say so. The first was for merges, the step that accepts a pull request and, for some projects, puts it live. The merge broker has its own identity, the account it acts as, with no access to the store at all. It holds the key it needs to act on GitHub, stored so that it can use the key but never copy it out. And it can only merge for projects on its list.
<!-- src: ADR 0009, Decision 1 (separate Function App, own managed identity, no rights on the store's storage; "It does one thing"); Decision 2 (GitHub App key "non-exportable" in Key Vault, signs but never leaves); Decision 5 (allow-list follows project tiers) -->

<!-- p: 08-07 | agreed 2026-11-24 -->
I don't approve a merge on the Hub. The Hub only shows me a card with a button, and the button opens the broker's own page. That page reads the facts straight from GitHub, never from Jimmy or the store: what the change is, which files it touches, whether its checks passed, whether it will put something live. So even if the Hub were broken into, or Jimmy followed some injected text, the worst it could do is show me a misleading card. The broker's page always shows what's really there, and nothing merges without my tap on it.
<!-- src: ADR 0009, Decision 3 ("The card is where the approval starts; the broker's page is where it is given"; reads facts from GitHub itself; "a Hub that has been broken into, or Jimmy following injected text, can at most show Ant a wrong card ... only Ant's tap merges") -->

<!-- p: 08-08 | agreed 2026-11-24 -->
I wanted a second check, but not a code for every merge. So the first time each day, the broker asks me to sign in and confirm with my face or fingerprint on my phone. After that, each merge for the next twelve hours is one tap. The riskiest kinds still ask for my face every time: anything that changes how the code is deployed, who can sign in, or what the runs are allowed to do. Later I added batches: one list of the night's safe changes, one approval for the lot, with anything risky kept off the list.
<!-- src: ADR 0009, Context ("Ant wants a second factor, but not a code for every merge (22 Oct, 10:43)"); Decision 4 (Microsoft sign-in and a passkey once a day, 12-hour session; "Face ID every time for the riskiest kinds", Ant 22 Oct 10:56: workflows, deployment, sign-in, permissions, what runs may do); Amendment 2 and JM-348 (batch with one passkey, Ant 3 Nov; risky kinds never in a batch; done 20 Nov on Ant's word) -->

<!-- p: 08-09 | agreed 2026-11-24 -->
The cloud got the same treatment. Changing the services in Azure, the cloud my projects run on, is the second power, and it has its own broker, built on the same pattern but kept apart from the first. They share the code for signing in, but nothing else: not an identity, not a key. That way, breaking into one doesn't give you both. As I write, its parts are built and waiting for me to switch it on. Until then, those changes are scripts I run myself, signed in as me.
<!-- src: ADR 0010, Decision 1 (separate func-jimmy-infra; "It is not the merge broker ... Keeping them apart means a break-in to one doesn't give both. They share the sign-in and passkey code ... not an identity, an app or a Key Vault"); Context (scripts Ant runs from his PC, signed in as himself); JM-239 (status doing, 20 Nov: apply and guards built on pull requests, due 27 Nov). CHECK at review: still not switched on -->

<!-- p: 08-10 | agreed 2026-11-24 -->
The third power is money. I have two kinds of capacity to spend. My Claude plan pays for the night runs. A separate pot of credit pays for extra runs and quick jobs, and it lapses if I don't use it. A third broker decides where each piece of work goes: the cheapest capacity that's allowed to take it. Allowed is the important word. Where the data lives decides what may run where, so my most private work only goes down routes built to keep it apart. That rule has a story of its own, which I'll come to in chapter 13.
<!-- src: ADR 0014, Context (plan pays nightly runs; API credit lapses if unused); title ("Work goes to the cheapest capacity that may take it"); Decision ("Where the data lives decides what may run where", routes-by-storage, each ring its own workspace and key). Chapter 13, 13-09 to 13-12 (agreed: the routes-by-storage story). No money figures -->

<!-- p: 08-11 | agreed 2026-11-24 -->
Some limits apply whichever way the work goes. The runs paid from credit never put anything live, and never give themselves new schedules, secrets or powers. And a short list of changes always waits for me, however the work was paid for: anything touching how things are deployed, who can do what, or the rules the runs themselves follow.
<!-- src: ADR 0014, Decision ("The hold list, the never list and freezes bind every route. Credit runs never deploy, and never add schedules, secrets or powers"); smoothey/jimmy governance/loops/merging.md (hold list) -->

<!-- p: 08-12 | agreed 2026-11-24 -->
Put together, it's one idea used three times. A power, and the data it could misuse, never sit in the same place. The facts I approve are read fresh, at the moment I approve them, from the real source. And for anything that matters, the last step is a person: me. In IT this is called separation of duties. I didn't set out to copy it. It's what you end up with once you ask, for every power, what happens if the thing holding it is tricked.
<!-- src: summary of 08-05 to 08-11 (ADR 0009, 0010, 0014); "separation of duties" is the standard term (no source needed beyond general knowledge; check at polish whether ch 11, Best practice by accident, should carry it instead) -->

<!-- p: 08-13 | agreed 2026-11-24 -->
None of this is free. Every merge costs me a tap, and some cost a look at my face. It would be quicker to let the runs do it all. That trade is deliberate, and chapter 14 explains why I've chosen to keep it, even when it slows me down.
<!-- src: chapter 5, 05-06 (agreed: "every pull request costs me a tap"); briefs ch 8 ("approvals and rings are the mechanics of the restraint ch 14 explains"); theme note holding back on access (Ant, 22 Nov 02:26) -->
