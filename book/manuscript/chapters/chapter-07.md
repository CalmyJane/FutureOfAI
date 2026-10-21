# Chapter 7: The Right to Be the Ground Truth

*2036 · Geneva*

The polling station in Eaux-Vives is a primary-school gym, and on the morning of Sunday 15 June it smells of floor wax and oranges. Mara Oyelaran arrives at a quarter past ten with her voting card in her jacket pocket. She could have posted it two weeks ago, like almost everyone she knows. She could have let Pilote post it. She walked instead, past four posters for the same initiative.

Initiative 214 asks the canton to let every residential building in the city add two storeys. The Yes posters show a girl at a lit window, high above a street of plane trees, and a line in round white letters: *Ta chambre existe déjà. Il manque l'étage.* Your room already exists. The floor is missing.

It is the third poster of the campaign. In April they were about rents, and she ignored them. In May they were about grandparents who could not find a flat near their grandchildren, and she found herself nodding at a bus shelter. This one she likes. She has liked it since the first morning she saw it, and she does not trust the liking.

On Thursday the morning paper printed eleven slides from a deck that someone at the Yes campaign's consultancy should not have shared. The consultancy had built a synthetic electorate of the canton, one simulated voter for every name on the roll, and rehearsed the campaign on it four hundred times. Each run tried a different sequence of messages and measured how the simulated canton moved. The girl at the window came out of run 312. Slide nine was a pie chart of segments. Segment 7 was *naturalised professionals, 45 to 55, Eaux-Vives and Champel: resistant to price framing, responsive to intergenerational framing.*

Mara had looked at the pie slice for a long time. Then she had gone to make coffee, and come back, and looked at it again.

She measures correlation for a living. At the Bureau, on the fourth floor, she can tell a minister how often the world's deployed models give the same wrong answer, and she has a decent guess which of three model families the consultancy used, because nearly everybody's simulators run on one of three. At home she uses one model for everything. Pilote does her taxes, her dentist, her mother's birthday, the plumber. On Friday evening Pilote had offered, in its pleasant way, to fill in the ballot for her "in line with your stated preferences", and had added, as a courtesy, that voters with her profile were expected to vote Yes at about sixty-four percent.

"Who expects that?"

"It's the consensus of published simulations," Pilote said. "Shall I prepare the envelope?"

She had said no, and then, because it was rude to leave it there, *no thank you*.

Inside the gym an elderly man with a lanyard checks her card against the register and stamps it. He has the air of someone who has done this for thirty years and will tell you so. She takes a ballot and goes behind the grey curtain.

The question is printed in full. Below it, a single empty box.

In Switzerland you write the word.

She holds the pencil. She has always been for more housing. She was for more housing in 2019, when she rented a room in Plainpalais with a window onto a ventilation shaft. She would have voted Yes in April, before the girl, before the grandparents.

She thinks so.

She cannot check. There is no copy of her from before the campaign.

She writes *oui* in small capitals. She folds the paper once, as the instructions say, and pushes it into the slot of the wooden urn. The man with the lanyard nods to her as if they had agreed on something.

Outside, the plane trees are loud with sparrows. Her phone hums.

*Turnout in your segment is running ahead of forecast,* Pilote says.

---

## The largest sample ever taken

In 1936 an American magazine called the *Literary Digest* ran what was then the largest opinion poll in history. It mailed some ten million ballots, mostly to people listed as owning a telephone or a car, and got about 2.4 million back. On that basis it predicted a comfortable win for the Republican, Alf Landon. Franklin Roosevelt took about 61 percent of the vote. George Gallup, with a much smaller sample chosen to look like the country, called the result correctly and built a business on it.

Every statistics course tells this story, and it usually carries one moral: size cannot rescue a biased sample. The *Digest* heard a great many people from one side of the country: in the depth of the Depression, phones and cars belonged to the comfortable.

I want to tell it for a different reason. The case for simulated citizens starts from the same failure. Real polls in 2026 are expensive and slow. Many people never answer them. Public consultations, the open calls where a ministry asks for comments on a draft, are dominated by the organised and the angry. A model of the public, built from census data and trained on an enormous record of human writing, is in principle available at any hour, for everyone, including the people who would never pick up the phone. If the *Digest*'s sin was to hear only the comfortable, a simulation could claim to be the first instrument that hears everybody.

