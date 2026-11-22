# Chapter 4: One place for the truth

<!-- p: 04-01 | agreed 2026-11-22 -->
AI sometimes says stupid things. Anyone who has used it for more than an afternoon has seen it: a confident answer that ignores something obvious, a plan that breaks a rule you agreed an hour ago, a fix for a problem you solved last week. For a long time I took that as a limit of the tool. Then I started asking a different question. Is it stupid, or has nobody given it the right context?
<!-- src: notes/interviews/build-the-thing/2026-11-22-theme-context.md (Ant, 22 Nov 00:38: "AI sometimes says stupid things. But is it stupid, or just not given the right context?") -->
<!-- rev: agreed by Ant 22 Nov 18:50 (as is) -->

<!-- p: 04-02 | agreed 2026-11-22 -->
Most of the time, it's the context. Think of the cleverest new colleague you've ever had, on their first morning. They know their trade inside out, and they know nothing about your place: what you've already tried, what the customer hates, which system falls over if you touch it. Every new chat with an AI is that first morning. Unless you give it what it needs to know, it will fill the gaps with sensible guesses, and some of those guesses will look stupid.
<!-- src: theme note (context); Claude's analogy, offered for Ant to accept -->
<!-- rev: agreed by Ant 22 Nov 18:50 -->

<!-- p: 04-03 | agreed 2026-11-22 -->
Here's an example from the week before we revealed Charlie's site. Releases were about to be frozen, and as we planned around the freeze, the AI kept asking me the same question about item after item: should this go before the freeze, or after? I gave the same answer every time. It felt like talking to someone who wasn't listening. But it wasn't stupid. Each chat started fresh, and my answer had never gone anywhere the next one could see. So on 24 October we wrote it down as a standing rule: before the freeze by default, unless there's a good reason not to. The question stopped.
<!-- src: Jimmy project chat "Jimmy dashboard draft PRs", 24 Oct 2026 (Ant frustrated at being repeatedly asked "before or after the freeze?" with a consistent answer; standing rule "before the freeze by default" approved, "it's perfect"); r2jimmy notes/freeze-timing-rule-proposal-2026-10-25.md -->
<!-- rev: agreed by Ant 22 Nov 18:49 -->

<!-- p: 04-03b | agreed 2026-11-22 -->
The same evening, I mentioned I'd be away from 1 to 13 November. The AI marked my time away as a freeze on all work. It was a sensible guess, and it was wrong. Being away didn't mean nothing could happen. It meant I'd have about two hours a day, on a laptop or my phone. Once I'd said so, that went into the store as the standard for any time away, so no chat would have to guess again.
<!-- src: same chat, 24 Oct 2026 (away 1 to 13 Nov first marked as a freeze; Ant: not a freeze but reduced access, about 2 hours a day on an internet-connected laptop or phone, the standard assumption for future away periods; away records updated to a 120-minutes-a-day budget) -->
<!-- rev: agreed by Ant 22 Nov 18:49 -->

<!-- p: 04-03c | agreed 2026-11-22 -->
It helps to know what "context" means to an AI. When it answers, it can only use what's in front of it at that moment: your message, the conversation so far, and any files, notes or instructions it has been given. That's its context. It doesn't carry anything over from one chat to the next unless something feeds it back in, and there's a limit to how much it can hold at once. When a long piece of work fills that space, older details start to drop out. So the question is never just whether the AI is clever enough. It's whether the right things are in front of it when it needs them.
<!-- src: Claude's plain explanation of an AI's context (and the context window); added at Ant's request, agreed as written 22 Nov 18:51 -->

<!-- p: 04-04 | agreed 2026-11-22 -->
Before the store, the context lived in three places, and none of them was good enough. Some of it was in old chats, which a new chat couldn't see. Some of it was in the AI's own memory, which I couldn't easily see, check or correct. And most of it was in my head, which meant I was the one typing it out again every time. Chapter 2 told how that pushed me to build the store. This chapter is about what it became.
<!-- src: interview 1b ("a lot of value sits in memories and isn't always visible to the person using the AI"); chapter 2, 02-05 (agreed) -->
<!-- rev: last sentence changed to avoid repeating 02-05; agreed by Ant 22 Nov 18:53 -->

