# Chapter 15: Working with AI is still work

<!--
First draft, 27 Nov 2026. Ant's title and theme (27 Nov 16:01): persistence, an experimental mindset, a callback to the scientific method. Briefs.md ch 15. Sources: store r2antbooks notes/interviews/build-the-thing/2026-11-27-theme-persistence-experiment.md, 2026-11-27-theme-adrs-revised.md, 2026-11-27-theme-ai-driving-ai.md; project doc claude/jimmy-9.md (3D Jimmy version 9 plan, agreed 27 Nov 14:55).
Point back to ch 12 (the first 3D Jimmy evening); don't retell it. The ending of the Jimmy 8 story waits on how version 9 turns out (15-06).
-->

<!-- p: 15-01 | draft 2026-11-27 -->
People sometimes talk about AI as if it does the work for you. A lot of the time it does. It writes the code, drafts the page, runs the night. But working with AI is still work. It's just a different kind. Less typing, more trying. You have an idea of what will work, you try it, you look honestly at what came back, and you change the idea. Then you do it again.
<!-- src: Ant, 27 Nov 16:01 (title: "Working with AI is still work"); theme note 2026-11-27-theme-persistence-experiment.md ("persistence, an experimental mindset, it's also a callback to the scientific method"). Wording is the drafter's: Ant to agree -->

<!-- p: 15-02 | draft 2026-11-27 -->
That loop has a name, and it's an old one. It's the scientific method. You make a guess, you test it, you look at the result, and you let the result change the guess. In chapter 13, the scientist's habit was scepticism: not believing something just because it agrees with you. This is the other half of the same habit. The AI makes each test fast and cheap. It doesn't decide what the test should be, and it won't tell you when to stop believing your guess. That part is still yours. So is the persistence to go round again when the result says no.
<!-- src: theme note (callback to the scientific method); chapter 13, the Ladybird and "scientist's habit" paragraphs (agreed: Ant thinks of himself as a scientist; "carry some scepticism around with you, the scientist's habit"). "It won't tell you when to stop believing your guess" ties to ch 12's rule of thumb, "believing your own is deadly". Drafter's wording: Ant to agree -->

<!-- p: 15-03 | draft 2026-11-27 -->
The longest-running experiment in this book is Jimmy in 3D. Chapter 12 told the story of the first evening, when the first version came out complete on paper and cursed in practice. That evening wasn't the end. By 27 November we were on version eight, and version eight kept fighting us. Every fix uncovered the next fault. Bend a leg, and the skin split. Mend that, and something else stretched.
<!-- src: claude/jimmy-9.md section 1 ("Why version 8 kept fighting us. Each fix uncovered the next fault"; 8d the everyday Jimmy on the Wall; Ant, 27 Nov 14:49: "take our difficulties with version 8 and plan a version 9"); chapter 12 (draft: version 1 "cursed"); JM-491: https://hub.smoothey.co.uk/dashboard#ref/JM-491. Versions 2 to 7 not described: Ant to say whether any is worth a line -->

<!-- p: 15-04 | draft 2026-11-27 -->
When we finally stopped and asked why, the answer wasn't in any of the fixes. It was in what we'd built on. The model was made of nearly a thousand overlapping plates instead of one skin, so the plates came apart wherever he bent. He'd been shaped sitting down, with his legs sunk into his chest, so every pose had to drag them back out. No amount of patching was going to fix that. Each patch cost more than the last. The honest result of the experiment was that the base had never been built to move.
<!-- src: claude/jimmy-9.md section 1 table ("Meshy built 8d as about 960 overlapping plates of skin, not one skin"; "He was modelled sitting, with his upper legs sunk into his chest"; "So the base was never built to bend"); section 5 ("Keep patching 8d: no. Each fix today cost more than the last") -->

<!-- p: 15-05 | draft 2026-11-27 -->
That's where persistence gets misunderstood. It isn't doing the same thing harder. Sometimes the persistent thing to do is to stop, put a bullet in the version you've got, and start again from a better base. That's what version nine is. A plain Jimmy first, built to bend, with one skin and a proper cat's skeleton. He has to pass a test of every pose he'll ever need, from a yawn to a dance, before anything pretty goes on top.
<!-- src: claude/jimmy-9.md sections 2 and 3 (two layers: base first, "one closed skin, a proper cat skeleton"; a range of motion test through every pose, including dance, Ant 14:58; "He has to pass a full posing test before anything pretty is added"); store 2026-11-27-sb6-answers.md (19-10: "I'm not precious about putting a bullet in something if needed"); chapter 19, 19-13 (draft) -->

<!-- p: 15-06 | draft 2026-11-27 -->
There's an irony in how we got there. Version eight was one AI driving another: Claude writing the instructions, Meshy building the model. When that went wrong, the fix wasn't fewer AIs. It was a third one. Gemini now draws Jimmy as a clean reference sheet first, front, side and back, standing square. Meshy builds his shape from all three views at once. Then Claude rebuilds that shape properly in Blender, by script, and tests every pose.
<!-- src: theme note 2026-11-27-theme-ai-driving-ai.md (Ant, 15:57: "The whole Jimmy 8 experience, though ironically the fix was to add a third AI to the loop (assuming the current approach we are working through works!)"); claude/jimmy-9.md section 4 (Gemini reference sheet, Meshy Multi-Image to 3D from front, side and back, Blender scripted rebuild and Rigify skeleton) and "Step 2" (first Meshy model, 27 Nov 16:00 to 16:10) -->
<!-- q: SB-6 15-06: the ending waits on version 9. Did the third AI fix it? One or two sentences on how it turned out, once we know -->

