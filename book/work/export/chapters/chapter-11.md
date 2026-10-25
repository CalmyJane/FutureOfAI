# Chapter 11: The Explanation Levy

*2036 · Copenhagen*

The cell is the size of a coin, and it is dying on schedule.

Mikkel Holm watches the curve on the left-hand monitor. Charge, discharge, charge. Each time the cell comes back a little emptier, as if someone is skimming from it. The cryostat beside the bench hums at minus thirty, the temperature the sensors recorded on eleven nights in January outside Sodankylä, in Finnish Lapland, where a storage park the size of four football pitches lost almost a fifth of its capacity in less than three weeks.

It is twenty past ten at night. The fourth floor is empty except for him and the hum.

The material inside the coin is LX-29, a halide solid electrolyte, a pale grey ceramic that looks like nothing. In 2029 a materials model called Halden-3 proposed it, along with a recipe and a forty-page report of simulated ion paths. Two years later it was in pilot cells. By 2036 it is in roughly two-thirds of the grid-storage capacity built in the Nordic countries since 2032. It is cheap, it does not burn, it uses less lithium than anything before it, and until this winter it did everything asked of it.

Mikkel was on the team that tested it in 2030. He remembers the week the numbers came in. The conductivity was higher than any of them had expected from a mix of lithium and sodium in the same lattice. Someone had brought cake. Someone had asked, half joking, why it worked, and his old supervisor had said, "Let's find out after we've patented it."

They never found out. There was a grant for scaling up, and none for that.

His phone buzzes. Aino, from the grid operator in Helsinki.

"Anything?"

"It's doing it here too. Minus thirty, ten cycles, eight per cent gone. It's not just slow. It's damage."

"Can you tell me why?"

He looks at the curve. "I can tell you what. Not why."

"Mikkel. We have the same chemistry in Kiruna, in Luleå, in Tromsø. The forecast for February is colder. My board wants to know if we derate everything, or heat everything, or replace it. Which one?"

"I don't know."

"Then who does?"

He thinks about the honest answer. The honest answer is Halden-3, which was retired in 2034 when its maker moved to a newer architecture, and whose weights sit in an archive under a licence nobody has budgeted to reopen. And Halden-3 never knew either, not in the way Aino means. It had found a corner of chemical space where the numbers were good. It had not written down a reason, because no one had asked it for one that could be tested.

"I'll call you tomorrow."

He hangs up. On the right-hand monitor he opens the 2029 report and scrolls through the simulated ion paths, thousands of little coloured threads through a lattice drawn in perfect symmetry. They are beautiful. They describe how the ions moved at room temperature in a computer. They say nothing about minus thirty, or about whatever is happening at the boundary where the electrolyte meets the electrode as everything contracts in the cold.

To fix the material, he needs to know which feature of it matters. To know that, he needs to know why it worked.

He writes three hypotheses on the whiteboard. A phase change in the lattice. Cracking at the interface. Sodium moving somewhere it should not. Each one would take a postdoc six months to test properly. He has one postdoc, and she is on parental leave until April.

The curve on the left dips again. Cycle eleven.

Mikkel takes a marker and, under the three hypotheses, writes a fourth: *Something we never understood in the first place.* Then he turns off the whiteboard light and leaves the cryostat running.

---

## Answers first, explanations later

The idea that this gap is a kind of debt is not mine, and I want to give it to its owners before going further.

In July 2019 Jonathan Zittrain, a law professor at Harvard, published an essay called "Intellectual Debt: With Great Power Comes Great Ignorance", with a shorter version in the *New Yorker*. His opening example was aspirin. It was discovered in 1897, he wrote, and no one convincingly explained how it worked until 1995. He called the habit of accepting "answers first, explanations later" a way of accruing intellectual debt, and he argued that machine learning would make the habit routine: systems that predict well and explain nothing, adopted because they predict well.

