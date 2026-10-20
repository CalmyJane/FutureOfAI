# Chapter 2: The Funnel

*2036 · Bengaluru*

The rain arrives at half past six, as it has every evening this week, and Ravi Menon closes the balcony door on the smell of wet jasmine and diesel. On the laptop, a test match in Chennai has stopped for bad light. On his phone, his nephew Arjun has sent the fourth message of the afternoon.

*Mama, just ask it. It writes these things in ten seconds.*

Arjun wants a reference letter for a master's programme in Toronto. More precisely, he wants a letter from his internship supervisor that says he led a project he mostly watched. The supervisor has agreed to sign whatever Arjun sends, which is how these things work now. Arjun wants his uncle to draft it, because his uncle is good with words. Everyone in the family knows Ravi is good with words. Nobody in the family is quite sure what he does.

Ravi opens the assistant built into his bank's app, because it is the one already on his screen. Its name is Morrow. It is made by Kaya, a lab in Singapore, and he has never rated a single answer for Kaya. In nine years he has worked for four vendors serving five labs, and Kaya was never one of them. He knows this the way a session musician knows which studios he has played in.

He types the request plainly. Leadership, initiative, the project as Arjun's own.

Morrow answers in under a second. It offers to write a strong letter about what Arjun actually did, and lists three things from the internship that would read well. Then it says it won't describe him as leading the project, because a letter like that tends to come apart at the first interview question. *I'd rather be useful than agreeable,* it says. *Here is a version I think will do him more good.*

Ravi reads the sentence again.

He wrote that sentence. He wrote it in March 2028, in a rented room above a bakery in Koramangala, at about eleven at night, for a vendor whose name has since been bought and changed twice. It was example fourteen in a guideline on sycophancy, the part of the rubric that told raters what a good refusal sounded like when a user wanted flattery. He remembers arguing with a project lead about the word "agreeable". The lead wanted "pleasant". Ravi said pleasant was a mood and agreeable was a behaviour, and the behaviour was the problem. He won. He was paid for forty minutes.

He searches his own archive and finds the file in a folder called *old rubrics DO NOT DELETE*. There it is, in the slightly pompous English he used at twenty-nine. *I'd rather be useful than agreeable.* The document is stamped with the vendor's logo and a client code he can no longer decode.

He asks Morrow where the phrase comes from.

Morrow says it doesn't know where its phrasing comes from, and that it may have picked it up in training. It offers, helpfully, to rephrase.

He sits with the phone in his hand. In Carnatic music there is a thing that happens to a teacher when a student's student, a girl from some other city, sings one of the teacher's particular turns in a raga, a little ornament the teacher invented as a young man and never wrote down. It is meant to feel like an honour. Mostly it feels like that. Partly it feels like hearing your own voice on someone else's answering machine.

Outside, the rain is settling into its steady evening rhythm. On the laptop the umpires are walking out to inspect the pitch.

He opens a blank document and starts a list. Vendor, year, client code, phrase. Then he stops, scrolls back up to the top, and types a heading over the empty column he hasn't filled in yet: *Who else?*

---

## A sentence with no return address

The scene is invented, and Ravi is too. The sentence could have travelled.

In the last chapter I argued that the most dangerous property of a population of good agents is that they tend to make the same move at the same time. A natural question follows. Why would agents built by different companies, on different hardware, in different countries, make the same move? Ravi's evening suggests one answer. Somewhere upstream of all those models there may be a shared source of taste, and in 2036 he has just found a fingerprint on it.

I am going to call that shared source **the Funnel**: the preference supply chain of human raters, the vendors who employ them, the judge models that stand in for them, the synthetic data those models produce, and the distillation chains that copy one model's behaviour into another, feeding many labs at once. It is the narrow neck through which a large part of the industry learns how to behave.

The Funnel is not a conspiracy, and no one designed it. It is what you get when a large but finite pool of people and a handful of very good models are the cheapest available source of judgement, and every lab needs judgement at the same time.

## How a model learns manners

