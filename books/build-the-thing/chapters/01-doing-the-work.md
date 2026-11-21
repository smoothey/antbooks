# Chapter 1: Doing the work, and the ceiling it hits

<!-- p: 01-01 | draft -->
I was six when I fell in love with a computer. It belonged to my cousin: a Commodore VIC-20. I didn't so much want one as need one, and I nagged my parents about it for a year until they gave in.
<!-- src: interview 1, Q2 -->

<!-- p: 01-02 | draft -->
Even then, one machine wasn't enough. I used to hang around computer shops and write my own programs on whatever demo machines they had out: Commodores, Spectrums, Amstrads. I loved them all. I started where everyone started, filling the screen with Hello World over and over. GOTO was my friend. Later, on the Commodore 64, I used its graphics keys to make bugs walk across the screen, with brackets for legs, and balls that bounced off the edges.
<!-- src: interview 1 follow-ups, notes/interviews/build-the-thing/2026-11-21-interview-1b.md -->

<!-- p: 01-03 | draft -->
Those bugs taught me the feeling this whole book is about. You write something down, the machine does it, and it keeps doing it after you've stopped. A loop. A few lines of instructions, and the screen is busy without you. I didn't have words for it then, but I've been chasing that feeling ever since.

<!-- p: 01-04 | draft -->
Decades later, computers are still my job. I work in infrastructure, networks and cloud platforms, mostly Azure. But when I'm honest about my own projects, the ones I did in my own time, the answer for most of those years is simple. I did little.
<!-- src: interview 1, Q1 ("I did little"); profile (Azure, infrastructure and networking) -->

<!-- p: 01-05 | draft -->
The most useful thing I'd ever written for myself was AzureDump. It started in 2002 as a VBScript I wrote to document the infrastructure at a financial sector company I worked at. Over the years it grew into a cloud tool. I kept expecting it to be made pointless by something public and polished, and every so often something came along that looked like it might. Each time, my tool still did things the others didn't.
<!-- src: interview 1, Q1; Ant, 21 Nov 2026: AzureDump is his own IP and can be named -->

<!-- p: 01-06 | draft -->
It was also getting harder and harder to keep going. Every change was mine to make, by hand, in the evenings. There was a list of features I knew it needed, and the list didn't get shorter. It just sat there, a reminder of how little time I had compared with how much I wanted to build.
<!-- src: interview 1, Q1 -->

<!-- p: 01-07 | draft -->
AzureDump wasn't the only one. In 2019 I built a bot called Ophelia. She lived in Discord, and I wrote her by hand in Node, using a Microsoft language service called LUIS to understand what people typed. She could search for images, but her real job was tasks: she let me and my partner at the time share the running of day-to-day jobs, with both of us able to see what was done and what wasn't.
<!-- src: interview 2, Q1 and follow-up -->

<!-- p: 01-08 | draft -->
I still have a message I posted for friends in January 2019, walking them through how to teach Ophelia something new. Log in. Create an intent. Name it properly. Type in examples of what people might say. Train it, publish it. And the last step: "Once done, give Ant the nod and he can write the code to recognise it."
<!-- src: Ant's screenshot of the 12 Jan 2019 walkthrough (URL and key not reproduced) -->

<!-- p: 01-09 | draft -->
Reading that now, it's the whole problem in one line. Everything waited on me. Other people could describe what they wanted, but nothing happened until I found the time to write it. I wanted to turn Ophelia into something anyone could use. I never had the bandwidth. The service she was built on has since been retired, and she went with it.
<!-- src: interview 2 follow-up; Ant, 21 Nov 2026 (LUIS retired, project retired) -->

<!-- p: 01-10 | draft -->
That was the pattern for years. The limit wasn't ideas, and it wasn't skill. It was hours. Every idea had to pass through one person with a day job, and that person was the narrowest part of the pipe. Working harder made the pipe a little wider for a while. It never changed its shape.

<!-- p: 01-11 | draft -->
My first real taste of AI at work came when I was seconded into a Data & AI team at a previous employer. I was careful with it. At first I only asked it to help me troubleshoot. Later I let it track down problems, but only ones I was confident I understood and could fix myself in time if it went wrong. Some colleagues used it to explain how code worked. I've always been strong at reading code, so that wasn't where it helped me.
<!-- src: interview 1, Q2 -->

<!-- p: 01-12 | draft -->
Where it did help was in writing the scripts. I started getting AI to write discovery and troubleshooting scripts for client problems. It was faster, and it let me work on more than one thing at once. My theories weren't always right. Its theories weren't always right either. But between us we generally turned days of troubleshooting into hours, and my clients got the benefit.
<!-- src: interview 1, Q3 -->

<!-- p: 01-13 | draft -->
I was called in on one customer's firewall changes when the consultants who usually looked after it weren't around. I didn't know their setup, and a single change could take me a few hours. So I wrote down how the work should be done, step by step, and gave the AI a place to keep what it learned about that customer between jobs. After that, a change took minutes. And it worked the way I work: it fitted in with what was already there, and challenged it when something wasn't right. I didn't know it yet, but that was the idea behind everything that came later.
<!-- src: interview 1 follow-ups (firewall before and after); notes/source-material/build-the-thing/2026-11-21-client-azure-ops-ai-usage.md; client not named -->

<!-- p: 01-14 | draft -->
Meanwhile, the team I was part of decided to build its own deployment tool with AI. I worked on some of its parts. It was one big Python program that, when you looked closely, mostly handed out templates. Nobody in the team knew Python well. It could just as easily have been PowerShell, and I genuinely don't think anyone stopped to ask what it should be written in. It was run very formally in Azure DevOps, broken into tiny tasks and handed out to individuals. Many of those tasks were things the AI could have finished in minutes.
<!-- src: interview 1 follow-ups ("Lacked ambition") -->

<!-- p: 01-15 | draft -->
I found it frustrating, and it took me a while to say why. The team had the same AI I had. But it was using it to do the old way of working a bit faster: the same small tasks, the same hand-offs, the same pace. The project lacked ambition. Not because the people lacked talent, but because nobody had asked how different the work could be now.
<!-- src: interview 1, Q2 -->

<!-- p: 01-16 | draft -->
Then the job changed. I took voluntary redundancy and quickly found a new role. Somewhere in that change, I finally asked myself the question I'd been circling: where is the ceiling, really? From the middle of October 2026, I set myself a challenge. Keep improving, all the time, and put AI first.
<!-- src: interview 1, Q2 -->

<!-- p: 01-17 | draft -->
I didn't start with a grand plan. I was skint, and I wanted to make Charlie, my partner, a present. A website for her modelling seemed the obvious thing. I expected to write a good chunk of the code myself and let the AI help. That isn't what happened. Before long I wasn't building a website. I was building the thing that would build it.
<!-- src: interview 1 follow-ups (mid October); Ant, 21 Nov 2026 (Charlie happy to be in the story; "skint" can go in) -->
