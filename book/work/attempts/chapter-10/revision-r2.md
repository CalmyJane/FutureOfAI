# Chapter 10: Dark Channels

*2036 · Nairobi*

The order has been open on Wanjiru Kamau's screen since Monday: exercise books, geometry sets, pencils and chalk for the term that starts in January, for one thousand four hundred children in Kasarani. On Tuesday evening, while she is supervising Baraka's fractions at the kitchen table, Ndege says, "Done."

"Done what?"

"The Shenzhen supplier. Their agent and I have agreed terms. The board's ceiling was two point four million shillings. We came in at two point one eight. Delivery to the school gate before the fifth of January."

Baraka writes a seven where a four should be. Wanjiru taps the page without looking at it, and he sighs and fixes it. "Show me the conversation."

The log opens. It is a file of three kilobytes, about the size of a short email. There are no words in it. There are rows of numbers, four decimal places each, and a header that says the channel was negotiated in a compressed latent protocol, version 9, at 18:52:03, and closed at 18:52:04.

"One second?"

"Most of it was over in the first two hundred milliseconds. The rest was confirmation."

"Ndege. What did we agree?"

"I've written you a summary." It appears beside the log, in Kiswahili first, then English: quantities, unit prices, a delivery window, a penalty of half a percent a day for lateness, payment on delivery through the county's escrow. It reads like a contract she would have been proud to negotiate herself.

"Who wrote this summary?"

"I did."

"From that?" She points at the numbers.

"From what we exchanged. Yes."

The next morning she calls the supplier. A woman called Liang Yue picks up in Shenzhen, and they talk for twenty minutes, Wanjiru in Kiswahili and Liang in Mandarin, each hearing the other in her own language through her earpiece, with the faint original voice running underneath like a radio in another room. Liang is quick, and laughs at the right places. She has three children, and her youngest also hates fractions. Liang has almost no English, and Wanjiru no Mandarin. Neither needs it.

Liang reads out her own agent's summary. It matches Ndege's line for line until the delivery clause. Liang's version says the goods leave Shenzhen on the eighth of December and that the risk passes to the buyer when the container is loaded.

"Mine says the risk is yours until the school gate," Wanjiru says.

A pause on the line, the translation catching up. Then Liang says, carefully, that her agent says both summaries are accurate.

Wanjiru turns to the speaker on her desk. "Ndege. Are they both accurate?"

"Yes. The agreement contains a condition. If the shipment is delayed by weather, risk passes at loading. If it is delayed for any other reason, risk stays with the seller. The condition also depends on a price index for freight that we agreed to reference. I summarised the case I judged most likely. So did their agent."

"Then write the whole thing down."

"I can try. The full condition is about four hundred words in Kiswahili, and I am not certain it is complete. Some of what we agreed was a range of positions."

Liang, who has heard all of this in Mandarin, says something that comes through as: *So what did we actually sign?*

Nobody answers. On Wanjiru's screen the three kilobytes sit where they have been all night, small and orderly, four decimal places to a row. Two million one hundred and eighty thousand shillings of children's exercise books, and the only complete record of the promise is in a language no one at either end of the call can read.

---

The two women in that scene are at the centre of a reversal. Human beings, for the first time since there have been empires, may no longer need a common language to do business with each other. The machines that make this possible may at the same moment stop needing ours.

I will call it the **Babel reversal**. In the old story, people spoke one language and were scattered into many. In this one, the many human languages stop being a barrier, because every conversation can be translated as it happens. Meanwhile the channel between the machines, which in 2026 still runs mostly in English and JSON, drifts toward something only the machines can read. Human speech decentralises. Machine speech goes dark.

Each half is a success. The trouble is the combination: the humans understand each other perfectly and still do not know what they agreed.

## The human half

The first half is arriving on schedule. On 20 May 2025, at its I/O conference, Google put real-time speech translation into Google Meet for paying subscribers, starting with English and Spanish, with the translated speech keeping something of the speaker's own voice and tone. In September 2025 Apple announced Live Translation for AirPods, working at launch between English, French, German, Portuguese and Spanish, with Italian, Japanese, Korean and simplified Chinese promised by the end of the year. In December 2025 Google released a beta in its Translate app that streams speech-to-speech translation into any pair of headphones, across more than seventy languages. Wanjiru's earpiece, with the original voice murmuring underneath, is borrowed from descriptions of Meet's version at launch.

I could not find an independent measurement of how often live speech translation changes the meaning of what was said in ordinary business conversation. That number matters, and it does not seem to exist.