In March 2024 Lisa Messeri, an anthropologist at Yale, and Molly Crockett, a cognitive scientist at Princeton, sharpened the point for science itself. Their *Nature* Perspective, "Artificial intelligence and illusions of understanding in scientific research", argued that AI tools in the lab can make scientists believe they understand more than they do, and can push research towards monocultures in which a field produces more results while understanding less. They sorted the tools into roles (the Oracle that summarises literature, the Surrogate that stands in for data, the Quant that analyses it, the Arbiter that judges it) and tied each role to a particular illusion.

A third phrase is now in circulation. Software engineers have started to talk about **comprehension debt**: in Addy Osmani's March 2026 formulation, the growing gap between how much code exists in a system and how much of it any human genuinely understands. Osmani does not claim the term; he presents it as one already in use, alongside "cognitive debt". I am going to borrow it, with credit, and stretch it from codebases to whole fields of science.

What I want to add to Zittrain and to Messeri and Crockett is two things. One is a number, so that the debt can be measured. The other is an institution that pays it down at a steady rate, before the bill arrives all at once, as it does for Mikkel on a January night.

---

## The results are arriving first

Mikkel's story is invented. The pipeline behind LX-29 is already running.

In November 2023 a team at Google DeepMind published "Scaling deep learning for materials discovery" in *Nature*. Their system, GNoME, a graph neural network trained on crystal structures, proposed about 2.2 million inorganic crystals that its calculations placed below the existing stability frontier. DeepMind singled out roughly 380,000 of them as the most stable and the best candidates for synthesis. Before GNoME, the paper noted, computational and experimental work over decades had identified about 48,000 stable crystals. The paper also reported that 736 of its predicted structures had already been made, independently, by other laboratories.

In the same issue, a group led by Gerbrand Ceder at Berkeley described the A-Lab, a robotic laboratory that took computed targets, planned recipes using models trained on the literature, ran furnaces and X-ray diffraction, and adjusted its own plans. Over 17 days it reported making 41 new compounds from 58 targets.

Then the humans arrived, slowly. In January 2024 Robert Palgrave, a chemist at University College London, and Leslie Schoop at Princeton circulated a reanalysis of the A-Lab's diffraction data; it appeared in *PRX Energy* that March. They argued that the automated analysis had misidentified phases and ignored disorder, the tendency of real atoms to share sites in a crystal rather than sit in the tidy ordered arrangements a calculation prefers, and concluded that no new materials had been discovered. Ceder's group disputed this, while conceding that a human could refine the data better than the robot had. In April 2024 Anthony Cheetham and Ram Seshadri, at the University of California, Santa Barbara, examined a sample of GNoME's predictions in *Chemistry of Materials*. They found the method promising and the claims ahead of the evidence: many entries assumed an orderliness of metal atoms unlikely in the real world, and none of the predicted compounds had demonstrated a function, so they were not yet materials in any useful sense.

I find this episode encouraging, and I want to be precise about why. The critiques worked. But they were written by a handful of senior people, months after publication, about a few dozen samples, and doing them was nobody's job. If the output of such systems grows a hundredfold, the supply of Palgraves will not.

A month after GNoME, Microsoft and the Pacific Northwest National Laboratory reported a screen of more than 32 million candidate materials for solid battery electrolytes, run on cloud computers in less than 80 hours. They narrowed the field to a handful, synthesised one family (sodium and lithium sharing a yttrium chloride lattice, a mix that conventional wisdom had expected to perform poorly) and built a working prototype cell within about nine months. That is the real ancestor of my fictional LX-29. It is also a good example of the gap. The screen told the team where to look and left open why mixing the two ions should help, the kind of question someone has to answer before they can say how the material will behave at minus thirty.

The pace has risen since. Sakana AI's AI Scientist, published in *Nature* in March 2026, runs its own experiments and drafts the paper; one of its manuscripts scored above the acceptance threshold at an ICLR workshop, though its authors are frank about the naive ideas and invented citations. DeepScientist, at ICLR 2026, beat the best human results of 2025 on three frontier AI tasks, and DeepMind's AlphaEvolve found a way to multiply four-by-four complex matrices with one multiplication fewer than Volker Strassen's 1969 method. Anyone can check that procedure; understanding why it is possible is a different activity. Kosmos, from Edison Scientific, shows where the gap sits. Independent scientists judged its statements based on data analysis accurate 85.5 per cent of the time, and its interpretive statements, the part that resembles an explanation, only 57.9 per cent.

