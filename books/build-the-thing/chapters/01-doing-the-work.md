# Chapter 1: Doing the work, and the ceiling it hits

<!-- p: 01-01 | draft -->
I was six when I fell in love with a computer. It belonged to my cousin: a Commodore VIC-20. I didn't so much want one as need one, and I nagged my parents about it for a year until they gave in.
<!-- src: interview 1, Q2 -->

<!-- p: 01-02 | draft -->
Even then, one machine wasn't enough. I used to hang around computer shops and write my own programs on whatever demo machines they had out: Commodores, Spectrums, Amstrads. I loved them all. I started where everyone started, filling the screen with Hello World over and over. GOTO was my friend. Later, on the Commodore 64, I used its graphics keys to make bugs walk across the screen, with brackets for legs, and balls that bounced off the edges.
<!-- src: interview 1 follow-ups, notes/interviews/build-the-thing/2026-11-21-interview-1b.md -->

<!-- p: 01-03 | draft -->
Those bugs taught me the feeling this whole book is about. You write something down, the machine does it, and it keeps doing it after you've stopped. A loop. A few lines of instructions, and the screen is busy without you. I didn't have words for it then, but I've been chasing that feeling ever since.

<!-- p: 01-18 | draft -->
At school I kept turning homework into software. For some of my GCSE assignments I wrote computer programs instead of just doing the coursework. Writing the program was almost certainly more work than the assignment itself, though the program listings in my appendices did look impressive. But it forced me to understand the subject properly. You can't write code for something you only half understand.
<!-- src: early years note, notes/interviews/build-the-thing/2026-11-22-early-years-and-game-theory.md -->

<!-- p: 01-24 | draft -->
School gave me one more thing I didn't value until much later. In Economics GCSE I came across an idea that turned my thinking upside down. I'd always assumed I should spend my time on whatever I was best at. The lesson was that what matters is where you add the most value, and those aren't always the same thing. Among the people I worked with I was usually the best developer. It would take a very different kind of tool before I understood what that lesson meant for me.
<!-- src: early years note (Economics GCSE, 22 Nov 00:11); name of the idea to confirm with Ant -->

<!-- p: 01-19 | draft -->
When I was 17, my mother lost her bridge partner and asked if I'd play with her the following week. I knew nothing about bridge. So I got some books from the library, read them, and started writing my own bridge programs on my Amiga 500, in a language called AMOS. The programs were limited. But to write them I had to understand the game, and a week later my mother and I placed in the top ten per cent. Nobody believed it was the first time I'd played. With humans, at least.
<!-- src: early years note (bridge at 17); check before print: his mother happy to be in it -->

<!-- p: 01-20 | draft -->
I've worked that way ever since, and it's exactly how I work with AI now. I have to be able to say clearly what I'm trying to achieve, just as I had to understand bridge to program it. The difference is that the AI makes it a conversation. I still have to understand the problem. I no longer have to do all of the typing.
<!-- src: early years note ("AI for me is the same way") -->

<!-- p: 01-21 | draft -->
I always wanted to be a programmer. My career took me a different way. During my software development degree I did a paid placement with a company in Brussels, in 2000. They spotted something in me early: I ended up doing consultancy, and teaching NT4 and networking courses. I was also responsible for setting up the classrooms, and that was where the real lesson was.
<!-- src: early years note (Brussels placement, 2000); employer not named -->

<!-- p: 01-22 | draft -->
Setting up a classroom for a course meant following a binder, step by step, machine by machine. It took hours, and it was the same hours every time. So I looked at the tools available, picked a disk imaging tool, and automated it. Each machine got hidden partitions on its hard drive that could put a course back in place on demand. Where a setup couldn't be made general enough for that, I built DVD-based installs instead. Hours became minutes. The time I got back is what let me start my consultancy and teaching career.
<!-- src: early years note; exact tool name to confirm with Ant ("Power Image Pro") -->

<!-- p: 01-23 | draft -->
They were a testing centre too, and they gave me my MCSE exams for free. On the back of how things went, they also paid for my MCSD, in Visual Basic 6. When I graduated they offered me a career there. I turned it down, because by then I'd met the woman who would become my wife. But I'd learned something I didn't fully notice at the time: the best use of my hours was building the thing that saved them.
<!-- src: early years note; check before print: the line about meeting his wife-to-be -->

<!-- p: 01-04 | draft -->
Since then my work has been in infrastructure, networks and cloud platforms, mostly Azure. But when I'm honest about my own projects, the ones I did in my own time, the answer for most of those years is simple. I did little.
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
