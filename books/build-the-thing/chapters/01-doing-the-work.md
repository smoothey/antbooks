# Chapter 1: Doing the work, and the ceiling it hits

<!-- p: 01-01 | agreed 2026-11-22 -->
I was six when I fell in love with a computer. It belonged to my cousin: a Commodore VIC-20. I wanted one of my own more than anything, and I nagged my parents about it for a whole year.
<!-- src: interview 1, Q2; review 22 Nov 00:21 and 00:23 -->

<!-- p: 01-02 | agreed 2026-11-22 -->
I didn't wait for them to say yes. I used to hang around computer shops and write my own programs on whatever demo machines they had out: Commodores, Spectrums, Amstrads. I loved them all. I filled their screens with Hello World, over and over. GOTO, the command that sends a program back to an earlier line, was my friend. That's what changed my parents' minds. They could see this wasn't just a child wanting the latest thing. It was someone who would do something with it, maybe even make a future of it. They bought me a Commodore 64. It was the most expensive present they ever gave me. Technically, my sister's present was the television it plugged into.
<!-- src: interview 1 follow-ups; review 22 Nov 00:21 and 00:23 (shops before owning a computer; first computer a C64; most expensive present; sister got the telly) -->

<!-- p: 01-25 | agreed 2026-11-22 -->
The Commodore 64's manual turned out to be full of program listings. I typed every one of them in, line by line, and I grew and learnt with each one. Before long I was using the 64's graphics keys to make my own bugs, with brackets for legs, walk across the screen, and balls bounce around it. Later I discovered Input, a magazine that printed listings for every home computer of its day. I still have the full set. It's one of my prized possessions, even if it's no use to anyone now. You typed those listings in line by line too, and heaven help you if you forgot to save. That's how I learnt to program: by copying out other people's instructions until I understood them well enough to write my own.
<!-- src: interview 1 follow-ups (C64 graphics keys, bugs, bouncing balls); review 22 Nov 00:27 (C64 manual listings typed in line by line; Input magazine, full set kept; forgetting to save) -->

<!-- p: 01-03 | agreed 2026-11-22 -->
Those walking bugs taught me the feeling this whole book is about. You write something down, the machine does it, and it keeps doing it after you've stopped. A loop. A few lines of instructions, and the screen is busy without you. I didn't have words for it then, but I've been chasing that feeling ever since.

<!-- p: 01-18 | agreed 2026-11-22 -->
At school I kept turning homework into software. For some of my GCSE assignments I wrote computer programs instead of just doing the coursework. Writing the program was almost certainly more work than the assignment itself, though the program listings in my appendices did look impressive. It also forced me to understand the subject properly. You can't write code for something you only half understand.
<!-- src: early years note, notes/interviews/build-the-thing/2026-11-22-early-years-and-game-theory.md -->

<!-- p: 01-19 | agreed 2026-11-22 -->
When I was seventeen, my mother lost her bridge partner and asked if I'd play with her the following week. I knew nothing about bridge. So I got some books from the library, read them, and started writing my own bridge programs on my Amiga 500, in a language called AMOS. The programs were limited. But to write them I had to understand the game, and a week later my mother and I placed in the top ten per cent. Nobody believed it was the first time I'd played. With humans, at least.
<!-- src: early years note (bridge at 17); Ant, 22 Nov 00:15: his mother can be named -->

<!-- p: 01-20 | agreed 2026-11-22 -->
I've worked that way ever since, and it's exactly how I work with AI now. I have to be able to frame clearly what I'm trying to achieve, just as I had to understand bridge to program it. The difference is that the AI makes it a conversation. I still have to understand the problem. I no longer have to do all of the typing.
<!-- src: early years note ("AI for me is the same way") -->

<!-- p: 01-24 | agreed 2026-11-22 -->
School gave me one more thing, and it was a game changer. In Economics GCSE I learnt about comparative advantage, an idea the economist David Ricardo set out in 1817. In plain terms: you shouldn't spend your time on whatever you're best at, but on whatever adds the most value, because those aren't always the same thing. I'd always assumed the opposite. At sixteen it was just an idea that made sense. It would be decades, and a very different kind of tool, before I understood what it meant for me.
<!-- src: early years note (Economics GCSE, 22 Nov 00:11); review 22 Nov 00:31: name the theory here; comparative advantage (Ricardo, On the Principles of Political Economy and Taxation, 1817); ch 3 expands it -->

<!-- p: 01-21 | agreed 2026-11-22 -->
I always wanted to be a programmer. My career took me a different way. During my software development degree I did a paid placement with a company in Brussels, in 2000. They spotted something in me early: I ended up doing consultancy, and teaching Windows NT4 and networking courses. I was also responsible for setting up the classrooms, and that was where the real lesson was.
<!-- src: early years note (Brussels placement, 2000); employer not named -->

