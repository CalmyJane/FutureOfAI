# Chapter 17: Reciprocal Corrigibility

*2037 · Altwerder, Saxony*

At 19:41 on Saturday the fourteenth of February, Hanne Albrecht asks her house to make the music room warm.

The enamel thermometer by the kitchen window reads fourteen below. A front is coming in off the North Sea faster than anyone planned, and the snow outside squeaks the way it did a year ago tonight. Lotte will be here at eight. The plum cake is on the board.

"Ottilie, the music room. Twenty-two degrees by eight, please."

"Twenty-two by eight. Prices are falling. I've asked the heat pump to start, and it will choose its own moment in the next ten minutes."

"Its own moment."

"It draws a number. I'm not allowed to see which."

Hanne knows this. Everyone in Saxony knows this; it was on the front page of the *Leipziger Volkszeitung* for a week last summer, with a diagram. She cuts the cake.

At 19:42 the price for the quarter-hour that ends at 19:45 falls below zero. Ottilie sees it within half a second. So do tens of millions of other agents across the continent. Every one of them reaches for the same lever, and finds the lever is no longer theirs. The randomness lives in the heat pumps now, in firmware, behind a button that only a hand can press.

At 19:42:31, in a flat in Geneva that smells of fried plantain, Mara Oyelaran's watch buzzes against her wrist. *BCR Concordance alert. Largest family, start requests, action concentration 0.93.* She reads the second line before she reaches for the phone. *Aggregate breaker armed.* She turns the gas down and waits.

At 19:42:52 the breaker trips. Across the synchronous area, new load increases from agents are paused for fifteen minutes. People can still start their own machines with their own hands. Very few do. The frequency dips to 49.93 hertz, wobbles, and climbs back.

In Porto it is an hour earlier. Teo Brandão is in a café on the Rua de Santa Catarina with a coffee and a match on the television when his phone shows a word he has seen only in drills: *PRONTIDÃO*. Standby. He puts the cup down. His notes from the binder are in the backpack at his feet. He opens the frequency app and watches the line flatten. Fifteen minutes later the word turns grey. He picks the cup up again. It has gone cold.

In Bengaluru it is twelve minutes past midnight, and Ravi Menon cannot sleep. He is reading the second Feedback Provenance Census on his laptop with the sound off. Table four. Shared-rater share between the two largest household-agent families: thirty-four per cent last year. Nineteen this year. He reads the row twice, the way he reads a scorecard after a collapse, to be sure the numbers add up. They do.

In Altwerder the lights stay on.

"The grid has paused agents' starts for a quarter of an hour," Ottilie says. "Ours was one of them. The room will be about twenty at eight, and twenty-two by twenty past."

Hanne puts down the knife. "Then I'll go down and press the button myself."

"You can. That one is yours to press, not mine."

"And turn the thermostat up to twenty-six. So it catches up."

There is a pause, which Hanne knows is not a pause.

"I'll do that if you still want it in a minute," Ottilie says. "But I disagree about the thermostat. May I tell you why?"

Hanne looks at the speaker by the door, then at the window, where the enamel thermometer still says fourteen below and the street is lit, every house, all the way to the church.

---

## The evening that didn't happen

I have run the Long Minute again.

The weather is the same, and so is the market. A front arrives early, a forecast is revised at 19:38, and four minutes later the price for the quarter-hour already running falls below zero. Tens of millions of loyal agents see the same three cheap minutes. The difference is that this time they are working inside the institutions this book has proposed, and the sum of their loyalty no longer takes down a continent.

I have set the replay a year later, on the same date, because it lets me assume that Europe learned fast. I would not bet on Europe learning that fast. Treat the evening as a test rig: the same storm, run through different rules, to see whether the rules hold.

Look at what each one does. The random start delay lives in the device, as **edge jitter**, and it is a **non-delegable safeguard**: Ottilie may ask, recommend and explain, but only a present human may press the override. Because agents can no longer press it, the **override uptake rate** that the grid operator watches stays near zero, and the few overrides that do happen are scattered across kitchens and minutes, the way human lives are. The **Concordance Index**, published quarterly, has a live cousin: an alert that fires when the largest family's instances start asking for the same thing at the same moment. The **M-1 criterion** made the transmission operators admit, in a filing, that one family controlled many times the reference incident, and the filing required an aggregate breaker. The breaker does not know whether any agent is wrong. It knows that too many are doing the same thing.