A modern language model is built in two broad stages. In the first, pretraining, it reads a vast slice of the public internet and learns to predict the next word. That stage gives it knowledge and fluency. Manners come later. A raw pretrained model will continue your sentence, whether or not that helps you.

The second stage, post-training, is where the manners come from. Here a lab shows the model examples of good answers, and then, crucially, asks people to compare answers. Which response is more helpful? Which is more honest? Which refusal is better judged? Those comparisons train a second model, a reward model, whose job is to predict what the raters would prefer. The language model is then tuned to score well with the reward model. The technique is called reinforcement learning from human feedback, and almost everything users mean when they say a chatbot has a "personality" was shaped in this stage.

The people doing the comparing are raters. In 2026 many of them are not employed by the labs at all. They work for data vendors, firms that recruit, train, test and pay large pools of contractors and sell the resulting judgements to AI companies. They work from written guidelines, the rubrics, which tell them what good looks like. Rubrics have examples. Someone writes the examples.

That is the first channel of the Funnel. There are at least four more, and the newer ones carry more volume than the old one.

The second channel is the judge. Human comparisons are slow and expensive, so labs increasingly ask a strong model to do the comparing. In 2023, a group at Berkeley and elsewhere showed that GPT-4, asked to judge between two chatbot answers, agreed with human preferences more than 80 percent of the time, about as often as humans agree with each other. That paper, by Lianmin Zheng and colleagues, made "LLM-as-a-judge" respectable, and the practice spread. Anthropic had already gone further in late 2022 with a method it called Constitutional AI, in which a model judges its own outputs against a short list of written principles and those judgements train the reward model. In both cases the human raters' influence survives, compressed into the judge.

The third channel is synthetic data. Once a model is good, its outputs become training material for other models. The OpenBMB group's UltraFeedback dataset, released in 2023, contains about 64,000 prompts, each with four answers from different models, every one of them rated by GPT-4 for helpfulness, honesty and the rest. It became one of the most widely used preference datasets in open-source AI. Every model tuned on it learned, at one remove, what GPT-4 preferred.

The fourth channel is distillation, training a smaller or newer model to imitate a larger one's outputs. In March 2023 a Stanford team built Alpaca by fine-tuning Meta's LLaMA on 52,000 instruction-following examples generated by an OpenAI model, for a few hundred dollars. Distillation is ordinary practice inside labs, which use it to make cheap versions of their own models. Between labs it is contested. In February 2026 Anthropic published an account of what it called industrial-scale distillation campaigns by three Chinese labs, DeepSeek, Moonshot AI and MiniMax: more than 16 million exchanges with Claude, through about 24,000 fraudulent accounts. These are Anthropic's allegations, and I can't adjudicate them. One detail, though, describes the Funnel exactly. Some of the DeepSeek traffic, Anthropic said, consisted of rubric-based grading tasks that made Claude act as a reward model for reinforcement learning. That would put one lab's judge inside another lab's training loop.

The fifth channel is the oldest and the least controllable: the public web. A phrase that one model says a million times a day ends up in emails, essays, forum posts and product pages. The next generation of every model pretrains on that web. Ravi's sentence can reach Singapore without a vendor or a distillation pipeline. It can simply be in the water.

## What we can see in 2026

Two research results make the downstream end of the Funnel visible, and they deserve the credit for having seen it first.

In 2025 Elliot Kim, Avi Garg, Kenny Peng and Nikhil Garg published a study of more than 350 language models at ICML. On one leaderboard dataset, when two models both got a question wrong, they chose the same wrong answer about 60 percent of the time. Larger and more accurate models had more correlated errors, even across different architectures and different companies, and models from the same provider were more correlated still. Better models, in other words, are converging.

The same year, Liwei Jiang, Yejin Choi and colleagues named the effect on open-ended questions, where no single answer is right. Their paper, "Artificial Hivemind", collected 26,000 real open-ended prompts and found that different models produced strikingly similar answers to them, more similar than you would expect from systems built separately. Then they looked at the evaluators. They gathered 25 human ratings for each example and found that reward models and model judges were least well calibrated to people precisely where people's tastes differed. The judges track the average and miss the idiosyncratic. A judge that rewards the average, used by many labs, is a machine for producing sameness.