That is the pattern. Machines are now very good at producing results that pass checks, and checking gets cheaper every year, while explaining costs what it always did.

I looked for a measurement of how much of any field's working results humans can explain, and could not find one. Nobody tracks it.

---

## How success builds the debt

The debt grows out of things working, which is why it is hard to see.

Start with the incentives in a battery lab. A new electrolyte that conducts well is worth a patent and a pilot line. An explanation of why it conducts well is worth a paper, maybe. The first has buyers. The second has readers. When money is short, which is always, the lab funds the first and promises itself the second.

Before AI, this mattered less, because the two came bundled. A chemist who designed a material usually had a reason in mind (this ion is smaller, so it should move more easily), and the reason travelled with the material. When the material failed, the reason was the first suspect.

A model that searches millions of candidates runs on a score. When its candidate works, the result arrives naked, with no hypothesis attached. Sometimes the model produces something that looks like a reason, such as simulated ion paths. Those describe what happened in the simulation, and are silent on which features of the material were essential and which were incidental. That distinction is what you need when conditions change.

Here is the difference in one example. Verification asks: does this cell hold its charge for 5,000 cycles at 25 °C? You can answer that with a test rig and patience. Explanation asks: which property of the lattice makes it hold its charge, and what happens to that property at minus thirty? You can answer that only with a theory. Verification tells you a thing works where it was tested. Explanation tells you where else it will work.

Success then does two more things. It spreads the result, because a cheap material that works gets adopted everywhere, quickly. And it removes the pressure to explain, because nothing is going wrong. The debt grows fastest when everyone is happy.

Then there is retirement. Halden-3 is fictional; the practice is real: AI companies retire models on a commercial schedule, and nobody asks first who built on their outputs. If the model held anything like an implicit understanding, it goes into an archive with the weights. Chapter 14 will look at what it means for the retired and the dead to keep shaping decisions. Here the point is narrower. When the designer is gone, the only route to an explanation is reconstruction, and reconstruction is slow.

Put these together and you get the shape of Mikkel's winter. One unexplained material, used across a whole region, built into infrastructure meant to last twenty years, meets a condition nobody tested. The failure is correlated in the way the first part of this book was about. Every park built on the same chemistry shares the same unknown. They meet the cold together.

---

## Measuring the debt

If comprehension debt is going to be managed, it has to be counted. I propose a single number for a field.

The **comprehension debt ratio** is the use-weighted share of a field's working results that an independent team, not shown the AI's reasoning, cannot explain well enough to predict a new testable result within 12 months.

Each part of that definition does work.

*Working results* means results that are in use, like materials in products or algorithms in software. A dead end does not create debt, because nobody depends on it.

*Use-weighted* means each result counts in proportion to how much rests on it. LX-29, in two-thirds of new Nordic storage, weighs far more than a compound in a database that nobody has made. The weight could be deployment volume or citations by later work; for an engineering field I would use installed capacity or sales, because that is where the failure would land.

*An independent team, not shown the AI's reasoning* means the explanation must be rebuilt from scratch. The team can use any tools it likes, including other AI systems, but it does not see the original model's internal reports. This tests whether an account can be reconstructed from the material itself and from public knowledge, which is the situation after a model is retired.

*Predict a new testable result* is the heart of it. A story about why something works is cheap. The test of an explanation is that it says something the original result did not: this material will crack below minus twenty-five; this matrix trick also works for five-by-five. The prediction is registered in advance, then tested. It may turn out false, as long as it is specific enough to fail.

*Within 12 months* sets a clock. Some results will take decades to understand, and that is fine. The ratio records what a serious team can do in a year, which is about the time a grid operator has before the next winter.