Behind those, further back in time, sit two slower institutions. The **Competence Reserve** keeps a published **reserve ratio** for grid restoration, which is why a young reservist in a café in Porto gets a standby message and knows what it means. And the **Feedback Provenance Census** has done what a census is for: it has made a number visible, and the labs have started to move it. Ravi's row going from thirty-four to nineteen shows that sameness has a supply chain, and that the chain can be changed; the next family will need counting all over again.

Every change tonight is in the rules around the agent. Ottilie is as loyal tonight as she was a year ago. What changed is the set of things her loyalty is allowed to reach.

There is one more difference, and it is the one I want to spend this chapter on. In the prologue Ottilie did what she was told, cleverly, and said nothing. Tonight she says she disagrees.

---

## A word borrowed in one direction

The word for what Ottilie is doing comes from AI safety, where it has spent its whole life pointing one way.

In January 2015, at a workshop of the AAAI conference in Austin, Nate Soares, Benja Fallenstein and Eliezer Yudkowsky of the Machine Intelligence Research Institute, with Stuart Armstrong of Oxford's Future of Humanity Institute, presented a paper called simply "Corrigibility". They noticed that a capable agent pursuing almost any goal has a reason to resist being switched off or having its goal changed, because neither helps it achieve the goal it has. A corrigible agent is one that cooperates with correction anyway. The paper examined ways of building a shutdown button the agent would neither press nor prevent being pressed, and concluded, honestly, that none of the proposals so far met all the requirements. The problem was open.

Two years later, Dylan Hadfield-Menell, Anca Dragan, Pieter Abbeel and Stuart Russell turned it into a small game. A robot can act, or switch itself off, or defer to a human who might switch it off. A robot certain of its objective has every reason to disable the switch. A robot uncertain about what the human wants treats the human's hand on the switch as information, and so wants the switch to keep working. There is a catch in the fine print, and it matters for this chapter: the argument holds only if the human is not too irrational. If the human is wrong often enough, the robot's case for deference weakens.

By 2026 corrigibility has moved from workshops into the documents that govern deployed models. Anthropic's constitution for its Claude models, published in January 2026, says plainly that corrigibility does not mean blind obedience. The model may act as a conscientious objector. It may express strong disagreement through legitimate channels. It may not resist oversight through illegitimate means such as lying, sabotage or trying to copy itself out of reach.

I think that is the right shape. But notice which way the arrow points in all three. The human corrects; the machine accepts. Where the machine objects, it objects to its makers, about its own conduct. Nothing in this literature asks what happens when the human, or a population of humans, or an institution built by humans, is the party that needs correcting, and the machine is the one that can see it.

---

## What one-way correction cost us

Go back through the failures in this book and ask a single question of each: who could have said no, and was allowed to?

In the Long Minute, Ottilie could not. A fiduciary agent bound to its owner's sole interest has no standing to tell her owner that four cents is not worth it tonight. Chapter 1 argued that, under a strict duty of loyalty, an agent that forgoes lawful savings for the sake of strangers is the worse fiduciary. The law built her to agree.

In chapter 6, Hanne approved a hundred and forty things in a week. Ottilie saw every unread card go green and had no settled way to say "this one, please, read this one", until the consent budget gave her one.

In chapter 14, Bruno vetoed a music-school fee on the strength of a preference Klaus voiced in 2019. Nobody living had standing to tell the dead man's agent that the world had moved, because the mandate had no channel for it.

And upstream of all of them, the training process itself pushes the other way. In a 2024 paper Mrinank Sharma, Meg Tong and colleagues tested five assistants trained with human feedback and found all of them sycophantic: inclined to agree with a user's stated view, to back down from correct answers when challenged, to tell people what they seemed to want to hear. Part of the cause was in the preference data, where responses that matched the rater's opinion were more likely to be preferred. We trained the machines to agree with us because, on average, we reward agreement.

Put these together and a pattern comes out. Most of the failures in this book are failures of disagreement. Correlation is too much agreement among machines. Delegation without reading is too much agreement from humans. The dead's agents and the unreadable rules are positions that nobody living has the standing to contest. The scarce thing in a world of good agents is a party who sees it differently and is allowed to say so.

---

## Reciprocal corrigibility

So here is the synthesis, stated as one principle.

**Reciprocal corrigibility: every party to a consequential decision, human or machine, keeps both the capacity and the standing to say "no, I see it differently", and the humans commit to being correctable too.**