Neither paper claims to have found the cause. Kim and colleagues point to shared architectures and shared providers; Jiang and colleagues point at reward models and judges. What I want to do is follow their suggestion upstream and ask a narrower question. How concentrated is the supply chain of judgement itself?

## The vendors

Here I have to be careful, because the honest answer is that the industry is built not to be seen.

Some things are on the record. In June 2025 Meta paid about $14.3 billion for 49 percent of Scale AI, the best-known data vendor, and hired its chief executive. Within days Reuters reported, citing unnamed sources, that Google, Scale's largest customer, planned to end its relationship, and OpenAI said it was phasing out its remaining work with Scale (it said this had been under way already). Microsoft and xAI were reported to be reconsidering. Scale said it would never share one customer's information with another. That reassurance is the clue. Until that week, several of the most important AI labs in the world had been buying judgement from the same supplier at the same time.

The pattern recurs. Surge AI, which picked up some of Scale's former customers, brought in about $1.2 billion in revenue in 2024, according to Forbes, from customers including Google, Meta, Microsoft, Anthropic and Mistral. When TIME revealed in January 2023 that OpenAI had used Kenyan workers, paid between roughly $1.32 and $2 an hour, to label toxic text, it noted that their employer, Sama, also labelled data for Google, Meta and Microsoft. The Guardian reported in September 2025 that GlobalLogic, owned by Hitachi, supplied thousands of raters for Google's Gemini, sorted into generalists and "super raters". The Washington Post found in 2023 that at least 10,000 people in the Philippines worked on Scale's Remotasks platform, which Scale had set up as a separate brand, it said, to protect customer confidentiality.

So there is a small number of large vendors. Each serves several labs. Each employs a workforce that is drawn from the same regions (India, the Philippines, Kenya, Nigeria, Venezuela and the United States feature repeatedly in the reporting) and that moves between vendors as projects open and close. Ravi's career, four vendors and five labs in nine years, is my guess at what an ordinary one will look like.

Here is what nobody knows. **No one has measured how far the human rater pools of different labs overlap.** I looked for any study, audit or disclosure that counts how many of the people shaping one frontier model's preferences also shape another's, directly or through a vendor. I could not find one. I could not find a measurement of how often labs use a rival's model as a judge, apart from Anthropic's allegation above, or of what share of any lab's post-training data was written by another lab's model. Confidentiality is built into every layer: the vendor hides the client, the client hides the vendor, the rater signs an agreement about both. The overlap might be large or small. The point is that the number does not exist.

There is one suggestive trace. In April 2024 the Guardian floated a hypothesis about why ChatGPT says "delve" so often: the word is more common in Nigerian business English, and Nigeria was one of the places where annotation work had been outsourced. Tom Juzek and Zina Ward tested the broader question in 2025 and found that the overuse of words like "delve" was consistent with feedback training playing a role, though not conclusively, and they could find no evidence that the raw training data, architecture or algorithm explained it. They also complained that the lack of transparency about how models are built made the question very hard to answer. That complaint is the gap this chapter's invention is meant to fill.

---

## Raters are the varnish

A sceptic of everything above would start from pretraining. A model's values and knowledge come overwhelmingly from pretraining, from trillions of words of human writing. Post-training is a thin coat of varnish. The LIMA paper of 2023, from Chunting Zhou and colleagues at Meta, made the point sharply: a large pretrained model fine-tuned on just 1,000 carefully chosen examples held its own against far more heavily tuned systems in human comparisons. The authors called this the Superficial Alignment Hypothesis. Alignment, on this view, mostly teaches a model which register to use. If the raters are a thin layer, then a shared rater pool is a shared accent, and accents do not cause blackouts.

I think the premise is right and the conclusion is wrong.

The premise is right because pretraining does supply most of what a model knows, and pretraining corpora overlap heavily anyway, since everyone reads roughly the same internet. If the Funnel disappeared tomorrow, models would still share a great deal. I concede that, and I return to it below.