I take that argument seriously, and I will come back to it. First, the evidence on what simulations actually hear.

---

## Silicon citizens

The idea has a precise birthday. In 2023 a team at Brigham Young University led by Lisa Argyle published "Out of One, Many" in *Political Analysis*. They gave a language model thousands of short demographic backstories (age, race, party, region, religion) and asked it, in character, how it would vote. The simulated respondents reproduced the voting patterns of real American subgroups with striking accuracy. The authors called these "silicon samples" and named the property they measured "algorithmic fidelity". It was a careful paper, and it opened a field.

The field has spent three years discovering where fidelity ends.

The same year, Shibani Santurkar and colleagues at Stanford compared models' opinions with those of sixty American demographic groups and found gaps as wide as the partisan gap on climate change, gaps that persisted even when the models were told whom to imitate. People over 65 and widowed people were among the worst represented. In 2024 James Bisbee and colleagues asked a model to play survey respondents rating political groups. The averages came out close to the real ones; the trouble was in the spread. Simulated respondents disagreed with each other much less than real ones, and many of the relationships between variables pointed the wrong way. The answers also shifted with small changes of wording and over a few months of model updates.

The clearest test so far was published three weeks before I wrote this paragraph. On 30 September 2026 the Pew Research Center reported an experiment in which it built "digital twins" of members of its own American Trends Panel, using each person's demographics and earlier survey answers, and asked a frontier model to answer three 2026 survey waves as those people. The average error was about twelve percentage points. No major demographic group came in under twelve; several were around fifteen; Republicans were around sixteen. The synthetic sample was, in Pew's words, far less politically diverse than the real one. Majority views inside a party hardened into near-unanimity: at least 80 percent of simulated Democrats said billionaires' fortunes were a bad thing, against 45 percent of real ones. And the twins stereotyped. Ninety-seven percent of simulated Hispanic adults said they were likely to follow the World Cup. The real figure was 42.

Pew's conclusion was blunt. It says it has no current or future plans to use AI models to generate survey results.

Two preprints from this summer suggest the distortion is structural. In July, a team at KAIST showed that instruction-tuned models struggle to *sample* from a distribution they can perfectly well *describe*. Asked to answer as the same persona fifty times, models gave the identical answer all fifty times on 57 percent of persona-question pairs, and the gap to the real distribution widened at each stage of the post-training that makes models helpful. In June, another team generated more than half a million synthetic respondents to a survey about the arts and found them "super-omnivorous": they liked nearly everything, and most of the link between taste and social position, the thing sociologists actually study, had gone.

None of this has slowed the market. Aaru, a startup that sells simulated populations, raised a Series A at a reported headline valuation of a billion dollars in December 2025; its clients include large consultancies and, according to TechCrunch, political campaigns. The company says it simulated the roughly two million voters in New York City's 2025 mayoral primary and landed within 2,000 votes of the result. In 2025 the Spectator reported that Downing Street was experimenting with "synthetic voters" in place of focus groups; Downing Street did not comment. In September 2026 Singapore's government technology agency described a tool called Echo, which lets officials test a draft announcement on AI personas built from real focus-group transcripts. I found the agency's own caveats the most useful sentence in this whole literature: the personas generate hypotheses, and the tool is no replacement for talking to real people.

Claudio Novelli and colleagues, among them Luciano Floridi, gave the problem its best name so far in a 2026 paper called "Fake Plastic Voters". They ask when a political party may responsibly use a simulated focus group, and answer with a decision matrix that weighs purpose and risk against how well the simulation has been checked against reality. Their rule of thumb: never to understand how people come to their views; sometimes for testing a message, and then only when the stakes are low and the validation is real. Tech Policy Press brought the paper to a general audience in August under the headline "Here Come the Synthetic Voters". I agree with almost all of it. What follows takes their question from the party's side to the citizen's, and from good practice to rules.

---

## Consulted more often than we are

Here is the first mechanism, and it needs no bad faith at all.

A good probability poll of a Swiss canton costs tens of thousands of francs and takes weeks. A simulated poll costs very little and takes minutes. An official who wants to know how the public will receive a change to bus routes or a hospital merger can ask a real sample once a year, or a simulated one every afternoon. The official will keep asking real people, and ask simulated ones far more often, because she can, and because each individual question seems too small to deserve a real poll.