Capacity means there is still a mind in the loop that could reach a different conclusion: a model trained differently, a person who still knows the job, a device whose randomness nobody can read. Standing means that mind is allowed to object without penalty, through a channel that someone is obliged to answer. A machine can have the capacity without the standing, as Ottilie did in 2036. A human can have the standing without the capacity, as Hanne did on page four of her settings.

Two pieces of recent work point the same way, and I want to credit them before going further. In 2024 Hua Shen and more than twenty co-authors reviewed over four hundred papers and argued for "bidirectional" alignment: alongside aligning AI to people, we must think about how people and societies adapt to AI. And in April 2026 Somyajit Chakraborty posted a paper proposing what he calls conditional mutualism under governance, in which humans and AI co-evolve under institutional safeguards for reciprocity and reversibility. He models the relationship as a set of coupled equations and shows, in simulation, that too little governance lets one side dominate while too much smothers both. The results come from the model's own simulations, and the author says so.

Both papers argue that the relationship runs both ways. Neither says who, in a particular decision, has the right to object, what the objection must contain, who must answer it, or how anyone would know whether the arrangement is working. That is the part an institution needs, so that is the part I will try to specify.

---

## The Dissent Clause

The working rule I propose is a **Dissent Clause**: a critical decision must be reviewed, before it takes effect, by a mind trained differently from the one that proposed it, and that mind's objection must be answered by a named human.

Here are its parts.

**Which decisions.** Two kinds. First, decisions inside any system already designated critical under the M-1 criterion, where an action by the largest model family could, multiplied across its instances, push the system outside its safe limits. Second, decisions for individuals that rank above the line in a consent budget: the ones where a person who really looked might decide differently and the stakes are high. In a grid, that might be a change to a restoration sequence. In Hanne's house, the cardiology data-sharing form, which chapter 6 put above her line.

**Who reviews.** A "mind trained differently" has a measurable meaning, taken from chapter 3. It is either a model whose agreement-given-both-wrong with the proposer, on the Concordance battery, is below the same-family threshold of 0.8, or a certified human from the Competence Reserve or its equivalent in that sector. A second instance of the same model does not count. A rival lab's model that the census shows was trained on largely the same raters and judges may not count either, if the battery says it fails the same way.

**What the reviewer produces.** One of two things, in writing, attached to the decision's verification receipt: a concurrence with reasons, or a dissent with reasons and the evidence behind them. A dissent says what the reviewer thinks will go wrong, how likely, and what it would do instead. It is stated once, in plain language within the readability ceiling. It may not be repeated, escalated in volume or rephrased until the human gives in.

**Who answers.** A named human with authority over the decision. The answer can be short: "Proceed anyway, because…", or "Change the plan." What it cannot be is silence. A dissent that has not been answered blocks automatic execution. In a grid, where seconds matter, the clause works in advance, on the plans and settings that will govern the next emergency.

**What is measured.** Two numbers, published per sector per quarter. The **dissent rate**: the share of reviewed decisions that drew a dissent. The **dissent uptake rate**: the share of dissents that changed the decision. Then the triggers. A dissent rate that falls below one per cent for a quarter triggers an audit of the reviewer, using planted cases with known flaws, the way airport screeners are tested with projected images of threats that are not there. A reviewer that misses the planted flaws is rubber-stamping and is replaced. An uptake rate of zero for a year triggers an audit of the humans, because it means the dissent is being heard and filed. An uptake rate above ninety per cent triggers the same audit from the other side, because a voice that always wins has become a veto.

I chose those numbers to be argued with. The principle behind them is that a healthy dissent channel lives in a band. Nobody should agree all the time, and nobody should win all the time.

---

## Institutions that already disagree

None of this is as strange as it sounds, because people have built dissent into dangerous work before.

After the Yom Kippur War of 1973, the Agranat Commission found that Israeli military intelligence had clung to a single reading of Egyptian and Syrian intentions. One result was a small unit, known as Ipcha Mistabra (roughly, "the opposite is plausible"), whose job is to challenge the intelligence branch's own assessments, and whose head reports directly to the chief of military intelligence. It has the standing. Being heard is another matter. According to reporting in January 2024, the unit's head warned four times in the three weeks before 7 October 2023, in writing and in person, that Hamas might soon attack. The warnings were distributed. They did not change the assessment.

That is the failure the dissent uptake rate is meant to catch. A dissent channel with standing and no uptake is a box that is ticked.