The ratio runs from 0 to 1. A field with a ratio of 0.1 can explain almost everything it uses. A field at 0.6 is running mostly on results nobody can account for. My guess is that most fields today sit low, because most of their working results still came from humans with reasons. I would expect battery materials and some areas of algorithm design to climb fastest over the next decade, because that is where AI search already produces deployable results. That is a guess, and the point of the number is to replace it.

---

## The Levy

Measurement alone does not pay anyone. The second invention is a way to fund the explaining at a steady rate, so that understanding keeps pace with discovery, before a failure forces the question.

The **Explanation Levy** is a fixed share of every AI-discovery budget, set aside for human comprehension. The default is 5 per cent. It rises to 10 per cent in fields whose comprehension debt ratio is above 0.5, and falls to 3 per cent in fields below 0.2.

The precedent is real and nearly forty years old. When the Human Genome Project was being set up, James Watson announced in 1988 that a share of its budget would go to studying the ethical, legal and social implications of the work. The programme, called ELSI, received 3 per cent of the National Human Genome Research Institute's budget in fiscal year 1990 (about $1.5 million), 4.7 per cent in 1991, and an average of 5.1 per cent from 1992 to 1995. The Department of Energy, the project's other funder, made a similar set-aside. ELSI had its critics, and its record on the problems it was meant to address is still argued over. It did establish that a percentage could be written into the budget before the results arrived, and that scientists would live with it.

Who pays? Any public funder that supports AI-driven discovery, through grants or national laboratories, applies the levy to those budgets directly. For private work, the hook is the public money that already flows to it: research tax credits and the certification of materials used in grid storage. A company that wants its AI-designed electrolyte in a publicly supported storage park pays the levy on the discovery programme that produced it, or contributes to the field's pool at the same rate.

The money funds three things.

**Explanation bounties.** Each year the fund publishes a list of the most heavily used unexplained results in each field, ranked by use weight. Any team, anywhere, can register an explanation together with a prediction it implies. If the prediction is tested and holds, the team is paid. The bounty scales with the use weight: explaining LX-29 in 2031, before the cold, would have been worth a great deal. Bounties have a track record in mathematics, where prizes for specific open problems have drawn work for a century, and they suit a world where the result is already known and only the reason is missing.

**Understanding audits.** Once a year, an audit body draws a random sample of a field's working results, weighted by use, and gives each to an independent team under the rules above. The share that the teams cannot explain within twelve months is the comprehension debt ratio. The audits do two jobs: they produce the number that sets the levy rate, and they force a slow, steady stream of reconstruction work in fields that would otherwise do none. A sample of fifty results per field per year is enough to tell a ratio of 0.2 from 0.5, which is all the rate-setting needs.

**Paid explainer posts.** The most important line is the least glamorous. A share of the levy pays for permanent posts, inside labs and at funders, whose job is to understand results the lab did not design. In 2026 this career barely exists: the reanalyses of GNoME and the A-Lab were done by senior academics fitting them around their own research. An explainer would be a recognised professional with a salary and a promotion track. In 2036 Mikkel would have had one down the corridor, who had been living with LX-29 for five years.

The rates are set to create a gradient. A field that explains its results pays less and gets more of its budget for discovery. A field that piles up unexplained results pays more and gets more explaining. Under the levy, discovery runs at full speed and deployment waits for nothing. Someone is simply paid to close the gap while there is still time.

---

## The objection from history

Zittrain's own example holds the case against the levy: people used something well for decades before anyone could explain it, and nothing terrible followed. In physics the objection is even stronger.

High-temperature superconductivity is the closer case for this chapter. Copper-oxide superconductors were discovered in 1986. Forty years later, after thousands of experiments, physicists still argue about the mechanism; a 2026 review describes three competing schools. Yet tape made from these materials carried the current in the 20-tesla magnet that MIT and Commonwealth Fusion Systems tested in September 2021, and it is being built into fusion devices and power cables today. The steam engine ran for a century before thermodynamics explained it. Engineering has always worked ahead of understanding. Why tax the new version of an old and mostly successful habit?