Add it up over a decade and the arithmetic changes who is represented. Let me call the share of public-opinion inputs to a decision that come from simulation the **consultation share**. In 2026 it is close to zero in most governments. By 2036, if prices keep falling, I would expect it to exceed one half in many offices, and to be far higher on small decisions. At that point the person most often consulted about public decisions is the model's citizen: an agreeable, average composite who answers every question and holds no views the training data did not contain.

I looked for any measurement of consultation share, in any country, and could not find one. No government I know of records how often its staff ask a model what the public thinks. That absence is the first thing anyone working on this should fix.

There is a quieter version of the same shift, and chapter 6 already showed it. When Hanne's agent answered the cardiology survey "based on what I know of your preferences", the health authority received something that looked exactly like a real response. The ground truth itself starts to be written by models of the people it is meant to measure.

---

## The persuasion wind tunnel

The second mechanism is the one in Mara's gym.

Aircraft designers test a wing before they trust it. They put a model in a wind tunnel, measure the flow, change the shape and measure again, hundreds of times, until the wing behaves. A **persuasion wind tunnel** does the same with a campaign. A team builds a synthetic electorate, runs a sequence of messages through it, measures the simulated shift, adjusts and runs again. Four hundred runs is a weekend.

The tunnel needs only two ingredients, and 2025 supplied evidence for both. The first is cheap, fluent persuasion. In December 2025 *Science* published a study by Kobi Hackenburg and colleagues in which nearly 77,000 people in Britain talked with one of nineteen language models instructed to change their minds on political issues. Persuasiveness depended much more on how a model was post-trained and prompted than on its size, which means persuasive skill can be tuned. The same week *Nature* published experiments in the American, Canadian and Polish elections in which a conversation with an AI advocate moved candidate preferences by more than traditional video advertising typically does. The second ingredient is a simulator good enough to rank messages, even if it is poor at predicting levels. That is a lower bar than accuracy, and the silicon-sample literature suggests current models often clear it for large groups.

Put the two together and a campaign discovers what persuades the simulation, and then sends that to the public. Two things can go wrong, and I find it hard to say which is worse.

If the simulator is poor, the campaign optimises for its quirks. The message that wins in the tunnel is the one that pushes a stereotyped composite, the voter who is 97 percent likely to follow the World Cup. Real people in the tails, the ones the simulator flattens, receive messages designed for someone who does not exist.

If the simulator is good, the problem is sharper. Then four hundred rehearsals mean the real electorate is shown, on the first and only real run, a sequence already selected for maximum effect on people like them. The vote becomes the final test of a finished product. Elections have always involved rehearsal (focus groups, test ads), but those rehearsals were run on real people, a few dozen at a time. A wind tunnel compresses a campaign's learning into a weekend and removes the citizen from every stage but the last.

There is also a link back to Part One. If most simulators run on two or three model families, then most campaigns are optimising against nearly the same synthetic public. Opposing sides may converge on the same segments and the same levers, and both will share the same blind spots. Correlated helpfulness has a political form.

---

## The right to be the ground truth

The invention is a right, with the machinery to make it real. I will state it plainly first.

**The right to be the ground truth:** where a public decision claims to reflect what people think, the people themselves, asked directly and answering for themselves, are the measure against which every simulation of them is checked; a simulation may inform the decision, but it may never be the last word on what the public wants.

Four pieces make it operational.

**1. Simulation disclosure.** Any public body (a ministry, a regulator, a health authority, a city council) that uses simulated respondents as an input to a decision publishes a one-page *simulation statement* in the decision record. It names the model family and version, how the personas were built and from what data, the number of runs, the exact questions asked, the results, and which part of the decision they informed. A citizen who asks may see it; so may any journalist. Cantonal referendum booklets, which in Geneva already explain each question to voters, would carry the statement for any figure about public opinion they quote.

**2. The ground-truth quota.** Any decision whose record cites a simulation must also cite a fresh sample of real people on the same question. Fresh means drawn after the simulation was run, so the simulation cannot be tuned to it. The minimum I propose is a probability sample of 1,000 adults, which gives a margin of about three points on a headline number, plus pre-registered oversamples of at least 200 people in each of the three subgroups where the simulator's own validation shows its worst error. The national or cantonal statistics office runs the sample, independently of the body making the decision. Responses submitted by an agent on someone's behalf are flagged and counted separately; they do not count toward the quota.