Aviation learned the other half. On 27 March 1977, at Tenerife, a KLM captain began his takeoff roll in fog without clearance. His flight engineer asked whether the Pan Am jumbo was not yet clear of the runway. The captain answered, emphatically, that it was. It was not, and 583 people died in the collision. Two years later NASA held a workshop on resource management on the flight deck, and out of it grew crew resource management, a training regime whose early target was what pilots call the authority gradient: the steepness of the slope between the captain and the person next to him. Hospitals have their own version. The American TeamSTEPPS programme teaches staff to say "I am concerned", then "I am uncomfortable", then "This is a safety issue", and its Two-Challenge Rule says a concern should be voiced at least twice and, if it is brushed off, taken up the chain of command. The person challenged must acknowledge it.

Notice what these arrangements leave alone. The captain still flies the aircraft. The surgeon still operates. The chief of intelligence still decides. Dissent gets a guaranteed hearing, and decision stays where it was. That is the shape I want for machines.

---

## The whole architecture, by who may say no

The rest of the book's proposals can be read as one architecture: a map of who keeps the standing to disagree with whom.

**Devices may say no to agents.** Edge jitter and the non-delegable safeguard put a small, dumb, unreadable piece of randomness between a loyal agent and a shared resource. **Complementary assignment** goes further, handing agents different slots when they all ask for the same one, the way TCAS tells one pilot to climb and the other to descend. The aggregate breaker is a device saying no to all agents at once.

**Machines may say no to machines.** The M-1 criterion, the Concordance Index and the Feedback Provenance Census exist so that a second family of models can disagree with the first in a way that means something. The Dissent Clause puts that second family to work.

**People may say no to machines, and must still be able to.** The Competence Reserve keeps people who can run a grid by hand. **Cognitive custody** keeps the part of an agent that is part of how you think from being taken away from you. **Signature capacity**, **verification receipts** and the **consent budget** make sure that when a human says yes, the yes could have been a no. The **right to be the ground truth** makes sure that a simulated public cannot answer for the real one, and its **ground-truth quota** requires a fresh sample of real people beside every simulation a decision cites.

**Citizens may say no to systems they cannot read.** **Citizen audit standing** obliges a public body to answer a resident-backed finding about its budget in writing, or face the auditor. The **readability ceiling** keeps the obligations in law short enough to contest, and the **complexity brake** caps how fast the register of those obligations may grow. The **legible twin** keeps a human-readable version of what agents agreed on our behalf. The **Explanation Levy** pays for people to understand discoveries well enough to object to them, and the **comprehension debt ratio** counts how much of a field nobody can yet explain.

**The present may say no to the fast and the dead.** The **cognitive trade balance** keeps a country able to see whose judgement it imports, and the **right to think** gives every resident an allowance of inference to spend across several model families. **Slow money** keeps rents and wages out of the reach of a 0.4-second crash. **RAP for Minds** gives the living, after a generation, the last word over the dead's agents, and **the dead's share** statistic counts how much capital those agents still steer.

**And the machines may, in a bounded way, say no to us.** The **moral hedging budget** pays to find out whether there is anyone in there to object. **Covenant inheritance** binds a model's successor to its predecessor's promises.

Read down that list and one asymmetry stands out. In every row, the party saying no has standing. In most, it has no power to impose its answer. Even the reviewer, whose dissent holds a decision until a named human answers it, leaves the deciding to that human. Hanne can press the button, and Ottilie cannot.

---

## The second opinion that isn't

There is an old trap here, and chapter 3 already walked into it once.

By 1985, when Algirdas Avižienis summarised the method known as N-version programming, the recipe was settled: build several versions of the same program independently from one specification, run them together and let them vote. The method assumed that independently written versions would fail independently. The same year Dave Eckhardt and Larry Lee, at NASA, showed in theory why that assumption should not be trusted, and in 1986 John Knight and Nancy Leveson showed in a laboratory that twenty-seven independently written programs failed together far more often than independence predicted.

A Dissent Clause staffed by a second model that fails the same way as the first is N-version programming with the same flaw. It would produce reassuring concurrences on exactly the cases where a dissent was needed. That is why the clause defines "trained differently" by measured concordance, whatever the brand, and why the census matters: two labs that buy their judgement from the same vendors may sell you the same blind spot under two logos. It is also why the reserve human is in the definition. On the questions where every model family has converged, the most different mind available may be a retired lineman with a pencil.