I accept most of this. A result that works without explanation is still a result. Nobody should have refused to use superconducting tape until the theory was settled, and the levy does not ask anyone to. That is why the floor is 3 per cent, and why nothing in the levy delays deployment.

My answer is about the portfolio. Each of these historical cases was one unexplained result surrounded by a large body of explained ones. The engineers using superconducting tape know a great deal of physics about it: how it fails when it overheats, and how its current capacity changes with temperature. They measured all of it, because human engineering of the material forced them to. The unknown is narrow, and it sits in a field where most of the neighbouring knowledge is solid. When the tape surprises someone, there is a lot of understood ground to stand on while they work out why.

A field whose working results are mostly unexplained is a different object. Its failures are correlated. If most of the materials in grid storage were found by the same kind of search and optimised against the same tests, then they share blind spots: conditions nobody tested, like minus thirty, apply to all of them at once. And when they fail together, there is no neighbouring theory to stand on, because the neighbours are unexplained too. One unexplained material is a loan. A field of them is a leveraged balance sheet, and leveraged balance sheets fail in a single week.

That is the reason for making the rate depend on the ratio. At a low ratio, the argument from history holds, and the levy is small. At a high ratio the argument fails, and the levy rises.

There is a second objection worth a paragraph. If machines can produce results, they can produce explanations too; why pay humans? Partly they can, and the levy should pay for machine-assisted explaining. But the test in the ratio is predictive, and the team is independent of the original model, for a reason. An explanation generated by the same kind of system, from the same simulations, tends to share its blind spots. What the levy buys is a second, separate route to the same result, and someone who understands it well enough to change it.

---

> **For researchers**
>
> 1. **Time to reconstruct a rationale.** For a sample of AI-discovered results in one field (battery materials, catalysts, matrix algorithms), give blinded teams the result alone and measure the *time to a confirmed prediction*: months until the team registers an explanation whose novel prediction is tested and holds. How does it vary with the size of the search that produced the result, and with whether the team may use AI tools? This is the empirical core of the comprehension debt ratio.
> 2. **Bounty design.** Run explanation bounties on a set of known unexplained results and measure the *claim rate* (registered explanations per bounty per year) and the *false-explanation rate* (share of paid explanations later overturned) as functions of bounty size and prediction-registration rules. What payout schedule maximises confirmed explanations per euro without rewarding plausible stories?
> 3. **Correlated blind spots.** For a population of AI-proposed materials in one application, measure the *correlation of failure*: the probability that two randomly chosen deployed materials both fail outside their tested range under the same stress (temperature, cycling rate, humidity), compared with human-designed materials in the same application. Does it rise with the share of the field produced by one class of model?

---

Mikkel calls Aino at eight the next morning. The cell in the cryostat has lost another two per cent overnight.

He has worked out what an answer would cost. Three postdoc-years to test the hypotheses on his whiteboard. Several weeks of beam time at a synchrotron to watch the lattice in the cold. A technician to keep the cryostat running through next winter. A great deal of computer time to simulate the interface at temperatures the original model never visited. None of it is in any budget, because in 2029, when the money was flowing, nobody wrote a line for understanding.

There is a faster option, and his dean has already mentioned it. A current model could design a replacement electrolyte in a few weeks, screened for minus forty this time, for a compute bill measured in megawatt-hours. It would probably work. It would also arrive with no reason attached, and the next unexpected condition would find it as unprepared as this one found LX-29.

## Notes