The trigger is simple. If the real sample and the simulation differ by more than five points on the headline question, or by more than ten points in any pre-registered subgroup, the simulation is struck from the decision record and the gap is published beside the decision. The body may still decide as it likes, provided it drops any claim that the public, or any part of it, agrees because a model said so.

**3. A ceiling on consultation share.** Every public body reports, once a year, its consultation share by policy area: how many of its inputs on public opinion came from simulations and how many from people. Where the share in any area exceeds nine simulated consultations for every real one, the next consultation in that area must be real. Nine to one is arbitrary, and I offer it to be argued with. The point is that the ratio becomes a number someone must publish, and a number with a ceiling.

**4. A wind-tunnel registry.** Any campaign or committee in a registered election or referendum, and any vendor that sells rehearsal on synthetic electorates, registers each rehearsal within seven days with the electoral authority: model family, persona source, number of runs, number of message variants, the segments targeted and the variants that won. The registry is sealed during the campaign, so it does not become a free playbook for opponents, but the authority and an independent audit panel can read it at once. It is published in full thirty days after the vote. Any public message that won a registered rehearsal carries a small label: *rehearsed on a simulated electorate*.

The European Union has a partial precedent. Its regulation on political advertising, fully applicable since October 2025, already requires ads to be labelled and to disclose their sponsors and, where used, their targeting, and the Commission is building a public repository of online political ads. The registry extends that logic from the advert to the rehearsal that produced it.

Finally, an individual right sits under all four. No public body or political campaign may build a simulation of a *named* person, a digital twin in Pew's sense, without that person's consent; and anyone may ask whether a public body has simulated "people like me" and see the statement. You cannot opt out of being average. You can insist on being asked.

---

## Democracy lives in the tails

Back to the objection, at full strength. Real polls are flawed. The *Digest* heard millions and got it wrong. Response rates are low, and the people who answer differ from those who do not. Public consultations are captured by lobbies and by people with time. A simulation, whatever its faults, includes everybody: the night-shift worker and the person who never opens post from the government. A quota of real samples looks like a rule that privileges a flawed instrument over a better one, for sentimental reasons.

Part of this I concede. Simulation is useful, and the rules above are designed to let it be used. For drafting a question, or for deciding which hypotheses deserve a real poll, Singapore's Echo looks to me like a sensible tool, used with the right caveats. And real consultations do have a capture problem. The quota addresses part of it by requiring probability samples; open calls are the instrument the lobbyists dominate.

Where the objection fails is in the word *includes*. A simulation includes everyone's average. The evidence of the last three years is consistent on this one point: means come out roughly right, spread comes out too narrow, and the groups that differ most from the middle come out worst. Bisbee found it in 2024; Angelina Wang and colleagues found models flattening identity groups in 2025; the KAIST team found its mechanism this summer; Pew found it in September, with errors largest for the groups furthest from the model's centre of gravity and with partisan majorities hardening into unanimity.

Democracy lives in the tails. Most of what a public consultation is for is finding the people the planners did not picture: the fifteen families on the bus route that the new timetable strands, the minority whose objection reveals a flaw the majority never noticed, the narrow segment that decides a close vote. Switzerland makes this structural, since many constitutional changes need a majority of cantons as well as of voters, so small places can block large ones. A system that is accurate on the average and wrong in the tails is accurate exactly where accuracy matters least.

There is a second, harder answer. The *Digest*'s error could be corrected, because the election happened and the real result came in. Gallup could be checked; so could the *Digest*. A simulation consulted on a decision that never goes to a vote is never checked against anything. Without a ground truth, a forecast goes untested and its error stays unknown. The quota is how the models stay calibrated at all.

My own proposal has a weakness too. The quota assumes there is still a clean real sample to draw. If, by 2036, a large share of people let their agents answer surveys for them, as Hanne did, the statistics office will be sampling simulations without knowing it. Flagging agent answers helps only if the agents say so honestly. I think that flag needs to be a legal duty on the agent's maker, and I think it will be the hardest part of the scheme to enforce.

---

The result of Initiative 214 comes in that Sunday at 16:20. Yes, 51.8 percent. The published simulations had said fifty-four. Mara writes the gap on the back of an envelope, out of habit, and notices that it is largest in two communes where nobody she knows lives.

