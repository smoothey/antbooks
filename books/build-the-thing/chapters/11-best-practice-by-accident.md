# Chapter 11: Best practice by accident

<!-- p: 11-01 | draft 2026-11-25 -->
A few weeks in, I looked at what Jimmy had become and recognised it. There was a backlog with codes, sizes and due dates. There were sprints. There were pull requests, reviews and a list of things that always wait for me. There was a daily report, a log of what went wrong, and a record of every decision and why we made it. It looked a lot like Azure DevOps, the tool the formal team in chapter 1 had run its work in. Only better, more targeted and more usable. None of that was the plan.
<!-- src: interview 2, follow-up 23:09 ("Jimmy resembles Azure DevOps, but better, more targeted and more usable. That was never an aim"); r2jimmy decisions backlog-dates (21 Oct), sizing-night-share (20 Oct), sprint-2026-10-20 and later sprint decisions; smoothey/jimmy governance/loops/merging.md (hold list); chapter 1 (agreed: the team run "very formally in Azure DevOps") -->

<!-- p: 11-02 | draft 2026-11-25 -->
I never sat down and said "let's do DevOps properly". Each piece arrived because something had just gone wrong, or was about to. A run built the same thing twice, so runs started reading the backlog first. A good change was undone by mistake, so we wrote down how to tell a real failure from a job that never started. Choices kept being questioned again later, so decisions got their own records, each with its reason. Each fix answered the problem in front of it. Only later did I notice that most of them already had names.
<!-- src: chapter 5, 05-05 (agreed: knowing where things stand "stops the same work being built twice"); r2jimmy lesson 2026-10-26-nightly-jimmy-1 (a job GitHub never started was read as a red main, and a good merge was reverted; merging.md section 4 changed); r2jimmy decision records from 18 Oct. The decision-records motive is the drafter's guess: see q -->
<!-- q: SB-6 11-02: why did decisions get their own records in the store? Replace the drafter's guess with the real reason -->

<!-- p: 11-03 | draft 2026-11-25 -->
That isn't how it's normally done. The textbook way is to pick a method first, set it up, and then do the work inside it. The team in chapter 1 did exactly that, and moved slowly. I've come to think the order matters more than the method. As I put it to Jimmy one evening: "I think we'd be slower if we started with them, but layering them on as we see the need is really keeping momentum."
<!-- src: interview 2, follow-up 23:09 (quote, lightly tidied in the store note; check exact words with Ant before print); chapter 1 (agreed: tiny tasks, slow pace). Keep this telling of the team short: brief says ch 1, intro, ch 3 and ch 11 each tell it differently -->

