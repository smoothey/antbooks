# Chapter 15: What you're actually talking to

<!--
First draft, 27 Nov 2026. Ant's theme (27 Nov 18:11): LLMs, intelligence and sentience and the distinctions, pragmatically; recognising the differences and frictions; when to speak normally and when to tailor the ask. Placed after ch 14 (Ant, 18:11). Source: store r2antbooks notes/interviews/build-the-thing/2026-11-27-theme-what-ai-is.md.
General background on how language models work (15-02) isn't from the store: it's plain, widely known background, kept deliberately simple. Ant to check the wording; any claim beyond it gets a cited source.
Sentience (15-04): say it's an open question; don't settle it.
Gap: a moment Ant was fooled into treating the AI as a person (15-11, answer later).
-->

<!-- p: 15-01 | draft 2026-11-27 -->
It's very easy to forget what you're talking to. The AI writes like a person. It says "I think". It apologises when it gets something wrong, makes the odd joke, and thanks me for a good idea. It has learnt from an enormous amount of human writing, so of course it sounds human. That's what makes it so pleasant to work with. It's also what makes it so easy to misjudge. One of the most useful things I've learnt is to keep three words apart: language model, intelligence and sentience.
<!-- src: theme note (Ant, 27 Nov 18:11: "AI mimics human traits so closely, it is easy to be fooled that you are dealing with a human"). The examples of human manner are the drafter's: Ant to agree -->

<!-- p: 15-02 | draft 2026-11-27 -->
A large language model is the thing itself. It has been trained on a vast amount of text to predict, again and again, what comes next. That sounds too simple to matter. But done at enormous scale, it turns into something that can explain, reason through a problem, write code and hold a conversation. Nothing in that description says it remembers you, knows what day it is, or wants anything.
<!-- src: general background (not from the store), kept deliberately plain: Ant to check the wording before print. Theme note (Ant: "LLMs, Inteligence and Sentience and the distinctions") -->

<!-- p: 15-03 | draft 2026-11-27 -->
Intelligence is a harder word, and I've stopped arguing about it. Whatever you call it, the AI does things that would look intelligent in a person. In chapter 14 it noticed backups nobody had looked at for seventeen months. But its intelligence is uneven in a way no colleague's would be. The same AI that can untangle three stacked causes of a fault will forget to tell me to fetch the latest code before I deploy, as chapter 16 showed. So I judge it by the result, task by task, not by the word.
<!-- src: chapter 14, 14-10 (draft: six machines unbacked for about seventeen months); store notes/source-material/build-the-thing/2026-11-21-client-azure-ops-ai-usage.md ("An LDAP auth failure turned out to be three stacked causes"); chapter 16, 16-02 and 16-03 (draft: deploying without pulling). "uneven in a way no colleague's would be" is the drafter's: Ant to agree -->

<!-- p: 15-04 | draft 2026-11-27 -->
Sentience is the hardest of the three: whether there's anything it feels like to be the AI. The honest answer is that nobody knows for certain, and serious people disagree. I don't need to settle it to work with it well. What I do need is to stop its human manner from making me assume it has human traits it doesn't. That's where most of the friction comes from.
<!-- src: theme note (Ant: sentience and the distinctions, "pragmatically"). The framing of sentience as an open question is deliberate (briefs.md ch 15): don't claim either way in print -->