<!-- p: 15-07 | draft 2026-11-27 -->
Using one AI to drive another is one of the most useful habits I've picked up. Claude writes the prompts for the image tool that made the cover of this book. It drives Meshy, a tool for making 3D models, so I don't have to sit in Meshy myself. And it researched how to hand some of the work off to the smaller models on my own computers, which chapter 21 describes. I stop being the go-between. I say what I want, once, to the AI that knows the most about the job, and it does the talking to the others.
<!-- src: theme note 2026-11-27-theme-ai-driving-ai.md (Ant, 15:55: "getting Claude to write prompts for other AI, getting it to drive Meshy etc"; 15:57 examples agreed: "Gemini prompts for the cover, our work on researching handoffs to local models"); SB-8 (cover in Gemini): https://hub.smoothey.co.uk/dashboard#ref/SB-8; chapter 21 (draft). "the AI that knows the most about the job" is the drafter's: Ant to agree. Gemini not named for the cover here: Ant to say whether to name it -->

<!-- p: 15-08 | draft 2026-11-27 -->
But each AI has its own habits, and the one doing the driving has to learn them. On the day we started version nine, Gemini couldn't open Jimmy's pictures when they were linked from a folder, so it drew a generic cat instead. Uploaded directly, it kept his face. Long, careful prompts were refused. One-line prompts went straight through, and small changes asked as "the same picture, but" worked best. None of that was in any instructions. It was found the way everything in this chapter is found: try it, look, change it.
<!-- src: claude/jimmy-9.md section 8, "First test" ("References must be uploaded, not added from Drive. From Drive, Gemini said it couldn't open them and drew a generic 3D black cat. Uploaded directly, it kept his face and style"; "Long prompts get refused ... Short ones go through") and "Build chosen" ("a long, careful prompt errored; a one-line prompt worked. Small fixes ('same picture, but…') work well") -->

<!-- p: 15-09 | draft 2026-11-27 -->
Experiments change decisions, too, and that's meant to happen. My architecture decision records, the notes from chapter 11 of what we decided and why, get revised more often than they would in a traditional project. I think that's right. A decision is only as good as what you knew when you made it. When new information turns up, the correct thing to do is to challenge the old decision, not to defend it.
<!-- src: theme note 2026-11-27-theme-adrs-revised.md (Ant, 15:16: "My ADRs get revised more often than they would with a traditional approach, but I'd argue it is the correct thing to challenge previous decisions especially in light of new information"); chapter 11, 11-14 (draft: ADRs) -->
<!-- q: SB-6 15-09: one real example of a decision reopened by new information would help here (ADR 0018 started the thought, but you didn't think it a good example). Or leave it general -->

<!-- p: 15-10 | draft 2026-11-27 -->
That raises a fair worry. If every decision can be reopened, how is it different from changing your mind every week? My rule of thumb is this. Respect the original intent of a decision. In some cases the intent can't change at all. But the detail is always fair game. The goal for Jimmy in 3D hasn't moved since the first evening: a Jimmy you'd take for the drawing at a glance, who can do everything the flat one can. The route to it has changed many times.
<!-- src: theme note 2026-11-27-theme-adrs-revised.md (Ant, 15:24: "try to respect the original intent of the decision that may be immutable in some cases, but the detail is always fair game for revision"); chapter 12, 12-04 (draft: the test, "take him for the drawing at a glance"); 12-01 (all his existing moves and more). The Jimmy example of intent against detail is the drafter's: Ant to agree -->

<!-- p: 15-11 | draft 2026-11-27 -->
This book is written the same way. An agreed paragraph stays set, unless new information changes what it says or a review reopens it. The final polish can change the wording, but never the meaning. The intent is protected, and the detail can move. It's the same rule as the decision records, in a different place, and it's why I trust a book that's been revised so many times.
<!-- src: PROCESS.md steps 4 and 5 (agreed paragraphs stay set unless new context or a review; the polish reviewer may change wording, never intent); theme note 2026-11-27-theme-adrs-revised.md (Claude's link to PROCESS.md, not agreed). "it's why I trust a book" is the drafter's: Ant to agree or cut -->

<!-- p: 15-12 | draft 2026-11-27 -->
None of this feels like a grind, because each try is cheap now. A version of Jimmy that once would have taken me a week of evenings takes an afternoon. A decision record takes minutes to change. That's the real gift of AI to persistence. It doesn't keep going for you. It makes going round again so cheap that you can afford to do it as many times as it takes.
<!-- src: drafter's synthesis. "a week of evenings" against "an afternoon" is an illustration, not a measure: Ant to give a real comparison or cut. Ties to chapter 3 (agreed: what compounds) -->

<!-- p: 15-13 | draft 2026-11-27 -->
So yes, the machine does a great deal of the work. But the loop is still mine: the guess, the test, the honest look, and the choice to go round again or to start from somewhere better. That's the work that's left. It's also the part I enjoy most. And as the next chapter shows, it isn't the only cost.
<!-- src: drafter's closing; leads into chapter 16, What it costs. "the part I enjoy most" is the drafter's: Ant to confirm -->