<!-- p: 11-04 | draft 2026-11-25 -->
It isn't new for me, either. Earlier chapters have already shown it three times. In chapter 1 I built an audit tool that listed everything we ran, before I'd heard of a configuration management database. In chapter 3 I built a stopgap for a crash and pushed for the real fix, which IT calls problem management. And in chapter 8 the brokers ended up as separation of duties, which I didn't set out to copy. Each time I solved the problem in front of me, and found the textbook name afterwards.
<!-- src: chapter 1, 01 audit tool paragraph (agreed: "before I'd even heard of ITIL or a configuration management database"); chapter 3, 03-05b and 03-05c (agreed: the Jade stopgap); chapter 8, 08-12 (agreed: "In IT this is called separation of duties. I didn't set out to copy it."); briefs.md ch 11 (refer back, don't retell) -->

<!-- p: 11-05 | draft 2026-11-25 -->
Here's what that list looks like now, set against the names the textbooks use.
<!-- figure: fig11-best-practice-by-accident goes after this paragraph. Its rows are a draft: agree them with Ant with this chapter (figures/README.md) -->

<!-- p: 11-06 | draft 2026-11-25 -->
Two of the habits I value most came from the firewall work, before Jimmy existed. The first is to pull before you build. Twice, a request arrived for a change the client had already half made themselves, in parallel, without telling anyone. Because the AI always read what was live before designing anything, the work got smaller instead of colliding. The night runs follow the same rule today. A run starts by taking stock, and it fetches the latest copy of anything it depends on before it pushes a change.
<!-- src: notes/source-material/build-the-thing/2026-11-21-client-azure-ops-ai-usage.md ("Pull before building. Twice the client had already built half of a request in parallel. Reading current state first made the work smaller."); interview 1b ("Step 2 was checking what already existed before designing anything. Requests were often half done already."); chapter 5, 05-05 (agreed); smoothey/jimmy governance/loops/CONTRACT.md ("Before any push, check the clock and fetch the branches you depend on") -->

<!-- p: 11-07 | draft 2026-11-25 -->
The second is to split a risky job so that a crash lands in the safe half. On that same client, two servers had to move to a different part of a data centre, and there was no way to move them in place. They had to be rebuilt. So the scripts came in two parts. The first part only prepared things: it added and copied, and could be undone. The second part did the cutover, the step you can't take back. If anything fell over halfway through the first part, we'd lost time, not data. Change managers would call that a rollback plan. To me it was just not wanting to explain to a client why their servers had gone.
<!-- src: client source note ("Design scripts so a crash lands in the safe half. Additive/reversible prepare split from destructive cutover meant every mid-run crash cost time, not data"; "A zone move that was really a rebuild ... staged prepare / cutover / rollback scripts plus a runbook"). Client kept anonymous; "a different part of a data centre" stands in for an availability zone: Ant to check the wording. Last sentence is the drafter's: Ant to confirm or replace -->

<!-- p: 11-08 | draft 2026-11-25 -->
The oddest one is user stories. In most teams, a user story comes first. Somebody writes "as a model, I want to pick my photos from my own folder, so that I don't have to upload them twice", and then the team builds it. On Charlie's site we did it the other way round. By 21 November the site already did a great deal, and nobody could say for certain what it did for whom. So we wrote the stories afterwards, each one in the user's own voice, and against each we noted what did it: an action, a page, a help screen. Or, where nothing did, we marked it as a gap.
<!-- src: smoothey/jimmy governance/stories/README.md (Ant, 21 Nov 2026: "Can we have a stories view on the hub too - other projects are going to need similar"; Charlie Doll started it, CD-933; stories carry wants, soThat, status covered/partly/gap/later, and proof); SB-1 themes ("user stories after the fact"). The example story is an illustration in the style of the real file, not quoted: Ant to agree or swap for a real one -->

<!-- p: 11-09 | draft 2026-11-25 -->
Written that way, a user story stops being a plan and becomes a check. It asks a question the code can't answer by itself: is there anyone this is for, and does it do what they need? The gaps became work for the night runs. And because the stories now sit on the Hub, every other project can use the same shape.
<!-- src: governance/stories/README.md (status gap; Hub Stories page reads docs/stories/stories.json; "the shared shape, so every project keeps the same file in the same place"). "The gaps became work for the night runs": Ant to confirm, or cut -->

<!-- p: 11-10 | draft 2026-11-25 -->
Arriving at a practice this way has one real advantage. You know why it exists, because you felt the pain it removes before you had it. Nobody had to persuade me that a run should read the backlog before it builds. I'd watched the same work get built twice. It's the difference between being told a stove is hot and having touched it. You don't forget, and you don't follow the rule for its own sake.
<!-- src: drafter's synthesis; chapter 5, 05-05 (agreed: knowing where things stand stops the same work being built twice). "I'd watched": Ant to confirm he saw it happen -->
<!-- q: SB-6 11-10: is there a better example of a practice you adopted only after feeling the pain? -->

<!-- p: 11-11 | draft 2026-11-25 -->
It has a cost too. Some wheels get reinvented. A few times we've built something by hand and found out later that it was a solved problem with a well-known shape. Now, when the same kind of trouble turns up twice, I ask what IT calls it, and read how other people solved it. Not to adopt their whole method. Just to borrow the part that fits.
<!-- src: drafter's reading; Ant to confirm the "ask what IT calls it" habit is his -->
<!-- q: SB-6 11-11: do you now look up the formal name when a problem repeats? An example would help (a wheel you reinvented, then found had a name) -->

<!-- p: 11-12 | draft 2026-11-25 -->
There's a pattern in which practices turned up and which didn't. Almost none of the ones that exist to share work out between people did. There was no one to hand tiny tasks to, so the elaborate business of handing them out never appeared. But every practice that exists to catch mistakes turned up, and early: reviews before anything goes live, a second look by something that didn't write the work, a freeze before a big moment, a record of what went wrong. When the AI does the work, coordinating people stops being the hard part. Being sure the work is right becomes the whole job.
<!-- src: drafter's synthesis from the fig11 list and chapters 5, 7 and 8; r2jimmy decision build-to-live-until-freeze and freeze-default-before (freezes); runs' independent reviews (r2jimmy JM-348 progress: "ran an independent review and fixed its five faults"). Ant to agree this reading; it is the chapter's main claim -->

<!-- p: 11-13 | draft 2026-11-25 -->
So if you're starting out, don't begin by choosing a method and filling in its forms. Begin by doing the work, with something that keeps a record of it. When something goes wrong, fix the cause and write down what you changed. When it goes wrong a second time, look up its name. The good practice will come. You'll just get to it by the shortest route, and you'll know why every piece of it is there.
<!-- src: drafter's closing; chapter 10 (draft: a lesson isn't learnt until it changes something). Check it doesn't pre-empt chapter 17 (Start small) -->