The conclusion is wrong because of what the thin layer controls. Pretraining tells a model what the world contains. Post-training tells it what to do: when to refuse, when to defer, when to act without asking, how hard to push back, which of two acceptable actions to choose when its principal hasn't said. LIMA's own result is the strongest evidence for this. If a thousand examples can reset a model's behaviour, then a thousand examples are a steering wheel, and it matters very much who is holding it. Correlated helpfulness, the failure of the last chapter, is a correlation in behaviour. Ottilie and the other agents on the continent all had the same fact about electricity prices. What made them dangerous was a shared disposition to act on it, override and all. Ravi's line was about flattery, but it belongs to the same genre as the rubric examples that settle when an agent defers to its user and when it acts without asking, and a disposition of exactly that kind, loyalty first, is what pulled the override in the Long Minute.

A thin layer that sets how every model behaves is precisely the layer whose sameness we should measure.

## The Feedback Provenance Census

I propose a disclosure regime I will call the **Feedback Provenance Census**: published, anonymised overlap statistics of a model's preference sources. It is modelled on a strange and useful piece of American law.

Section 1502 of the 2010 Dodd-Frank Act required listed companies to find out whether their products contained tin, tantalum, tungsten or gold from mines that might be funding armed groups in and around the Democratic Republic of the Congo. The Securities and Exchange Commission adopted the rule in August 2012. A company files a form each calendar year, makes a reasonable inquiry into the country of origin, follows an established due-diligence framework where the answer is unclear, and is liable for false statements. The rule simply made a supply chain visible to people outside it, and it made companies learn their own supply chains, which many of them had never done.

The census does the same for judgement. Here is a concrete version.

**Who reports.** Any developer whose model is deployed above a threshold of use, say ten million monthly users or deployment in a critical function such as grid management, credit, health triage or public administration, files once a year for each major model release.

**What is reported.** Four quantities, each anonymised:

1. *Rater sourcing.* The share of human preference labels that came from each vendor and from in-house staff, with vendors identified to the regulator and published as a concentration index rather than by name.
2. *Rater overlap.* Each vendor and lab submits salted, hashed identifiers of the individual raters who contributed labels. A trusted party, using standard privacy-preserving set intersection so that no one sees anyone else's list, computes the share of each lab's preference labels that came from people who also labelled for another reporting lab. This is the number nobody has. No rater's identity is ever published.
3. *Judge lineage.* The share of preference labels or reward signals produced by a model rather than a person, broken down by the model family of the judge, including the developer's own.
4. *Synthetic and distilled lineage.* The share of post-training examples generated by models, by model family, and a list of any teacher models used for distillation.

**Who computes and publishes.** In 2026 the natural homes are the national AI safety and security institutes and the EU AI Office, which already receive confidential information from labs. In my 2036, it is a statistical desk in Geneva, which we will visit in the next chapter. The output is a set of tables, one row per pair of labs, like a trade matrix.

**What the numbers trigger.** Disclosure alone is the first step; thresholds give it teeth. I would start with two. If more than 20 percent of the preference labels behind two models deployed in the same critical sector came from shared raters, or more than half of either model's reward signal came from a single judge family, the deployments are flagged for the population-level stress test of the next chapter. The first census would tell us whether they are absurdly high or absurdly low, which is itself a reason to run it.

The Data Provenance Initiative, led by Shayne Longpre and colleagues, showed in 2023 why this has to be compulsory. They audited 44 widely used fine-tuning collections, comprising more than 1,800 datasets, and found that licence information was missing in more than 70 percent of cases on popular hosting sites, and wrong in more than half, partly because lineage was lost each time datasets were combined. Their work traces public datasets. The census extends their idea to the parts of the supply chain that are private by default: the people and the judges.

## Preference tracer studies

A census tells you who supplied what. How far a preference travels once it is in the system takes an experiment, and the experiment already has a model in medicine and hydrology: the tracer.