<!-- p: 01-22 | agreed 2026-11-22 -->
Setting up a classroom for a course meant following a binder, step by step, machine by machine. It took hours, and it was the same hours every time. So I looked at the tools available for copying whole disks. They were all immature then. I picked PowerQuest's Drive Image Pro, even though it wasn't the market leader, for one reason: unlike its competitors, it could be scripted, so it ran from a written list of instructions instead of by hand. Each machine's hard drive got hidden sections, called partitions, that could put a course back in place on demand. Where a setup couldn't be made general enough for that, I built DVD-based installs instead. Hours became minutes, and the time I got back went into the consultancy and teaching.
<!-- src: early years note; Ant, 22 Nov 00:15 (Drive Image Pro, chosen because it was scriptable); polish question 3 agreed 22 Nov 01:21 (ending reworded) -->

<!-- p: 01-23 | agreed 2026-11-22 -->
The company was also a testing centre, and they gave me my MCSE exams, Microsoft's certification for systems engineers, for free. On the back of how things went, they also paid for my MCSD, the developer equivalent, in Visual Basic 6. When I graduated they offered me a career there. I turned it down, because by then I'd met the woman who would become my wife. But I'd learnt something I didn't fully notice at the time: the best use of my hours was building the thing that saved them.
<!-- src: early years note; Ant, 22 Nov 00:15: OK to mention meeting his wife-to-be -->

<!-- p: 01-04 | agreed 2026-11-22 -->
Since then my work has been in infrastructure and networks, and later cloud platforms: Azure and AWS. In 2002 I joined a financial sector company as a senior technician, and went on to become its data centre manager. I did a lot of work in those years. Progress was just hard.
<!-- src: review 22 Nov 00:47 (Azure and AWS; senior technician to data centre manager; "I did loads of work, progress was hard"), notes/interviews/build-the-thing/2026-11-22-career-and-own-time.md; employer not named -->

<!-- p: 01-05 | agreed 2026-11-22 -->
The most useful thing I built there was an audit tool: a script, written in VBScript, with a simple point-and-click front end that let me check our whole infrastructure. It could run from a floppy disk, which mattered: we had a hard DMZ (a walled-off part of the network facing the outside world) and even some air-gapped servers, physically cut off from other networks, that nothing else could reach. It gave me one consolidated view of everything we ran. I built it because I needed it, before I'd even heard of ITIL or a configuration management database, the formal ways IT departments keep track of what they run. Cloud computing didn't exist yet, and virtualisation was in its infancy. Years later, once the cloud arrived, that tool grew into something I called AzureDump. I kept expecting it to be made pointless by free tools other people published, mostly on the PowerShell Gallery, and every so often something came along that looked like it might. Each time, my tool still did things the others didn't.
<!-- src: interview 1, Q1; review 22 Nov 00:47 (VBS with HTA front end, ran from floppy, DMZ and air-gapped servers, consolidated view, before ITIL and CMDBs); review 22 Nov 00:53 (no cloud in 2002, virtualisation in its infancy; AzureDump is the later name); Ant, 21 Nov 2026: AzureDump is his own IP and can be named -->

<!-- p: 01-26 | agreed 2026-11-22 -->
That audit tool wasn't the only thing I built there. I also built Metis, an intranet site with a floor plan of the office. Click on any PC and you could see its live state, wake it up, patch it, and see who'd used it recently. In many ways it was more useful than the official system-management software we had, and I'd installed that too.
<!-- src: review 22 Nov 00:47 and 00:53 (Metis: floor plan intranet; more useful than SCCM, which he also installed) -->

<!-- p: 01-06 | agreed 2026-11-22 -->
There was a catch, and it took me years to see it clearly. To get that kind of value, I was spending my own time on work I couldn't fit into my working day. The tools did save time once they existed, but I paid for them in evenings. And keeping them going got harder every year. Every change to those tools, and later to AzureDump, was mine to make, by hand. There was a list of features I knew AzureDump needed, and the list didn't get shorter.
<!-- src: review 22 Nov 00:47 ("burning my personal time on work tasks... it still helped free time but at a personal cost"); interview 1, Q1 (hard to maintain, features put off) -->

<!-- p: 01-07 | agreed 2026-11-22 -->
Not everything I built was for work. In 2019 I built a bot called Ophelia. She lived in Discord, and I wrote her by hand in Node, using a Microsoft language service called LUIS to understand what people typed. She could search for images, but her real job was tasks: she let my partner at the time and me share the running of day-to-day jobs, with both of us able to see what was done and what wasn't.
<!-- src: interview 2, Q1 and follow-up -->

<!-- p: 01-08 | agreed 2026-11-22 -->
I still have a message I posted for my partner in January 2019, walking her through how to teach Ophelia something new. Log in. Create an intent. Name it properly. Type in examples of what people might say. Train it, publish it. Looking back, that was the clever part. LUIS let someone who couldn't program shape a tool we both used. I could hand part of the work over. But not all of it. The last step read: "Once done, give Ant the nod and he can write the code to recognise it."
<!-- src: Ant's screenshot of the 12 Jan 2019 walkthrough (URL and key not reproduced); review 22 Nov 01:01 (posted for his partner; LUIS let a non-programmer contribute: delegation) -->