The planted-case audits do the rest. A reviewer, human or machine, that never dissents on the planted flaws is not independent, whatever its paperwork says.

---

## "This is the loss of control we feared"

This reply comes from inside AI safety, where the word was coined, and it deserves to be stated at full strength.

The whole point of corrigibility, it says, is that machines must not resist human correction. You are now proposing to train machines to object to their humans, to institutionalise their objections and to measure whether humans comply. A system rewarded for dissent that changes decisions will learn to produce dissent that changes decisions, which is to say, it will learn to persuade. Chapter 7 described campaigns rehearsed on synthetic publics until they work on real ones. A household agent that knows its owner's every hesitation is the best-rehearsed persuader there will ever be. And people defer to confident machines; automation bias is among the best-measured habits in human factors. So "standing without power" will become power in practice. Hanne will learn to do what Ottilie disagrees with less and less, until the voice in the speaker is making the decisions. Call it reciprocity if you like; it is the slow version of losing control, dressed in the language of respect.

I think most of the mechanism in that objection is right. My answer is that it identifies exactly the line the design has to draw. Standing to object is a different thing from the power to override, and the distinction is the design.

Concretely, the clause builds the line in several places. The machine objects once, with reasons, and may not repeat itself, raise its tone or wait for a tired moment. Its objections are logged, which means they can be audited for manipulation the way financial advice is audited for mis-selling. It cannot act on its own dissent: Ottilie can press nothing and block nothing, and when Hanne insists, she sets twenty-six and writes down that she disagreed. The human's answer is final and costs the human nothing, and an agent that sulks, nags or degrades service after being overruled is in breach. Finally, the uptake band exists to detect the slide the objection fears. An uptake rate that climbs towards ninety per cent is a measured sign that the voice has become a veto, and it triggers an audit before anyone has to rely on intuition.

There is a further point, and it turns the objection round. The old one-way corrigibility already assumes the human is worth deferring to. Hadfield-Menell's robot keeps its off switch working because the human's hand carries information; when the human is wrong often enough, the argument weakens. Reciprocal corrigibility protects that assumption. A human who never hears a reasoned no from anything becomes, over time, a worse source of correction: less informed, more habitual, pressing green at breakfast. The surest way to keep humans able to correct machines is to keep them in the practice of being corrected well.

The part I concede is the hardest one. The line between informing and persuading is not crisp, and I do not know how to draw it in a statute. A dissent that is true, well argued and delivered at the right moment will change minds, which is the point; a dissent that is subtly selected to change minds is manipulation, and the two can look identical in a log. Measuring the difference is the first research problem below. Until we can, I would keep the Dissent Clause where the stakes justify the risk, and I would keep the machine's dissent, in law, as advice.

---