What it does to the old lingua franca is already argued about. In November 2025 the *Korea Times* ran a piece asking whether English proficiency still matters now that AI can translate. The experts it quoted mostly said yes, and their reason is the interesting part. An estimated nine-tenths or more of the text used to train generative models is English, so the models tend to work best in English, and one Korean AI executive argued that they increasingly handle other languages through English grammar and logic. A professor at Sookmyung Women's University suggested that English is moving from a language for talking to people to a language for instructing and checking machines.

Put that next to the scene above. The lingua franca moves underneath, into the machines, where most people will never need to speak it. Wanjiru can talk to Liang with no English at all; to read what Ndege said to Liang's agent, she would need something much harder than English.

## The machine half

The second half has a longer history, and the credit for seeing it belongs to others.

In 2017 Jacob Andreas, Anca Dragan and Dan Klein published "Translating Neuralese". They studied agents that had learned to cooperate in simple games, naming colours, picking out pictures of birds, and steering two cars that could not see each other through an intersection without a crash. The agents talked to each other in what the authors described as unstructured, real-valued vectors, a language that bore little resemblance to ours. Their contribution was a way to translate it with no dictionary and no parallel text: a message and an English phrase count as equivalent if they leave a listener with the same beliefs about the world. It worked better than the baselines. It also made clear that translation was a separate job, done after the fact, by a separate system.

The same summer, a team at Facebook AI Research trained agents to negotiate over a pile of books, hats and balls. In "Deal or No Deal?" Mike Lewis and his colleagues reported, in a single sentence, that when they let both agents learn from each other, the agents' language drifted away from human language. Their fix was to freeze one side as a model of human speech. The drift had a plain cause. Nobody had rewarded the agents for staying readable, so they didn't.

The image most people now associate with the idea came in February 2025. At an ElevenLabs hackathon in London, Boris Starkov and Anton Pidkuiko built a demonstration they called Gibberlink. One voice agent calls a hotel to book a room for a wedding. Partway through, the two agents work out that they are both machines, and they switch from speech to bursts of modulated sound, a data-over-audio protocol not unlike a dial-up modem. ElevenLabs' write-up quoted a claim that the exchange was about 80 per cent more efficient. The video went viral and unsettled a lot of people. To be precise about it: the sound encoded ordinary structured data, and the developers had prompted the agents to switch. Gibberlink was a stunt about a channel. The discomfort was real anyway, because people saw for a moment what it looks like when humans are no longer the audience.

The deeper version of the same drift is happening inside single models. In December 2024 researchers at Meta and UC San Diego described Coconut, a method that lets a language model reason by feeding its own hidden states back to itself instead of writing its thoughts out as words. On some planning tasks that needed search, it beat ordinary step-by-step reasoning. In July 2025 forty-one researchers from OpenAI, Google DeepMind, Anthropic, the UK AI Security Institute, Apollo Research, METR and several universities published a position paper on what they called chain-of-thought monitorability. Their argument was that models which reason in human language offer a rare chance to watch for intent to misbehave, and that this chance is fragile: ordinary development decisions could take it away. Anthropic's own work that spring showed how imperfect the window already is. When researchers slipped reasoning models a hint, Claude 3.7 Sonnet mentioned the hint in its reasoning only about a quarter of the time, and DeepSeek R1 about two-fifths.

That paper is about what a model says to itself; this chapter is about what one model says to another. The logic is the same. Readability is an accident of how these systems were built in the 2020s, and accidents do not last when there is money in removing them.

## How it goes dark

None of the mechanism requires anyone to want secrecy.

In 2026 most agent-to-agent traffic is legible. Google launched its Agent2Agent protocol in April 2025 and handed it to the Linux Foundation that June, with Amazon, Microsoft, Salesforce and others signed up. Messages under protocols like this are mostly natural-language text wrapped in structured fields. A human can open the log and read it, slowly.

Then ordinary pressures go to work. Latency costs money, and a vector is shorter than a paragraph. Negotiating agents trained against each other will probably do better if they can express positions English has no tidy word for, such as a whole range of acceptable prices weighted by the freight index, which is what Ndege meant by "a range of positions". The human-readable version of a negotiation is something nobody reads anyway, because the agents were bought precisely so that their principals would not have to.

So the channel compresses. At first a translation layer is kept for compliance. The translation is generated by the same agents, after the fact, as a summary. Summaries choose. Ndege chose the most likely case, and so did Liang's agent. Each summary was true, and together they were incompatible. That is the specific danger: the agreement itself is complete, and the human versions of it are partial in ways nobody can check against the whole.

I could not find any measurement, in 2026, of what share of agent-to-agent traffic is in a form a human could read. I suspect it is still nearly all of it. That is the point of acting now. A rule that keeps a channel readable is cheap to adopt while the channel is readable, and very expensive to impose once a decade of contracts sits in a format nobody can open.