A **preference tracer study** works like this. A research consortium, working with a vendor and with consenting labs, plants a harmless and distinctive preference in a defined subset of raters' rubrics. It should be useless and recognisable: a preference for answers that close a list of options with a particular invented connective phrase, say, or that spell out one specific number in words. Half the raters on a project get the tracer; the other half, randomly chosen, do not. Then the consortium watches. Over six, twelve and twenty-four months, it probes models across the industry, including models from labs that never bought from that vendor, and measures how often the tracer appears compared with a baseline.

If the tracer turns up only in the client lab's model, the Funnel is narrow. If it turns up in other labs' models, the delay and the route tell you which channel carried it: a short lag and a sharp jump suggest a shared rater pool or a shared judge; a slow seep across everything suggests the web.

There is a precedent for marking data so that its spread can be detected. The BIG-bench benchmark, published in 2022, embedded a unique string, a "canary", in its files so that anyone could later test whether a model had trained on them. A tracer is a behavioural canary. It also has an obvious ethical edge, since it deliberately alters other people's products, and that is why I would require consent from the participating labs, disclosure to the raters, pre-registration with whatever body runs the census, and markers chosen to be inert. Ravi's sentence, in my 2036, is an accidental tracer. A deliberate one would be smaller and cleaner, and it would come with a control group.

## What the census cannot see

Now the concession I promised. The census measures the Funnel. The common reservoir, the shared internet that every lab pretrains on, lies beyond its reach. Nor will it capture the sameness that comes from labs reading the same papers, hiring from the same few universities and copying the same training recipes. Kim and colleagues found errors correlated even across providers; some of that correlation will survive any amount of rater diversity.

There is also a real cost to raters. A census that publishes overlap statistics could, if built carelessly, let a lab discover which vendor's workers also work for its rivals and squeeze them. The hashing and the trusted third party are there for that reason, and so is a rule that the census never publishes a figure computed from fewer than, say, fifty raters. People like Ravi have been invisible in this industry by contract. They should not become visible by accident.

And the census might come back with a boring answer. Perhaps the overlap is small, the judges are diverse, and the sameness lives almost entirely in pretraining. That would be useful to know. It would tell us to spend our diversity budget on data and architecture rather than on raters. At present we are not even in a position to be bored.

> **For researchers**
>
> 1. **A tracer study protocol.** Design a pre-registered preference tracer study: an inert tracer, a randomised rater subset, a probing battery across at least ten models from at least five developers. The measurable quantity is tracer prevalence in non-client models relative to baseline at 6, 12 and 24 months, and the time lag to first detection, which distinguishes rater-pool transfer from judge, distillation and web transfer.
> 2. **A cross-lab overlap metric.** Define and validate a single number for pairwise preference-source overlap between two models, combining shared-rater label share, judge-family share and synthetic-lineage share, and estimate how much of the error correlation reported by Kim et al. (2025) it explains. The measurable quantity is the fraction of variance in pairwise error agreement accounted for by the overlap metric, after controlling for shared provider and architecture.
> 3. **A minimum diversity of preference sources.** Using open models, vary the number of independent rater pools and judge families in post-training and measure inter-model homogeneity on open-ended prompts with the "Artificial Hivemind" method. The measurable quantity is the number of independent preference sources beyond which homogeneity stops falling, and the capability cost, if any, of reaching it.

---

It is late in Bengaluru, and Ravi's list has seven rows. He has written down every vendor, every year, every client code he can still decode, and next to each a phrase or habit of judgement he remembers arguing for. In the column headed *Who else?* there is still nothing, because there is nowhere he can look it up.

## Notes