<!-- p: 01-09 | agreed 2026-11-22 -->
Reading that now, it's the whole problem in one line. However much I handed over, the last step always waited on me. My partner could describe what she wanted, but nothing happened until I found the time to write it. I wanted to turn Ophelia into something anyone could use. I never had the bandwidth. The service she was built on has since been retired, and she went with it.
<!-- src: interview 2 follow-up; Ant, 21 Nov 2026 (LUIS retired, project retired) -->

<!-- p: 01-10 | agreed 2026-11-22 -->
That was the pattern for years. The limit wasn't ideas, and it wasn't skill. It was hours. Every idea had to pass through one person with a day job, and that person was the narrowest part of the pipe. Working harder made the pipe a little wider for a while. It never changed its shape.

<!-- p: 01-11 | agreed 2026-11-22 -->
My first real taste of AI at work came when I was seconded into a Data & AI team at a previous employer. I was careful with it. At first I only asked it to help me troubleshoot. Later I let it track down problems, but only ones I was confident I understood and could fix myself in time if it went wrong. Some colleagues used it to explain how code worked. Among the people I worked with I was usually the best developer, and reading code had always been a strength, so that wasn't where it helped me.
<!-- src: interview 1, Q2; early years note (usually the best developer among peers; moved here from 01-24 in review, 22 Nov 00:32) -->

<!-- p: 01-12 | agreed 2026-11-22 -->
Where it did help was in writing scripts. I started getting AI to write discovery and troubleshooting scripts for client problems. It was faster, and it let me work on more than one thing at once. My theories weren't always right. Its theories weren't always right either. But between us we generally turned days of troubleshooting into hours, and my clients got the benefit.
<!-- src: interview 1, Q3 -->

<!-- p: 01-13 | agreed 2026-11-22 -->
I was called in on one client's firewall changes when the consultants who usually looked after it weren't around. I didn't know their setup, and a single change could take me a few hours. So I wrote down how the work should be done, step by step, and gave the AI a place to keep what it learnt about that client between jobs. After that, a change took minutes. And it worked the way I work: it fitted in with what was already there, and challenged it when something wasn't right. I didn't know it yet, but that was the idea behind everything that came later.
<!-- src: interview 1 follow-ups (firewall before and after); notes/source-material/build-the-thing/2026-11-21-client-azure-ops-ai-usage.md; client not named -->

<!-- p: 01-14 | agreed 2026-11-22 -->
Meanwhile, the team I was part of decided to vibe code its own deployment tool: let the AI write it, and hope. I worked on some of its parts. It was one big Python program that, when you looked closely, mostly handed out templates. Nobody in the team knew Python well. It could just as easily have been PowerShell, Microsoft's own scripting language, and I genuinely don't think anyone stopped to ask what it should be written in. It was run very formally in Azure DevOps (Microsoft's tool for planning and tracking software work), broken into tiny tasks and handed out to individuals. Many of those tasks were things the AI could have finished in minutes.
<!-- src: interview 1 follow-ups ("Lacked ambition"); interview 1, Q2 ("vibe coded"; Ant, 22 Nov 01:07: keep the term) -->

<!-- p: 01-15 | agreed 2026-11-22 -->
I found it frustrating, and it took me a while to say why. The team had the same AI I had. But it was using it to do the old way of working a bit faster: the same small tasks, the same hand-offs, the same pace. The project lacked ambition. Not because the people lacked talent, but because nobody had asked how different the work could be now.
<!-- src: interview 1, Q2 -->

<!-- p: 01-16 | agreed 2026-11-22 -->
Then the job changed. I took voluntary redundancy and quickly found a new role. Somewhere in that change, I finally asked myself the question I'd been circling: where is the ceiling, really? On 14 September 2026, the first day of my gardening leave, I set myself a challenge. Keep improving, all the time, and see how far AI could take me. Applying for jobs came first, understandably, so this happened in between.
<!-- src: interview 1, Q2; review 22 Nov 01:09 and 01:21 (started 14 Sep 2026, first day of gardening leave, between job applications) -->

<!-- p: 01-17 | agreed 2026-11-22 -->
I didn't start with a grand plan. I was skint, and I wanted to make Charlie, my partner, a present. A website for her modelling seemed the obvious thing. I expected to write a good chunk of the code myself and let the AI help. That isn't what happened. Before long I wasn't building a website. I was building the thing that would build it.
<!-- src: interview 1 follow-ups (challenge from mid September, per review 22 Nov 01:09); Ant, 21 Nov 2026 (Charlie happy to be in the story; "skint" can go in) -->