<!-- p: 04-05 | agreed 2026-11-22 -->
It became the one place for the truth. It holds a small number of kinds of thing, and each has a plain job. The backlog is the list of work still to do, with every item given a short code, such as JM-458. A progress record says where a project is today and what it needs from me. Decisions record what we agreed and why, so nobody argues the same point twice. Lessons record what went wrong and what we changed. Run reports say what happened each night. And messages let one chat ask another for something, the way colleagues leave each other notes.
<!-- src: ADR 0002 (record kinds: backlog, state, run, message, loop, grant, decision, lesson, event); Jimmy Store connector instructions (codes such as UT-1 given by the store; needsAnt asks in the progress record) -->
<!-- rev: 'It became', example code JM-458 (this book's first backlog item, r2jimmy); agreed by Ant 22 Nov 18:55 -->

<!-- p: 04-06 | agreed 2026-11-22 -->
I built it in my own Azure account, not inside any one AI product, and that was deliberate. If I change assistant, or plan, or the product changes under me, the store is still there. I can read it myself, without any AI in the way. The backups are mine, and so are the rules about who can see what. Scripts and other tools can reach it, not just chats. The price is that I now run a small service of my own, and its health is my job.
<!-- src: ADR 0002 (context: state lived in claude.ai, tied to one vendor's product, no backups Ant controlled; consequences: survives a change of assistant or plan, Ant can read it directly, backups and access rules are his; "Bad: Ant now runs a service") -->
<!-- rev: agreed by Ant 22 Nov 18:56 -->

<!-- p: 04-07 | agreed 2026-11-22 -->
It has three front doors onto the same truth. One is for the AI: the MCP connection from chapter 2, which lets any of my chats read and write. One is for scripts and devices. And one is a web page for me, the Hub. Whichever door you come in by, you see the same records, under the same rules. A night run, a daytime chat and I all look at the same backlog, so nobody is working from an old copy.
<!-- src: ADR 0002 (three front doors on one router and one policy: /mcp for Claude, REST /v1 for scripts and devices, the Jimmy Hub site; "one source of truth") -->
<!-- rev: agreed by Ant 22 Nov 18:58; figure fig04 goes after this paragraph -->

<!-- p: 04-08 | agreed 2026-11-22 -->
Having one place also raises a problem you don't get with notes in your head: two workers changing the same thing at once. A night run and a daytime chat might both update the same progress record within a minute of each other. If the second one simply overwrote the first, work would vanish without anyone noticing. So every change says, in effect, "only save this if the record still looks the way I last saw it." If someone else got there first, the change is refused, the worker reads the new version, and tries again.
<!-- src: ADR 0002 ("etag-checked writes"); Jimmy Store connector instructions (expected_etag: "only change it if it still has this etag ... otherwise you get a conflict") -->
<!-- rev: agreed by Ant 22 Nov 18:59 -->

<!-- p: 04-09 | agreed 2026-11-22 -->
Privacy needed the same kind of care, built in rather than hoped for. The store holds very different things: my own notes, things Charlie and I share, and project work that other people may one day see. I didn't want the line between them to depend on an AI remembering a rule, because a rule that only lives in what you tell an AI can be talked round. So the lines are built into the store itself. Each part has a privacy ring, and the store checks every request against it, whatever the AI has been told. Chapter 8 goes into how that works.
<!-- src: ADR 0003 (rings; "A rule that lives only in a prompt ... can be talked round"; "enforced in the store's code ... never in what a model is told") -->
<!-- rev: new opening; agreed by Ant 22 Nov 19:00 -->

<!-- p: 04-10 | agreed 2026-11-22 -->
I'd seen what one place for the truth could do before I built it. On the firewall work in chapter 1, the AI kept notes about that customer between jobs: what the network looked like, how they named things, what had gone wrong before. Each new session started already knowing all that, instead of rediscovering it. And when the AI hit a trap once, the trap went into the notes, so it didn't fall into it again. Looking back at that work, the conclusion I wrote down was simple: memory is what made it compound.
<!-- src: notes/source-material/build-the-thing/2026-11-21-client-azure-ops-ai-usage.md ("Project memory carried state between sessions ... Each new session started primed instead of re-discovering the estate"; "Memory is what made it compound. Banked gotchas ... stopped repeat mistakes across sessions"); chapter 1, 01-13 (agreed) -->
<!-- rev: 'I wrote down' kept, confirmed by Ant 22 Nov 19:02 -->

<!-- p: 04-11 | agreed 2026-11-22 -->
The store does the same for everything. When a chat starts work on Charlie's site, it reads the site's progress record and backlog before it does anything else. It knows what's been done, what's waiting, and what's waiting on me. When it finishes, it writes back what changed, so the next chat, or the next night, starts from where it left off rather than from nothing. Every piece of work leaves the store a little more complete than it found it.
<!-- src: project instructions (Ultra Transcenders project: "Write state/progress there whenever you work on it; keep open items there as backlog"); Jimmy Store connector instructions -->
<!-- rev: Charlie's site example confirmed by Ant 22 Nov 19:03 -->

<!-- p: 04-12 | agreed 2026-11-22 -->
That's why I now think good context management drives AI productivity more than anything else. Clever wording in a prompt helps a little, once. The right context, kept in one place where every chat and every run can reach it, helps every time. If an AI keeps getting something wrong, my first question isn't "how do I word this better?" It's "what doesn't it know?" More often than not, the answer belongs in the store.
<!-- src: theme note (Ant: "Good context management really drives AI productivity"); introduction, 00-04 (agreed: clever wording mattered far less) -->
<!-- rev: agreed by Ant 22 Nov 19:05 -->

<!-- p: 04-13 | agreed 2026-11-22 -->
One place for the truth also has to know what it must never hold. Passwords, keys and other secrets never go in. Neither does anything from clients' systems, or other people's private details. Each project has its own short list of things that never go in the store, a report or a change, and every chat and run is told it at the start. Knowing what to leave out is as much a part of good context as knowing what to put in.
<!-- src: Jimmy project register ("never" list on every project); ADR 0003 ("Client data never goes in the store"); Jimmy Store connector instructions (never-store rules) -->
<!-- rev: agreed by Ant 22 Nov 19:06 (as is) -->

<!-- p: 04-14 | agreed 2026-11-22 -->
With the store in place, the AI stopped starting every morning as a stranger. It knew the work, the rules and the history, and it could pick up where the last worker had stopped. That raised an obvious question. If it could carry on from where I'd left off, did it need me there at all while it worked? The next chapter is about the nights.
<!-- src: bridge to ch 5, Work while you sleep -->
<!-- rev: 'left off'; agreed by Ant 22 Nov 19:19 -->