<!-- p: 15-05 | draft 2026-11-27 -->
Here are the differences that have cost me most. It doesn't remember. Unless it's given the context, every new conversation starts from nothing, however friendly the last one was. Chapter 4 asked whether the AI is stupid or just missing context, and nine times out of ten it's the context. It doesn't know what time it is, either. Its picture of the world goes stale inside a single conversation: it doesn't know I've just merged something from my phone, as chapter 16 told.
<!-- src: chapter 4 (agreed: "Is the AI stupid, or missing context?"); store notes/interviews/build-the-thing/2026-11-22-theme-context.md; chapter 16, 16-04 and 16-05 (draft: the AI's picture goes stale; merging from a phone). "nine times out of ten" is an illustration, not a measure: Ant to agree or cut -->

<!-- p: 15-06 | draft 2026-11-27 -->
It has no feel for its own speed. Left to itself, it plans as though a team of people were doing the work, until it's shown its own pace, as chapter 3 described. It agrees too easily, and the more it knows about you, the more it agrees, which was chapter 13. And it sounds just as sure when it's wrong as when it's right. In chapter 14 it reported a job as failed with total confidence, and the job was fine.
<!-- src: chapter 3 (agreed: the borrowed pace); chapter 13 (agreed: AI built to fit your preferences; memory makes it agree more); chapter 14, 14-09 (draft: the false FAILED report) -->

<!-- p: 15-07 | draft 2026-11-27 -->
None of that makes it less useful. It means the person working with it has to fill the gaps a human colleague would fill without being asked. A colleague would say "hang on, has that been merged?" A colleague would know what day it is. The AI won't, unless you build that into how you work with it.
<!-- src: drafter's synthesis from 15-05 and 15-06; ties to chapter 16 (draft: the habits nobody writes down). Ant to agree -->

<!-- p: 15-08 | draft 2026-11-27 -->
So when do I just talk to it, and when do I change how I ask? My rule has two halves. The first is about the job. When I'm thinking, exploring an idea or making a decision, I talk normally, as I would to a colleague. I ask it to interview me, to argue the other side, to walk me through something. When it has to do work without me there, I tailor the ask: precise, written down, and something it can check. That's why the night runs read written rules before they start, and why the instructions say "check it live, not from memory".
<!-- src: theme note; Ant, 27 Nov 18:11 (picked both suggested rules: "Talk normally to explore and decide; tailor (precise, written down, checkable) when it has to do the work unattended", Claude's wording chosen by Ant); chapter 13, 13-13 (agreed: asking it to argue the other side); chapter 23 (draft: interview me, walk me through); smoothey/jimmy CLAUDE.md (check a pull request's state on GitHub now, never from memory); governance/loops/CONTRACT.md (runs read their runbook first) -->

<!-- p: 15-09 | draft 2026-11-27 -->
The second half is about who's listening. I talk normally to the main assistant I work with every day. When it's another AI, or a tool, the ask gets short and literal. Chapter 18 told how the image tool refused long, careful prompts, and did what it was asked with one line. That isn't rudeness. It's speaking the language the listener actually understands.
<!-- src: Ant, 27 Nov 18:11 (picked "Talk normally to the main assistant; tailor short and literal when it's another AI or a tool", Claude's wording chosen by Ant); chapter 18, 18-08 (draft: Gemini refused long prompts; one-liners went through). "That isn't rudeness" is the drafter's -->

<!-- p: 15-10 | draft 2026-11-27 -->
The best tailoring I've done is telling the AI what good looks like, in a form it can check. In chapter 12, version one of 3D Jimmy ticked every box I'd asked for and still looked wrong. The fix was a test anyone could apply: in a still, could you take him for the drawing at a glance? Once that test was written down, the AI had something to aim at that wasn't my mood.
<!-- src: chapter 12, 12-04 and 12-05 (draft: the test; the goal as first phrased). "that wasn't my mood" is the drafter's: Ant to agree -->

<!-- p: 15-11 | draft 2026-11-27 -->
[A moment you treated the AI like a person and it cost you, in your words.]
<!-- q: SB-6 15-11: a time you caught yourself treating the AI as if it were a person (assuming it remembered, trusting its tone, being polite instead of precise) and it cost you something -->

<!-- p: 15-12 | draft 2026-11-27 -->
So I try to treat it as what it is. Not a person, and not a calculator either. Something new, that's brilliant at some things, blind to others, and very good at sounding like one of us. The better I know where the differences are, the less they trip me up, and the more of its real ability I get to use.
<!-- src: drafter's closing. Ant to agree -->