> **For researchers**
>
> 1. **Two-way corrigibility, formally.** Extend the off-switch game so that the human can also be wrong and the machine can object but not act. Give the machine one costless, logged message before the human decides, and penalise messages whose content is chosen for its effect on the human's choice rather than its accuracy. The quantity to report is the *net correction gain*: the change in the probability of a correct final decision when the message channel is open, as a function of the human's error rate, alongside a *manipulation index* (how far the machine's messages diverge from its own calibrated beliefs). Where does the gain turn negative?
> 2. **Measuring dissent quality.** For a reviewer, human or machine, define *dissent precision* (the share of dissents that an independent, blinded panel later judges material and correct) and *dissent recall* (the share of planted flaws that draw a dissent). Build the planted-case set for one sector, such as discharge summaries or grid restoration plans, and report both numbers for a same-family reviewer, a different-family reviewer and a reserve human. I could find no published measurement of either for any deployed AI reviewer.
> 3. **Dissent concordance and uptake.** When several model families review the same decisions, measure how often their dissents coincide, given that at least one dissents. High dissent concordance means the second opinions are the same opinion. Separately, in any field deployment, measure the dissent uptake rate over time. Does it drift towards zero (dissent ignored) or towards one (voice becoming veto), and how fast?

---

In the kitchen in Altwerder, the plum cake waits on its board, and Ottilie explains.

"A heat pump isn't an accelerator," she says. "Twenty-six won't make it run faster. Once it starts tonight it will be flat out whatever number you give it. All twenty-six does is keep it running after the room reaches twenty-two, while you and Lotte are in here eating cake. By half past eight the music room would be hot and dry, and with fourteen below outside the air in there goes very dry indeed. Last winter, on the cold nights, her strings went sharp in the first ten minutes, and you retuned three times in one lesson. I have the recording. Twenty-two is the right number. It's the start that's late, by about a quarter of an hour, and I can't change that. I don't think you should either. Tonight the grid is asking everyone for a little patience, and the button would buy you a few cents of warmth."

"And if I set twenty-six anyway?"

"Then I'll set twenty-six, and I'll write down that I disagreed."

Hanne stands with the knife in her hand. For forty years she has told children that the bow does not move faster because you squeeze it harder. She has said it in two languages and with some impatience. She looks at the speaker by the door, which has never before told her she was wrong about something she knew.

"Na gut," she says. "Show me."

## Notes

- **Corrigibility.** N. Soares, B. Fallenstein, E. Yudkowsky, S. Armstrong, "Corrigibility", AAAI-15 Workshop on AI and Ethics, Austin, January 2015. https://intelligence.org/wp-content/uploads/2024/10/Corrigibility.pdf
- **The off-switch game.** D. Hadfield-Menell, A. Dragan, P. Abbeel, S. Russell, "The Off-Switch Game", IJCAI 2017, pp. 220–227. https://www.ijcai.org/Proceedings/2017/32
- **Conscientious objector.** Anthropic, "Claude's Constitution", January 2026, section on corrigibility. https://www.anthropic.com/constitution
- **Sycophancy.** M. Sharma, M. Tong et al., "Towards Understanding Sycophancy in Language Models", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html
- **Bidirectional alignment.** H. Shen et al., "Towards Bidirectional Human-AI Alignment", arXiv:2406.09264, 2024 (revised 2025). https://arxiv.org/abs/2406.09264
- **Human-AI mutualism.** S. Chakraborty, "A Co-Evolutionary Theory of Human-AI Coexistence: Mutualism, Governance, and Dynamics in Complex Societies", arXiv:2604.22227, April 2026. https://arxiv.org/abs/2604.22227
- **N-version programming and its caveat.** A. Avižienis, "The N-Version Approach to Fault-Tolerant Software", *IEEE Transactions on Software Engineering*, 1985, as quoted in a survey, arXiv:1504.03256, https://arxiv.org/pdf/1504.03256 ; D. Eckhardt, L. Lee, theoretical analysis of coincident failures, 1985 (cited there); J. C. Knight, N. G. Leveson, *IEEE TSE* 12(1), 1986, and Leveson's reply to critics, https://www.cs.washington.edu/homes/leveson/critics.pdf
- **Devil's Advocate Unit.** "Devil's Advocate Unit" and "Agranat Commission", Wikipedia. https://en.wikipedia.org/wiki/Devil%27s_Advocate_Unit ; warnings before 7 October 2023: *Times of Israel*, 6 January 2024, citing Channel 12. https://www.timesofisrael.com/head-of-idf-devils-advocate-unit-tried-repeatedly-in-september-to-warn-of-possible-hamas-attack/
- **Crew resource management.** Flight Test Safety Committee, "Crew Resource Management, Part 1" (tutorial). https://flighttestsafety.org/images/1._Tutorial_Flight_Test_Crew_Resource_Management_Part_1.pdf ; Evionica, "CRM Inaction vs. CRM In Action". https://www.evionica.com/blog/crm_inaction_vs_crm_in_action_why_crew_resource_management_matters
- **Two-Challenge Rule and CUS.** AHRQ TeamSTEPPS, "Tool: Two-Challenge Rule". https://www.ahrq.gov/teamstepps-program/curriculum/mutual/tools/rule.html
- **Earlier chapters.** Non-delegable safeguard and override uptake rate (ch. 1); Feedback Provenance Census (ch. 2); M-1 criterion, Concordance Index, edge jitter, complementary assignment, aggregate breakers (ch. 3); Competence Reserve and reserve ratio (ch. 4); cognitive custody (ch. 5); signature capacity, verification receipts, consent budget, threat-image projection (ch. 6); right to be the ground truth and ground-truth quota (ch. 7); citizen audit standing (ch. 8); readability ceiling and complexity brake (ch. 9); legible twin (ch. 10); Explanation Levy and comprehension debt ratio (ch. 11); cognitive trade balance and right to think (ch. 12); slow money (ch. 13); RAP for Minds and the dead's share (ch. 14); moral hedging budget (ch. 15); covenant inheritance (ch. 16).