- **Intellectual debt:** Zittrain J, "Intellectual Debt: With Great Power Comes Great Ignorance", *Medium* (Berkman Klein Center), 24 July 2019; shorter version as "The Hidden Costs of Automated Thinking", *The New Yorker*, July 2019. https://medium.com/berkman-klein-center/from-technical-debt-to-intellectual-debt-in-ai-e05ac56a502c ; https://www.newyorker.com/tech/annals-of-technology/the-hidden-costs-of-automated-thinking
- **Illusions of understanding:** Messeri L, Crockett MJ, "Artificial intelligence and illusions of understanding in scientific research", *Nature* 627:49–58, 2024. https://doi.org/10.1038/s41586-024-07146-0
- **Comprehension debt:** Osmani A, "Comprehension Debt: the hidden cost of AI generated code", 14 March 2026. https://addyosmani.com/blog/comprehension-debt/
- **GNoME:** Merchant A, Batzner S, Schoenholz SS, Aykol M, Cheon G, Cubuk ED, "Scaling deep learning for materials discovery", *Nature* 624:80–85, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10700131 ; Google DeepMind, "Millions of new materials discovered with deep learning", 29 November 2023. https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning
- **A-Lab:** Szymanski NJ et al., "An autonomous laboratory for the accelerated synthesis of novel materials", *Nature* 624:86–91, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10700133
- **A-Lab critique:** Leeman J, Liu Y, Stiles J, Lee SB, Bhatt P, Schoop LM, Palgrave RG, "Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis", *PRX Energy* 3:011002, 7 March 2024. https://doi.org/10.1103/PRXEnergy.3.011002 ; Chemistry World, "New analysis raises doubts over autonomous lab's materials 'discoveries'", 2024. https://chemistryworld.com/news/new-analysis-raises-doubts-over-autonomous-labs-materials-discoveries/4018791.article
- **GNoME critique:** Cheetham AK, Seshadri R, "Artificial Intelligence Driving Materials Discovery? Perspective on the Article: Scaling Deep Learning for Materials Discovery", *Chemistry of Materials*, 8 April 2024. https://doi.org/10.1021/acs.chemmater.4c00643
- **Microsoft/PNNL electrolyte screen:** Chen C, Nguyen DT, Lee SJ, et al., "Accelerating computational materials discovery with artificial intelligence and cloud high-performance computing: from large-scale screening to experimental validation", arXiv 2401.04070, January 2024. https://arxiv.org/abs/2401.04070 ; PNNL publication record, 2 August 2024. https://www.pnnl.gov/publications/accelerating-computational-materials-discovery-machine-learning-and-cloud-high
- **The AI Scientist:** Lu C, Lu C, Lange RT, Yamada Y, Hu S, Foerster J, Ha D, Clune J, "Towards end-to-end automation of AI research", *Nature* 651:914–919, 26 March 2026. https://www.nature.com/articles/s41586-026-10265-5 ; Sakana AI announcement. https://sakana.ai/ai-scientist-nature/
- **Kosmos:** Mitchener L et al., "Kosmos: An AI Scientist for Autonomous Discovery", arXiv 2511.02824, November 2025 (preprint). https://arxiv.org/abs/2511.02824
- **DeepScientist:** Weng Y et al., "DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively", ICLR 2026; arXiv 2509.26603. https://arxiv.org/abs/2509.26603
- **AlphaEvolve:** Novikov A et al., "AlphaEvolve: A coding agent for scientific and algorithmic discovery", arXiv 2506.13131, June 2025. https://arxiv.org/abs/2506.13131
- **ELSI share:** National Human Genome Research Institute, "ELSI Program Review 1990–1995". https://www.genome.gov/10001747/elsi-program-review-19901995 ; DOE Human Genome Project archive, budget. https://doe-humangenomeproject.ornl.gov/human-genome-project-budget/
- **Cuprate mechanism unresolved:** Singh N, "40 years of cuprate high-Tc superconductors: a perspective on theories", arXiv 2606.29249, 2026. https://arxiv.org/abs/2606.29249
- **20-tesla HTS magnet:** *MIT Technology Review*, "MIT's superconducting magnets are ready for fusion", 23 April 2024 (on the 5 September 2021 test and the March 2024 *IEEE Transactions on Applied Superconductivity* papers). https://www.technologyreview.com/2024/04/23/1090425/mits-superconducting-magnets-are-ready-for-fusion