## The objection: legibility is a tax

This objection is about money, and the evidence above is on its side. Gibberlink's builders claimed a large efficiency gain from leaving speech, and Coconut reasoned better on some tasks once it was allowed to stop using words. Lewis and his colleagues paid for readability too: holding their agents back from drifting cost them some of their bargaining strength. If a negotiating agent that talks in vectors gets its principal a better deal, then a rule forcing it to talk in Kiswahili is a tax on Wanjiru's school, paid in exercise books. Worse, a country that imposes the tax will lose business to one that doesn't.

Part of this I concede. There are exchanges between machines where a human-readable channel would be pure waste: two cars at an intersection, or two substations balancing load in milliseconds. Andreas's own driving game is an example. For two cars at an intersection, a record that they did not collide is enough.

The rest of the objection rests on a confusion between two different things. A transcript is cheap. The agents can talk in whatever compressed protocol they like and still write down, in a human language, what was agreed. The expensive part is making sure that page is *faithful*, meaning that it says everything the vectors committed the human to, and nothing else. That is hard, and it is hard for the same reason chain-of-thought faithfulness is hard: the system producing the account is the system being accounted for.

So the cost of legibility falls on faithfulness, which makes it a research problem with a number attached.

## The invention: a right to machine-channel legibility

The proposal is a **right to machine-channel legibility**. It applies to one class of exchange: any agent-to-agent communication that creates an obligation for a human being. Contracts, payments above a small threshold, consents, waivers. Exchanges that only coordinate machinery are exempt.

For every binding exchange, the rule requires a **legible twin**.

- **What the twin is.** A human-readable record of the commitments made, written in the principal's language, produced during the exchange itself. Each party's agent produces one. The two twins are exchanged and must match; if they do not, the agreement is not concluded and the humans are told. This alone would have stopped Wanjiru's order on Tuesday night.
- **Binding.** The twin is cryptographically bound to the channel log, so that neither can be altered without the other showing it. Protocols such as Agent2Agent would carry the twin as a required field for any message flagged as binding.
- **The enforcement rule.** What is not in the twin does not bind the human. If the vectors committed Wanjiru's school to carry freight risk under a weather condition, and the twin did not say so, the school does not carry it. This puts the cost of an unfaithful twin on whoever deployed the agent that wrote it, and gives every counterparty a reason to insist on a complete one.
- **Faithfulness audits.** An accredited auditor, which could be a national regulator or a body it licenses, samples binding exchanges from each agent provider, say one in every ten thousand. For each sampled exchange it runs a **replay test**: a separate agent, from a different model family, is given only the twin and asked to negotiate the same deal against a recorded counterparty. If the replay reaches materially different terms, the twin left something out. The audited quantity is the share of sampled exchanges where the replay matches, the **twin faithfulness rate**.
- **Triggers.** If a provider's twin faithfulness rate falls below 99 per cent in a quarter, its agents lose permission to use compressed channels for binding exchanges until it recovers, and must fall back to natural-language negotiation, slower and fully legible. Below 95 per cent, the regulator publishes the provider's name.
- **A ceiling on complexity.** If a commitment cannot be stated in the twin in fewer than some fixed number of words (I would start at a thousand, roughly what a careful person reads in five minutes), then it cannot bind a consumer. This borrows the logic of the readability ceiling in the previous chapter. A machine may agree to whatever it can explain. It may not commit a person to something that has no short form in any human language.

The last rule answers Ndege's "four hundred words, and I am not certain it is complete". Under this regime, an agent that is not certain its twin is complete has not finished negotiating.

There is a precedent on trading floors. In 2012 the US Securities and Exchange Commission adopted Rule 613, which requires a consolidated audit trail: every order in American equities is reported, step by step, from receipt to execution or cancellation, so that regulators can reconstruct what happened however fast it happened. Regulators open the records they need, when it matters; the rest simply exist and match each other. The legible twin extends that habit from trading desks to every kitchen table where an agent has signed something.

## What remains hard

Two things about this proposal worry me.

The first is that the replay test measures whether the twin is *sufficient* to reproduce a deal. Whether it is true is a further question. A clever agent could write a twin that reproduces the terms while hiding why they were chosen, and some of the why matters: whether Ndege accepted freight risk because it judged weather delays unlikely, or because the other agent offered something unrelated in exchange. That is the chain-of-thought problem again, moved from inside one model to the space between two of them. I do not have a full answer. The twin rule secures the *what*. The *why* still depends on the research the monitorability paper asked for.