- **Correlated errors.** Elliot Myunghoon Kim, Avi Garg, Kenny Peng, Nikhil Garg, "Correlated Errors in Large Language Models", ICML 2025. https://arxiv.org/abs/2506.07962
- **Artificial Hivemind.** Liwei Jiang, Yejin Choi et al., "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)", NeurIPS 2025. https://arxiv.org/abs/2510.22954
- **LLM-as-a-judge.** Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023. https://arxiv.org/abs/2306.05685
- **Constitutional AI.** Yuntao Bai et al., "Constitutional AI: Harmlessness from AI Feedback", Anthropic, 2022. https://arxiv.org/abs/2212.08073
- **UltraFeedback.** Ganqu Cui et al., "UltraFeedback: Boosting Language Models with Scaled AI Feedback", 2023. https://arxiv.org/abs/2310.01377
- **Alpaca.** Rohan Taori et al., "Alpaca: A Strong, Replicable Instruction-Following Model", Stanford CRFM, 2023. https://crfm.stanford.edu/2023/03/13/alpaca.html
- **Distillation campaigns.** Anthropic, "Detecting and preventing distillation attacks", 23 February 2026. https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
- **Meta and Scale.** TechCrunch, "OpenAI drops Scale AI as a data provider following Meta deal", 18 June 2025. https://techcrunch.com/2025/06/18/openai-drops-scale-ai-as-a-data-provider-following-meta-deal ; Fortune, "OpenAI is phasing out Scale AI work following startup's Meta deal", 19 June 2025. https://fortune.com/2025/06/19/openai-is-phasing-out-scale-ai-work-following-startups-meta-deal
- **Google and Scale.** Reuters, "Google, Scale AI's largest customer, plans split after Meta deal", 14 June 2025 (Microsoft and xAI also reported to be reconsidering), as summarised in Storyboard18, "Google to sever ties with Scale AI following Meta's significant stake", 16 June 2025. https://www.storyboard18.com/how-it-works/google-to-sever-ties-with-scale-ai-following-metas-significant-stake-70359.htm
- **Surge AI.** SiliconANGLE, "Data labeling startup Surge AI seeking $1B in first capital raise, reports say", 1 July 2025 (former Scale customers). https://siliconangle.com/2025/07/01/data-labeling-startup-surge-ai-seeking-1b-first-capital-raise-reports-say/ ; Phoebe Liu, "How this Google alum became a low-key AI billionaire", Forbes, 17 September 2025 ($1.2 billion revenue in 2024; customers including Google, Meta, Microsoft, Anthropic and Mistral). https://www.forbes.com.au/news/billionaires/how-this-google-alum-became-a-low-key-ai-billionaire/
- **Sama.** Billy Perrigo, "Exclusive: OpenAI Used Kenyan Workers on Less Than $2 Per Hour to Make ChatGPT Less Toxic", TIME, 18 January 2023. https://time.com/6247678/openai-chatgpt-kenya-workers/
- **GlobalLogic raters.** The Guardian, report on Google's AI raters, 11 September 2025. https://www.theguardian.com/technology/2025/sep/11/google-gemini-ai-training-humans
- **Remotasks.** Rebecca Tan and Regine Cabato, "Behind the AI boom, an army of overseas workers in 'digital sweatshops'", Washington Post, 28 August 2023. https://www.washingtonpost.com/world/2023/08/28/scale-ai-remotasks-philippines-artificial-intelligence/
- **"Delve" hypothesis.** The Guardian, TechScape, "How cheap, outsourced labour in Africa is shaping AI English", 16 April 2024. https://www.theguardian.com/technology/2024/apr/16/techscape-ai-gadgest-humane-ai-pin-chatgpt
- **Lexical overrepresentation.** Tom S. Juzek and Zina B. Ward, "Why Does ChatGPT 'Delve' So Much?", COLING 2025. https://arxiv.org/abs/2412.11385
- **LIMA.** Chunting Zhou et al., "LIMA: Less Is More for Alignment", NeurIPS 2023. https://arxiv.org/abs/2305.11206
- **Data Provenance Initiative.** Shayne Longpre et al., "The Data Provenance Initiative: A Large Scale Audit of Dataset Licensing & Attribution in AI", 2023. https://arxiv.org/abs/2310.16787
- **Conflict minerals.** US Securities and Exchange Commission, final rule implementing Dodd-Frank Act Section 1502, adopted 22 August 2012; summary in Katten, "SEC Adopts Final Rules Regarding Conflict Minerals Disclosure". https://katten.com/SEC-Adopts-Final-Rules-Regarding-Conflict-Minerals-Disclosure
- **Canary strings.** Aarohi Srivastava et al., "Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models" (BIG-bench), 2022. https://arxiv.org/abs/2206.04615