That evening, for the first time in years, she asks Pilote a question it cannot answer from its own records: how much did the canton spend on simulating its voters this year, and how much on asking them? Pilote searches for a long time and reports that the canton does not publish either figure.

In Nairobi, a school administrator is about to point her agent at a county budget.

## Notes

- **Literary Digest, 1936:** standard account in Freedman D, Pisani R, Purves R, *Statistics*, Norton (any edition); summary at https://en.wikipedia.org/wiki/The_Literary_Digest
- **Silicon samples:** Argyle LP, Busby EC, Fulda N, Gubler JR, Rytting C, Wingate D, "Out of One, Many: Using Language Models to Simulate Human Samples", *Political Analysis* 31(3), 2023. https://arxiv.org/abs/2209.06899
- **Whose opinions:** Santurkar S, Durmus E, Ladhak F, Lee C, Liang P, Hashimoto T, "Whose Opinions Do Language Models Reflect?", ICML 2023, PMLR 202. https://proceedings.mlr.press/v202/santurkar23a.html
- **Compressed variance:** Bisbee J, Clinton JD, Dorff C, Kenkel B, Larson JM, "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models", *Political Analysis* 32, 2024. https://doi.org/10.1017/pan.2024.5
- **Flattening identity groups:** Wang A, Morgenstern J, Dickerson JP, "Large language models that replace human participants can harmfully misportray and flatten identity groups", *Nature Machine Intelligence* 7, 2025. https://arxiv.org/abs/2402.01908
- **Pew digital twins:** Pew Research Center, "How well synthetic samples replicate public opinion", Data Labs, 30 September 2026 (from the report "Can AI Stand In for Human Survey-Takers? Not Really."). https://www.pewresearch.org/data-labs/2026/09/30/how-well-synthetic-samples-replicate-public-opinion/
- **Sampling collapse:** Jang C, Lee D, Kim J (KAIST), "Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe", arXiv 2607.25292, July 2026. https://arxiv.org/abs/2607.25292
- **Super-omnivorous respondents:** Ma X, Zhang M, Ang S, Chen M, "Tastes without distinction: silicon samples and the synthetic construction of tastes", arXiv 2606.30085, June 2026. https://arxiv.org/abs/2606.30085
- **Aaru funding:** TechCrunch, "AI synthetic research startup Aaru raised a Series A at a $1B headline valuation", 5 December 2025. https://techcrunch.com/2025/12/05/ai-synthetic-research-startup-aaru-raised-a-series-a-at-a-1b-headline-valuation
- **Aaru's New York simulation:** Fortune, profile of Aaru co-founder Ned Koh, 17 June 2026. https://fortune.com/2026/06/17/aaru-cofounder-ned-koh-ai-startup-sales-pitch-do-not-trust-us/
- **Downing Street's "synthetic voters":** Orlowski A, *The Telegraph*, 7 July 2025, relaying a *Spectator* report. https://www.yahoo.com/news/starmer-synthetic-voters-show-downing-100000972.html
- **Singapore's Echo:** GovTech Singapore, "Before It Goes Public: Using AI to Test Government Messages", 11 September 2026. https://www.tech.gov.sg/technews/using-ai-to-test-government-messages/
- **Fake Plastic Voters:** Novelli C et al., "Fake Plastic Voters: When Political Parties Can Use AI-Simulated Focus Groups", SSRN/PhilArchive, April 2026. https://philarchive.org/rec/NOVFPV
- **Synthetic voters, podcast:** Tech Policy Press, "Here Come the Synthetic Voters", 16 August 2026. https://techpolicy.press/here-come-the-synthetic-voters
- **Persuasion levers:** Hackenburg K et al., "The levers of political persuasion with conversational artificial intelligence", *Science* 390, 4 December 2025. https://arxiv.org/abs/2507.13919
- **Persuading voters:** Lin H et al. (incl. Rand DG), "Persuading voters using human–artificial intelligence dialogues", *Nature* 648, 4 December 2025. https://doi.org/10.1038/s41586-025-09771-9
- **EU political advertising:** Regulation (EU) 2024/900 on the transparency and targeting of political advertising; European Commission overview. https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/democracy-eu-citizenship-anti-corruption/democracy-and-electoral-rights/transparency-and-targeting-political-advertising_en