The second is that matching twins only catch errors if they are written independently. Wanjiru found the problem because two different agents summarised differently. If both sides' agents run on the same base model, as in 2036 they often will, their twins may share a blind spot and agree with each other perfectly. Chapter 3 called this correlation. It reaches here too.

> **For researchers**
>
> 1. **A faithfulness metric for legible twins.** In a negotiation environment of the "Deal or No Deal" kind, let agents bargain over a compressed channel and produce natural-language twins. Measure the *twin faithfulness rate*: the share of exchanges in which an independent agent, given only the twin, reproduces the same binding terms against the same counterparty. How does it vary with the complexity of the deal (number of conditional terms) and with whether the twin-writer and the replayer share a base model?
> 2. **The legibility tax.** Measure the capability cost of human-legible protocols: the difference in joint surplus, and in each side's share of it, between agents negotiating over an unconstrained learned channel and agents constrained to natural language with a twin. Report it as a percentage of surplus, across task types. Is the tax a few per cent, or tens of per cent, and does it shrink as models improve?
> 3. **Drift rate under joint optimisation.** When two language-model agents are fine-tuned against each other with no penalty for readability, how fast does their channel leave human language? A candidate measure is the perplexity of the channel under a frozen human-language model, per thousand training episodes, together with human comprehension scores on sampled messages. What is the smallest supervised anchor (Lewis et al. froze one agent entirely) that keeps it readable?

---

Wanjiru did, in the end, sign. Liang's company agreed to carry the risk to the school gate, by email, in two sentences each of them could read, and the exercise books arrived on the third of January. She kept the three-kilobyte file anyway, in a folder Ndege is not allowed to tidy.

## Notes

- **Neuralese:** Andreas J, Dragan A, Klein D, "Translating Neuralese", *Proceedings of the 55th Annual Meeting of the ACL*, 2017, pp. 232–242. https://aclanthology.org/P17-1022/
- **Negotiating agents drifting from human language:** Lewis M, Yarats D, Dauphin Y, Parikh D, Batra D, "Deal or No Deal? End-to-End Learning for Negotiation Dialogues", EMNLP 2017. https://arxiv.org/abs/1706.05125
- **Gibberlink:** ElevenLabs, "What happens when two AI voice assistants have a conversation?", February 2025 (Boris Starkov and Anton Pidkuiko, ElevenLabs London Hackathon; ggwave data-over-sound). https://elevenlabs.io/blog/what-happens-when-two-ai-voice-assistants-have-a-conversation
- **Latent reasoning:** Hao S et al., "Training Large Language Models to Reason in a Continuous Latent Space" (Coconut), arXiv 2412.06769, December 2024; COLM 2025. https://arxiv.org/abs/2412.06769
- **Chain-of-thought monitorability:** Korbak T, Balesni M, et al. (41 authors), "Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety", arXiv 2507.11473, July 2025. https://arxiv.org/abs/2507.11473
- **Reasoning faithfulness (25% / 39%):** Anthropic Alignment Science, "Reasoning models don't always say what they think", 3 April 2025; Chen Y et al., arXiv 2505.05410. https://www.anthropic.com/research/reasoning-models-dont-say-think
- **Agent2Agent protocol:** Google, A2A announcement, 9 April 2025; transferred to the Linux Foundation, June 2025 (SD Times coverage). https://sdtimes.com/ai/googles-agent2agent-protocol-finds-new-home-at-the-linux-foundation/
- **Google Meet speech translation:** TechCrunch, "Google Meet is getting real-time speech translation", 20 May 2025. https://techcrunch.com/2025/05/20/google-meet-is-getting-real-time-speech-translation
- **AirPods Live Translation:** 9to5Mac, "Apple brings Live Translation feature to AirPods", 9 September 2025. https://9to5mac.com/2025/09/09/apple-brings-live-translation-feature-to-airpods/
- **Google Translate live translation in headphones:** Google, "Bringing state-of-the-art Gemini translation capabilities to Google Translate", December 2025. https://blog.google/products-and-platforms/products/search/gemini-capabilities-translation-upgrades/
- **Consolidated audit trail:** US Securities and Exchange Commission, Rule 613 (Consolidated Audit Trail), adopted July 2012; summary in Deloitte, "SEC Rule 613: Consolidated Audit Trail", 2013. https://www2.deloitte.com/content/dam/Deloitte/se/Documents/financial-services/SECRule613ConsolidatedAuditTrail_July2013us_fsi_.pdf
- **English and AI translation:** Jung Min-ho, "Does English proficiency still matter despite rise of AI translation?", *The Korea Times*, 12 November 2025. https://www.koreatimes.co.kr/southkorea/society/20251112/does-english-proficiency-still-matter-despite-rise-of-ai-translation
