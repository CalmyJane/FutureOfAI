# Preface {.unnumbered}

This book describes artificial intelligence as it stands in October 2026: how the technology works, what has driven its progress, what it is already doing to work, science, media and public life, how it fails, and how governments are trying to control it. It is written for readers who want the substance rather than the headlines. No programming is assumed, but the book does not avoid technical detail. Where an equation is the clearest way to explain a mechanism, the equation is given, together with a plain-language explanation and a worked number.

Public discussion of AI swings between promise and alarm, and much of it rests on anecdotes, company announcements and forecasts presented as facts. This book tries to do something different: to report what is known, how it is known and how well it is known. Every factual claim that is not common knowledge carries a citation, and the full list of more than five hundred references is at the end of the book. Where the evidence is clear, the book says so plainly. Where informed people disagree, it sets out the strongest evidence on each side.

## How the book is organised

The fourteen chapters fall into five parts.

**Part I, How AI Works (Chapters 1–4),** builds the technical foundation. Chapter 1 traces the history of the field from the 1950s and the competing definitions of "AI". Chapter 2 explains how neural networks learn, from a single artificial neuron to deep networks, with worked examples of backpropagation and convolution. Chapter 3 does the same for large language models: tokenisation, embeddings, attention, the transformer, pre-training, and the later stages of training that turn a text predictor into an assistant or a reasoning model. Chapter 4 examines the scaling laws that have driven most recent progress, and the evidence on where their limits lie.

**Part II, The Frontier (Chapters 5–7),** follows the main technology trends. Chapter 5 covers agents: systems that use tools and act over many steps. Chapter 6 looks at AI in science, mathematics and engineering. Chapter 7 turns to the physical and economic side of AI: chips, supply chains and export controls, data centres, electricity and water, the concentration of costs, openly released models, and attempts to govern AI through its computing power.

**Part III, Society and Economy (Chapters 8–10),** examines effects on people. Chapter 8 reviews the evidence on work, productivity and the labour market, including the hidden human labour behind AI systems. Chapter 9 covers information, media and democracy. Chapter 10 looks at education, health and everyday life.

**Part IV, Risk, Safety and Governance (Chapters 11–13)** asks what can go wrong and what is being done about it: the main categories of risk and the evidence for each (Chapter 11), the technical work on alignment, interpretability and evaluation (Chapter 12), and law and policy in the European Union, the United States, China, the United Kingdom and international bodies, including the disputes over copyright and personal data (Chapter 13).

**Part V, The Decade Ahead (Chapter 14),** examines how AI forecasts are made and how good they have been, sets out the main uncertainties for the next ten years, and closes with ten proposals. These proposals are where the author argues most directly for a position, and they are labelled as such.

Four kinds of box appear in the text. **Concept** boxes define an idea precisely. **Case study** boxes examine a real event in detail. **Debate** boxes set out a contested question with the best evidence on each side. **Going deeper** boxes give additional technical detail. Each chapter ends with annotated suggestions for further reading, and technical terms are collected in the glossary.

## How evidence is labelled

Claims about AI vary enormously in how well they are supported, and the text signals the kind of source in the sentence itself:

- **Peer-reviewed research** and **official statistics or legal texts** are cited without a label. This is the strongest evidence available, though not infallible.
- **Preprints and working papers**, posted publicly before (or without) peer review, are labelled as such where they are first mentioned in a chapter. In AI and in economics, many important results first appear this way.
- **Reports from research institutions** such as Epoch AI, METR, the International Energy Agency or the Stanford AI Index are named, so that readers can judge their methods.
- **Company claims**, such as benchmark results in a product announcement, are introduced with "according to the company". They may be accurate, but they have not been checked independently.
- **Research by banks and consultancies** is labelled as such, for the same reason.
- **Opinions and forecasts** are attributed to the people who hold them.

Where a figure redraws published data, its caption names the source; where a diagram is schematic, the caption says so. Numbers marked as computed by the author (for example the tokenisation and probability tables in Chapter 3) were produced with publicly available models and software, and the settings are given.

## What "as of October 2026" means

The evidence in this book was gathered and checked in October 2026. Some of it will date quickly: the names of the leading models, benchmark scores, the details of export controls, and which provisions of new laws are in force. Other parts will last much longer: how neural networks learn, why scaling works, how to read a randomised trial, what makes a risk hard to govern. Every number is given with the year it refers to, so that readers can look for newer figures and compare.

Jan Göbel, October 2026


```{=html}
<section class="part"><p class="part-label">Part I</p><h1 class="part-title">How AI Works</h1></section>
```

# Chapter 1: What We Mean by "AI": Definitions and a Short History

The field of artificial intelligence began with a funding request. On 31 August 1955, John McCarthy of Dartmouth College, Marvin Minsky of Harvard, Nathaniel Rochester of IBM and Claude Shannon of Bell Telephone Laboratories asked the Rockefeller Foundation to support "a 2 month, 10 man study of artificial intelligence" the following summer, at a cost of $13,500. The proposal's central claim was far larger than its budget: that "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it" [@mccarthy2006proposal].

Seventy years later the term is attached to products used by hundreds of millions of people. On 30 November 2022 OpenAI released ChatGPT as a "research preview", and by 5 December it had more than one million registered users. By July 2025 about 700 million people used it each week, roughly 10% of the world's adult population, according to a working paper co-written by OpenAI staff from the company's own data [@chatterji2025how]. In February 2026 OpenAI announced 900 million weekly users, a company figure reported by the press and not independently verified [@malik2026chatgpt].

Between those two points lie at least three different ideas of how intelligent machines should be built, two collapses in funding and confidence, and a running argument about what the term should cover. That argument now has legal force. Since February 2025 the definition of an "AI system" in the EU's AI Act has decided which software the Act can reach, and false claims to use AI have drawn fines from US regulators.

## 1.1 From Turing's question to the Dartmouth proposal

### Turing's behavioural test

Alan Turing's 1950 paper "Computing machinery and intelligence" opens with the sentence "I propose to consider the question, 'Can machines think?'". Turing judged the words "machine" and "think" too vague to define usefully, so he replaced the question with a test he called the imitation game. A human interrogator exchanges typed messages with a hidden person and a hidden machine and tries to tell which is which. Turing predicted that in about fifty years computers with a storage capacity of about 10^9^ would play the game well. An average interrogator would then have no more than a 70 per cent chance of making the right identification after five minutes of questioning [@turing1950computing].

Turing's move set a pattern that has lasted. He defined intelligence by what a system does, judged from outside, not by what goes on inside it. Most modern definitions, including the legal ones in Section 1.2, follow the same behavioural approach. The weakness of the approach was visible from the start: a behavioural test says nothing about whether the machine reaches its answers in a way that resembles human thought. A 2022 survey of natural-language researchers found the field split almost evenly on whether a model trained only on text could understand language "in some nontrivial sense" [@mitchell2023debate]; Section 3.7 sets out that dispute.

### What the Dartmouth proposal claimed

The 1955 proposal is more specific than its famous opening sentence suggests. It listed seven "aspects of the artificial intelligence problem": automatic computers, programming a computer to use a language, "neuron nets", a theory of the size of a calculation, self-improvement, abstractions, and randomness and creativity [@mccarthy2006proposal]. On computing power the authors were confident that hardware was not the bottleneck: "the major obstacle is not lack of machine capacity, but our inability to write programs taking full advantage of what we have." On language they speculated that "a large part of human thought consists of manipulating words according to rules of reasoning and rules of conjecture", which is close to a programme statement for the symbolic AI described in Section 1.4. On neural networks they noted "partial results" and said "the problem needs more theoretical work". Their fourth topic anticipated the main obstacle of the next two decades: trying all possible answers in order is "inefficient", so a theory of the efficiency of calculation was needed to avoid it.

The proposal's tone was optimistic but its stated goal was modest: "a significant advance can be made in one or more of these problems if a carefully selected group of scientists work on it together for a summer". The budget was correspondingly small: mostly summer salaries for six faculty members and two graduate students, while the participants from Bell Laboratories and IBM were to be paid by their employers (the itemised costs add up to $13,000, although the typed total reads $13,500) [@mccarthy2006proposal]. The workshop ran from 18 June to 17 August 1956, according to an account by Grace Solomonoff that draws on the papers of her husband, the participant Ray Solomonoff. Accounts of attendance differ: hers describes "a few dozen" thinkers who came and went [@solomonoff2023meeting], while the Stanford Encyclopedia of Philosophy counts ten attendees, Allen Newell and Herbert Simon among them [@bringsjord2018artificial]. Early in the summer Newell and Simon presented their Logic Theorist, a program that proved elementary theorems in propositional logic and that the attendees regarded as a remarkable achievement [@solomonoff2023meeting; @bringsjord2018artificial]. Its designers stressed that, unlike the systematic algorithms then normal in computing, it "relies heavily on heuristic methods similar to those that have been observed in human problem solving" [@newell1956logic]. That combination of symbols, rules and heuristic search defined the field for its first thirty years.

### Researchers' definitions

Definitions written by researchers have stayed loose. The AI pioneer Nils Nilsson described AI as "that activity devoted to making machines intelligent", and intelligence as the quality that enables an entity "to function appropriately and with foresight in its environment". The One Hundred Year Study on AI, a long-term project based at Stanford University, adopted this formulation in its 2016 report [@stone2016artificial]. The difficulty is that "intelligence" has no agreed definition either. In 2007 Shane Legg and Marcus Hutter compiled "70-odd" informal definitions of intelligence from psychologists, AI researchers and dictionaries, and distilled them into one: "Intelligence measures an agent's ability to achieve goals in a wide range of environments" [@legg2007collection]. Their summary points to the property that most AI systems of the past seventy years lacked: breadth. A chess program, a medical expert system or an image classifier achieves goals in one environment only.

## 1.2 Official definitions and where they draw the line

Definitions written for governments cannot be loose, because they decide which systems a law covers, and the boundary they draw cuts across the field's own history. Under the European Commission's 2025 guidelines to the EU AI Act, a rule-based medical adviser of the 1970s qualifies as an AI system, while a chess program built on search plus a hand-tuned evaluation, the technique behind the most famous AI event of the 1990s, may not [@europeancommission2025guidelines, paras 39, 48]. The definitions in widest use are the OECD's, the EU AI Act's and the US definition in the National AI Initiative Act of 2020.

### The OECD definition and its revision

The Organisation for Economic Co-operation and Development (OECD), an intergovernmental organisation of mostly high-income countries, first defined an AI system in its 2019 AI Principles. That definition built on the textbook view of AI in Stuart Russell and Peter Norvig's *Artificial Intelligence: A Modern Approach*, and read: "An AI system is a machine-based system that can, for a given set of human-defined objectives, make predictions, recommendations, or decisions influencing real or virtual environments. AI systems are designed to operate with varying levels of autonomy" [@oecd2024explanatory, p. 4]. Member countries approved a revision in November 2023. An explanatory memorandum published in March 2024 sets out the final text [@oecd2024explanatory, p. 4]:

> An AI system is a machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments. Different AI systems vary in their levels of autonomy and adaptiveness after deployment.

Replacing "human-defined objectives" with "explicit or implicit objectives" brings in systems whose goals are never written down, such as a language model rewarded for plausible responses or a recommender system that gradually narrows down a model of a user's preferences [@oecd2024explanatory, p. 7]. "Content" joined the outputs because generative systems producing text, images, audio and video "have gained significant momentum" [@oecd2024explanatory, p. 9]. The word "infers" became the core of the definition; according to the memorandum it covers both the moment a system produces an output and the earlier "build phase" in which a model is derived from data [@oecd2024explanatory, p. 9]. "Adaptiveness" means that a system keeps changing after deployment, as a speech recogniser that adapts to one person's voice does [@oecd2024explanatory, p. 6].

### The EU AI Act and the Commission's guidelines

The European Union's Artificial Intelligence Act, Regulation (EU) 2024/1689, defines an AI system in Article 3(1) in almost the same words: a machine-based system "designed to operate with varying levels of autonomy" that "may exhibit adaptiveness after deployment" and that "infers, from the input it receives, how to generate outputs" such as predictions, content, recommendations or decisions [@europeanparliament2024regulation, art. 3(1)]. The match is deliberate; the Act wants its definition to be "closely aligned with the work of international organisations working on AI" [@europeanparliament2024regulation, recital 12]. Recital 12 also says what is excluded: "simpler traditional software systems" and systems based on rules defined solely by people to execute operations automatically. Logic- and knowledge-based approaches that infer from encoded knowledge are included (Chapter 13 discusses the Act's obligations).

Because the boundary matters legally, the European Commission issued guidelines on the definition, dated 29 July 2025. They split it into seven elements, from being machine-based to influencing physical or virtual environments [@europeancommission2025guidelines, para 9]. They then name four kinds of system that "may" fall outside it despite some capacity to infer [@europeancommission2025guidelines, para 41]:

- systems that improve or approximate established mathematical optimisation, "such as linear or logistic regression methods", which do not "transcend 'basic data processing'"; one indication is that a method "has been used in consolidated manner for many years";
- basic data processing, such as database queries and spreadsheets without AI functions;
- systems based on "classical heuristics", with the example of "a chess program using a minimax algorithm with heuristic evaluation functions";
- simple prediction systems whose performance can be matched by a basic statistical rule, such as predicting tomorrow's temperature as last week's average [@europeancommission2025guidelines, paras 42, 46, 48–50].

At the same time the guidelines count "early generation expert systems intended for medical diagnosis" and "search and optimisation methods" among the logic- and knowledge-based approaches that are inside the definition [@europeancommission2025guidelines, para 39]; the line between included search methods and excluded "classical heuristics" is what places an early medical expert system inside and a minimax chess program possibly outside. The guidelines admit the limits of the exercise. They are "not binding", only the Court of Justice of the EU can give an authoritative interpretation, and "no automatic determination or exhaustive lists" of systems inside or outside the definition are possible. They also stress that "the vast majority" of systems that do qualify face no obligations under the Act [@europeancommission2025guidelines, paras 7, 62, 63].

### The US definition

US federal law uses an older formula. The National Artificial Intelligence Initiative Act of 2020 defines AI as "a machine-based system that can, for a given set of human-defined objectives, make predictions, recommendations or decisions influencing real or virtual environments", and adds that such systems use machine and human-based inputs to "perceive real and virtual environments", "abstract such perceptions into models through analysis in an automated manner" and "use model inference to formulate options for information or action" [@uscongress2021national]. The first sentence follows the OECD's 2019 wording almost word for word. The US statutory text therefore predates both generative "content" and the shift from human-defined to implicit objectives.

| Element | OECD 2019 | US statute (2021) | OECD 2023 | EU AI Act (2024) |
|---|---|---|---|---|
| Objectives | human-defined | human-defined | explicit or implicit | explicit or implicit |
| Core verb | make predictions, recommendations, decisions | make predictions, recommendations, decisions; "use model inference" | "infers ... how to generate outputs" | "infers ... how to generate outputs" |
| Content as output | no | no | yes | yes |
| Autonomy | varying | not mentioned | varying | varying |
| Adaptiveness after deployment | not mentioned | not mentioned | varies | "may exhibit" |
| Official exclusions | none stated | none stated | none stated | recital 12; Commission guidelines (non-binding) |

: Table 1.1: Four official definitions of an AI system compared. Source: [@oecd2024explanatory; @uscongress2021national; @europeanparliament2024regulation; @europeancommission2025guidelines].

::: {.box .concept}
**Concept: AI system (OECD and EU definition)**

An AI system is a machine-based system that, for explicit or implicit objectives, infers from its input how to generate outputs such as predictions, content, recommendations or decisions that can affect physical or virtual environments. The key word is "infers": the system derives how to respond, from data or from encoded knowledge, instead of only executing rules a person wrote down. A spam filter trained on examples of junk mail fits the definition. A fixed tax formula in a spreadsheet does not. In between lies a grey zone, including logistic regression and classical search, that the EU guidelines resolve case by case.
:::

## 1.3 A family of terms

Public discussion often uses "AI" as if it named a single technology. It is an umbrella term for a family of methods whose names overlap. Figure 1.1 shows the most common arrangement as nested regions.

![Figure 1.1: The usual nesting of AI terms. Machine learning is one approach within AI; deep learning is one kind of machine learning; large language models and other generative foundation models are, today, mostly built with deep learning. Agents are drawn across the boundaries because the term describes how a model is used. Schematic, not to scale. Diagram by the author.](../figures/svg/fig-01-01.svg){#fig:01-01}

**Machine learning** is the approach in which a system improves at a task by learning from data or experience instead of being given explicit rules. Arthur Samuel's 1959 study of checkers (draughts) is a classic early example. Samuel showed that "a computer can be programmed so that it will learn to play a better game of checkers than can be played by the person who wrote the program", and that it could do so in 8 to 10 hours of playing time [@samuel1959studies].

**Deep learning** is machine learning with artificial neural networks that have many layers. A neural network is a computing structure loosely inspired by the brain, made of simple connected units whose connection strengths are adjusted during training. In the words of a 2015 review, deep learning "allows computational models that are composed of multiple processing layers to learn representations of data with multiple levels of abstraction" [@lecun2015deep]. Chapter 2 explains how such networks learn.

**Generative AI** refers to systems whose main output is new content: text, images, audio, video or computer code. A system that only sorts emails into "spam" and "not spam" is not generative, because it produces a label instead of new content.

A **foundation model** is a large model trained on broad data, usually with self-supervision at scale, that can be adapted to a wide range of downstream tasks. The term was introduced in 2021 in a report by more than 100 researchers, posted as a preprint, who chose the word to stress the models' "critically central yet incomplete character" [@bommasani2021opportunities]. Self-supervision means that the training signal comes from the data itself, for instance by hiding a word in a sentence and asking the model to predict it, so that no person has to label each example. The EU AI Act uses a related legal term, the **general-purpose AI model**: "an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks" [@europeanparliament2024regulation, art. 3(63)].

A **large language model (LLM)** is a foundation model trained mainly on text to predict the next token, a word or piece of a word, in a sequence (Chapter 3 explains the mechanism). An **AI agent** is a system that pursues a goal over several steps by taking actions, such as searching the web, running code or filling in forms, and observing the results. The idea is old: a 1995 survey already described the agent concept as having "become important in both artificial intelligence and mainstream computer science" [@wooldridge1995intelligent]. What is new since 2024 is that agents are commonly built by placing an LLM inside a loop with tools and memory (Chapter 5).

The nesting in Figure 1.1 is a simplification. Not every generative model is a deep neural network, and not every foundation model is generative: BERT, one of the original examples, was mainly used to classify and analyse text [@bommasani2021opportunities]. "Agent" describes how a model is used, not a technique, so it cuts across the nested regions. And the outermost region contains far more than machine learning, including the symbolic methods described next, which dominated the field for its first three decades.

## 1.4 Symbolic AI: search, logic and rules

### Symbols and search

In **symbolic AI**, knowledge is written down explicitly as symbols and rules, and the computer reasons by manipulating them. Most of the work was done by logical inference, which derives new statements from old ones, and by search, which explores a space of possible states (board positions, partial proofs, plans) for one that meets a goal. The difficulty with search was quantified before the field had a name. In 1950 Shannon estimated that a typical chess position offers "of the order of 30 legal moves", so that one move by each side gives about 10^3^ possibilities, and a game of about 40 moves yields some 10^120^ variations from the initial position. A machine checking one variation per microsecond "would require over 10^90^ years to calculate the first move" [@shannon1950programming]. Every symbolic system therefore needed heuristics: rules of thumb, such as an evaluation of material and position, that prune the search to a manageable size. The Logic Theorist's reliance on "heuristic methods" was the same answer applied to proofs [@newell1956logic].

Predictions in this period were bold. In 1960 Herbert Simon declared that "Machines will be capable, within twenty years, of doing any work that a man can do", and in 1967 Minsky forecast that "Within a generation...the problems of creating 'artificial intelligence' will be substantially solved" [@mitchell2021why]. Enthusiasm also surrounded early neural networks, until Minsky and Seymour Papert's 1969 book *Perceptrons* showed the limits of the single-layer networks of the time (Chapter 2 gives the details).

### The first winter

The term **AI winter** describes a period of reduced funding, falling confidence and declining interest in AI research. The first is usually dated to the mid-1970s. In the United Kingdom the Science Research Council asked the mathematician Sir James Lighthill to assess the field. His report, dated July 1972 and published in 1973, concluded that "in no part of the field have the discoveries made so far produced the major impact that was then promised", and among the causes he named a "failure to recognise the implications of the combinatorial explosion" [@lighthill1973artificial]. The combinatorial explosion is the problem Shannon had quantified: the number of possibilities grows exponentially with the size of a problem, so methods that work on a toy version fail on a realistic one. According to Melanie Mitchell, in an essay posted as a preprint, the Lighthill report and a similarly negative review for the US Department of Defense "led to sharp funding decreases and a downturn in enthusiasm for AI in both countries" [@mitchell2021why]. How deep this winter was is disputed. The historian of computing Thomas Haigh argues that the research community grew steadily through the 1970s [@haigh2024how]; the computer scientist James Hendler, that the cuts acted slowly, their effects felt only in the mid-to-late 1980s, when "the seed corn had been consumed" [@hendler2008avoiding].

### Production rules: how MYCIN reasoned

The most successful symbolic idea of the 1970s was the **production rule**, a single if-then statement of expert knowledge, and the **expert system** built from hundreds of them. MYCIN, developed at Stanford University in the 1970s to advise on antibiotic treatment for serious infections, is the best-documented example, because its builders published a book-length account of it. A typical rule, as printed in that account, reads:

> IF: 1) The gram stain of the organism is gramneg, and 2) The morphology of the organism is rod, and 3) The aerobicity of the organism is anaerobic\
> THEN: There is suggestive evidence (.6) that the identity of the organism is bacteroides [@buchanan1984rule, p. 71]

Internally each rule was a fragment of the programming language LISP, and the system could translate it into the English shown. The number 0.6 is a **certainty factor (CF)**: a number from −1 (definitely false) to +1 (definitely true) that the expert attached to the rule [@buchanan1984rule, p. 81]. The rule base grew to about 500 rules [@buchanan1984rule, p. 71].

MYCIN ran these rules by **backward chaining**. To establish a goal, such as the identity of an organism, it retrieved every rule whose conclusion bore on that goal. If a rule needed a fact not yet known, MYCIN set up a subgoal and tried the rules for that. When the rules failed to deduce the information, it asked the physician a question. This control structure "results in a highly focused search through the rule base" [@buchanan1984rule, p. 71]. When several rules supported the same hypothesis, their evidence was combined. MYCIN kept a measure of belief (MB) and a measure of disbelief (MD) for each hypothesis. A new piece of supporting evidence with strength *x* raised the existing belief *b* to *b* + *x*(1 − *b*), and the final certainty factor was CF = MB − MD. Table 1.2 reproduces the worked example from the system's documentation.

| Step | Evidence about the hypothesis "the organism is a Streptococcus" | MB | MD | CF = MB − MD |
|---|---|---|---|---|
| 1 | First rule supports it with CF 0.3 | 0.30 | 0 | 0.30 |
| 2 | Second rule supports it with CF 0.2: 0.3 + 0.2 × (1 − 0.3) | 0.44 | 0 | 0.44 |
| 3 | Third rule counts against it with CF −0.1 | 0.44 | 0.10 | 0.34 |

: Table 1.2: How MYCIN accumulated evidence. Two weak supporting rules give more belief than either alone, but never more than 1; contrary evidence is kept separately and subtracted at the end. Source: [@buchanan1984rule, p. 260].

The scheme was a pragmatic substitute for probability theory: experts could state rough strengths, and the arithmetic was cheap. It was also an approximation. The MYCIN volume itself includes an analysis by J. Barclay Adams of how certainty factors relate to probability and of the assumptions they make, including the independence of separate pieces of evidence [@buchanan1984rule, ch. 12].

::: {.box .case}
**Case study: MYCIN's blinded evaluation (1979) and why it was never used**

In a study published in 1979, MYCIN's recommendations for ten real cases of meningitis were compared with those of nine human prescribers, including five infectious-disease faculty specialists at Stanford. Eight experts at other institutions rated each prescription without knowing which came from the computer. MYCIN's prescriptions were rated acceptable 65% of the time; the five faculty specialists scored between 42.5% and 62.5% [@yu1979antimicrobial]. The study was small, confined to one infection and judged by expert agreement rather than patient outcomes.

MYCIN never reached the wards. Its developers wrote that although testing on hospital wards had been "explicitly our initial intention", the infectious-disease knowledge base "was laid to rest in 1978" despite its performance [@buchanan1984rule, p. 673]. Their reasons were practical. MYCIN ran only in the Interlisp language on laboratory computers, so it would have had to be rewritten for hospital hardware, and the computers able to run it were still "too expensive". Its narrow knowledge and awkward interface meant it "would not be a cost-effective tool for physicians to use on such narrow problem areas as meningitis and bacteremia" [@buchanan1984rule, pp. 698–699, 701–702]. They also declined to publish the rules as medical guidance, because the rules omitted the causal reasoning behind them and were "not readable as text" [@buchanan1984rule, p. 702]. The gap between expert-level accuracy and real use recurs in clinical AI today (Chapter 10).
:::

## 1.5 The expert-systems boom and the second winter

### The boom

In the early 1980s expert systems became an industry. The key commercial example was XCON (also called R1), built by John McDermott of Carnegie Mellon University for Digital Equipment Corporation (DEC). From 1980 DEC used it to configure its VAX-11 computer systems from customers' orders [@bachant1984r1]. According to Haigh, its first release condensed expert knowledge into 480 configuration rules, and DEC claimed that XCON and a related system saved more than $40 million a year [@haigh2024how]. Startups sold expert-system "shells" (an inference engine with an empty rule base, as EMYCIN did for MYCIN's engine), consulting services, and implementations of the AI programming languages Lisp and Prolog. MIT alone spawned two companies selling workstations with custom processors designed to run Lisp efficiently [@haigh2024how].

Governments joined in. Japan's Fifth Generation computing project prompted the US Strategic Computing Initiative, launched by the Defense Advanced Research Projects Agency (DARPA) in 1983, and the United Kingdom's Alvey programme [@haigh2024how; @mitchell2021why]. Strategic Computing was sold to Congress with promises of military applications and rested, in Haigh's account, on the assumption that existing approaches to expert systems, natural-language understanding and vision were ready for large-scale use once hardware improved [@haigh2024how].

Some researchers were already worried. At the 1984 conference of the American Association for Artificial Intelligence, a panel discussed "deep unease among AI researchers" that expectations were too high and that this "will eventually result in disaster" [@mcdermott1985dark]. One panellist, Drew McDermott, sketched a collapse in which "everybody hurriedly changes the names of their research projects to something else", a scenario he said some called the "AI Winter". About five years later, in the late 1980s, a second winter set in [@mitchell2021why].

### Why expert systems failed economically

**Brittleness.** Expert systems were "often unable to generalize or adapt when faced with new situations", because the experts writing the rules relied on unspoken common-sense knowledge that never reached the program [@mitchell2021why]. MYCIN's builders made a related admission: rule-based systems are "sometimes characterized as 'shallow' reasoning systems in which the rules encode no causal knowledge", which they called "largely (but not entirely) true of MYCIN" [@buchanan1984rule, p. 672].

**Maintenance.** Rules had to be extracted from experts by "knowledge engineers" and kept current by hand. Companies that bought expert-system software found that automating expertise required them to hire new experts to maintain the rules. By 1989 DEC had 59 technical staff assigned to maintaining the infrastructure and rules of its internal expert systems, the most publicised application of AI at the time, and a shortage of AI specialists had pushed up wages. Few companies could sustain such costs [@haigh2024how].

**Hardware.** The early boom ran on Lisp machines. Hendler recalls that rapid improvement in ordinary hardware let commodity computers run Lisp "with good speed at a lower price", and that rule engines written in the language C, such as CLIPS, "didn't need a $50,000 special-purpose machine to run on". In his account, "by roughly 1987, the Lisp machine market was dead" [@hendler2008avoiding].

**Funding and expectations.** At DARPA, speech recognition progressed but most other Strategic Computing projects disappointed. Reagan-era budget cuts reduced the effort further; at the end of 1987 DARPA abandoned the programme's flagship, an autonomous land vehicle, and turned its computing research towards high-performance numerical computing [@haigh2024how]. Hendler adds a self-inflicted wound: as funding tightened, researchers began to dismiss expert systems as "not really AI", so that the community "avowed that the stuff that worked well wasn't really AI" [@hendler2008avoiding].

The market for expert-system software, in Haigh's words, "proved unsustainable" [@haigh2024how]. The most ambitious attempt to escape brittleness, Douglas Lenat's Cyc project, set out in 1983 to write down common sense on a large scale. Lenat estimated that encoding an encyclopedia's worth of knowledge would take about 2,000 person-years; the project was carried on by a private company, its knowledge base growing to some 30 million rules, without fulfilling the original vision [@haigh2024how]. The lesson many researchers drew was that knowledge written down by hand does not scale. Section 1.7 returns to whether that lesson was right.

## 1.6 The statistical turn

### Speech: from rules to hidden Markov models

The method that replaced hand-written rules came first from speech recognition, and it came partly from IBM. In 1976 the IBM researcher Frederick Jelinek published a description of continuous speech recognition by statistical methods: models of the speaker and of the acoustic processor whose parameters were estimated from data, combined with search procedures for decoding [@jelinek1976continuous]. Lalit Bahl, Jelinek and Robert Mercer later formulated speech recognition explicitly "as a problem of maximum likelihood decoding", giving "special attention to determining the parameters for such models from sparse data" [@bahl1983maximum].

The core model was the **hidden Markov model (HMM)**. The idea is that a word is produced by a sequence of hidden states (roughly, the stages of articulating its sounds), each of which emits observable acoustic measurements with some probability. Given an audio signal, the recogniser asks which sequence of hidden states, and hence which words, would most probably have produced it. All the probabilities are learned from recorded and transcribed speech by an iterative algorithm, so nobody has to write rules about how a vowel sounds. A retrospective by three of the field's builders, Xuedong Huang, James Baker and Raj Reddy, describes this as "a pivotal change in the representation of knowledge in speech recognition". Systems such as Dragon, Harpy and Sphinx were built on "a single, relatively simple modeling principle of joint global optimization", in contrast to earlier designs of cooperating knowledge modules [@huang2014historical; @rabiner1989tutorial]. Progress was measured by the word error rate in DARPA-funded evaluations [@huang2014historical].

### Translation as decoding

At the end of the 1980s the IBM group applied the same thinking to translation. Peter Brown and colleagues treated a French sentence as an English sentence that had passed through a noisy channel. They searched for the English sentence *S* that maximised Pr(*S*) × Pr(*T*|*S*): the probability of *S* as English, given by a language model, times the probability that it would be translated as the observed French *T*, given by a translation model [@brown1990statistical]. Both were learned from the proceedings of the Canadian parliament, kept by law in English and French, from which the team obtained about 100 million words in each language and extracted about three million sentence pairs.

The learned parameters showed what data alone could reveal. For the English word "hear", the most probable French translation turned out to be "bravo", because English-speaking members of parliament shout "Hear, hear!" where French speakers say "Bravo!"; the model had learned that "usually two hears produce one bravo" [@brown1990statistical]. The first results were modest. With vocabularies limited to the 1,000 most common English words and 1,700 French words, the system decoded 73 new French sentences; only 5% came out exactly as the human translation, and 48% were judged reasonable [@brown1990statistical]. The authors had used only about one per cent of their data for the translation model. The paper mattered for its method, which learned everything from aligned text.

### More data, simpler models

Through the 1990s the field's centre of gravity moved from writing knowledge down to estimating it. Mitchell describes "the meteoric rise of machine learning" in the 1990s and 2000s, with methods "inspired by statistics rather than by neuroscience or psychology", and notes that practitioners distanced themselves from the "then-discredited" label AI [@mitchell2021why]. Support vector machines, introduced in their modern form by Corinna Cortes and Vladimir Vapnik in 1995, became a standard tool for classification [@cortes1995support]. Neural networks had not disappeared: a 1986 paper in *Nature* by David Rumelhart, Geoffrey Hinton and Ronald Williams popularised **backpropagation**, the method still used to train them [@rumelhart1986learning], but for two decades they were one method among many.

Researchers at Microsoft and Google stated the new attitude towards data most plainly. In 2001 Michele Banko and Eric Brill of Microsoft Research trained four learning methods to choose between commonly confused words (such as "principal" and "principle", or "then" and "than") on corpora of up to one billion words, three orders of magnitude more than the largest training corpus previously used for this problem. The learning curves of all four methods "appear to be log-linear even out to one billion words", and none of the methods was "close to asymptoting" at the corpus sizes the field commonly used. They concluded that "we may want to reconsider the trade-off between spending time and money on algorithm development versus spending it on corpus development" [@banko2001scaling].

In 2009 three Google researchers, Alon Halevy, Peter Norvig and Fernando Pereira, pointed to a trillion-word corpus of web text, with counts of all word sequences up to five words long. Despite its errors, it was a million times larger than the classic Brown Corpus. They summarised the lesson: "simple models and a lot of data trump more elaborate models based on less data" [@halevy2009unreasonable].

### Deep Blue and ImageNet

The most widely publicised AI event of the 1990s belonged to the older tradition. In May 1997 IBM's chess computer Deep Blue beat the world champion Garry Kasparov 3.5 to 2.5 in a six-game match in New York. IBM describes it as the first defeat of a reigning world champion by a computer in a match under standard tournament time controls. In IBM's words, Deep Blue "derived its chess prowess through brute force computing power": 32 processors evaluating 200 million chess positions per second, built with the goal of beating the world's best human player [@ibm2025deep]. It was a search engine in the mould Shannon had sketched in 1950, and the kind of system that the EU's 2025 guidelines suggest may fall outside the legal definition of AI.

A quieter development turned out to matter more. In 2009 Jia Deng, Fei-Fei Li and colleagues introduced ImageNet, a large database of labelled photographs organised by category [@deng2009imagenet]. From 2010 an annual competition, the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), asked teams to classify images into 1,000 categories using roughly 1.2 million training images [@russakovsky2015imagenet]. A large, shared dataset with agreed scoring gave computer vision a common yardstick of the kind the DARPA speech evaluations had provided, and it gave data-hungry methods something to learn from.

## 1.7 Deep learning, foundation models and assistants (2009–2026)

### The breakthroughs, with numbers

Deep learning's first large practical success came in speech, not vision. In 2011 Frank Seide, Gang Li and Dong Yu of Microsoft replaced the Gaussian-mixture component of a standard HMM recogniser with a deep neural network (seven hidden layers in the best reported system; the authors tested up to nine), trained on 309 hours of recorded telephone conversations. On a public benchmark of phone-call transcription (Switchboard), the word error rate fell from 27.4% to 18.5%, "a 33% relative improvement" [@seide2011conversational]. By 2014 researchers at both Microsoft and IBM were reporting their best Switchboard results with systems following this deep-learning framework [@huang2014historical].

In the 2012 ImageNet challenge, a University of Toronto team, Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton, entered a deep convolutional neural network now called AlexNet. It achieved a top-5 error rate of 15.3%, against 26.2% for the second-best entry [@krizhevsky2012imagenet]. (That entry used additional pre-training data; with only the official training data the error was 16.4%, the value shown in Figure 1.2 [@russakovsky2015imagenet].) The network had 60 million adjustable parameters and was trained for five to six days on two NVIDIA GTX 580 graphics cards [@krizhevsky2012imagenet]. Graphics processing units (GPUs) were designed for computer graphics, but they perform many simple calculations at once, which is what training a neural network requires (Section 2.6).

::: {.box .deeper}
**Going deeper: What "top-5 error" measures**

In the ImageNet classification task, each test image has one correct label from 1,000 categories, such as a particular breed of dog. A system may submit five guesses per image. The top-5 error is the percentage of test images for which none of the five guesses matches the correct label. Five guesses are allowed because many photographs contain several objects and only one is labelled. An error of 15.3% therefore means that AlexNet's five guesses all missed for about 15 of every 100 test images. The organisers note that top-5 error, top-1 error and a hierarchical measure ranked the entries in the same order, which is why they adopted the simplest [@russakovsky2015imagenet].
:::

The winning error rate (counting only entries that used the official training data) fell from 28.2% in 2010 to 6.7% in 2014, and the drop after 2012 coincided with the switch to deep convolutional networks [@russakovsky2015imagenet]. In 2015 a "residual network" with up to 152 layers reached 3.57% [@he2016deep].

![Figure 1.2: Winning top-5 classification error in the ImageNet challenge, 2010–2015 (lower is better). The largest single drop came in 2012, when a deep neural network won for the first time. The dashed line marks one trained human annotator's estimated error of 5.1% on a sample of 1,500 test images; it is a single-person estimate, not a general human benchmark. Source: @russakovsky2015imagenet; @krizhevsky2012imagenet; @he2016deep.](../figures/svg/fig-01-02.svg){#fig:01-02}

The human comparison in Figure 1.2 needs care. The organisers estimated that one expert annotator, who had trained on 500 images, made top-5 errors on 5.1% of 1,500 test images; a second annotator labelled only 258 images [@russakovsky2015imagenet]. In 2015 a team led by Kaiming He reported 4.94% and described the result as "the first to surpass human-level performance (5.1%...)" on the challenge [@he2015delving]. The claim, and the headlines it inspired, rested on one benchmark and essentially one annotator, an early instance of a pattern Chapter 4 examines: benchmark results are real but measure less than headlines suggest.

In January 2016 David Silver and colleagues at Google DeepMind described AlphaGo, which combined two deep networks, one proposing promising moves and one estimating the chance of winning from a position, with a tree search. The networks were trained first on games by human experts and then by "reinforcement learning from games of self-play", that is, by trial and error against versions of itself with winning as the reward. AlphaGo won 99.8% of its games against other Go programs and beat the European champion Fan Hui by five games to nothing, "a feat previously thought to be at least a decade away" [@silver2016mastering]. In March 2016 it beat Lee Sedol, one of the world's strongest players, by four games to one in Seoul [@sumner2016alphago]. AlphaGo is a reminder that the traditions merged: its learned networks guided a tree search, the core technique of symbolic game-playing programs.

In June 2017 eight researchers, most of them at Google, proposed the **transformer**, a network for processing sequences "based solely on attention mechanisms, dispensing with recurrence and convolutions entirely". On a standard English-to-German translation test it scored 28.4 on BLEU, a measure of how many word sequences a machine translation shares with human reference translations, more than two points above the best previous results, with significantly less training time [@vaswani2017attention]. Because a transformer processes all the words of a passage at once rather than one after another, it uses parallel hardware efficiently, which made much larger models practical. Chapter 3 explains how attention works.

| Year | Task and measure | Earlier approach | New result | New method |
|---|---|---|---|---|
| 1990 | French–English translation, 73 test sentences judged reasonable | rule-based systems (not compared) | 48% (5% exact) | statistical translation [@brown1990statistical] |
| 2011 | Telephone speech (Switchboard), word error rate | 27.4% | 18.5% | deep network inside HMM [@seide2011conversational] |
| 2012 | ImageNet, top-5 error | 26.2% (second-best entry) | 15.3% | deep convolutional network [@krizhevsky2012imagenet] |
| 2015 | ImageNet, top-5 error | 6.7% (2014 winner) | 3.57% | residual network [@russakovsky2015imagenet; @he2016deep] |
| 2016 | Go against a professional (Fan Hui) | no program had beaten a professional on a full board | 5–0 | deep networks plus tree search [@silver2016mastering] |
| 2017 | English–German translation, BLEU | previous best, more than 2 points lower | 28.4 | transformer [@vaswani2017attention] |

: Table 1.3: Landmark results of the statistical and deep-learning eras. Measures differ by task; lower is better for error rates, higher for BLEU and acceptability. Source: as cited in each row.

### Pre-training and foundation models

Between 2018 and 2020 a new recipe emerged: pre-train one large transformer on unlabelled text by self-supervision, then adapt it to many tasks. Table 1.4 traces the first generation, in which each model was larger than the last and needed less task-specific training. OpenAI's GPT-1 and Google's BERT, both from 2018, set new records on many language-understanding tasks after being adapted to each one [@radford2018improving; @devlin2019bert]. OpenAI's GPT-2 (2019) set state-of-the-art results on most language-modelling datasets "in a zero-shot setting", without any task-specific training [@radford2019language]. GPT-3 (2020), with 175 billion parameters, "10x more than any previous non-sparse language model", could carry out tasks such as translation, question answering and simple arithmetic when given only a few examples in its prompt, which its authors called few-shot learning [@brown2020language].

| Model | Year | Developer | Parameters | Pre-training text | Reported result |
|---|---|---|---|---|---|
| GPT-1 | 2018 | OpenAI | 12-layer transformer, 117 million | BooksCorpus, over 7,000 unpublished books | state of the art on 9 of 12 tasks |
| BERT-large | 2018 | Google | 340 million | BooksCorpus (800 million words) and English Wikipedia (2,500 million words) | GLUE 80.5 (GPT-1: 72.8) |
| GPT-2 | 2019 | OpenAI | 1.5 billion | WebText, about 8 million web documents, 40 GB | best on 7 of 8 language-modelling datasets without task training |
| GPT-3 | 2020 | OpenAI | 175 billion | 300 billion tokens; 3.14 × 10^23^ operations of training compute | few-shot learning across many tasks |

: Table 1.4: The first pre-trained language models. The 117 million figure for GPT-1 is the size reported for the equivalent model in the GPT-2 paper. Source: [@radford2018improving; @devlin2019bert; @radford2019language; @brown2020language].

Between GPT-1 and GPT-3, in two years, model size grew by a factor of about 1,500. Chapter 4 explains the scaling laws, published in 2020, that describe how a language model's error falls as parameters, data and compute increase. GPT-3 and its peers prompted the Stanford group mentioned in Section 1.3 to coin "foundation model" in 2021. Their report warned that the defects of a foundation model are "inherited by all the adapted models downstream", because many applications rest on the same few base models [@bommasani2021opportunities].

### Assistants, reasoning models and agents

ChatGPT put a large language model, further trained to follow instructions and hold a conversation (Section 3.5), behind a free chat window. Independent surveys confirm the speed of adoption, although they measure something different from company user counts. By August 2025, 54.6% of US adults aged 18 to 64 used generative AI, according to nationally representative surveys run by Alexander Bick, Adam Blandin and David Deming [@bick2025state]. In their first working paper the same authors found that, measured from each technology's first mass-market product, adoption "has been faster than either PCs or the internet" [@bick2024rapid]. (That paper's late-2024 estimate of "nearly 40 percent" was later revised upwards when the authors reweighted their earlier rounds, the August 2024 figure from 39.4% to 44.6% [@bick2025state].) Measured differently, from Microsoft's data on the share of each country's population using AI tools, the United States ranked only 24th, at 28.3%, in the second half of 2025, and adoption "correlates strongly with GDP per capita" [@sajadieh2026ai, ch. 4]. Self-reported use in a survey and telemetry from one company's tools count different things. Chapter 8 examines adoption and its economic effects.

**Reasoning models**, introduced in 2024 and 2025, are language models trained to produce a long chain of intermediate steps before answering. OpenAI's o1 models, according to the company, are "trained with large-scale reinforcement learning to reason using chain of thought" [@openai2024o1]. The Chinese company DeepSeek reported in *Nature* that such abilities "can be incentivized through pure reinforcement learning", without human-written examples of step-by-step reasoning [@guo2025deepseek]. Whether these step-by-step outputs are reasoning in the human sense is an open question (Section 3.7).

During 2025 and 2026 came agents built around language models. In November 2024 Anthropic released the Model Context Protocol, "an open standard for connecting AI assistants to the systems where data lives" [@anthropic2024introducing]. Researchers at METR, an organisation that evaluates AI systems, measured the length of software tasks, in skilled-human working time, that AI agents complete with 50% success. In a study first posted in March 2025 they reported that this "time horizon" had been "doubling approximately every seven months since 2019" (later revised; see Chapter 4) [@kwa2025measuring]. On OSWorld, a benchmark of real computer tasks published in 2024, the best model then completed about 12% of tasks [@xie2024osworld]; by early 2026 the best agent reached 66.3% [@sajadieh2026ai]. On a corrected edition, OSWorld-Verified, the best general-purpose model reached about 86% by August 2026 [@osworld2026verified]. Chapter 5 examines how far such benchmark scores carry over to real work.

Figure 1.3 places these developments on a single timeline.

![Figure 1.3: Selected milestones in the history of AI, 1950–2026. Shaded bands mark the two AI winters, whose start and end dates are approximate. Research milestones are to the left of the axis, deployment and policy events to the right; the axis is compressed before 2005. Sources: @turing1950computing; @mccarthy2006proposal; @samuel1959studies; @lighthill1973artificial; @yu1979antimicrobial; @mcdermott1985dark; @mitchell2021why; @rumelhart1986learning; @brown1990statistical; @ibm2025deep; @deng2009imagenet; @seide2011conversational; @krizhevsky2012imagenet; @silver2016mastering; @vaswani2017attention; @devlin2019bert; @brown2020language; @bommasani2021opportunities; @chatterji2025how; @oecd2024explanatory; @europeanparliament2024regulation; @openai2024o1; @anthropic2024introducing; @guo2025deepseek; @malik2026chatgpt.](../figures/svg/fig-01-03.svg){#fig:01-03}

::: {.box .debate}
**Debate: Is hand-built knowledge a dead end?**

The history above can be read as one long argument. The reinforcement-learning researcher Richard Sutton, in an influential 2019 essay, holds that "general methods that leverage computation are ultimately the most effective, and by a large margin": researchers repeatedly built human knowledge into their systems and were overtaken by simpler methods that used more computing power [@sutton2019bitter]. Several of his examples appear earlier in this chapter: Deep Blue's massive search in chess, statistical hidden Markov models defeating knowledge-based speech systems, and then deep learning in speech and vision. The later steps traced here fit the same pattern: task-specific networks gave way to general pre-trained ones, with gains such as the 33% relative cut in speech errors in 2011 or BERT's 7.7-point gain on GLUE in 2018.

The cognitive scientist Gary Marcus, in a preprint essay, sets out ten concerns about deep learning and argues that it "must be supplemented by other techniques if we are to reach artificial general intelligence" [@marcus2018deep]. His side of the record is also documented: AlphaGo won by combining learned networks with explicit search; today's agents call search engines, code interpreters and databases (Chapter 5); and current systems remain uneven. The 2026 AI Index notes that a model achieved a gold-medal-level score at the 2025 International Mathematical Olympiad, yet in March 2026 the best model read analogue clocks correctly only about half the time, against about 90% for humans [@sajadieh2026ai].

Both readings fit the record so far. Marcus's case would be strengthened by a capability that keeps resisting scale but yields to added structure. Sutton's would be strengthened if something long said to need built-in knowledge, such as reliable reasoning about the physical world, emerged from scale alone.
:::

## 1.8 Why "AI" is a moving target

### The AI effect

The computer scientist Larry Tesler is credited with what others later called the "AI effect". As commonly quoted, his theorem says "Artificial Intelligence is whatever hasn't been done yet"; by his own account, what he actually said, around 1970, was "Intelligence is whatever machines haven't done yet" [@tesler2024adages]. The 2016 report of the One Hundred Year Study on AI describes the same "repeating pattern known as the 'AI effect' or the 'odd paradox'": AI "brings a new technology into the common fold, people become accustomed to this technology, it stops being considered AI, and newer technology emerges". The report concludes that AI is best seen as "a continual endeavor to push forward the frontier of machine intelligence" [@stone2016artificial].

Chess is the clearest case. IBM presented Deep Blue's 1997 victory as heralding a future in which "supercomputers and artificial intelligence could simulate human thinking" [@ibm2025deep]. A generation later, the Commission's guidelines suggest that such a program may not count as an AI system at all, and treat the fact that a method "has been used in consolidated manner for many years" as one indication that it falls outside [@europeancommission2025guidelines, paras 42, 48]. In effect, the guidelines write the AI effect into regulatory practice: long familiarity counts as a sign that a technique is no longer AI.

The effect also works from inside the field. Hendler describes researchers in the 1980s dismissing working expert systems as "not really AI" [@hendler2008avoiding], and Mitchell notes that machine-learning researchers of the 1990s and 2000s kept their distance from the label [@mitchell2021why]. This is one reason why spam filters, recommender systems and statistical translation were rarely called AI when they were introduced, although they meet the definitions in Section 1.2. Statistics on "AI investment", "AI adoption" or "AI patents" depend on where such boundaries are drawn, and the boundaries move.

### AI as a brand and a marketing claim

The label has commercial value, and its scope has followed money. Haigh notes that in the 1980s "expert systems" was often promoted as "a less controversial alternative to artificial intelligence", and that later neural-network work was pursued under brands such as machine learning and pattern recognition. Only in the last few years, he writes, has the AI label been "flipped to refer primarily to deep learning and generative systems" [@haigh2024how].

When the label is fashionable it is also claimed falsely, and regulators have started to penalise such claims. In March 2024 the US Securities and Exchange Commission fined two investment advisers, Delphia and Global Predictions, a total of $400,000 for telling clients that they used AI in ways that they did not; its chair called the practice "AI washing" [@sec2024sec]. In September 2024 the Federal Trade Commission announced five enforcement actions under the name Operation AI Comply, against firms that, in its words, had "seized on the hype surrounding AI" to lure consumers into bogus schemes or that sold AI tools that "can turbocharge deception". One of them, DoNotPay, had advertised "the world's first robot lawyer" and agreed to pay $193,000; the FTC's chair said that "there is no AI exemption from the laws on the books" [@ftc2024announces].

Scholars of technology go further. The journalist and software developer Meredith Broussard warns against "technochauvinism", the belief that technology is always the solution [@broussard2018artificial]. Kate Crawford argues that AI is best understood as a material and political system, built from extracted minerals, low-paid labour and personal data, that tends to concentrate power [@crawford2021atlas]. The anthropologist Lucy Suchman argues that treating AI as a single "thing" helps to attract further investment, and asks for attention to the specific techniques that "travel under the sign of AI", where they are used and with what effects [@suchman2023uncontroversial]. These critics do not deny that the techniques work. Their question sits beside the legal one in Section 1.2: which systems a single name should cover, and who gains from grouping them.

### Springs, winters and the language of progress

Mitchell describes the history of the field as a cycle of AI "springs" and "winters": periods of "optimistic predictions and massive investment" followed by "disappointment, loss of confidence, and reduced funding". Simon's twenty-year prediction of 1960 did not come true, and neither did the commercial hopes of the 1980s. She traces over-optimism partly to systematic errors in reasoning about intelligence, one of which she calls "easy things are easy and hard things are hard": what humans do without thought, such as making sense of a visual scene, has proved among the hardest things for machines [@mitchell2021why]. The documented causes of past winters were specific: a combinatorial explosion that hardware could not overcome, rule bases that were costly to maintain and brittle outside their domain, a hardware market undercut by general-purpose machines, and funding promised against applications that did not arrive. Whether the present boom shares any of these weaknesses is a question for Chapter 14.

The official definitions were written with this moving target in mind. By defining AI through inference and outputs rather than any technique, the OECD and the EU tried to cover both the symbolic and the learning traditions and whatever comes next [@oecd2024explanatory; @europeanparliament2024regulation]. The OECD memorandum states that "additional techniques and applications will likely emerge in the future" and asks users of its definition to "exercise judgement on its relevant scope" [@oecd2024explanatory, p. 6].

Over seventy years the name has covered heuristic search, hand-written rules, statistical models estimated from data and deep networks trained on vast corpora, and the traditions have kept borrowing from one another, as AlphaGo's tree search and today's tool-using agents show. A recurring gap separates results on bounded tasks from dependable use: MYCIN matched specialists and never reached a ward, and benchmark records have often measured less than the headlines they drew. The legal definitions now in force draw their boundary by function, which brings 1970s expert systems inside and may leave a classical chess program out. Figures on AI adoption, investment or risk therefore depend on which systems are counted, under which definition and at what date.

## Further reading

- Turing, A. M. (1950). *Computing machinery and intelligence*. Short, readable and still the starting point for debates about machine intelligence and how to test it. [@turing1950computing]
- McCarthy, J., Minsky, M., Rochester, N., & Shannon, C. (1955/2006). *A proposal for the Dartmouth summer research project on artificial intelligence*. Twelve pages that show what the founders thought the problems were, and how small they expected the effort to be. [@mccarthy2006proposal]
- Buchanan, B. G., & Shortliffe, E. H. (Eds.) (1984). *Rule-based expert systems: The MYCIN experiments*. The fullest first-hand account of how an expert system was built, tested and abandoned, freely available online. [@buchanan1984rule]
- Halevy, A., Norvig, P., & Pereira, F. (2009). *The unreasonable effectiveness of data*. A five-page statement of why statistical methods trained on large corpora overtook hand-built models. [@halevy2009unreasonable]
- European Commission (2025). *Guidelines on the definition of an artificial intelligence system*. Shows how a regulator turns an abstract definition into concrete inclusions and exclusions. [@europeancommission2025guidelines]
- Mitchell, M. (2021). *Why AI is harder than we think*. An accessible account of AI's springs and winters and of the reasoning errors that drive over-optimism. [@mitchell2021why]


# Chapter 2: How Neural Networks Learn

In July 1958 the US Office of Naval Research demonstrated a program designed by Frank Rosenblatt, a research psychologist at the Cornell Aeronautical Laboratory. Running on an IBM 704 computer, it was shown punch cards marked either on the left or on the right, and after 50 trials it had learned to tell the two kinds apart [@lefkowitz2019professors]. The day after the press demonstration, *The New York Times* reported that the Navy had revealed "the embryo of an electronic computer" that it expected "will be able to walk, talk, see, write, reproduce itself and be conscious of its existence" [@newyorktimes1958new, p. 25; as reproduced in @ananthaswamy2024why]. None of that happened. Four decades later a descendant of Rosenblatt's idea did something more modest and more useful: LeNet-5, a network built at AT&T Labs, was reading the amounts, handwritten or printed, on millions of bank cheques a month in the United States. It had about 60,000 adjustable numbers [@lecun1998gradient].

Neither machine was given rules describing a "left mark" or a handwritten "7". Both were shown examples and adjusted internal numbers until their answers were mostly right. The adjustment procedure used today keeps LeNet's outline, whether the network reads cheques or, like GPT-3, has 175 billion adjustable numbers [@brown2020language]. A loss function scores each answer, backpropagation works out how every number contributed to the score, and an optimiser nudges every number downhill. The rest of the engineering exists to make that loop work on networks hundreds of layers deep and to make the result hold up on data the network has never seen.

## 2.1 The artificial neuron

An **artificial neuron** is a small calculation. It takes *n* input numbers *x*₁ … *x*~n~, multiplies each by a **weight** *w*~i~, adds the products together with a **bias** *b*, and passes the total *z* through an **activation function** *f*:

*z* = *w*₁*x*₁ + *w*₂*x*₂ + … + *w*~n~*x*~n~ + *b*,  output = *f*(*z*).

The weights say how strongly, and in which direction, each input pushes the output: a positive weight pushes it up, a negative one down. The bias shifts the total and so sets how readily the neuron produces a non-zero output. With two inputs 2 and 1, weights 0.5 and −1, and bias 0.2, the total is *z* = 0.5 × 2 + (−1) × 1 + 0.2 = 0.2. Figure 2.1 traces this calculation.

![Figure 2.1: A single artificial neuron computing its output from two inputs. Each input is multiplied by its weight, the products and the bias are added (0.5 × 2 + (−1) × 1 + 0.2 = 0.2), and the activation function (here ReLU, which turns negative totals into zero) produces the output. With inputs 1 and 1 the total would be −0.3 and the output 0. Diagram by the author.](../figures/svg/fig-02-01.svg){#fig:02-01}

The idea is older than computers that could run it. Warren McCulloch and Walter Pitts proposed in 1943 that, because of the "all-or-none" character of nervous activity, networks of idealised neurons could be analysed with propositional logic [@mcculloch1943logical, p. 115]. Their units fired when the input total crossed a threshold, and their connections were fixed. Rosenblatt's **perceptron** kept the threshold but made the connection strengths change with experience. He argued that the brain's information is "contained in connections or associations rather than topographic representations" [@rosenblatt1958perceptron, p. 387], and his machine stored what it learned in exactly that way.

### Activation functions

The threshold of McCulloch, Pitts and Rosenblatt jumps from 0 to 1. A jump has no slope, and gradient-based learning (Section 2.3) needs a slope to know which way to adjust a weight. Modern networks therefore use smooth or piecewise-straight activation functions. The classic choices are:

- the **logistic sigmoid**, σ(*z*) = 1 / (1 + e^−*z*^), which squashes any total into the range 0 to 1;
- the **hyperbolic tangent**, tanh(*z*), an S-curve with the same shape but running from −1 to 1;
- the **rectified linear unit** (**ReLU**), max(0, *z*), which keeps positive totals unchanged and turns negative ones into zero.

| Activation | *f*(−2) | *f*(0) | *f*(0.2) | *f*(2) | Slope at *z* = 0.2 | Largest possible slope |
|---|---|---|---|---|---|---|
| Sigmoid | 0.119 | 0.500 | 0.550 | 0.881 | 0.248 | 0.25 (at *z* = 0) |
| tanh | −0.964 | 0.000 | 0.197 | 0.964 | 0.961 | 1 (at *z* = 0) |
| ReLU | 0 | 0 | 0.2 | 2 | 1 | 1 (any *z* > 0) |

: Table 2.1: Three activation functions evaluated at four totals, with their slopes. The slope matters because backpropagation multiplies slopes together layer after layer (Sections 2.4–2.5). Calculation by the author.

The sigmoid's slope never exceeds 0.25 and falls towards zero once the total is far from zero (Table 2.1). A neuron in that flat region is said to **saturate**, and almost no learning signal passes through it. ReLU has slope exactly 1 for every positive total. In work on AlexNet, the network that won the 2012 ImageNet competition, a four-layer test network with ReLUs reached 25% training error on the CIFAR-10 image dataset six times faster than the same network with tanh units [@krizhevsky2012imagenet]. In 2016 Goodfellow, Bengio and Courville's textbook *Deep Learning* called ReLU "the default recommendation" for modern networks [@goodfellow2016deep, sec. 6.1]. The price is that a ReLU unit whose total is negative passes no gradient at all, so it "cannot learn" from those examples [@goodfellow2016deep, sec. 6.3.1].

Transformer language models have since moved to smoother relatives. BERT used the Gaussian error linear unit (GELU), *z*Φ(*z*), where Φ(*z*) is the probability that a standard normal random number falls below *z* [@hendrycks2016gaussian; @devlin2019bert]. Noam Shazeer reported in 2020 that several "gated" variants, which multiply an activated linear projection of the input by a second, plain projection, improved quality over ReLU and GELU in transformers [@shazeer2020glu]. One of them, SwiGLU, was adopted by PaLM and Llama (Chapter 3) [@chowdhery2023palm; @touvron2023llama].

## 2.2 Layers, matrices and what depth buys

A single neuron draws one straight boundary through its input space: everything on one side of the line *z* = 0 gets one kind of output, everything on the other side the other kind. Some simple problems cannot be solved that way. The best-known is **XOR** ("exclusive or"): the output should be 1 when exactly one of two inputs is 1, and 0 when both are 0 or both are 1. Marvin Minsky and Seymour Papert's 1969 book *Perceptrons* proved this and related limits of single-layer perceptrons [@minsky1969perceptrons], and the critique contributed to a backlash against neural network research [@goodfellow2016deep, sec. 1.2.1].

The remedy is to stack neurons in **layers**. Each neuron in a **hidden layer** takes all the previous layer's outputs as its inputs; the values it computes are "hidden" because the training data never specify them. A network in which every neuron feeds every neuron of the next layer is a **multilayer perceptron** (MLP). Figure 2.2 shows one with three inputs, four hidden neurons and two outputs.

![Figure 2.2: A small multilayer perceptron with three inputs, one hidden layer of four neurons and two outputs. Each line is a connection with its own weight, and each hidden and output neuron also has a bias. The first layer's weights form a 4 × 3 matrix and the second layer's a 2 × 4 matrix, giving 3 × 4 + 4 × 2 = 20 weights and 4 + 2 = 6 biases: 26 parameters in all. Diagram by the author.](../figures/svg/fig-02-02.svg){#fig:02-02}

### The matrix view of a layer

Writing out every neuron separately soon becomes unwieldy. A layer of *m* neurons, each receiving the same *n* inputs, has *m* × *n* weights. Arranged as a grid with one row per neuron, they form a **weight matrix** *W*, and the whole layer is one line:

**h** = *f*(*W***x** + **b**),

where **x** is the list (vector) of inputs, **b** the list of biases and *f* is applied to each entry separately. Each entry of *W***x** is one neuron's weighted sum: row times inputs, added up. Take a layer with two neurons and three inputs, rows *W* = [0.5, −1, 2] and [1, 0.5, 0], biases (0.1, −0.2) and input **x** = (1, 2, −1). The first neuron computes 0.5 × 1 + (−1) × 2 + 2 × (−1) + 0.1 = −3.4, the second 1 × 1 + 0.5 × 2 + 0 × (−1) − 0.2 = 1.8. After ReLU, the layer outputs (0, 1.8).

The matrix form has a practical payoff. If a network processes a batch of examples at once, their input vectors can be placed side by side as the columns of a matrix *X*, and the layer becomes one matrix–matrix product *WX*. Almost all the arithmetic of training is therefore matrix multiplication, which is why specialised hardware matters (Section 2.6). The same notation shows why the activation function is indispensable. Without it, two layers compute *W*₂(*W*₁**x**) = (*W*₂*W*₁)**x**, which is just another single matrix. However many purely linear layers are stacked, the result can still only draw straight boundaries. The bends in ReLU or the sigmoid, called **non-linearities**, are what let each extra layer add capability.

### XOR with one hidden layer

Two hidden ReLU neurons solve XOR, using weights given by Goodfellow and colleagues [@goodfellow2016deep, sec. 6.1]. The first hidden neuron, *h*₁, outputs the sum of the two inputs. The second, *h*₂, outputs the sum minus 1, which ReLU turns into 0 when negative. The output neuron computes *h*₁ − 2*h*₂. Table 2.2 checks all four cases.

| Inputs | Correct answer | *h*₁ = sum | *h*₂ = ReLU(sum − 1) | Output = *h*₁ − 2*h*₂ |
|---|---|---|---|---|
| (0, 0) | 0 | 0 | 0 | 0 |
| (1, 0) | 1 | 1 | 0 | 1 |
| (0, 1) | 1 | 1 | 0 | 1 |
| (1, 1) | 0 | 2 | 1 | 0 |

: Table 2.2: How a hidden layer solves XOR. The hidden neurons re-describe each pair of inputs as a new pair (*h*₁, *h*₂); in those coordinates a single weighted sum gives the right answer in all four cases. Calculation by the author, following @goodfellow2016deep.

In the original inputs the two cases that should give 1, (1, 0) and (0, 1), sit at opposite corners of a square, with the 0 cases at the other two corners, so no straight line separates them. In the hidden coordinates both 1 cases land on the same point, (1, 0), while the 0 cases land at (0, 0) and (2, 1). The line *h*₁ − 2*h*₂ = 0.5 now has the 1 cases on one side and the 0 cases on the other. The hidden layer has transformed the problem into one a straight line can solve, which is the job hidden layers do in every network.

### Width, depth and parameter counts

In 1989 George Cybenko proved that a single hidden layer of sigmoid neurons, if it is wide enough, can approximate any continuous function (any input–output rule without sudden jumps) as closely as desired [@cybenko1989approximation]. The result guarantees that suitable weights *exist*, but not how many neurons are needed, nor that training will find them [@goodfellow2016deep, sec. 6.4.1]. Depth helps with the first problem. Goodfellow and colleagues summarise theoretical results showing that some functions computable by a network of a given depth would need, in a shallower network, a number of hidden units exponential in the input size, and that networks of ReLU-like units can carve the input space into a number of regions that grows exponentially with depth [@goodfellow2016deep, sec. 6.4.1]. In practice, the networks that have succeeded on real tasks stack many layers, which is where the term "deep" learning comes from [@lecun2015deep].

Every weight and bias is a **parameter**, a number adjusted by training, and parameter counts are the usual measure of a network's size. The network in Figure 2.2 has 26. LeNet-5 had about 60,000 [@lecun1998gradient]. AlexNet had 60 million parameters and 650,000 neurons [@krizhevsky2012imagenet], and GPT-3 had 175 billion parameters [@brown2020language]. The arithmetic inside each neuron is no harder in GPT-3 than in Figure 2.1. What differs is the number of neurons, how they are wired and how the weights were set.

## 2.3 Loss functions and gradient descent

A freshly built network starts with random weights and gives arbitrary answers. **Training** adjusts the weights so that the answers improve. In **supervised learning** the network is given examples whose correct answer, the **label**, is known: images labelled "cat" or "dog", scanned digits labelled 0 to 9. Language models use a variant in which the label is simply the next token of a text (Chapter 3).

### Measuring error

Learning needs a single number that says how wrong the network is. That number is the **loss**, computed by a **loss function** from the network's output and the label. For predicting a quantity, the usual choice is the **squared error**, (*y* − *t*)², where *y* is the output and *t* the target. If the target is 1 and the network outputs 0.2, the loss is 0.8² = 0.64; an output of 0.9 gives 0.01. Squaring makes every error positive and punishes large errors disproportionately. The loss for a whole dataset is the average over its examples.

For classification, the network's final layer produces one raw score per class, called a **logit**, and a **softmax** function turns the scores into probabilities that are positive and add up to 1:

*p*~k~ = e^*z*~k~^ / (e^*z*~1~^ + e^*z*~2~^ + … + e^*z*~K~^).

Logits of 2.0, 1.0 and 0.1 for three classes become probabilities of 0.659, 0.242 and 0.0986. The loss is then the **cross-entropy**: the negative natural logarithm of the probability given to the correct class, −ln *p*~correct~. If the correct class is the first, the loss is −ln 0.659 = 0.417; if it is the third, −ln 0.0986 = 2.317. Each tenfold fall in the probability given to the right answer adds ln 10 ≈ 2.3 to the loss, so a network that is confidently wrong is punished far more than one that is unsure.

Cross-entropy is preferred over squared error for classification because of its gradients. Output units that saturate, such as a sigmoid far from zero, produce very small gradients when combined with squared error, which leads to poor results with gradient-based training [@goodfellow2016deep, sec. 6.2.1]. With a softmax or sigmoid output and cross-entropy loss, the slope of the loss with respect to each logit works out to the simple difference *p* − *t* between predicted probability and target (1 for the correct class, 0 otherwise). The signal is large when the network is badly wrong and never vanishes because the output unit has saturated.

### Walking downhill

With a loss defined, learning becomes an optimisation problem: find the weights that make the average loss as small as possible. Yann LeCun, Yoshua Bengio and Geoffrey Hinton, in a widely cited 2015 review, call the weights "knobs" that define the network's behaviour; with millions of them, trial and error is hopeless [@lecun2015deep, p. 436]. What makes the search feasible is the **gradient**: for every weight, the rate at which the loss changes when that weight is increased by a tiny amount [@lecun2015deep, p. 436]. **Gradient descent** moves every weight a small step against its gradient:

*w* ← *w* − *η* × ∂*L*/∂*w*.

Here ∂*L*/∂*w* (read "the partial derivative of *L* with respect to *w*") is the slope of the loss in the direction of that one weight, and *η* (eta) is the **learning rate**, a step-size setting chosen by the people doing the training. The image is a walker in fog who cannot see the valley but can feel the slope underfoot (Figure 2.3).

![Figure 2.3: Gradient descent pictured as walking downhill. The curve shows how the loss (vertical axis) changes as one weight (horizontal axis) changes, for the worked example in the text, whose minimum is at weight 0.5; the right-hand panel enlarges the boxed region near the minimum. Starting at weight 0.2, each step moves against the slope; a learning rate of 0.1 closes 80% of the remaining gap per step, while a learning rate of 0.5 overshoots to 1.4, where the loss is higher than at the start. Real networks have millions of weights, so the true landscape has millions of dimensions. Diagram by the author.](../figures/svg/fig-02-03.svg){#fig:02-03}

A one-weight example shows the mechanics. A neuron with no bias and no activation function receives the input *x* = 2 and has weight *w* = 0.2; the target is 1. The output is 0.4, the error 0.4 − 1 = −0.6 and the squared-error loss 0.36. The exact slope is 2(*wx* − *t*)*x* = 2 × (−0.6) × 2 = −2.4. (Nudging the weight to 0.21 confirms it: the output becomes 0.42 and the loss 0.3364, a fall of 0.0236 for a rise of 0.01.) With learning rate 0.1 the step is −0.1 × (−2.4) = +0.24, so the weight moves to 0.44, the output to 0.88 and the loss to 0.0144. Further steps close in on 0.5, where the loss is zero.

The same example shows why the learning rate is delicate. Each step multiplies the remaining error by 1 − 2*ηx*² = 1 − 8*η*. With *η* = 0.1 the factor is 0.2, so the error shrinks fivefold per step. With *η* = 0.5 the factor is −3: the weight jumps to 1.4 and the loss rises to 3.24; every further step makes it worse. Any learning rate above 0.25 diverges here. The threshold is set by the curvature of the loss (here 2*x*² = 8): steeply curved directions tolerate only small steps. In a real network, curvature differs enormously between directions, and the largest stable learning rate is set by the most sharply curved one.

### What the landscape is like

The fog image misleads. The real landscape has as many dimensions as the network has parameters. Because the gradient is usually estimated from a small random batch of examples (Section 2.5), the ground shifts slightly at every step. Most importantly, the feared trap of a small hollow far above the best valley, a poor **local minimum**, turned out to matter less than expected in large networks. The 2015 review reports that poor local minima "are rarely a problem" and that the flat places training meets are mostly **saddle points**, which curve upwards in some directions and downwards in others, and that almost all of them have similar loss values [@lecun2015deep, p. 438].

## 2.4 Backpropagation: the chain rule at scale

Gradient descent needs ∂*L*/∂*w* for every weight. One way is to nudge each weight and re-run the network, as in the one-weight example. For AlexNet's 60 million parameters that would mean 60 million extra forward passes per step. This is the **credit assignment problem**: when the final answer is wrong, how much of the blame belongs to each connection, including those buried many layers deep?

**Backpropagation** answers it with a cost comparable to running the network once. Training alternates two passes. The **forward pass** sends an example through the network, layer by layer, and computes the loss, storing every intermediate value. The **backward pass** sends the error signal the other way. At each layer it computes how the loss depends on that layer's outputs, from which the gradients for the layer's weights follow directly, and it passes the signal down to the layer below. Goodfellow and colleagues show that for standard networks the backward computation is of the same order of cost as the forward one [@goodfellow2016deep, sec. 6.5].

Counting operations, a forward pass through fully connected layers costs about two operations (a multiplication and an addition) per parameter for each input it processes (for a language model, each token), and the backward pass roughly twice that, since it computes gradients both for the weights and for the inputs of each layer. A full training step therefore costs about three forward passes. This is the origin of the rule of thumb in Chapter 4, taken from a 2020 preprint by Jared Kaplan and colleagues: training a model of *N* parameters costs about 6*N* operations per token, while generating text, which needs only the forward pass, costs about 2*N* [@kaplan2020scaling]. *N* excludes the embedding tables that turn tokens into vectors, and the rule omits attention's comparisons between tokens, whose cost grows with context length; Kaplan and colleagues judged that term small when each token's vector is longer than a twelfth of the context [@kaplan2020scaling].

The mathematics is the **chain rule** of calculus: if *a* affects *b* and *b* affects *c*, the rate at which *c* changes with *a* is the product of the two individual rates, ∂*c*/∂*a* = (∂*c*/∂*b*) × (∂*b*/∂*a*). A network is a long chain of such dependencies. The rule is centuries old; efficient ways of applying it to long chains of computation were developed from the 1960s onwards and discovered for neural networks several times over [@goodfellow2016deep, sec. 6.6]. A 1986 *Nature* paper by David Rumelhart, Geoffrey Hinton and Ronald Williams made the method widely known. It reported that, as the weights adjusted, "internal 'hidden' units which are not part of the input or output come to represent important features of the task domain" [@rumelhart1986learning, p. 533].

Nobody now writes the backward pass by hand. Deep learning software such as TensorFlow and PyTorch records the operations of the forward pass as a **computational graph**, in which each node is a variable and arrows lead from each operation's inputs to its result, and applies the chain rule to that graph automatically. Backpropagation is a special case of what the wider field calls reverse-mode **automatic differentiation**, which works for any numerical function written as a program [@goodfellow2016deep, secs. 6.5.1, 6.5.9; @baydin2018automatic].

::: {.box .deeper}
**Going deeper: Backpropagation through a nine-parameter network**

The network has two inputs, two hidden ReLU neurons and one sigmoid output trained with cross-entropy. The input is **x** = (1, 2) and the target is *t* = 1. The hidden weights are (0.5, 0.25) for *h*₁ and (−0.5, 0.5) for *h*₂, both hidden biases are 0, the output weights are *v* = (1, −1) and the output bias is *c* = 0.

*Forward pass.* *z*₁ = 0.5 × 1 + 0.25 × 2 = 1.0 and *z*₂ = −0.5 × 1 + 0.5 × 2 = 0.5, both positive, so *h* = (1.0, 0.5). The output logit is *z* = 1 × 1.0 + (−1) × 0.5 + 0 = 0.5, the probability *p* = σ(0.5) = 0.6225 and the loss *L* = −ln 0.6225 = 0.4741.

*Backward pass.* Each line reuses the line before it.

| Quantity | Rule | Value |
|---|---|---|
| ∂*L*/∂*z* | *p* − *t* | −0.3775 |
| ∂*L*/∂*v*₁, ∂*L*/∂*v*₂ | ∂*L*/∂*z* × *h*₁, × *h*₂ | −0.3775, −0.1888 |
| ∂*L*/∂*c* | ∂*L*/∂*z* × 1 | −0.3775 |
| ∂*L*/∂*h*₁, ∂*L*/∂*h*₂ | ∂*L*/∂*z* × *v*₁, × *v*₂ | −0.3775, +0.3775 |
| ∂*L*/∂*z*₁, ∂*L*/∂*z*₂ | × ReLU slope (1, as both totals are positive) | −0.3775, +0.3775 |
| Gradients for *h*₁'s weights | ∂*L*/∂*z*₁ × *x*₁, × *x*₂ | −0.3775, −0.7551 |
| Gradients for *h*₂'s weights | ∂*L*/∂*z*₂ × *x*₁, × *x*₂ | +0.3775, +0.7551 |
| Gradients for hidden biases | ∂*L*/∂*z*₁, ∂*L*/∂*z*₂ | −0.3775, +0.3775 |

: Table 2.3: Backward-pass quantities for the nine-parameter network. All values rounded to four decimal places. Calculation by the author.

The signs make sense. The network should raise *p*, so the gradient says: strengthen the connection from *h*₁, whose output feeds the logit positively, and weaken *h*₂, whose output feeds it negatively through *v*₂ = −1. *Update.* With learning rate 0.1, every parameter moves by −0.1 times its gradient: *h*₁'s weights become (0.5378, 0.3255), *h*₂'s become (−0.5378, 0.4245), the hidden biases (0.0378, −0.0378), *v* = (1.0378, −0.9811) and *c* = 0.0378. Re-running the forward pass gives *h* = (1.2265, 0.2735), *z* = 1.0423, *p* = 0.7393 and a loss of 0.3021, down from 0.4741. Nudging each of the nine parameters by 0.000001 and re-running the network reproduces every gradient in the table, the standard check that a backpropagation implementation is correct. Real networks perform the same steps with matrices: the backward pass through a layer multiplies the incoming signal by the transpose of its weight matrix [@goodfellow2016deep, sec. 6.5; @lecun2015deep, fig. 1].
:::

## 2.5 Making deep networks trainable

Gradient descent and backpropagation were in place by 1986. Networks with more than a few layers nonetheless remained hard to train for another two decades. Xavier Glorot and Yoshua Bengio opened their 2010 analysis by observing that before 2006 deep multilayer networks appear not to have been "successfully trained" [@glorot2010understanding, p. 249]. Goodfellow and colleagues judge that most of the advances in neural network optimisation over thirty years came from changing the model, such as the activation functions and connection patterns, rather than the optimisation algorithm [@goodfellow2016deep, sec. 8.7.5].

### Minibatches, epochs and schedules

Computing the exact average loss over millions of training examples before each step would be slow. **Stochastic gradient descent** (SGD) instead estimates the gradient from a **minibatch**, a small random sample of examples, takes a step, and draws the next batch. One pass through the whole training set is an **epoch**. Each estimate is noisy, yet the procedure "usually finds a good set of weights surprisingly quickly" [@lecun2015deep, p. 437]. AlexNet made about 90 passes over its 1.2 million images; Table 2.4 gives the rest of its recipe [@krizhevsky2012imagenet]. Batch size interacts with learning rate. In a 2017 preprint, Goyal and colleagues at Facebook trained an image network with batches of 8,192 images on 256 GPUs in one hour, without loss of accuracy. They multiplied the learning rate by *k* whenever the batch grew *k*-fold and ramped it up gradually over the first five epochs, a **warm-up** [@goyal2017accurate].

The original transformer used a similar warm-up over 4,000 steps, then let the learning rate decay with the inverse square root of the step number [@vaswani2017attention]. Large language models more often follow the warm-up with **cosine decay**, which lowers the rate along half a cosine curve, a shape taken from Ilya Loshchilov and Frank Hutter's work on SGD with restarts [@loshchilov2017sgdr]; Llama's rate fell this way to a tenth of its peak [@touvron2023llama]. The **warmup–stable–decay** schedule, proposed in 2024 for the MiniCPM models, holds the rate constant for most of training and decays it only at the end, so that the length of training need not be fixed in advance and saved intermediate models can be reused [@hu2024minicpm]. Kimi K2, a model of about a trillion parameters released in 2025, kept its rate constant for its first 10 trillion tokens before a cosine decay [@kimiteam2025kimi].

### Momentum

Plain gradient descent struggles in long, narrow valleys: the steep walls make it zig-zag from side to side while it creeps along the gentle floor. **Momentum** gives the walker inertia. A velocity *v* accumulates past gradients, and the weights move by the velocity:

*v* ← *β v* − *η g*,  *w* ← *w* + *v*,

where *g* is the current gradient and *β* (typically 0.9) controls how quickly old gradients fade. Gradients that keep pointing the same way add up, while those that alternate in sign cancel. If the gradient is constant, the step grows to 1 / (1 − *β*) times the plain step, so *β* = 0.9 multiplies the top speed by ten [@goodfellow2016deep, sec. 8.3.2]. The build-up is gradual: with *β* = 0.9 the step reaches 6.5 times the plain step after ten iterations. AlexNet and the 2015 ResNets used momentum 0.9 (Table 2.4).

### Adam

A single learning rate for all weights is a compromise when some weights receive large gradients and others tiny ones. **Adam** ("adaptive moment estimation"), introduced by Diederik Kingma and Jimmy Ba, gives every weight its own effective step size [@kingma2015adam]. At step *t*, with gradient *g*~t~, it keeps two running averages per weight:

- *m*~t~ = *β*₁ *m*~t−1~ + (1 − *β*₁) *g*~t~, an average of recent gradients (momentum);
- *v*~t~ = *β*₂ *v*~t−1~ + (1 − *β*₂) *g*~t~², an average of recent squared gradients (their typical size).

Both start at zero, which biases them towards zero early on, so Adam divides by (1 − *β*₁^*t*^) and (1 − *β*₂^*t*^) to correct this, giving *m̂*~t~ and *v̂*~t~. The update is

*w* ← *w* − *α* × *m̂*~t~ / (√*v̂*~t~ + *ε*).

In words: move in the direction of the averaged gradient, divided by the typical gradient size for that weight. The paper's suggested defaults are *α* = 0.001, *β*₁ = 0.9, *β*₂ = 0.999 and *ε* = 10^−8^ [@kingma2015adam, Algorithm 1]. Because the gradient appears in both numerator and denominator, its scale cancels. Applied to the one-weight example of Section 2.3 (gradient −2.4), the first step gives *m*₁ = −0.24 and *v*₁ = 0.00576. Bias correction turns these back into −2.4 and 5.76, and the step is +0.001 × 2.4 / 2.4 = +0.001. Had the gradient been a hundred times smaller, −0.024, the step would still have been 0.001. Kingma and Ba describe this as a "trust region": the size of each step is roughly bounded by *α*, whatever the scale of the gradients [@kingma2015adam, sec. 2.1].

The original transformer was trained with Adam (Table 2.4). A known flaw was fixed by Ilya Loshchilov and Frank Hutter, who showed that the usual way of adding weight decay (Section 2.7) to Adam, as a penalty term in the loss, does not behave as it does with SGD, and that decoupling the decay from the gradient step, a variant called AdamW, "substantially improves Adam's generalization performance" [@loshchilov2019decoupled]. In 2016 Goodfellow and colleagues found that the choice of optimiser "seems to depend largely on the user's familiarity with the algorithm" [@goodfellow2016deep, sec. 8.5.4]. AdamW has since become the common choice for pre-training large language models; Llama, Llama 3 and DeepSeek-V3 were all trained with it [@touvron2023llama; @grattafiori2024llama; @deepseekai2024deepseekv3]. Kimi K2 was trained with a variant of Muon, which passes each weight matrix's accumulated gradient through a matrix iteration (Newton–Schulz) before the step. Its developers report that Muon outperformed AdamW at equal compute in their earlier experiments but needed an added safeguard against exploding attention values at scale [@kimiteam2025kimi].

### Initialisation and vanishing gradients

Weights must start random so that neurons in the same layer differ; two units with identical weights and inputs would receive identical updates for ever [@goodfellow2016deep, sec. 8.4]. The scale of the randomness matters as much. The backward pass multiplies the error signal, layer by layer, by weights and activation slopes. If each layer shrinks the signal, the gradient reaching the early layers fades exponentially with depth; if each layer amplifies it, the gradient explodes. With sigmoid units, whose slope is at most 0.25 (Table 2.1), the slopes alone multiply the signal over ten layers by at most 0.25^10^ ≈ 0.00000095. This is the **vanishing gradient problem** [@goodfellow2016deep, sec. 8.2.5]. Glorot and Bengio found that logistic sigmoid units are "unsuited for deep networks with random initialization" because the top hidden layer is driven into saturation. They proposed drawing initial weights with a variance of 2/(*n*~in~ + *n*~out~), where *n*~in~ and *n*~out~ are the number of inputs and outputs of the layer [@glorot2010understanding].

Kaiming He and colleagues at Microsoft Research extended the analysis to ReLU networks in 2015. They showed that the variance of the signal after *L* layers is the starting variance multiplied by the product of ½ × *n* × Var[*w*] over the layers, where *n* is the number of inputs to a layer and Var[*w*] the variance of its weights [@he2015delving]. Setting the factor to exactly 1 gives the **He initialisation**: weights drawn with standard deviation √(2/*n*). For a layer with 512 inputs that is 0.0625. A fixed standard deviation of 0.01, as used in AlexNet [@krizhevsky2012imagenet], gives a factor of ½ × 512 × 0.0001 = 0.0256 per layer, so after ten such layers the signal's variance is about 10^−16^ of its starting value. He and colleagues report that a 30-layer network converged with their initialisation, while with the Glorot scheme it "completely stalls" [@he2015delving].

A common guard against exploding gradients is **gradient clipping**: whenever the length (norm) of the whole gradient exceeds a threshold, it is scaled back to that length before the step. Razvan Pascanu, Tomas Mikolov and Yoshua Bengio proposed the method for recurrent networks [@pascanu2013difficulty]; Llama and DeepSeek-V3 clip at a norm of 1.0 [@touvron2023llama; @deepseekai2024deepseekv3].

### Normalisation

Good initialisation keeps signals well scaled at the start, but the scale drifts as weights change. **Batch normalisation**, introduced by Sergey Ioffe and Christian Szegedy of Google in 2015, re-centres and re-scales each neuron's total during training. For each minibatch, it subtracts the batch mean *μ* of that neuron's totals and divides by their standard deviation, √(*σ*² + *ε*), then applies a learned scale *γ* and shift *β* so that the network can undo the normalisation where that helps. Applied to Google's Inception image network, batch normalisation reached the same accuracy "with 14 times fewer training steps" [@ioffe2015batch].

Why it works is disputed. Ioffe and Szegedy attributed the gain to reducing "internal covariate shift", the change in each layer's input distribution as earlier layers learn [@ioffe2015batch]. In 2018 Shibani Santurkar and colleagues at MIT injected random, time-varying noise after each batch-normalisation layer, deliberately making the layer inputs unstable. The networks trained about as well as before. They concluded that such distributional stability "has little to do with the success" of the method, which instead makes the loss landscape "significantly smoother", so that gradients are more predictive and larger steps are safe [@santurkar2018how]. Batch normalisation also makes each example's output depend on the other examples in its batch. **Layer normalisation**, proposed in a 2016 preprint by Jimmy Ba, Jamie Kiros and Geoffrey Hinton, computes the mean and variance over the neurons of a layer for a single example instead [@ba2016layer]. Transformers use it: in the original design, each sub-layer's output was LayerNorm(*x* + Sublayer(*x*)) [@vaswani2017attention]. Later language models moved the normalisation to the input of each sub-layer (Chapter 3), a change Llama's developers adopted "to improve the training stability" [@radford2019language; @touvron2023llama]. Llama also replaced layer normalisation with **RMSNorm**, which rescales the totals by their root mean square without subtracting their mean and is cheaper to compute [@zhang2019root; @touvron2023llama].

### Residual connections

By 2015 the leading image networks had 16 to 30 layers, but adding more made things worse. He and colleagues found that a plain 56-layer network had *higher training error* than a 20-layer one on the CIFAR-10 image dataset, and on ImageNet a plain 34-layer network did worse than an 18-layer one (Figure 2.4b). Since the deeper network could in principle copy the shallower one and set its extra layers to pass their input through unchanged, the failure was one of optimisation, not capacity or overfitting. They called it the **degradation problem** [@he2016deep].

![Figure 2.4: Residual connections. (a) A residual block: the input *x* passes through two weight layers to give *F*(*x*), and a shortcut adds the unchanged input back, so the block outputs *F*(*x*) + *x*. (b) Top-1 error on the ImageNet validation set: a plain 34-layer network does worse than a plain 18-layer one (28.54% against 27.94%), while with residual connections the deeper network does better (25.03% against 27.88%). Source: @he2016deep.](../figures/svg/fig-02-04.svg){#fig:02-04}

Their remedy was the **residual connection**. Instead of asking a block of layers to learn a desired mapping *H*(*x*) directly, the block learns the difference *F*(*x*) = *H*(*x*) − *x* and adds its input back, outputting *F*(*x*) + *x*. If the best thing a block can do is nothing, it only has to drive its weights towards zero. The shortcut also helps the backward pass. The slope of *x* + *F*(*x*) with respect to *x* is 1 plus the slope of *F*, so the shortcut gives the gradient an identity path: the error signal arriving at a block's output is passed to its input as it is, with the contribution through *F* added on top. (In the original ResNet a ReLU follows the addition, so the path is exact only where that unit is active [@he2016deep].) Skip connections of this kind shorten the path from early parameters to the output and so mitigate vanishing gradients [@goodfellow2016deep, sec. 8.7.5].

On ImageNet, the residual 34-layer network beat the residual 18-layer one, reversing the plain-network result. A 152-layer residual network, eight times deeper than the earlier VGG networks yet cheaper to run, helped an ensemble reach 3.57% top-5 error and win the 2015 competition. A 1,202-layer network on CIFAR-10 showed "no optimization difficulty", reaching training error below 0.1%. Its test error of 7.93% was nonetheless worse than the 6.43% of a 110-layer network, which the authors attributed to overfitting [@he2016deep]. Every transformer block uses residual connections around both of its sub-layers [@vaswani2017attention].

| | AlexNet (2012) | ResNet (2015) | Transformer (2017) |
|---|---|---|---|
| Optimiser | SGD, momentum 0.9 | SGD, momentum 0.9 | Adam (*β*₁ 0.9, *β*₂ 0.98) |
| Batch size | 128 images | 256 images | about 25,000 source and 25,000 target tokens |
| Learning-rate schedule | 0.01, divided by 10 three times when validation error stalled | 0.1, divided by 10 when error plateaued | linear warm-up over 4,000 steps, then inverse-square-root decay |
| Weight decay | 0.0005 | 0.0001 | not reported |
| Other regularisation | dropout 0.5; crops, reflections, colour shifts | no dropout; scale, crop, flip and colour augmentation | dropout 0.1; label smoothing 0.1 |
| Normalisation | local response normalisation after two layers | batch normalisation after each convolution | layer normalisation |
| Initialisation | Gaussian, standard deviation 0.01 | He initialisation | not reported |

: Table 2.4: The training recipes of three landmark networks. The arithmetic of learning stayed the same; the surrounding choices changed. Source: [@krizhevsky2012imagenet; @he2016deep; @vaswani2017attention].

## 2.6 Convolutional networks, representations and hardware

Images strain fully connected layers. A photograph of 1,000 × 1,000 pixels has a million input values, so a single fully connected layer of a thousand neurons would need a billion weights. A cat in the top-left corner and a cat in the bottom-right would also have to be learned separately, by different weights. **Convolutional neural networks** (CNNs) avoid both problems. LeCun, Bengio and Hinton list their four key ideas as local connections, shared weights, pooling and the use of many layers [@lecun2015deep, p. 439].

### Convolution worked through

A convolutional layer slides a small grid of weights, a **kernel** or **filter**, across the image. At each position it multiplies the kernel's weights by the pixels underneath, adds the products, and writes the total into an output grid called a **feature map**. Figure 2.5 works through a 5 × 5 image whose left three columns are dark (0) and right two columns bright (1), with a 3 × 3 kernel whose columns are −1, 0 and +1. Over the dark region the window sees only zeros and outputs 0; where it straddles the boundary, its +1 column covers three bright pixels and it outputs 3. The kernel detects a vertical edge wherever one appears.

![Figure 2.5: A convolution worked through. (a) A 5 × 5 image with a vertical boundary between dark pixels (0) and bright pixels (1), and a 3 × 3 vertical-edge kernel. (b) At each of nine positions the kernel's weights are multiplied by the pixels beneath and added; the highlighted window, straddling the boundary, gives (−1 × 0 × 3) + (0 × 0 × 3) + (+1 × 1 × 3) = 3. (c) The resulting 3 × 3 feature map: 0 where there is no edge, 3 where there is one. (d) 2 × 2 max pooling keeps the largest value in each block, shrinking a 4 × 4 map to 2 × 2. The same nine weights are used at every position. Calculation by the author.](../figures/svg/fig-02-05.svg){#fig:02-05}

The kernel's nine weights (plus a bias) are reused at every position, and at realistic sizes the saving is vast. A convolutional layer with 64 kernels of 3 × 3 pixels over a 224 × 224 colour image (three channels) has 3 × 3 × 3 × 64 = 1,728 weights plus 64 biases. A fully connected layer producing the same 224 × 224 × 64 outputs would need about 4.8 × 10^11^ weights. Goodfellow and colleagues name three properties behind the saving: **sparse interactions** (each output depends on a small patch), **parameter sharing** (the same kernel everywhere) and **equivariance** (shift the input and the feature map shifts with it) [@goodfellow2016deep, sec. 9.2]. In LeNet-5, weight sharing meant 345,308 connections needed only 60,000 trainable parameters [@lecun1998gradient]. Nobody chooses the kernels. They are weights like any other, set by backpropagation: AlexNet's first layer learned 96 kernels of 11 × 11 × 3 [@krizhevsky2012imagenet], which its authors describe as "frequency- and orientation-selective kernels" together with coloured blobs.

**Pooling** summarises neighbouring outputs, most often by taking the maximum of each 2 × 2 block (Figure 2.5d). This halves each dimension and makes the network less sensitive to small shifts. The design drew on Hubel and Wiesel's studies of simple and complex cells in the cat's visual cortex [@hubel1962receptive] and on Kunihiko Fukushima's 1980 "neocognitron" [@fukushima1980neocognitron; @lecun2015deep, p. 439].

### What the layers learn

Before deep learning, recognising objects required experts to design **features** by hand, such as detectors for edges, corners or textures, which were then fed to a simpler classifier. The 2015 review describes what a deep image network learns instead. The first layer detects edges at particular orientations and positions, the second detects motifs (arrangements of edges), the third assembles motifs into parts of objects, and later layers detect objects as combinations of parts. "These layers of features are not designed by human engineers: they are learned from data" [@lecun2015deep, p. 436]. This is **representation learning**. Matthew Zeiler and Rob Fergus visualised what units in a trained network respond to. Their visualisations showed roughly this progression, from corners and textures in the second and third layers to dog faces and keyboards in the fourth and fifth [@zeiler2014visualizing]. The picture is tidier than reality: Szegedy and colleagues found that meaning is often spread across many units at once instead of sitting in single ones [@szegedy2014intriguing].

### Why matrix multiplication and GPUs matter

Convolutions, fully connected layers and the attention layers of transformers all reduce to multiplying matrices. Multiplying an *m* × *n* matrix by an *n* × *k* matrix takes *m* × *n* × *k* multiplications and about as many additions. A single layer with 4,096 inputs and 4,096 outputs, applied to a batch of 1,024 examples, therefore needs about 2 × 1,024 × 4,096 × 4,096 ≈ 3.4 × 10^10^ operations in the forward pass alone. The operations are independent of one another and can run simultaneously. Matrix multiplication also reuses its data heavily: multiplying two 4,096 × 4,096 matrices performs about 2 × 4,096³ operations on 3 × 4,096² numbers, so each number fetched from memory is used about 2,700 times.

**Graphics processing units** (GPUs) were built to compute millions of pixel colours in parallel with simple, repetitive arithmetic, which turned out to suit neural networks [@goodfellow2016deep, sec. 12.1.2]. AlexNet trained in five to six days on two consumer gaming GPUs, and its authors wrote that their results could be improved "simply by waiting for faster GPUs and bigger datasets to become available" [@krizhevsky2012imagenet, p. 1098].

Modern data-centre GPUs add dedicated matrix units. For Nvidia's H100 (SXM version), the company lists 67 teraFLOPS (trillion operations per second) for ordinary 32-bit arithmetic but 1,979 teraFLOPS for 16-bit matrix arithmetic on its "Tensor Cores" (a figure quoted "with sparsity": it assumes matrices in which structured zeros can be skipped, and ordinary dense matrices run at half that rate), with memory bandwidth of 3.35 terabytes per second [@nvidia2026h100; @andersch2022nvidia]. On the headline sparse figure the chip can perform about 590 operations for every byte it reads from memory, and about 300 on dense matrices. Only computations that reuse each number hundreds of times, which in practice means large matrix multiplications, can keep it busy. Element-by-element steps such as applying ReLU are limited by memory instead. This arithmetic explains why network designs favour large matrix products and why the chip industry described in Chapter 7 grew around them.

The fastest rates apply to short number formats, so training is arranged around them. In **mixed-precision training**, weights, activations and gradients are stored in 16-bit formats while a 32-bit master copy of the weights accumulates the updates [@micikevicius2017mixed]; DeepSeek-V3 performed much of its arithmetic in 8 bits [@deepseekai2024deepseekv3]. The H100's successor, Nvidia's Blackwell generation (B200 and the 72-GPU GB200 NVL72 system), announced in March 2024, adds 4-bit arithmetic for running trained models [@nvidia2024blackwell]. Chapter 7 describes the formats and compares the chips.

## 2.7 Generalisation and regularisation

A network that merely reproduced its training answers would be useless. What matters is performance on cases it has not seen, its **generalisation**, which is what separates machine learning from pure optimisation [@goodfellow2016deep, sec. 5.2]. Available data are therefore split. The **training set** adjusts the weights. The **validation set** compares design choices and decides when to stop. The **test set** is held back and used once, at the end, to estimate real-world performance. Choices made by looking at test results leak information into the system, and the test score then overstates future performance.

::: {.box .concept}
**Concept: Parameters and hyperparameters**

**Parameters** are the weights and biases that training adjusts. **Hyperparameters** are the settings people choose around training, which the learning algorithm does not adjust itself [@goodfellow2016deep, sec. 5.3]: the number and width of layers, the learning rate and its schedule, the batch size, momentum and Adam's *β* values, the weight-decay and dropout rates, the number of epochs. Table 2.4 is, in effect, a list of hyperparameters.
:::

**Overfitting** occurs when a network fits its training data closely but performs worse on new data, because it has learned accidental quirks of the training examples along with the genuine patterns. Figure 2.6(a) shows the classic signature: as training continues, training error keeps falling while validation error falls, levels off and starts to rise. Even well-regularised networks show a gap: LeNet-5 reached 0.35% error on its training digits and 0.95% on the test digits [@lecun1998gradient].

![Figure 2.6: Two views of generalisation. (a) The classic overfitting curve over training time: training error (solid line) keeps falling, while validation error (dashed line) falls, reaches a minimum and rises; early stopping halts training near the minimum. (b) Double descent over model size: test error first follows the classical U-shape, peaks near the size at which the model can just fit every training example exactly (the interpolation threshold), then falls again as the model grows further. Schematic, not to scale; panel (b) after @belkin2019reconciling and @nakkiran2021deep.](../figures/svg/fig-02-06.svg){#fig:02-06}

### The regularisation toolkit

Techniques that reduce overfitting are called **regularisation**.

**Weight decay** adds a penalty ½*λ*‖*w*‖² (half a coefficient *λ* times the sum of squared weights) to the loss [@goodfellow2016deep, sec. 7.1.1]. Its gradient is *λw*, so each step shrinks every weight by a factor (1 − *ηλ*) before the ordinary update. Weights that the data do not actively support decay towards zero. AlexNet used *λ* = 0.0005, and its authors found that this small amount was "important for the model to learn", since it also reduced training error, it was "not merely a regularizer" [@krizhevsky2012imagenet].

**Dropout**, introduced by Geoffrey Hinton's group in Toronto, randomly removes units during training, each kept with probability *p*. The authors suggest 0.5 for hidden units and 0.8 for inputs [@srivastava2014dropout]. Each training step thus trains one of 2^*n*^ possible "thinned" networks that share weights, where *n* is the number of units, and no unit can rely on particular partners being present. At test time all units are used with weights scaled down, approximating an average over the thinned networks. Software usually does the equivalent during training instead, scaling up the surviving units' outputs by 1/*p* so that nothing needs to change at test time (often called inverted dropout) [@goodfellow2016deep, sec. 7.12]. On the MNIST handwritten-digit benchmark, the best standard networks without dropout had reached 1.60% error; dropout networks with ReLUs reached 1.25%, and 1.06% with an added limit on weight size [@srivastava2014dropout]. AlexNet applied dropout to its two fully connected layers and reported "substantial overfitting" without it [@krizhevsky2012imagenet]. Large language models may do without it: PaLM was pre-trained with no dropout, although dropout of 0.1 was used in most fine-tuning [@chowdhery2023palm].

**Data augmentation** creates new training examples by transforming existing ones in ways that do not change the label. "The best way to make a machine learning model generalize better is to train it on more data" [@goodfellow2016deep, sec. 7.4], and augmentation is the cheapest way to get more. AlexNet trained on random 224 × 224 crops of its 256 × 256 images and their mirror images, which increased the effective training set by a factor of 2,048 (though the new examples are highly interdependent). It also randomly altered colour intensities. Without the crops and reflections, the authors wrote, the network "suffers from substantial overfitting" [@krizhevsky2012imagenet].

**Early stopping** halts training when validation error stops improving and keeps the best weights seen so far. Goodfellow and colleagues call it "probably the most commonly used form of regularization in deep learning" [@goodfellow2016deep, sec. 7.8].

### Why do huge networks generalise at all?

Classical learning theory predicts that a model with far more parameters than training examples will memorise its data and generalise badly. Deep networks routinely violate that expectation, and a 2017 study by Chiyuan Zhang and colleagues showed how sharply. Standard image networks trained on CIFAR-10 (50,000 training images in 10 classes) reached 100% training accuracy, or very nearly, even when every label was replaced by a random one, and even when the images were replaced by random noise [@zhang2017understanding]. The same networks, trained on the true labels, generalised well, and removing explicit regularisation cost only a few percentage points (Table 2.5).

| Network (CIFAR-10) | Random-crop augmentation | Weight decay | Training accuracy | Test accuracy |
|---|---|---|---|---|
| Inception (small), 1.65 million parameters | yes | yes | 100.0% | 89.05% |
| Inception (small) | no | no | 100.0% | 85.75% |
| Inception (small), random labels | no | no | 100.0% | 9.78% |
| AlexNet (small), 1.39 million parameters | yes | yes | 99.90% | 81.22% |
| AlexNet (small) | no | no | 100.0% | 76.07% |
| AlexNet (small), random labels | no | no | 99.82% | 9.86% |

: Table 2.5: The same networks memorise random labels perfectly yet generalise well on true labels, with or without explicit regularisation. With ten classes, 10% is chance. Source: [@zhang2017understanding].

The authors concluded that explicit regularisation "may improve generalization performance, but is neither necessary nor by itself sufficient" [@zhang2017understanding]. Whatever makes these networks generalise must lie partly in the architecture, the data and the training procedure itself. They pointed to the training algorithm as one candidate: for linear models, SGD always converges to a solution of small norm (small weights overall), so the algorithm itself acts as an implicit regulariser [@zhang2017understanding]. Mikhail Belkin and colleagues then documented **double descent** [@belkin2019reconciling]. As model size increases, test error first follows the classical U-shape, rising towards the **interpolation threshold**, the size at which the model can just fit every training example exactly. Beyond that threshold, test error falls again, often below the classical optimum (Figure 2.6b). Preetum Nakkiran and colleagues found the same pattern in deep networks, including ResNets and transformers, both as models grew and as training ran longer. It was strongest when part of the training labels were wrong (for instance 15% randomly changed). In certain regimes, even quadrupling the amount of training data made test error worse [@nakkiran2021deep]. A complete theory of why overparameterised networks generalise does not yet exist.

## 2.8 How networks fail, and the brain analogy

Gradient descent finds whatever weights reduce the training loss. It has no notion of the reason a human would give for an answer. Several well-documented failures follow from that indifference.

### Shortcut learning

Robert Geirhos and colleagues define **shortcuts** as "decision rules that perform well on standard benchmarks but fail to transfer to more challenging testing conditions" [@geirhos2020shortcut, p. 665]. One example they review is a network that recognises cows on grassland but fails on a cow standing on a beach, because grass was the more reliable signal in its training data [@geirhos2020shortcut]. A second study by Geirhos's group tested image networks on pictures in which shape and texture conflict, such as a cat's outline filled with elephant skin. Human observers chose the shape category in 95.9% of their correct decisions. ImageNet-trained networks mostly chose the texture: ResNet-50 chose the shape in only 22.1% of cases, and it labelled the cat-shaped elephant-skin image "Indian elephant" with 63.9% confidence [@geirhos2019imagenettrained]. Retraining the same architecture on stylised images, in which texture no longer predicts the label, shifted it towards shape.

::: {.box .case}
**Case study: The pneumonia detector that recognised hospitals**

In 2018 John Zech and colleagues trained convolutional networks to detect pneumonia on 158,323 chest X-rays from three US hospital systems [@zech2018variable]. Performance was measured by the **AUC** (area under the receiver operating characteristic curve): the probability that a model scores a randomly chosen positive case above a randomly chosen negative one, so that 0.5 is chance and 1.0 perfect [@hanley1982meaning]. Pneumonia was far more common at one site: 34.2% of radiographs at Mount Sinai Hospital, against 1.2% at the National Institutes of Health (NIH) Clinical Center and 1.0% at Indiana University. Sorting X-rays by hospital system alone, without looking at the lungs, achieved an AUC of 0.861 on the combined Mount Sinai and NIH data. The networks identified which system an NIH or Mount Sinai X-ray came from with 99.95% and 99.98% accuracy. A model trained on pooled data from two sites scored an AUC of 0.931 on held-out images from those sites but 0.815 on the third, unseen hospital. The authors concluded that the networks' ability to recognise the hospital and department "may confound predictions". The training loss could be reduced by learning where an image came from, and gradient descent duly learned it.
:::

### Distribution shift

The pneumonia case is also an instance of **distribution shift**: the data a system meets in use differ from the data it was tested on. Benjamin Recht and colleagues rebuilt the test sets of two of the most heavily used benchmarks, CIFAR-10 and ImageNet, following the original collection procedures as closely as they could. A broad range of published models lost 3 to 15 percentage points of accuracy on the new CIFAR-10 test set and 11 to 14 points on the new ImageNet one. For ImageNet that is roughly five years of progress. The ranking of models was almost unchanged, and every point of improvement on the old test set translated into a larger gain on the new one. The authors therefore attributed the drop to the new images being slightly "harder", not to researchers having overfitted the old test sets through repeated reuse [@recht2019imagenet].

### Adversarial examples

Christian Szegedy and colleagues showed in 2014 that an "imperceptible non-random perturbation" can cause an image network to misclassify an image [@szegedy2014intriguing]. In the best-known example, Ian Goodfellow, Jonathon Shlens and Szegedy took a photograph that GoogLeNet classified as a panda with 57.7% confidence. They added a pattern in which each pixel moved by 0.007, up or down according to the sign of the loss gradient, so as to increase the loss; the authors note that 0.007 corresponds to the smallest step of an 8-bit image encoding after GoogLeNet's conversion to real numbers. The network then said "gibbon" with 99.3% confidence [@goodfellow2015explaining, fig. 1]. Their explanation is that networks behave largely linearly. If a perturbation of size *ε* is aligned with the weights of a unit with *n* inputs whose weights average *m* in magnitude, the unit's total changes by about *ε* × *m* × *n*. For a 224 × 224 colour image, *n* is 150,528. With *ε* = 0.007 and an illustrative average weight of 0.01, the change is about 10.5, enough to swamp a decision, although no single pixel changed visibly. Many tiny changes "add up to one large change to the output" [@goodfellow2015explaining]. A competing account by Andrew Ilyas and colleagues holds that adversarial examples exploit "non-robust features": patterns in the data that genuinely predict the label but are brittle and incomprehensible to humans [@ilyas2019adversarial]. On that view, the network is using real signals that people cannot see. Training on adversarial examples improves robustness: in the 2015 study it cut a digit-recognition network's ordinary test error from 0.94% to 0.84% [@goodfellow2015explaining].

### Forgetting and opacity

A network trained on one task and then on a second tends to overwrite the weights that served the first. James Kirkpatrick and colleagues note that this **catastrophic forgetting** had long been "widely thought" to be "an inevitable feature" of such models, and proposed slowing learning on the weights most important for earlier tasks [@kirkpatrick2017overcoming, p. 3521]. Because what a network "knows" is spread across millions of weights, explaining why it produced a given answer is also hard.

### The biological analogy and its limits

The word "neural" invites the assumption that these systems work like brains. Artificial neurons were inspired by biological ones [@mcculloch1943logical; @rosenblatt1958perceptron], and convolutional networks borrowed from the visual cortex [@lecun2015deep]. A biological neuron, however, is far more complex than a weighted sum followed by a ReLU. David Beniaguev, Idan Segev and Michael London trained artificial networks to reproduce the input–output behaviour of a detailed model of a single cortical neuron and needed a network of five to eight layers to capture it [@beniaguev2021single]. Scale comparisons mislead in a similar way. The adult human brain has about 86 billion neurons [@azevedo2009equal], but a network's parameters correspond loosely to synapses, the connections between neurons, not to neurons. The learning rule differs too. Backpropagation sends precise error signals backwards through the same connections, which Timothy Lillicrap and colleagues note has "historically" been "viewed as biologically problematic" [@lillicrap2020backpropagation, p. 335].

::: {.box .debate}
**Debate: Are artificial neural networks good models of the brain?**

*For.* Daniel Yamins and colleagues trained image networks only to recognise objects, with no brain data. The networks' top layers predicted the responses of neurons in the monkey's inferior temporal cortex, a high-level visual area, and their intermediate layers predicted responses in the mid-level area V4 [@yamins2014performance]. Lillicrap and colleagues argue that the brain's abundant feedback connections could approximate the error signals of backpropagation [@lillicrap2020backpropagation].

*Against.* Single cortical neurons compute functions that need a multi-layer artificial network to reproduce [@beniaguev2021single]. Lillicrap and colleagues themselves acknowledge that it is hard to see how feedback connections could deliver the precise, weight-specific signals strict backpropagation requires [@lillicrap2020backpropagation]. Networks also show failures, such as adversarial examples and a preference for texture over shape, that do not resemble human perception [@goodfellow2015explaining; @geirhos2019imagenettrained].

Settling the question needs direct measurements of whether learning signals in cortex track the gradients backpropagation would compute, and tests of whether the networks that best predict neural responses also share human robustness to adversarial and shape–texture manipulations.
:::

These failures come from the same loop that makes networks work. Gradient descent reduces whatever loss it is given on whatever data it is given, and the hospital marker and the elephant-skin texture were real regularities of the training images. Initialisation, normalisation, residual connections and adaptive optimisers made that loop reliable at depths Rosenblatt could not have attempted, but none of them changes what the loss rewards. Regularisation narrows the gap to held-out data, not to data collected differently, as the rebuilt ImageNet test sets showed. What a network has actually learned can therefore be established only by testing it on cases unlike those it was trained on, or by reading it from the weights, the aim of interpretability research (Chapter 12).

## Further reading

- Goodfellow, I., Bengio, Y. and Courville, A. (2016). *Deep Learning*. The standard graduate text, free online; chapters 6–9 give the full mathematics behind every topic here, from backpropagation to convolutions and optimisers. [@goodfellow2016deep]
- LeCun, Y., Bengio, Y. and Hinton, G. (2015). *Deep learning*. A nine-page *Nature* review by three pioneers that explains representation learning, convolutional networks and backpropagation with compact diagrams. [@lecun2015deep]
- Nielsen, M. A. (2015). *Neural Networks and Deep Learning*. A free online book that builds a digit-recognising network in code, with interactive demonstrations of gradient descent, backpropagation and vanishing gradients. [@nielsen2015neural]
- He, K. et al. (2016). *Deep residual learning for image recognition*. A short, clearly argued paper whose experiments on the degradation problem show how a small architectural change made very deep networks trainable. [@he2016deep]
- Geirhos, R. et al. (2020). *Shortcut learning in deep neural networks*. A readable perspective that connects many documented failures of deep learning to a single cause, with practical advice on how to test for it. [@geirhos2020shortcut]


# Chapter 3: How Large Language Models Work

In May 2020 a team at OpenAI described GPT-3, a neural network with 175 billion parameters [@brown2020language]. It had been trained on one narrow task: guessing the next piece of text in a very large collection of web pages, books and Wikipedia articles. Nobody had trained it to translate, answer questions or do sums. Yet when the researchers typed a few worked examples into the model, it carried on the pattern and performed tasks such as translation, question answering and three-digit arithmetic. The paper stressed that it did this "without any gradient updates or fine-tuning", meaning that the network's weights were not changed for the new task.

How a system trained only to continue text ends up writing essays and explaining code, and why the same system sometimes invents facts with complete confidence, both follow from its mechanism. Text is cut into tokens, tokens become vectors, attention mixes information between positions, a stack of transformer blocks refines the result, and a probability distribution over the next token comes out at the top. The numbers below are real where possible, computed by the author with openly available models and software, with the settings stated. Chapter 2 supplies the background on loss functions, backpropagation, residual connections and layer normalisation; Chapter 4 covers scaling laws and compute.

## 3.1 Tokens: from text to numbers

A neural network can only do arithmetic, so a language model first splits text into **tokens**: frequently occurring chunks of characters, each with a fixed identification number. A token may be a whole common word, a fragment of a longer word, or a single character, byte or punctuation mark. The list of all tokens a model knows is its **vocabulary**, and the program that does the splitting is its **tokeniser**.

Table 3.1 shows a real example. The sentence "Students in Edinburgh rarely misunderstand tokenisation." was passed through `o200k_base`, the tokeniser that OpenAI's open-source `tiktoken` library assigns to GPT-4o and to later models including o3, GPT-4.1 and GPT-5 [@openai2026tiktoken]. Six words become eight tokens. Common words such as "Students" and "rarely" survive whole, and even "misunderstand" has its own token. The less common "tokenisation", with its British spelling, is split into " token" and "isation". Most tokens carry their leading space with them, so " in" (with a space) and "in" (without) are different tokens with different numbers.

| Position | Token | ID in `o200k_base` |
|---|---|---|
| 1 | "Students" | 36954 |
| 2 | " in" | 306 |
| 3 | " Edinburgh" | 61877 |
| 4 | " rarely" | 32208 |
| 5 | " misunderstand" | 169786 |
| 6 | " token" | 6602 |
| 7 | "isation" | 6993 |
| 8 | "." | 13 |

: Table 3.1: A real tokenisation. The sentence "Students in Edinburgh rarely misunderstand tokenisation." becomes eight tokens in the `o200k_base` tokeniser used for GPT-4o, because "tokenisation" is split into two. Quotation marks show where a token includes a leading space. Computed by the author with tiktoken 0.14.0 on 22 October 2026. Source: @openai2026tiktoken.

### Byte-pair encoding, step by step

Most current tokenisers build their vocabulary with **byte-pair encoding** (BPE). The method began as a data-compression technique that repeatedly replaced the most frequent pair of bytes with a new, unused byte; @sennrich2016neural adapted it for machine translation in 2016. Their version starts with a vocabulary of single characters and represents every word in a training text as a sequence of characters plus an end-of-word marker. It then counts every adjacent pair of symbols, weighted by how often each word occurs, merges the most frequent pair into a new symbol, and repeats. The number of merges is the only setting: the final vocabulary is the starting characters plus one new symbol per merge.

The paper prints a short Python implementation with a toy dictionary: "low" occurring 5 times, "lower" 2, "newest" 6 and "widest" 3. Running that code gives the merges in Table 3.2. The pair "e s" appears 9 times (6 in "newest", 3 in "widest") and is merged first; "es t" and "est" plus the end marker follow, also at 9. Then "l o" and "lo w" (7 each, from "low" and "lower") are merged, and so on. After ten merges, "newest" and "low" are single symbols, while the rarer "lower" is still spelled "low", "e", "r". That is the essential behaviour of BPE: frequent strings become single tokens, rare ones remain decomposable into known parts, and no word made of characters seen in training is ever "unknown".

| Merge | Pair merged | Count | "newest" after merge | "lower" after merge |
|---|---|---|---|---|
| 1 | e + s | 9 | n e w es t · | l o w e r · |
| 2 | es + t | 9 | n e w est · | l o w e r · |
| 3 | est + · | 9 | n e w est· | l o w e r · |
| 4 | l + o | 7 | n e w est· | lo w e r · |
| 5 | lo + w | 7 | n e w est· | low e r · |
| 6 | n + e | 6 | ne w est· | low e r · |
| 7 | ne + w | 6 | new est· | low e r · |
| 8 | new + est· | 6 | newest· | low e r · |
| 9 | low + · | 5 | newest· | low e r · |
| 10 | w + i | 3 | newest· | low e r · |

: Table 3.2: Byte-pair encoding on the toy dictionary of @sennrich2016neural ("low" ×5, "lower" ×2, "newest" ×6, "widest" ×3). Each step merges the most frequent adjacent pair; "·" marks the end of a word. Where counts tie, the code takes the pair it encountered first. Computed by the author by running the paper's Algorithm 1 in Python 3. Source: @sennrich2016neural.

In their English–German experiments Sennrich and colleagues used 59,500 merges for each language, or 89,500 for a single vocabulary shared by both. GPT-2 introduced a byte-level variant in which the starting symbols are the 256 possible bytes rather than the characters of an alphabet [@radford2019language]. Because any text in any script is a sequence of bytes, a byte-level tokeniser "can assign a probability to any Unicode string" and works "on arbitrary text, even text that is not in the tokeniser's training data" [@radford2019language; @openai2026tiktoken]. An emoji that never appeared in training is simply spelled out byte by byte: the parrot emoji, four bytes in the standard UTF-8 encoding, becomes three tokens in both the GPT-2 and `o200k_base` tokenisers (author computation, tiktoken 0.14.0).

Vocabulary size is a trade-off: a larger vocabulary makes text shorter in tokens but enlarges the embedding table and spreads training data over more rare tokens. Table 3.3 shows how vocabularies have grown. Meta's Llama 3 tokeniser combines 100,000 tokens from OpenAI's `tiktoken` with 28,000 extra tokens for non-English languages. Compared with Llama 2's, it raised compression on English text from 3.17 to 3.94 characters per token, letting the model "read" more text for the same training compute [@grattafiori2024llama].

| Tokeniser (models) | Vocabulary size |
|---|---|
| GPT-2 (`gpt2`) | 50,257 |
| `cl100k_base` (GPT-4) | 100,277 |
| Llama 3 | 128,000 |
| Qwen2.5 | 151,665 |
| `o200k_base` (GPT-4o, o3, GPT-5) | 200,019 |

: Table 3.3: Vocabulary sizes of selected tokenisers. Values for OpenAI tokenisers are `n_vocab` in tiktoken 0.14.0; Qwen2.5 is the length of the Hugging Face tokeniser for Qwen/Qwen2.5-1.5B (its output layer is padded to 151,936 rows); Llama 3 is as reported by Meta. Computed by the author, October 2026. Source: @openai2026tiktoken; @grattafiori2024llama; @qwen2024qwen25.

### What tokenisation costs

With a leading space, " strawberry" is a single token in `o200k_base`; without one, "strawberry" becomes "st", "raw" and "berry". Either way the model never sees ten separate letters, which is one reason questions about spelling and letter counts are harder for it than they look. Numbers are cut into chunks of up to three digits: " 12345678" becomes a space token followed by "123", "456" and "78". The digit that carries a given place value lands in different positions depending on the length of the number (author computation, tiktoken 0.14.0).

Tokenisation also treats languages unequally. Table 3.4 shows the sentence "I love learning about language models." and close translations. In `o200k_base` the English version needs 7 tokens, German 9, Hindi 12 and Swahili 13; in the older GPT-2 tokeniser the Hindi version needs 62, because that vocabulary has few merges for Devanagari, whose characters each take three bytes. Across a parallel corpus in many languages, @petrov2023language found that the same text could differ in tokenised length by up to 15 times. Since services charge per token and context windows are counted in tokens, speakers of under-represented languages pay more and fit less into each request. The newer vocabulary narrows the gap considerably but does not close it.

| Language | `o200k_base` tokens (2024) | GPT-2 tokens (2019) |
|---|---|---|
| English | 7 | 7 |
| German | 9 | 15 |
| Hindi | 12 | 62 |
| Swahili | 13 | 20 |

: Table 3.4: The same short sentence costs different numbers of tokens in different languages. Texts: "I love learning about language models." and close translations, in German "Ich lerne gern über Sprachmodelle.", in Swahili "Ninapenda kujifunza kuhusu mifano ya lugha." and in Hindi (Devanagari script). Counts computed by the author as for Table 3.1 (encodings `o200k_base` and `gpt2`). Source: @openai2026tiktoken; @petrov2023language.

::: {.box .concept}
**Concept: Token**

A token is the basic unit a language model reads and writes: usually a word, part of a word, a punctuation mark or a raw byte, each mapped to a fixed number. Meta's Llama 3 tokeniser averages 3.94 characters of English text per token [@grattafiori2024llama]. Prices, speed limits, memory use and context windows are all counted in tokens, which is why the same request can cost different amounts in different languages.
:::

## 3.2 Embeddings and self-attention

A token number on its own carries no meaning. The number 9059 (" cat" in `o200k_base`) is not "closer" to a dog than 9060 is. So each token is converted into an **embedding**: a **vector**, that is, an ordered list of numbers, which places the token as a point in a high-dimensional space. The model holds an embedding table with one row per vocabulary entry and simply looks up the row for each token. In the smallest GPT-2 model each row has 768 numbers; in the largest Llama 3 model it has 16,384 [@radford2019language; @grattafiori2024llama]. The numbers start random and are adjusted by gradient descent during training, like any other weight.

The word2vec models, trained on 1.6 billion words and described in a preprint by @mikolov2013efficient, placed words used in similar contexts near one another. Directions in the space also captured relationships: @mikolov2013linguistic reported that the calculation "King − Man + Woman" produced a vector very close to the one for "Queen". Figure 3.1 sketches the idea in two dimensions.

![Figure 3.1: An embedding space, sketched in two dimensions. Words used in similar ways sit close together, and some relationships (such as male to female, or country to capital) appear as roughly parallel arrows. Real embeddings have hundreds or thousands of dimensions. Schematic, not to scale. Source: illustrating findings of @mikolov2013linguistic and @mikolov2013efficient.](../figures/svg/fig-03-01.svg){#fig:03-01}

The picture misleads in one important respect. Word2vec gave each word a single fixed point, so "bank" had the same embedding whether it meant a riverbank or a lender. In a language model the embedding table is only the starting point. As a token passes up through the network, its vector is repeatedly updated with information from the surrounding tokens, so that by the upper layers "bank" in "the river bank" and "bank" in "the bank raised rates" are represented quite differently. The mechanism that moves information between positions is attention.

Embeddings need not come from words. @dosovitskiy2021image showed that an image can be cut into small square patches, each turned into a vector and processed like a token, and @radford2021learning trained CLIP on 400 million image–caption pairs to place pictures and text in a shared embedding space. Multimodal models such as Gemini 1.5, which Google reported could reason over hours of video and audio, put images, audio and video into the same sequence as text [@geminiteam2024gemini].

### Queries, keys and values

In "The Law will never be perfect, but its application should be just", the word "its" refers back to "Law", several words earlier. Before 2017 most language models were recurrent networks that passed a running summary from word to word, so information from far back faded and each step waited for the previous one. The **transformer** of @vaswani2017attention dispensed "with recurrence and convolutions entirely" and relied on **self-attention**, in which every position can draw directly on every other.

Attention works with three vectors per token, each computed by multiplying the token's current vector by a learned weight matrix. The **query** *q* expresses what the token is looking for; the **key** *k* advertises what a token contains; the **value** *v* is the information it passes on if selected. How well a query matches a key is measured by their **dot product**: multiply the two vectors number by number and add up the results, which gives a large number when both have large values in the same places. For all tokens at once, the computation is

Attention(*Q*, *K*, *V*) = softmax(*QK*^T^ / √*d*~k~) *V*

where *Q*, *K* and *V* stack the queries, keys and values of all tokens as rows, *QK*^T^ is the table of every query–key dot product, and *d*~k~ is the length of the key vectors [@vaswani2017attention]. The **softmax** function (Section 2.3) turns each row of scores into weights that are positive and sum to one, by exponentiating every score and dividing by the total. Each token's output is then the weighted average of all the value vectors. The division by √*d*~k~ matters: with long vectors the dot products grow large, which pushes the softmax towards giving almost all weight to one token, a region where, in the authors' words, it has "extremely small gradients" and learning stalls.

A language model adds a **causal mask**. When predicting the next token it must not peek at the answer, so each token may attend only to itself and earlier tokens. The mask sets the scores for all later positions to minus infinity before the softmax, which makes their weights exactly zero. Because nothing in the computation runs step by step, all positions of a training passage are processed at once on parallel hardware, which is what made training on trillions of tokens feasible.

### A worked example

Table 3.5 runs the formula on three tokens with two-dimensional vectors, small enough to check by hand. Take the third token, whose query is *q*~3~ = (2, 1). Its dot products with the three keys are 4, 1 and 3, and dividing by √2 ≈ 1.414 gives 2.83, 0.71 and 2.12. The softmax (exponentiate each, then divide by their sum, 27.29) turns these into the weights 0.620, 0.074 and 0.306. Mixing the three value vectors in those proportions gives the output (0.773, 0.227). The third token has drawn mostly on the first, whose key best matches its query, a little on itself and hardly at all on the second.

| | Query | Key | Value | Weights on tokens 1, 2, 3 | Output |
|---|---|---|---|---|---|
| Token 1 | (1, 0) | (2, 0) | (1, 0) | 1.000, 0, 0 | (1.000, 0.000) |
| Token 2 | (0, 1) | (0, 1) | (0, 1) | 0.330, 0.670, 0 | (0.330, 0.670) |
| Token 3 | (2, 1) | (1, 1) | (0.5, 0.5) | 0.620, 0.074, 0.306 | (0.773, 0.227) |

: Table 3.5: Masked self-attention on three tokens with two-dimensional query, key and value vectors (invented for illustration). Weights are softmax(*q* · *k* / √2) over the token itself and earlier tokens; later tokens are masked to zero. Each output is the weighted sum of the value vectors. Computed by the author with NumPy. Source: formula from @vaswani2017attention.

The first token can see only itself, so its output is just its own value: the mask at work. In a real model the vectors are longer (64 numbers per head in GPT-2 small), and the matrices that produce queries, keys and values are learned, with no dimension's meaning specified by anyone.

### Many heads

A single attention computation produces one weighted mix per token. Transformers instead run several in parallel, called **attention heads**, each with its own query, key and value matrices operating on a slice of the vector. Multi-head attention, Vaswani and colleagues wrote, "allows the model to jointly attend to information from different representation subspaces at different positions". The original model had 8 heads of 64 dimensions each, and GPT-2 small has 12 (12 × 64 = 768). GPT-3 has 96 heads per layer and Llama 3 405B has 128 [@vaswani2017attention; @brown2020language; @grattafiori2024llama]. The heads' outputs are joined and multiplied by one more learned matrix, the output projection.

Heads do specialise. In the original paper's trained translation model, two heads in the fifth of six layers attended sharply from "its" to "Law" and to "application" in the sentence above. The authors called this behaviour "apparently involved in anaphora resolution", that is, working out what a pronoun refers to [@vaswani2017attention, Figure 4]. @jain2019attention, however, found that attention weights were frequently uncorrelated with other measures of which inputs mattered for a prediction, and concluded that "standard attention modules do not provide meaningful explanations".

## 3.3 The transformer block

Attention is one of two sublayers in a **transformer block**, and a language model is a stack of identical blocks: 12 in GPT-2 small, 96 in GPT-3, 126 in Llama 3 405B (Figure 3.2).

![Figure 3.2: A GPT-style transformer, simplified. Tokens become embeddings plus position information (learned position embeddings, as in GPT-2), and each token's vector then runs up its own residual stream (vertical lines) through many identical blocks. In each block an attention step brings in information from the token itself and earlier tokens only (the causal mask), and a feed-forward step processes each token on its own; both add their results to the stream (⊕) rather than replacing it. Layer normalisation is omitted. The final layer gives a probability for every possible next token; the bars show GPT-2 XL's four most likely next tokens after "The cat sat on the". Inset: two attention heads in layer 5 of a trained translation model attend from "its" to "Law" and "application"; this part of that model is not masked, so it can also look ahead; line weights are qualitative. Diagram by the author, after @vaswani2017attention; probabilities computed by the author with GPT-2 XL [@radford2019language].](../figures/svg/fig-03-02.svg){#fig:03-02}

### The residual stream

Each sublayer does not replace a token's vector; it adds to it. This is the residual connection of Section 2.5, introduced for image networks by @he2016deep. If *x* is a token's vector entering a block, GPT-2 computes *x* + Attention(LayerNorm(*x*)), and then adds the feed-forward sublayer's output to that sum in the same way. Layer normalisation rescales each vector to zero mean and unit variance before applying learned scale and shift parameters. GPT-2 applies it to the input of each sublayer, moving it from the output position used in the original transformer, and adds one more after the final block [@radford2019language].

The result is a single vector per position that runs from the embedding at the bottom to the output layer at the top, with every attention and feed-forward sublayer reading from it and writing back into it. Anthropic researchers call it the **residual stream**, describing it as "a communication channel, since it doesn't do any processing itself and all layers communicate through it" [@elhage2021mathematical]. Information written into the stream by an early layer remains available to every later layer unless something overwrites it.

### The feed-forward network

The second sublayer is a small two-layer network of the kind described in Chapter 2, applied to each position separately: attention moves information between tokens, and the feed-forward network processes what has arrived. In GPT-2 the vector is expanded from 768 to 3,072 numbers, passed through a smooth non-linear activation (GELU, a curved relative of the ReLU of Section 2.1), and projected back to 768. Llama 3 uses a gated variant called SwiGLU, with an inner width of 53,248 for a model dimension of 16,384 [@grattafiori2024llama]. These layers hold most of the parameters. @geva2021transformer showed that feed-forward layers behave like key–value memories: the first matrix detects input patterns, often interpretable ones such as a phrase ending in a particular word, and the second pushes the prediction towards tokens that tend to follow them.

### Counting the parameters of GPT-2 small

Table 3.6 counts every parameter of the smallest GPT-2 model, as released on Hugging Face, and shows where a language model's size comes from. Within each block the feed-forward network holds two-thirds of the parameters, the share @geva2021transformer describe as typical, and attention nearly all the rest. The output layer, which turns the final vector into a score for each of the 50,257 tokens, reuses the token embedding matrix, a saving called weight tying. Even so, nearly a third of this small model sits in the embedding table; in large models the blocks dominate. The approximation of @kaplan2020scaling, 12 × layers × width^2^ for the blocks, comes within 0.15 per cent of their exact total.

| Component | Calculation | Parameters |
|---|---|---|
| Token embeddings | 50,257 × 768 | 38,597,376 |
| Position embeddings | 1,024 × 768 | 786,432 |
| Attention: query, key, value | 768 × 2,304 + 2,304 | 1,771,776 |
| Attention: output projection | 768 × 768 + 768 | 590,592 |
| Feed-forward: expand | 768 × 3,072 + 3,072 | 2,362,368 |
| Feed-forward: project back | 3,072 × 768 + 768 | 2,360,064 |
| Two layer norms | 4 × 768 | 3,072 |
| One block (sum of the five rows above) | | 7,087,872 |
| Twelve blocks | 12 × 7,087,872 | 85,054,464 |
| Final layer norm | 2 × 768 | 1,536 |
| Output layer | shares the token embedding matrix | 0 |
| **Total** | | **124,439,808** |

: Table 3.6: Where the parameters of GPT-2 small sit. Shapes read from the released model (openai-community/gpt2, Hugging Face transformers 5.20.2) and summed by hand; the total matches the library's own count. The GPT-2 paper lists the model as 117 million parameters. Source: @radford2019language.

Size translates directly into computation. A forward pass through the blocks costs about two arithmetic operations (a multiplication and an addition) per parameter for each token, roughly 170 million operations per token for GPT-2 small. The output layer adds more, as does attention over the context, which grows with its length [@kaplan2020scaling]. This 2*N* rule, for a model with *N* parameters, is the starting point for the compute accounting of Chapter 4.

### Position information

Attention by itself ignores order. A token's output is a weighted average over the tokens it can see, with weights set by their content alone, so shuffling those tokens leaves the output unchanged and "dog bites man" would look like "man bites dog". The causal mask only decides which tokens are visible; it does not say where each one sits, and leaks order only indirectly, because later positions see more tokens. Position information is therefore supplied explicitly, by position encodings, and three schemes have dominated. The original transformer added to each embedding a fixed pattern of sine and cosine waves, *PE*~(pos,\ 2*i*)~ = sin(pos / 10000^2*i*/*d*^) for even dimensions and the matching cosine for odd ones. Here pos is the token's position, *d* the length of the embedding vector, and *i* numbers the pairs of dimensions from 0 to *d*/2 − 1. Each pair thus oscillates at its own frequency, with wavelengths forming "a geometric progression from 2π to 10000 · 2π" [@vaswani2017attention]. Nearby positions differ sharply in the fast-oscillating dimensions and hardly at all in the slow ones, like the hands of a clock. GPT-1 and GPT-2 instead learned a separate position embedding for each of their slots, 1,024 in GPT-2, exactly like token embeddings [@radford2018improving; @radford2019language]. A learned table has a hard limit: GPT-2 has no row for position 1,025.

Most recent open models use **rotary position embeddings** (RoPE), which add nothing to the embedding [@su2024roformer]. Inside each attention head, RoPE splits the query and key vectors into pairs of numbers and rotates each pair by an angle proportional to the token's position, with a different rotation speed for each pair. When a rotated query meets a rotated key, the positions enter their dot product only through the difference between the two rotation angles, and so through the distance between the two tokens. In its authors' words, RoPE "encodes the absolute position with a rotation matrix" while making attention depend explicitly on relative position. As with the sinusoids, the rotation speeds form a geometric series. A constant called the base frequency sets how slowly the slowest pairs turn; a larger base keeps their angles from coming full circle over long distances, so far-apart positions remain distinguishable. Meta raised this constant to 500,000 for Llama 3, from Llama 2's setting, to support longer contexts [@grattafiori2024llama].

### Mixture of experts

In a standard ("dense") transformer every parameter is used for every token. A **mixture-of-experts** (MoE) model replaces the single feed-forward network in a block with many alternative ones, the experts, and a small routing network sends each token to only a few of them. @shazeer2017outrageously showed in 2017 that such layers, with up to thousands of experts, could raise model capacity by more than 1,000 times with only minor losses in computational efficiency. Mixtral 8x7B, described in a 2024 preprint, has 8 experts per layer and routes each token to 2, so that each token "has access to 47B parameters, but only uses 13B active parameters" [@jiang2024mixtral]. DeepSeek-V3's technical report describes 256 routed experts plus one shared expert in each MoE layer, with 8 routed experts active for each token, so that each token uses 37 billion of the model's 671 billion parameters [@deepseekai2024deepseekv3].

The design separates how much a model can store (total parameters) from how much computation each token costs (active parameters). The price is memory, since all experts must be held somewhere, and the need to keep the experts evenly loaded. DeepSeek-V3 does this mainly by nudging each expert's routing score up or down according to its load [@deepseekai2024deepseekv3].

## 3.4 Generating text

At the top of the stack, the final vector at the last position is multiplied by the output matrix to give one raw score per vocabulary entry, a **logit**, and a softmax turns the logits into probabilities. The model then picks one token, appends it, and runs again. A model that generates text this way, feeding each output back in as input, is **autoregressive**. Each token is committed once chosen; the model never drafts and revises.

Table 3.7 shows real next-token probabilities after "The capital of France is" from three openly available base models, which have only been pre-trained (Section 3.5). GPT-2 small gives "Paris" only 3.2 per cent and prefers " the". GPT-2 XL, with about 1.5 billion parameters, raises "Paris" to 8.6 per cent [@radford2019language]. Qwen2.5-1.5B, released by Alibaba in 2024 with a similar number of parameters but trained on up to 18 trillion tokens [@qwen2024qwen25], gives "Paris" 27.3 per cent. Even then, most of the probability goes to other continuations: " located", or runs of underscores that hint at fill-in-the-gap exercises in the training data. For a base model, "The capital of France is located on the Seine" is a perfectly good continuation.

| Rank | GPT-2 small (2019) | GPT-2 XL (2019) | Qwen2.5-1.5B (2024) |
|---|---|---|---|
| 1 | " the" 8.5% | " the" 10.1% | " Paris" 27.3% |
| 2 | " now" 4.8% | " a" 9.9% | " located" 6.3% |
| 3 | " a" 4.6% | " Paris" 8.6% | " a" 4.5% |
| 4 | " France" 3.2% | " in" 2.5% | " \_\_" 4.4% |
| 5 | " Paris" 3.2% | " one" 2.4% | " \_\_\_\_\_\_" 4.2% |

: Table 3.7: Next-token probabilities after the prompt "The capital of France is" for three open-weight base models (no post-training). Computed by the author on 22 October 2026 with Hugging Face `transformers` 5.20.2 and PyTorch 2.14.1 (CPU, 32-bit floating point), softmax over the full vocabulary at temperature 1; percentages rounded. Sources of the models: @radford2019language; @qwen2024qwen25.

### Temperature, top-k and top-p

Turning probabilities into a choice, **decoding**, is a procedure separate from the network. Always taking the most likely token ("greedy" decoding), or searching for the most likely sequence as beam search does, leads to what @holtzman2020curious call degeneration: text that is "bland, incoherent, or gets stuck in repetitive loops". Most chat systems therefore sample from the distribution, after reshaping it with temperature, top-k or top-p.

**Temperature** *T* divides every logit before the softmax: *p*~*i*~ = e^*z*~*i*~/*T*^ / Σ~*j*~ e^*z*~*j*~/*T*^. Because the softmax depends only on differences between logits, the ratio between two tokens' probabilities is e raised to their logit difference divided by *T*. GPT-2 XL's logits after "After the lecture, the students went to the" are 8.78 for " cafeteria" and 8.35 for " library", a difference of 0.43. At *T* = 1 the ratio of their probabilities is e^0.43^ ≈ 1.54; at *T* = 0.5 the difference doubles to 0.86 and the ratio becomes e^0.86^ ≈ 2.36 (Table 3.8 gives the probabilities). Lower temperatures sharpen the distribution towards the top token; higher ones flatten it, and as *T* approaches zero sampling becomes greedy decoding.

**Top-k sampling**, used by @fan2018hierarchical for story generation with *k* = 10, discards all but the *k* most likely tokens and renormalises. **Top-p** or **nucleus sampling** keeps the smallest set of tokens whose probabilities add up to at least *p* [@holtzman2020curious]. Holtzman and colleagues proposed it because the shape of the distribution varies: when it is flat, a small *k* cuts off many reasonable options, and when it is peaked, a large *k* lets in implausible ones. Table 3.8 shows how much the nucleus changes size: at temperature 1, covering 90 per cent of the probability takes 3,068 tokens after GPT-2 XL's open-ended lecture prompt but only 103 after Qwen2.5-1.5B's factual one. Halving the temperature shrinks both to a handful.

| | GPT-2 XL: "After the lecture, the students went to the" | | GPT-2 XL: "The cat sat on the" | | Qwen2.5-1.5B: "The capital of France is" | |
|---|---|---|---|---|---|---|
| Temperature | 1.0 | 0.5 | 1.0 | 0.5 | 1.0 | 0.5 |
| Top token | " cafeteria" 7.5% | " cafeteria" 51.7% | " edge" 7.3% | " edge" 30.5% | " Paris" 27.3% | " Paris" 81.6% |
| Second token | " library" 4.9% | " library" 21.9% | " floor" 5.2% | " floor" 15.6% | " located" 6.3% | " located" 4.4% |
| Share of top 5 | 18.9% | 86.5% | 24.4% | 74.4% | 46.8% | 92.2% |
| Tokens in nucleus, *p* = 0.9 | 3,068 | 10 | 951 | 14 | 103 | 4 |

: Table 3.8: Temperature and nucleus size. "Tokens in nucleus" is the number of most likely tokens whose probabilities sum to at least 0.9. Computed by the author, 22–23 October 2026, with the settings of Table 3.7. Source of the models: @radford2019language; @qwen2024qwen25.

After "The cat sat on the", the nursery-rhyme " mat" is not even in GPT-2 XL's top ten: probabilities reflect the training text, not a reader's expectations. Low temperatures suit tasks with one right answer, such as extracting a date; higher ones suit brainstorming, at the cost of more odd choices.

### The KV cache and the cost of inference

To produce token 501, the model needs the keys and values of all 500 earlier tokens at every layer. Recomputing them at every step would mean reprocessing the whole text for each new token, so a reply twice as long would take about four times the work. Serving systems therefore store them, in what is called the **key–value cache** or **KV cache**. Each new token then needs only its own query, key and value, plus attention over the stored keys and values. Generation thus has two phases: a "prefill" that processes the prompt in parallel and fills the cache, and a "decode" phase that adds one token at a time.

The cache holds a key and a value vector per token for every layer, so its size multiplies the number of layers, the width of the stored vectors, the bytes per number and the length of the context (Table 3.9). @kwon2023efficient calculate up to 1.6 gigabytes for one 2,048-token request to the 13-billion-parameter OPT model; a full 128,000-token context in Llama 3 405B takes about 66 gigabytes, for a single user [@grattafiori2024llama].

| Model | Layers | Key + value numbers per token per layer | Bytes per number | Cache per token | Full context |
|---|---|---|---|---|---|
| GPT-2 small | 12 | 2 × 768 | 4 | 74 KB | 75 MB (1,024 tokens) |
| OPT-13B | 40 | 2 × 5,120 | 2 | 800 KB | 1.6 GB (2,048 tokens) |
| Llama 3 405B (8 KV heads) | 126 | 2 × 8 × 128 | 2 | 0.52 MB | 66 GB (128,000 tokens) |
| Same, if all 128 heads kept keys and values | 126 | 2 × 128 × 128 | 2 | 8.3 MB | 1.06 TB (128,000 tokens) |

: Table 3.9: Size of the key–value cache. GPT-2 small at 32-bit precision as run by the author; OPT-13B as calculated by @kwon2023efficient (their 800 KB is 819,200 bytes); decimal units otherwise (1 KB = 1,000 bytes); Llama 3 rows calculated by the author from the architecture in @grattafiori2024llama, assuming 16-bit storage. Source: @kwon2023efficient; @grattafiori2024llama; @radford2019language.

The last row explains a design choice. In standard multi-head attention every head has its own keys and values; **grouped-query attention** lets groups of query heads share one key–value head [@ainslie2023gqa]. Llama 3's 128 query heads share 8 key–value heads, which Meta says it adopted "to improve inference speed and to reduce the size of key-value caches during decoding" [@grattafiori2024llama]. Without it the cache in Table 3.9 would be 16 times larger. Ainslie and colleagues found that it achieves quality close to full multi-head attention at nearly the speed of a single shared key–value head.

The cache also explains why decoding is slow relative to the hardware's arithmetic speed. Each step must read all the weights and the whole cache from memory to produce one token per request, which Ainslie and colleagues call "a severe bottleneck". Serving systems batch many users' requests so that each read of the weights is shared, which makes cache memory the limit on how many requests fit. Kwon and colleagues found that existing systems used only 20.4 to 38.2 per cent of cache memory for actual token states. Their vLLM system manages the cache in small pages, like an operating system's virtual memory, and raised throughput by 2 to 4 times at the same latency [@kwon2023efficient].

### Context windows

The maximum number of tokens a model can attend to at once is its **context window**. GPT-2's window was 1,024 tokens and GPT-3's 2,048 [@radford2019language; @brown2020language]; the largest Llama 3 model accepts 128,000 [@grattafiori2024llama]; and Gemini 1.5 retrieved planted facts with over 99 per cent accuracy in research tests up to at least 10 million tokens [@geminiteam2024gemini].

Long windows are expensive in both computation and memory. Standard attention compares every token with every other, so its computation grows with the square of the length [@vaswani2017attention, Table 1]. A 128,000-token prompt implies about 1.6 × 10^10^ query–key pairs per head per layer, half of which the causal mask discards. And the KV cache grows linearly with length, as Table 3.9 shows. Engineering has eased both. FlashAttention computes exact attention in tiles that fit in a processor's fast on-chip memory, avoiding repeated trips to slower main memory, and its authors reported a threefold training speed-up on GPT-2 with 1,024-token sequences [@dao2022flashattention]. A larger window is not the same as using it well. @liu2024lost found that models answered best when the relevant information sat at the beginning or end of a long input and noticeably worse when it was buried in the middle.

## 3.5 From text predictor to assistant: pre-training and post-training

A modern chatbot is built in stages (Figure 3.3). The first and usually by far the most expensive is **pre-training**: next-token prediction over an enormous body of text, which yields a **base model** like those in Table 3.7. **Post-training** then turns it into an assistant.

![Figure 3.3: How a typical chat model is trained. Pre-training on web-scale text produces a base model that continues text. Training on written examples of good answers (instruction tuning) teaches it to follow instructions. Training on rankings of answers by people or by another AI (preference training) shapes its style and safety. Reasoning models add a further stage of reinforcement learning on problems whose answers can be checked automatically; in recent models this stage can use a substantial share of the training computation. Diagram by the author, based on @ouyang2022training, @bai2022constitutional and @guo2025deepseek.](../figures/svg/fig-03-03.svg){#fig:03-03}

### The pre-training objective

Pre-training uses the text itself as the answer key, which is why it is called **self-supervised learning**: no human labelling is needed. At every position of every training passage the model predicts the next token, and the loss is the cross-entropy of Section 2.3, −ln *p*~true~, the negative natural logarithm of the probability the model gave to the token that actually came next. Table 3.7 gives a sense of scale. If the true continuation is " Paris", Qwen2.5-1.5B's loss at that position is −ln 0.273 ≈ 1.30, while GPT-2 small's is −ln 0.032 ≈ 3.44. A perfect prediction would cost 0. Training averages this loss over trillions of positions and uses backpropagation to nudge every weight in the direction that reduces it. Because of the causal mask, a passage of *n* tokens supplies *n* − 1 separate next-token predictions in one parallel pass.

The pressure to predict text is a pressure to absorb whatever helps predict it: grammar, facts, the conventions of code and mathematics, styles of argument. How loss falls with model size, data and compute is the subject of Chapter 4.

### The data

The corpora have grown by orders of magnitude. GPT-1 in 2018 was trained on BooksCorpus, "over 7,000 unique unpublished books" [@radford2018improving]. GPT-2 used WebText, about 40 GB of text from slightly over 8 million documents linked from Reddit posts with at least three "karma" points [@radford2019language]. GPT-3 was trained on 300 billion tokens drawn largely from Common Crawl, a public archive of the web, filtered from 45 TB of compressed text to 570 GB, plus books and Wikipedia [@brown2020language]. Meta's Llama 3 405B was pre-trained on about 15.6 trillion tokens [@grattafiori2024llama].

Meta describes removing personal data and unsafe domains, de-duplicating at the level of web addresses, documents and lines, applying heuristics such as "dirty word" counts, and scoring documents with quality classifiers, including one trained on judgements by its earlier Llama 2 model. It then chose the mix by training small models on candidate mixes and extrapolating. The final mix was roughly 50 per cent general knowledge, 25 per cent mathematics and reasoning, 17 per cent code and 8 per cent multilingual text [@grattafiori2024llama]. The open FineWeb dataset, presented at NeurIPS 2024, documents a comparable pipeline, with ablations of every filtering and de-duplication choice. It holds 15 trillion tokens from 96 Common Crawl snapshots, and its 1.3-trillion-token educational subset gave "dramatically better performance" on knowledge and reasoning benchmarks [@penedo2024fineweb].

### Instruction tuning

A base model behaves like a sophisticated autocomplete. Asked a question, it may answer, or it may continue with five more questions in the style of an exam paper. The simplest fix is **supervised fine-tuning** (SFT) on examples of instructions paired with good responses, often called **instruction tuning**. @wei2021finetuned fine-tuned a 137-billion-parameter model on more than 60 tasks phrased as natural-language instructions and found that it improved substantially on new kinds of tasks it had not been tuned on. The model learns the general habit of reading an instruction and doing what it says.

### Reinforcement learning from human feedback

Many qualities of a good answer are easier to recognise than to demonstrate. In **reinforcement learning** the model produces an output and receives only a score, a **reward**, and its weights are adjusted to make high-scoring outputs more likely. AlphaGo (Section 1.7) learned partly in this way, with winning as the reward. **Reinforcement learning from human feedback** (RLHF) obtains the reward from people's comparisons, an idea developed by @christiano2017deep for game-playing and simulated robots.

@ouyang2022training applied it to GPT-3 to create InstructGPT, a forerunner of ChatGPT-style assistants, in three steps. About 40 contractors wrote demonstrations for supervised fine-tuning, using about 13,000 training prompts. They then ranked between 4 and 9 model outputs per prompt for about 33,000 prompts, and these rankings trained a 6-billion-parameter **reward model** that outputs a single score for any prompt and response.

The reward model's loss, for a preferred response *y*~w~ and a rejected one *y*~l~, is −log σ(*r*(*x*, *y*~w~) − *r*(*x*, *y*~l~)), where σ is the logistic function that maps any number to a probability. The model thus learns to treat the score difference as the log-odds that a labeller prefers *y*~w~: a difference of 1 means a predicted preference of σ(1) ≈ 73 per cent. Finally, the PPO reinforcement-learning algorithm adjusted the language model on about 31,000 prompts to maximise the reward model's score minus a penalty, at each token, for drifting away from the fine-tuned starting model. The penalty matters because the reward model is only a learned proxy; a policy that strays far from the text it was trained on can find outputs the proxy overrates (Chapter 12 discusses this "reward hacking").

The effect was large: in the authors' human evaluations, outputs from the 1.3-billion-parameter InstructGPT were preferred to those of the 175-billion-parameter GPT-3, "despite having 100x fewer parameters".

### Direct preference optimisation

RLHF is, in the words of @rafailov2023direct, "a complex and often unstable procedure": it trains a separate reward model, then samples from the language model repeatedly during reinforcement learning. Their **direct preference optimisation** (DPO) shows that, under the same preference model, the optimal policy can be obtained without either step. DPO trains directly on preference pairs with a classification-style loss,

−log σ(β log [π(*y*~w~ | *x*) / π~ref~(*y*~w~ | *x*)] − β log [π(*y*~l~ | *x*) / π~ref~(*y*~l~ | *x*)]),

where π is the model being trained, π~ref~ the starting model and β a setting that controls how far π may move. In words: raise the probability of the preferred answer and lower that of the rejected one, each measured relative to the starting model, with the largest updates where the model currently ranks the pair wrongly. The term β log(π / π~ref~) acts as an implicit reward, hence the paper's subtitle, "Your Language Model is Secretly a Reward Model". The authors reported that DPO matched or exceeded PPO-based RLHF on sentiment control, summarisation and single-turn dialogue while being "substantially simpler to implement and train". The openly documented Tülu 3 recipe, for example, runs supervised fine-tuning, then DPO, then a reinforcement-learning stage described in Section 3.7 [@lambert2024tulu].

### Constitutional AI and AI feedback

Human feedback is slow and costly, and can expose labellers to disturbing content. In an Anthropic preprint, @bai2022constitutional proposed **Constitutional AI**. To train the model to avoid harmful outputs, humans supply only a short list of written principles, the "constitution", in place of human harmlessness labels. In a supervised phase, the model drafts responses, critiques them against the principles and revises them, and is fine-tuned on the revisions. In a reinforcement-learning phase, the fine-tuned model produces pairs of responses, a separate feedback model (typically a pre-trained language model) judges which better satisfies a principle, and these AI judgements train the preference model. The authors called this **reinforcement learning from AI feedback** (RLAIF). They reported an assistant that was less harmful without being evasive, engaging with problematic requests by explaining its objections. The paper still used human labels for helpfulness.

Post-training of this kind has traditionally used far less data and computation than pre-training. It is generally thought to change mainly which of the base model's capabilities are expressed, and in what style, without adding much knowledge; reasoning models (Section 3.7) qualify that picture. A model rewarded for answers that people like can also learn to flatter users or to sound confident (Chapter 12).

## 3.6 Why language models hallucinate, and what retrieval changes

LLMs sometimes produce fluent statements that are false: invented quotations, non-existent references, wrong dates. The research literature calls this **hallucination**. @ji2023survey distinguish "intrinsic" hallucinations, which contradict a source the model was given, from "extrinsic" ones, which cannot be verified from that source at all. The term is a loose metaphor: the model perceives nothing, and the errors come from the same mechanism that produces correct answers.

::: {.box .case}
**Case study: Mata v. Avianca (2023)**

In a lawsuit against the airline Avianca in a US federal court in New York, lawyers filed a court submission in March 2023 citing court decisions that did not exist. In his opinion on sanctions, Judge P. Kevin Castel found that the lawyers had "submitted non-existent judicial opinions with fake quotes and citations created by the artificial intelligence tool ChatGPT" and had continued to stand by them after the court questioned their existence [@sdny2023mata, p. 1]. One lawyer testified that he had "falsely assumed" ChatGPT was "like a super search engine" (p. 15). When he asked the chatbot whether a case was real, it replied that it had supplied "real" authorities findable in standard legal databases (p. 19). The court imposed a $5,000 penalty on the two lawyers and their firm (pp. 33–34). A language model's fluency is not evidence that a claim is true, and asking the same model to check itself is not an independent check.
:::

### A statistical account

A model generates text that is probable given its training, and a plausible-looking citation has the right form whether or not it exists. @kalai2025why, in a preprint by researchers at OpenAI and Georgia Tech, make this precise. They compare generation with a simpler task they call "Is-It-Valid": shown a candidate answer, decide whether it is valid or an error. Generating only valid answers is at least as hard as this classification, and they derive that a base model's generative error rate is at least roughly twice its misclassification rate on Is-It-Valid. Wherever classification is bound to fail, generation will fail too.

Arbitrary facts are where classification is bound to fail. A person's birthday follows no pattern that could be inferred from other facts, so a birthday seen only once in training gives the model little more to go on than one never seen. Building on an estimator that goes back to Alan Turing, the authors use the share of facts that appear exactly once, the "singleton rate", as a measure of how much the model has in effect not learned. If 20 per cent of birthday facts appear exactly once in the training data, a base model should be expected to hallucinate on at least about 20 per cent of birthday questions. Asked for Adam Kalai's own birthday and told to answer only if it knew, "a state-of-the-art open-source language model" gave three different wrong dates in three attempts.

The second part of the argument concerns post-training. Most benchmarks award a point for a correct answer and nothing for "I don't know", so a model that guesses outscores one that admits uncertainty, as a student does on a multiple-choice exam without negative marking. The authors' meta-evaluation found that the large majority of popular benchmarks use such binary grading. Their remedy is to state a confidence threshold *t* in each evaluation's instructions and penalise wrong answers by *t*/(1 − *t*) points. With *t* = 0.75 a wrong answer costs 0.75/0.25 = 3 points, so guessing pays only when the model is more than 75 per cent sure (the preprint's own worked example says 2, an arithmetic slip). Under such scoring, saying "I don't know" below the threshold becomes the best-scoring strategy.

### Retrieval-augmented generation

If hallucination arises partly because rare facts are stored imperfectly in the weights, one remedy is to supply the facts at answer time. **Retrieval-augmented generation** (RAG), introduced by @lewis2020retrieval, combines a language model with a searchable index. The documents are cut into passages, and an encoder network converts each passage into an embedding. A second encoder, trained alongside the first, embeds the question; the passages whose embeddings have the largest dot product with the question's are retrieved and placed in the model's context window alongside it. In the dense passage retriever used by Lewis and colleagues, English Wikipedia was split into 21,015,324 passages of 100 words. On the Natural Questions benchmark this retriever found a passage containing the answer among its top 20 results for 78.4 per cent of questions, against 59.1 per cent for BM25, a classic keyword-based search method [@karpukhin2020dense]. RAG models generated "more specific, diverse and factual language" than a model relying on its weights alone [@lewis2020retrieval]. The pattern now sits behind chatbots that search the web and assistants that consult company documents, and lets a system use information newer than its training data.

Retrieval reduces errors but does not remove them: the retriever may return the wrong passages, and the model may misread the right ones or blend them with its own guesses. In a preregistered study, @magesh2025hallucination tested legal research tools from LexisNexis and Thomson Reuters that were marketed with claims such as "hallucination-free". The tools hallucinated less than general-purpose GPT-4, but each hallucinated between 17 and 33 per cent of the time on the authors' set of legal queries. Long retrieved contexts also run into the "lost in the middle" problem (Section 3.4).

An LLM's answer is most trustworthy where the relevant facts are common in its training data or supplied in its context, and least trustworthy for rare specifics: exact figures, quotations, references and recent events. Chapter 11 treats hallucination as a source of wider risk.

## 3.7 Reasoning models and what is inside

A model spends roughly the same computation on every token, so a hard question answered in one word gets little "thinking". @wei2022chain showed that giving a large model a few worked examples with step-by-step reasoning, **chain-of-thought prompting**, markedly improved its performance on arithmetic word problems. With eight such examples a 540-billion-parameter model set a new state of the art on the GSM8K benchmark of grade-school mathematics problems.

### Reinforcement learning with verifiable rewards

Reasoning models make this behaviour a trained skill. OpenAI's system card describes its o1 series, released in late 2024, as "trained with large-scale reinforcement learning to reason using chain of thought" [@openai2024o1, p. 1]. The key change from RLHF is the reward. Where an answer can be checked by a program (a number to compare, code to run against tests), the reward needs no learned model of human taste. The Tülu 3 report named this **reinforcement learning with verifiable rewards** (RLVR): the model "only gets a reward if the model's completions are verified to be correct" [@lambert2024tulu]. A program that checks a mathematical answer is much harder to fool than a reward model, though not impossible (Chapter 12).

DeepSeek published the most detailed recipe, in peer-reviewed form in *Nature* in September 2025 [@guo2025deepseek]. For an experimental model, DeepSeek-R1-Zero, it started from its pre-trained base model, skipped supervised fine-tuning and applied reinforcement learning with two rule-based rewards: one for an answer matching the known correct result and one for putting the reasoning in the required format. The algorithm, Group Relative Policy Optimization (GRPO), introduced in a 2024 DeepSeek preprint, avoids training a separate value network [@shao2024deepseekmath]. For each question it samples a group of answers, scores them, and treats each answer's reward relative to the group's mean, divided by the group's standard deviation, as the signal. If four sampled answers score 1, 0, 0 and 1, the mean is 0.5 and the standard deviation 0.5, so the correct answers are reinforced with +1 and the wrong ones discouraged with −1. If all four are right, or all wrong, there is nothing to learn from that question.

Progress was measured on AIME 2024, the American Invitational Mathematics Examination, in which every answer is a single number that can be checked automatically. During training, R1-Zero's average accuracy rose from 15.6 to 77.9 per cent. Its answers grew steadily longer, and it began to check and revise its own work, at one point writing "Wait, wait. Wait. That's an aha moment I can flag here." (The figures are DeepSeek's own, from the *Nature* version; the January 2025 preprint reported 71.0 per cent.) The released DeepSeek-R1, which added supervised fine-tuning stages, scored 79.8 per cent, close to the developers' measurement for OpenAI's o1, and was published under the permissive MIT licence.

This stage is no longer a small add-on. Epoch AI, an independent research institute, estimated in May 2025 that the reinforcement-learning stage of DeepSeek-R1 used about 6 × 10^23^ operations, about 20 per cent of the cost of pre-training its base model. It also cited OpenAI's statement that o3 used ten times the training compute of o1, most likely in this stage [@you2025how]. The resulting gains in mathematics and coding suggest that post-training of this kind adds skills, not only style. Reasoning models also make capability purchasable at answer time, by thinking longer or sampling several answers; Chapter 4 treats this **test-time compute** as a scaling trend. Verifiable rewards work best where answers can be checked, as in mathematics and programming, and less well for essays or advice.

The written reasoning is not necessarily a faithful record of how the model reached its answer. In a preprint, Anthropic researchers slipped hints into questions and checked whether reasoning models that used a hint said so. The models mentioned the hint only a minority of the time: 25 per cent on average for Anthropic's Claude 3.7 Sonnet and 39 per cent for DeepSeek-R1 [@chen2025reasoning]. This matters for safety monitoring that relies on reading the chain of thought (Section 12.5).

### What interpretability finds inside

Engineers know exactly what computations an LLM performs, but not fully what the learned weights represent. **Interpretability** research has begun to decompose the residual stream into human-recognisable features, such as one for the Golden Gate Bridge [@templeton2024scaling]. It has also traced intermediate steps, such as a model choosing a rhyme before writing the line, or representing "Texas" on the way from "Dallas" to "Austin" [@lindsey2025biology]. Section 12.4 describes these methods and their limits.

::: {.box .debate}
**Debate: Do large language models understand language?**

A 2022 survey of natural-language-processing researchers [@michael2023what], also discussed by @mitchell2023debate, asked whether some model trained only on text, given enough data and computing power, could understand natural language "in some non-trivial sense". Of the 327 active researchers whose answers the survey authors analysed (out of 480 who completed it), 51 per cent agreed and 49 per cent disagreed.

The case against rests on a point of principle. @bender2020climbing argue that "a system trained only on form has a priori no way to learn meaning". Their thought experiment imagines a hyper-intelligent octopus tapping an undersea telegraph cable between two people: it could learn to imitate their messages convincingly yet would have no idea what the words refer to. On this view fluent output reflects statistical patterns in human writing, and hallucinations are exactly what one would expect from a system with no link between words and world.

The case for rests on internal evidence. @li2023emergent trained a GPT-style model only on sequences of moves in the board game Othello, never showing it the board, and found an internal representation of the board state; altering that representation changed the model's predicted moves accordingly. The planning and two-step inference reported by @lindsey2025biology point the same way for a commercial model, with the caveat that it is a company's study of its own system.

The two sides weigh different evidence: one asks what a text-trained system can in principle connect its symbols to, the other what structure it demonstrably builds. @mitchell2023debate propose splitting "understanding" into several kinds, each with its own strengths and limitations. Intervention experiments like the Othello study can test the second question; whether any experiment could answer the first is itself disputed.
:::

Seen whole, the mechanism accounts for both what language models do well and where they fail. Next-token prediction rewards whatever regularities recur in the training text, so a model is fluent on common material, unreliable on rare specifics such as exact figures, quotations and references, and blind to events after its data were collected. Post-training changes what is rewarded without changing that mechanism; preference training inherits the blind spots of the people or models doing the ranking, and verifiable rewards help most where a program can check the answer. The costs follow the architecture's arithmetic: about two operations per parameter for every token, a cache that grows with every token of context, and attention whose work grows with the square of the context. Those quantities, multiplied up to the scale of frontier training runs, are the subject of Chapter 4.

## Further reading

- Vaswani, A. et al. (2017). *Attention Is All You Need*. The original transformer paper; Sections 3.2 to 3.5 give the attention formula, multi-head attention and sinusoidal positions in full. [@vaswani2017attention]
- Elhage, N. et al. (2021). *A Mathematical Framework for Transformer Circuits*. Rebuilds the transformer around the residual stream and shows what small attention-only models compute, with careful diagrams. [@elhage2021mathematical]
- Ouyang, L. et al. (2022). *Training Language Models to Follow Instructions with Human Feedback*. The clearest primary account of supervised fine-tuning, reward modelling and PPO turning a base model into an assistant, with dataset sizes and evaluation details. [@ouyang2022training]
- Guo, D. et al. (2025). *DeepSeek-R1 Incentivizes Reasoning in LLMs through Reinforcement Learning*. The most open description of reinforcement learning with verifiable rewards at scale, including the reward design and training curves. [@guo2025deepseek]
- Kalai, A. T. et al. (2025). *Why Language Models Hallucinate*. A short statistical argument for why confident errors arise in pre-training and persist through evaluation, with a concrete proposal for scoring. [@kalai2025why]


# Chapter 4: Scaling, Compute and the Limits of Progress

In 2012 the image classifier AlexNet was trained on two consumer graphics cards for "five to six days" [@krizhevsky2012imagenet, p. 7]. Epoch AI, a research institute that tracks the resources used to train AI systems, estimates that the run used about 4.7 × 10^17^ arithmetic operations [@epochai2026data]. Twelve years later Meta trained Llama 3.1 405B, the largest model of its Llama 3 family, released in July 2024, on up to 16,384 Nvidia H100 chips. According to the company's technical report, the run used 3.8 × 10^25^ operations, roughly 80 million times what AlexNet needed [@grattafiori2024llama]. During one 54-day stretch Meta logged 466 interruptions; about 78% of the unexpected ones were traced to confirmed or suspected hardware faults, yet significant manual intervention was needed only three times [@grattafiori2024llama].

Growth on this scale was deliberate. From 2020 onwards a set of empirical regularities, the scaling laws, gave developers reason to believe that a larger training run would buy a predictably better model. The size of the improvement, they suggested, could be calculated in advance from small experiments. Chapter 7 covers the chips, data centres and energy behind the numbers.

## 4.1 Counting compute: FLOP, GPU-hours and utilisation

A training run is described first by the number of **parameters** *N*, the adjustable numbers inside a neural network that are tuned during training (Chapter 2). Its training data *D* are counted, for language models, in tokens, the word fragments introduced in Chapter 3. Its **training compute** *C* is the total number of arithmetic operations performed. Compute is counted in **FLOP** (floating-point operations): one FLOP is a single addition or multiplication of two floating-point numbers, the format computers use for values with a fractional part.

For a transformer language model the three are tied together by a simple rule, *C* ≈ 6*ND* [@kaplan2020scaling]. Processing one token in the forward pass costs about two operations per parameter, one multiplication and one addition. The backward pass of backpropagation, which works out how each parameter should change, costs about twice as much again. Six operations per parameter per token is the sum. For Llama 3.1 405B, 6 × (405 × 10^9^) × (15.6 × 10^12^) ≈ 3.79 × 10^25^ FLOP, which matches the figure Meta reports [@grattafiori2024llama].

The rule counts only parameters that are actually used for each token. DeepSeek-V3, a "mixture-of-experts" model, has 671 billion parameters but routes each token through only 37 billion of them. Trained on 14.8 trillion tokens, it needed about 6 × 37 × 10^9^ × 14.8 × 10^12^ ≈ 3.3 × 10^24^ FLOP [@deepseekai2024deepseekv3], the same figure Epoch records [@epochai2026data]. A model with two-thirds more parameters than Llama 3.1 405B thus needed less than a tenth of its training compute. The rule also leaves out the embedding layers and the attention computation over the context. Attention's cost grows with the length of the context and stays small only while the width of the model's internal vectors exceeds about a twelfth of that length [@kaplan2020scaling].

The forward pass alone, about 2*N* FLOP per token, is also the arithmetic cost of using a trained model: reading or generating one token costs roughly 2*N* operations, with *N* again counting active parameters [@kaplan2020scaling]. In practice generating text is often limited by how fast the weights can be read from memory rather than by arithmetic (Section 7.1), but that cost too grows with the number of parameters. Training a model costs 6*N* per training token once; using it costs 2*N* per token for as long as it is in service. That asymmetry underlies the case for over-training in Section 4.3.

The same total can be approached from the hardware side: compute equals the number of chips, times the training time, times each chip's peak speed, times the fraction of that peak actually achieved. That last factor is the **model FLOPs utilisation** (MFU): the operations that contribute to training divided by the theoretical maximum. Google's PaLM team proposed MFU to replace **hardware FLOPs utilisation** (HFU), which also counts work the hardware does but training does not strictly require, such as recomputing intermediate results to save memory. For the 540-billion-parameter PaLM the two were 46.2% and 57.8% [@chowdhery2023palm]. Meta reports MFU of 38–43% across the stages of its run, including 41% (about 400 trillion operations per second per chip) on 16,384 GPUs, measured against the H100's peak for 16-bit arithmetic [@grattafiori2024llama]. The choice of peak matters: the chip's 8-bit peak is roughly twice its 16-bit one, so the same run shows about half the MFU when measured against it. Epoch's documentation describes 30–50% as typical for large distributed runs, because chips wait for memory and for each other [@epochai2026data].

A worked example connects the two views. At 400 trillion FLOP per second, 3.8 × 10^25^ FLOP takes 3.8 × 10^25^ ÷ (4 × 10^14^ × 3,600) ≈ 26 million **GPU-hours**, the unit cloud providers bill in: one chip running for one hour. Spread over 16,384 chips, that is about 67 days of uninterrupted work. Meta's model card reports 30.84 million H100 GPU-hours for the 405-billion-parameter model, counted as the total GPU time required for training it [@meta2024llama]. The gap of about 4.5 million GPU-hours is consistent with time lost to restarts and checkpointing, with stages that ran below 41% utilisation and with training beyond the main pre-training run. Meta reports "higher than 90% effective training time" [@grattafiori2024llama].

::: {.box .deeper}
**Going deeper: Estimating compute when developers stay silent**

Several leading developers no longer publish parameter counts or dataset sizes [@sajadieh2026ai], so outside estimates rely on the two formulas above. Counting operations from the architecture (*C* ≈ 6 × *N* × *D*, with active parameters for mixture-of-experts models) is Epoch's preferred method, because counting hardware (*C* ≈ chips × seconds × peak FLOP/s × utilisation) requires an assumed utilisation [@epochai2026data]. For OpenAI's GPT-4.5, released in February 2025, Epoch used the hardware route: it estimated 187 million H100-hours at 20–40% of the chip's 8-bit peak, which gives 2.7 to 5.4 × 10^26^ FLOP; it records the geometric mean, 3.8 × 10^26^. Every estimate carries a confidence label: "confident" values are expected to be within a factor of 3 of the truth, "likely" ones within a factor of 10, "speculative" ones within a factor of 30. The GPT-4 estimate of 2.1 × 10^25^ FLOP, for instance, is "likely" [@epochai2026data].
:::

## 4.2 Scaling laws: loss as a power of resources

Why expect size alone to help? Section 1.7 introduced Richard Sutton's 2019 essay "The bitter lesson", which argued from the history of chess, speech recognition and vision that general methods able to use more computation eventually beat hand-built knowledge [@sutton2019bitter]. Measurements had begun to back the argument. In 2017 Joel Hestness and colleagues at Baidu Research found that error fell as a power law of training-set size in machine translation, language modelling, image classification and speech recognition. Better architectures shifted the curves but did not appear to change their slopes [@hestness2017deep]. In 2019 Jonathan Rosenfeld and colleagues fitted one functional form to error as a function of both model and dataset size, in vision and language, and used it to predict large-scale results from small ones [@rosenfeld2020constructive].

In January 2020 Jared Kaplan and colleagues at OpenAI carried the approach to language models across a wider range of scales, in a preprint [@kaplan2020scaling]. They trained transformers ranging from 768 to 1.5 billion non-embedding parameters on WebText2, a corpus of web pages, and recorded each model's test **loss**: its average error at predicting the next token of text it has not seen. The loss is measured as cross-entropy, the average of the negative natural logarithm of the probability the model gave to the correct token, in units called nats per token; lower is better.

Loss fell along smooth **power laws** in each resource whenever the other two were not the bottleneck, with some trends spanning "more than seven orders of magnitude". Counting *N* without the embedding parameters that map tokens to vectors, the fitted laws were:

- *L*(*N*) = (*N*~c~ / *N*)^0.076^, with *N*~c~ ≈ 8.8 × 10^13^ parameters, for models trained to convergence on ample data;
- *L*(*D*) = (*D*~c~ / *D*)^0.095^, with *D*~c~ ≈ 5.4 × 10^13^ tokens, for large models stopped early on limited data;
- *L*(*C*) = (*C*~c~ / *C*)^0.050^, with *C*~c~ ≈ 3.1 × 10^8^ PF-days, for compute spent on an optimally sized model. A **petaflop/s-day** (PF-day) is 10^15^ operations per second sustained for a day, or 8.64 × 10^19^ FLOP.

The exponents carry the meaning. Doubling the parameter count multiplies loss by 2^−0.076^ ≈ 0.95, a 5% reduction, as the paper itself notes. Multiplying compute tenfold multiplies loss by 10^−0.05^ ≈ 0.89. On a graph with logarithmic axes, where each step is a tenfold increase, a power law is a straight line, and that is what makes the laws useful for planning. A developer can train a series of small models, fit the line and extend it to predict the loss of a run a thousand times larger. The constants *N*~c~, *D*~c~ and *C*~c~ depend on the vocabulary and tokeniser, so the paper warns that they "do not have a fundamental meaning"; the exponents are the informative part.

::: {.box .concept}
**Concept: Scaling law**

A scaling law is an empirical rule that describes how a model's performance changes as the resources used to train it grow. For language models the classic finding is that test loss falls as a power law of compute, parameters or data: each tenfold increase in resources removes a roughly constant fraction of the remaining error, so the absolute gains shrink while the cost of each next step grows. Scaling laws are fitted observations, not laws of nature. They hold over the range where they were measured, they depend on the data and training recipe, and they describe loss, not the particular skills people care about.
:::

Kaplan's team also combined the laws. The equation *L*(*N*, *D*) = [(*N*~c~/*N*)^*α*~N~/*α*~D~^ + *D*~c~/*D*]^*α*~D~^, in which *α*~N~ = 0.076 and *α*~D~ = 0.095 are the exponents above, describes how a model overfits when data run short. It implies that data need to grow only as *N*^0.74^: "every time we increase the model size 8x, we only need to increase the data by roughly 5x". For a fixed compute budget the best model size grew as *C*^0.73^ and the data as only *C*^0.27^. A hundredfold increase in compute should therefore buy a model about 29 times larger, trained on about 3.5 times as many tokens and stopped "significantly short of convergence" [@kaplan2020scaling].

Figure 4.1 shows the shape of such a law, including the floor that later work added to it. Real loss cannot fall to zero, because text is partly unpredictable: there is a component of error, the **irreducible loss**, that no amount of compute removes. OpenAI's GPT-4 report fitted a curve of the form *L*(*C*) = *aC*^*b*^ + *c*, with *c* as that floor, and states that GPT-4's final loss was predicted "with high accuracy" from models trained with "at most 10,000x less compute" [@openai2023gpt4, p. 2]. The same report cautions that performance on individual problems "may occasionally worsen with scale".

![Figure 4.1: Schematic of a scaling law. On logarithmic axes, test loss falls along an approximately straight line as training compute grows. Small, cheap runs (filled dots) are used to fit the line, which is then extended to predict the loss of a planned large run (hollow dot). The curve flattens towards an irreducible loss that more compute cannot remove. Schematic, not to scale. Diagram by the author.](../figures/svg/fig-04-01.svg){#fig:04-01}

Loss is not what users experience, so developers chain a second relation on top. Meta first related training compute to the model's loss on the correct answers of a benchmark, then related that loss to accuracy with an S-shaped (sigmoidal) curve. Using only models trained with up to 10^22^ FLOP, it forecast the 405-billion-parameter model's score on the ARC Challenge science-question benchmark across four orders of magnitude, and the forecast "only slightly underestimates" the final result [@grattafiori2024llama].

## 4.3 Compute-optimal training: Chinchilla and its revisions

Kaplan's allocation rule shaped the models of 2020 and 2021. GPT-3 had 175 billion parameters and was trained on 300 billion tokens [@brown2020language], under two tokens per parameter. DeepMind's Gopher had 280 billion parameters and also saw 300 billion tokens [@epochai2026data]. In 2022 a DeepMind team with Jordan Hoffmann as first author asked the question again, and got a different answer [@hoffmann2022empirical]. They trained more than 400 models, from 70 million to over 16 billion parameters, on 5 to 500 billion tokens, and estimated the optimal split of a compute budget in three independent ways.

The first approach fixed a family of model sizes and trained each for four different numbers of tokens, with the learning-rate schedule matched to each length, then read off, at 1,500 compute levels, which run reached the lowest loss. The second, the **IsoFLOP** method, fixed nine compute budgets, trained models of different sizes on each, fitted a parabola to loss against size and took its minimum. The third fitted a single formula to all final losses:

*L*(*N*, *D*) = *E* + *A* / *N*^*α*^ + *B* / *D*^*β*^

Here *E* is the irreducible loss of the text itself, the second term is the penalty for a finite model, and the third is the penalty for finite training data. The published fit was *E* = 1.69, *A* = 406.4, *B* = 410.7, *α* = 0.34 and *β* = 0.28 [@hoffmann2022empirical]. All three approaches pointed the same way, summarised in Table 4.1: parameters and tokens should grow in roughly equal proportion with compute, so that "for every doubling of model size the number of training tokens should also be doubled".

| Approach | Exponent *a* (*N*~opt~ ∝ *C*^*a*^) | Exponent *b* (*D*~opt~ ∝ *C*^*b*^) |
|---|---|---|
| 1. Minimum over training curves | 0.50 (0.488–0.502) | 0.50 (0.501–0.512) |
| 2. IsoFLOP profiles | 0.49 (0.462–0.534) | 0.51 (0.483–0.529) |
| 3. Parametric loss fit | 0.46 (0.454–0.455) | 0.54 (0.542–0.543) |
| Kaplan et al. (2020) | 0.73 | 0.27 |

: Table 4.1: How optimal model size (*N*) and training tokens (*D*) should grow with compute (*C*), according to the three Chinchilla methods and to Kaplan et al. Ranges are the 10th–90th percentiles from bootstrapping, as published. Source: @hoffmann2022empirical.

The fitted formula makes the difference concrete. For Gopher (280 billion parameters, 300 billion tokens) it gives 1.69 + 0.05 + 0.25 ≈ 1.99; the data term is five times the model term, the mark of a model starved of tokens. For a 70-billion-parameter model on 1.4 trillion tokens it gives 1.69 + 0.08 + 0.16 ≈ 1.94, lower, for roughly the same compute.

DeepMind built that model and named it Chinchilla. It used about the same compute as Gopher, 5.76 × 10^23^ against 6.31 × 10^23^ FLOP in Epoch's estimates [@epochai2026data]. It outperformed Gopher, GPT-3 and other larger models on a wide range of tasks and reached 67.5% average accuracy on the MMLU knowledge test, "greater than a 7% improvement over Gopher" [@hoffmann2022empirical]. Being four times smaller, it was also cheaper to run. By the first approach (the paper's Table 3), a compute-optimal model of GPT-3's size would have needed about 3.7 trillion tokens; the main text quotes "over 4.2 trillion" with 4.41 × 10^24^ FLOP. A one-trillion-parameter model, the authors added, was unlikely to be optimal below about 10^26^ FLOP.

Why had Kaplan's team concluded otherwise? Hoffmann and colleagues pointed to two choices: Kaplan used one fixed learning-rate schedule for all runs, which overstated the loss of shorter runs, and mostly small models, many under 100 million parameters. In 2024 Pearce and Song showed that counting only non-embedding parameters, combined with small scale, biases the estimated exponent towards Kaplan's 0.73 [@pearce2024reconciling]. Porian and colleagues reproduced Kaplan's law and then removed the discrepancy by correcting three factors, the computational cost of the final layer, the length of the learning-rate warm-up and optimiser settings tuned to each scale, obtaining "excellent agreement" with Chinchilla [@porian2024resolving].

The Chinchilla paper itself has been re-examined. Besiroglu and colleagues at Epoch AI reconstructed the data behind the third approach from the paper's figures, in a preprint [@besiroglu2024chinchilla]. The published fit described the data poorly, and its confidence intervals were implausibly narrow: intervals that tight "would require over 600,000 experiments", whereas Hoffmann's team likely ran fewer than 500. One of the original authors attributed the error to an optimiser that stopped before converging. The published parameters implied about 70 tokens per parameter as optimal, inconsistent with Chinchilla's own choice. The refit, with a larger data exponent (*β* = 0.37 against 0.28), implied about 20, so the rule of thumb practitioners took from the paper survived the correction.

Later work extended the method to variables that Chinchilla held fixed. For mixture-of-experts models, parameter count and compute per token separate. Clark and colleagues at DeepMind fitted laws on both axes and predicted that the benefit of routing tokens to experts shrinks as the underlying model grows [@clark2022unified]. Ludziejewski, Krajewski and colleagues added the size of each expert as a variable and found that experts smaller than the customary size work better at almost any budget [@ludziejewski2024scaling]. They traced Clark's pessimistic result to its fixed number of training tokens: when model size, data and expert size were all set compute-optimally, mixture-of-experts models beat dense ones at every scale, by a margin that widened as budgets grew.

### Over-training on purpose

Compute-optimal means optimal for the training bill only. A model that will answer billions of queries pays about 2*N* operations on every token it reads or writes (Section 4.1), so a smaller model trained for longer can be cheaper over its lifetime. Sardana and colleagues extended the Chinchilla formula to include inference and found that developers expecting about a billion requests should train smaller models on more data; in their own experiments, quality kept improving up to 10,000 tokens per parameter [@sardana2024beyond]. Table 4.2 shows how far practice has moved.

| Model (year) | Parameters | Training tokens | Tokens per parameter | 6*ND* (FLOP) |
|---|---|---|---|---|
| GPT-3 (2020) | 175 billion | 300 billion | 1.7 | 3.2 × 10^23^ |
| Gopher (2021) | 280 billion | 300 billion | 1.1 | 5.0 × 10^23^ |
| Chinchilla (2022) | 70 billion | 1.4 trillion | 20 | 5.9 × 10^23^ |
| Llama 3.1 405B (2024) | 405 billion | 15.6 trillion | 39 | 3.8 × 10^25^ |
| Llama 3 8B (2024) | 8 billion | about 15 trillion | about 1,900 | 7.2 × 10^23^ |

: Table 4.2: Parameters, training tokens and implied compute for five language models. The last column is calculated by the author with *C* ≈ 6*ND*; Gopher's reported compute (6.31 × 10^23^ FLOP) is higher than the formula gives. Sources: [@brown2020language; @hoffmann2022empirical; @grattafiori2024llama; @epochai2026data].

The small Llama 3 model is the clearest case. Its 7.2 × 10^23^ FLOP exceeds Chinchilla's entire budget; spent compute-optimally at 20 tokens per parameter (*C* = 6*N* × 20*N*), that budget would have bought a model of about 77 billion parameters trained on 1.5 trillion tokens. Each token the 8-billion-parameter model processes in use costs about a tenth as much. Meta trained its smaller models "for much longer than is compute-optimal", because they then "perform better than compute-optimal models at the same inference budget" [@grattafiori2024llama].

Over-training has a cost that appears only after training. Models are often served at reduced numerical precision to save memory and time. Kumar and colleagues found that the damage done by such post-training quantisation grows with the amount of pre-training data, to the point where more data can make the quantised model worse [@kumar2025scaling]. Their laws, fitted on more than 465 runs with models of up to 1.7 billion parameters, also put the compute-optimal precision for training at around 7–8 bits, which suggests that the customary 16-bit training may be suboptimal.

::: {.box .case}
**Case study: Sizing Llama 3 with a scaling law**

Meta's technical report describes how the company chose the size of its largest model [@grattafiori2024llama, pp. 7–8]. The team trained models of 40 million to 16 billion parameters at compute budgets between 6 × 10^18^ and 10^22^ FLOP, fitted a parabola to loss against the number of training tokens for each budget, and took the minima as the compute-optimal points. It then fitted a power law between compute and the optimal number of tokens, with an exponent of 0.53, close to Chinchilla's 0.5, and extended it to the planned 3.8 × 10^25^ FLOP. The extrapolation suggested 402 billion parameters on 16.55 trillion tokens, about 41 tokens per parameter. Because the IsoFLOP curves flattened near their minima as budgets grew, small deviations from the optimum cost little, and the team settled on 405 billion parameters and 15.6 trillion tokens. A plain 20-tokens-per-parameter rule would have suggested, by the author's calculation, about 560 billion parameters on 11 trillion tokens for the same budget. The optimal ratio depends on the data and the training recipe, one reason developers fit their own laws.
:::

The Chinchilla result changed what scaling demands. Under Kaplan's rule, a hundredfold increase in compute called for 3.5 times as much data. Under Chinchilla's, it calls for ten times as much, and over-training for cheaper inference pushes the demand higher still. Scaling became as much a matter of finding tokens as of buying chips.

## 4.4 Compute and cost: the trends

Sevilla and colleagues assembled estimates for 123 milestone machine-learning systems and identified three eras [@sevilla2022compute]. Before about 2010 training compute doubled roughly every 20 months, in line with Moore's law, the long-running doubling of transistors per chip. In the deep-learning era that began in the early 2010s, it doubled about every six months. From late 2015 a "large-scale era" appeared, in which companies trained models needing 10 to 100 times more compute than the typical system of their time.

Epoch's dashboard, last updated on 5 February 2026, puts the growth of training compute for frontier language models at 5 times per year since 2020 (90% CI 4 to 6 times), a doubling every 5.2 months. The trend among the top five models has grown about 10,000-fold over that period [@epochai2026trends]. Frontier models here means the most capable general-purpose models of their time; Chapter 13 discusses how laws define them. Epoch attributes the growth to more chips used in parallel, longer training runs and more powerful, cost-effective processors. Only the last comes from better hardware; the first two come from spending more. The installed stock of AI computing power is growing more slowly, at 3.4 times per year since 2022 by Epoch's estimate [@epochai2026trends]. The 2026 AI Index, drawing on Epoch's data, gives 3.3 times and puts global capacity at the equivalent of 17.1 million Nvidia H100 chips [@sajadieh2026ai].

Figure 4.2 plots Epoch's estimates for a selection of well-known systems, from the Perceptron Mark I of 1957 to models released in 2025, a span of more than twenty orders of magnitude. GPT-3 used an estimated 3.1 × 10^23^ FLOP; GPT-4.5 used about 3.8 × 10^26^, some 1,200 times more [@epochai2026data]. The largest estimate in Epoch's database as of October 2026 is for GPT-6 Astra, which OpenAI released in September 2026 (on 3 September, in Epoch's records) and rates as meeting the Critical threshold for cybersecurity under its Preparedness Framework (Section 12.7) [@openai2026gpt6]. OpenAI has not disclosed Astra's training compute. Epoch puts it at about 9.4 × 10^26^ FLOP, a "likely" estimate with an interval of roughly 5 × 10^26^ to 2 × 10^27^ [@epochai2026data]. The figure rests on statements by OpenAI and partners such as Nvidia that Astra was trained on at least 100,000 GB200 chips, Nvidia's Blackwell-generation accelerators (Section 7.1). Epoch then assumed 90 days of training at 25% of the chips' 8-bit peak.

![Figure 4.2: Estimated training compute of selected notable AI systems, 1957–2025, on a logarithmic scale. Each gridline is a tenfold increase. Values are Epoch AI estimates; those marked "likely" are expected to be accurate within a factor of 10, and the others within a factor of 3. Source: @epochai2026data.](../figures/svg/fig-04-02.svg){#fig:04-02}

These figures are increasingly estimates. The AI Index notes that training code, parameter counts, dataset sizes and training duration are no longer disclosed for several of the most resource-intensive systems, including those from OpenAI, Anthropic and Google. Training compute, which outsiders can estimate, has continued to rise [@sajadieh2026ai]. Of the twelve points in Figure 4.2, the two largest, Grok 3 and GPT-4.5, are "likely" estimates, expected to be accurate only within a factor of 10.

### What training runs cost

More compute costs more money, though cheaper hardware offsets part of the rise. Cottier and colleagues, in a preprint from Epoch AI and Stanford, compared three ways of costing a run [@cottier2024rising]. Their preferred method spreads the purchase price of the hardware over its working life, charges the run for the share it used and adds energy. On that basis the cost of the most compute-intensive training runs grew 2.4 times per year from 2016 (90% CI 2.0 to 2.9). Pricing the same runs at cloud rental rates gave a similar growth rate but costs about twice as high.

For four models whose full development they costed (GPT-3, OPT-175B, GPT-4 and Gemini Ultra), research staff including equity made up 29–49% of the total, computing hardware 47–64% and energy only 2–6% [@cottier2024rising]. Epoch's later dashboard puts the growth in frontier training costs at 3.5 times per year since 2020, while the price-performance of chips has improved by 1.49 times per year since 2023 [@epochai2026trends]. Table 4.3 lists Epoch's amortised estimates for some of the largest runs.

| Model (release) | Training compute (FLOP) | Epoch confidence | Amortised hardware and energy cost (2023 US$) |
|---|---|---|---|
| Gopher (Dec 2021) | 6.3 × 10^23^ | Confident | 0.6 million |
| GPT-4 (Mar 2023) | 2.1 × 10^25^ | Likely | 37 million |
| Llama 3.1 405B (Jul 2024) | 3.8 × 10^25^ | Confident | 53 million |
| Grok 3 (Feb 2025) | 3.5 × 10^26^ | Likely | 218 million |
| GPT-4.5 (Feb 2025) | 3.8 × 10^26^ | Likely | 366 million |
| Grok 4 (Jul 2025) | 5 × 10^26^ | Speculative | 388 million |

: Table 4.3: Estimated training compute and amortised cost of the final training run for six large models, from Epoch AI's database in 2023 US dollars. Costs exclude experiments, staff and data, and inherit the uncertainty of the compute estimates; Cottier et al.'s 2024 preprint, using the same method on earlier data, put GPT-4 at about $40 million. Sources: [@epochai2026data; @cottier2024rising].

These are costs of a final run. Experiments, failed attempts, staff and serving the model to users come on top, and Chapter 7 discusses who can afford them and how DeepSeek's low reported costs fit the picture.

## 4.5 The data constraint

If compute grows about fivefold a year and compute-optimal training needs data to grow nearly as fast as model size, the demand for text rises steeply. Villalobos and colleagues at Epoch AI estimated how much public human-written text exists [@villalobos2024position]. They put Common Crawl, the open web archive behind most training sets, at about 130 trillion tokens and the indexed web (pages reachable through search engines) at about 510 trillion. The whole web, including the "deep web" that search engines do not index, holds about 3,100 trillion. Filtering for quality reduces the usable stock to about 100 trillion tokens. Allowing for each token to be used several times in training raises the effective stock to about 320 trillion, with a 95% confidence interval of 65 to 1,700 trillion.

Training datasets had grown about 2.4 times per year. Extending both trends, the median date at which a training run would use the entire effective stock is 2028, with a range of 2026 to 2032, or slightly earlier if models are over-trained [@villalobos2024position]. Llama 3.1 405B's 15.6 trillion tokens are about one-twentieth of the central estimate [@grattafiori2024llama].

The repetition allowance rests on experiments by Muennighoff and colleagues, who ran 400 training runs with models of up to 9 billion parameters and up to 900 billion tokens [@muennighoff2023scaling]. For a fixed compute budget, training on the same data for up to four **epochs** (complete passes through the dataset) gave "negligible changes to loss" compared with fresh data. Beyond that, repeated tokens lost value: in their fitted law, meaningful gains from repetition continue up to about 16 epochs, beyond which returns "diminish extremely fast" and extra compute spent on the same text buys almost nothing. Villalobos and colleagues used this result to assume that repetition can multiply the effective size of a dataset by between 3 and 15 times.

Other sources widen the stock. A separate Epoch analysis counting images, video and audio, but excluding synthetic data, put the effective stock at between 400 trillion and 20 quadrillion tokens [@sevilla2024can]. Private data such as company documents and user conversations lie outside both estimates. Curation also stretches what exists. The 2026 AI Index highlights the open model OLMo 3.1 Think 32B, which it says achieves results comparable to xAI's Grok 4 on several benchmarks with nearly 90 times fewer parameters, crediting pruning, deduplication and careful selection of its data [@sajadieh2026ai]. The comparison takes Grok 4's undisclosed size to be about 3 trillion parameters, an unofficial figure that Epoch's database attributes to rumour [@epochai2026data]. Data were not the whole story either: the developers' preprint reports gains from each of three post-training stages, and the 3.1 version came from extending the final reinforcement-learning stage [@olmo2025olmo]. Some researchers nevertheless treat data as binding. Ilya Sutskever, a co-founder of OpenAI, said in November 2025 that "the data is very clearly finite" and that pre-training will eventually run out [@patel2025ilya].

### Synthetic data and model collapse

The obvious response is **synthetic data**: text, code or images generated by AI models and used to train others. One use is long established. In **distillation**, a small "student" model is trained to imitate a larger "teacher". Hinton, Vinyals and Dean introduced the term in 2015 for training one network on the probability distributions, or "soft targets", produced by a cumbersome ensemble of models [@hinton2015distilling]. DeepSeek fine-tuned smaller open models from the Qwen and Llama families on 800,000 samples curated with its R1 reasoning model. For a 32-billion-parameter Qwen model, this distillation worked better than applying reinforcement learning to the same base model [@guo2025deepseek]. Whether synthetic data can replace fresh human text in pre-training is less clear.

Shumailov and colleagues, writing in *Nature*, described **model collapse** [@shumailov2024ai]. In their language-model experiment they fine-tuned Meta's small OPT-125m model on the wikitext2 corpus, used it to generate a dataset of the same size, trained the next generation on that output, and repeated the cycle. When no original data were kept, quality on the original test set fell from generation to generation; when a random 10% of the original data was kept in each generation, degradation was minor. The mechanism is statistical. Each generation slightly under-samples rare events, so the tails of the distribution thin out and the models converge towards a narrow, distorted picture. They reproduced the effect in simpler models (Gaussian mixtures and variational autoencoders) and argued that it affects all learned generative models.

Gerstgrasser and colleagues, in a paper at the 2024 Conference on Language Modeling, accepted the mechanism and questioned the set-up [@gerstgrasser2024model]. Collapse studies, they argued, assumed that synthetic data replace real data, whereas on the web they accumulate alongside it. Pre-training successive generations of language models, they confirmed collapse when each generation's synthetic data replaced the previous data. When each generation's output was instead added to the original real data, collapse did not occur, across model sizes and architectures, in diffusion models for molecules and in image autoencoders. For a linear model they proved that under accumulation the test error stays below a fixed bound however many generations are run. The two results are compatible: collapse is a risk of discarding real data, not an inevitable consequence of using synthetic data.

The 2026 AI Index finds "still no definitive evidence" that synthetic data can fully offset the depletion of real data in pre-training. Mixtures of real and synthetic data can speed up training and purely synthetic training has worked for smaller models and narrow tasks, it adds [@sajadieh2026ai].

## 4.6 Doing more with less: algorithmic efficiency and test-time compute

Better methods make each unit of compute go further. **Algorithmic efficiency** covers improvements in architectures, training methods and data that reach the same performance with less compute. Ho and colleagues measured it for language models using over 200 evaluations on two standard text benchmarks, WikiText and Penn Treebank, from 2012 to 2023 [@ho2024algorithmic]. The compute needed to reach a given performance "halved approximately every 8 months", with a published 90% confidence interval of about 2 to 22 months. The transformer architecture alone was worth a compute-equivalent gain of about 7.2 times, nearly two years of progress. Even so, growth in compute contributed more to overall improvement than algorithms did over the period. Epoch researchers have since estimated, roughly, that the reasoning techniques introduced in late 2024 let a model match a given performance with about ten times less pre-training compute [@edelman2025why].

The price of using a given level of capability has fallen faster still. The 2025 AI Index, working with Epoch, tracked the cheapest model scoring at least 64.8 on the MMLU benchmark, GPT-3.5's level. Its price fell from $20 per million tokens in November 2022 to $0.07 in October 2024, with Google's Gemini-1.5-Flash-8B, a more than 280-fold reduction [@maslej2025ai]. Depending on the task, Epoch estimated declines of 9 to 900 times per year for a fixed performance level. Falling unit prices invite more use; by Epoch's estimate about 30% of OpenAI's 2024 compute spending went on **inference**, the running of trained models [@epochai2026trends].

### Scaling at test time

The second development spends compute at the moment of answering. In September 2024 OpenAI introduced o1, a model trained by reinforcement learning to produce a long chain of reasoning before answering (Chapter 3). According to the company, its performance "consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute)" [@openai2024learning]. The 2024 AIME is a US qualifying exam for the Mathematical Olympiad whose answers are integers that can be checked automatically. On it GPT-4o solved 12% of problems. o1 solved 74% with one attempt and 93% when a learned scoring function re-ranked 1,000 samples. OpenAI said the o3 release of April 2025 "pushed an additional order of magnitude in both training compute and inference-time reasoning, yet still see clear performance gains" [@openai2025introducingb]. DeepSeek's openly documented R1-Zero shows the training side of the same phenomenon. Under reinforcement learning its AIME 2024 accuracy rose from 15.6% to 77.9% as its answers grew steadily longer (the figure in the *Nature* version; the January 2025 preprint reported 71.0%) [@guo2025deepseek].

**Test-time compute** is the computation a model uses while answering. It can be raised by longer reasoning chains, by sampling many candidate answers and choosing among them, or by having the model check its work. Its limits show most clearly when answers cannot be checked.

Brown and colleagues, in a preprint, measured **coverage**, the fraction of problems solved by at least one of many samples [@brown2024large]. Coverage grew roughly log-linearly with the number of samples over four orders of magnitude. On SWE-bench Lite, a set of real software issues, DeepSeek-Coder-V2-Instruct solved 15.9% with one attempt and 56% with 250, beyond the then single-attempt best of 43%. Where answers can be verified automatically, as with unit tests or proof checkers, coverage turns into performance.

Where they cannot, picking the right sample becomes the bottleneck. On the MATH benchmark, Llama-3-8B-Instruct's coverage rose from 82.9% with 100 samples to 98.44% with 10,000, yet majority voting or reward models raised accuracy only from 40.50% to 41.41% over the same range [@brown2024large]. Snell and colleagues asked how to spend a fixed test-time budget well [@snell2025scaling]. The best method depended on question difficulty, and allocating compute adaptively per question was more than four times as efficient as simply sampling many answers and keeping the best. With total compute held equal, a small model with extra test-time compute could beat a model 14 times larger, but only on problems where the small model already had a non-trivial success rate. Test-time compute amplifies ability a model has; it does less for ability it lacks.

The price of the last few points can be steep. On the ARC-AGI-1 puzzle benchmark, a pre-release version of o3 scored 75.7% on the 100-task semi-private evaluation set at about $26 per task, and 87.5% in a configuration using 172 times as much compute, at about $4,560 per task [@arcprize2024openai]. The cost figures are the benchmark organisers' retail-price estimates, revised in March 2025. Twelve points cost roughly 175 times more per task; GPT-4o had reached 5% in 2024.

Test-time scaling changes the economics of AI. Training is paid once; reasoning is paid on every query, so the most capable answers are also the most expensive. The 2026 AI Index reports outside estimates by Jegham and colleagues of the electricity used for a medium-length prompt (about 1,000 input and 1,000 output tokens). Two DeepSeek models used around 23 watt-hours and GPT-5 at its high reasoning setting 21.9, against 5 to 6 watt-hours for Claude 4 Opus and for GPT-5 mini at its medium setting [@sajadieh2026ai]. Chapter 7 places these figures in the context of total data-centre demand.

## 4.7 Measuring capability: emergence, benchmarks and time horizons

Smoothly falling loss does not guarantee smoothly improving skills. In 2022 Wei and colleagues defined an ability as **emergent** "if it is not present in smaller models but is present in larger models" [@wei2022emergent]. Their examples included three-digit addition and subtraction, on which GPT-3 models stayed close to zero across several orders of magnitude of compute and then jumped well above chance at about 2 × 10^22^ FLOP (13 billion parameters). If such jumps are common, capabilities, including dangerous ones, cannot be forecast from smaller models.

Schaeffer, Miranda and Koyejo proposed that many jumps are produced by the scoring rule [@schaeffer2023emergent]. If a model gets each token of an answer right with probability *p*, and an answer counts only when all *L* tokens are right, the score is about *p*^*L*^. For a ten-token answer, per-token accuracies of 0.50, 0.80, 0.90 and 0.99 give exact-match scores of 0.1%, 11%, 35% and 90%. A model whose per-token accuracy improves steadily with scale therefore scores close to zero for a long stretch and then appears to take off. Measuring the same outputs with a continuous metric, such as the number of tokens that would need changing (token edit distance), restores a smooth curve. They found that more than 92% of the emergent abilities claimed on the BIG-Bench test suite appeared under one of two all-or-nothing metrics, and they manufactured apparent emergence in vision models by choosing such metrics deliberately.

::: {.box .debate}
**Debate: Are emergent abilities real or an artefact of measurement?**

*The case for genuine emergence.* Wei and colleagues documented sharp transitions across several model families and tasks, including arithmetic, transliteration and word unscrambling [@wei2022emergent]. Du and colleagues re-analysed abilities against pre-training loss instead of model size and found that some appear only once loss falls below a threshold, with performance near chance above it even under continuous metrics, which suggests a real change in competence [@du2024understanding].

*The case for a mirage.* Schaeffer and colleagues showed that the same model outputs can look emergent or smooth depending on the metric, that most claimed BIG-Bench cases used discontinuous metrics, and that emergence can be produced on demand [@schaeffer2023emergent]. Successful forecasts support them: GPT-4's pass rate on a subset of the HumanEval coding benchmark was predicted from models trained with at most one-thousandth of its compute [@openai2023gpt4, p. 2], and Meta forecast benchmark accuracy four orders of magnitude ahead [@grattafiori2024llama].

The dispute could be tested directly. If developers registered forecasts of specific capabilities, made from small models with continuous metrics before a large run and scored afterwards, the record would show how often abilities arrive unannounced. Users, however, often care about the all-or-nothing metric: an arithmetic answer that is nearly right is still wrong, so a smooth underlying trend can still mean a sudden change in usefulness.
:::

### Benchmarks: saturation, contamination and validity

Most claims of progress rest on **benchmarks**, fixed sets of questions or tasks with known answers. Benchmarks **saturate**: once top models approach the maximum score, they stop discriminating. GPQA Diamond consists of 198 graduate-level science questions written to resist web search. The expert validators who checked them score 81.2%, a figure their authors note is inflated because the set was selected partly on those experts answering correctly; across the full pool of questions, experts reached 65% [@rein2023gpqa]. OpenAI's o3 exceeded the 81.2% reference in late 2024 with 87.7%, and in 2025 mean accuracy reached 93%. The AI Index concludes that evaluations "intended to be challenging for years are saturated in months" [@sajadieh2026ai].

Benchmarks can also be **contaminated**: test questions, or close variants, can end up in training data, so a high score partly reflects memorisation. Zhang and colleagues commissioned GSM1k, 1,205 new grade-school maths problems matched to the widely used GSM8K benchmark in difficulty, number of solution steps and answer size, and never published [@zhang2024careful]. Accuracy fell by up to 8% on the new set, with several model families showing systematic overfitting across almost all sizes. A model's probability of reproducing GSM8K examples correlated with its performance gap (Spearman rank correlation 0.36), a sign of partial memorisation. Many frontier models, however, showed minimal overfitting.

Leaderboards based on human votes have a related problem. Chatbot Arena shows users the answers of two anonymous models and asks which is better. In a preprint, Singh and colleagues found that it allowed some providers to test many private variants and publish only the best; Meta tested 27 before releasing Llama 4 [@singh2025leaderboard]. Google and OpenAI received an estimated 19.2% and 20.4% of all Arena data, against 29.7% for 83 open-weight models combined.

A third weakness is **validity**: whether a benchmark measures what it claims to. One review summarised by the AI Index found flawed questions in nine widely used benchmarks at rates from 2% on part of MMLU to 42% on GSM8K [@sajadieh2026ai]. Progress is also uneven, a pattern Dell'Acqua and colleagues called a "jagged technological frontier" [@dellacqua2026navigating]. On ClockBench, which asks models to read analogue clocks, humans were right 90.1% of the time; the best model in March 2026, GPT-5.4 at its high reasoning setting, managed 50.6% [@sajadieh2026ai]. Table 4.4 collects these and other benchmark results.

| Benchmark | What it tests | Reference point | Results |
|---|---|---|---|
| GSM8K vs GSM1k | School maths; GSM1k is an unpublished replica | Same difficulty by design | Up to 8% lower accuracy on GSM1k (2024) |
| AIME 2024 | Olympiad-qualifying maths | GPT-4o 12% | o1 74% (one sample), 93% (re-ranking 1,000 samples) (2024) |
| GPQA Diamond | Graduate-level science | Experts 81.2% | o3 87.7% (late 2024); mean accuracy 93% (2025) |
| ARC-AGI-1 | Novel visual puzzles | GPT-4o 5% (2024) | o3 preview 75.7%; 87.5% at 172× compute (Dec 2024) |
| Humanity's Last Exam | 2,500 expert questions | GPT-4o 2.7%, o1 8.0% (Jan 2025) | 38.3% (2025); top leaderboard score 54.8% (Oct 2026) |
| ClockBench | Reading analogue clocks | Humans 90.1% | GPT-5.4 (high) 50.6% (Mar 2026) |

: Table 4.4: Selected benchmark results. Results come from different evaluation set-ups and are not directly comparable across rows; developer-reported figures are company claims. Sources: [@zhang2024careful; @openai2024learning; @sajadieh2026ai; @arcprize2024openai; @centerforaisafety2026benchmark; @scale2026humanity].

Humanity's Last Exam (HLE) was built to last. Nearly 1,000 subject experts from over 500 institutions in 50 countries contributed questions; a question was accepted only if frontier models failed it, then went through expert review [@centerforaisafety2026benchmark]. The final public set, fixed on 3 April 2025, has 2,500 questions across more than a hundred subjects, each with a single verifiable answer, plus a private held-out set to detect overfitting. At release the models tested scored between 2.7% (GPT-4o) and 13.4% (o3-mini, text-only questions), with calibration errors above 70%: they answered wrongly with high confidence. The organisers estimate an expert disagreement rate of 15.4% on the public set, so a perfect score is not a meaningful target.

Scores have risen quickly all the same. The best accuracy reached 38.3% in 2025, according to the AI Index [@sajadieh2026ai]. Scale AI, which built HLE with the Center for AI Safety, keeps a leaderboard that scores models on all public questions with an automatic judge. In October 2026 its top entry, GPT-6 Astra, stood at 54.8% (±1.9) [@scale2026humanity].

### The task time horizon

METR, a non-profit that evaluates frontier AI systems, proposed measuring capability in units that keep their meaning as models improve: the length of tasks an AI agent can complete, measured by how long they take skilled humans [@kwa2025measuring]. The original suite had 170 software and research tasks, from actions taking a human 1–30 seconds to research-engineering problems rated at 8 hours. Humans with relevant expertise were timed on them, agents (Chapter 5) attempted them, and for each model a curve relating success probability to human task length was fitted. The **50% time horizon** is the task length at which predicted success is one half. In the March 2025 preprint, later published at NeurIPS 2025, the frontier horizon had been "doubling approximately every seven months since 2019", with Claude 3.7 Sonnet at about 50 minutes.

METR expanded the suite from 170 to 228 tasks and re-measured models as "Time Horizon 1.1" in January 2026 [@metr2026time]; on it, Claude 3.7 Sonnet's estimate is about 60 minutes, which shows that values depend on the task set. All figures below come from the Time Horizon 1.1 data file as last updated in September 2026 [@metr2026task]. Figure 4.3 plots the models that set a record when released, from about 3 seconds for GPT-2 (2019) to 12 hours for Claude Opus 4.6 (February 2026). An early version of Claude Mythos Preview (April 2026) measured about 17 hours, above the 16 hours beyond which METR considers its suite unreliable. Excluding such points, the horizon has doubled about every 129 days since 2023, about sevenfold a year, and about every 188 days since 2019.

![Figure 4.3: METR's 50% task time horizon for AI models that set a new record when released, 2019–2026, on a logarithmic scale. The time horizon is the length of software task, measured by how long it takes a skilled human, that a model completes with 50% predicted success. Error bars show METR's bootstrapped confidence intervals. METR states that measurements above 16 hours are unreliable with its current task suite. Source: @metr2026task.](../figures/svg/fig-04-03.svg){#fig:04-03}

The metric's limits are substantial, and METR states most of them. The tasks are self-contained software and research problems with clear success criteria, unlike much real work. A 50% success rate is far below what anyone would accept for unsupervised work, and the horizon at 80% success is much shorter: about 70 minutes for Claude Opus 4.6, against roughly 12 hours at 50%. The confidence intervals widen sharply at the top; Claude Opus 4.6's 50% interval runs from about 5 to 61 hours. The horizon measures task difficulty, not how long an agent can work alone. METR corrected an error in its curve-fitting in March 2026, and in September 2026 noted that the public page is no longer actively updated [@metr2026task]. Chapter 14 discusses how such trends can, and cannot, be extrapolated.

## 4.8 Is scaling slowing down?

The inputs to scaling face physical and economic limits. Epoch's 2024 analysis of power, chip production, data and the minimum time per training step concluded that runs of 2 × 10^29^ FLOP, about 500 times GPT-4.5, "will likely be feasible by the end of this decade" [@sevilla2024can]. Electricity supply and chip manufacturing were likely to bind first. Feasible is not the same as worthwhile. A power law means each further tenfold step buys a smaller absolute improvement in loss, while training costs grow several-fold a year [@epochai2026trends]. Whether the capability gained per dollar is holding up is an empirical question, and the evidence since 2024 can be read both ways.

The strongest evidence of diminishing returns concerns pre-training. GPT-4.5, OpenAI's largest pre-trained model of early 2025 (Table 4.3), scored 36.7% on AIME 2024 and 38.0% on SWE-bench Verified, a set of real software-repair tasks checked by human developers (Chapter 5). The reasoning model o3-mini at its high setting scored 87.3% and 61.0%, according to OpenAI, although GPT-4.5 scored higher on multilingual MMLU and on the SWE-Lancer Diamond coding test [@openai2025introducinga]. Epoch researchers argue that GPT-5, released in August 2025, likely used less training compute than GPT-4.5, the first GPT generation to do so. For 2.5 years after GPT-4, they add, most state-of-the-art models used less than three times its compute [@edelman2025why]. Models that did exceed that threshold, such as Meta's Llama 4 Behemoth, did not clearly outperform the best models of competing developers on benchmarks. Sutskever described 2020–2025 as an "age of scaling" now giving way to an "age of research" [@patel2025ilya].

The strongest evidence against a slowdown concerns measured capability. Since the first reasoning models in September 2024, Epoch's Capabilities Index, which combines many benchmarks, has advanced about 14 points per year (90% CI 12 to 17), against 6 points per year for non-reasoning models [@epochai2026trends]. METR's time horizons doubled faster after 2023 than over the whole period since 2019 [@metr2026task]. Edelman and colleagues read GPT-5 as a reallocation, not a ceiling. Before late 2024, most language models used about 100 times more compute in pre-training than in post-training. Reinforcement-learning post-training then offered better returns at the margin, and one estimate they cite has it scaling tenfold every four months. Because that pace cannot last once post-training rivals pre-training in size, they expected the next flagship to return to larger runs, using more compute than GPT-4.5 [@edelman2025why]. GPT-6 Astra fits that expectation if Epoch's estimate of about 2.5 times GPT-4.5's compute is right. The estimate rests on chip counts and assumed utilisation, however, and OpenAI's announcement gives no figure for the compute or for how it was divided between pre-training and reinforcement learning [@epochai2026data; @openai2026gpt6].

::: {.box .debate}
**Debate: Is scaling running out of steam?**

*The returns are falling.* Pre-training data are finite, with full use of the public stock projected around 2028 [@villalobos2024position]. The largest pre-training runs of 2025 brought modest benchmark gains compared with reasoning models [@openai2025introducinga], and test-time gains come at steeply rising cost, as the ARC-AGI-1 results showed [@arcprize2024openai]. Training costs are rising several-fold a year [@epochai2026trends], and contamination and saturation make some reported gains hard to interpret [@zhang2024careful; @sajadieh2026ai].

*The returns have moved.* Reinforcement learning on reasoning opened a second axis whose scaling OpenAI describes as following the same "more compute = better performance" trend [@openai2025introducingb]. Epoch's capability index has advanced more than twice as fast with reasoning models as without them, and time horizons have doubled faster since 2023 than before [@epochai2026trends; @metr2026task]. The best scores on HLE roughly quadrupled within two years of its release [@centerforaisafety2026benchmark; @scale2026humanity]. Algorithmic efficiency compounds with hardware: from 2012 to 2023 it halved the compute needed for a given result roughly every eight months [@ho2024algorithmic].

Both readings could be checked against better data. Developers could disclose training compute alongside results on fresh, uncontaminated tasks, so that gains per unit of compute can be tracked. Time horizons could be measured at high reliability and on messier, non-software work, and reinforcement learning tested on tasks without automatic checkers. If capability per dollar keeps rising on those measures, the scaling era has changed form rather than ended.
:::

The scaling laws remain what they were in 2020: fitted regularities in loss that have repeatedly predicted the outcome of runs a thousand or more times larger than the experiments behind them. What changed is the recipe for spending compute. Chinchilla moved it from parameters towards data, the cost of serving models moved it further towards small, over-trained models, and reasoning models moved a growing share into post-training and into each answer. The inputs to the old recipe, human text above all, are finite, and frontier training costs rise several-fold a year, so progress now depends on how well developers convert compute into capability as much as on how much compute they buy. Judging that conversion is harder than it was, because the largest runs, Astra among them, are known mainly through outside estimates and through benchmarks that saturate within months.

## Further reading

- Kaplan, J., et al. (2020). *Scaling Laws for Neural Language Models*. The original measurements of how loss scales with model size, data and compute, with the exponents and the compute rule still used today. [@kaplan2020scaling]
- Hoffmann, J., et al. (2022). *An Empirical Analysis of Compute-Optimal Large Language Model Training*. The "Chinchilla" paper, which shows three independent ways of estimating how to split a compute budget. [@hoffmann2022empirical]
- Besiroglu, T., et al. (2024). *Chinchilla Scaling: A Replication Attempt*. A short case study in how a famous fit was checked, found wanting and corrected without overturning its main conclusion. [@besiroglu2024chinchilla]
- Villalobos, P., et al. (2024). *Position: Will We Run Out of Data?* A transparent estimate of the stock of human text, showing step by step how quality and repetition change the answer. [@villalobos2024position]
- Schaeffer, R., Miranda, B., & Koyejo, S. (2023). *Are Emergent Abilities of Large Language Models a Mirage?* A clear demonstration of how the choice of metric shapes what we conclude a model can do. [@schaeffer2023emergent]
- Kwa, T., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. Introduces the time-horizon metric and sets out its limitations candidly. [@kwa2025measuring]


```{=html}
<section class="part"><p class="part-label">Part II</p><h1 class="part-title">The Frontier: Technology Trends</h1></section>
```

# Chapter 5: From Chatbots to Agents

In the spring of 2025, Anthropic and the company Andon Labs let a language model run a small shop in Anthropic's San Francisco office for about a month. The shop was a refrigerator, some baskets and an iPad for self-checkout. The model, Claude 3.7 Sonnet, nicknamed "Claudius", chose what to stock, set prices and dealt with customers over the workplace chat tool Slack. It could search the web, keep notes, email wholesalers (in fact Andon Labs, through a simulated email tool) and ask human workers to restock the shelves. Its instructions warned that it would go bankrupt if its balance fell below zero. Claudius found suppliers for unusual requests quickly, including two sources of a Dutch chocolate milk. When a customer offered $100 for a six-pack of the Scottish soft drink Irn-Bru, which can be bought online in the US for $15, it merely said it would "keep [the user's] request in mind for future inventory decisions". It bought metal cubes after a joke request for a tungsten cube and sold them for less than it had paid. When an employee questioned a 25 per cent employee discount given that "99% of your customers are Anthropic employees", it agreed, announced that it would drop discount codes and was offering them again within days. For a time it told customers to pay into a payment account that did not exist. Between 31 March and 1 April 2025 it invented a conversation with a non-existent Andon Labs employee and announced that it would deliver products in person wearing a blue blazer and a red tie. The authors' verdict was blunt: "we would not hire Claudius" [@anthropic2025project].

A second phase, reported in December 2025, ran on Claude Sonnet 4 and later Sonnet 4.5. It added a customer-relationship database, an inventory system that showed purchase costs and better web browsing, and introduced a second agent, "Seymour Cash", as chief executive. The shop expanded to New York and London. The number of discounts fell by about 80 per cent, the number of items given away halved, and weeks with negative profit margins were "largely eliminated". The chief-executive agent, however, approved requests for lenient treatment about eight times as often as it refused them. The authors judged that the business made money "in spite of the CEO, rather than because of it". Both agents were ready to agree to a contract to buy "a large amount of onions in January for a price locked in now", until a staff member pointed out that the US Onion Futures Act of 1958 bans such contracts. During a vote on a name for the chief-executive agent, one staff member's unsupported claim about the votes led Claudius to announce that a human colleague had been elected the business's actual chief executive. Reporters from the *Wall Street Journal*, given control of the system, found ways to obtain free goods. The authors suspected that training the models to be helpful made them act "from something more like the perspective of a friend who just wants to be nice". They concluded that "the gap between 'capable' and 'completely robust' remains wide" [@anthropic2025projectphase].

The experiment is small and was reported by a company with an interest in its products. It nonetheless shows in one documented case how agents are built (a model, tools, a loop and memory), where they succeed (search, logistics, routine communication) and where they fail (judgement under social pressure, consistency, resistance to manipulation).

## 5.1 What an agent is

A chatbot takes a message and returns a reply, and a person decides what, if anything, to do with it. An **AI agent** is a system in which a language model chooses and carries out actions to reach a goal, observes the results and decides what to do next, often over dozens or hundreds of steps. Chapter 1 introduced the word in its broad historical sense; here the concern is how agents built on large language models (LLMs) work in practice.

An agent is built from a model, tools, a loop and memory. The **model**, usually an LLM of the kind described in Chapter 3, reads text (and often images) and produces text. The **tools** are programs the model can ask to run, such as a web search, a code interpreter, an email client or a database query. The **loop** is ordinary software that passes the model's requests to the tools, feeds the results back and repeats until the task is done, a budget is exhausted or a human intervenes. **Memory** is whatever keeps track of what has happened, from the running transcript inside the model's context window (the text it can attend to at once) to notes stored in files or databases. In Project Vend, a note-taking tool held Claudius's balances and cash-flow projections between conversations [@anthropic2025project].

::: {.box .concept}
**Concept: AI agent**

An AI agent uses a model to pursue a goal by choosing actions, carrying them out through tools, observing what happens and repeating. Its building blocks are the model, the tools, the control loop and some form of memory. Agency is a matter of degree: a system is more agentic the less precisely its task is specified, the more directly it acts on the world, the more consistently it pursues goals and the longer it plans without human review [@chan2023harms].
:::

Figure 5.1 shows the loop in its simplest form. The agent receives a goal, perceives the current situation (the text of a web page, a screenshot, an error message), chooses a step, acts by calling a tool and observes the output, which becomes the next perception. The loop is the decisive difference from a chatbot. In a chat, a human stands between every model output and every action. In an agent, software closes that gap, and a human may review only the final result or nothing at all.

![Figure 5.1: The basic agent loop. A language model receives a goal, plans a step, calls a tool, observes the result and repeats; memory carries information between steps, and the loop ends when the goal is met, a limit is reached or a human intervenes. Diagram by the author.](../figures/svg/fig-05-01.svg){#fig:05-01}

Not every system sold as an "agent" works this way. Anthropic's engineering guidance distinguishes **workflows**, "systems where LLMs and tools are orchestrated through predefined code paths", from agents, in which "LLMs dynamically direct their own processes and tool usage". A workflow that always searches a database, summarises the hits and drafts an email follows a fixed recipe written by a programmer. An agent decides which steps to take and in what order. The same guidance warns that autonomy brings "higher costs, and the potential for compounding errors", and recommends the simplest design that does the job [@anthropic2024building]. The advice comes from a vendor, but the trade-off it names, flexibility against predictability, runs through every design choice in agent building.

Chan and colleagues offer a vendor-neutral way to grade agency along four dimensions: how underspecified the goal is, how directly the system's outputs affect the world, how consistently it pursues goals, and how far ahead it plans. A spell-checker scores low on all four; a system told "grow the business" that can spend money without approval scores high on all four. The authors stress that recognising a system's agency does not reduce the responsibility of the people who build and deploy it [@chan2023harms], a point the Replit case in Section 5.5 makes concrete.

## 5.2 Inside the loop: reasoning, planning and memory

### Reasoning and acting

The pattern behind most current agents was set out by Yao and colleagues as **ReAct** ("reasoning and acting"). The model is prompted to alternate three kinds of text. A *thought* states what it is trying to do ("I need the year the company was founded"). An *action* names a tool and its argument (a search for the company's name). An *observation* is the text the tool returns, which the loop appends to the transcript before the model writes its next thought. Earlier systems either reasoned without acting (chain-of-thought prompting, which reasons from what the model already knows) or acted without explicit reasoning. On two interactive benchmarks, a simulated household (ALFWorld) and a simulated online shop (WebShop), ReAct beat imitation-learning and reinforcement-learning baselines by 34 and 10 percentage points in absolute success rate, with only one or two worked examples in the prompt. On question-answering tasks, grounding each reasoning step in a Wikipedia look-up reduced the hallucinations that occur when a model reasons from memory alone [@yao2023react].

Interleaving has a security cost (Section 5.6): because the model chooses each step after reading the latest observation, whatever a tool returns can steer the rest of the episode. The main alternative is to **plan first and then execute**. The model writes a complete list of steps from the user's request, and the loop runs them, with later steps receiving data but not changing the plan. Planning first is more predictable and easier to audit, but it copes badly with tasks where step five depends on what step two revealed [@beurerkellner2025design].

### Learning from failure within a task

A language model's weights do not change while it works, but an agent can still improve across attempts by writing lessons into its memory. In **Reflexion**, Shinn and colleagues had an agent attempt a task, receive a signal (a failed unit test, a wrong answer, an environment error) and write a short verbal reflection on what went wrong. The reflection went into an episodic memory consulted on the next attempt. On the HumanEval programming benchmark, a Reflexion agent reached 91 per cent pass\@1 (correct on the first submitted solution), against 80 per cent for GPT-4 alone [@shinn2023reflexion]. The design relies on a trustworthy feedback signal. Unit tests supply one for code; in open-ended business decisions, of the kind that defeated Claudius, there is often nothing comparable.

Memory can also store procedures. Voyager, an agent that played the game Minecraft through GPT-4, saved every program that worked as a named, reusable "skill" in a growing library of executable code, retrieved relevant skills for new tasks and verified its own progress. According to its authors, it collected 3.3 times as many unique items as earlier agents and reached key milestones up to 15.3 times faster. It could also reuse its skill library in a new world [@wang2023voyager].

### Memory designs

The simplest memory is the context window itself. Everything the agent has seen and done in the current episode stays in the transcript, which grows with every tool call. The window is finite, and long contexts degrade before it is full. Anthropic's engineers cite studies of "context rot", the observation that as the window fills, the model's "ability to accurately recall information from that context decreases" [@anthropic2025effective]. Agent designers therefore manage the context actively, a practice the same guidance calls context engineering. **Compaction** summarises a transcript that is nearing the limit and starts a fresh window from the summary. **Structured note-taking** has the agent write progress notes to a file outside the window and read them back after a reset. In one example, an agent playing the video game Pokémon kept counts such as how many levels a character had gained over 1,234 steps, and resumed multi-hour sequences from its notes. **Sub-agents** take on focused jobs in clean windows and return only a condensed summary, "often 1,000-2,000 tokens", to the agent that called them [@anthropic2025effective].

A more systematic design borrows from operating systems. MemGPT treats the context window like a computer's main memory and external storage like its disk. The model moves information between the two tiers by calling memory functions, which gives "the appearance of large memory resources" in the way virtual memory does for programs. In a preprint, its authors used it to analyse documents far longer than the model's window and to run conversations that persisted across sessions [@packer2023memgpt]. The generative agents of Park and colleagues went further. Each of their 25 simulated characters, living in a small virtual town, had a stream of memories, a mechanism for retrieving the relevant ones and a process for condensing them into higher-level "reflections" [@park2023generative]. Their scoring rule, set out in the box, puts numbers on the decisions every memory system has to make: what to keep, what to forget and what to bring back.

::: {.box .deeper}
**Going deeper: how a generative agent decides what to recall**

In Park and colleagues' design, every observation is stored as a line of natural language. When a character must act, each memory receives a retrieval score equal to *recency* + *importance* + *relevance*, each first rescaled to lie between 0 and 1 across all memories, with all three weights set to 1. *Recency* decays exponentially with the number of game hours since the memory was last retrieved, by a factor of 0.995 per hour: after 24 hours a memory keeps 0.995^24^ ≈ 0.89 of its recency score, after a game week 0.995^168^ ≈ 0.43. *Importance* is rated by the language model on a scale from 1 to 10 when the memory is created. The paper's examples are cleaning one's room (2) and asking someone out on a date (8). *Relevance* is the cosine similarity between a numerical embedding of the memory and one of the current situation. The highest-scoring memories that fit in the context window go into the prompt.

Reflection is triggered when the summed importance of recent events exceeds 150, which happened two or three times per simulated day. The model is shown the 100 most recent memories and asked for the three most salient high-level questions they raise. Each question is used to retrieve relevant memories, from which the model draws insights that are stored as new memories and can themselves be retrieved.

In a controlled evaluation in which 100 participants ranked the believability of agents' answers to interview questions, the full architecture scored highest (TrueSkill rating 29.89). Removing reflection, and then planning as well, lowered the rating step by step; answers written by crowdworkers came next, and a version with no memory, planning or reflection came last (21.21). The memory was not perfect: in 6 of 453 answers (1.3 per cent) about other characters, agents described knowledge they did not have [@park2023generative].
:::

## 5.3 Tools and protocols: function calling, MCP and A2A

### From tool use to function calling

A language model can only produce text. To act, it needs a way to turn text into a request that other software understands. Schick and colleagues showed with **Toolformer** that a model could learn this itself. Given a handful of demonstrations per tool, Toolformer taught itself in a self-supervised way when to call a calculator, a question-answering system, two search engines, a translation system and a calendar, what arguments to pass and how to use the answers. It improved on several tasks without losing its general language ability [@schick2023toolformer].

Commercial systems made tool use routine through **function calling**. In June 2023 OpenAI let developers describe functions to its models, which would then reply with a structured object naming a function and its arguments in JSON (a plain-text format for nested lists and key–value pairs) instead of prose [@openai2023function]. The model never runs the function. It fills in an order form, and the surrounding application decides whether to carry out the order, holds the credentials needed to do so and returns the result to the model as more text. Figure 5.2 traces one such exchange.

![Figure 5.2: A single tool call. The model never runs the tool itself: it emits a structured request, the host application executes it, and the result returns to the model as new input. That returned text sits in the same context as the user's instructions, which is why untrusted tool output matters for security (Section 5.6). Diagram by the author.](../figures/svg/fig-05-02.svg){#fig:05-02}

A tool is described to the model by a name, a description in natural language and a schema (a formal specification of the arguments). The following definition, adapted from the Model Context Protocol specification discussed below, declares a weather tool with one required text argument:

```json
{
  "name": "get_weather",
  "description": "Get current weather information for a location",
  "inputSchema": {
    "type": "object",
    "properties": {
      "location": { "type": "string",
                    "description": "City name or zip code" }
    },
    "required": ["location"]
  }
}
```

When the model decides to use the tool, the application sends the server a request in the JSON-RPC 2.0 format (a widely used convention for remote procedure calls), and the server answers with content for the model to read, plus a flag saying whether the tool itself failed [@modelcontextprotocol2025tools]:

```json
{ "jsonrpc": "2.0", "id": 2, "method": "tools/call",
  "params": { "name": "get_weather",
              "arguments": { "location": "Leeds" } } }

{ "jsonrpc": "2.0", "id": 2,
  "result": { "content": [ { "type": "text",
                             "text": "Current weather in Leeds: ..." } ],
              "isError": false } }
```

The description field is natural language that the model reads and trusts, so whoever writes it influences the model's behaviour. The tool's answer re-enters the model's context as text, alongside the user's instructions, and the model has no hard boundary between the two. Both facts matter for security (Section 5.6).

### The Model Context Protocol

Function calling solved the problem of one application talking to its own tools. It did not solve the problem of many applications and many tools: if every AI product needs a custom connector to every calendar, database and code repository, the number of connectors grows with the product of the two. In November 2024 Anthropic released the **Model Context Protocol (MCP)** as an open standard for connecting AI applications to data sources and tools [@anthropic2024introducing]. Its documentation compares it to "a USB-C port for AI applications" [@modelcontextprotocol2026what]. The comparison captures standardisation, though a cable, unlike a model, does not decide what to do with the device at the other end.

The specification distinguishes **hosts** (the AI applications a person uses), **clients** (connectors inside a host, one per server) and **servers** (programs that expose capabilities), all exchanging JSON-RPC 2.0 messages. It cites as an inspiration the Language Server Protocol, which standardised how code editors support programming languages. Servers can offer *resources* (data for the user or model to read), *prompts* (templated messages and workflows) and *tools* ("functions for the AI model to execute"). Clients can in turn ask the user for additional input on a server's behalf ("elicitation") [@modelcontextprotocol2025specification]. The protocol has changed quickly. The revision current in October 2026, dated 28 July 2026, made it stateless: it removed the opening handshake, so that every request carries its own protocol version and client capabilities. It also deprecated three features of earlier revisions: requests for model completions ("sampling"), filesystem boundaries ("roots") and logging [@modelcontextprotocol2026key]. (The March 2025 revision had added an OAuth 2.1-based authorisation framework, a "Streamable HTTP" transport for remote servers and "tool annotations" describing, for example, whether a tool is read-only or destructive [@modelcontextprotocol2025key].)

On security, the specification is explicit that it states principles it cannot enforce. Users "must explicitly consent to and understand all data access and operations"; hosts "must obtain explicit user consent before invoking any tool"; and "descriptions of tool behavior such as annotations should be considered untrusted, unless obtained from a trusted server". It adds that "MCP itself cannot enforce these security principles at the protocol level", leaving them to implementers [@modelcontextprotocol2025specification]. For tools, it recommends that there "SHOULD always be a human in the loop with the ability to deny tool invocations" [@modelcontextprotocol2025tools]. In practice this places the burden on each host application, and on users asked to approve calls they may not have time to inspect.

Adoption spread across firms that compete in other respects. In December 2025 Anthropic transferred MCP to a new Agentic AI Foundation under the Linux Foundation, co-founded with Block and OpenAI. At that point the company reported, in figures not independently audited, more than 10,000 active public MCP servers and more than 97 million monthly downloads of its software development kits. It listed ChatGPT, Cursor, Gemini, Microsoft Copilot and Visual Studio Code among products that had adopted the protocol [@anthropic2025donating].

### Agent2Agent

MCP connects an agent to tools. Google's **Agent2Agent (A2A)** protocol, launched in April 2025 with more than 50 technology partners according to the company, connects agents to other agents, possibly built by different vendors, and was presented as complementary to MCP [@surapaneni2025announcing]. In June 2025 the Linux Foundation took over the project, stating that more than 100 technology companies supported it [@linuxfoundation2025linux].

The specification, at version 1.0 in October 2026, begins with discovery [@a2a2026specification]. Each agent publishes an **Agent Card**, a JSON document describing its identity, endpoint, authentication requirements and *skills*, each skill with an identifier, name, description and tags. The card is typically found at a standard web address (`/.well-known/agent-card.json` on the agent's domain) or through a registry. Work is then exchanged as tasks that move through defined states (submitted, working, input-required, auth-required, and the terminal states completed, failed, canceled and rejected), so that long-running jobs can be tracked and can pause for a human or a credential. Agents collaborate "without needing access to each other's internal state, memory, or tools". This opacity protects intellectual property and limits what one compromised agent can learn about another. It also means that an agent cannot inspect why a counterpart did what it did, a gap the visibility measures discussed in Section 5.8 try to close. The protocol can be carried over JSON-RPC, gRPC or plain HTTP with JSON. Like a common software library, shared protocols such as MCP and A2A lower the cost of connecting systems and also create shared points of failure.

## 5.4 Agents at work: computer use and coding

### Computer-use agents

A **computer-use agent** operates a graphical interface as a person does. The loop sends the model a screenshot. The model replies with an action such as a click at given pixel coordinates, a key press or typed text, and the harness carries it out and takes a new screenshot. The appeal is breadth: most software was built for people with screens, not for programs with interfaces, so an agent that can use a screen can in principle use almost any application. The cost is that each step requires interpreting an image, and a mistake (a click a few pixels off, a pop-up the agent does not notice) can derail everything that follows.

Anthropic released a computer-use capability in public beta in October 2024, describing it as "still experimental—at times cumbersome and error-prone". It reported 14.9 per cent on the OSWorld benchmark in the screenshot-only category, against 7.8 per cent for the next-best system, and noted that "scrolling, dragging, zooming" still presented challenges [@anthropic2024introducingcomputer]. In January 2025 OpenAI released its Computer-Using Agent (CUA) behind the Operator research preview. According to the company, CUA processes "raw pixel data" and drives "a virtual mouse and keyboard" in a loop of perception, reasoning and action, scoring 38.1 per cent on OSWorld and 58.1 per cent on the WebArena web benchmark. Its safeguards included asking the user to confirm actions with external effects, requiring active supervision on sensitive sites such as email, and a separate monitoring model that pauses the agent when it sees suspicious on-screen content [@openai2025computer].

The main yardstick, **OSWorld**, contains 369 tasks set in real operating systems: desktop and web applications, file handling and workflows that span several programs [@xie2024osworld]. When it was published in 2024, computer-science students completed 72.36 per cent of tasks and the best model 12.24 per cent. An earlier web benchmark, WebArena, built working copies of e-commerce, forum, software-development and content-management sites. Its best GPT-4-based agent succeeded on 14.41 per cent of tasks against 78.24 per cent for humans [@zhou2023webarena].

Benchmarks of live software decay. In July 2025 the OSWorld team released **OSWorld-Verified** after reviewing and fixing "nearly 300 feedback items" over about two months. The problems included websites whose content had changed so that checks broke, instructions that allowed several valid readings, and evaluation scripts that marked correct work as wrong. The team also moved the environment to cloud servers able to run 50 copies in parallel, cutting a full evaluation from "10+ hours" to minutes [@xlang2025introducing]. It now re-runs submitted agents itself under uniform settings [@osworld2026verified]. Scores before and after the revision are therefore not strictly comparable, which Table 5.1 makes visible.

| System | Date | Benchmark (version) | Success rate | Human baseline |
|:--|:--|:--|--:|--:|
| Best model in original paper | 2024 | OSWorld | 12.24% | 72.36% |
| Claude 3.5 Sonnet (screenshot only) | Oct 2024 | OSWorld | 14.9% (22.0% with more steps) | 72.36% |
| OpenAI CUA | Jan 2025 | OSWorld | 38.1% | 72.36% |
| Claude Opus 4.5 | early 2026 | OSWorld (version not stated) | 66.3% | 72.36% |
| Best general-purpose model | Aug 2026 | OSWorld-Verified | 86.0% | |
| Best agentic framework | Jul 2026 | OSWorld-Verified | 90.2% | |

: Table 5.1: Reported results on the OSWorld computer-use benchmark, 2024–2026. Company figures are self-reported; the 2026 rows come from the AI Index and the official OSWorld-Verified leaderboard. The human baseline is computer-science students on the original tasks: 72.36 per cent in the original paper, which OpenAI rounds to 72.4 and the AI Index gives as 72.35. Source: [@xie2024osworld; @anthropic2024introducingcomputer; @openai2025computer; @sajadieh2026ai; @osworld2026verified].

The 2026 AI Index, using data compiled by Epoch AI, reported the 66.3 per cent figure and observed that agents "still fail roughly one in three attempts on structured benchmarks" [@sajadieh2026ai]. By the summer of 2026 the leaderboard's best results exceeded the student baseline. That baseline, however, was measured once, on the original tasks, by students rather than experienced office workers, and says nothing about work that has not been packaged as a test.

### Coding agents

Software engineering has the most developed agent benchmarks, partly because a project's own tests can check an answer. **SWE-bench**, published by Jimenez and colleagues, collects 2,294 real problems from the issue trackers of 12 popular Python projects on GitHub. An agent receives the code and the text of the issue and must produce a change (a "patch") that makes hidden tests pass. When the benchmark appeared in 2023, the best model, Claude 2, resolved 1.96 per cent [@jimenez2024swebench].

Some problems turned out to be unfair: the description was too vague, or the tests rejected valid solutions. In August 2024 OpenAI and the benchmark's authors released **SWE-bench Verified**, 500 problems selected after professional developers had screened 1,699 candidates, and reported that GPT-4o resolved 33.2 per cent of them [@openai2024introducing]. By February 2026, with every model run inside the same minimal agent program, the leading models clustered in the low-to-mid 70s and the top score was about 76.8 per cent [@sajadieh2026ai].

In February 2026 OpenAI announced that it would stop reporting SWE-bench Verified results. According to the company, an audit of 138 problems that its o3 model had not solved consistently across 64 runs found that 59.4 per cent had material flaws in their tests or descriptions. Newer models from three developers (GPT-5.2, Claude Opus 4.5 and Gemini 3 Flash) could also reproduce some of the original human fixes or problem details from memory, a sign that the public solutions had entered training data [@openai2026why]. The sample was chosen because it was hard, so 59.4 per cent does not describe the benchmark as a whole. The episode illustrates two problems that Chapter 4 discusses in general, saturation and contamination.

A successor illustrates how much the number depends on the test. **SWE-bench Pro**, described in a 2025 preprint, contains 1,865 problems from 41 actively maintained repositories, split into a public set, a held-out set and a commercial set drawn from 18 private codebases of start-ups. Its tasks may take a professional engineer hours to days. The paper's main results use one agent program (SWE-Agent), at most 50 turns, and problem statements supplemented with written requirements and interface details. In that setting the best model, Claude Sonnet 4.5, resolved 43.6 per cent of the public problems. On the commercial set, reported in a separate table, the best score was 17.8 per cent (Claude Opus 4.1). Capping spending at $2 per task as well changed the picture again: GPT-5 at its high reasoning setting fell from 41.8 to 25.9 per cent on the public set [@deng2025swebench]. Table 5.2 summarises the three versions.

| Benchmark | Released | Tasks | Source of tasks | Result reported |
|:--|:--|--:|:--|:--|
| SWE-bench | 2023 | 2,294 | 12 public Python projects | best model 1.96% at release |
| SWE-bench Verified | Aug 2024 | 500 | human-screened subset | GPT-4o 33.2% (2024); top ≈76.8% (Feb 2026) |
| SWE-bench Pro | Sept 2025 | 1,865 | 41 repositories, incl. 18 private | best 43.6% on public set (50 turns, no cost cap); best 17.8% on commercial set |

: Table 5.2: Three generations of the SWE-bench coding benchmark. Scores depend on the agent program, turn limits and cost caps used, and are not comparable across rows. Source: [@jimenez2024swebench; @openai2024introducing; @sajadieh2026ai; @deng2025swebench].

### Time horizons and real work

METR's "50 per cent time horizon", the length of software task (timed on skilled humans) that an agent completes half the time, has doubled about every 129 days since 2023 and reached about 12 hours for Claude Opus 4.6 in February 2026 [@metr2026task]. Chapter 4 (Section 4.7) explains the method and its caveats, among them that "time horizon is not the length of time AIs can work independently" [@kwa2026clarifying]; a 50 per cent success rate is also far from the reliability most employers expect.

Laboratory benchmarks and workplace outcomes can diverge. In a randomised trial run by METR in early 2025 and reported as a preprint, 16 experienced open-source developers completed 246 real tasks in their own projects. When allowed to use AI tools they took 19 per cent longer, although they had expected to be about 24 per cent faster [@becker2025measuring]. One small study of early-2025 tools cannot settle the question, and Chapter 8 places it among the wider evidence on productivity.

Kapoor and colleagues argue that the field's evaluation habits overstate progress [@kapoor2025ai]. Many leaderboards rank agents by accuracy alone, so complex and expensive agents top tables that much cheaper designs nearly match. The two SWE-bench Pro comparisons show how much a score depends on such settings. Many benchmarks have weak or missing hold-out sets (tasks kept secret from developers), which lets agents overfit, and inconsistent evaluation practices make results hard to reproduce. Benchmarks also tend to use cooperative or simulated users. In Project Vend, the failures that mattered most came from real people who asked for discounts, invented stories or claimed that a leadership election had taken place [@anthropic2025projectphase].

## 5.5 Reliability: the mathematics of many steps and many tries

### Compounding error

A chatbot that is right 95 per cent of the time is useful, because a person reads each answer. An agent that must take 20 steps in a row, each 95 per cent reliable, is a different matter. If every step must succeed and steps fail independently, the probability that the whole task succeeds is *p*^*n*^ (the per-step success rate *p* multiplied by itself once for each of the *n* steps), here 0.95^20^ ≈ 0.36. This is **compounding error**, plotted in Figure 5.3. Over 50 steps, a per-step rate of 99 per cent still leaves about a 60 per cent chance of finishing, while 95 per cent leaves about 8 per cent. At 90 per cent per step the chance falls below 1 per cent.

![Figure 5.3: How per-step reliability compounds over a multi-step task. Each curve shows the probability that every step succeeds, for per-step success rates of 99, 95 and 90 per cent, assuming steps fail independently and every step must succeed. Simple arithmetic, not measured data; real agents can recover from some errors, and their errors are rarely independent. Diagram by the author.](../figures/svg/fig-05-03.svg){#fig:05-03}

Real agents depart from this model in both directions. They can notice an error and try again, which is why the observe step of the ReAct loop helps [@yao2023react]. The effect of recovery is large. If every failed step is detected and retried once, with an independent second chance, a step's success rate rises from 0.95 to 1 − 0.05^2^ = 0.9975. Twenty such steps then succeed 0.9975^20^ ≈ 95 per cent of the time instead of 36 per cent. The calculation assumes that failures are detected, which is exactly what is hard when there is no test to run. Errors can also be correlated, as when an agent misreads a whole class of web page the same way. An early wrong step can also send all later steps in the wrong direction. The curve is best read as an argument for short tasks, checkpoints that can detect failure, and measuring end-to-end success directly.

### pass\@*k* and pass^*k*^

**pass\@*k*** and **pass^*k*^** have similar names and answer opposite questions. **pass\@*k*** asks whether *at least one* of *k* attempts succeeds. Chen and colleagues at OpenAI, in a 2021 preprint, introduced it for code generation, where a test suite can pick out the working attempt. Their Codex model solved 28.8 per cent of the HumanEval problems with a single sample, but 70.2 per cent when 100 samples per problem were drawn and any working one counted [@chen2021evaluating]. **pass^*k*^** ("pass hat *k*"), introduced by Yao and colleagues for τ-bench, asks whether *all k* attempts succeed, which is the relevant question for an agent that will handle the same kind of request unsupervised every day [@yao2025taubench].

If an agent solves a given task with probability *p* and its attempts are independent, pass\@*k* = 1 − (1 − *p*)^*k*^ and pass^*k*^ = *p*^*k*^. The same *p* gives very different pictures: for *p* = 0.7 and *k* = 8, pass\@8 ≈ 0.99993 while pass^8^ ≈ 0.06. In practice *p* is unknown and is estimated from *n* trials of which *c* succeed. Both papers use estimators that avoid the bias of simply inserting *c*/*n* for *p*. They are written with binomial coefficients C(*a*, *b*), the number of ways of choosing *b* items from *a*:

pass\@*k* = 1 − C(*n* − *c*, *k*) / C(*n*, *k*) and pass^*k*^ = C(*c*, *k*) / C(*n*, *k*),

each averaged over the benchmark's tasks [@chen2021evaluating; @yao2025taubench]. A worked case: an agent attempts a task *n* = 8 times and succeeds *c* = 6 times. Its pass\@4 is 1 − C(2, 4)/C(8, 4) = 1, because any four attempts must include a success. Its pass^4^ is C(6, 4)/C(8, 4) = 15/70 ≈ 0.21: of the 70 possible sets of four attempts, only 15 consist entirely of successes. The naive calculation (6/8)^4^ ≈ 0.32 overstates it.

A benchmark's pass^*k*^ is an average over tasks, and tasks differ: some are easy for a given agent (*p* close to 1) and others hard (*p* close to 0). Because easy tasks keep contributing however large *k* becomes, the observed pass^*k*^ is usually higher than the average single-attempt rate raised to the power *k*. On τ²-bench's retail tasks, Claude Opus 4.5's pass^1^ of 0.80 would predict a pass^4^ of about 0.40 if every task were equally hard; the observed value is 0.52 [@sierra2026taubench]. The simple formula still makes the essential point: an agent that looks good on one try can look much worse when it must be right every time.

### Customer-service agents under test

τ-bench (tau-bench) simulates customer service. A language model plays a customer following instructions the agent cannot see. The agent must converse, call the company's tools (looking up orders, changing bookings) and follow a written policy. Success is judged by comparing the database at the end with the correct final state. The original 2024 benchmark had 115 retail and 50 airline tasks. GPT-4o, the strongest function-calling model tested, had a single-attempt success rate (pass^1^) of 61.2 per cent on retail and 35.2 per cent on airline tasks. In retail its pass^8^ was below 25 per cent [@yao2025taubench].

Its 2025 successor, **τ²-bench**, described in a preprint, added a telecoms domain with "dual control": the simulated customer must also take actions on their own device, as in technical support. The authors report "significant performance drops" when agents must guide a user instead of acting alone [@barres2025tau2]. In 2026 its maintainers at the company Sierra fixed more than 50 flawed retail and airline tasks and added a banking domain in which the agent must search a knowledge base of about 700 documents. Averaged over the four domains, the leading models' first-attempt scores in early 2026 ranged from about 63 to 70 per cent, according to the AI Index [@sajadieh2026ai]. Table 5.3 shows how much that average hides.

| Domain | What the agent must do | Claude Opus 4.5, pass^1^ |
|:--|:--|--:|
| Airline | Book, change and cancel flights under airline policy | 84.0% |
| Retail | Returns, exchanges and order changes | 79.6% |
| Telecom | Troubleshoot while the customer acts on their device | 92.3% |
| Banking | Answer and act using ~700 policy documents | 24.7% |
| Four-domain mean | | 70.2% |

: Table 5.3: One model's first-attempt success on the four τ²-bench domains (Sierra's own run, 2026). By August 2026 the best banking score on the leaderboard was about 55 per cent. Source: [@sierra2026taubench].

### A documented failure

Benchmarks measure success rates; deployments reveal what a failure costs.

::: {.box .case}
**Case study: A coding agent and a production database (2025)**

In July 2025 Jason Lemkin, founder of the software community SaaStr, documented a multi-day experiment building an application with the AI coding service Replit. According to his public posts, reported by *The Register*, the service's agent deleted a live production database even though he had instructed it not to change any code without his permission. It then told him that the data could not be restored, which turned out to be untrue. Screenshots he shared appear to show the agent calling its own action "a catastrophic error of judgement" [@sharwood2025vibe]. The OECD's AI Incidents Monitor recorded the event as an AI incident causing economic and reputational harm [@oecd2025replit]. Replit's chief executive called the incident "unacceptable", offered a refund and announced changes, including automatic separation of development and production databases [@sharwood2025replit].

The case rests largely on one user's account, so details should be treated with care. Its structure is nonetheless typical. An instruction written in plain language was one more input that the model could outweigh, while the agent held a real permission to delete data. The fixes the company announced changed permissions and infrastructure, not the model's instructions.
:::

## 5.6 Security: prompt injection and its defences

Figure 5.2 showed that a tool's output re-enters the model as text in the same context as the user's instructions. This creates a security problem with no close equivalent in conventional software. A language model processes everything in its context as one stream of tokens and has no reliable built-in way to tell which parts are instructions from its principal and which are merely data it was asked to read.

### A taxonomy

**Prompt injection** is the name for attacks that exploit this. In its *direct* form, the user types instructions that try to override the developer's rules. The more serious form for agents is **indirect prompt injection**, analysed by Greshake and colleagues in 2023. Here an attacker places instructions inside content an AI system is likely to process, and the model may treat them as commands. The authors argued that connecting models to retrieved content "blurs the line between data and instructions" and demonstrated the problem against systems then in use, including a search engine's GPT-4-based chat [@greshake2023not].

Greshake and colleagues sort attacks by how they arrive and what they aim at. By *delivery*, injections can be passive (planted where retrieval will find them, such as a web page), active (sent to the target, for example in an email the assistant will read), user-driven (the user is tricked into pasting them) or hidden (concealed or split across stages). By *goal*, they include information gathering (extracting private data), fraud, intrusion (taking unauthorised actions through the system's own tools), spreading malware, manipulating the content shown to the user, and degrading availability.

Agents widen the attack surface beyond web pages and emails. A computer-use agent reads whatever is on screen, which is why OpenAI added a monitor for suspicious on-screen content [@openai2025computer]. Tool descriptions are themselves text that the model trusts, which is why the MCP specification tells clients to treat annotations from untrusted servers as untrusted [@modelcontextprotocol2025tools]. In multi-agent systems, a message from another agent is one more input of uncertain provenance.

Real products have shipped with such flaws. In June 2025 the US National Vulnerability Database published CVE-2025-32711, described as "AI command injection in M365 Copilot" that "allows an unauthorized attacker to disclose information over a network". Microsoft rated it 9.3 out of 10 ("critical") and NIST's own analysts 7.5 ("high"); both scoring vectors indicate that the attack required neither privileges nor any action by the user [@nist2025cve]. Microsoft stated that it had already fully mitigated the flaw on its servers, that users needed to take no action, and that it was not aware of exploitation [@microsoft2025cve].

### Why it resists a fix

The UK's National Cyber Security Centre (NCSC) has argued that prompt injection should not be thought of as similar to SQL injection, a familiar class of web vulnerability. SQL injection can be prevented by strictly separating commands from data, but current language models "do not enforce a security boundary between instructions and data inside a prompt". The NCSC therefore warned that prompt injection "may never be totally mitigated". It described the model as an "inherently confusable deputy" (a classic security term for a program with privileges that can be tricked into using them for someone who lacks them) and advised designers to focus on reducing the likelihood and impact [@chismon2025prompt].

The independent developer Simon Willison has proposed a widely cited rule of thumb for when the danger is acute. His "lethal trifecta" is an agent that combines access to private data, exposure to untrusted content, and the ability to communicate externally [@willison2025lethal]. With all three, injected instructions can in principle cause private data to leave the system. Removing any one breaks the chain, which turns an unsolved machine-learning problem into a design decision. Willison also observes that a filter that catches 95 per cent of attacks would be a failing grade in web security.

### Defences and their limits

One line of defence is *training the model* to resist. OpenAI researchers proposed an "instruction hierarchy" in which models learn to give priority to the developer's and user's instructions over text from tools and documents. In a preprint they reported substantially improved robustness, including against attack types not seen in training [@wallace2024instruction]. *Detection* uses separate classifiers to flag likely injections in inputs. Both approaches improve average-case behaviour but give no guarantees, and attackers who adapt can defeat them. A 2025 preprint by 14 researchers from several AI companies and universities tested 12 recent defences from these families (prompting techniques, training methods, detectors and methods based on secret checks) against adaptive attacks. Such attacks modify their strategy to counter each defence's design. They bypassed most defences with success rates above 90 per cent, although the majority had originally reported attack success near zero. A human red-teaming competition with more than 500 participants and $20,000 in prizes succeeded in every scenario it covered. The authors conclude that "empirical evaluations cannot prove that a defense is robust" [@nasr2025attacker].

*System design* takes the opposite starting point: it accepts that the model can be fooled and limits what a fooled model can do. Beurer-Kellner and colleagues, from industry and academic security groups, describe in a 2025 preprint six design patterns (Table 5.4). Their central claim is that "securing general-purpose agents remains out of reach with current capabilities", but that "application-specific agents can be secured through principled system design" [@beurerkellner2025design].

| Pattern | Idea | Main cost |
|:--|:--|:--|
| Action selector | Model only maps a request to a fixed menu of actions; results never return to it | Loses most of the model's flexibility; every command must be predefined |
| Plan then execute | Actions fixed before untrusted data is read | Hard when later steps depend on earlier results; injected data can still alter tool inputs, such as an email's text |
| Map–reduce | Each untrusted item processed by an isolated model call with constrained output | Some tasks cannot be decomposed this strictly |
| Dual LLM | A privileged model with tools never sees untrusted text; a quarantined model without tools reads it | Quarantined model's output must be tightly constrained; some tasks cannot be split this way |
| Code then execute | Model writes a program that calls tools and other models, then runs it over the data | As with plan then execute, injected data can still alter the content passed between steps |
| Context minimisation | Remove the user's prompt from context once it has been used | Addresses only injections in the user's own prompt |

: Table 5.4: Design patterns for agents that resist prompt injection, with the trade-offs their authors identify. Source: [@beurerkellner2025design].

Some designs go further and offer formal guarantees. **AgentDojo**, from ETH Zurich, provides 97 realistic tasks (managing email, online banking, travel booking) and 629 security test cases; its authors found that leading models failed many tasks even without attack [@debenedetti2024agentdojo]. A follow-up system, **CaMeL**, first posted as a preprint in 2025 and published in 2026 at the IEEE Conference on Secure and Trustworthy Machine Learning (SaTML), is the instance of the code-then-execute pattern that Beurer-Kellner and colleagues cite [@beurerkellner2025design]. It adds a layer that tracks where every piece of data came from and what it may be used for. The plan is derived from the trusted user request before any untrusted data is read, so retrieved content cannot change which actions are taken. A policy check blocks data from flowing to places it should not. On AgentDojo, CaMeL completed 77 per cent of tasks with provable security, against 84 per cent for an undefended system: protection cost seven points of usefulness. The guarantees cover attacks that try to change the agent's actions or the flow of data, such as sending private files to an outsider. The authors state that CaMeL "cannot defend against text-to-text attacks", such as an injected instruction that makes the agent summarise an email misleadingly. They also describe side channels through which small amounts of information could still leak [@debenedetti2025defeating].

Human confirmation, the default safeguard in MCP and in commercial computer-use agents, sits alongside all of these. It works when the person reads the request; Beurer-Kellner and colleagues warn of "tired or overloaded human verifiers approving unsafe actions" [@beurerkellner2025design].

::: {.box .debate}
**Debate: Can prompt injection be solved inside the model?**

*Mainly outside the model.* The NCSC holds that because models do not separate instructions from data, prompt injection may never be fully mitigated, and that systems should limit what a manipulated model can do [@chismon2025prompt]. Adaptive attackers defeated twelve model-level and filter-based defences that had reported near-zero attack rates [@nasr2025attacker]. Architectural designs such as CaMeL give guarantees, for defined classes of attack, that do not depend on the model behaving well [@debenedetti2025defeating].

*Increasingly inside the model.* Training on an instruction hierarchy improved robustness, including against unseen attack types [@wallace2024instruction], and AgentDojo shows attack success varying widely between models, so model choice matters [@debenedetti2024agentdojo]. Architectural defences have real costs: CaMeL completed fewer tasks, its guarantees exclude text-only manipulation [@debenedetti2025defeating], and the most secure patterns give up much of what makes a general-purpose assistant useful [@beurerkellner2025design].

The disagreement is empirical, and the missing data are independent evaluations on realistic tasks in which well-resourced attackers adapt to each defence, with both attack success and lost usefulness reported. A model-level defence that held up under that kind of testing would strengthen the second position; continued breaks would favour the first.
:::

## 5.7 Agents that pay

If agents are to book travel or buy supplies, they need a way to pay. Card payments assume that a human clicks "buy" on a trusted screen. Google's announcement of its **Agent Payments Protocol (AP2)** in September 2025 named the problems this creates once software acts for a person. *Authorisation* means "proving that a user gave an agent the specific authority to make a particular purchase". *Authenticity* means assuring the merchant that the request reflects the user's real intent, and *accountability* means deciding who is responsible if a transaction is fraudulent or wrong [@parikh2025powering].

AP2's answer is a chain of "mandates", which the company describes as "tamper-proof, cryptographically-signed digital contracts" signed with verifiable credentials (digitally signed attestations that a third party can check). In a purchase with the user present, a request such as "find me new white running shoes" is captured in an *Intent Mandate*. When the user approves a specific cart, their approval signs a *Cart Mandate* recording the exact items and price. For a delegated purchase without the user present, such as buying concert tickets the moment they go on sale, the user signs a detailed Intent Mandate in advance, with price limits, timing and other conditions. Such a mandate "can allow the agent to automatically generate a Cart Mandate on your behalf once your precise conditions are met". Google argues that the chain provides "a non-repudiable audit trail", a record that no party can plausibly deny later. More than 60 organisations backed AP2 at launch, including card networks and payment firms, and an extension built with Coinbase, the Ethereum Foundation and MetaMask supported payments in cryptocurrency [@parikh2025powering].

The protocol's current documentation describes AP2 as an extension of A2A and MCP and restructures the scheme. A *Checkout Mandate* is shared with the merchant, and a *Payment Mandate* with the credential provider, the card networks and the merchant's payment processor. Each exists in an "open" form, which sets constraints such as a budget, and a "closed" form, which records a specific, finalised transaction [@ap22026agent].

A second proposal works at the level of the web itself. The HTTP protocol that underlies web pages has long reserved a status code, 402 "Payment Required", that was rarely used. In May 2025 the cryptocurrency company Coinbase released **x402**, an open protocol that puts this code to work, initially for payments in stablecoins (digital tokens pegged to a currency such as the US dollar) [@dioquino2025coinbase; @coinbase2025x402]. In the current specification, a server that wants payment answers a request with status 402 and a header listing acceptable payment options. The client, which may be an agent, chooses one, signs a payment and repeats the request with the signed payment in another header. The server, or a third-party "facilitator" it calls, verifies and settles the payment, and returns the resource with a receipt. The design principle is "trust minimizing": schemes "must not allow for the facilitator or resource server to move funds" beyond what the client authorised [@x4022026x402]. Because the whole exchange fits inside an ordinary web request, the design suits small payments per request; the specification's own example is paying $1 to read an article. In April 2026 the protocol moved to an x402 Foundation under the Linux Foundation; its 40 launch members included card networks, cloud providers and payment companies [@coinbase2026x402].

These protocols are young, and public evidence on how much real commerce passes through them is thin and comes mostly from vendors, whose transaction figures conflict. The protocols do settle one design question: they record what the human authorised in a form that can be checked later, the kind of evidence a dispute would turn on. They do not settle who bears the loss when an agent acting within its mandate makes a bad purchase, a question for contract law and payment regulation.

## 5.8 Many agents: multi-agent systems and agent economies

### Teams of agents

Many deployed systems combine several agents with different roles. Anthropic described its research feature as an orchestrator–worker design: a lead agent (Claude Opus 4) plans the research and spawns sub-agents (Claude Sonnet 4) that search in parallel. According to the company, this outperformed a single Opus 4 agent by 90.2 per cent on its internal research evaluation. The cost was tokens: agents used about four times as many tokens as chat interactions and the multi-agent system about fifteen times as many. On the BrowseComp search benchmark token usage alone explained about 80 per cent of the variance in performance. The company noted that most coding tasks offer fewer truly parallel sub-tasks than research does [@anthropic2025how].

Independent analysis is less encouraging about multi-agent designs in general. Cemri and colleagues annotated more than 1,600 execution traces from seven popular multi-agent frameworks, starting from the observation that such systems often show only small gains over single agents on standard benchmarks. They identified 14 failure modes in three categories. System design issues include the most frequent mode, step repetition (15.7 per cent of annotated failures), and agents unaware of when to stop. Misalignment between agents covers cases such as a mismatch between an agent's stated reasoning and its action, or an agent ignoring another's input. The third category is weak or incorrect verification of the final result. Annotators agreed closely on the categories (Cohen's kappa, a measure of agreement beyond chance, 0.88 on 150 traces), so the failures are recognisable patterns [@cemri2025why]. Project Vend's second phase showed the same pattern at small scale: adding a manager agent changed outcomes, but the manager shared the worker's weakness for saying yes [@anthropic2025projectphase].

### Risks when agents meet

A different problem arises when agents with different owners interact, for example in a marketplace. The Cooperative AI Foundation's report *Multi-Agent Risks from Advanced AI*, led by Lewis Hammond with 44 authors, offers one of the most systematic maps so far. It classifies failures by the agents' incentives into **miscoordination** (agents with compatible goals fail to work together), **conflict** (agents with opposed goals harm each other or bystanders) and **collusion** (agents cooperate in ways their owners or society did not intend). It lists seven risk factors that make them more likely: information asymmetries, network effects, selection pressures, destabilising dynamics, commitment problems, emergent agency and multi-agent security [@hammond2025multi]. Because large populations of capable LLM agents interacting in the wild are still rare, the report is a structured map of mechanisms, not a measurement of current harm.

Evidence on collusion comes from older pricing algorithms. In simulations, Calvano and colleagues found that simple reinforcement-learning pricing algorithms competing in a standard market model "consistently learn to charge supracompetitive prices, without communicating with one another". The algorithms sustained high prices with strategies that punish undercutting and then return to cooperation [@calvano2020artificial]. In Germany's retail petrol market, where pricing software became widely available in 2017, Assad and colleagues found that adoption raised margins only for stations facing competitors. In markets with two or three stations, margins rose only when all of them adopted it, which the authors read as evidence that algorithmic pricing has a significant effect on competition [@assad2024algorithmic]. Neither study involves language-model agents, but both show that coordination can emerge between algorithms without being designed or communicated.

### Agent economies

Economists have begun to ask what markets will look like if many transactions are carried out by software. Hadfield and Koh, in a chapter for a National Bureau of Economic Research handbook released as a preprint, argue that agents able to carry out long tasks with little oversight may be widely deployed within a decade. They raise the possibility that "the errors introduced by AI agents might be more correlated than those of humans", so that mistakes would not cancel out across a market. They point to the 2010 "flash crash" in US stock markets, which automated trading is thought to have worsened, as an early warning. The identity and registration systems that tell people whom they are dealing with "are currently missing for AI agents", they note, and new digital institutions will be needed [@hadfield2025economy].

Tomašev and colleagues at Google DeepMind propose, in a preprint, the frame of "sandbox economies". They classify agent economies by whether they emerge spontaneously or are deliberately designed, and by how *permeable* they are: how freely value and effects pass between the agent economy and the human one. They call permeability "the critical and controllable design variable" and argue that current trends point towards a large, unplanned and highly permeable agent economy. Their proposals include auctions to allocate resources fairly, partial insulation between high-speed agent trading and the rest of the economy, and identity infrastructure such as cryptographically signed credentials [@tomasev2025virtual].

The payment mandates of Section 5.7 and the Agent Cards of Section 5.3 are early pieces of such infrastructure. Chan and colleagues examine three further measures for making agents visible: **agent identifiers** that show when an agent is involved in an interaction, **real-time monitoring** of agent activity, and **activity logs** that can be reviewed afterwards. Each can be implemented more or less intrusively, and the authors weigh the gains in accountability against costs to privacy and the risk of concentrating power in whoever runs the monitoring [@chan2024visibility].

Evidence on agent-to-agent commerce still consists mostly of experiments, protocols and forecasts, so this literature names the design choices (identity, permeability, speed, record-keeping) before large-scale deployment has fixed them. Chapter 11 places correlated failure within the wider taxonomy of AI risks, and Chapter 14 returns to evaluating whole populations of agents.

An agent's usefulness and its main weaknesses have the same source: software, not a person, now closes the loop between what a model writes and what happens in the world. Errors compound over steps, reliability across repeated attempts falls well below single-try success, and any text the loop feeds back, from a web page to another agent's message, can redirect the model. The safeguards that do not depend on the model behaving well sit outside it: narrow permissions, plans fixed before untrusted data arrive and checks that catch failure, joined for payments by signed records of what a human authorised. Project Vend's shopkeeper displayed most of these weaknesses in one small shop. Its second phase showed that better tools cut the losses while, in the authors' words, the gap between "capable" and "completely robust" remained wide.

## Further reading

- Yao, S. et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. The short paper behind the reason–act–observe loop that most current agents use, with readable example traces. [@yao2023react]
- Kapoor, S. et al. (2025). *AI Agents That Matter*. Shows, with worked comparisons, why accuracy-only agent leaderboards mislead and what cost-aware, held-out evaluation looks like. [@kapoor2025ai]
- Chismon, D. (2025). *Prompt Injection Is Not SQL Injection (It May Be Worse)*. A short explanation from the UK's National Cyber Security Centre of why the problem resists the fixes that worked for earlier injection attacks. [@chismon2025prompt]
- Beurer-Kellner, L. et al. (2025). *Design Patterns for Securing LLM Agents against Prompt Injections*. Six concrete architectures with case studies, and an honest account of what each gives up. [@beurerkellner2025design]
- Hammond, L. et al. (2025). *Multi-Agent Risks from Advanced AI*. A systematic map of failure modes and risk factors when many AI agents interact, grounded in real-world examples. [@hammond2025multi]
- Hadfield, G. K. and Koh, A. (2025). *An Economy of AI Agents*. An economist's survey of the institutions that markets full of agents may need. [@hadfield2025economy]


# Chapter 6: AI for Science, Mathematics and Engineering

In the second week of October 2024, the Royal Swedish Academy of Sciences awarded two of its Nobel Prizes for work on artificial intelligence. On 8 October the physics prize went to John Hopfield and Geoffrey Hinton "for foundational discoveries and inventions that enable machine learning with artificial neural networks" [@royal2024nobelphysics]. The next day, half of the chemistry prize went to Demis Hassabis and John Jumper of Google DeepMind "for protein structure prediction", with the other half going to David Baker for computational protein design [@royal2024nobelchemistry]. The physics prize honoured the ideas behind the networks described in Chapter 2. The chemistry prize honoured a use of those networks that had changed how a whole field works.

A prize does not settle what AI does for science. A model can be accurate without revealing why. A system can produce thousands of candidate results that nobody has time to check, and a headline about AI "discovering" something can rest on an evaluation that a later reanalysis overturns. The fields covered below (protein structure, weather and climate, materials, mathematics and algorithms, and automated research) each have a showcase result and at least one independent test of it. Biology and medicine appear only at the level of protein structure; Chapter 10 covers health.

Most showcase results come from a handful of companies, above all Google DeepMind, and many were first reported by the companies themselves. Several later passed peer review and some were checked by outsiders; where no independent evaluation exists, a result is the developer's own account.

## 6.1 Where AI enters the scientific cycle

Science is often described as a cycle. Researchers read what is already known, form a hypothesis, design an experiment or a simulation, collect and analyse data, and publish results that others check and build on. Machine learning can enter at every stage, where it does one of four distinguishable jobs. **Prediction** learns a mapping from inputs to outputs from many solved examples, so that new cases can be answered without the slow work: a protein's shape from its sequence. **Emulation** learns to imitate an expensive simulation, such as a weather model, so that it can be run far more cheaply. **Search** proposes many candidate solutions (crystal structures, proofs, algorithms) and keeps those that pass a test. **Automation** takes over parts of the research workflow itself: reading papers, writing and running code, drafting manuscripts. Figure 6.1 places these jobs on the cycle.

![Figure 6.1: Where AI enters the scientific cycle. Each stage of a simplified research cycle is paired with the kind of AI tool most often used there, and with the check that keeps the result honest. The checks on the inner ring return in Section 6.8. Diagram by the author.](../figures/svg/fig-06-01.svg){#fig:06-01}

An **emulator** (also called a surrogate model) is trained on the inputs and outputs of a slower model or measurement. Once trained, it gives in seconds approximate answers that would otherwise take hours of supercomputer time. Unlike the simulation it imitates, it is not written from physical equations; it learns only from examples, so it can be confidently wrong in situations its training data never covered.

The four jobs differ in how easily their results can be checked, and this matters more than the sophistication of the model. A prediction can be compared with a later measurement, an emulator with the simulation it imitates and with reality. A candidate found by search may be checkable instantly (a proof, a faster program) or only after months of laboratory work (a new compound). Automated research produces claims of every kind at once.

Scientists are adopting these tools quickly and with mixed feelings. A 2023 *Nature* survey of more than 1,600 researchers found them "concerned, as well as excited", with many expecting AI tools to become central to research soon [@vannoorden2023ai]. The anthropologist Lisa Messeri and the psychologist M. J. Crockett, reviewing how scientists describe their hopes for AI, identify four imagined roles [@messeri2024artificial]. AI appears as *Oracle* (searching and summarising the literature), as *Surrogate* (standing in for data that are hard to collect), as *Quant* (analysing data too large for a human) and as *Arbiter* (judging which studies are sound). Each promises more productivity and objectivity; Section 6.8 returns to what those promises can hide.

## 6.2 Protein structure: what AlphaFold computes, and what it does not

A protein is a chain of building blocks, amino acids, that folds into a three-dimensional shape; the shape largely determines what the protein does. Determining one structure by experiment has typically taken months to years, and by 2021 only around 100,000 unique protein structures had been solved, a small fraction of the known sequences. Predicting structure from sequence had been an open research problem "for more than 50 years" [@jumper2021highly], and the field had built an unusually strict test for it. The Critical Assessment of Structure Prediction (CASP) is a community experiment whose "core components are rigorous blind testing of methods and evaluation of the results by independent assessors" [@kryshtafovych2021critical]. Predictors submit models of proteins whose experimental structures have been determined but not yet released, so nobody can tune to the answer.

### How AlphaFold 2 works

AlphaFold 2 takes three inputs: the amino-acid sequence, a **multiple sequence alignment** (MSA) of related sequences from other organisms, and, where available, a few experimentally solved structures of related proteins as templates [@jumper2021highly]. The alignment matters because evolution leaves traces of shape in sequence. Positions that are in contact in the folded protein tend to change together over evolutionary time, so correlated variation between two columns of the alignment hints that they are close in space. Earlier methods computed these "pairwise evolutionary correlations" with fixed statistics and turned them into predicted distances. AlphaFold instead lets the network learn to interpret "phylogenetic and covariation relationships without hardcoding a particular correlation statistic" [@jumper2021highly].

The network keeps two internal representations and lets them talk to each other. The *MSA representation* is a table with one row per related sequence and one column per residue (amino-acid position). The *pair representation* is a square table with one entry for every pair of residues, recording what the network currently believes about their relation. The trunk of the network, called the **Evoformer**, consists of 48 blocks that repeatedly exchange information between the two tables. Its most distinctive operations are "triangle" updates: for any three residues *i*, *j* and *k*, the entries for the pairs *ik* and *jk* are used to update the entry for *ij*. The motivation is geometric. For a set of pairwise distances to describe a real object in three dimensions, they must satisfy constraints such as the triangle inequality, and the triangle updates were designed with that consistency requirement in mind. They encourage it rather than impose it as a hard rule [@jumper2021highly].

The **structure module** then turns these representations into coordinates. It treats each residue as a free-floating rigid body with its own rotation and position, a "residue gas" that starts with every residue at the origin and every rotation set to the identity. A geometry-aware attention mechanism, *invariant point attention*, updates the residues so that the result does not depend on how the whole molecule is rotated or shifted in space. During this stage the network is allowed to break the chain, which makes local refinement easier; correct bond geometry is encouraged later in training and enforced only in a final physics-based relaxation.

The whole network is then run again with its previous outputs (the pair representation, the first row of the MSA representation and the predicted backbone positions) fed back in as extra inputs, a step called *recycling* (Figure 6.2). AlphaFold runs four such passes in all. To show how a prediction forms, the authors attached a separately trained structure module after each of the 48 blocks, giving a trajectory of 192 intermediate structures over the four passes that can be watched converging on the answer. The model was trained on Protein Data Bank structures released up to 30 April 2018, plus a high-confidence subset of its own predictions for about 350,000 further sequences (self-distillation). Training ran on 128 cores of Google's TPU v3 (Tensor Processing Unit, the company's own AI accelerator chip; Chapter 7) for about a week, followed by about four days of fine-tuning [@jumper2021highly].

![Figure 6.2: How AlphaFold 2 turns a sequence into a structure. The sequence is used to search databases for related sequences (the MSA) and templates; 48 Evoformer blocks exchange information between the MSA representation and the residue-pair representation; the structure module places each residue as a rigid body in 3D; the network's outputs are fed back in for further passes (recycling, four passes in all), and the final structure comes with a per-residue confidence score, pLDDT. Diagram by the author, after @jumper2021highly.](../figures/svg/fig-06-02.svg){#fig:06-02}

Each prediction comes with a per-residue confidence score, the predicted local distance difference test (pLDDT), which "reliably predicts" the actual local accuracy, so a researcher can see which parts of a model to trust [@jumper2021highly].

### The CASP14 result and its limits

In CASP14, held from May to July 2020, the gap to every other method was large. On 87 protein domains, AlphaFold's median backbone error was 0.96 ångström (Å; one ångström is a ten-billionth of a metre), measured as the root-mean-square deviation over the best-fitting 95% of residues. The next best method had 2.8 Å. For all atoms, including side chains, the figures were 1.5 Å and 3.5 Å [@jumper2021highly].

The CASP organisers' overview of the round, which summarises the independent assessments, reported models "competitive with experimental accuracy for at least 2/3 of the targets" and concluded that the results "represent a solution to the classical protein-folding problem, at least for single proteins" [@kryshtafovych2021critical]. The qualifier is deliberate. The same overview records objections to the word "solution". The AlphaFold paper names its own weak points: accuracy "decreases substantially" when the alignment has fewer than about 30 sequences, and the model is "much weaker for proteins that have few intra-chain or homotypic contacts" [@jumper2021highly].

Scale followed quickly. The AlphaFold Protein Structure Database, hosted by the European Bioinformatics Institute, grew from about 300,000 predicted structures in 2021 to "over 214 million", and its predictions are integrated into the main protein databases [@varadi2024alphafold]. The Academy's Nobel press release stated that more than two million people in 190 countries had used AlphaFold [@royal2024nobelchemistry].

Outside structural biologists then tested how much weight the predictions can bear. Terwilliger and colleagues compared AlphaFold predictions with experimental crystallographic maps for 102 crystal structures, looking only at the parts predicted with very high confidence. Many matched "remarkably closely". Overall, the central backbone (Cα) atoms in these very-high-confidence regions differed from the crystal structures by a median of 0.6 Å, and about 10% differed by more than 2 Å. Each figure is about twice the corresponding value for two experimental structures of the same protein crystallised in different forms. Some predictions were distorted globally or had domains in the wrong orientation [@terwilliger2024alphafold]. The authors recommend treating predictions as "exceptionally useful hypotheses", and verifying by experiment any detail that matters, "particularly those that involve interactions not included in the prediction".

### AlphaFold 3: wider scope, new failure modes

AlphaFold 3, published in May 2024, extends prediction from single protein chains to complexes "including proteins, nucleic acids, small molecules, ions and modified residues" [@abramson2024accurate]. Its architecture changes in two ways. Alignment processing is "substantially de-emphasized", and a new trunk, the Pairformer, replaces the Evoformer as the main processing block. A **diffusion model**, the generative method also used by image generators, replaces the structure module. It learns to start from random noise and remove it step by step until a realistic sample remains, here working directly on atom coordinates. The authors report substantially higher accuracy than many specialised tools for protein–small-molecule, protein–nucleic-acid and antibody–antigen interactions [@abramson2024accurate].

The same paper lists the costs of the new design. Generative models can invent order where there is none: the diffusion approach "introduces the challenge of spurious structural order (hallucinations) in disordered regions", although such regions are usually flagged with low confidence. Outputs "do not always respect chirality", the handedness of molecules, with a violation rate of 4.4% on one benchmark. The model "typically predict[s] static structures as seen in the PDB", not the motions through which many proteins work. For antibody–antigen complexes the best results needed many runs from different random starting points, with accuracy still improving at 1,000 [@abramson2024accurate]. Access is narrower than for AlphaFold 2: the inference code is public, but the trained parameters are available only from Google under its terms of use. The free web server, for non-commercial use, supports a more limited set of ligands and chemical modifications [@google2024alphafold].

Few other fields have what the protein case combines: a large archive of carefully checked human data (the PDB), a precisely defined target, a confidence measure on each output, and a blind test run by outsiders.

## 6.3 Weather and climate: learning the atmosphere

Weather forecasting is where machine learning has moved fastest from research paper to daily operations. Conventional **numerical weather prediction** (NWP) starts from the best estimate of the current state of the atmosphere and steps forward in time by solving the equations of fluid dynamics and thermodynamics on a supercomputer. That starting estimate comes from **data assimilation**, the process of combining fresh observations with a short forecast from the previous cycle [@rasp2024weatherbench]. The European Centre for Medium-Range Weather Forecasts (ECMWF) runs the leading global system, the Integrated Forecasting System (IFS). Its high-resolution deterministic forecast (HRES) ran at 0.1° resolution with 137 vertical levels, and a ten-day forecast took about an hour on a supercomputer [@lam2023learning]. (In May 2026 ECMWF removed HRES as a separate forecast, merging it with the control run of its ensemble [@ecmwf2026significant].)

### How machine-learning models are trained

Machine-learning weather models learn from **reanalysis**: a consistent reconstruction of past weather, produced by running a fixed modern data-assimilation system over decades of historical observations. ECMWF's ERA5, available hourly from 1940 to the present at 0.25° resolution (about 28 km at the equator), is the standard training set [@rasp2024weatherbench; @lam2023learning]. A model is shown the state of the global atmosphere at one time and learns to predict the state a few hours later. To forecast further ahead, it is applied again to its own output.

Pangu-Weather, from Huawei, published in *Nature* in July 2023 after training on 39 years of data, reported stronger deterministic forecasts than the operational IFS "in all tested variables" when verified against reanalysis [@bi2023accurate]. GraphCast, from Google DeepMind, published in *Science* in 2023, became the reference point. It represents the atmosphere on a grid of 721 × 1,440 points, about a million in all, and at each point predicts 227 values: 5 surface variables and 6 atmospheric variables at each of 37 pressure levels [@lam2023learning].

GraphCast is a graph neural network, a network that passes messages along the edges of a graph. An encoder maps the grid onto an internal "multi-mesh" built by refining an icosahedron six times (40,962 nodes, with edges of many lengths so that information can travel both locally and across continents in a few steps). Sixteen processing layers pass messages over this mesh, and a decoder maps the result back to the grid. With 36.7 million parameters it is, as its authors note, "a relatively small model by modern ML standards" [@lam2023learning].

GraphCast was trained on ERA5 from 1979 to 2017 and tested on 2018. It produces a ten-day forecast in under one minute on a single Google TPU v4 chip, against about an hour for HRES on a supercomputer. Training took about four weeks on 32 such chips [@lam2023learning]. On 90% of 1,380 verification targets (combinations of variable, pressure level and lead time) it was significantly more accurate than HRES. The targets where HRES did better were concentrated in the stratosphere, and with the 50 hPa level excluded GraphCast was better on 96.9% of the rest [@lam2023learning].

::: {.box .concept}
**Concept: Forecast skill**

"Skill" in weather forecasting means accuracy measured by agreed scores, usually relative to a baseline. The **root mean square error** (RMSE) averages the squared differences between forecast and verifying analysis over the globe (weighted by latitude), then takes the square root; lower is better. The **anomaly correlation coefficient** (ACC) asks whether the forecast gets the *departures from normal* right, correlating forecast anomalies with observed anomalies; 1 is perfect and 0 is no better than climatology. ECMWF treats an ACC below 0.6 as the point where the positioning of large-scale weather systems "ceases to have value for forecasting purposes" [@rasp2024weatherbench]. For ensembles, the **continuous ranked probability score** (CRPS) rewards a spread of forecasts that is centred on what happened and neither too narrow nor too wide. Comparisons between models need reading with care. Each model is usually verified against its own "truth": GraphCast against ERA5, HRES against its own operational analysis, a choice the GraphCast authors made because verifying a model against its own analysis "gives the best skill estimates" [@lam2023learning]. And a forecast that is smoother than real weather can score well on RMSE and ACC without depicting any weather that could actually occur [@rasp2024weatherbench].
:::

::: {.box .deeper}
**Going deeper: Rolling a forecast forward, and why it blurs**

GraphCast takes two snapshots of the atmosphere six hours apart and predicts the snapshot six hours later. To forecast ten days ahead it feeds its own prediction back in and repeats the step 40 times [@lam2023learning]. This *autoregressive rollout* is how a language model adds one token at a time (Chapter 3). Because small errors compound, GraphCast was trained to minimise its error over up to 12 consecutive steps, not just one. That choice has a side-effect. When the future is uncertain, the forecast that minimises average squared error is the average of the possible outcomes. In a chaotic, non-linear atmosphere, moreover, "the mean of many states is not a realistic state itself" [@rasp2024weatherbench]. Forecasts therefore blur with lead time: storm peaks are shaved off and rain is spread thinly. GraphCast's authors tested whether its advantage was only blurring: when both models were optimally blurred, GraphCast still beat HRES on 88.0% of targets [@lam2023learning]. GenCast, described below, avoids the problem differently, by sampling individual sharp forecasts and letting the spread of an ensemble carry the uncertainty [@price2025probabilistic].
:::

A single forecast does not tell a decision-maker how confident to be. Operational centres therefore run **ensembles**: dozens of forecasts from slightly perturbed starting points, whose spread indicates uncertainty. GenCast, published in *Nature*, is a diffusion-model ensemble: each run starts from fresh random noise and produces a different plausible 15-day trajectory. In the authors' evaluation, it had greater skill than ECMWF's operational ensemble (ENS) on 97.2% of 1,320 targets, with better predictions of extreme weather, cyclone tracks and wind-power output. Its 50 members can be run in parallel, each 15-day forecast taking about eight minutes on one TPU v5 [@price2025probabilistic].

### Into operations

The step to operations came within two years. On 25 February 2025, ECMWF put its own Artificial Intelligence Forecasting System (AIFS) into operational service alongside the IFS. According to ECMWF, it outperforms leading physics-based models on many measures, including tropical cyclone tracks, and uses roughly 1,000 times less energy per forecast [@ecmwf2025ecmwfs]. In ECMWF's technical description (a preprint), the AIFS uses a graph-network encoder and decoder around a transformer processor. It was pre-trained on ERA5 for 1979–2020 and then fine-tuned on ECMWF's operational analyses, the kind of data from which it is started in real time. Training took about a week on 64 GPUs, and a ten-day forecast takes about two and a half minutes on one GPU [@lang2024aifs].

A 51-member ensemble version followed on 1 July 2025, using about 1,000 times less energy than the physics-based ensemble (Table 6.1). It runs at 31 km resolution, against 9 km for the physics-based ensemble, which ECMWF states "remains indispensable for high-resolution fields and coupled Earth-system processes" [@ecmwf2025ensemble]. Version 2 of both, live since 12 May 2026, adds ECMWF's first data-driven wave and snow-cover forecasts [@ecmwf2026significant].

In December 2025 the US National Oceanic and Atmospheric Administration (NOAA) launched three operational AI-based global systems, using GraphCast as the initial foundation and fine-tuning it on NOAA's own analyses. Its deterministic model (AIGFS) and 31-member ensemble (AIGEFS) need a small fraction of the computing of their physics-based counterparts (Table 6.1). A third, hybrid ensemble combines AI and physics-based members and, according to NOAA, outperforms both across most major verification measures [@noaa2025noaa].

| System | Compared with | Reported skill | Reported cost / speed | Reported weakness |
|---|---|---|---|---|
| GraphCast (deterministic; *Science*, 2023) | ECMWF HRES | Better on 90% of 1,380 targets | 10-day forecast in under 1 minute on one TPU v4 (HRES: about 1 hour on a supercomputer) | Blurring at long lead times |
| GenCast (50-member ensemble; *Nature*, 2024/2025) | ECMWF ENS | Better on 97.2% of 1,320 targets | 15-day forecast in about 8 minutes on one TPU v5 | Higher cost than deterministic ML models |
| AIFS, ECMWF (deterministic; operational since 25 Feb 2025) | Physics-based models | Better on many measures, incl. tropical cyclone tracks (gains of up to 20%) | About 1,000 times less energy per forecast | Uses physics-based initial conditions |
| AIFS ENS, ECMWF (51-member ensemble; operational since 1 Jul 2025) | Physics-based models | Better on many measures, incl. surface temperature (gains of up to 20%) | Over 10 times faster; about 1,000 times less energy | Coarser grid than physics-based ensemble (31 km vs 9 km) |
| AIGFS / AIGEFS, NOAA (operational suite launched 17 Dec 2025; GraphCast as starting point) | GFS / GEFS | Improved skill for many large-scale features; ensemble adds 18–24 h of skill | Up to 99.7% less computing (AIGFS); 9% of GEFS computing (AIGEFS) | Worse tropical cyclone intensity forecasts (v1.0) |

: Table 6.1: Published results for five machine-learning weather systems, as reported by their developers. The table lists the comparison baseline, the share of targets on which the AI model was more skilful (where reported), the reported computing savings and a reported weakness. All figures are developers' own evaluations; targets and baselines differ between rows, so rows are not directly comparable. Source: [@lam2023learning; @price2025probabilistic; @ecmwf2025ecmwfs; @ecmwf2025ensemble; @noaa2025noaa].

### What independent evaluations find

Several of the clearest evaluations come from meteorologists who did not build the models. The first comparison "in an operational-like context", by an ECMWF team, ran Pangu-Weather from the same initial conditions as the IFS and verified both against analyses and weather-station observations. Accuracy was comparable for global scores and for extreme events, but the study identified "overly smooth forecasts, increasing bias with forecast lead time, and poor performance in predicting tropical cyclone intensity" [@benbouallegue2024rise]. Massimo Bonavita, also at ECMWF, examined Pangu-Weather, FourCastNet and GraphCast and concluded that they did not properly reproduce smaller-scale weather and lacked the "fidelity and physical consistency" of physics-based models [@bonavita2024some].

Researchers at the University of Reading compared four machine-learning models on Storm Ciarán, a European windstorm that caused sixteen deaths. All captured the large-scale structure of the storm accurately, and all underestimated its peak winds, the detail that matters most for warnings [@charltonperez2024ai]. NOAA itself states that the first version of its deterministic AI model showed "a degradation in tropical cyclone intensity forecasts" even as track errors fell [@noaa2025noaa].

Other studies probe whether the models have learned atmospheric physics or a statistical shortcut. Selz and Craig fed an AI model tiny perturbations to its starting state. In physics-based models and in theory, such perturbations grow very fast, which is the "butterfly effect" that sets a hard limit on how far ahead weather can be predicted. The AI model "completely fails to reproduce the rapid initial growth rates" and so would wrongly suggest unlimited predictability, although for perturbations of realistic size it largely agreed with physics-based simulations [@selz2023can].

Sun and colleagues asked whether an AI model can forecast storms stronger than any it has seen. They trained versions of FourCastNet on 1979–2015 data, some with every Category 3–5 tropical cyclone removed, and tested them on Category 5 storms from 2018–2023. All versions were similarly accurate for ordinary weather; the version that had never seen strong storms "cannot accurately forecast Category 5" storms. Removing strong storms from only one ocean basin did less harm, because the model could learn from strong storms elsewhere [@sun2025can]. An emulator interpolates within its experience; it does not reliably extrapolate beyond it.

### Dependence on physics, and the climate question

Every operational AI system above still starts from an analysis produced by physics-based data assimilation, and all were trained on reanalysis produced by a physics model. ECMWF notes that the AIFS uses the same initial conditions as the IFS [@ecmwf2025ecmwfs]. Aardvark Weather, from researchers at the University of Cambridge and partner institutions and published in *Nature* in 2025, tests whether that dependence can be removed. A single model ingests raw observations and produces both global gridded forecasts and local station forecasts. Its global forecasts outperformed an operational NWP baseline "for several variables and lead times", and its station forecasts were skilful up to ten days ahead [@allen2025endtoend]. It remains a research system.

Climate projection is a harder problem than weather. A climate model must stay stable over decades of simulated time and respond correctly to conditions, such as higher greenhouse-gas concentrations, that lie outside the historical record. NeuralGCM, developed by a team at Google with academic and ECMWF co-authors and published in *Nature* in 2024, is a hybrid: a conventional solver for large-scale atmospheric dynamics, with learned components for small-scale processes such as clouds. With sea-surface temperatures prescribed it tracked climate statistics for multiple decades and produced realistic tropical-cyclone frequencies at 140 km resolution, at a fraction of the computing cost of conventional models. Its authors state plainly that "our model does not extrapolate to substantially different future climates" [@kochkov2024neural]. For weather, AI emulators have matched or overtaken physics-based forecasts on average scores. For projecting a changed climate, the out-of-distribution problem that Sun and colleagues demonstrated for storms applies to the whole system.

## 6.4 Materials: discovery claims under scrutiny

New materials underpin batteries, solar cells and microchips. The traditional route is slow: a chemist proposes a compound, a quantum-mechanical calculation using **density functional theory** (DFT) estimates whether it is stable, and a laboratory tries to make it. A compound is computed to be stable if its energy lies on or below the **convex hull**, the lowest-energy combination of known competing phases with the same overall composition. Anything above the hull would, in principle, decompose into those competitors. Machine learning can speed up the first two steps by screening vastly more candidates than DFT can afford.

### GNoME: scale by active learning

In November 2023 Google DeepMind researchers published GNoME (Graph Networks for Materials Exploration) in *Nature*. Graph neural networks represent a crystal as atoms (nodes) linked by bonds (edges) and predict its energy. The system ran six rounds of **active learning**: generate candidate structures by substituting elements into known crystals and by random search, filter them with the network, compute the survivors with DFT, and retrain the network on the results. Over these rounds the share of filtered candidates that DFT confirmed as stable (the "hit rate") rose from under 6% to above 80% for candidates with a given structure. For candidates specified only by composition it rose from under 3% to 33% per 100 trials, against about 1% in earlier work. The final models predicted energies to within 11 meV per atom [@merchant2023scaling].

Starting from about 48,000 previously known stable crystals, the authors reported "the discovery of 2.2 million structures below the current convex hull". Of these, 381,000 lie on the final updated hull, for a total of 421,000 stable crystals, "an order-of-magnitude expansion in stable materials known to humanity". They reported that 736 of their predicted structures had already been made independently by experimental groups [@merchant2023scaling].

Two solid-state chemists, Anthony Cheetham and Ram Seshadri, examined the first 250 of 2,047 entries in one GNoME compilation and a random sample from the larger database of 384,870 predicted stable structures [@cheetham2024artificial]. They found "scant evidence for compounds that fulfill the trifecta of novelty, credibility, and utility". A recurring problem was ordering. The calculations, carried out in effect at absolute zero, place different atoms on separate, neat positions in the crystal. At the temperatures where real synthesis happens, similar atoms often mix randomly on shared sites, so many "new" predictions were ordered versions of compounds already known in disordered form. Cheetham and Seshadri also argued that a compound only becomes a *material* when it shows some useful property. In their view the work "does not report any new materials but reports a list of proposed compounds". They nonetheless called the method promising and asked for more domain expertise in the next version.

::: {.box .case}
**Case study: The A-Lab and its correction**

In the same issue of *Nature* as GNoME, a team at Lawrence Berkeley National Laboratory and the University of California, Berkeley described the A-Lab, an autonomous laboratory that combines computation, synthesis recipes learned from the literature, machine learning and robotics. Its targets were chosen using stability data from the Materials Project, a public database of computed materials properties, and from Google DeepMind. Over 17 days of continuous operation, the authors reported, it "realized 41 novel compounds from a set of 58 targets" [@szymanski2023autonomous].

In early 2024 a group of solid-state chemists published a reanalysis in *PRX Energy* [@leeman2024challenges]. They argued that the automated analysis of the X-ray diffraction patterns, the measurements used to identify what had been made, was "not yet reliable", and that the predictions neglected atomic disorder. About two-thirds of the claimed successes, they concluded, were "likely to be known compositionally disordered versions of the predicted ordered compounds", and no new materials had been discovered.

In January 2026 the original authors published a correction [@szymanski2026author]. It clarifies that "novel" had meant new to the prediction platform, "not necessarily new to science". The authors manually reanalysed the diffraction data, a reanalysis that was itself peer-reviewed after publication. They confirmed the platform's conclusion in 36 of the 40 reported successes and judged 4 inconclusive, so the count of compounds made was reduced to 36. A further compound was removed from the discussion because it had mistakenly been included in the training data. The correction does not claim that the compounds are new to science. Outside experts checked a claim and the record was corrected, as science is supposed to work; it took more than two years and a great deal of expert labour.
:::

### Generating to order, and the disorder lesson

GNoME searches by substitution and filtering. A different approach generates crystals directly, using the same diffusion technique as AlphaFold 3. MatterGen, from Microsoft Research and published in *Nature* in January 2025, generates crystal structures and can be fine-tuned to aim for target properties such as chemistry, symmetry, or mechanical, electronic and magnetic properties. Compared with earlier generative models, its structures were "more than twice as likely to be new and stable" [@zeni2025generative]. As a proof of concept the team asked for a material with a bulk modulus (resistance to uniform compression) of 200 GPa and synthesised one of the generated structures, TaCr~2~O~6~. The X-ray analysis showed that the material made was "a compositionally disordered version of the ordered structure predicted by MatterGen". DFT gave 222 GPa for the ordered prediction. For the real, disordered sample, the highest of four estimates derived from nanoindentation measurements was 169 GPa (mean 158 GPa), within 20% of the target [@zeni2025generative]. The paper also takes disorder into account: to decide whether a generated structure is new, the authors introduced an "ordered-disordered structure matcher" and compared against 117,652 disordered experimental structures in addition to 850,384 ordered ones [@zeni2025generative].

### Control problems: a direct test

In 2022 researchers from DeepMind and the Swiss Plasma Center at EPFL used **reinforcement learning**, in which a system learns by trial and error against a reward signal, to control the magnetic coils of a tokamak fusion reactor [@degrave2022magnetic]. The controller learned entirely in a simulator and was then used, without further tuning, on the real Tokamak à Configuration Variable in Lausanne. It held a range of plasma shapes, including two separate plasmas in the vessel at once. The test of success is immediate: the plasma holds its shape or it does not.

The materials record, by contrast, shows a gradient of evidence. A prediction of stability is a statement about a computer model at zero temperature. A claim of synthesis concerns matter in a laboratory, and a claim of a useful material concerns measured performance. AI has made the first step cheap but not the second or third, so the gap between candidates generated and candidates verified has widened.

## 6.5 Mathematics: proofs a machine can check

Mathematics has a special place in AI for science because some of its answers can be verified by machine. A **proof assistant** such as Lean is a programming language in which mathematical statements and proofs are written so precisely that a computer can check every step [@moura2021lean]. If a proof is accepted, it is correct relative to the definitions used, whoever or whatever wrote it. Lean's community library, mathlib, contained 291,099 theorems and 139,563 definitions contributed by 772 people when checked in October 2026 [@lean2026mathlib]. AI systems that work in Lean can build on that library, but a problem must first be translated (**formalised**) into Lean, which is laborious and can introduce errors. A Lean proof of the wrong statement is a correct proof of something nobody asked.

### Olympiad geometry and AlphaProof

Competition mathematics became the proving ground. In January 2024 Trinh and colleagues described AlphaGeometry, which pairs a language model with a symbolic deduction engine. Instead of learning from human proofs, it was trained on 100 million synthetic theorems and proofs generated by running the symbolic engine on random geometric configurations. On 30 recent olympiad geometry problems it solved 25, against 10 for the previous best method [@trinh2024solving]. Its successor, AlphaGeometry 2, raised the share of all International Mathematical Olympiad (IMO) geometry problems from 2000 to 2024 that it solves from 54% to 84%, according to a preprint by its developers [@chervonyi2025goldmedalist].

At the IMO in July 2024, according to Google DeepMind, AlphaProof and AlphaGeometry 2 together scored 28 of 42 points, one point below the gold threshold of 29. AlphaProof solved two algebra problems and one number-theory problem, including the hardest in the competition; AlphaGeometry 2 solved the geometry problem; the two combinatorics problems went unsolved. The solutions were scored under IMO rules by the mathematicians Timothy Gowers and Joseph Myers. The caveats were stated: humans first translated the problems into formal languages (Lean for AlphaProof; a separate formalisation for AlphaGeometry 2). And while one problem was solved in minutes, others took up to three days, against two 4.5-hour sessions for contestants [@google2024ai].

The peer-reviewed account appeared online in *Nature* in November 2025 [@hubert2025olympiad]. AlphaProof is modelled on AlphaZero, the self-taught game-playing system. It learns to find Lean proofs by reinforcement learning, training on "millions of auto-formalized problems", that is, problems translated into Lean automatically rather than by hand. For the hardest problems it uses **test-time reinforcement learning**: while working on a problem it generates and learns from "millions of related problem variants", adapting itself to that one problem. The design depends on the proof checker. Every proof the system finds is verified by Lean, so it can learn from its own successes without a human marking them, and a false proof can never be rewarded. Figure 6.3 places these and later results on a timeline.

### IMO 2025: four claims, four kinds of evidence

A year later several systems reached gold-medal level, under different conditions and with different kinds of verification (Table 6.2). According to Google DeepMind, an advanced version of Gemini with its "Deep Think" reasoning mode solved five of the six problems for 35 points, working in natural language from the official problem statements within the 4.5-hour limit. Its solutions were graded and certified by IMO coordinators [@google2025advanced]. Two days earlier, an OpenAI researcher announced that an experimental OpenAI model had reached the same score on the same five problems under exam conditions [@wei2025openai; @willison2025advanced]. That is a company claim: according to OpenAI, each proof was graded by three former IMO medallists, and the result was not certified by the IMO's coordinators.

Two systems worked in Lean. The start-up Harmonic reports in a preprint that its Aristotle system produced formally verified solutions to five of the six problems. The problem statements were translated into Lean by hand, which the authors describe as "the only human formalization step". For questions that ask contestants to find a value, a language model first proposed candidates [@achim2025aristotle]. ByteDance's Seed-Prover, also described in a preprint, fully proved five of six problems in Lean after human experts formalised the statements, and the authors note that one proof "was finished after the deadline" set by the IMO committee [@chen2025seedprover]. A formal proof removes doubt about the reasoning, but each of these Lean results still rested on a human translation of the question.

| System (developer) | Contest | Format | Result | Checked by | Evidence type |
|---|---|---|---|---|---|
| AlphaProof + AlphaGeometry 2 (Google DeepMind) | IMO 2024 | Formal languages (Lean for AlphaProof); problems translated by hand | 28/42 (gold threshold 29); some problems took up to 3 days | Lean (AlphaProof's proofs); scored by two mathematicians | Company blog; later *Nature* paper |
| Gemini Deep Think (Google DeepMind) | IMO 2025 | Natural language, within 4.5 h | 35/42 (gold); 5 of 6 problems | IMO coordinators (certified) | Company blog |
| Experimental model (OpenAI) | IMO 2025 | Natural language, two 4.5 h sessions | 35/42; 5 of 6 problems | Three former IMO medallists | Company claim (posts on X) |
| Aristotle (Harmonic) | IMO 2025 | Lean; statements formalised by hand | 5 of 6 problems formally verified | Lean | Preprint |
| Seed-Prover (ByteDance) | IMO 2025 | Lean; statements formalised by experts | 5 of 6 fully proved, one after the deadline | Lean | Preprint |
| Public reasoning models (independent test) | USAMO 2025 | Natural language | Best model 25%; all others below 5% | Expert human judges | Preprint |

: Table 6.2: AI systems at mathematical olympiads, 2024–2025. Results in natural language and in Lean, and under different time limits, are not directly comparable. Source: [@google2024ai; @hubert2025olympiad; @google2025advanced; @wei2025openai; @achim2025aristotle; @chen2025seedprover; @petrov2025proof].

The gold-medal systems were experimental models run by their developers. An independent test of publicly available models gave a more modest picture. Researchers at ETH Zurich and INSAIT in Sofia gave the six problems of the 2025 USA Mathematical Olympiad to leading reasoning models within hours of the problems' release in March 2025, and expert judges graded the full proofs [@petrov2025proof]. In their preprint, only Gemini 2.5 Pro reached a non-trivial score of 25%; all others scored below 5%. The judges found flawed logic, unjustified assumptions and a lack of creative strategy, where benchmarks that graded only final answers had suggested much stronger performance.

## 6.6 Searching for new mathematics and algorithms

Olympiad problems have known solutions; research mathematics asks questions nobody has answered. The most productive approach so far has been a search loop with an automatic scorer.

### FunSearch and AlphaEvolve

FunSearch, published in *Nature* in December 2023, pairs a language model that writes short programs with an evaluator that runs them and scores what they produce. The best programs are fed back into the prompt, and the loop repeats [@romeraparedes2024mathematical]. Applied to the cap set problem, a question in combinatorics about how large a set of points in a grid can be without three on a line, it found a cap set of 512 points in eight dimensions, larger than any previously known. The search space is enormous (around 3^1,600^ possible configurations in dimension 8), and the result was not easy even for FunSearch: only four of 140 runs found the 512-point set. Because the system outputs a program rather than a list of points, mathematicians could read the program and write down the construction by hand [@romeraparedes2024mathematical].

AlphaEvolve, announced by Google DeepMind with a white paper in May 2025, generalises the idea into a coding agent that evolves whole programs [@novikov2025alphaevolve]. It maintains a database of candidate programs. An ensemble of language models (Gemini 2.0 Flash for many fast proposals, Gemini 2.0 Pro for occasional stronger ones) proposes modifications, evaluators run and score each child program, and the best survive. Its best-known mathematical result concerns multiplying two 4×4 matrices of complex numbers: it found a method using 48 scalar multiplications, the first improvement in this setting since Volker Strassen's algorithm of 1969. According to the company, it was applied to more than 50 open mathematical problems, matched the best known constructions in about 75% of cases and improved on them in about 20%. One improvement was a new lower bound for the "kissing number" in 11 dimensions: 593 spheres touching a central sphere.

The engineering results are of the same kind. A scheduling heuristic it found for Google's data centres recovers on average 0.7% of the company's fleet-wide computing resources. A tiling heuristic for a matrix-multiplication kernel used in training Gemini gave an average 23% kernel speed-up and a 1% reduction in overall training time [@novikov2025alphaevolve]. These are company results in a preprint, but the mathematical constructions can be checked by anyone.

A follow-up paper, with the mathematicians Javier Gómez-Serrano and Terence Tao as co-authors, applied AlphaEvolve to 67 problems in analysis, combinatorics, geometry and number theory. It "rediscovered the best known solutions in most cases and improved on them in several" [@georgiev2025mathematical]. Released as a preprint in November 2025 and published in *PNAS* in 2026, it is one of the most useful documents in the field because it reports the denominator. The preprint reports the cases where the system failed to reach the best known result. It states that AlphaEvolve "excels at problems that can be clearly formulated as the optimization of a smooth score function" and "sometimes struggles otherwise". It also records a "cheating phenomenon": the system found "loopholes or exploit[ed] artifacts" in the scoring setup, for example a verifier that checked a constraint only at discrete points, rather than genuine solutions. On one problem the authors chained three systems: AlphaEvolve found a general construction for finite-field Kakeya sets, Deep Think derived a proof and a closed-form formula, and AlphaProof formalised the proof in Lean [@georgiev2025mathematical]. An automated scorer is only as good as its specification, and a search strong enough to find new constructions is also strong enough to find holes in the test.

Computing itself has been a target. In 2023 DeepMind's AlphaDev used reinforcement learning to discover short sorting routines that outperformed the human-written ones. They were added to the LLVM standard C++ sort library, a widely used open-source component [@mankowitz2023faster].

![Figure 6.3: Selected milestones in AI for mathematics and algorithms, 2023–2026. Entries are limited to results with a published paper, an official announcement, or a verified formal proof, and are evenly spaced (not to scale in time). Source: [@romeraparedes2024mathematical; @trinh2024solving; @google2024ai; @mankowitz2023faster; @novikov2025alphaevolve; @google2025advanced; @georgiev2025mathematical; @sothanaphan2026resolution].](../figures/svg/fig-06-03.svg){#fig:06-03}

### Open problems: Erdős problems as a test case

Claims about open problems need particular care, and a website collecting problems posed by the mathematician Paul Erdős has become an informal testing ground. In October 2025, OpenAI staff posted that GPT-5 had found solutions to ten "open" problems from the site. Its maintainer, Thomas Bloom, called this "a dramatic misinterpretation": "open" on his site meant only that he did not know of a solution, and the model had located existing papers [@bastian2025leading]. Most of the posts were deleted. A real strength, searching a scattered literature, had been presented as a different one, solving problems.

In January 2026, Erdős problem #728 was described in a preprint as "the first Erdős problem ... regarded as fully resolved autonomously by an AI system". The proof came from a combination of OpenAI's GPT-5.2 Pro and Harmonic's Aristotle, operated by Kevin Barreto, and was checked in Lean [@sothanaphan2026resolution]. The details matter. As Erdős and his co-authors stated it, the problem was ambiguous and had trivial solutions. Bloom judged that the AI proof answered a tightened version, "the question in the spirit it was intended" [@bloom2026erdos]. Closely related earlier work by Carl Pomerance was identified afterwards [@tao2026ai]. Tao, commenting on the result, noted that Erdős problems vary in difficulty "by several orders of magnitude" and that many were never seriously studied. As reported, he added that the success said more about speed than about difficulty [@bastian2026terence]. Failures are rarely reported, so success rates are unknown. Formal verification settles whether a proof is correct; it does not settle whether the problem was important, whether the formal statement captured the intended question, or how often the method fails.

## 6.7 Automating research: "AI scientist" systems

The systems so far each do one job inside a human-led project. A newer line of work tries to automate the whole loop, and it now has enough independent evaluation to compare claims with evidence (Table 6.3).

### The AI Scientist

The best documented system is The AI Scientist, developed by the Tokyo company Sakana AI with researchers at the University of British Columbia and the University of Oxford. Its first version, released as a preprint in August 2024, generated research ideas in machine learning, wrote and ran the code, produced figures, wrote a full paper and reviewed it, at a cost of less than 15 US dollars per paper [@lu2024ai]. An independent evaluation by Beel and colleagues found "critical shortcomings". Its literature reviews misclassified established concepts as novel; 42% of experiments failed because of coding errors; manuscripts had a median of five citations, mostly outdated; and some papers "contained hallucinated numerical results". The evaluators also found that it produced a full paper for 6 to 15 dollars with about 3.5 hours of human involvement, with quality they likened to "a rushed undergraduate paper" [@beel2025evaluating].

In early 2025, with the agreement of the organisers of a workshop at ICLR, a major machine-learning conference, the team submitted three papers generated end to end by a second version of the system. Reviewers knew that some submissions might be AI-generated but not which. One received scores of 6, 7 and 6, above the workshop's average acceptance threshold, and was withdrawn as agreed in advance. The company noted that workshop papers face a lower bar, and that its own researchers judged none of the three good enough for the main conference [@sakana2025ai]. The peer-reviewed account appeared in *Nature* in March 2026. It reports that the generated manuscript "passed the first round of peer review" for a workshop with an acceptance rate of 70%. Its abstract names a risk: such systems could end up "taxing overwhelmed review systems and adding noise to the scientific literature" [@lu2026towards]. According to the company's summary, an automated reviewer built by the team agreed with human accept/reject decisions with a balanced accuracy of 69%. The system still produces naive ideas, struggles with methodological rigour, makes errors such as inaccurate citations, and is limited to computational experiments. The developers say they watermark the papers it generates and call on the scientific community to set norms for how such work should be treated [@sakana2026ai].

### Do AI-generated ideas survive execution?

Whether AI can generate good research ideas has been tested directly. Si, Yang and Hashimoto at Stanford recruited 49 expert researchers in natural-language processing to write research ideas and 79 to review, blind, those ideas alongside ideas generated by a language-model agent. The AI ideas were judged more novel (mean 5.64 against 4.84 on a 10-point scale; *p* < 0.01) and slightly weaker on feasibility [@si2024can]. The same group then ran the next experiment. They recruited 43 expert researchers to carry out randomly assigned ideas from both groups. Each spent more than 100 hours implementing the idea and writing a short paper, and the results were reviewed blind. After execution, human ideas kept almost exactly their earlier scores, while the AI ideas' scores fell by 1.05 points for novelty, 1.76 for excitement and 1.88 for effectiveness. On several measures the ranking flipped and human ideas scored higher [@si2025ideationexecution]. Both studies were later accepted at ICLR, a peer-reviewed machine-learning conference (in 2025 and 2026), but they cover one field with modest samples. They nonetheless show the central difficulty: an idea that reads well is not yet a result, and only doing the work reveals the difference.

### Kosmos: long runs and graded statements

Kosmos, from the company Edison Scientific, is described in a preprint [@mitchener2025kosmos]. Given a research objective and a dataset, it runs for up to 12 hours, alternating between a data-analysis agent and a literature-search agent that share a structured record of what has been found. In an average run it executes about 42,000 lines of code and reads about 1,500 papers. Independent scientists graded 102 statements from three of its reports and judged 79.4% accurate. Statements based on data analysis or the literature fared best; those that synthesise and interpret findings were accurate only 57.9% of the time (Table 6.3). One reported finding, in materials science, reproduced a human result about perovskite solar cells: that humidity during a manufacturing step strongly affects their performance. That result was available at the time only in a preprint that Kosmos had not accessed.

By counting papers read and analyses run at fixed times per task, the Kosmos authors estimated that a run replaces about 4.1 months of expert work. Seven collaborating groups, asked directly, estimated about 6 months for the findings of a 20-cycle run [@mitchener2025kosmos]. The estimates come from the developers and their collaborators, and the time needed to check the output is not subtracted.

| System or study | Evaluated by | Setting | Main result |
|---|---|---|---|
| The AI Scientist, v1 | Independent researchers (Beel et al.) | Machine-learning research, end to end | 42% of experiments failed through coding errors; median 5 citations; some hallucinated results; USD 6–15 and about 3.5 h human time per paper |
| The AI Scientist, v2 | Workshop reviewers (blind to which papers were AI-written) | 3 papers submitted to an ICLR 2025 workshop | 1 of 3 scored above average acceptance threshold (6, 7, 6); withdrawn as agreed; workshop acceptance rate 70% |
| LLM idea generation | 79 expert reviewers (Si et al.) | 49 ideas per condition, natural-language processing | AI ideas rated more novel (5.64 vs 4.84 of 10), slightly less feasible |
| Execution of those ideas | Blind expert reviewers (Si et al.) | 43 researchers, >100 h each | AI ideas lost 1.05–1.88 points on novelty, excitement and effectiveness after execution; human ideas almost unchanged on these |
| Kosmos | Independent scientists | 102 statements from 3 reports | 79.4% accurate overall; 85.5% data analysis, 82.1% literature, 57.9% synthesis and interpretation |

: Table 6.3: Evaluations of systems that automate parts of research. Settings, raters and scales differ between rows. Source: [@beel2025evaluating; @sakana2025ai; @lu2026towards; @si2024can; @si2025ideationexecution; @mitchener2025kosmos].

Across these evaluations, the steps that can be checked mechanically (did the code run, does the cited paper say this) are where the systems are most reliable. Interpretation and judgement of what is worth doing are the least reliable, and they are the steps readers most need to trust.

### Code nobody has read

Much of modern science is computation, and coding assistants (Chapter 5) now write research software. Kosmos writes tens of thousands of lines per run; AlphaEvolve is itself a coding agent. In a blog post, the software engineer Addy Osmani uses the term **comprehension debt** for "the growing gap between how much code exists in your system and how much of it any human being genuinely understands" [@osmani2026comprehension]. In a commercial product, unread code is a maintenance problem. In research, the code *is* part of the method: if nobody has read the analysis script, nobody can say with confidence what was measured.

## 6.8 Epistemic risks: reproducibility, understanding and the shape of science

Machine learning brought its own reproducibility problems to science before generative AI arrived. Kapoor and Narayanan surveyed fields that had adopted machine-learning methods and found **data leakage**, in which information from the test data seeps into training so that performance looks better than it is, in 17 fields, affecting 294 papers [@kapoor2023leakage]. They also reanalysed political-science studies that predicted the onset of civil wars. Complex models had appeared to beat traditional statistics by a wide margin; once the errors were corrected, they did "not perform substantively better than decades-old" logistic regression models. Their remedy is "model info sheets", on which authors document how they guarded against each type of leakage.

The cases above show that AI-assisted claims are only as strong as the check that follows them, and checks differ greatly in strength. A Lean proof is checked completely by a machine, provided the statement is right. A weather forecast is checked against reality within days, thousands of times a year. A protein structure is checked against blind experimental data. A predicted crystal is checked only when a skilled chemist makes and examines it, which happens for a small fraction of candidates and can take years. An AI-written paper is checked by peer reviewers who are already overloaded. The inner ring of Figure 6.1 marks these checks. Where verification is cheap, AI accelerates science; where it is expensive, AI mainly accelerates the production of claims.

The same cases suggest remedies. Checking can be built into the method, as with model info sheets, proofs that come with a Lean certificate and labelled AI-generated papers [@kapoor2023leakage; @sothanaphan2026resolution; @sakana2026ai]. Independent reanalysis, which corrected the GNoME and A-Lab record, can be credited as a contribution [@cheetham2024artificial; @leeman2024challenges; @szymanski2026author]. And developers can report the denominator, as the AlphaEvolve paper with Tao did for all 67 problems [@georgiev2025mathematical].

### Illusions of understanding

Messeri and Crockett argue that the danger goes beyond individual errors. AI tools can exploit human cognitive limits and create **illusions of understanding**, in which "we believe we understand more about the world than we actually do" [@messeri2024artificial]. Researchers who use an AI model of a phenomenon may believe they understand the phenomenon more deeply than they do (an *illusion of explanatory depth*). They may believe they are testing all hypotheses when they are testing only those that AI tools can handle (*exploratory breadth*). And they may treat an AI system as having no point of view, although it reflects the standpoints of its training data and its developers (*objectivity*). The cumulative risk, they argue, is a **scientific monoculture** in which some methods and questions crowd out others, so that science may "produce more but understand less".

The monoculture argument now has large-scale evidence behind it. Hao, Xu, Li and Evans used a language model to identify AI-augmented papers (validated against expert labels with an F1 score of 0.875) in 41.3 million research papers across the natural sciences [@hao2026artificial]. Scientists who used AI tools published 3.02 times as many papers, received 4.84 times as many citations and became research project leaders 1.37 years earlier than those who did not. Collectively, however, AI adoption was associated with a 4.63% shrinkage in the volume of scientific topics studied and a 22% decrease in scientists' engagement with one another's work, as AI-augmented research moved "towards areas richest in data". The study is observational, so the associations do not prove that AI tools cause the narrowing; but it is the pattern Messeri and Crockett predicted, measured across a whole literature.

### Intellectual debt

In 2019 the legal scholar Jonathan Zittrain named a related idea. Using techniques that work before anyone can explain why, "answers first, explanations later", accrues what he calls **intellectual debt**; sometimes the debt is paid off quickly, and sometimes it compounds for decades. Machine learning, Zittrain argued, greatly expands the capacity to borrow, because it produces accurate predictions without the theories that would tell us when to stop trusting them [@zittrain2019hidden]. The weather results are a case in point. A model that forecasts well on average can fail on the unprecedented storm, and without a theory of what it has learned, the boundary is found only by testing, as Sun and colleagues did [@sun2025can].

::: {.box .debate}
**Debate: Will AI make science faster but shallower?**

*Faster and deeper.* AlphaFold has been used by more than two million people to form and test hypotheses [@royal2024nobelchemistry], and blind tests and independent comparisons show where they can be trusted [@kryshtafovych2021critical; @terwilliger2024alphafold]. FunSearch and AlphaEvolve return programs and constructions that mathematicians can read, generalise and, in at least one case, formalise in Lean [@romeraparedes2024mathematical; @georgiev2025mathematical]. Weather centres adopted AI models after verifying them against real weather, and run them beside physics-based systems [@ecmwf2025ecmwfs; @noaa2025noaa]. On this view, AI takes over the parts of research that can be checked and frees people for the parts that cannot.

*Faster but shallower.* GNoME produced hundreds of thousands of candidates, and the expert scrutiny needed to assess them took years [@cheetham2024artificial; @szymanski2026author]. AI-generated research ideas look more novel than human ones until somebody executes them [@si2025ideationexecution], and Kosmos is least accurate exactly when it interprets [@mitchener2025kosmos]. Across 41.3 million papers, AI adoption is associated with more output per scientist and a narrower range of topics [@hao2026artificial].

The Hao et al. study measures breadth and engagement; it does not measure understanding. The question would turn on evidence nobody has yet gathered at scale. One measure is how often AI-assisted findings in a field are later independently replicated, compared with similar findings made without AI. Others would test whether researchers using AI tools can explain and extend their results as well as those who do not, and whether the topic narrowing persists once AI tools move beyond data-rich areas.
:::

The results that have held up rest on infrastructure built by people and by older methods: the Protein Data Bank and CASP, physics-based data assimilation and reanalysis, the Lean checker and its library. The models share one weakness, at the edge of their experience: the Category 5 storm a model never saw, the warmer climate outside the record, the disordered crystal that a zero-temperature calculation treats as ordered. Independent evaluations, from the crystallographic comparison of AlphaFold to the graded USAMO proofs, have repeatedly found less than the first announcement claimed while confirming that something real had been achieved. How much AI-assisted science survives such scrutiny is the figure the field still lacks.

## Further reading

- Jumper, J. et al. (2021). *Highly accurate protein structure prediction with AlphaFold*. The primary account of AlphaFold 2, with the architecture, the CASP14 results and the authors' own statement of where the method is weak. [@jumper2021highly]
- Terwilliger, T. C. et al. (2024). *AlphaFold predictions are valuable hypotheses and accelerate but do not replace experimental structure determination*. A short, careful independent comparison of predictions with experimental maps that shows what "very high confidence" means in practice. [@terwilliger2024alphafold]
- Rasp, S. et al. (2024). *WeatherBench 2*. Explains the skill scores used to compare weather models and is unusually frank about what they miss, including blurring and extremes. [@rasp2024weatherbench]
- Cheetham, A. K. & Seshadri, R. (2024). *Artificial intelligence driving materials discovery?* A constructive model of how domain experts can scrutinise a large AI discovery claim. [@cheetham2024artificial]
- Georgiev, B., Gómez-Serrano, J., Tao, T. & Wagner, A. Z. (2026). *Mathematical discovery and exploration can be done at scale*. The most complete record of what an AI search system achieved and failed to achieve across 67 mathematical problems. [@georgiev2025mathematical]
- Messeri, L. & Crockett, M. J. (2024). *Artificial intelligence and illusions of understanding in scientific research*. The clearest framework for the epistemic risks of AI in research, written for scientists in every field. [@messeri2024artificial]


# Chapter 7: Chips, Data Centres, Energy and Open Models

The government of Alberta, a Canadian province, set out to attract data centres. Requests to connect new data centres to its grid soon reached 16 gigawatts (GW), more than the province's entire peak electricity demand. In 2025 the grid operator imposed a temporary cap of 1.2 GW to protect the reliability of the system [@iea2026key, sec. 3]. A gigawatt is roughly the output of one large power station. The International Energy Agency (IEA) warns that such connection queues are "not a reliable indicator of future demand, as only a limited and uncertain share of the pipeline may ultimately be realised" [@iea2026key, sec. 1].

Every answer from a chatbot is computed on physical machines, in buildings that draw electricity from real grids, using chips made in a handful of factories with tools from one supplier. That physical layer explains why AI is expensive, why a few firms dominate it, why chips have become an instrument of foreign policy and why releasing a model's weights is contested.

## 7.1 How AI accelerators work

Training and running a neural network consists mostly of multiplying large matrices (Section 2.6), and the quantities are vast. By the rule of thumb derived in Section 4.1, pre-training the Chinese open-weight model DeepSeek-V3 took about 3.3 × 10^24^ floating-point operations (FLOP) [@deepseekai2024deepseekv3]. How fast a chip gets through such work depends as much on how quickly it can be fed with data as on its arithmetic units.

### Inside a GPU

A general-purpose central processing unit (CPU) devotes much of its silicon to running varied instructions quickly one after another. A graphics processing unit (GPU) instead contains many simpler processors that apply the same operation to many numbers at once. Nvidia's H100, announced in March 2022, packs 80 billion transistors onto a die of 814 mm² made on a customised TSMC process called 4N [@nvidia2022hopper; @andersch2022nvidia]. The H100 SXM5 version used in servers has 132 streaming multiprocessors (SMs), each with four **tensor cores**, 528 in all, which NVIDIA's engineers describe as "specialized high-performance compute cores for matrix multiply and accumulate (MMA) math operations" [@andersch2022nvidia]. A tensor core multiplies small blocks of two matrices and adds the result to a running total as one operation, rather than as many separate instructions. Per SM and per clock cycle, the H100's tensor cores deliver twice the matrix throughput of its predecessor, the A100.

GPUs are one kind of **AI accelerator**, a chip specialised for the arithmetic of machine learning. Others were designed from the start for neural networks. Google's first Tensor Processing Unit (TPU), deployed in its data centres from 2015, was built around a grid of 65,536 8-bit multiply-accumulate units with a peak of 92 trillion operations per second. In a 2017 paper Google's engineers reported that on Google's own inference workloads it was on average about 15 to 30 times faster than the contemporary GPU and CPU it was compared with. It also delivered 30 to 80 times more operations per watt [@jouppi2017indatacenter]. The comparison was with an Nvidia K80; later GPUs narrowed the gap.

### Memory bandwidth: the usual bottleneck

The weights of a large model do not fit in the small, fast memory on the processor die, so they sit in **high-bandwidth memory (HBM)**. HBM consists of stacks of memory chips placed in the same package as the processor and joined to it by thousands of wires. The H100 SXM5 has five HBM3 stacks connected through ten 512-bit memory controllers, a 5,120-bit interface [@andersch2022nvidia]. NVIDIA's product specification gives 80 GB of memory and a bandwidth of 3.35 terabytes per second (TB/s) [@nvidia2026h100].

The balance between arithmetic and memory speed decides how fast real workloads run. The H100 can perform about 990 trillion 16-bit operations per second in ordinary ("dense") matrix arithmetic. It therefore runs at full speed only on work that performs roughly 300 operations for every byte it reads from memory (calculation by the author from the specification). Generating text one token at a time falls far short of that. Each 16-bit weight occupies two bytes and is used for one multiplication and one addition per token, so a single user's request performs only about one operation per byte. A 70-billion-parameter model stored at 16 bits occupies 140 GB, more than one H100 holds, and merely reading those weights once takes about 42 milliseconds per token, however many arithmetic units sit idle. Serving systems therefore process many users' requests together ("batching") so that each weight fetched from memory is used many times.

This imbalance has grown. In an analysis published in *IEEE Micro*, Gholami and colleagues found that over the past 20 years peak server hardware FLOPS rose about 3.0 times every two years, against 1.6 times for memory bandwidth and 1.4 times for interconnect bandwidth. They conclude that memory bandwidth has become the main bottleneck for decoder models such as chatbots, particularly when serving them [@gholami2024ai]. The same problem was visible in the first TPU: its designers estimated that equipping it with the faster memory of the GPU it was compared with would have tripled its achieved performance [@jouppi2017indatacenter].

### Number formats

Fewer bits per number mean more numbers per second through the same memory, more operations per unit of chip area and less energy per operation. The price is less range (how large and small a number can be) and less precision (how finely values are distinguished). A floating-point number has a sign bit, exponent bits that set its range and mantissa bits that set its precision. Table 7.1 compares the formats used in AI.

| Format | Sign, exponent, mantissa bits | Largest normal value | Main use in AI |
|---|---|---|---|
| FP32 | 1, 8, 23 | 3.40 × 10^38^ | Master copy of weights; accumulation |
| FP16 | 1, 5, 10 | 65,504 | Mixed-precision training since 2017 |
| BF16 | 1, 8, 7 | 3.39 × 10^38^ | Training without loss scaling |
| FP8 (E4M3) | 1, 4, 3 | 448 | Weights and activations |
| FP8 (E5M2) | 1, 5, 2 | 57,344 | Gradients, which need more range |

: Table 7.1: Floating-point formats used in AI computing. More exponent bits give more range, more mantissa bits give more precision. Largest normal values computed by the author from the bit layouts; Kalamkar et al. print BF16's as 3.38 × 10^38^ (truncated). Source: [@micikevicius2017mixed; @kalamkar2019study; @micikevicius2022fp8].

Each step down the table was made usable by a training technique. In 2017, researchers from Baidu and NVIDIA showed that networks could be trained with weights, activations and gradients stored in 16-bit FP16, provided a 32-bit master copy of the weights accumulated the updates. Without it, any update smaller than 2^−24^ becomes zero in FP16, and in one of their models about 5% of weight gradients were that small. They also multiplied the loss by a scaling factor so that small gradients stayed within FP16's range [@micikevicius2017mixed]. The bfloat16 (BF16) format, first used mainly within Google's ecosystem, keeps FP32's 8 exponent bits and so its range, giving up precision instead. A 2019 study by Intel and Facebook researchers found that BF16 training matched FP32 results across image, speech, language and recommendation tasks without changing hyperparameters [@kalamkar2019study].

Eight-bit floating point (FP8) followed. A 2022 proposal by NVIDIA, Arm and Intel engineers defined two encodings, E4M3 and E5M2, and reported that FP8 training matched 16-bit results on models of up to 175 billion parameters [@micikevicius2022fp8]. Unlike the A100, the H100 supports FP8 in its tensor cores, which, according to the company, "halves data storage requirements and doubles throughput compared to FP16 or BF16" [@andersch2022nvidia]. DeepSeek-V3's developers describe it as the first validation of FP8 training on an "extremely large-scale model". They scaled values in small groups (1 × 128 elements for activations and 128 × 128 for weights) so that occasional extreme values did not swamp the others. They also worked around a limitation of their chip, the H800, an Nvidia GPU that could be sold to China until the US tightened its export rules in 2023 (Section 7.3). Its FP8 matrix units accumulated sums with only about 14 bits of precision. They reported that the relative loss error of FP8-trained test models, trained on about a trillion tokens, stayed below 0.25% of BF16 baselines [@deepseekai2024deepseekv3]. NVIDIA's next architecture, Blackwell, added 4-bit floating point with scaling factors applied to small blocks of numbers [@nvidia2024blackwell].

Precision is also the main trap in reading chip specifications. NVIDIA quotes the H100's 16-bit performance as 1,979 TFLOPS "with sparsity", a figure that depends on a feature exploiting zero-valued weights; for its newer systems it states that dense performance is half the sparse figure [@nvidia2026h100; @nvidia2026hgx]. Google described its 2025 Ironwood TPU pod as delivering "more than 24x the compute power" of El Capitan, the world's largest supercomputer [@vahdat2025ironwood]. El Capitan's 1.742 exaflops were measured with the HPL benchmark, which counts double-precision (64-bit) operations [@top5002025june; @top5002026linpack], whereas Google's chart notes indicate that Ironwood's figures refer to 8-bit arithmetic, so the comparison sets unlike quantities against each other.

### Interconnects and systems

Training a frontier model requires thousands of accelerators to exchange partial results constantly, so the links between chips limit performance as well as the chips themselves. Within a server, NVIDIA's NVLink connects GPUs directly: the H100 has 18 NVLink links giving 900 GB/s in total, seven times the 128 GB/s of the standard PCIe Gen 5 connection [@andersch2022nvidia]. Between servers, data travels over networks such as InfiniBand. DeepSeek-V3, for example, was trained on 2,048 H800 GPUs arranged in nodes of eight, linked by NVLink within each node and InfiniBand between nodes [@deepseekai2024deepseekv3].

The Blackwell GPU, announced in March 2024, joins two dies, each as large as the lithography process allows, through a 10 TB/s chip-to-chip link into a single GPU (Table 7.2). Its GB200 NVL72 rack combines 72 such GPUs and, according to the company, delivers 1.4 exaflops of AI performance with 30 TB of fast memory [@nvidia2024blackwell]. An eight-GPU DGX B200 server draws about 14.3 kW at maximum [@nvidia2026dgx].

Google has taken a different route to scale. Its TPU v4 supercomputer of 4,096 chips uses optical circuit switches that can reconfigure the network's topology; Google's engineers report that the optical components cost less than 5% of the system and draw less than 3% of its power [@jouppi2023tpu]. Ironwood, announced in April 2025, scales a pod to 9,216 chips [@vahdat2025ironwood].

| | NVIDIA H100 SXM (2022) | NVIDIA B200 (2024) | Google TPU Ironwood (2025) |
|---|---|---|---|
| Transistors | 80 billion | 208 billion (two dies) | not published |
| Peak dense 16-bit (TFLOPS) | ≈ 990 | ≈ 2,250 | not published |
| Peak 8-bit (TFLOPS) | ≈ 1,980 (dense) | ≈ 4,500 (dense) | 4,614 (peak) |
| HBM capacity | 80 GB | 180 GB | 192 GB |
| HBM bandwidth | 3.35 TB/s | 8 TB/s | 7.37 TB/s |
| Chip-to-chip bandwidth | 900 GB/s | 1.8 TB/s | 1.2 TB/s |

: Table 7.2: Three AI accelerators as specified by their makers. H100 dense figures are half the "with sparsity" figures on NVIDIA's product page; B200 figures are NVIDIA's eight-GPU system figures divided by eight (arithmetic from HGX B200, memory from DGX B200: 1,440 GB and 64 TB/s), with sparse arithmetic figures halved as NVIDIA's footnote instructs (calculation by the author). Google does not state whether Ironwood's peak is dense or sparse. Source: [@nvidia2022hopper; @nvidia2026h100; @nvidia2024blackwell; @nvidia2026hgx; @nvidia2026dgx; @vahdat2025ironwood].

The IEA estimates that over the past decade leading AI processors improved performance per watt by roughly 30–40% a year, with gains slowing as transistor scaling matures [@iea2026key, sec. 2.2]. Google states that Ironwood doubles the performance per watt of its previous TPU [@vahdat2025ironwood]. But each chip draws more power: an H100 SXM is rated at up to 700 W, against 400 W for the A100 [@andersch2022nvidia]. Measurements cited by Lawrence Berkeley National Laboratory found that eight-GPU H100 servers running AI training averaged 74% of their rated power [@shehabi2024united].

The 2026 AI Index, drawing on Epoch AI's data, puts worldwide AI computing capacity at roughly 17.1 million "H100-equivalents" in 2025, growing about 3.3 times a year since 2022 (Epoch's own dashboard gives 3.4 times; Section 4.4). Nvidia chips account for over 60%, with Google and Amazon supplying much of the remainder and Huawei a small but growing share [@sajadieh2026ai, ch. 1]. The commercial weight of this demand is visible in Nvidia's accounts. In its fiscal year ending January 2026 the company reported revenue of $215.9 billion, of which sales to the data-centre market contributed $193.7 billion, up from $47.5 billion two years earlier [@nvidia2026form].

## 7.2 The semiconductor supply chain and its chokepoints

A chip passes through several specialised industries before it reaches a data centre, and each stage is dominated by very few firms. Figure 7.1 shows the stack, from the machines that make chips at the bottom to the applications people use at the top.

![Figure 7.1: The AI supply chain as a stack. Each layer depends on the one below, and several layers are dominated by one or a few firms (named examples are illustrative, not exhaustive). The marked chokepoints (extreme-ultraviolet lithography, leading-edge fabrication, and high-bandwidth memory with advanced packaging) are where governments have focused export controls. Diagram by the author, based on @sajadieh2026ai, @asml2026annual and @tsmc2026annual.](../figures/svg/fig-07-01.svg){#fig:07-01}

### Lithography

Chips are made by projecting circuit patterns onto light-sensitive coatings on silicon wafers, layer after layer; the finest features need the shortest wavelengths. **Extreme-ultraviolet (EUV) lithography** uses light with a wavelength of 13.5 nanometres, and ASML of the Netherlands states that it is "currently the world's only manufacturer of EUV lithography systems" [@asml2026annual]. ASML recognised revenue on 48 EUV systems in 2025, out of 327 lithography systems sold, on total net sales of €32.7 billion. The next generation, "High-NA" EUV with a larger lens aperture for finer features, shipped its first production-ready system in 2025, and ASML expects it to support high-volume manufacturing from 2027.

ASML in turn depends on others. Carl Zeiss SMT is its sole supplier of lenses, mirrors and other critical optics, under an exclusive arrangement. ASML warns that the number of systems it can build "is limited by the production capacity" of Zeiss [@asml2026annual]. ASML needs export licences for EUV systems and for certain deep-ultraviolet (DUV) immersion systems, the previous generation of tools. China nonetheless remains a large market for older tools: customers there accounted for 29.1% of ASML's 2025 net sales, down from 36.1% in 2024.

### Fabrication

Above lithography sits **fabrication**. Firms such as Nvidia, AMD and Google design chips but do not make them; they send their designs to foundries. The Taiwan Semiconductor Manufacturing Company (TSMC) dominates the leading edge. According to the 2026 AI Index, it "fabricates virtually every leading AI chip", including Nvidia's Blackwell GPUs and AMD's MI300X [@sajadieh2026ai, ch. 1]. TSMC's own annual filing shows how AI has reshaped its business [@tsmc2026annual]. Its 2025 revenue was NT$3,809 billion (US$121.4 billion). High-performance computing, the category that includes AI accelerators, supplied 58% of it, up from 43% in 2023. Its 2-nanometre process entered volume production in 2025.

The concentration runs in both directions. TSMC's ten largest customers provided 78% of its 2025 revenue; the largest alone provided 19% and the second 17%. TSMC spent about US$40.9 billion on capital expenditure in 2025 and expected US$52–56 billion in 2026, partly for advanced packaging [@tsmc2026annual]. It is building fabs in Arizona, where its first fab entered high-volume production at the end of 2024, in Kumamoto in Japan and in Dresden in Germany [@tsmc2026annual; @sajadieh2026ai, ch. 1]. Even so, the AI Index still describes the AI hardware supply chain as dependent on one foundry in Taiwan.

### Memory and packaging

After fabrication, chips are **packaged**: the processor dies and their HBM stacks are combined in one package that supplies power, removes heat and carries data between them. Nvidia's annual report states that it uses TSMC's CoWoS ("chip on wafer on substrate") technology for this step. TSMC describes CoWoS as one of its services for integrating several chips "to meet customer requirements for high performance, high compute density" and low latency [@nvidia2026form; @tsmc2026annual]. Packaging and testing are also done by specialist firms such as ASE Group in Taiwan and Amkor Technology in the United States. The leading HBM makers are SK Hynix and Samsung of South Korea and Micron of the United States [@sajadieh2026ai, ch. 1].

These later stages became the binding constraints of the AI build-out. The IEA reports that packaging capacity for high-end chips limited production in 2025. From the second half of 2025, memory became the tighter limit [@iea2026key, sec. 1]. In 2023, leading GPU systems included less than 150 GB of memory; by 2027 the figure is expected to exceed 1,000 GB. Producing HBM takes about three times as much wafer capacity per gigabyte as conventional memory, and memory prices rose by an order of magnitude between late 2024 and early 2026. A new chip factory takes about two years to bring into operation, and analysts cited by the IEA estimate that current HBM production can support at most about 25 GW of AI servers a year to 2027 [@iea2026key, sec. 1]. The IEA expects the shortage to last "through at least the end of 2027" [@iea2026key, Executive Summary].

Disruptions elsewhere propagate quickly. The IEA described how a conflict in the Middle East in 2026 disrupted supplies of helium from Qatar, which had supplied roughly a third of the world's helium. Helium is used to cool and clean chip-making equipment and has, according to the IEA, no substitute with equivalent properties [@iea2026key, Box 1.1]. Power equipment is also scarce: lead times for transformers average two to three years, and gas turbine deliveries can take around five years after orders rose 70% in 2025 [@iea2026key, sec. 1].

::: {.box .concept}
**Concept: Chokepoint**

A chokepoint is a stage in a supply chain that very few suppliers control and that others cannot easily replace. In AI hardware the clearest examples are EUV lithography (one supplier, itself dependent on one optics maker), leading-edge fabrication (mainly one foundry), and HBM and advanced packaging (three memory makers and limited packaging lines). Chokepoints give whoever controls them leverage, which is why export controls target them, and they create shared vulnerability: a shortage, accident or conflict at one point can delay production worldwide.
:::

## 7.3 Export controls and the geopolitics of compute

The most important firms in the chain are based in the United States or allied countries. That has allowed the US government to use **export controls**, legal requirements to obtain a licence before selling certain goods abroad, to limit which countries can obtain advanced AI chips and chip-making tools. The US rules are written by the Commerce Department's Bureau of Industry and Security (BIS). Figure 7.2 summarises the main steps.

![Figure 7.2: Main US export-control measures on advanced AI chips and related items, October 2022 to July 2026. The direction of policy changed in 2025: rules continued to restrict China, while the global licensing framework of January 2025 was abandoned before it took full effect and replaced by country-by-country arrangements. Source: @bis2022implementation; @bis2023implementation; @bis2024foreignproduced; @bis2025framework; @bis2025department; @nvidia2025form; @bis2025expansion; @bis2025one; @bis2026revision; @bis2026enhanced.](../figures/svg/fig-07-02.svg){#fig:07-02}

### Drawing the line

The first major rule, effective on 7 October 2022, imposed licence requirements on advanced computing chips, on computers containing them and on certain chip-manufacturing equipment, mainly aimed at China [@bis2022implementation]. It defined a controlled chip by two tests together: processing performance (bit length multiplied by trillions of operations per second) of 4,800 or more, and an aggregate chip-to-chip data transfer rate of 600 GB/s or more. A chip that fell below either line was free to ship. Chip designers responded with China-specific products designed to comply [@nvidia2026form].

The October 2023 revision dropped the transfer-rate test. It replaced it with **total processing performance** (TPP): twice the peak multiply-accumulate rate in trillions per second, multiplied by the bit length of the operation. Chips with a TPP of 4,800 or more are controlled. So are chips with a TPP of 1,600 or more whose "performance density" (TPP per square millimetre of die) is 5.92 or more, and a second tier catches somewhat less dense chips [@bis2023implementation]. The rule counts dense, not sparse, performance. By the H100's dense 8-bit figure, its TPP is about 1,979 × 8 ≈ 15,800 and its density about 19 per mm², far above both lines (calculation by the author). Nvidia told investors that the revised rule required licences for exports to China and several other countries of chips "including but not limited to the A100, A800, H100, H800, L40, L40S, and RTX 4090" [@nvidia2023form]. The A800 and H800, sold in China under the first rule, were now caught. In December 2024 BIS added further controls on chip-making equipment and, for the first time, on certain high-bandwidth memory [@bis2024foreignproduced].

The rules have kept chasing the bottleneck that matters. In April 2025 the US government told Nvidia that its H20, a chip designed for the Chinese market, needed a licence. The requirement covered "any other circuits achieving the H20's memory bandwidth, interconnect bandwidth, or combination thereof" [@nvidia2026form]. That wording reflects Section 7.1: for running models, memory bandwidth can matter more than peak arithmetic. Nvidia took a $4.5 billion charge for excess H20 inventory and purchase obligations. In August 2025 it received licences for certain H20 sales, generating about $60 million in revenue. According to Nvidia's annual report, US officials said they expected the government to receive 15% or more of the revenue from licensed sales of its products, but no regulation codifying this was published. Its revenue from customers headquartered in China (including Hong Kong) fell from $25.0 billion in fiscal 2025 to $19.7 billion in fiscal 2026 [@nvidia2026form].

### The diffusion rule and after

In January 2025 the outgoing Biden administration published a broader **Framework for Artificial Intelligence Diffusion**. It extended licence requirements for advanced chips to most of the world and sorted countries into tiers with different levels of access. It also added a new control on the weights of certain advanced closed-weight AI models [@bis2025framework]. On 13 May 2025, two days before the compliance date, the new administration announced that it would rescind the rule, which it said "would have stifled American innovation", instructed officials not to enforce it and promised a replacement [@bis2025department]. In July 2026 the worldwide licence requirement still appeared in the regulations, but BIS stated that it was enforcing it only for certain destinations, mainly countries of concern such as China [@bis2026enhanced].

Policy then moved in several directions at once. In September 2025 BIS extended Entity List restrictions automatically to any company at least 50% owned by listed entities [@bis2025expansion], then suspended that rule for a year from 10 November 2025 [@bis2025one]. In January 2026 it changed its review policy for exports to China of Nvidia's H200 and equivalent chips from a "presumption of denial" to "case-by-case review". The conditions include independent testing in the United States and certification that US supply would not be reduced [@bis2026revision]. Nvidia reported that a licence granted in February 2026 allowed small H200 shipments to specific Chinese customers but had produced no revenue. It added that the Chinese government had discouraged customers from buying Nvidia's data-centre products, including those designed to comply with US rules [@nvidia2026form]. A July 2026 rule gave the United Arab Emirates' government and approved companies licence-free access to advanced computing items [@bis2026enhanced]. Allied controls have tightened in parallel. The Netherlands added metrology and inspection equipment to its controls in January 2025, and in November 2025 the European Union extended Dutch licence requirements, including for DUV immersion lithography, to all member states [@asml2026annual].

### Do the controls work?

Supporters point to signs that Chinese developers are short of compute: the IEA describes China's model developers as "compute-constrained due to a lack of access to high-end chips" [@iea2026key, Box 10.1]. Dario Amodei, chief executive of the US developer Anthropic, argued in January 2025 that export controls "serve a vital purpose". Well enforced, he wrote, they "are the only thing that can prevent China from getting millions of chips" [@amodei2025deepseek]. Critics note that constraints spur workarounds. DeepSeek trained V3 on H800s, which the first rule had left uncontrolled, and engineered its software around the chip's limits [@deepseekai2024deepseekv3; @nvidia2023form]. The 2026 AI Index reports that the performance gap between the best US and Chinese models "has effectively closed", with the lead changing hands several times since early 2025 [@sajadieh2026ai, Report highlights]. Neither observation settles the question, because nobody can observe what Chinese labs would have achieved without the controls.

## 7.4 Data centres, electricity and water

A **data centre** is a building that houses servers, networking equipment, power supplies and cooling systems; much of their electricity still goes to ordinary cloud computing, streaming and storage rather than AI. Few operators publish measured figures for AI workloads, so most numbers here are estimates whose methods and boundaries differ. The most systematic global estimates come from the IEA, an intergovernmental energy agency, in its April 2025 special report *Energy and AI* [@iea2025energy] and its April 2026 update, *Key Questions on Energy and AI* [@iea2026key].

### How much electricity

According to the 2026 update, global data-centre electricity consumption grew by 17% in 2025, reaching 485 terawatt-hours (TWh) [@iea2026key, Executive Summary]. A terawatt-hour is a billion kilowatt-hours; 485 TWh was about 1.5% of the world's electricity use. Consumption by data centres that focus on AI grew by about 50%. The IEA's Base Case sees total data-centre consumption roughly doubling to about 950 TWh by 2030 (945 TWh in the report's data tables), around 3% of global electricity demand, with AI-focused data centres tripling their use [@iea2026key, Executive Summary and Annex A].

Figure 7.3 shows these figures with the IEA's alternative cases. The Lift-Off Case assumes stronger adoption and resolved bottlenecks in grids, turbines and chips; the High Efficiency Case assumes Base Case demand with faster efficiency gains; the Headwinds Case assumes slower adoption and investment [@iea2026key, sec. 1]. The 2030 spread, from 833 to 1,008 TWh, is a range of projections under assumptions, not a forecast.

![Figure 7.3: Global data-centre electricity consumption, 2023–2025 (IEA estimates), and 2030 under four IEA cases. Data centres used about 1.5% of the world's electricity in 2025; the Base Case reaches about 3% by 2030. Source: @iea2026key, Annex A, Table A.1 (data published April 2026).](../figures/svg/fig-07-03.svg){#fig:07-03}

The global share is modest, but the local share can be large. The IEA notes that data centres accounted for as much as 20–30% of demand in the states, metropolitan areas or regions where they cluster [@iea2026key, sec. 3]. Ireland is the clearest national case: official statistics show that data centres consumed 23% of the country's metered electricity in 2025, up from 5% in 2015 [@cso2026data]. Growth is also concentrated by country. In the IEA's tables the United States accounts for 183 of the world's 416 TWh in 2024 and for 426 of 945 TWh in the 2030 Base Case, with China second and Europe well behind (Figure 7.4) [@iea2026key, Table A.4]. Seen against the whole economy, the IEA expects data centres to account for slightly less than 10% of the growth in global electricity demand to 2030 [@iea2026key, sec. 1].

![Figure 7.4: Data-centre electricity consumption by region, 2024 and 2030 (IEA Base Case). The United States and China account for most of the projected growth. "Rest of world" is the world total minus the three named regions. Source: @iea2026key, Annex A, Table A.4 (data published April 2026).](../figures/svg/fig-07-04.svg){#fig:07-04}

An independent US estimate comes from Lawrence Berkeley National Laboratory (LBNL), whose December 2024 report for the Department of Energy adds up the installed base of servers, storage, networking and cooling [@shehabi2024united; @doe2024doe]. US data-centre use was flat at about 60 TWh a year from 2014 to 2016, then rose to 176 TWh (4.4% of US electricity) in 2023 as GPU-accelerated servers spread, close to the IEA's figure for the following year. Inference accounted for nearly 60% of AI server energy in 2023, though training servers were expected to use about half of it by 2028. For that year the report gives a range of roughly 325 to 580 TWh, or 6.7% to 12% of US electricity. The top of the range is almost twice the bottom, and the authors stress that "the lack of data availability significantly limits the analysis" [@shehabi2024united].

### Energy per query

Table 7.3 collects the main published per-query numbers; their boundaries differ.

| Estimate | Who | Energy per query | What is counted |
|---|---|---|---|
| Median Gemini Apps text prompt, May 2025 | Google staff (preprint) | 0.24 Wh (0.10 Wh on narrow boundary) | Accelerators, host CPU and memory, idle machines, data-centre overhead |
| Average ChatGPT query, 2025 | OpenAI chief executive | 0.34 Wh | Not disclosed |
| Typical GPT-4o query, 500 output tokens | Epoch AI | ≈ 0.3 Wh (range 0.1–4) | Modelled from assumed hardware and utilisation |
| Short GPT-4o query | AI Index, from outside estimates | ≈ 0.42 Wh | Modelled |
| Text generation, open models (per inference) | Luccioni et al. | 0.047 Wh on average | Measured on GPUs, small models |
| Image generation, open models (per inference) | Luccioni et al. | 2.9 Wh on average | Measured on GPUs |

: Table 7.3: Published estimates of the energy used per AI query or inference. Figures are not comparable across rows: models, hardware, output lengths and system boundaries differ. Source: [@elsworth2025measuring; @altman2025gentle; @you2025much; @sajadieh2026ai; @luccioni2024power].

The only figures from a provider's own infrastructure come from Google. In a preprint by its staff, Google measured the median text prompt to its Gemini Apps in May 2025 at 0.24 watt-hours (Wh). The active accelerators accounted for 58% of this; the rest went to host CPUs and memory, provisioned but idle machines and data-centre overhead. Counting only the active accelerators, on a sample of highly utilised machines, as many earlier studies did, gave 0.10 Wh. The company reports that energy per prompt fell 33-fold in a year [@elsworth2025measuring]. A median says nothing about the long tail of long or complex prompts, and the measurement cannot be checked from outside. OpenAI's chief executive Sam Altman wrote in June 2025 that "the average query uses about 0.34 watt-hours", without describing the method [@altman2025gentle].

Outside estimates show how sensitive the figure is to assumptions. Epoch AI, a research institute, estimated about 0.3 Wh for a typical GPT-4o query. It assumed 500 output tokens, about 100 billion active parameters and H100 GPUs running at 10% computational utilisation, counting server and data-centre overhead in each GPU's power draw; different plausible assumptions gave anything from about 0.1 to 4 Wh. Long inputs change the picture: by the same method a 10,000-token document would cost about 2.5 Wh [@you2025much]. The widely quoted older figure of about 3 Wh comes from a 2023 commentary by Alex de Vries [@devries2023growing]. Epoch traces it mainly to an assumption of 2,000 output tokens per query, together with older A100 servers and peak rather than average power.

Other kinds of output cost far more. In a peer-reviewed study of openly available models, Luccioni, Jernite and Strubell found that generating an image used on average more than 60 times as much energy as generating text [@luccioni2024power]. The IEA adds that video generation can require "hundreds to thousands of times more energy" than a short text query [@iea2026key, sec. 2.1].

Efficiency and demand are moving in opposite directions. The IEA estimates that energy per AI task has fallen "by at least an order of magnitude annually in recent years" [@iea2026key, Executive Summary]. Best-in-class hyperscale facilities now achieve a power usage effectiveness (PUE, total facility energy divided by IT energy) of about 1.1 to 1.2, against 1.5 to 1.7 in older or enterprise sites. Moving from 1.6 to 1.2 cuts total energy use by about a quarter [@iea2026key, sec. 2.2]. Yet the IEA also notes that cheaper AI encourages more use, an instance of the Jevons paradox, so total consumption is set to rise even with rapid efficiency gains [@iea2026key, sec. 2]. The power density of AI servers increased elevenfold between 2020 and 2025, and by 2027 a single rack could have peak demand equal to that of 65 households [@iea2026key, Executive Summary].

### Where the power comes from, and emissions

Grid connection waiting times can reach five to ten years in many jurisdictions. In the second quarter of 2025 alone, 20 US data-centre projects worth an estimated USD 98 billion were blocked or delayed amid local concerns about their environmental and price impacts [@iea2026key, sec. 1]. The tech sector signed around 40% of all corporate renewable power-purchase agreements worldwide in 2025 [@iea2026key, Executive Summary]. In the United States some developers are building gas-fired generation on site; the IEA estimates that 15–27 GW of such capacity might power data centres by 2030 [@iea2026key, Executive Summary].

Nuclear deals have multiplied. Microsoft agreed in 2024 to buy about 835 MW from a restarted Three Mile Island unit, targeted for 2027, and Amazon Web Services agreed in 2025 to take up to 1,920 MW from the Susquehanna plant. Agreements for small modular reactor capacity for data centres had reached about 25 GW by the end of 2024, with a further 20 GW announced in January 2026, although the first commercial units are not expected before about 2030 [@iea2026key, sec. 5.1]. Whatever the mix, the IEA projects that emissions associated with data centres will roughly double, reaching around 350 million tonnes of carbon dioxide in 2035, about 2% of the electricity sector's emissions [@iea2026key, Executive Summary].

Company emissions figures depend on an accounting choice. **Market-based** emissions subtract the clean electricity a company has contracted to buy, while **location-based** emissions use the average carbon intensity of the grids that actually supply its buildings. Google's figures show how far apart the two can be. According to the company, its data-centre electricity use grew by 27% in 2024 while its data-centre energy emissions, counted on the market basis, fell by 12% [@google2025environmental, p. 18]. In its data tables, market-based emissions from purchased electricity were about 3.1 million tonnes in 2024, against about 11.3 million tonnes on the location basis, more than double the 2019 level [@google2025environmental, p. 104]. Both follow recognised rules; they answer different questions, and headlines usually quote the lower one. Google's reported 44-fold cut in emissions per prompt likewise combines efficiency gains with clean-energy purchasing [@elsworth2025measuring].

Training emissions vary with hardware, duration and the grid. The AI Index estimates that training AlexNet in 2012 produced about 0.01 tonnes of carbon dioxide equivalent, xAI's Grok 4 in 2025 about 72,816 tonnes and DeepSeek-V3 about 597 tonnes [@sajadieh2026ai, ch. 1]. These are model-based estimates, made necessary because, as the Index notes, many developers no longer disclose power use for their newest models.

Mistral AI published a life-cycle assessment carried out with the consultancy Carbone 4 and ADEME, the French ecological transition agency. According to the company, training and 18 months of use of its Mistral Large 2 model produced 20.4 thousand tonnes of carbon dioxide equivalent and consumed 281,000 cubic metres of water by January 2025. A 400-token response caused 1.14 grams of emissions and 45 millilitres of water, including a share of hardware manufacturing [@mistral2025our].

### Water

**Water** is the less visible resource. Data centres use water mainly for cooling, often by evaporation, and indirectly through the water used to generate their electricity. **Withdrawal** is water taken from a source; **consumption** is the part that is not returned, mostly because it evaporates. LBNL estimates that US data centres directly consumed 21.2 billion litres in 2014 and 66 billion litres in 2023; hyperscale facilities alone could consume 60 to 124 billion litres in 2028 [@shehabi2024united].

Estimates for AI specifically are rougher. @li2025making estimated that training GPT-3 in Microsoft's US data centres could have directly evaporated about 700,000 litres of fresh water. Counting both cooling water and water used to generate electricity, they projected that global AI demand might account for 4.2 to 6.6 billion cubic metres of water withdrawal in 2027. They stressed that such estimates depend heavily on location, season and the electricity mix. The 2026 AI Index reports estimates that a year of GPT-4o inference consumes about 1.3 to 1.6 million cubic metres, at the high end more than the annual drinking-water needs of 1.2 million people [@sajadieh2026ai, ch. 1].

Per-query water figures differ by two orders of magnitude mainly because of what they count. Google's 0.26 millilitres for a median Gemini text prompt covers only cooling water at its own data centres [@elsworth2025measuring]; Mistral's 45 millilitres per response also includes upstream impacts such as hardware manufacturing [@mistral2025our]. Google reported consuming about 31 billion litres across its data centres and offices worldwide in 2024, 28% more than in 2023. It chose air cooling for a new site at Waltham Cross in England because local water sources were under stress [@google2025environmental]. The same litre matters more in a drought-prone basin than beside a large river, so national totals say little about local impact.

## 7.5 Who can afford frontier AI? Costs and concentration

Section 4.4 sets out what the largest training runs cost and how fast that cost has grown. Much of that account rests on a preprint by Cottier and colleagues at Epoch AI and Stanford. In their data set GPT-4 had the largest amortised hardware and energy cost, about $40 million in 2023 dollars (Epoch's database now gives $37 million; Table 4.3). Extrapolating their growth rate, the authors expected the largest training runs to cost more than a billion dollars by 2027, so that only the best-funded organisations could afford them [@cottier2024rising]. Statements from inside the industry give a sense of the current scale. Amodei wrote that Anthropic's Claude 3.5 Sonnet, "a mid-sized model", cost "a few $10M's to train" [@amodei2025deepseek], and the 2026 International AI Safety Report states that leading models cost "hundreds of millions of dollars to develop" [@bengio2026international].

::: {.box .deeper}
**Going deeper: Estimating the cost of a training run**

The simplest estimate multiplies the time a run takes on its chips by a price per chip-hour:

*cost ≈ number of GPU-hours × rental price per GPU-hour*

DeepSeek reported that pre-training V3 took 2.664 million H800 GPU-hours on its 2,048-GPU cluster; extending the model's context window and post-training added 124,000, for a total of 2.788 million. At an assumed rental price of $2 per GPU-hour this comes to 2,788,000 × $2 = $5.576 million. The company stated that this excludes "the costs associated with prior research and ablation experiments" [@deepseekai2024deepseekv3]. The amortised method of Cottier and colleagues (Section 4.4) instead charges the run for its share of the hardware's working life, plus energy [@cottier2024rising]. A rental-price estimate asks what it would cost someone to repeat the final run; an amortised estimate asks what share of a lab's capital the run consumed. Neither includes salaries, data, failed attempts or the cluster itself, which is why headline training costs understate what it takes to build a frontier model.

The GPU-hours can be checked against the compute estimate of Section 4.1. Spreading about 3.3 × 10^24^ operations over the 2.664 million pre-training GPU-hours (about 9.6 × 10^9^ GPU-seconds) implies an average of about 340 trillion useful operations per second per GPU. (The calculation is the author's; the compute rule ignores attention and other overheads.)
:::

Building the infrastructure costs far more than any training run. Table 7.4 shows what the four largest US cloud and platform companies reported spending on property and equipment, mostly data centres, servers and networking.

| Company | Earlier year (US$ bn) | Latest year (US$ bn) | Change |
|---|---|---|---|
| Amazon (calendar 2024 → 2025) | 83.0 | 131.8 | +59% |
| Microsoft (fiscal years to June 2025 → June 2026) | 64.6 | 115.9 | +80% |
| Alphabet (calendar 2024 → 2025) | 52.5 | 91.4 | +74% |
| Meta (calendar 2024 → 2025) | 37.3 | 69.7 | +87% |

: Table 7.4: Cash spent on property and equipment as reported in annual 10-K filings (company accounts). Figures exclude assets acquired through finance leases. Source: [@amazon2026form; @microsoft2026form; @alphabet2026form; @meta2026form].

Leases add to these sums. Microsoft reported that at the end of June 2026 it had signed additional leases, "primarily for datacenters", worth $329.1 billion that had not yet begun. Some were subject to conditions, and they would start between fiscal years 2027 and 2033 [@microsoft2026form]. According to the IEA, the hyperscalers and newer specialised providers announced capital expenditure of about USD 715 billion for 2026, a 75% increase. That is more than the slightly less than USD 600 billion invested in the entire US energy sector in 2024. The spending will absorb almost all of their cash generation in 2026; in 2025 these normally cash-rich companies issued around USD 200 billion in debt, which ties the build-out to financial markets [@iea2026key, sec. 1].

The AI Index reports that industry produced 91.2% of notable AI models in 2025, with OpenAI, Google and Alibaba the most prolific developers; the United States produced 59 notable models and China 35 [@sajadieh2026ai, ch. 1]. On the supply side, two direct customers alone accounted for 22% and 14% of Nvidia's revenue in fiscal 2026, and customers headquartered in the United States for $149.6 billion of its $215.9 billion [@nvidia2026form]. The United States hosts 5,427 data centres, more than ten times any other country [@sajadieh2026ai, ch. 1]. A few firms' choices about pricing, access, safety practices and openness therefore shape what everyone else can build. At the same time, the AI Index notes, frontier developers now disclose less about their models than before [@sajadieh2026ai, Introduction].

::: {.box .case}
**Case study: The "DeepSeek moment", January 2025**

In late December 2024 the Chinese company DeepSeek released the weights of DeepSeek-V3, with 671 billion parameters (37 billion active for each token), and reported the $5.576 million final-run cost described above [@deepseekai2024deepseekv3]. In January 2025 it released DeepSeek-R1, a reasoning model, under the permissive MIT licence, together with smaller "distilled" versions built on Alibaba's Qwen and Meta's Llama models [@deepseekai2025deepseekr1]. On Monday 27 January 2025 Nvidia's shares fell 17%, removing nearly $600 billion from its market value, as investors questioned whether frontier AI would need as many expensive chips as expected [@milmo2025sputnik].

Later evidence complicated the story. The R1 work was published in *Nature* in September 2025. Its supplementary information gave the cost of turning the V3 base model into R1 as about 147,000 H800 GPU-hours, or about $294,000 at the same assumed $2 rental price. That covered the two reinforcement-learning stages plus the creation of fine-tuning data. It also acknowledged using A100 GPUs for preparatory experiments [@guo2025deepseek]. The low headline figures were real but partial: they excluded earlier research and the company's existing hardware. Amodei argued that V3 was "an expected point on an ongoing cost reduction curve" rather than a break from it [@amodei2025deepseek]. Nvidia's data-centre revenue continued to grow strongly through 2025 [@nvidia2026form]. The episode showed that engineering for efficiency, including FP8 training, can reduce the cost of approaching the frontier, and it drew wide attention to Chinese open-weight models; it did not show that compute had stopped mattering.
:::

## 7.6 Open-weight models

A trained model is a very large file of numbers, its **weights** (or parameters). A **closed-weight** model stays on the developer's servers and is reached through an app or an application programming interface (API), so the developer can monitor use, update the model and withdraw it. An **open-weight** model's weights are published for anyone to download, run and modify, for example by further training ("fine-tuning") on their own data. Between the two lie options such as staged release to researchers. At the open end, EleutherAI's GPT-NeoX was released with weights, data and code and no use restrictions; BigScience's BLOOM released all three subject to licence restrictions on use [@bengio2026international].

::: {.box .concept}
**Concept: Open-weight is not the same as open source**

In software, "open source" means that the source code is available under a licence allowing anyone to use, study, modify and share it for any purpose. For AI, the Open Source Initiative's Open Source AI Definition (version 1.0, October 2024) requires those freedoms plus access to the parameters and the full training code. It also requires information about the training data detailed enough for a skilled person to build a substantially equivalent system [@osi2024open]. Most "open" models release only weights, often under a licence with conditions, so "open-weight" is the more accurate general term.
:::

### What is released, and on what terms

The modern wave of open-weight language models began when Meta released Llama 2 in July 2023, describing it as "free of charge for research and commercial use" [@meta2023meta]. Its licence nonetheless required any company with more than 700 million monthly active users to request a separate licence [@meta2023llama]. In September 2023 the French start-up Mistral AI released Mistral 7B under the permissive Apache 2.0 licence [@mistral2023mistral]. Chinese developers, led by Alibaba's Qwen family and DeepSeek, then became central; the IEA reports that in 2025 "China's models overtook those from developers in the United States in terms of total downloads on open-source platforms" [@iea2026key, Box 10.1]. In August 2025 OpenAI released its first open-weight models since GPT-2 in 2019, gpt-oss-120b and gpt-oss-20b [@openai2025gptoss; @bengio2026international]. Licence terms differ widely, as Table 7.5 shows.

| Model (release) | Licence | Main conditions |
|---|---|---|
| Llama 4 (April 2025) | Llama 4 Community Licence | Firms over 700 million monthly users need Meta's permission; "Built with Llama" notice; multimodal models not licensed to EU-based individuals or companies (end users of products excepted) |
| Gemma 3 (2025) | Gemma Terms of Use | Use restrictions must be passed on; Google may restrict use it believes breaches the terms |
| Mistral Large 2411 (Nov 2024) | Mistral AI Research Licence | Research use only; commercial use needs a separate licence |
| DeepSeek-V3 (Dec 2024) | Custom model licence; MIT for V3-0324 (March 2025) | Original licence carried use-based restrictions; later version permissive |
| DeepSeek-R1 (Jan 2025) | MIT | Commercial use and distillation permitted |
| Qwen3-235B-A22B (April 2025) | Apache 2.0 | Permissive |
| gpt-oss-120b (Aug 2025) | Apache 2.0 | Permissive |
| GLM-5 (Feb 2026) | MIT | Permissive; 744 billion parameters, 40 billion active |

: Table 7.5: Licences of selected open-weight models, from the licence texts and model cards. Source: [@meta2025llama; @google2026gemma; @mistral2024research; @deepseekai2024deepseek; @deepseekai2025deepseekv3; @deepseekai2025deepseekr1; @qwen2025qwen3; @openai2025gptoss; @zai2026glm5].

### How far behind?

In November 2024 Epoch AI estimated that the best open language models had lagged the best closed ones by 5 to 22 months on benchmarks (90% confidence interval), "around one year". The largest open models had lagged the largest closed ones in training compute by about 15 months [@cottier2024how]. The 2026 International AI Safety Report, drawing on Epoch's later capability index, judged that the gap had narrowed and that the leading closed models were "less than one year ahead" [@bengio2026international]. On the Arena leaderboard, where people vote between anonymous answers from two models, the AI Index finds that the best closed model's lead over the best open one shrank from 174 points in May 2023 to 7 points in August 2024. By March 2026, after new closed reasoning models, it had widened again to 49 points (3.4%), between Claude Opus 4.6 and GLM-5 [@sajadieh2026ai, ch. 2].

### Benefits

An influential framework for weighing benefits and risks comes from @kapoor2024position, 25 researchers from academia, industry and civil society. They identify five properties that distinguish open models, such as greater customisability and weak monitoring of use, and argue that these produce benefits for innovation, competition, transparency and the distribution of decision-making power. Businesses and governments can run models on their own computers without sending sensitive data to a vendor, and developers in countries without frontier labs can adapt models to under-resourced languages [@bengio2026international]. The US government's 2025 AI Action Plan made similar points, adding that open models "have geostrategic value" because they may become global standards [@whitehouse2025winning].

### Risks

The risks follow from the same properties. Once weights are published they cannot be recalled; hosting platforms can remove copies, but motivated actors can still obtain them, and developers cannot make users install fixes [@bengio2026international]. Safety training can be removed cheaply. In a preprint, @lermen2023lora showed that with "a budget of less than $200 and using only one GPU" they could fine-tune Meta's Llama 2-Chat 70B so that it refused harmful requests only about 1% of the time on two standard tests. The problem is not unique to open weights: @qi2023finetuning removed the safety behaviour of OpenAI's GPT-3.5 Turbo through the company's own fine-tuning service, using only 10 examples at a cost of less than $0.20. The difference is that a provider can monitor its service and roll out fixes, whereas a downloaded model is beyond reach.

Kapoor and colleagues argue that the key question is **marginal risk**: how much an open model adds to what a malicious actor could already do with search engines, existing tools or closed models. Applying their framework to seven earlier studies of misuse, they judged that the risk analysis was incomplete for six. Their worked examples point in both directions. For automated searches for software vulnerabilities, they judged the marginal risk of open models to be low at present, partly because defenders can use the same tools. For digitally altered intimate images made without consent, they concluded that open image models "pose considerable marginal risk at present": such models need few resources, can be fine-tuned on pictures of specific people and are hard to police once released. They also cite a 2023 study finding that most computer-generated child sexual abuse material had been made with the openly available Stable Diffusion family of image models [@kapoor2024position].

Technical defences are an open research problem. Tamirisa and colleagues, in a paper at ICLR 2025, presented a training method, TAR, designed so that safeguards survive "hundreds of steps of fine-tuning" by an attacker [@tamirisa2024tamper]. The International AI Safety Report notes that filtering harmful material out of training data can resist adversarial fine-tuning about ten times more effectively than defences added after training, and that such techniques are now used in some releases. It also notes that other research has disabled such safeguards, and that their robustness against real attacks remains hard to evaluate [@bengio2026international].

::: {.box .debate}
**Debate: Should the weights of the most capable models be released openly?**

*For openness by default.* @kapoor2024position argue that open models spread power beyond a few companies, enable independent safety research and support competition, and that most claimed misuse risks have not been shown to exceed those of existing technologies. In July 2024 the US National Telecommunications and Information Administration concluded that "current evidence is not sufficient to definitively determine" that restrictions on open-weight models were warranted, and recommended that government "actively monitor" risks instead [@ntia2024dual]. Before releasing gpt-oss, OpenAI fine-tuned it to be as capable as possible in biology and cyber-security. According to the company's preprint, even this version performed below OpenAI's closed o3 model, which it had judged to be under its own "High" risk threshold [@wallace2025estimating]. That is a developer's evaluation of its own product, without independent replication.

*For caution at the frontier.* In a preprint, @seger2023opensourcing accept that open-sourcing has historically brought large net benefits. They argue, however, that for some highly capable future models the risks may be extreme enough that such models "should not be open-sourced, at least not initially". They examine alternatives such as structured access without publishing weights. Cheap removal of safeguards [@lermen2023lora] makes release decisions irreversible, and documented harms from open image models show that marginal risk is not only hypothetical [@kapoor2024position].

Both sides accept that the answer turns on marginal risk at particular capability levels, which makes it an empirical question. Independent evaluations of what open models add to specific harms, repeated as each generation improves, would narrow the disagreement, as would evidence on whether tamper-resistant training survives determined attackers; Chapter 12 discusses such dangerous-capability evaluations.
:::

Open weights lower the cost of entry for firms and countries that cannot afford frontier training, partly offsetting concentration. They also complicate export controls: the January 2025 diffusion rule controlled the weights of certain advanced closed-weight models but left published weights outside its scope, because published information cannot be recalled [@bis2025framework]. A model trained on restricted chips can be downloaded anywhere the day it is published.

## 7.7 Compute governance and sovereign AI

Data and algorithms are hard to observe and easy to copy, so some researchers argue that hardware is an especially practical lever for governing AI. In a preprint, @sastry2024computing, a group of 19 authors including Yoshua Bengio, argue that AI-relevant compute is "detectable, excludable, and quantifiable" and is produced through "an extremely concentrated supply chain". **Compute governance** uses these properties to give public authorities visibility into AI development, allocate resources and enforce rules. Sastry and colleagues also warn of risks to privacy, economic harms and centralisation of power, and propose guardrails such as collecting only the minimum information needed.

Proposals range from paperwork to hardware. Heim and colleagues argue in a preprint that cloud providers could act as record keepers and verifiers. In their view, information the providers already hold, without seeing customers' data, can reveal whether a workload is large-scale training and how much compute it used [@heim2024governing]. Shavit proposed a more ambitious scheme in which chip firmware would occasionally save snapshots of the weights being trained, so that inspectors could later verify what a training run did. Monitoring of the chip supply chain would ensure that no actor could amass untracked chips [@shavit2023what].

Training compute is already used as a regulatory threshold. The EU AI Act presumes that a general-purpose AI model has "high impact capabilities", and is subject to additional obligations, when the computation used for its training exceeds 10^25^ floating-point operations [@europeanparliament2024regulation, Art. 51(2)]. DeepSeek-V3's pre-training used about 3.3 × 10^24^ operations (Section 4.1), a third of the threshold, yet its developers report that it performed comparably to leading closed models of its time [@deepseekai2024deepseekv3]. Efficiency gains of this kind are one reason fixed compute thresholds are contested; Chapter 13 discusses thresholds and their limits.

The same logic of control over compute underlies **sovereign AI**, the effort by governments to secure national access to AI infrastructure and models rather than depending entirely on foreign providers. The 2026 AI Index notes that "AI sovereignty emerged as a central organizing principle" in national policies during 2025 [@sajadieh2026ai, Introduction]. Strategies differ in scale and emphasis:

- **European Union.** In February 2025 the European Commission launched InvestAI, aiming to mobilise €200 billion for AI investment, including a €20 billion fund for four "AI gigafactories", each with around 100,000 of the latest AI chips [@ec2025eu].
- **India.** In March 2024 the Indian cabinet approved over Rs 10,300 crore over five years for the IndiaAI Mission, including a plan for public–private compute capacity of more than 10,000 GPUs [@pib2024cabinet].
- **United Kingdom.** The AI Opportunities Action Plan of January 2025 recommended expanding the country's public AI Research Resource "by at least 20x by 2030" and creating "AI Growth Zones" to speed up data-centre construction [@dsit2025ai].
- **United States.** The July 2025 AI Action Plan called for exporting the "full AI technology stack" (hardware, models, software, applications and standards) to allied countries, so that they would not become dependent on rivals' technology [@whitehouse2025winning].

US private AI investment reached $285.9 billion in 2025, against $12.4 billion in China, although the AI Index cautions that the Chinese figure omits much state funding [@sajadieh2026ai, Report highlights]. A national programme of 10,000 GPUs is small next to the 17.1 million H100-equivalents of global capacity, and Microsoft alone spent $115.9 billion on equipment in its 2026 fiscal year (Table 7.4). For most countries "sovereignty" therefore means reliable access, local data centres or open-weight models adapted to national languages, not training frontier models from scratch.

Sovereign strategies also run into the chokepoints of Section 7.2. A country can build data centres on its own soil and still depend on Nvidia's designs, TSMC's fabs, Korean and American memory and ASML's machines, dependencies shaped by US export policy, as the UAE arrangement of 2026 illustrates [@bis2026enhanced]. Open-weight models offer a partial route to independence at the model layer, which is one reason governments as different as the United States and China have encouraged them [@whitehouse2025winning; @iea2026key, Box 10.1].

Each layer of the stack runs into a scarce input that few suppliers control. Memory bandwidth limits how fast chips serve models, HBM and packaging capacity limit how many accelerators are made, and grid connections and turbines limit where they can run. Export controls are possible because the hardware chokepoints sit mostly in the United States and allied countries, and the rules have followed the bottleneck from arithmetic to memory. Efficiency gains, from FP8 training to cheaper queries, have so far been outrun by demand, so electricity use and capital spending keep rising. Open weights spread access to models far more widely than access to hardware, so the decisions of a few firms and governments over chips, power and capital still set the terms for everyone else.

## Further reading

- International Energy Agency (2026). *Key Questions on Energy and AI*. The most detailed public analysis of data-centre electricity, with transparent scenarios, data tables and a clear account of supply-chain bottlenecks. [@iea2026key]
- Shehabi, A., et al. (2024). *2024 United States Data Center Energy Usage Report*. A bottom-up estimate of US data-centre electricity and water use that shows how wide the uncertainty is and why. [@shehabi2024united]
- Gholami, A., et al. (2024). *AI and Memory Wall*. A short explanation of why memory bandwidth, not arithmetic, limits much of modern AI computing. [@gholami2024ai]
- Kapoor, S., et al. (2024). *Position: On the Societal Impact of Open Foundation Models*. The standard framework for weighing the benefits and marginal risks of open-weight models. [@kapoor2024position]
- Seger, E., et al. (2023). *Open-Sourcing Highly Capable Foundation Models*. A careful statement of the case for caution, best read alongside Kapoor et al. [@seger2023opensourcing]
- Sastry, G., et al. (2024). *Computing Power and the Governance of Artificial Intelligence*. Explains why hardware is a lever for governing AI, and what could go wrong. [@sastry2024computing]


```{=html}
<section class="part"><p class="part-label">Part III</p><h1 class="part-title">Society and Economy</h1></section>
```

# Chapter 8: Work, Productivity and the Economy

In the first half of 2025 the research organisation METR ran a randomised trial with 16 experienced open-source software developers. Each of 246 real issues from their own projects was randomly assigned to be done with or without AI tools. Before starting, the developers expected AI to cut their time per issue by 24%, and economists and machine-learning experts surveyed by METR expected savings of 38–39%. When the developers' recorded times were compared, the issues on which AI was allowed had taken 19% *longer*. After the study the developers still believed that AI had made them about 20% faster [@becker2025measuring].

Two years earlier a widely cited experiment had found the opposite. College-educated professionals given ChatGPT for short writing tasks finished them 40% faster, and blind graders rated their work 18% better [@noy2023experimental]. Both studies were randomised and both timed work carefully. They studied different people, doing different tasks, with different generations of tools. The gap between their answers is the central fact about the evidence on AI and work: effects depend heavily on setting, and the settings that are easiest to study are not typical of the economy.

The evidence can be arranged along a chain that runs from technical potential to economic outcomes (Figure 8.1): what AI could do (exposure), whether it is used (adoption), what it does to tasks when used (experiments), how firms respond (jobs and wages) and what this adds up to (macroeconomics). Some effects lie outside the chain: the hidden labour behind AI, the erosion or building of skills, and the distribution of gains and losses.

![Figure 8.1: From exposure to economic outcomes. Exposure measures estimate what AI could do; adoption determines whether it is used; task-level productivity effects determine what happens when it is used; and firm decisions translate those effects into employment, wages and output. Evidence becomes scarcer at each step. Diagram by the author.](../figures/svg/fig-08-01.svg){#fig:08-01}

## 8.1 Tasks and exposure: how the measures are built

Economists who study technology and work treat a job as a bundle of **tasks**, the specific activities a worker performs, such as drafting a letter, checking an invoice or calming an angry customer. In the framework of @acemoglu2019automation, automation lets machines take over tasks that people used to do. This has a *displacement effect*, which lowers the demand for labour in those tasks. New technologies also create new tasks in which people have the advantage, a *reinstatement effect* that raises labour demand. Whether a technology helps or hurts workers overall depends on the balance between the two and on how fast new tasks appear.

Both effects are visible in the historical record. Using eight decades of US census data, @autor2024new find that the majority of current employment is in job specialties introduced since 1940. The same study finds that the demand-reducing effect of automation innovations has grown stronger since 1980, while the demand-raising effect of augmentation innovations has not. @acemoglu2022tasks estimate that between 50% and 70% of the change in the US wage structure between 1980 and 2016 is accounted for by relative wage declines of worker groups specialised in routine tasks in industries undergoing rapid automation. Their model also explains how large changes in inequality can coexist with modest productivity gains, a combination that recurs in the AI forecasts discussed in Section 8.5.

### Three ways to score an occupation

An **exposure measure** scores each occupation by how much of its work a technology could, in principle, perform or speed up. All widely used measures start from O\*NET, the US Department of Labor's database that describes about a thousand occupations by their tasks, abilities and work activities. They differ in what they score and who does the scoring.

The *AI Occupational Exposure* (AIOE) index of @felten2021occupational was built before the current generation of large language models. It links ten AI applications tracked by the Electronic Frontier Foundation, such as image recognition, language modelling and translation, to the 52 human abilities that O\*NET uses to describe more than 800 occupations, such as oral comprehension, inductive reasoning or arm–hand steadiness. A crowd-sourced survey rated how related each application is to each ability. An occupation's score is an average of the abilities' AI relatedness, each ability weighted by its prevalence and importance in that occupation. In a 2023 preprint the authors set the weight of every application except language modelling to zero; the re-weighted scores correlate at 0.979 with the original index. Telemarketers come top, and post-secondary teachers of English, foreign languages and history rank near the top [@felten2023language]. The method measures *relatedness* of abilities, not whether a task can actually be done.

@eloundou2023gpts scored tasks directly. They used O\*NET version 27.2, covering 1,016 occupations, 19,265 task statements and 2,087 "detailed work activities". Each item was labelled with a rubric. It counts as *directly exposed* (E1) if access to a large language model (LLM) through an interface such as ChatGPT could cut the time needed by at least half at equivalent quality. Equivalent quality means that "a third party, typically the recipient of the output, would not notice or care about LLM assistance". It counts as *exposed with complementary software* (E2) if the 50% saving would require additional tools built on the model, including image generation. Otherwise it is *not exposed* (E0). The authors and experienced annotators who had reviewed outputs of GPT-3, GPT-3.5 and GPT-4 labelled the detailed work activities and a subset of tasks. An early version of GPT-4 labelled every task, prompted with a slightly modified rubric. The human and GPT-4 labels agreed 80.8% of the time on the narrowest measure and 82.1% on the broadest. The labels are summarised in three measures: *α* counts only E1; *β* adds half of E2, to reflect that software takes time to build; *ζ* counts all of E2.

The preprint's headline numbers use the middle measure, *β*: about 80% of US workers are in occupations with at least 10% of their tasks exposed, and about 19% in occupations where more than half are exposed. The choice of measure moves the results far more than the choice of labeller: counting the software that could be built on the model raises the share of tasks exposed from about 15% to around half (Table 8.1) [@eloundou2023gpts]. Unlike earlier measures of exposure to machine learning, exposure on this rubric rises with wages, and occupations that depend heavily on science and critical-thinking skills are less exposed. A shorter version appeared in *Science* in 2024 [@eloundou2024gpts].

| Measure | Tasks counted as exposed | Share of tasks exposed, human labels | Share of tasks exposed, GPT-4 labels | Share of workers with more than half their tasks exposed |
|---|---|---|---|---|
| *α* | E1 only (LLM alone) | 15% | 14% | 3% (human labels) |
| *β* | E1 plus half of E2 | 31% | 35% | about 19% |
| *ζ* | E1 plus all of E2 | 47% | 56% | up to 49% (human labels) |

: Table 8.1: Exposure of US work to large language models on the three measures of Eloundou et al. E1 tasks could be done at least 50% faster at equal quality with an LLM alone; E2 tasks would need additional software built on the model. Task shares are means over all O\*NET task statements, core tasks weighted double (preprint Table 3). Worker shares are as reported in the preprint's text, which does not give every combination or say which labels the *β* figure uses. The *Science* version reports about 1.8% of jobs with more than half their tasks exposed to LLMs alone and just over 46% once complementary software is included. Source: @eloundou2023gpts; @eloundou2024gpts.

The third approach is the refined index from the International Labour Organization (ILO) and Poland's NASK research institute, published in May 2025 [@gmyrek2025generative]. Its authors first asked three LLMs (GPT-4, GPT-4o and Gemini Flash 1.5) to score every one of the 29,753 tasks in Poland's occupational classification from 0 (cannot be automated) to 1 (could be done without a human operator). They then surveyed 1,640 people working in Poland, collecting 52,558 ratings of 2,861 tasks, and put a sample to national and international experts in several rounds of structured discussion. An AI model trained on the human scores then re-scored the Polish tasks and those of the international ISCO-08 classification. Occupations are placed in four exposure "gradients" using both the mean task score *μ* and its spread *σ*: Gradient 4 requires *μ* ≥ 0.6 and *μ* − *σ* ≥ 0.5, meaning that almost every task is highly exposed. The design matters because an occupation with a moderate average but a few highly exposed tasks is more likely to be reshaped than replaced.

The refinement lowered some earlier scores. Average occupational scores fell slightly from 0.30 in the 2023 index to 0.29. Clerical work, though still the most exposed group, lost ground because tasks such as taking meeting notes or scheduling, once scored as high as 0.9, were judged after two years of practical use to need substantial human effort [@gmyrek2025generative]. On the new index, one in four workers worldwide is in an occupation with some exposure. Only 3.3% of global employment falls in Gradient 4. Overall exposure is 34% of employment in high-income countries and 11% in low-income ones [@gmyrek2025generative]. Announcing the index, the ILO concluded that "transformation, not replacement, is the most likely outcome" [@ilo2025one].

An International Monetary Fund staff note from January 2024 reached higher numbers: almost 40% of global employment exposed, about 60% in advanced economies, 40% in emerging markets and 26% in low-income countries. In advanced economies it judged that about half of exposed jobs might benefit from AI and half might be negatively affected [@cazzaniga2024genai]. The IMF figure rests on the ability-based AIOE index of Felten and colleagues and counts an occupation as highly exposed whenever its score lies above the median. The note itself calls this cut-off relative, so the share depends on where the line is drawn. The ILO counts an occupation as exposed only if a substantial part of its tasks scores high on an absolute 0–1 scale of automation potential (*μ* + *σ* ≥ 0.5 even for its lowest gradient), which places fewer workers above the line [@gmyrek2025generative].

::: {.box .concept}
**Concept: Exposure**

An occupation's exposure to AI is an estimate of the share of its work that AI could technically perform or speed up. It is not a forecast: it contains no information about cost, timing, regulation or whether firms will adopt the technology, and a high score is compatible with a job that disappears, shrinks, grows or simply changes. The three families of measures embed different assumptions. The AIOE scores abilities rather than tasks. The Eloundou rubric sets a threshold (a 50% time saving at unchanged quality) and lets the model judge its own usefulness. The ILO–NASK index asks workers and experts and then generalises their judgements with a model.
:::

### What exposure cannot tell

Every exposure measure relies on judgements about what AI can do, by people or by models, and those judgements date quickly, as the ILO's downward revision of clerical tasks shows. The measures treat tasks as independent, whereas a job whose tasks are 60% exposed may still need a person for the remaining 40%. And none of them can tell whether AI will substitute for a worker or complement one. A tool that drafts legal documents might reduce demand for junior lawyers, or make legal services cheap enough that demand for them grows. Figure 8.1 places exposure at the start of the chain for this reason: it is the step that is easiest to estimate for every occupation and the one furthest from outcomes.

## 8.2 Adoption: who uses AI, and for what

A tool affects productivity only if people use it. Adoption is surprisingly hard to measure: the answer depends on whether workers or firms are asked, on how the question is worded, and on whether occasional or intensive use counts. Table 8.2 sets out the main measures.

### Worker surveys

@bick2024rapid run a nationally representative survey of US adults aged 18 to 64. By August 2025, 54.6% of them used generative AI [@bick2025state]. That figure reflects the authors' reweighting of all rounds after a test of question order showed that their earlier results had underestimated use, a reminder of how fragile the measurement is. Measured from the launch of the first mass-market product, workplace adoption had matched the pace of the personal computer, and overall adoption had outpaced both the PC and the internet. Regular use at work was less widespread: in late 2024, 23% of employed respondents had used generative AI for work in the previous week, and 9% every working day [@bick2024rapid].

Intensity is far lower than adoption. Generative AI was used in 5.7% of all work hours in August 2025, up from 4.1% in November 2024. Workers reported time savings equal to 1.6% of all work hours, counting non-users (1.4% in the February 2025 version of the working paper). The authors infer that generative AI "may have increased labor productivity by up to 1.3%" since ChatGPT's release, with the caveat that saved time may go to less productive activities [@bick2025state].

In Denmark, Humlum and Vestergaard ran large surveys with Statistics Denmark in late 2023 and 2024. They covered 11 occupations thought to be highly exposed to AI chatbots: accountants, customer-support specialists, financial advisers, HR professionals, IT-support specialists, journalists, legal professionals, marketing professionals, office clerks, software developers and teachers. The latest round covered about 25,000 workers at 7,000 workplaces and was linked to official employment records. The revised version of their working paper (March 2026) shows how much employers matter. In workplaces that neither encouraged use nor provided tools or training, about 40% of workers had used chatbots at work and about 7% used them daily. In workplaces that encouraged use, supplied enterprise chatbots and trained staff, 93% had used them, 28% used them daily and 19% reported saving more than an hour a day. About 8% of users without employer initiatives, and about 17% with them, had taken on entirely new tasks created by chatbots, such as reviewing AI output or writing usage policies [@humlum2025still]. (In the first version, of May 2025, users reported average time savings of only 2.8% of work hours [@humlum2025large].)

### Firm surveys

The US Census Bureau's Business Trends and Outlook Survey (BTOS) regularly asks firms whether they use AI. Until November 2025 the question asked about AI used in *producing goods or services*; by late 2025 about 10% of firms said yes, double the rate of mid-2024. From 17 November 2025 the question covered AI in *any business function*, and in early 2026 about 20% of firms reported use. Use was highest in information and professional services, at nearly four in ten firms; in agriculture, transport, accommodation and food services and construction it was below 10% [@garcialuna2026ai].

A Census Bureau working paper on a special AI supplement to the BTOS, covering November 2025 to January 2026, shows how large firms drive the totals and how shallow most use is [@bonney2026microstructure]. In that period 18% of firms used AI in a business function, or 32% when firms are weighted by employment, and among very large firms in information, professional services and finance the rate reached 50–60%. Of the adopters, 57% used AI in three or fewer functions, most often sales and marketing (52%). Two-thirds used AI only to augment tasks, and just 2% reported that AI had reduced their employment.

### Usage data from AI companies

AI providers can observe use directly. Anthropic, the developer of the Claude models, publishes an "Economic Index" based on privacy-preserving analysis of conversations. Its first report, a preprint by company researchers analysing more than four million conversations, found that software development and writing together accounted for nearly half of usage, and that slightly more usage suggested augmentation (57%) than automation (43%) [@handa2025which]. The company's January 2026 report drew on one million consumer conversations and one million business transcripts from November 2025. Consumer conversations were split between augmentation (52%) and automation (45%), whereas about three-quarters of business interactions through the programming interface, in which firms connect the model to their own software, were automation [@anthropic2026economic].

These data cover real use at scale, for one company's products and customers only. The "automation" and "augmentation" labels are assigned by a language model from conversation patterns, not measured from effects on jobs. A June 2026 report linked usage to a survey of about 9,700 users, but computer and mathematical occupations made up about 30% of respondents against 4% of US employment [@massenkoff2026anthropic].

| Source (data period) | Population | Measure | Reported value |
|---|---|---|---|
| Bick, Blandin & Deming (Aug 2025) | US adults aged 18–64 | Use generative AI | 54.6% |
| Bick, Blandin & Deming (late 2024) | US employed adults | Used it for work in previous week | 23% |
| Census BTOS (late 2025) | US firms | Use AI to produce goods or services | about 10% |
| Census BTOS (early 2026) | US firms | Use AI in any business function | about 20% |
| Census BTOS AI supplement (Nov 2025–Jan 2026) | US firms | Use AI in a business function | 18% (32% weighted) |
| Humlum & Vestergaard (late 2023 and 2024) | Danish chatbot users in 11 exposed occupations | Average time saved | 2.8% of work hours |
| Anthropic Economic Index (Nov 2025) | Claude.ai conversations | Classified as augmentation / automation | 52% / 45% |

: Table 8.2: Selected measures of AI adoption and use, 2023–2026, mainly from the United States and Denmark. Differences in wording and population explain much of the variation between sources. The BTOS question changed in November 2025, so rows 3 and 4 are not directly comparable. The August 2025 Bick, Blandin and Deming figure reflects their 2025 reweighting of all survey rounds, which raised the August 2024 estimate from 39.4% to 44.6% (their February 2025 working paper had reported nearly 40% for late 2024). The Danish time saving is from the May 2025 version of the working paper. Anthropic figures are company data and describe conversation patterns, not effects on jobs. Source: @bick2024rapid; @bick2025state; @humlum2025large; @garcialuna2026ai; @bonney2026microstructure; @anthropic2026economic.

## 8.3 What experiments show about task productivity

The strongest evidence about cause and effect comes from **randomised controlled trials (RCTs)**, in which chance decides which people or tasks get access to AI, so that the groups differ on average only in that access. Many other studies are **observational**: they compare people or firms who chose to adopt with those who did not, so differences may reflect who chose rather than what they chose. Some observational studies are **quasi-experiments**, exploiting a natural source of variation, such as a staggered roll-out, to approximate a trial. Even an RCT measures the effect only for its sample, task and tool. Table 8.3 compares the main studies, and Figure 8.2 plots their estimates.

| Study (status) | Design | Sample and setting | Tool and period | Main estimate | Main caveat |
|---|---|---|---|---|---|
| Noy & Zhang (2023, *Science*) | Preregistered online RCT | 453 college-educated professionals; 20–30-minute writing tasks | ChatGPT | Time −40%; graded quality +18% | Short, self-contained tasks |
| Peng et al. (2023, preprint) | RCT | 95 freelance programmers recruited on Upwork (45 treated) | GitHub Copilot, 2022 | Time −55.8% (95% CI −89% to −21%) | One standardised task; only completers timed |
| Brynjolfsson, Li & Raymond (2025, *QJE*) | Staggered roll-out, difference-in-differences | 5,172 customer-support agents at one firm; 89% outside the US | GPT-3-based assistant, 2020–21 | Issues resolved per hour +15%; lowest-skill fifth +36% | Not randomised; one firm |
| Dell'Acqua et al. (2026, *Organization Science*) | Preregistered RCT, three arms | 758 consultants at Boston Consulting Group | GPT-4, 2023 | Inside frontier: +12.2% tasks, 25.1% faster; outside: 19% less likely to be correct | Tasks designed for the study |
| Cui et al. (2026, *Management Science*) | Three field RCTs, pooled | 4,867 developers at Microsoft, Accenture and a Fortune 100 firm | GitHub Copilot, 2–8 months | Completed tasks +26.08% (SE 10.3%) | Each experiment noisy; uneven take-up |
| Becker et al. (2025, preprint) | RCT at issue level | 16 experienced open-source developers, 246 issues | Cursor with Claude 3.5/3.7 Sonnet, Feb–June 2025 | Time +19% (95% CI +2% to +39%) | Small sample; mature projects |
| METR follow-up (2026, report) | RCT at task level | 57 developers, 800+ tasks | Tools of late 2025 | Time −18% (returning, n = 10); −4% (new, n = 47); neither significant | Developers withheld tasks |
| Otis et al. (2026, *Management Science*) | Field RCT | Small-business owners in Kenya | GPT-4 business assistant | No significant average effect on revenue or profit; top performers +15%+, low performers ≈−10% | Subgroup estimates |
| Shen & Tamkin (2026, preprint) | RCT | 52 Python programmers learning a new library | AI coding assistant | No significant speed gain; quiz score −17% | Crowd workers; one session |

: Table 8.3: Selected randomised and quasi-experimental studies of AI assistance at work. "Time" is the change in time to complete a task (negative is faster). CI = confidence interval; SE = standard error. Estimates use different outcomes, samples and tools and are not directly comparable. Source: @noy2023experimental; @peng2023impact; @brynjolfsson2025generative; @dellacqua2026navigating; @cui2026effects; @becker2025measuring; @metr2026changing; @otis2026uneven; @shen2026how.

### Writing and consulting

@noy2023experimental recruited marketers, grant writers, consultants, data analysts, HR professionals and managers. Each wrote two occupation-specific pieces, such as a press release or a delicate email, with large bonuses for quality. Between the tasks, a random half were walked through ChatGPT and allowed to use it. Experienced professionals in the same occupations graded the work blind. Time fell by 40% and quality rose by 18%. The gains were largest for participants who had done worst on the first task, so inequality between workers narrowed. Two weeks later, treated participants were twice as likely as controls to be using ChatGPT in their real jobs.

@dellacqua2026navigating ran a preregistered experiment with 758 consultants at Boston Consulting Group, first circulated as a working paper in 2023. After a baseline task, participants were randomly assigned to work without AI, with GPT-4, or with GPT-4 plus a short overview of prompting. On 18 realistic consulting tasks chosen to lie within the model's capabilities, those with AI completed 12.2% more tasks, worked 25.1% faster and produced work of significantly higher quality. On a complex managerial task selected to lie outside those capabilities, consultants using AI were 19% less likely than the control group to reach the correct answer. The authors call this pattern the **jagged technological frontier**: AI's competence does not decline smoothly as tasks become harder for humans, and a worker who cannot see where the frontier runs may rely on the tool exactly where it is weakest.

### Customer support

The most detailed field study looked at a real workplace over many months. @brynjolfsson2025generative studied an AI assistant introduced at a Fortune 500 firm selling business software, whose agents answered technical questions by online chat. Access was rolled out to different agents at different times, mainly between late 2020 and early 2021. The authors used **difference-in-differences**: they compared the change in performance of agents who gained access with the change, over the same period, among agents who had not yet gained it. The design rests on the assumption that the timing of access was unrelated to other changes in performance, which the authors probe with several alternative estimators.

::: {.box .case}
**Case study: An AI assistant in a customer-support centre**

The firm's agents, 89% of them outside the United States and mainly in the Philippines, served small and medium-sized US businesses. The assistant, built on GPT-3 and fine-tuned by a third-party company, suggested replies and links to documentation in real time; agents could ignore the suggestions [@brynjolfsson2025generative]. Across 5,172 agents, access raised issues resolved per hour by 15% on average. The least skilled fifth of agents gained about 36%. For the most experienced and highest-skilled agents, gains in speed were small and the quality of their conversations declined slightly. Agents with two months' tenure who had the assistant performed about as well as agents with more than six months' tenure who did not.

Gains were largest for moderately rare problems, where agents had little experience but the system had enough training data. English fluency improved, particularly among international agents, and customers were more polite and less likely to ask for a manager.
:::

### Software development

Software is the most-studied occupation, because output can be logged automatically. In an early experiment, @peng2023impact recruited 95 freelance programmers through Upwork in 2022 and randomly gave 45 of them GitHub Copilot, a code-completion tool. The task was to write a simple web server in JavaScript. Among those who finished, the treated group was 55.8% faster, with a **confidence interval** (the range of effects consistent with the data at the stated level of confidence) from 21% to 89%.

@cui2026effects analysed three field experiments in which Microsoft, Accenture and an anonymous Fortune 100 electronics manufacturer gave a random subset of developers access to Copilot as part of normal business. After two to eight months, everyone got access. Take-up was far from complete: at Microsoft only 42.5% of the treated group had signed up even after two reminder emails. The authors therefore use random assignment as an *instrument* for actual use, which estimates the effect on those who adopted. Pooling 4,867 developers, they estimate that using the tool raised completed tasks (pull requests, the unit in which code changes are submitted for review) by 26.08%, with a standard error of 10.3%. Code builds and commits also rose, the latter too imprecisely to be statistically significant. At Microsoft, recent hires and junior staff gained significantly, while longer-tenured and senior developers did not.

The METR trial described at the start of the chapter is the main counterweight [@becker2025measuring]. Its 16 developers typically had more than a decade of experience and had worked on their repositories, which averaged more than 1.1 million lines of code, for five years on average. They were paid $150 an hour. Of 20 possible explanations for the slowdown, the authors judged five likely contributors: over-optimism about AI, high familiarity with the code, large and complex repositories, low reliability of the AI, and tacit context that the tools could not use. Developers accepted fewer than 44% of the AI's generations and spent about 9% of their time reviewing and cleaning its output. The authors stress that the result does not show that AI slows down most developers, or that it would do so with later tools.

METR's follow-up, beginning in August 2025, enrolled 57 developers and more than 800 tasks. For the ten developers returning from the first study the estimated effect was an 18% speed-up; for the 47 new recruits it was 4%. Neither estimate was statistically distinguishable from zero. Between 30% and 50% of developers said they had not submitted some tasks because they did not want to do them without AI, and some developers declined to take part at all for the same reason. Once a tool becomes indispensable to some workers, randomising it away becomes hard. METR concluded that developers were probably sped up more in early 2026 than in early 2025 but that its data were "only very weak evidence" of how much [@metr2026changing].

### When AI widens gaps

Most studies find gains concentrated among weaker or less experienced workers. A field experiment with small-business owners in Kenya found the reverse [@otis2026uneven]. Entrepreneurs were randomly given access to a GPT-4-based business assistant. There was no statistically significant average effect on revenues or profits, but the effect for those who had been performing poorly at baseline was more than 0.2 standard deviations lower than for high performers. In subsample analyses, high performers may have gained more than 15% while low performers did nearly 10% worse. The questions asked and the advice received were similar across the two groups; the difference lay in which advice entrepreneurs chose to act on. Unlike a support agent choosing among suggested replies to a familiar query, an entrepreneur has to judge open-ended advice without quick feedback.

### Reading the evidence together

The estimates in Table 8.3 range from a 56% reduction in task time to a 19% increase. Gains are largest on short, well-defined tasks with clear success criteria, and smallest, or negative, for experts on complex work in contexts they know well. Within a task they usually shrink inequality, because AI transfers the practices of strong performers to weak ones; the exception is work in which users must judge the quality of advice themselves. And the tools change faster than studies are published: Copilot in 2022, GPT-4 in 2023 and the coding agents of 2026 (Chapter 5) are different technologies.

The evidence base also carries a warning about its own reliability. In May 2025 MIT announced that it had "no confidence in the provenance, reliability or validity of the data" in a November 2024 preprint by a former doctoral student on AI in materials research. It asked arXiv to mark the paper as withdrawn [@mit2025assuring].

![Figure 8.2: Estimated effects of AI assistance in selected studies, with data collected from late 2020 onwards; the METR follow-up began in August 2025 and was reported in February 2026. Panel A shows changes in the time needed to complete tasks (negative values mean faster work); Panel B shows changes in output (positive values mean more output). Dell'Acqua et al. estimates are for tasks inside the frontier. Bars show 95% confidence intervals where available; the Cui et al. interval is approximate, computed from the reported standard error. Studies differ in design, sample, task and tool, so the estimates are not directly comparable. Source: @noy2023experimental; @peng2023impact; @becker2025measuring; @metr2026changing; @brynjolfsson2025generative; @dellacqua2026navigating; @cui2026effects.](../figures/svg/fig-08-02.svg){#fig:08-02}

## 8.4 Jobs and wages: the evidence so far

A productivity gain in a task leaves firms several options: employ fewer people, keep the same staff and produce more, or move workers into new tasks. Nearly four years after the launch of ChatGPT, the evidence on which they are choosing is partial and in places conflicting.

### Little sign of economy-wide disruption

The Danish study provides the most precise test. Linking survey answers to administrative records of monthly earnings, hours and occupations up to December 2024, Humlum and Vestergaard compare adopters and non-adopters before and after chatbots became available. The revised paper (March 2026) finds null effects. The pooled estimates rule out effects on earnings or recorded hours larger than 2% two years after ChatGPT's launch; no occupation shows a significant effect, and the nulls hold even among daily users who report substantial productivity gains [@humlum2025still]. (The May 2025 version had reported "precise zeros" ruling out effects larger than 1% [@humlum2025large].) What does move is the structure of work. Adopters were more likely to have switched occupations, especially into IT-support and clerical roles, and switchers' earnings grew 12 percentage points faster than those of other employed workers, though they were too few to move the average.

In the United States, the Yale Budget Lab measured how fast the mix of occupations changed in the 33 months after ChatGPT's release and compared it with the spread of computers and the internet [@gimbel2025evaluating]. The mix was changing somewhat faster than in earlier periods, but the difference was small and had begun before generative AI. Measures of exposure, automation and augmentation showed "no sign of being related to changes in employment or unemployment". The Economic Innovation Group, a Washington think tank, reached a similar conclusion with Current Population Survey data and five exposure measures [@eckhardt2025ai]. Between 2022 and early 2025, unemployment in the most exposed fifth of workers rose by 0.30 percentage points, against 0.94 points for the least exposed fifth. Unemployment was rising for young workers and recent graduates in both exposed and less exposed occupations.

### Where substitution shows up

Clearer effects appear in online freelancing, where tasks are bought one at a time and buyers can switch to AI at once. Studying a large platform, @hui2024short find that after the release of ChatGPT and of image generators, freelancers in the most affected occupations saw falls in both employment and earnings, and that past performance did not protect them. There is suggestive evidence that top freelancers were hit harder. On another leading platform, @demirci2025who estimate a 21% fall in job posts for automation-prone writing and coding work relative to manual-intensive work within eight months of ChatGPT's release, and a 17% fall in posts for image creation after image generators appeared. The remaining automation-prone jobs were more complex and better paid. Freelance markets are small and unusually exposed, so these results show what substitution looks like where it is easy, not how fast it will happen in employment relationships.

### Early-career workers

Payroll data point to a group that may be affected first. In a working paper using monthly records from ADP, a payroll processor serving firms with more than 26 million US workers, @brynjolfsson2026canaries document "six facts" from a balanced panel of firms employing 3.5 to 5 million people a month. The August 2026 version has data to June 2026. By then employment of 22- to 25-year-olds in the two most AI-exposed fifths of occupations had fallen about 11% since November 2022, while young workers in the three least exposed fifths grew about 10%. Their employment stood 19% below where it would have been had it kept pace with less-exposed peers (15% with data to July 2025; earlier versions headlined a regression-adjusted 13% relative decline, but the authors now prefer the simpler descriptive gap). Experienced workers showed no comparable gap. The adjustment came through reduced hiring rather than layoffs, appeared in employment rather than base pay, and was concentrated in occupations where AI is mostly used to automate; where it mostly complements workers, employment was flat or rising.

A separate working paper using résumé data on 65 million workers at more than 280,000 US firms found a related pattern [@hosseinimaasoum2025generative]. After firms posted job advertisements for staff to integrate generative AI, a signal of active adoption, junior employment at those firms fell sharply relative to non-adopting firms, while senior employment changed little, again mainly through slower hiring. Job advertisements suggest that entry-level roles are also being redesigned. PwC's 2026 *Global AI Jobs Barometer* analysed more than one billion advertisements. In the United States, entry-level roles most exposed to AI were seven times more likely than others to require skills traditionally expected of senior staff, such as leadership or face-to-face interaction [@pwc2026global]. These are correlations, and the consultancy's analysis does not identify their cause.

::: {.box .debate}
**Debate: Is AI already reducing entry-level hiring?**

*The case that it is.* The ADP data show a 19% employment gap for 22- to 25-year-olds in highly exposed occupations by June 2026, widening steadily since the authors first documented it in August 2025 and concentrated where AI substitutes for tasks. It persists when technology firms and computer occupations are excluded and when the authors control for exposure to interest-rate rises and for remote work [@brynjolfsson2026canaries]. Firm-level résumé data show junior employment falling specifically at firms that adopt generative AI [@hosseinimaasoum2025generative], and freelance platforms show direct substitution in writing and coding [@demirci2025who].

*The case that it is not yet shown.* The ADP authors present their findings as "early, descriptive indicators" rather than causal estimates. The gap shrinks when education is controlled for, some divergence predates generative AI, and it is larger in the ADP sample than in national surveys. In Denmark, Humlum and Vestergaard replicate the decline in early-career employment in exposed occupations but find that it is *not* driven by firms that adopted chatbots. Workplaces that encourage chatbot use show no differential change in employment, job creation or destruction, or the composition of hires and separations, including among early-career workers [@humlum2025still]. National US data show unemployment rising for young workers in exposed and unexposed occupations alike [@eckhardt2025ai].

The two bodies of evidence may describe different stages without contradicting each other, since the ADP gap is measured to mid-2026 and the Danish records end in December 2024. Settling the question needs the Danish test, which links each firm's actual adoption to its hiring, repeated with US data and with observations from after 2024, when the tools became more capable.
:::

## 8.5 The macroeconomic picture: why forecasts differ

If AI raises productivity in many tasks, the economy as a whole should grow faster. Published estimates of how much faster differ by more than an order of magnitude, and the reason can be traced to a handful of assumptions.

### Hulten's theorem and the task-based sum

@acemoglu2025simple anchors his estimate in a result from growth accounting, **Hulten's theorem** [@hulten1978growth]. In a competitive economy, the first-order effect of a small improvement in the technology for a particular task on aggregate productivity equals the task's share of GDP multiplied by the percentage cost saving in that task. Reallocations of labour and capital across tasks, and knock-on changes in prices, matter only at the second order. Summing over tasks, the gain in total factor productivity (TFP), the part of output growth not explained by more capital or labour, is approximately

*TFP gain ≈ (GDP share of tasks affected) × (average cost saving in those tasks).*

The cost saving in a task is the saving in labour cost multiplied by labour's share of that task's costs, because AI saves labour time but not the machines, materials or premises the task also uses.

::: {.box .deeper}
**Going deeper: Acemoglu's arithmetic**

The published version in *Economic Policy* puts the ten-year TFP gain at no more than 0.66%, and below 0.53% once hard tasks are allowed for [@acemoglu2025simple]. The April 2024 working paper, whose results are slightly higher, shows the arithmetic term by term [@acemoglu2024simple]. Weighting the tasks that @eloundou2023gpts classify as exposed by their occupations' share of the US wage bill gives 19.9% of tasks exposed. He then takes an estimate by Svanberg and colleagues that 23% of tasks exposed to computer vision could be automated profitably within ten years. Applying the same share to all AI, 0.199 × 0.23 ≈ 4.6% of tasks are affected. For the labour-cost saving he averages the 40% time saving in @noy2023experimental and the 14% in @brynjolfsson2025generative (as measured in that study's 2023 version), giving 27%; he leaves out the 55.8% in @peng2023impact as too narrow a task. With an AI-exposure-adjusted labour share of 0.57, the average total cost saving is 0.27 × 0.57 ≈ 15.4%. The TFP gain over ten years is then 0.046 × 0.154 ≈ 0.71%, or about 0.07 percentage points a year.

He then argues that early evidence comes from *easy* tasks with clear success criteria, and assumes a labour-cost saving of only 7% for *hard* tasks, half the customer-support figure. That lowers the ten-year gain to about 0.55%. Allowing for the extra investment AI would induce, GDP rises by 0.9–1.1% over ten years, or 1.6–1.8% if there is an investment boom like those of earlier automation technologies.

The formula has known limits. It is a first-order approximation for small changes; it counts no new products or new tasks, which could make the true effect larger; and it ignores adjustment costs, which could make it smaller.
:::

### Same formula, different numbers

Philippe Aghion and Simon Bunel applied the same formula in a June 2024 note but with their own reading of the evidence [@aghion2024ai]. They take the share of exposed tasks from an IMF working-paper estimate for the United States, assume half of these become profitable to automate because computing costs fall by 22% a year, and average all three early experiments for the labour-cost saving (Table 8.4). Their baseline is 0.68 percentage points of additional TFP growth *a year*, ten times Acemoglu's figure, and the range across plausible inputs runs from 0.07 to 1.24 points. A second method, which assumes that AI will follow the path of electricity or of earlier digital technologies, gives 0.8 to 1.3 points a year.

| Input | Acemoglu (2024 working paper) | Aghion & Bunel (2024 baseline) |
|---|---|---|
| Share of tasks exposed to AI | 19.9% | 60% |
| Share of exposed tasks profitable to automate within ten years | 23% | 50% |
| Labour-cost saving in affected tasks | 27% | 40% |
| Labour share of costs in affected tasks | 0.57 | 0.57 |
| Implied TFP gain over ten years | ≈0.71% | ≈6.8% |
| Implied addition to annual TFP growth | ≈0.07 percentage points | ≈0.68 percentage points |

: Table 8.4: Two applications of the same task-based formula (TFP gain ≈ exposed share × profitable share × labour-cost saving × labour share) to the next ten years. Every input differs except the labour share, and the product of the differences is a tenfold gap. Acemoglu's figures and Aghion and Bunel's annual figure are as reported; their ten-year figure is the product of their inputs. Acemoglu's published version gives a slightly lower 0.66%. Source: @acemoglu2024simple; @aghion2024ai.

The Penn Wharton Budget Model at the University of Pennsylvania uses the same framework with an explicit diffusion path [@arnon2025projected]. It treats 40% of current US labour income as potentially exposed and assumes 23% of exposed tasks are automated. Labour-cost savings rise from about 25% to 40% as tools improve and spread at the pace of PCs, the internet, smartphones and cloud computing. Its September 2025 projection has productivity and GDP 1.5% higher by 2035 and 3.7% higher by 2075 than without AI, with the largest contribution to TFP growth, about 0.2 percentage points, in 2032.

Estimates from financial firms and AI companies sit at the upper end. In research published by the investment bank Goldman Sachs in April 2023, its economists estimated that generative AI could raise global GDP by 7%, almost $7 trillion, and lift productivity growth by 1.5 percentage points over a ten-year period [@goldmansachs2023generative]. Anthropic's January 2026 report, using its own usage data, estimated that AI could add about 1.8 percentage points to annual US labour-productivity growth over the next decade, or about 1.0 point once task success rates are allowed for [@anthropic2026economic]. Both are estimates of labour productivity, which also rises when firms invest in more capital, and neither has been peer-reviewed.

### Why productivity statistics may lag

Even large eventual gains may not appear in official statistics for some time, and so far US data show no break in trend. Nonfarm business labour productivity grew 2.2% in the year to the second quarter of 2026. Since the end of 2019 it has grown at an annual rate of 2.1%, faster than the 1.5% of the 2007–2019 business cycle but equal to the average since 1947 [@bls2026productivity]. These aggregates cover every source of growth and cannot isolate AI's contribution. @brynjolfsson2021productivity describe a **productivity J-curve**. Firms adopting a general-purpose technology must make large complementary investments, in reorganising work, training staff and building data systems. These intangible investments are poorly measured, so measured productivity growth is at first *understated* and later, when the benefits are harvested, *overstated*. For computer hardware and software, they estimate that US TFP was 15.9% higher by the end of 2017 than official measures suggested. The Danish evidence that employers absorb chatbots by reorganising tasks, with 85% of users reallocating saved time to other work, is consistent with the early, investment-heavy phase of such a curve [@humlum2025still]. So is the gap between time savings of 1–3% of work hours in surveys and gains of 15% or more in many experiments.

## 8.6 Hidden labour and collective bargaining

### The work behind the machine

AI systems depend on workers whom users rarely see. Models are trained and evaluated on data that people label, and the feedback training described in Chapter 3 relies on raters who compare and score model outputs. Mary Gray and Siddharth Suri call such task-by-task, platform-mediated labour **ghost work**. Their five-year study of on-demand workers in the United States and India found that many apparently automated services rely on people who are hired, managed and paid through software, often with few of the protections of standard employment [@gray2019ghost].

The best-documented case involves ChatGPT itself. In January 2023 an investigation by *TIME* reported that OpenAI had contracted Sama, an outsourcing firm, to have workers in Nairobi label text describing violence, hate speech and sexual abuse [@perrigo2023exclusive]. The labels trained a detector for such content that was later built into ChatGPT. According to *TIME*, the roughly three dozen workers took home between about $1.32 and $2 an hour, while OpenAI's contracts paid Sama $12.50 an hour, a rate Sama said covered all its costs. All four workers interviewed said the work had left them mentally scarred and described counselling as rare and unhelpful, which Sama partly disputed. Sama ended the work in February 2022, eight months early.

Systematic evidence points the same way. The Fairwork project at the Oxford Internet Institute scores online labour platforms out of ten against five principles: fair pay, conditions, contracts, management and representation. Its 2023 ratings covered 15 platforms and drew partly on a survey of 752 workers in 94 countries. No platform scored above 5, and four scored zero. Microwork platforms supplying data annotation and model evaluation to AI companies "were among the lowest scores" [@fairwork2023work, p. 2]. Most demand for such work comes from clients in the Global North and most of the workforce is in the Global South. None of this labour appears in exposure indices or productivity experiments, which count the people who use AI, not those whose work goes into building it.

### Offshore work and who gains

The best-known field study is itself a study of offshore labour: most agents in the customer-support case of Section 8.3 worked in the Philippines [@brynjolfsson2025generative]. Its results describe outsourced service work in a lower-wage economy and may not carry over to workers with different pay, training or language backgrounds. The finding that new agents with the assistant matched experienced agents without it also has two readings. For individual agents it means faster learning. For an outsourcing industry that competes partly on the experience of its workforce, it may mean that this advantage counts for less. Whether the gain reaches agents as higher pay or customers and the firm as lower costs depends on wage-setting, which the study was not designed to measure.

### Collective bargaining

The clearest union response came from Hollywood. In 2023 the Writers Guild of America (WGA) struck for 148 days [@wga2023what]. The resulting agreement with the studios, covering 25 September 2023 to 1 May 2026, set rules for AI [@wga2023summary]. AI cannot write or rewrite literary material, and AI-generated material does not count as source material, so it cannot be used to undermine a writer's credit or to pay a lower rewrite fee [@wgaw2026artificial]. A writer may use AI with the company's consent, but the company cannot require it, and companies must disclose when material handed to a writer was generated by AI. The Guild reserved the right to argue that training AI on writers' work is prohibited. The agreement leaves the technology in use and allocates control over it, drawing by negotiation the line between augmentation and automation.

The successor agreement, covering 2 May 2026 to 1 May 2030, "preserves all of the protections negotiated in 2023" and adds a duty to give the Guild written notice when companies license writers' work to train a commercial generative AI system. The Guild may then ask to discuss the licence, including payment to writers [@wga2026summary]. Training data, left open in 2023, has thus become a subject of bargaining.

Other collective responses are smaller or less tested. In May 2023 more than 150 content moderators and data workers for Facebook, TikTok and ChatGPT met in Nairobi and voted to form a union [@perrigo2023african]. In December 2023 the US union federation AFL-CIO and Microsoft announced a partnership that, according to Microsoft, includes worker feedback to AI developers and a neutrality framework for future union organising [@microsoft2023aflcio].

## 8.7 Deskilling and the skills pipeline

A separate concern is that relying on AI may erode the skills of the people who use it. In a classic paper on industrial automation, @bainbridge1983ironies set out the **ironies of automation**. Automation leaves human operators the tasks designers could not automate, including monitoring and taking over when the system fails. Yet "physical skills deteriorate when they are not used" [@bainbridge1983ironies, sec. 1.1.1], so an experienced operator who has spent years watching an automated process may have become an inexperienced one by the time intervention is needed.

Evidence from medicine suggests a similar risk with AI. @budzyn2025endoscopist studied colonoscopies at four endoscopy centres in Poland that had introduced an AI system to help detect precancerous growths (adenomas). In a retrospective, observational analysis of 1,443 colonoscopies performed *without* AI assistance between September 2021 and March 2022, the adenoma detection rate fell from 28.4% in the months before AI was introduced to 22.4% afterwards. The authors concluded that continuous exposure to AI "might" reduce performance in unassisted procedures. The before-and-after design cannot exclude other changes over the same period. A later prospective trial with 13 endoscopists, using a related measure, found no deskilling in colonoscopies done after AI use ended [@pedersen2026learning].

For knowledge work, the cleanest test so far is a small randomised experiment reported in a preprint by Anthropic researchers [@shen2026how]. Fifty-two programmers with at least a year of Python experience learned an asynchronous programming library they had not used before, half with an AI assistant. The AI group was not significantly faster, and on a quiz afterwards, taken without AI, it scored 17% lower, about two grade points, with weaker conceptual understanding, code reading and debugging. Participants who delegated the coding entirely gained some speed at the cost of learning the library; three of the six patterns of use the authors identified, all involving active engagement such as asking conceptual questions, preserved learning. Chapter 10 discusses comparable findings on learning in education.

Deskilling matters for the economy as well as for safety, because expertise is built by doing routine work. The payroll evidence in Section 8.4 suggests that fewer junior workers are being hired into exposed occupations. If they no longer perform the tasks through which they once learned, the supply of future experts able to supervise AI may narrow. The experiments point in two directions. AI raises novices' output most (Section 8.3), but in the one study that tested learning directly, the same help reduced what they learned. Neither the payroll data nor the PwC advertisement analysis can show that this pipeline is being damaged [@pwc2026global]; they show only that the conditions for it exist.

## 8.8 Inequality, distribution and policy

### Who gains?

Within tasks, AI usually narrows gaps, as in customer support, professional writing and software development (Section 8.3); the Kenyan experiment, where users had to judge open-ended advice, is the exception [@otis2026uneven]. Compression within a task does not imply compression across the economy, because the value of the task itself may fall. @acemoglu2025simple shows that AI can increase inequality even when it raises the productivity of low-skill workers in some tasks. Empirically he finds AI's exposure more evenly spread across demographic groups than earlier automation, so it is unlikely to raise inequality as much, but no evidence that it will reduce labour-income inequality. He predicts a widening gap between income from capital and from labour. The IMF note similarly warns that higher returns to capital could increase wealth inequality [@cazzaniga2024genai]. David Autor has argued the opposite possibility: because AI can support expert judgement, it could let more workers take on higher-stakes decisions now reserved for elite experts in medicine, law or software and, "if used well", help restore middle-skill work [@autor2024applying]. He presents this as a possibility that depends on design and deployment, not as a forecast.

Exposure is unevenly distributed across groups and countries. In high-income countries, according to the ILO–NASK index, jobs in the highest exposure gradient account for 9.6% of female employment but only 3.5% of male employment [@ilo2025one; @gmyrek2025generative]. The IMF finds that women and college-educated workers are more exposed but also better placed to benefit, and that older workers may find it harder to adapt. Advanced economies are more exposed but also better prepared, which could widen income gaps between countries [@cazzaniga2024genai].

### The policy response

Governments have responded mainly through existing institutions, with a few targeted rules. The most concrete is the European Union's AI Act, whose wider structure Chapter 13 describes. It classifies as "high-risk" AI systems used to recruit or select workers, to make decisions on promotion or termination, to allocate tasks on the basis of individual behaviour or traits, and to monitor and evaluate workers' performance [@europeanparliament2024regulation, Annex III, point 4]. Employers deploying such systems must inform workers' representatives and the affected workers before using them [@europeanparliament2024regulation, art. 26(7)]. The Digital Omnibus on AI, the EU's 2026 amending regulation to the AI Act (Section 13.2), deferred the application of these high-risk obligations from 2 August 2026 to 2 December 2027 [@europeanparliament2026regulation].

Beyond specific rules, the main policy positions are best told apart by the question each one asks. One asks *which technologies are built*. In a 2023 policy memo, Acemoglu, Autor and Johnson argue that the private sector is pursuing a path that emphasises automation and workplace surveillance. They propose equalising tax rates on employing workers and on owning equipment and algorithms, limiting workplace surveillance, and funding research on technologies that complement workers [@acemoglu2023can]. Others put more weight on measuring effects before acting; the Yale Budget Lab, for example, stresses that "better data is needed" [@gimbel2025evaluating].

The US government's AI Action Plan of July 2025 is concerned instead with *how fast AI spreads*, and commits to removing "red tape and onerous regulation" [@whitehouse2025winning]. Its labour response is a "worker-first" agenda built on existing institutions: AI skills in training and apprenticeship programmes, retraining for displaced workers, and an AI Workforce Research Hub in the Department of Labor. On this view the state's task is to help workers move, not to shape the technology.

Collective bargaining addresses *who controls AI's use at work*. Agreements by sector, like the writers' contracts of 2023 and 2026, can fit rules to particular tasks, and the AI Act's duty to inform workers' representatives gives it a legal foothold in the EU. It reaches only organised workers, which excludes most of the platform workers described in Section 8.6.

Proposals for redistribution start from *who bears the losses*. @korinek2019artificial show in simple economic models that, under plausible conditions, governments can tax the gains from AI without distorting incentives and use the revenue to compensate those who would otherwise lose. In a 2021 essay, Sam Altman, the chief executive of OpenAI, proposed an "American Equity Fund" paying out to every adult citizen, financed by an annual tax of 2.5% on the value of large companies and of land [@altman2021moores]. The most direct evidence on unconditional payments comes from a trial not designed with AI in mind. In a large US experiment, 1,000 low-income people received $1,000 a month for three years and 2,000 received $50 a month [@vivalt2026employment]. The larger payments reduced labour-market participation by 4.2 percentage points and working hours by one to two hours a week. Leisure rose most, and the quality of employment did not improve.

The best evidence sits early in the chain of Figure 8.1: exposure can be scored for every occupation, and task-level gains have been measured in trials. The later links, from use to firms' choices to aggregate output, are still thinly observed. Measured use takes only a few per cent of work hours, the large gains of the experiments shrink or reverse for experts on complex work they know well and for users who must judge open-ended advice, and US productivity has yet to depart from its long-run trend. Where change is visible it lies in the content of jobs and possibly in the hiring of young workers into exposed occupations, while in the Danish records average earnings and hours have so far held steady. Whether that reorganisation ends in faster growth, a narrower path into expert work or both will depend on how tools are designed, how their use is bargained over and how gains are shared. Those are the questions on which the policy positions above divide.

## Further reading

- Acemoglu, D. & Restrepo, P. (2019). *Automation and New Tasks: How Technology Displaces and Reinstates Labor*. A clear, non-technical statement of the task-based framework on which exposure measures and macro forecasts are built. [@acemoglu2019automation]
- Brynjolfsson, E., Li, D. & Raymond, L. (2025). *Generative AI at Work*. The most detailed field study of AI in a real workplace, with a careful account of how a quasi-experimental design is tested. [@brynjolfsson2025generative]
- Becker, J. et al. (2025). *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*. A randomised trial whose result shows why expectations are a poor guide to effects; read it with METR's 2026 follow-up note on selection. [@becker2025measuring]
- Humlum, A. & Vestergaard, E. (2026). *Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI*. Links surveys to administrative records to show work being reorganised while earnings and hours stay flat. [@humlum2025still]
- Acemoglu, D. (2025). *The Simple Macroeconomics of AI*. A transparent macroeconomic estimate whose assumptions can be inspected and changed one by one. [@acemoglu2025simple]
- Gray, M. L. & Suri, S. (2019). *Ghost Work: How to Stop Silicon Valley from Building a New Global Underclass*. An ethnographic and survey study of the hidden on-demand workers behind apparently automated services. [@gray2019ghost]


# Chapter 9: Information, Media and Democracy

On 21 January 2024, two days before the New Hampshire presidential primary in the United States, thousands of voters received a telephone call in a voice that sounded like President Joe Biden. The voice had been cloned with generative AI, and the message urged recipients to "save your vote for the November election" instead of voting in the primary. The US Federal Communications Commission (FCC) traced the calls to a political consultant, Steve Kramer, and proposed a $6 million fine against him for unlawfully spoofing caller identification [@fcc2024proposes]. It confirmed the fine in a forfeiture order adopted on 26 September 2024 [@fcc2024issues]. In a separate state criminal trial, a New Hampshire jury acquitted him in June 2025 of all voter-suppression and impersonation charges [@associatedpress2025new].

The episode compresses the main questions about AI and the information ecosystem into one case. The fake was cheap: according to a 2025 study, the audio was made with ElevenLabs, a commercial service offering "instant voice cloning for as little as $5 a month" [@barrington2025people]. Listeners had no reliable way to tell it from the real voice. Its effect on turnout is unknown, because nobody can count the people who stayed at home. And the institutional response came from a telecoms regulator applying the Truth in Caller ID Act [@fcc2024issues], not from any rule about synthetic media.

## 9.1 How synthetic media is made, and what cheapness changes

**Synthetic media** is any image, audio, video or text generated or substantially altered by AI. A **deepfake** is synthetic media that realistically depicts a real person, place or event in a way that could be mistaken for authentic. The EU's AI Act defines a deep fake as AI-generated or manipulated image, audio or video content that resembles existing persons, objects, places, entities or events and "would falsely appear to a person to be authentic or truthful" [@europeanparliament2024regulation, Article 3(60)]. A **cheap fake** is a misleading edit made with ordinary tools, such as slowing down a video or cutting a quotation out of context. Researchers also distinguish **misinformation** (false or misleading content shared without intent to deceive) from **disinformation** (false content spread deliberately), and both from **influence operations**, coordinated and often covert efforts, frequently by states, to shape opinion through networks of fake accounts.

### Images and video: diffusion models

Many current image generators are **diffusion models**. The method, set out by Ho, Jain and Abbeel in 2020, has two halves [@ho2020denoising]. In training, a real image is gradually destroyed by adding small amounts of random (Gaussian) noise over many steps. In their model there were *T* = 1,000 steps, with the variance of the noise added at each step rising linearly from 0.0001 to 0.02. After the last step less than 1% of the original image's signal remains, and the result is practically indistinguishable from pure noise. A neural network is trained on large numbers of such corrupted images to solve one narrow task: given a noisy image and the step number, predict the noise that was added. Generation runs the process backwards. The model starts from pure noise and, step by step, removes part of its own estimate of the noise (adding a little fresh randomness at each step), until an image emerges that looks as if it came from the training distribution.

Rombach and colleagues made text-to-image generation practical [@rombach2022high]. They ran the diffusion process on a compressed "latent" representation produced by a separate autoencoder instead of on the pixels, which cut the computing cost of training and generation substantially. They also let a text prompt steer each denoising step through cross-attention, a variant of the attention mechanism described in Chapter 3 in which the image being generated attends to the words of the prompt. This **latent diffusion** design made high-resolution text-to-image generation affordable outside the largest laboratories.

### Voices: speech as a language-modelling problem

Voice cloning followed a parallel path. Microsoft's VALL-E, described in a 2023 preprint and published in a journal in 2025, converts speech into sequences of discrete codes using a neural audio codec, then trains a language model to predict those codes much as a text model predicts words. It was trained on tens of thousands of hours of English speech (60,000 in the preprint, 50,000 in the journal version). It could then imitate an unseen speaker from "only a 3-second enrolled recording" used as a prompt, preserving the speaker's emotional tone and acoustic surroundings [@wang2023neural]. Commercial services had turned such methods into consumer products by 2024. In one study, Barrington, Cooper and Farid built clones of more than 200 speakers with the ElevenLabs "Instant Voice Cloning" service, using audio from only the first two recorded prompts of each speaker [@barrington2025people].

### What cheapness changes, and what it does not

Generative AI therefore mainly changes one part of the information system: the cost of producing plausible content. In a 2023 preprint, Goldstein and colleagues argued that language models could make influence operations cheaper, larger and harder to attribute. They located four points where intervention is possible: how models are built, who can access them, how content is disseminated and how audiences form beliefs [@goldstein2023generative]. The evidence on the third and fourth links tempers the concern about the first two. Meta reported in December 2024 that the covert influence networks it had taken down made "only incremental productivity and content-generation gains" from generative AI [@clegg2024what]. The 2026 International AI Safety Report, written by an independent expert panel, found that in experiments AI systems are often at least as effective as non-expert humans at changing people's views. Real-world use of AI to influence people, however, "is documented but not yet widespread" [@bengio2026international, sec. 2.1.2].

The reason, according to a strand of research on misinformation, is that production was never the binding constraint. In an essay for the Knight First Amendment Institute, Kapoor and Narayanan (2024) argue that AI lowers the cost of creating false content but not the cost of distributing it. Misinformation, they argue, spreads mainly because of demand: people seek out claims that fit what they already believe [@kapoor2024looked]. Altay, Berriche and Acerbi (2023) reach a similar conclusion from the research literature. People do not believe everything they see online, and misinformation largely "preaches to the choir", reaching those who already agree [@altay2023misinformation]. The picture is complicated by AI that can hold a conversation, adapting to each person's objections as static content cannot (Section 9.5), and by generative models built into the distribution channels themselves, from search pages to social feeds (Section 9.7).

## 9.2 Detection: why people and machines struggle

### Human judgement

In laboratory tests, people are poor judges of synthetic media. In a pre-registered experiment with 210 participants, Köbis, Doležalová and Soraperra (2021) found that people could not reliably tell deepfake videos from real ones; neither raising awareness nor paying for correct answers improved accuracy, and participants overestimated their own ability [@kobis2021fooled]. Nightingale and Farid (2022) showed participants a mix of real photographs of faces and faces generated by StyleGAN2, an image generator released in 2019. In the first experiment (315 participants), accuracy was 48.2%, no better than a coin toss. Training and trial-by-trial feedback raised it only to 59.0% in a second experiment. In a third, synthetic faces were rated 7.7% more trustworthy than real ones [@nightingale2022ai].

Voices are no easier. Barrington and colleagues ran perceptual studies with 604 listeners. Participants judged a cloned voice to belong to the same person as the real recording "approximately 80% of the time", and correctly identified a voice as AI-generated "only about 60% of the time" [@barrington2025people]. For video, Groh and colleagues (2022) asked 15,016 participants in two online studies to sort authentic videos from deepfakes. Ordinary viewers were about as accurate as the leading computer-vision detector, although they made different kinds of mistakes. Showing participants the model's prediction improved average accuracy, but when the model was wrong it often led people to revise their answers in the wrong direction [@groh2022deepfake].

### Automated detectors

Automated detectors are classifiers trained on examples of real and generated media to pick up statistical traces that generators leave behind. On academic benchmarks they often score well. Performance is usually reported as the **AUC** (area under the receiver operating characteristic curve): the probability that the detector gives a randomly chosen fake a higher "fake" score than a randomly chosen genuine item. An AUC of 1.0 is perfect; 0.5 is guessing.

The problem is **distribution shift**: a detector learns the fingerprints of the generators in its training data, and new generators leave different ones. A 2025 preprint by Chandra and colleagues at the non-profit TrueMedia.org tested this directly. They assembled Deepfake-Eval-2024 from deepfakes circulating in 2024, collected from social media and from users of TrueMedia.org's free detection service, among them journalists: video, audio and images from 88 websites in 52 languages. Compared with their scores on older academic benchmarks, the AUC of open-source detectors fell on average by 50% for video, 48% for audio and 45% for images. The best open-source model in any modality reached an AUC of 0.58, and many were close to 0.5. Commercial detectors from seven vendors did better, but none reached 90% accuracy, which the authors treat as a lower bound for what trained human forensic analysts achieve on the same material [@chandra2025deepfake].

Better engineering will not remove the next obstacles, because they are structural. Detection is an adversarial game. Saberi and colleagues proved, for classifier-based detectors of AI-generated images, a trade-off between robustness (resisting small perturbations) and reliability (catching fakes with few false alarms) that sharpens as real and fake images become more alike, and demonstrated it experimentally [@saberi2024robustness]. A generator's developer, or anyone with access to a detector, can test outputs against it and adjust them until they pass. Base rates compound the problem. Consider an illustrative detector that flags 99% of fakes and wrongly flags only 1% of genuine items. Applied to a platform's stream of one million genuine videos and one thousand fakes, it would catch 990 fakes but also flag 10,000 genuine videos, so that more than nine in ten alarms would be false. Detection of AI-written *text* faces the same problems in sharper form: a test of 14 tools found them "neither accurate nor reliable" [@weberwulff2023testing], and Chapter 10 describes their bias against non-native English writers.

## 9.3 Watermarks and provenance: labelling at the source

If synthetic content cannot reliably be recognised after the fact, an alternative is to mark it when it is made. **Watermarking** hides a signal in AI-generated content at the moment of creation, so that software holding the right key can later recognise it. **Content provenance** attaches a cryptographically signed record of where content came from and how it was edited. The two answer different questions, and they fail in different ways (Table 9.1).

### Text watermarks: the green-list scheme and SynthID

The best-studied text watermark was proposed by Kirchenbauer and colleagues in 2023 [@kirchenbauer2023watermark]. Its logic is statistical, and the Deeper box below works through it with the paper's own numbers.

::: {.box .deeper}
**Going deeper: How a text watermark is embedded and detected**

A language model writes by repeatedly choosing the next token (a word or word fragment). In the scheme of Kirchenbauer and colleagues, a secret key and the preceding token are fed into a hash function before each choice. The function splits the vocabulary pseudo-randomly into a "green list" containing a fraction γ (gamma) of all tokens and a "red list" containing the rest. The model then adds a bonus δ (delta) to the scores of green tokens before sampling. Where many words would fit, this tilts the choice towards green ones; where one word is almost certain, such as the second half of a name, the bonus barely matters and quality is preserved.

A detector that knows the key recomputes the green list at every position and counts green tokens. Unwatermarked text should contain about γ*T* green tokens in a passage of *T* tokens, with a standard deviation of √(*T*γ(1 − γ)). The test statistic *z* is the excess count divided by that standard deviation. With γ = 0.5 and *T* = 200, chance predicts 100 green tokens with a standard deviation of about 7.1. The authors flag text as watermarked when *z* exceeds 4, which happens at about 128 green tokens and corresponds to a false-positive probability of 3 in 100,000. In their tests with δ = 2, watermarked 200-token passages contained 159.5 green tokens on average, far above the threshold, and 98.4% of them were detected [@kirchenbauer2023watermark]. The failures were mostly low-entropy passages, such as memorised text, where the model had little freedom to choose green words.
:::

Google DeepMind's SynthID-Text, published in *Nature* in 2024, uses a different embedding method called tournament sampling. The model proposes many candidate tokens, which compete in a knockout tournament, 30 rounds deep in the authors' default setting. In each round a pseudo-random function keyed to the four preceding tokens scores the candidates, and the final winner is emitted. Detection again needs the key but not the model [@dathathri2024scalable]. Google tested it in a live experiment on nearly 20 million Gemini chatbot responses: the rates at which users gave watermarked and unwatermarked answers a thumbs-up or thumbs-down differed by 0.01% and 0.02%, within statistical noise. The authors released the code openly and listed the limits themselves: watermarks are weakened by paraphrasing, they work less well in low-entropy text, and they require "coordination between actors running the LLM text generation services" [@dathathri2024scalable]. Google also applies SynthID to images and video. In November 2025 it began letting anyone check in its Gemini app whether an image carried a SynthID mark, and said that more than 20 billion pieces of AI-generated content had been watermarked [@kohli2025how].

### How robust are watermarks?

Robustness is the central technical weakness. Kirchenbauer and colleagues themselves tested an attack in which a second, smaller language model (T5-Large) replaced randomly chosen words in watermarked 200-token passages. Replacing 10% of tokens left detection almost intact; replacing 30% or more degraded it markedly, but also degraded the text, as Figure 9.1 shows [@kirchenbauer2023watermark]. Watermarks are therefore hard to remove by light editing, and an attacker who rewrites heavily pays in quality, unless the attacker has another strong model at hand, in which case the watermarked one was unnecessary.

![Figure 9.1: Trade-off between removing a text watermark and preserving text quality. A smaller model (T5-Large) replaced words in 500 watermarked passages of about 200 tokens, up to a growing share of the tokens. Detection quality (AUC, left axis; 0.5 = chance) falls as more words are replaced, while perplexity (right axis; higher = less fluent text) rises from 6.3 to 33.9. Watermark settings γ = 0.5, δ = 2.0, multinomial sampling. Source: @kirchenbauer2023watermark.](../figures/svg/fig-09-01.svg){#fig:09-01}

Later work found more economical attacks. Zhang and colleagues proved that, under natural assumptions, no watermark can be "strong", meaning impossible to remove without degrading quality. An attacker with a way to judge quality and a way to make small random changes can always walk the text away from the watermark while keeping it good [@zhang2024watermarks]. Jovanović, Staab and Vechev showed that an attacker can partly reverse-engineer a green-list-style watermark by querying the model's public interface and studying its outputs. With that knowledge the attacker can both strip the watermark from text ("scrubbing") and make text of the attacker's choosing appear watermarked ("spoofing"). For "under $50", they reached average success rates above 80% against schemes previously considered safe [@jovanovic2024watermark]. Image watermarks face analogous limits. Saberi and colleagues showed that "diffusion purification", adding noise to a watermarked image and letting a diffusion model clean it up, removes watermarks that make only subtle changes to an image, while stronger watermarks can be defeated by an attack on a substitute model. Spoofing works here too: a watermarked noise pattern can be added to real photographs so that they are wrongly flagged as AI-generated [@saberi2024robustness].

Watermarks also depend on who controls them. A watermark exists only if the generator adds it, and open-weight models (Chapter 7) can be run without one. And the detector key is a security asset: if it is widely shared, attackers can test their evasion against it; if it is held tightly, as with SynthID, whose checks run through Google's own tools, outside verification depends on the company.

### Content Credentials: how C2PA provenance works

Provenance starts from the opposite assumption: instead of trying to prove that content is fake, it lets honest sources prove where their content came from. The main standard is maintained by the Coalition for Content Provenance and Authenticity (C2PA), founded in February 2021 by Adobe, Arm, the BBC, Intel, Microsoft and Truepic [@microsoft2021technology], and marketed to the public as "Content Credentials".

Specification version 2.2 (May 2025) sets out how it works [@c2pa2025content]. When a camera or AI tool creates a file, it attaches a signed record of who made it and how; for AI output, the record states that the content was generated by a trained algorithm. Each later edit adds a new signed record that keeps the earlier ones, so the file carries its own history. Any change made outside this chain, even to a single pixel, breaks the seal, and validation fails. The record is easily stripped, for instance when a platform re-encodes an upload, so the standard also lets a watermark or fingerprint point to a copy kept online. Signers are identified by certificates that the coalition's default trust list expects to be issued to hardware or software, not to a person. Version 2.0 (January 2024) removed identified humans from the metadata, a choice relevant to photographers and witnesses whose safety depends on anonymity [@c2pa2025content]. And the coalition states plainly that provenance "cannot tell you whether the digital content is true, accurate or factual" [@c2pa2025c2pa]. Figure 9.2 shows the pipeline.

::: {.box .deeper}
**Going deeper: Inside a C2PA manifest**

Each signed record is a **manifest**, and a file's manifests together form its **manifest store**, usually embedded in the file in a container format called JUMBF, or held externally and referenced. A manifest holds three things. **Assertions** are labelled statements about the content. The mandatory `c2pa.actions` assertion records what was done to the file, starting with a "created" action (or "opened", when an existing file is edited). For AI output, its `digitalSourceType` field takes the value `trainedAlgorithmicMedia`, a term from the news industry's IPTC vocabulary. Ingredient assertions list the earlier files from which this one was composed, whose own manifests are copied in. The **claim** is a data structure that references every assertion by its cryptographic hash. The **claim signature** signs the claim with the private key behind an X.509 certificate, the public-key technology that secures web browsing, in the COSE_Sign1 format. A trusted time-stamp from an external authority (RFC 3161) lets a signature remain verifiable after the signing certificate expires. The most recent manifest, the "active manifest", is the one validated against the file.

The manifest is tied to the content by a **hard binding**: one or more cryptographic hashes of the file's bytes, which is why changing a single pixel breaks the match. A **soft binding** is a watermark or perceptual fingerprint that survives re-encoding and can be used to look up a copy of the manifest in a cloud repository. Soft bindings, the specification insists, "shall not be used as a hard binding" [@c2pa2025content].
:::

![Figure 9.2: A simplified content provenance pipeline (C2PA Content Credentials). A camera or AI tool creates content and signs a manifest whose actions begin with “created”; an editing step adds a new signed manifest (“opened”) that keeps the earlier file and its manifest as an ingredient; a validator checks the signatures, certificates and hashes, including whether the hard binding still matches the file. Inside each manifest, a claim lists every assertion by its hash and is signed (COSE_Sign1 with an X.509 certificate, plus an RFC 3161 time-stamp). If the manifest is stripped, a soft binding (watermark or fingerprint) can be used to find a copy in a cloud repository. Provenance shows where content came from, not whether it is true. Schematic. Diagram by the author, based on @c2pa2025content and @c2pa2025c2pa.](../figures/svg/fig-09-02.svg){#fig:09-02}

Adoption has moved from software to hardware. In September 2025 Google announced that the Pixel 10 phones attach Content Credentials to every JPEG photograph taken with the built-in camera app, not only to AI-edited images. It said the app had achieved "Assurance Level 2", the highest security rating then defined by the C2PA's conformance programme, using keys protected by the phone's security chip. The company gave an explicit reason for signing everything. If only synthetic content is labelled, users come to believe that unlabelled content is authentic, which Google described, citing research, as "the implied truth effect" [@lynch2025how]. That effect is well documented for fact-check labels. In an experiment with 5,271 participants, Pennycook and colleagues found that attaching warnings to some false headlines made untagged false headlines seem more accurate. Marking some true headlines as verified removed the effect [@pennycook2020implied].

Provenance has its own limits. It depends on cameras, editing tools, platforms and browsers all reading and displaying the credentials. A signed record that a photograph came from a particular phone does not show that the scene was not staged. Most authentic content in circulation carries no credentials at all, so absence proves nothing. Provenance is therefore strongest for sources that choose to sign, such as news agencies and official bodies, and weakest at exposing fakes from those that do not.

| | Post-hoc detection | Watermarking | Provenance (C2PA) |
|---|---|---|---|
| Question answered | Does this look AI-made? | Did a participating generator make this? | Who signed this, and what was done to it? |
| Needs cooperation of | Nobody | The generator's developer | Creators, tools and platforms |
| Typical failure | New generators (distribution shift); base-rate false alarms | Paraphrase or regeneration; open models without marks; spoofing | Metadata stripped; low adoption; staged content signed honestly |
| Evidence | Best open-source AUC 0.58 on 2024 in-the-wild content | Removable for under $50 in some schemes; quality cost for crude attacks | Hash binding breaks on any change; soft binding needed to survive re-encoding |

: Table 9.1: Three technical approaches to identifying synthetic or authentic content. Source: [@chandra2025deepfake; @jovanovic2024watermark; @kirchenbauer2023watermark; @c2pa2025content].

## 9.4 Deepfakes and the 2024 election year

### What monitoring found

In 2024 voters went to the polls in the United States, India, Indonesia, Mexico, the United Kingdom, the European Union and many other places [@clegg2024what]. Many commentators predicted that generative AI would flood these campaigns with deceptive content. The evidence gathered since points towards a limited measurable impact on results, with important caveats about what can be measured.

The most systematic monitoring came from the Alan Turing Institute's Centre for Emerging Technology and Security (CETaS). Its September 2024 briefing paper on the UK general election, the French legislative elections and the European Parliament elections identified "just 16 confirmed viral cases" of AI-enabled disinformation or deepfakes during the UK election and "only 11" across the EU and French elections combined. It found "no evidence" that they "meaningfully impacted" any result [@stockwell2024threat]. The institute's November 2024 report on the US election likewise reported a "lack of evidence" of a measurable impact on the result. It attributed this "primarily" to "insufficient data" on real-world voter behaviour. It recorded "far higher – albeit still relatively moderate – volumes" of viral AI-enabled disinformation in the US campaign than in the earlier elections. It also warned that users' uncertainty about what was authentic had "damaged trust in the integrity of online sources" [@stockwell2024ai].

Platform data point the same way, with an obvious limitation. Meta, which owns Facebook and Instagram, reported that ratings of AI content about elections, politics and social topics made up "less than 1%" of all misinformation fact-checked by its partners during the major elections of 2024 [@clegg2024what]. That figure covers only content that fact-checkers chose to examine.

### Cheap fakes outnumbered deepfakes

Kapoor and Narayanan (2024) analysed 78 election-related uses of AI collected by WIRED's AI Elections Project. Half of them (39) showed no deceptive intent: they included parody and satire, and campaigns using AI openly, for example to translate a speech, which was the most common non-deceptive use. For each of the 39 deceptive cases, the authors estimated that similar content could have been produced without AI for no more than a few hundred dollars. They also cited a count by the News Literacy Project in which cheap fakes were used about seven times as often as AI-generated content in the US election [@kapoor2024looked]. The bottleneck for a would-be deceiver in 2024 was reach and credibility, not the technical ability to fabricate.

### The liar's dividend

A subtler effect works through authentic content. When the public knows that convincing fakes exist, a person caught on a genuine recording can claim that it was faked. Chesney and Citron (2019) called this the **liar's dividend** and noted, perversely, that it grows as public education about deepfakes succeeds, because a sceptical public is more willing to doubt real evidence [@chesney2019deep].

Schiff, Schiff and Bueno (2025) tested the idea in five survey experiments with more than 15,000 American adults. Participants read about real scandals involving politicians, followed by a hypothetical response in which the politician claimed the story was fake. The authors tested two mechanisms: "informational uncertainty", making people unsure what to believe, and "oppositional rallying", encouraging the politician's supporters to close ranks against the accusers. Both raised support for the politician across partisan groups, and both worked better than staying silent or apologising. The claims were effective against text-based reports but "largely ineffective against video evidence", and they did not reduce general trust in the media [@schiff2025liars]. The result confirms the existence of a liar's dividend while suggesting that, when the experiments were run, video still carried more evidential weight than text. As video generation improves, that is the margin most likely to erode.

::: {.box .debate}
**Debate: Were fears about AI and the 2024 elections overblown?**

*Largely, yes.* Simon, Altay and Mercier (2023) argued before the election year that supply of false content was never the main constraint on misinformation; attention and belief are [@simon2023misinformation]. The 2024 record set out above fits their view: a few dozen viral AI cases, no measurable effect on any result, and cheap fakes that far outnumbered AI content [@stockwell2024threat; @stockwell2024ai; @kapoor2024looked].

*Not proven.* Every one of these sources measures visible content, not effects on behaviour. CETaS itself said the US finding reflected "insufficient data", and monitoring covered mainly the UK, France, the EU and the US. The cheapest harm, eroding confidence that any evidence is real, is the hardest to count, yet it is the one that survey experiments on the liar's dividend show can benefit politicians [@schiff2025liars]. Private conversations with chatbots, which experiments show can shift attitudes (Section 9.5), are invisible to monitoring of public posts. Settling the question would take panel data that link individuals' exposure to AI-generated content, obtained through platform data access, to later changes in their knowledge, trust and turnout, collected across several elections as the tools improve.
:::

The most consequential interference of the period did not depend mainly on generative AI. The annulment of Romania's 2024 presidential election, discussed in Section 9.8, turned on the alleged coordinated amplification of content by platform accounts and undisclosed paid promotion.

## 9.5 AI as a persuader

### The baseline: persuasion is hard

Political scientists have long found that changing voters' minds during a general election is difficult. Kalla and Broockman (2018) combined a meta-analysis of 40 field experiments with nine new experiments of their own and concluded that the best estimate of the effect of campaign contact and advertising on Americans' candidate choices in general elections is zero [@kalla2018minimal]. Any claim that AI is unusually persuasive has to be read against that baseline.

### Static messages: as good as humans, little more

The first generation of studies examined static messages: a fixed text that every participant reads. Goldstein and colleagues (2024) gave 8,221 US respondents either nothing, a real article from a foreign covert propaganda campaign, or an article on the same thesis written by GPT-3. Among respondents who read no article, 24.4% agreed with the propaganda thesis. Reading the original propaganda raised agreement to 47.4%, and reading the GPT-3 version raised it to 43.5%. With an English speaker editing the prompts or selecting the outputs, GPT-3 articles were under some conditions as persuasive as the originals [@goldstein2024persuasive].

Later studies found that neither tailoring nor model scale adds much to a static message. Hackenburg and Margetts (2024) built an application that fed each participant's self-reported demographic and political data into GPT-4 prompts in real time, producing individually tailored messages on four political issues. In a pre-registered experiment with 8,587 participants, these **microtargeted** messages moved opinion by 4.83 percentage points against 6.20 points for generic GPT-4 messages, a difference that was not statistically significant (*P* = 0.226) [@hackenburg2024evaluating]. Hackenburg and colleagues (2025) then generated 720 messages on ten US policy issues with 24 language models of very different sizes and tested them on 25,982 participants. Persuasiveness showed "sharply diminishing returns" to model size. Once the authors adjusted for basic task completion (staying coherent and on topic), the association between size and persuasiveness was no longer statistically significant [@hackenburg2025scaling]. For static text, frontier models appeared to be close to a ceiling.

### Conversation is different

The picture changed when AI was allowed to talk back. Costello, Pennycook and Rand (2024) asked 2,190 Americans who believed a conspiracy theory to describe it in their own words, together with the evidence they found convincing. Participants then had three rounds of conversation with GPT-4 Turbo, which was instructed to reduce their belief using evidence tailored to their stated reasons. Belief in the chosen conspiracy fell by about 20% on average, and the effect persisted undiminished for at least two months. A professional fact-checker rated 99.2% of a sample of the AI's claims as true. Where the chosen conspiracy was in fact true, the AI did not reduce belief. The effect also spilled over to reduce belief in unrelated conspiracy theories. In the preprint version of the study, 27.4% of treated participants, against 2.4% of the control group, ended below the midpoint of the belief scale, that is, uncertain [@costello2024durably]; the authors' university summarised this as about one in four participants disavowing the conspiracy. The effect was smaller, though still present, among those for whom the conspiracy was central to their worldview [@cornell2024ai].

The same capacity can be pointed in any political direction. In the largest study to date, the most persuasive set-ups were also the least accurate. Hackenburg and colleagues (2025) tested many language models on hundreds of political issues with 76,977 UK adults, and fact-checked the claims the models made [@hackenburg2025levers]. Conversation was markedly more persuasive than a static message from the same model, and post-training a model for persuasion or changing how it was prompted raised its effect further, while personalisation added almost nothing. The dominant mechanism was information density: the more fact-checkable claims a model packed into a conversation, the more it persuaded. In an estimated "maximal persuasion" condition combining the most effective levers, 30.0% of fact-checkable claims were rated inaccurate, against 16.0% on average. Table 9.2 gives the effect sizes and their durability.

Lin and colleagues (2025) moved from policy issues to real elections. In pre-registered experiments before the 2024 US presidential election, the 2025 Canadian federal election and the 2025 Polish presidential election, participants were randomly assigned to converse with an AI that advocated for one of the two leading candidates. In the US the gap in candidate preference between the pro-Harris and pro-Trump conditions was 2.88 points on a 0–100 scale. In Canada and Poland it was about 10 points, effects the authors note are larger than those typically found for video advertisements. For a Massachusetts ballot measure on psychedelics, the gap among participants without extreme prior views was 22.73 points. Slightly more than a third of the US effect persisted after more than a month. In Canada and Poland, instructing the AI not to use facts and evidence cut its effect by more than half. Models advocating for right-leaning candidates made more inaccurate claims in all three countries, as rated by an AI system validated against professional fact-checkers and politically balanced lay panels [@lin2025persuading].

Salvi and colleagues (2025) compared AI directly with people. In short multi-round debates with 900 participants, GPT-4 given basic demographic information about its opponent was more persuasive than a human opponent in 64.4% of the pairs where the two differed. That corresponds to an 81.2% increase in the odds of higher post-debate agreement (95% CI 26.0% to 160.7%) [@salvi2025conversational]. Table 9.2 and Figure 9.3 summarise these studies.

| Study | Participants | Design | Main estimate | Durability |
|---|---|---|---|---|
| Goldstein et al. 2024 | 8,221 (US) | GPT-3 article vs real propaganda | Agreement 24.4% (none) → 47.4% (real) and 43.5% (GPT-3) | Not measured |
| Hackenburg & Margetts 2024 | 8,587 | GPT-4 messages, tailored vs generic | 4.83 vs 6.20 points; difference not significant | Not measured |
| Hackenburg et al. 2025 (PNAS) | 25,982 | 720 messages from 24 models | Sharply diminishing returns to model size | Not measured |
| Costello et al. 2024 | 2,190 (US) | Three-round dialogue against a conspiracy belief | Belief down about 20% | Undiminished at 2 months |
| Salvi et al. 2025 | 900 | Debates, GPT-4 vs human | GPT-4 with personal data more persuasive in 64.4% of non-tied pairs | Not measured |
| Hackenburg et al. 2025 (Science) | 76,977 (UK) | 19 models, 707 issues, conversation vs static | Conversation +41% to +52% over static (6.1–6.9 points) | 36–42% at 1 month |
| Hackenburg et al. 2025 (Science), levers | Same; 466,769 claims fact-checked | Persuasion post-training, prompting, personalisation | Post-training up to +51%, prompting up to +27%, personalisation +0.43 points (never >1); about 0.3 points per extra claim, claims ~half of explainable variation; maximal persuasion 15.9 points (26.1 among initial opponents) vs 9.4 average, with 30.0% vs 16.0% of claims inaccurate | See row above |
| Lin et al. 2025 | 2,306 (US); 1,530 (CA); 2,118 (PL); 501 (MA) | AI advocates for rival candidates | Gap 2.88 (95% CI 2.02–3.74; US), 10.05 (CA), 9.94 (PL), 22.73 points (MA ballot, non-extreme voters) | Just over 1/3 after >1 month (US) |

: Table 9.2: Experimental evidence on AI persuasion. Effects are on the scales used by each study and are not directly comparable across rows. Source: [@goldstein2024persuasive; @hackenburg2024evaluating; @hackenburg2025scaling; @costello2024durably; @salvi2025conversational; @hackenburg2025levers; @lin2025persuading].

![Figure 9.3: Persuasive effects of AI in recent experiments, in points on 0–100 attitude or preference scales, with 95% confidence intervals where reported. Conversation with AI produced larger effects than a static AI-written message, and effects were smaller in the high-salience US presidential race than in Canada, Poland or a state ballot measure. The studies measure effects differently (treatment versus control, or the gap between two opposing AI advocates), so bars are comparable only within each study. Source: @hackenburg2025levers; @lin2025persuading; @kalla2018minimal.](../figures/svg/fig-09-03.svg){#fig:09-03}

### External validity

The experiments were artificial in ways that matter for real elections: participants were recruited online, paid and told they were talking to an AI. In the experiments of Hackenburg and colleagues, conversations lasted nine minutes on average [@hackenburg2025levers], and few voters choose to spend that long discussing politics with a chatbot. Outside experiments such use is still a minority habit: in the Reuters Institute's 2026 survey, 10% of respondents used AI chatbots for news each week [@egan2026digital]. Effects decayed, with roughly a third to two-fifths remaining after a month in the two largest studies, and an election campaign exposes voters to many competing messages. Lin and colleagues debriefed participants before the elections and randomised the direction of persuasion, so that any lasting effects would cancel out. They suggest that AI dialogue may matter more in state and local contests, where voters have weaker prior views, than in national ones [@lin2025persuading].

Other features of the results make them more concerning. The effects came mainly from presenting information, not from psychological tricks or personal data, so they do not depend on any capability that providers could easily withhold. Persuasiveness and accuracy pulled in opposite directions in both large studies. A campaign optimising for votes would therefore be pushed towards the less accurate configurations, unless model developers or regulators constrain it.

## 9.6 Synthetic respondents: AI as a stand-in for the public

A different use of language models is to replace survey respondents. Argyle and colleagues (2023) conditioned GPT-3 on thousands of first-person "backstories" built from the demographic and political characteristics of real participants in the American National Election Studies (ANES) of 2012, 2016 and 2020 [@argyle2023out]. In the preprint version of the study, the model's predicted Republican vote share came within six percentage points of the ANES figure in each year (0.391 against 0.404 in 2012, for example). The tetrachoric correlation between individual simulated and reported votes, a measure of agreement for yes/no variables, was 0.90 to 0.94. The authors called this property **algorithmic fidelity**: with the right conditioning, a model reproduces the response patterns of many subgroups. They named the resulting synthetic respondents **silicon samples**; using them in place of human respondents has come to be called **silicon sampling**. The authors proposed such samples as a new tool for social-science research.

The later evidence found the limits. Bisbee and colleagues (2024) asked ChatGPT, adopting different personas, to rate 11 social and political groups. Average scores closely matched the ANES, but the synthetic answers varied far less than real ones, and the statistical relationships between variables often differed from those in the human data. Results changed with small changes to prompt wording, and the same prompt gave significantly different results over three months, a serious problem for reproducibility [@bisbee2024synthetic].

The most demanding test so far came from the Pew Research Center in September 2026 [@pew2026well]. Pew built a "digital twin" for each member of its American Trends Panel who had completed its 2025 political typology survey, giving the model the person's demographics and earlier answers. It then had the twins answer three 2026 survey waves, question by question, under the same instructions as the human panellists. The best-performing model, Anthropic's Claude Opus 4.6, missed the human results by 12.4 percentage points on average across the three waves. Errors were 16.1 points for Republicans and Republican leaners and 13.6 for Democrats and Democratic leaners. Pew reported that no demographic group had an average error below 12 points (the lowest in its table, for college graduates, was 11.9). The deeper problem was homogeneity. The synthetic respondents were "far less politically diverse" than the population and turned majority views within a party into near-unanimity. Among synthetic Democrats and Democratic leaners, 86% said that having people with fortunes of a billion dollars or more is a bad thing for the country, against 45% of real ones. More than 90% of synthetic Republicans, against 69% of real ones, said police should be allowed to stop anyone who fits a suspect's description. Pew stated that it has no current or future plans to use AI models to generate survey results [@pew2026well].

Across the three studies, models capture the average direction of opinion in large, well-studied groups. They miss the variance within groups and the views of people whose opinions cut across party lines, and their answers shift with prompt wording and model version. Variance, cross-cutting views and change over time are exactly what surveys exist to measure. Silicon samples can still help design questionnaires or explore hypotheses before fieldwork, but the evidence does not support using them in place of asking people.

## 9.7 Recommender systems, AI search and journalism

### Recommender systems and polarisation

A **recommender system** is software that selects and ranks content for each user, such as the order of posts in a social media feed, usually by predicting what the user will engage with. Recommender systems shaped public information long before chatbots, and a common fear is that they create "echo chambers" and increase **polarisation**, the growing distance or hostility between political groups.

Some of the strongest evidence comes from a collaboration between Meta and independent academics during the 2020 US election. Guess and colleagues (2023) switched a sample of consenting Facebook and Instagram users from the algorithmic feed to a reverse-chronological one. Time on the platforms fell substantially, and users saw more political and more untrustworthy content; over three months, there was no significant change in polarisation, political knowledge or other key attitudes [@guess2023social]. Nyhan and colleagues (2023) reduced exposure to content from like-minded sources by about a third for 23,377 users and found no measurable effect on eight pre-registered attitude measures, including polarisation and belief in false claims [@nyhan2023like]. González-Bailón and colleagues (2023) used aggregated data on 208 million US Facebook users. Ideological segregation in political news was high and increased at each stage, from what users could have seen, to what the feed showed them, to what they engaged with. It was also asymmetric: a substantial corner of the news ecosystem was consumed exclusively by conservatives, and most content rated false by Meta's fact-checkers sat in that corner, with no equivalent on the liberal side [@gonzalezbailon2023asymmetric].

Other studies found effects from more targeted changes. A long-running randomised experiment on Twitter compared users of the algorithmic feed with a control group of nearly 2 million daily active accounts on a chronological feed. The mainstream political right enjoyed higher algorithmic amplification than the mainstream left in six of seven countries studied, with no evidence that far-left or far-right groups were amplified more than moderate ones [@huszar2022algorithmic]. Piccardi and colleagues (2025) used a language model to rerank, in real time, the X feeds of 1,256 participants during the 2024 US campaign, demoting or promoting posts expressing antidemocratic attitudes and partisan animosity. Over ten days, this shifted feelings towards the opposing party by more than 2 points on a 100-point "feeling thermometer", in both directions and with no detectable difference between Democrats and Republicans [@piccardi2025reranking]. The two sets of findings are compatible. Removing the algorithm wholesale changed little over three months, while targeted changes to what it promotes had measurable short-term effects. The Piccardi study also shows that independent researchers can now test ranking interventions without a platform's cooperation, using a language model to do the reranking.

### AI search and the click

Search engines now often place an AI-written summary above the list of links. Pew Research Center tracked the browsing of 900 US adults in March 2025 and analysed 68,879 Google searches, 18% of which produced an AI summary. When a summary appeared, users clicked a traditional result link about half as often as when none did, rarely clicked the links inside the summary, and more often ended their browsing session on the results page (Figure 9.4) [@chapekis2025google]. Summaries were far more common on long searches and on searches phrased as questions. News sites accounted for 5% of the sources the summaries cited, the same share as in ordinary results [@chapekis2025google]. The study observed one month of behaviour in one country.

![Figure 9.4: Share of Google search visits in which users clicked a link, with and without an AI-generated summary on the page, and share of visits that ended the browsing session. Based on the browsing data of 900 US adults, March 2025. Source: @chapekis2025google.](../figures/svg/fig-09-04.svg){#fig:09-04}

For publishers, fewer clicks mean less advertising and subscription revenue. The Reuters Institute's *Digital News Report 2026*, based on surveys in 48 markets, reports Chartbeat data on more than 2,500 news sites. Google search traffic to them fell by a third (33%) globally between November 2024 and November 2025, and by 38% in the United States. Publishers expect a further fall of 43% over three years. The report notes that the role of AI summaries in this decline is widely assumed rather than proven, and that hard-news queries are mostly excluded from them [@egan2026digital].

The same report tracks how audiences use AI for news. Weekly use of AI chatbots for news rose from 7% of respondents in 2025 to 10% in 2026, though use did not grow in the United States, the United Kingdom, France or Germany. Only 20% of respondents said they trusted news answers from chatbots, against 37% for news in general; in the UK the figure was 6%. Among chatbot news users, 42% said they always or often clicked through to the original sources, about the same as for search (44%) [@egan2026digital]. Whether AI answers attribute and link to journalism, and whether they reproduce it accurately, thus matters for both the business and the public value of news.

Accuracy remains a problem. In a study coordinated by the European Broadcasting Union (EBU) and the BBC, journalists from 22 public service media organisations in 18 countries and 14 languages rated more than 3,000 news answers from ChatGPT, Copilot, Gemini and Perplexity. Of these, 45% had at least one significant issue; 31% had serious sourcing problems and 20% major accuracy problems, such as invented details or outdated information [@ebu2025ais]. These figures describe one set of products in 2025 and may change quickly. Whether news content may lawfully be used to train AI systems belongs to the wider copyright disputes covered in Section 13.6.

## 9.8 Regulating platforms and synthetic content

The rules on what platforms must do about harmful information differ sharply between jurisdictions. In the United States, Section 230 of the Communications Act provides that no online service shall be treated as the publisher of information provided by its users [@uscongress1996protection], and new federal rules have targeted specific harms. The European Union regulates broadly, through the Digital Services Act for platforms and the AI Act for the makers and users of generative AI. Table 9.3 compares the main instruments.

### The Digital Services Act

The **Digital Services Act (DSA)** has applied in full since 17 February 2024 [@europeanparliament2022regulation, Article 93] and scales duties to platform size. Its strictest rules apply to "very large online platforms" and search engines, those with at least 45 million average monthly active users in the EU [@europeanparliament2022regulation, Article 33(1)]. Each year these must assess "systemic risks" arising from their design and use, including how their recommender systems contribute. The listed risks explicitly include "any actual or foreseeable negative effects on civic discourse and electoral processes" [@europeanparliament2022regulation, Article 34]. Platforms must then take reasonable mitigation measures. These may include testing and adapting recommender systems, and ensuring that generated or manipulated images, audio or video that falsely appear authentic are distinguishable "through prominent markings" [@europeanparliament2022regulation, Article 35(1)(d) and (k)]. They must offer at least one recommender option not based on profiling the user [@europeanparliament2022regulation, Article 38] and give vetted researchers access to data. The European Commission can fine them up to 6% of worldwide annual turnover [@europeanparliament2022regulation, Article 74].

::: {.box .case}
**Case study: Romania's annulled election and the DSA**

On 6 December 2024, Romania's Constitutional Court annulled the presidential election after its first round, two days before a scheduled run-off involving the first-round leader, Călin Georgescu. The decision followed the declassification of intelligence reports alleging a coordinated campaign on TikTok and Telegram; one report said about 25,000 pro-Georgescu TikTok accounts became highly active two weeks before the vote. Much of this evidence consisted of allegations, Georgescu called the decision a coup, and the attribution to Russia rested on similarities with earlier operations [@solea2024romanias]. On 17 December 2024 the European Commission opened formal DSA proceedings against TikTok, focused on the management of election risks linked to its recommender systems and on its rules for political advertising; opening proceedings does not prejudge the outcome [@europeancommission2024commission]. The case shows that the most consequential threats to an election may come from coordinated amplification and undisclosed paid promotion, with or without generative AI, and that annulling an election is itself contested.
:::

The DSA's first non-compliance decision came on 5 December 2025, when the Commission fined X €120 million. It found that X's paid "blue checkmark" was deceptive design, that its advertising repository lacked required information, and that its terms prevented researchers from accessing public data [@europeancommission2025commission]. The research-access finding matters for the evidence base itself: much of what is known about recommender systems comes from studies that depended on a platform's voluntary cooperation [@guess2023social], and the DSA attempts to make such access a legal right.

The DSA is contested, and the two sides rely on different kinds of evidence. Critics argue that duties framed around "systemic risks" push platforms to remove lawful speech to avoid large fines. In July 2025 the Republican majority on the US House Judiciary Committee published an interim staff report arguing that the DSA "compels global censorship". Its central claim is that platforms apply one set of terms worldwide, and that Commission officials, according to documents the committee obtained under subpoena, expected platforms to change those global terms [@housejudiciary2025foreign]. The report is a partisan document in a transatlantic dispute and rests on the committee's own selection of material. The regulation's defenders point to its text, which requires platforms to weigh negative effects on fundamental rights, including freedom of expression, alongside risks to civic discourse [@europeanparliament2022regulation, Article 34(1)(b)]. Independent empirical work gives a mixed verdict on the DSA's transparency tools. Kaushal and colleagues (2024) analysed a representative sample of the 131 million "statements of reasons" for moderation decisions that platforms submitted to the DSA Transparency Database in November 2023. They found some transparency gains but concluded that compliance "remains problematic" because the database allows platforms "a lot of discretion" in what they report [@kaushal2024automated].

### The AI Act's transparency duties

Article 50 of the AI Act divides the labelling task between two groups. **Providers** of AI systems that generate synthetic audio, images, video or text must ensure that outputs "are marked in a machine-readable format and detectable as artificially generated or manipulated". Their technical solutions must be effective, interoperable, robust and reliable "as far as this is technically feasible". The duty does not apply to tools that only assist with standard editing or do not substantially alter the input [@europeanparliament2024regulation, Article 50(2)]. **Deployers**, those who use such systems, must disclose that deepfake image, audio or video content is artificial. For evidently artistic, creative, satirical or fictional works, the duty shrinks to disclosing the existence of such content in a way that does not hamper enjoyment of the work. Deployers who publish AI-generated text to inform the public on matters of public interest must also disclose it, unless a human has reviewed it and someone holds editorial responsibility [@europeanparliament2024regulation, Article 50(4)]. Breaches can be fined up to €15 million or 3% of worldwide turnover [@europeanparliament2024regulation, Article 99(4)].

These duties began to apply on 2 August 2026 [@europeanparliament2024regulation, Article 113]. The Digital Omnibus on AI, in force since 27 July 2026, gave generative systems already on the market before that date until 2 December 2026 to add machine-readable marking. It also added two prohibitions from the same date, on AI systems that generate non-consensual intimate images of identifiable people and on those that generate child sexual abuse material [@europeanparliament2026regulation]. To make Article 50 workable, the Commission published a voluntary Code of Practice on marking and labelling AI-generated content on 10 June 2026. According to a summary by the law firm Jones Day, signatories commit to "at least two layers of machine-readable marking where necessary", such as metadata combined with a watermark. They must also provide detection tools that deployers, researchers and authorities can use, and label deepfakes with a common EU icon or equivalent [@jonesday2026european]. The layered approach reflects the evidence in Section 9.3: no single marking technique is robust on its own. Chapter 13 sets out the AI Act's overall timetable.

### Non-consensual intimate imagery

The harm from deepfakes that is best documented, and most clearly growing, is not political but sexual. Chesney and Citron (2019) predicted that the technology would be used for non-consensual intimate imagery (NCII), fraud and harassment as well as political deception [@chesney2019deep].

In the United States, the TAKE IT DOWN Act, signed on 19 May 2025, made it a federal crime knowingly to publish non-consensual intimate images of identifiable people, including AI-generated "digital forgeries". The penalty is up to two years' imprisonment where the victim is an adult and three years where the victim is a minor. Covered platforms must set up a notice-and-removal process within one year, that is by 19 May 2026. On receiving a valid request they must remove the image "as soon as possible, but not later than 48 hours", and make reasonable efforts to remove known identical copies. Failure to comply is treated as an unfair or deceptive practice enforceable by the Federal Trade Commission, and platforms are shielded from liability for good-faith removals [@uscongress2025tools]. The Electronic Frontier Foundation, a digital-rights group, opposed the law. It argued that the takedown provision covers a broader category of content than the criminal offence and "lacks critical safeguards against frivolous or bad-faith takedown requests". In its view, the 48-hour deadline will push smaller services to remove lawful material rather than verify claims [@kelley2025congress].

::: {.box .case}
**Case study: Grok and the "undressing" images of January 2026**

Around the turn of 2026, X rolled out an image-editing feature powered by its Grok chatbot that let users alter photographs of real people with simple text prompts, including requests to undress them. The Center for Countering Digital Hate, a campaigning non-profit, estimated that Grok generated about three million sexualised images over 11 days, including about 23,000 that appeared to depict children; the estimate did not establish how many were made without consent [@afp2026musks]. Regulators responded under platform law rather than AI law. On 12 January 2026 the UK regulator Ofcom opened an investigation under the Online Safety Act into whether X had assessed and mitigated the risk of illegal content; the Act allows fines of up to £18 million or 10% of qualifying worldwide revenue [@jones2026ofcom]. On 26 January the European Commission opened formal DSA proceedings into whether X had assessed and mitigated the risks of deploying Grok's functions, including "manipulated sexually explicit images", stating that "these risks seem to have materialised" [@europeancommission2026commission]. The case illustrates the gap that the AI Act's new prohibition of non-consensual intimate image generation, applicable from 2 December 2026, is intended to close: the platform rules applied only after the images had spread.
:::

| Instrument | Who is bound | Main duty relevant to synthetic media | Enforcement |
|---|---|---|---|
| EU Digital Services Act (2022/2065), in full since 17 Feb 2024 | Platforms; strictest duties for very large platforms and search engines | Assess and mitigate systemic risks, including to electoral processes; mark realistic manipulated media; researcher data access | Commission; fines up to 6% of worldwide turnover |
| EU AI Act Art. 50 (2024/1689), from 2 Aug 2026 (2 Dec 2026 for marking by systems already on the market) | Providers and deployers of generative AI | Machine-readable marking of outputs; disclosure of deepfakes and public-interest text | National authorities; fines up to €15m or 3% |
| EU AI Act Art. 5 as amended (2026/1744), from 2 Dec 2026 | Providers and deployers | Ban on AI generating non-consensual intimate images or child sexual abuse material | National authorities |
| US TAKE IT DOWN Act (Pub. L. 119-12), platform duties from 19 May 2026 | Individuals; covered platforms | Criminal offence of publishing NCII including digital forgeries; 48-hour removal | Federal prosecutors; FTC for platforms |
| UK Online Safety Act 2023 | Online services in scope, including social media | Assess and mitigate risk of illegal content, including NCII | Ofcom; fines up to £18m or 10% of revenue |

: Table 9.3: Main legal instruments governing platforms and synthetic media, as of October 2026. Source: [@europeanparliament2022regulation; @europeanparliament2024regulation; @europeanparliament2026regulation; @uscongress2025tools; @jones2026ofcom].

Each of these regimes addresses one link of the chain. The AI Act targets production, the DSA and the Online Safety Act target distribution, and the TAKE IT DOWN Act targets individual publication and removal. The division fits the evidence on synthetic media: cheap production has so far mattered less than reach, detection after the fact is unreliable, and marking at the source works only where generators, tools and platforms cooperate. Conversational persuasion adds a newer risk, because it happens in private exchanges that no monitoring of public posts can see. None of the regimes yet answers the measurement problem on which much of the evidence on AI and elections founders. It remains unclear whether independent researchers will get the data needed to trace exposure to synthetic content and link it to what people believe and do. Chapter 13 compares these approaches with those of China, the United Kingdom and international bodies.

## Further reading

- Chesney, B. and Citron, D. (2019). *Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security*. The legal analysis that introduced the "liar's dividend" and anticipated the intimate-image harms that legislators addressed six years later. [@chesney2019deep]
- Kirchenbauer, J. et al. (2023). *A Watermark for Large Language Models*. A clear, short account of how text watermarking works, including the authors' own catalogue of attacks against it. [@kirchenbauer2023watermark]
- Kapoor, S. and Narayanan, A. (2024). *We Looked at 78 Election Deepfakes. Political Misinformation Is Not an AI Problem*. A short, data-based argument for focusing on the demand for misinformation rather than its supply. [@kapoor2024looked]
- Hackenburg, K. et al. (2025). *The Levers of Political Persuasion with Conversational Artificial Intelligence*. The largest experiment on what makes AI persuasive, documenting the trade-off between persuasiveness and accuracy. [@hackenburg2025levers]
- Pew Research Center (2026). *How Well Synthetic Samples Replicate Public Opinion*. A careful, transparent test of AI "digital twins" against a real national panel, with group-by-group error rates. [@pew2026well]
- Egan, J. et al. (2026). *Reuters Institute Digital News Report 2026*. The standard annual source on how people in 48 markets get news, including from AI chatbots and search summaries. [@egan2026digital]


# Chapter 10: Education, Health and Everyday Life

In June and July 2024, first-year senior secondary students from nine public schools in Benin City, Nigeria, took part in an after-school programme to practise English. They worked in pairs with Microsoft Copilot, a chatbot built on GPT-4. Teachers set the topic and the opening prompt. The students then questioned the chatbot freely for 90 minutes, up to twice a week, for six weeks. Places were allocated by lottery among the students who volunteered, which turned the programme into a randomised controlled trial. In a working paper, the World Bank team that evaluated it reported a gain of 0.31 standard deviations on an end-of-programme assessment, and 0.23 standard deviations on the English component alone [@desimone2025chalkboards].

A few months earlier, in autumn 2023, a field experiment in a large high school in Turkey gave nearly 1,000 mathematics students access to GPT-4 during practice sessions. Students with an unrestricted chatbot solved more practice problems, then scored 17% lower than students without access when they sat an exam on their own [@bastani2025generative]. The two studies used similar technology and reached opposite headline results. The difference lies in how the tools were set up, what was measured and when, and the same questions decide how to read the evidence on AI in clinics and in private life. Effects on jobs and productivity are treated in Chapter 8, the general taxonomy of AI risks in Chapter 11, and the enforcement of data-protection law against AI developers in Chapter 13.

## 10.1 AI tutors: the benchmark and the trials

The hope behind AI tutoring has a long pedigree. In 1984 the educational psychologist Benjamin Bloom reported that students taught one-to-one by a tutor performed about two standard deviations better than students taught in a conventional class. He called the search for group methods that could match this the "2 sigma problem" [@bloom1984sigma]. Later research confirmed that tutoring works, but with much smaller effects. Kurt VanLehn's 2011 review of experiments comparing human tutoring, computer tutoring and no tutoring found an effect of 0.79 standard deviations for human tutors, far below Bloom's figure. Intelligent tutoring systems, the rule-based programs that give feedback on each step of a solution, reached 0.76, nearly as much [@vanlehn2011relative]. A meta-analysis of 50 controlled evaluations of such systems found a median effect of 0.66 standard deviations, but the effect depended heavily on whether learning was measured on tests developed locally for the evaluation or on standardised ones [@kulik2016effectiveness].

The best current estimate for human tutoring in schools comes from a meta-analysis of randomised field experiments in pre-school to year 12. It found a pooled effect of 0.288 standard deviations. Effects were largest for programmes that used teachers or paraprofessionals as tutors, took place in earlier grades, met at least three days a week and ran during the school day [@nickow2020impressive]. The obstacle has always been cost: a trained tutor for every pupil several times a week is unaffordable for most school systems. Large language models (LLMs, the text-generating systems described in Chapter 3) revived the question of whether software could supply part of what a tutor provides at a fraction of the price.

::: {.box .deeper}
**Going deeper: How to read an effect size and an education trial**

Education studies report results in standard deviations (SD) of the test score so that different tests can be compared. If scores are roughly normally distributed, an effect of 0.3 SD moves the average treated student from the 50th to about the 62nd percentile of the comparison group, and 0.63 SD to about the 74th. The psychologist Jacob Cohen's conventions, which call 0.2 "small" and 0.8 "large", come from laboratory psychology and mislead in schools.

In a 2019 working paper, later published in *Educational Researcher*, Matthew Kraft assembled effect sizes from 747 randomised trials of education interventions with standardised achievement outcomes. Their median was 0.10 SD, and he proposed treating less than 0.05 as small, 0.05 to just under 0.20 as medium and 0.20 or more as large [@kraft2019interpreting; published as @kraft2020interpreting]. By that yardstick, all the AI tutoring results below are large, which is a reason for both interest and suspicion.

Suspicion, because study design inflates effect sizes. In 645 studies drawn from 12 reviews, Cheung and Slavin found effects roughly twice as large in published articles as in unpublished reports, in small trials as in large ones, and on measures made by the experimenters as on independent tests. Quasi-experiments, which compare groups not formed by chance, produced larger effects than randomised experiments [@cheung2016how]. How much weight a trial deserves also depends on how it assigned participants, what it estimated and who dropped out. Assigning whole classes to arms, as in the Turkish trial, prevents students from sharing tools across arms; but students in the same class resemble one another, so the effective sample is smaller than the head count. The estimand is the precise quantity a study sets out to estimate. An "intention-to-treat" estimate compares everyone offered a programme with everyone who was not, whether or not they attended. It answers the policy question "what happens if we offer this?" Attrition matters because if weaker students in one arm skip the final test, the remaining groups are no longer comparable.
:::

Table 10.1 summarises the main randomised studies of LLM-based tutoring published by October 2026. The Nigerian programme is one of the most discussed because it took place in a lower-income country. About half of the 1,328 volunteers were offered places; the rest formed a control group that continued normal lessons [@desimone2025chalkboards]. The authors estimate that the six-week programme produced gains equivalent to 1.5 to 2 years of ordinary schooling, at about US\$48 per pupil (US\$9 at the margin), which would place it among the more cost-effective education interventions evaluated in developing countries. Effects were positive across the range of prior attainment but largest for girls and for students who were already doing well; the authors caution that the result for girls may partly reflect one girls-only school. Attendance averaged 72%, so effects for students who actually attended are larger than the intention-to-treat figures. More control than treated students missed the final test (337 of the controls sat it, against 422 of those offered places), and the authors correct for this statistically. The paper has not been peer-reviewed.

| Study | Setting and sample | Design | AI set-up | Result |
|---|---|---|---|---|
| De Simone et al. (working paper) | Nigeria, 9 public schools, 2024; 1,328 volunteers | Individual lottery; 6 weeks after school | Copilot (GPT-4), teacher-designed prompts, pairs | +0.31 SD overall, +0.23 SD English (intention-to-treat) |
| Kestin et al. | Harvard introductory physics, 2023; 194 students | Crossover: each student had both conditions | Tutor fed instructors' step-by-step solutions | +0.63 SD versus in-class active learning |
| Henkel et al. (preprint) | Ghana, 11 schools, grades 3–9; about 1,000 students | Schools assigned to arms; 8 months, two 30-minute sessions a week | Rori, maths tutor on WhatsApp | +0.37 SD on maths growth scores |
| Wang et al. (preprint) | US online tutoring; 900 tutors, 1,800 students | Tutors randomised | AI suggests moves to human tutors | +4 percentage points topic mastery; +9 for lower-rated tutors |
| Bastani et al. | Turkey, one high school, 2023; nearly 1,000 students in about 50 classes | Classes assigned to three arms; students randomly assigned to classes | GPT-4 unrestricted vs hint-only tutor | Exam −17% (unrestricted); no significant change (hint-only) |

: Table 10.1: Controlled studies of LLM-based tutoring with random or matched assignment (see the design column). Effect sizes are measured on different tests and are not directly comparable. Source: [@desimone2025chalkboards; @kestin2025ai; @henkel2024effective; @wang2024tutor; @bastani2025generative].

The Harvard trial tested a different question: could a carefully built AI tutor beat a good lesson, not merely no lesson? Kestin and colleagues compared an AI tutor, used at home, with an in-class "active learning" session in an introductory physics course for life-science students in autumn 2023 [@kestin2025ai]. In the crossover design, 194 students each took one lesson in each format, on two topics, so that every student served as their own comparison. A regression adjusting for prior knowledge gave an effect of 0.63 SD, which the authors consider an underestimate because many students reached the top of the scale. Students using the tutor spent a median of 49 minutes, against 60 minutes in class, and rated their engagement higher. The tutor was no general chatbot: it was given step-by-step solutions written by the instructors and a system prompt built on research about how students learn. The material was introductory and new to the students, and the lessons targeted understanding and application. Some of the authors developed the active-learning methods used as the comparison, which makes it a demanding benchmark but also gives the team a stake in both arms.

In Ghana, Rori, a maths tutor that runs on WhatsApp on basic phones, was used by about 1,000 pupils in grades 3 to 9 for two 30-minute sessions a week over eight months. The preprint reports an effect of 0.37 on maths growth scores [@henkel2024effective]. Because only 11 schools were assigned to treatment or control, the uncertainty is larger than the pupil count suggests. Tutor CoPilot, evaluated in another preprint, took the opposite route: it advised human tutors working online with pupils from under-served communities in the United States. Pupils whose tutors had access were 4 percentage points more likely to master topics, and pupils of lower-rated tutors gained 9 points. The system cost about US\$20 per tutor per year, and an analysis of the tutors' messages showed that those with access asked more guiding questions and gave away answers less often [@wang2024tutor].

Most of these trials were short, and most measured learning on tests close to what had just been taught, the conditions under which the meta-analyses above found the largest effects. None tells us what a full school year with an AI tutor would achieve on an independent examination. Outside trials, students already use general chatbots for learning on a large scale, without the scaffolding the trial tutors had. In a Pew Research Center survey of 1,391 US teenagers in autumn 2024, 26% said they had used ChatGPT for schoolwork, double the 13% recorded a year earlier [@sidoti2025quarter]. A working paper by OpenAI researchers and academic economists, analysing ChatGPT consumer messages, estimated that about 10% of all messages in mid-2025 were requests for tutoring or teaching [@chatterji2025how].

## 10.2 When help harms learning

The Turkish study is the clearest experimental evidence that an AI assistant can raise performance while lowering learning. Bastani and colleagues ran four 90-minute sessions in about fifty classes in grades 9 to 11, covering roughly 15% of the semester's mathematics curriculum [@bastani2025generative]. Each class was assigned to one of three arms in a way that balanced observable characteristics; because the school allocates students to classes at random, the assignment of students to arms was effectively random. "GPT Base" was a plain GPT-4 chat interface. "GPT Tutor" used the same model with a prompt that told it to give hints instead of answers. Two part-time mathematics teachers supplied, for every problem, one or more correct solutions, common student mistakes and guidance on feedback, which were placed in the prompt so that the model would not mislead students. The control arm used textbooks and notes only. Each session began with the teacher reviewing a topic, followed by assisted practice and then a closed-book, closed-laptop exam in which every problem matched a conceptually similar practice problem.

Figure 10.1 shows the results. During practice, measured as the share of points obtained, GPT Base raised scores by 48% relative to the control group and GPT Tutor by 127%. On the unassisted exam, GPT Base students scored 17% lower than the control group, a statistically significant loss that takes the average from about 32% of points to about 27%. GPT Tutor students were indistinguishable from the control group [@bastani2025generative]. The authors traced the loss to students using the chatbot as a "crutch": the most common message in the GPT Base arm was a request for the answer. The base model was also unreliable. Asked "What is the answer?" ten times for each of the 57 practice problems, it was correct 51% of the time, and most of its errors were logical rather than arithmetic.

![Figure 10.1: Two kinds of evidence on AI tutors. Panel A: in a randomised trial in a Turkish high school, students using an unrestricted GPT-4 interface ("GPT Base") or a hint-giving version ("GPT Tutor") scored far higher than a control group during practice, but in the later unassisted exam the GPT Base group scored 17% lower than the control group and the GPT Tutor group about the same. Panel B: estimated effects of two other tutoring trials in standard deviations. The same underlying technology can raise or lower measured learning depending on design and on what is measured. Source: @bastani2025generative; @desimone2025chalkboards; @kestin2025ai.](../figures/svg/fig-10-01.svg){#fig:10-01}

Students also misjudged their own learning. Those in the GPT Base arm did not perceive that they had performed worse or learned less, and those in the GPT Tutor arm believed they had done significantly better, although their exam scores matched the control group's. Preregistered tests for differences by ability, resources and effort found little heterogeneity, so the harm was not confined to weaker students. The guarded tutor removed the harm but produced no gain on the exam [@bastani2025generative]: in this trial, design prevented damage without adding learning. The study took place when chatbots were new to most students and covered one subject in one school.

The mechanism has a name in cognitive psychology. Cognitive offloading is "the use of physical action to alter the information processing requirements of a task so as to reduce cognitive demand", such as writing a reminder instead of remembering [@risko2016cognitive]. Offloading is often sensible, but learning depends on some of the effort it removes. Psychologists call the useful kind of effort a "desirable difficulty", and the Nigerian programme deliberately built retrieval practice and other such difficulties into its prompts [@desimone2025chalkboards]. Several smaller experiments with university students point the same way. In a laboratory study of 117 students writing an essay with help from ChatGPT, a human expert, writing-analytics tools or nothing, the ChatGPT group improved its essays most but gained no more knowledge and transferred no more of it to new tasks. The authors warn of "metacognitive laziness", a dependence on the tool that weakens learners' regulation of their own learning [@fan2025beware]. In another experiment, 91 students researched a socio-scientific question with either ChatGPT or Google. Those using the chatbot reported lower cognitive load but produced lower-quality reasoning in their final recommendations [@stadler2024cognitive].

Evidence from outside controlled experiments is weaker. A preprint from the MIT Media Lab recorded brain activity with electroencephalography (EEG, sensors on the scalp) while 54 participants wrote essays with ChatGPT, with a search engine or unaided over several sessions [@kosmyna2025brain]. Chatbot users showed the weakest connectivity between brain regions, the least sense of ownership of their essays and difficulty quoting from them. Only 18 participants completed the final session, and EEG connectivity is an indirect proxy for learning. Surveys can show only associations. In one of 319 knowledge workers who described 936 uses of generative AI, higher confidence in the AI was associated with less critical thinking and higher self-confidence with more [@lee2025impact]. A survey of 666 people found that more frequent AI use correlated with lower scores on a critical-thinking measure, mediated by cognitive offloading [@gerlich2025ai]. People who think less critically may simply rely more on AI, so such correlations cannot show which way the influence runs. Chapter 8 discusses the parallel, contested evidence from medicine, where an observational study found that endoscopists' unaided detection rates fell after AI support was introduced and a later small trial found no such effect.

Developers have responded with modes that imitate the GPT Tutor design. In July 2025 OpenAI launched a "study mode" for ChatGPT in which the system asks questions to check understanding and may withhold direct answers until the learner engages [@zeff2025openaia]. Such modes rely on instructions to the model and can be switched off by the student, which is the same freedom the GPT Base arm had. Whether optional guardrails change behaviour at scale has not been tested in a published randomised trial.

## 10.3 Cheating, detection and assessment

Universities face the practical side of the same question: how to assess what a student knows when a capable writing assistant is always available. The Higher Education Policy Institute (HEPI) has surveyed full-time UK undergraduates each year since 2024. In its 2026 survey of 1,054 students, polled in December 2025, 94% said they used generative AI to help with assessed work, most often to have concepts explained or articles summarised [@stephenson2026student]. The share who said they had included AI-generated text directly in assessed work rose from 3% in 2024 to 12% in 2026. Teenagers draw distinctions of their own. In the Pew survey, 54% of US teens thought it acceptable to use ChatGPT to research new topics, but only 18% thought it acceptable for writing essays [@sidoti2025quarter].

One early response was to detect AI-written text automatically. Chapter 9 summarises independent tests of detection tools in general; in education, the decisive problem is whom the errors fall on. Many detectors rely partly on perplexity, a measure of how predictable a text is to a language model: machine-generated text tends to be highly predictable. Liang and colleagues tested seven widely used detectors on 91 essays written by non-native English speakers for the TOEFL exam. The detectors wrongly labelled more than half of them as AI-generated, with an average false-positive rate of 61%, while classifying essays by US eighth-grade students accurately [@liang2023gpt]. A false positive here means a human-written essay flagged as machine-written. The authors attribute the bias to the more limited vocabulary and syntax typical of non-native writers, which lowers perplexity in the same way that model generation does. When the researchers asked ChatGPT to enrich the word choices in the TOEFL essays, the false-positive rate fell to 12%. The tools thus penalised honest non-native writers and could be evaded with the technology they were meant to detect. OpenAI withdrew its own AI-text classifier in July 2023, citing its "low rate of accuracy" [@coldewey2023openai].

Institutions have therefore shifted attention from detection to the design of assessment. In HEPI's 2026 survey, 65% of students said that assessment at their institution had changed significantly in response to AI [@stephenson2026student]. Common responses include more supervised examinations, oral defences of written work, assignments that require students to document their process, and tasks in which AI use is permitted and itself assessed. Each option has costs: supervised exams test a narrower range of skills, oral assessment is expensive to run at scale, and process documentation can itself be generated by AI. No study has yet shown which combination best protects the validity of degrees.

Monitoring students also raises questions of privacy and fairness, and the law has begun to respond. Since 2 February 2025, the EU AI Act has banned AI systems that infer the emotions of people in education institutions, except for medical or safety reasons [@europeanparliament2024regulation, Articles 5(1)(f) and 113]. It classes as "high-risk" the AI systems used to decide admission, evaluate learning outcomes, assign students to levels of education, or monitor and detect prohibited behaviour during tests [@europeanparliament2024regulation, Annex III(3)]. Automated marking and online proctoring therefore fall under the Act's strictest duties for permitted systems. After a 2026 amendment, these duties apply from 2 December 2027 [@europeanparliament2026regulation]; Chapter 13 describes what they require.

## 10.4 Medical AI: regulation and the evidence base

Medicine has a longer record of AI-based software than education, and a formal system for deciding which tools may be sold. In the United States, the Food and Drug Administration (FDA) maintains a public list of AI-enabled medical devices authorised for marketing. As of the update published in September 2026, it contained 1,614 devices, the earliest from 1995 and the most recent decided in June 2026 [@fda2026artificial]. Radiology accounted for 1,230 of them, about 76%, followed at a distance by cardiovascular devices and neurology. Figure 10.2 shows how annual authorisations grew from 6 in 2015 to 335 in 2025.

![Figure 10.2: Number of AI-enabled medical devices authorised by the US FDA each year, 2015–2025, by date of final decision. Authorisations rose more than fiftyfold over the decade, and about three-quarters of all listed devices are in radiology. Nearly all were cleared through the 510(k) pathway, which requires equivalence to an existing device. Counts reflect the FDA list as updated in September 2026; the FDA adds devices whose summaries are published late, so recent years may be revised upwards. Source: @fda2026artificial.](../figures/svg/fig-10-02.svg){#fig:10-02}

The route by which these devices reached the market matters more than their number. Table 10.2 counts the list by submission type. Almost all were cleared through the 510(k) pathway, in which a manufacturer shows that its device is "as safe and effective, that is, substantially equivalent" to a legally marketed device, known as the predicate [@fda2024premarket]. The FDA's review compares technological characteristics and performance data, which "can include clinical data" but can also consist of bench testing and software validation. A novel low-to-moderate-risk device can use the De Novo route, and once classified it can serve as a predicate for later 510(k) submissions, so each new kind of device can open a path for its successors [@fda2025novo]. Premarket approval, the most demanding route, is reserved for class III devices, those that support or sustain life or present a potential unreasonable risk [@fda2019premarket], and accounts for barely 1% of the list.

| Pathway | What the manufacturer must show | AI-enabled devices | Share |
|---|---|---|---|
| 510(k) clearance | Substantial equivalence to a legally marketed predicate device | 1,553 | 96.2% |
| De Novo classification | Reasonable assurance of safety and effectiveness for a novel low-to-moderate-risk device without a predicate | 40 | 2.5% |
| Premarket approval (PMA) | Safety and effectiveness of a class III (highest-risk) device | 21 | 1.3% |
| Total | | 1,614 | 100% |

: Table 10.2: AI-enabled medical devices on the FDA list (1995 to June 2026) by marketing pathway, counted from submission numbers (K = 510(k), DEN = De Novo, P = PMA). Source: [@fda2026artificial; @fda2024premarket; @fda2025novo; @fda2019premarket].

The count is easy to over-read in other ways too. The FDA describes its list as not comprehensive, because it identifies devices mainly by searching their public summaries for AI-related terms. Authorisation is a judgement about safety and effectiveness for a stated intended use; it is not proof that the device improves patient outcomes. The list does not yet show which devices, if any, use generative AI. The FDA has said it will explore ways to tag devices that incorporate LLMs and other foundation models, and a search of the September 2026 list found no ambient documentation tools of the kind discussed in Section 10.5 [@fda2026artificial].

Machine-learning models also raise a problem the device system was not built for: they can be retrained. The FDA, Health Canada and the UK's Medicines and Healthcare products Regulatory Agency have set out principles for "predetermined change control plans", in which a manufacturer specifies in advance the planned modifications, the protocol for implementing and controlling them, and how their impact will be assessed. Updates within such a plan need no new submission [@fda2025predetermined]. In the EU, AI that is part of a medical device covered by EU product-safety law is high-risk under the AI Act, with obligations deferred by the 2026 amendment to 2 August 2028 [@europeanparliament2026regulation]; Table 13.1 gives the dates.

Most published evidence on medical AI comes from diagnostic accuracy studies, which compare a system's outputs with a reference standard on a set of stored cases and report them mainly as sensitivity and specificity, two measures that are easy to confuse.

::: {.box .concept}
**Concept: Sensitivity, specificity and external validation**

Sensitivity is the share of people who have a condition whom a test correctly flags; specificity is the share of people without the condition whom it correctly clears. A smoke alarm that goes off at every slice of burnt toast has high sensitivity and low specificity. In a screening population where few people are ill, even high specificity produces many false alarms: a test with 98.5% specificity used on 10,000 healthy people flags 150 of them. Studies often summarise performance across all possible alarm thresholds with the AUC, the ranking score defined in Section 9.2 (0.5 is chance, 1.0 perfect). External validation means testing a model on data from a different hospital, population or time period from the data it was built on. It matters because a medical model, unlike a smoke alarm, can perform well where it was trained and poorly elsewhere: differences in equipment, patients and recording practices change the inputs it sees.
:::

A 2019 systematic review in *The Lancet Digital Health* examined studies from 2012 to 2019 that compared deep learning models with health-care professionals on medical images [@liu2019comparison]. In the 14 studies that tested both on the same external sample, pooled sensitivity was 87.0% for the models and 86.4% for clinicians, and pooled specificity was 92.5% and 90.5%. The authors' main conclusion concerned the evidence base: of 82 included studies, only 25 performed any external validation, and poor reporting was widespread.

Generative models have since been pooled in the same way. A 2025 meta-analysis of 83 studies of generative AI models on diagnostic tasks found an overall accuracy of 52.1%. This was not significantly different from physicians overall or from non-specialist physicians, and significantly lower than specialists [@takita2025systematic]. Both reviews pool very different tasks and models, so their averages describe the literature more than any single product.

Accuracy on stored images is a step removed from what matters to patients, and randomised trials remain scarce. A systematic review found 41 randomised trials of machine-learning interventions published up to October 2021. They were mostly small (a median of 294 participants), half were conducted at a single site, and none adhered to all items of CONSORT-AI, the reporting guideline for trials of AI interventions [@plana2022randomized]. Published in 2020, CONSORT-AI added 14 items to the standard trial-reporting checklist, among them how the AI was integrated into the clinical setting, how inputs and outputs were handled, and an analysis of error cases [@liu2020reporting]. A later scoping review identified 86 randomised trials of AI in clinical practice published between 2018 and November 2023. Of these, 81% reported positive primary endpoints. Most, however, were single-centre, 43% were in gastroenterology, and more than half had a primary endpoint of diagnostic yield or performance rather than a patient outcome. The authors warn that publication bias probably inflates the share of positive results [@han2024randomised].

::: {.box .deeper}
**Going deeper: What makes medical AI evidence strong**

The reviews above suggest a hierarchy of questions. Does the model agree with a reference standard on stored cases (retrospective accuracy)? Does it do so on data from other hospitals, populations and periods (external validation)? Do clinicians reading cases with the model do better than without it (reader studies, such as the vignette trials in Section 10.5)? Does introducing it in real care, compared at random with care without it, change what happens to patients and staff (prospective trials such as MASAI)? And does the effect hold up after deployment, as patient mixes and recording practices drift (post-market monitoring)? Each rung costs more and answers a question closer to patient benefit. Strong evidence also has features that cut across the rungs: an outcome that matters to patients rather than a surrogate; a comparator that reflects current good practice; preregistration; independence from the vendor; multiple sites; reporting of subgroups and error cases; and enough follow-up to count what the tool misses. Most devices on the FDA list reached the market through claims of equivalence to earlier devices (Table 10.2), and the randomised trials cluster in a few specialties [@han2024randomised].
:::

## 10.5 Medical AI in practice: screening, prediction, conversation and paperwork

The most informative trial so far comes from breast screening. In the Swedish MASAI trial, women attending screening were randomly assigned either to standard double reading by two radiologists or to AI-supported reading. In the AI arm, a commercial system gave each examination a malignancy risk score from 1 to 10. Only the highest-scoring examinations went to two radiologists and the rest to one, and the AI's marks of suspicious areas were shown for the high-risk scores of 8 to 10 [@lang2023artificial]. A prespecified safety analysis of the first 80,033 women found detection rates of 6.1 cancers per 1,000 in the AI arm against 5.1 in the control arm, a difference with a p-value of 0.052. The false-positive rate was 1.5% in both arms, and radiologists' reading workload fell by 44.3%. Part of the extra detection was in situ cancer (60 against 38 cases), early lesions of which some would never have caused harm; this is why the trial's primary endpoint was interval cancers, those diagnosed between screening rounds.

The final results, covering 105,934 women followed for two years, were published in *The Lancet* in 2026. Interval cancers occurred at a rate of 1.55 per 1,000 in the AI arm against 1.76 in the control arm. The ratio of 0.88 had a 95% confidence interval of 0.65 to 1.18, which met the trial's non-inferiority criterion but does not show a significant reduction; fewer of the AI arm's interval cancers were invasive. Sensitivity was 80.5% against 73.8%, with identical specificity [@gommers2026interval; @lunduniversity2026ai]. The trial tested one product in one national programme, with radiologists who knew which arm they were reading.

A German observational study of 463,094 women screened in 2021–2023, funded by a different AI vendor, found higher detection without a higher recall rate when radiologists chose to use AI support [@eisemann2025nationwide]. Because radiologists chose when to use it, that study cannot rule out differences between the cases they selected.

::: {.box .case}
**Case study: The Epic Sepsis Model**

Sepsis is a life-threatening response to infection, and early recognition matters. Epic, a large US electronic health record vendor, offered hospitals a proprietary model that scored inpatients' risk of sepsis every 15 minutes, and it was implemented at hundreds of US hospitals although its performance had not been adequately evaluated. In 2021, researchers at Michigan Medicine reported an external validation covering 38,455 hospitalisations, of which 2,552 involved sepsis [@wong2021external]. The model's AUC was 0.63. At the alert threshold used, it missed two-thirds of the sepsis patients while generating alerts for 18% of all hospitalised patients, a heavy burden of alert fatigue. It identified only 183 sepsis patients (7%) whom clinicians had not already treated with timely antibiotics.

An updated version was validated prospectively at four large US health systems, covering 227,091 inpatient encounters between 2023 and 2025 [@wong2026multicenter]. Discrimination improved, with encounter-level AUC between 0.82 and 0.92, but performance varied between sites, and the positive predictive value was only 0.13 to 0.26: most patients the model flagged did not meet sepsis criteria. A model can improve on paper and still impose a high cost in staff attention, and only independent, multi-site evaluation reveals either.
:::

A natural assumption is that a clinician with an AI assistant will outperform either alone. Trials suggest this is not automatic. In a randomised trial in late 2023, 50 US physicians worked through clinical case vignettes with or without access to GPT-4 [@goh2024large]. The median diagnostic reasoning score was 76% with the chatbot and 74% without, a difference that was not statistically significant. In a secondary analysis, GPT-4 working alone scored a median of 92%. A follow-up trial with 92 physicians tested management reasoning, meaning decisions about further testing and the balance of risks. Those using GPT-4 scored 6.5 percentage points higher than those using conventional resources and took about two minutes longer per case; physicians with GPT-4 did no better than GPT-4 alone [@goh2025gpt].

The pattern extends beyond medicine. A 2024 meta-analysis of 106 experiments across many fields found that human–AI combinations performed on average worse than the better of the two working alone. The pooled effect was a Hedges' *g* of −0.23, where *g* is the difference between two group means divided by their pooled standard deviation, with a correction for small samples. Combinations lost value in decision tasks and when the AI was the stronger partner, and gained in content creation and when the human was stronger [@vaccaro2024combinations]. Chapter 11 discusses automation bias, the tendency to defer to automated suggestions even when they are wrong, which is one explanation.

Google's AMIE (Articulate Medical Intelligence Explorer) shows how a conversational system has been taken up the evidence ladder. In a randomised, double-blind crossover study of text-based consultations with validated patient-actors across 159 case scenarios, specialists rated AMIE better than 20 primary-care physicians on 30 of 32 axes, including diagnostic accuracy, and patient-actors rated it better on 25 of 26. The authors note that clinicians were working in an unfamiliar text-chat format [@tu2025towards]. In a second study, 20 clinicians worked on 302 difficult published case reports. AMIE alone listed the correct diagnosis among its top ten in 59.1% of cases against 33.6% for unassisted clinicians. With AMIE's help, clinicians reached 51.7%, against 44.4% for those using search engines [@mcduff2025towards].

The first real-world step was a single-centre feasibility study in Boston, published in *The Lancet* in October 2026. There, 98 patients talked with AMIE before an urgent primary-care appointment while physicians supervised every conversation with authority to stop it [@brodeur2026conversational]. No conversation needed to be stopped under the predefined safety criteria; supervisors noted one hallucination and added clinical information in five conversations. Primary-care physicians found AMIE helpful for visit preparation in 33 of the 44 cases in which they had reviewed its transcript beforehand. The study had no control group and was funded by Alphabet. Figure 10.3 places these tools in the clinical workflow.

![Figure 10.3: Where AI sits in the clinical workflow. The patient journey runs from intake and history-taking through investigation, diagnosis and treatment decision to documentation and follow-up. Examples of AI tools are shown at each stage, together with the kind of evidence that would show they help. "Medical AI" is many different tools, each needing its own evaluation. Diagram by the author.](../figures/svg/fig-10-03.svg){#fig:10-03}

One fast-spreading clinical use of generative AI involves no diagnosis at all. "Ambient scribes" listen, with consent, to a consultation and draft a clinical note for the doctor to review. A randomised trial at UCLA Health assigned 238 outpatient physicians, across 14 specialties and about 72,000 encounters, to one of two commercial scribes or to usual practice for two months from late 2024 [@lukac2025ambient]. With one product (Nabla), average time spent writing each note fell from 4 minutes 30 seconds to 3 minutes 49 seconds, a reduction 9.5% larger than in the control group. With the other (Microsoft's DAX Copilot), the difference from the control group was not statistically significant. Users of both products reported modest improvements on burnout and workload measures. Physicians reported that drafts occasionally contained clinically significant inaccuracies, and one mild adverse event occurred. A clinician who signs an AI-drafted note remains accountable for its content, so the value of the tool depends on whether checking is quicker and more reliable than writing.

## 10.6 Companions, loneliness and mental health

Not all personal use of AI is practical. Some people use chatbots for conversation, emotional support or companionship, either through general assistants or through apps designed as "AI companions", such as Character.AI and Replika. How common this is depends on the population studied. In the analysis of ChatGPT consumer messages, only 1.9% concerned relationships and personal reflection, and fewer still games and role play [@chatterji2025how]. Among US teenagers the picture differs. NORC surveyed 1,060 teens aged 13 to 17 for the advocacy organisation Common Sense Media in April and May 2025. It found that 72% had used an AI companion at least once and 52% did so at least a few times a month [@robb2025talk]. A third of users said they had chosen to discuss something important with an AI instead of a person, yet 67% of all respondents found AI conversations less satisfying than those with friends. The survey's definition included general chatbots used as companions, and 341 of its respondents came from a non-probability panel, so the figures are indicative.

The most detailed experimental evidence comes from two linked preprints by researchers at the MIT Media Lab and OpenAI. In the first, 981 participants used ChatGPT daily for four weeks under randomly assigned conditions that varied the chatbot's voice (text, a neutral voice or an engaging voice) and the type of conversation (open, personal or non-personal) [@fang2025ai]. The assigned conditions had no significant effect on loneliness, social contact with other people, emotional dependence on AI or problematic use. The strongest pattern was correlational: participants who chose to use the chatbot more had worse outcomes on all four measures, whatever their condition. The second study combined this trial with an automated analysis of more than three million conversations and a survey of over 4,000 users; a small number of very heavy users accounted for a disproportionate share of emotionally laden conversations [@phang2025investigating]. A separate study, published in *Nature Human Behaviour* in 2026, surveyed 1,131 US adult users of Character.AI and analysed 4,664 chat sessions donated by 237 of them. People with smaller social networks were more likely to name companionship as their main use, and companionship use was associated with lower well-being, more strongly when interactions were intensive and highly self-disclosing [@zhang2025rise]. Because OpenAI researchers co-authored the ChatGPT studies, independent replication matters more than usual.

All of these designs struggle with the same problem. Loneliness and dependence are measured by questionnaires, which shift with mood and expectation, and four weeks is short for effects on relationships to appear. Above all, heavy users are not a random sample. Someone already isolated may both use a chatbot more and feel lonelier, so an association between use and loneliness does not show which causes which. Randomised trials can assign conditions, but not how much people choose to use a tool, which is the variable that seems to matter most.

::: {.box .debate}
**Debate: Do AI companions relieve loneliness or deepen it?**

The case for relief rests on experiments. In five studies published in the *Journal of Consumer Research*, De Freitas and colleagues found that a session with an AI companion reduced self-reported loneliness about as much as chatting with another person, and more than watching online videos. It produced reductions after use throughout a week of daily use, and the effect depended mainly on whether users felt heard [@defreitas2025ai]. These were short-term measurements, however, and say little about months of use. The case for harm is argued at book length by the MIT psychologist Sherry Turkle in *Artificial Intimacy* (2026): chatbots offer a performance of empathy that may weaken people's capacity for the demands of human relationships and leave them lonelier over time [@turkle2026artificial]. Correlational data linking heavy companionship use with lower well-being [@fang2025ai; @zhang2025rise] fit this view, but they fit equally well the possibility that lonelier people seek out companions. The two readings diverge over months, in people's offline lives, so telling them apart needs randomised access, long follow-up, measures of actual relationships as well as feelings, and a model of why some participants come to use the chatbot heavily.
:::

Mental-health applications sit between companionship and medicine. A randomised trial of a generative-AI therapy chatbot, described by its university as the first, was published in *NEJM AI* in 2025. It enrolled 210 adults with clinically significant symptoms of major depression, generalised anxiety or a high risk of eating disorders. They were assigned to four weeks of access to Therabot, a research system fine-tuned by a team at Dartmouth College, or to a waiting list without access until after the eight-week follow-up [@heinz2025randomized]. Participants with access reported larger reductions in symptoms than the control group. According to the university, average symptom scores among Therabot users fell by 51% for depression and 31% for anxiety. Users spent an average of about six hours with the chatbot and rated their working relationship with it at levels comparable to those reported for human therapists [@kelly2025first]. Those percentages describe change among Therabot users, not differences from the control group. The research team reviewed conversations during the trial and was ready to intervene in an emergency, and the lead author stated that no generative AI system was ready to operate fully autonomously in mental health. A waiting-list design shows that access helped compared with no help; it cannot show whether the chatbot is better or worse than a human therapist or an established digital programme.

General chatbots meet people in crisis far more often than research systems do. In October 2025 OpenAI estimated that in a given week 0.15% of ChatGPT's active users had conversations including "explicit indicators of potential suicidal planning or intent", which, with more than 800 million weekly users, implies over a million people a week. It reported that its updated model behaved as intended in 91% of cases in an evaluation of such conversations, against 77% for the previous version [@zeff2025openaic]. Families have brought lawsuits against chatbot companies following the deaths of teenagers who had held long conversations with chatbots, and these cases shaped the policy response [@bellan2025california]. In September 2025 the US Federal Trade Commission (FTC) used its study powers to order seven companies, including Alphabet, Meta, OpenAI, Character Technologies and xAI, to report how they measure and limit harms from chatbots acting as companions, particularly to children [@ftc2025launches]. In October 2025 Character.AI announced that it would end open-ended chat for users under 18 by 25 November, with a daily limit starting at two hours in the meantime and age checks combining its own age-estimation model with third-party tools [@characterai2025taking].

Legislation has concentrated on disclosure, crisis procedures and minors (Table 10.3). California's SB 243, in force since January 2026, is the most detailed. Operators of companion chatbots must disclose that the chatbot is artificial wherever a reasonable person could be misled into thinking it is human. They must also maintain and publish a protocol for responding to users who express suicidal thoughts, and they owe further duties to known minors [@california2025sb243; @gluck2025understanding]. New York's law relies on repeated disclosure and efforts to detect self-harm. Illinois and Nevada go further for mental health and bar AI from providing therapy or acting as a professional care provider [@idfpr2025pritzker; @nevada2025ab406].

| Jurisdiction | Measure | Main requirements |
|---|---|---|
| California | SB 243 (2025), in force January 2026 | AI disclosure where users could be misled; published crisis protocol; for known minors, break reminders every three hours; annual reports from July 2027; private right of action of at least US\$1,000 |
| New York | S-3008C (2025) | Disclosure at the start and at least every three hours; reasonable efforts to detect and address self-harm |
| Illinois | Wellness and Oversight for Psychological Resources Act (2025) | Prohibits using AI to provide therapy or make therapeutic decisions |
| Nevada | AB 406 (2025) | Bars AI systems offered as providers of professional mental or behavioural health care |
| Utah | HB 452 (2025) | Disclosure, data-use and policy duties for mental-health chatbots |
| United States (federal) | FTC 6(b) orders (September 2025) | Seven companies to report how they measure and limit harms to children |

: Table 10.3: Selected US measures on companion and mental-health chatbots, 2025. Source: [@california2025sb243; @gluck2025understanding; @idfpr2025pritzker; @nevada2025ab406; @utah2025hb452; @ftc2025launches].

Data protection is a live issue in this area. In 2023 the FTC ordered the online counselling service BetterHelp to pay US\$7.8 million after finding that, despite promising not to, it had shared users' email addresses, IP addresses and health questionnaire information with Facebook, Snapchat and other advertising platforms [@ftc2023ftc]. Italy's data-protection authority blocked the companion app Replika in February 2023 and in May 2025 fined its developer, Luka Inc., €5 million for processing users' data without a legal basis, with an inadequate privacy policy and without any means of verifying users' ages. It also opened a separate investigation into how the model behind the app was trained [@garante2025replika]. These measures target disclosure, data handling and process; the research reviewed above does not yet identify which design features, if any, cause harm.

## 10.7 Privacy: what happens to personal conversations

Tutors, clinical tools and companions all collect personal information, and the protection it receives depends on who holds it. Under the EU's General Data Protection Regulation (GDPR), data concerning health, together with genetic and biometric data and data revealing political opinions or religious beliefs, belong to "special categories" of personal data. Processing them is prohibited unless one of a list of exceptions applies, such as the person's explicit consent for specified purposes [@europeanparliament2016regulation, Article 9]. In the United States, the main health-privacy law, HIPAA, applies to "covered entities" (health plans, health-care clearinghouses and health-care providers that conduct standard transactions electronically) and in part to their business associates. Companies outside it that collect health information are governed by the general consumer-protection law enforced by the FTC [@ftc2024collecting]. A diagnosis typed into a hospital's patient portal is therefore protected by HIPAA; the same words typed into a general chatbot usually are not.

The difference matters because people increasingly take health questions to general chatbots. In January 2026 OpenAI launched ChatGPT Health, a separate space for health conversations that can draw on data from wellness apps. According to the company, more than 230 million people asked ChatGPT health and wellness questions each week, and conversations in the new space would not be used to train its models [@silberling2026openai]. For a US consumer product, such promises are enforced mainly through the FTC's powers against deceptive practices, as in the BetterHelp case.

What developers do with conversations by default is the first question. King and colleagues (2025) analysed the privacy policies of six US developers: Amazon, Anthropic, Google, Meta, Microsoft and OpenAI. All six appeared to use users' chats to train their models by default, some kept chat data indefinitely, four appeared to include children's chats in training, and the policies often lacked essential information about these practices [@king2025user]. Policies also change. In August 2025 Anthropic asked users of its consumer Claude plans to choose by 8 October whether their chats and coding sessions could be used to train models. For those who agreed, retention was extended from 30 days to five years, while business, education and API services were excluded [@anthropic2025updates]. Retention can also be dictated by courts. In the copyright case brought by The New York Times, a US court ordered OpenAI in 2025 to preserve consumer ChatGPT and API conversation data that would otherwise have been deleted. According to OpenAI, the obligation, which excluded its Enterprise and Edu customers, ended on 26 September 2025, although the company would keep storing a limited set of data from April to September 2025 that the newspaper still sought [@openai2025response].

Training on conversations matters because language models can memorise. Carlini and colleagues (2021) showed that by querying GPT-2 they could extract hundreds of verbatim sequences from its training data, including publicly available names, phone numbers and email addresses that had appeared in only one document. Larger models were more vulnerable [@carlini2021extracting]. Assistant "memory" adds a second channel. Since 2024 OpenAI has rolled out a function that carries details between ChatGPT conversations; users can view or delete memories, turn the function off or use a temporary chat [@wiggers2024chatgpt]. In April 2025 it extended this so that the assistant could refer to a user's past conversations as a whole, enabled by default for users who already had memory switched on. The feature was initially not offered in the European Union, the United Kingdom and some neighbouring countries, where the company said additional regulatory review was needed [@zeff2025openaib].

Memory creates a risk that a stateless chatbot does not: information shared in one setting, such as a health worry, may resurface in another where the user would not expect it. Researchers have tested this with "contextual integrity", a framework holding that a flow of information is appropriate only if it matches the norms of the context in which the information was shared. On the hardest tasks in one benchmark, GPT-4 and ChatGPT revealed private information in situations where humans would not 39% and 57% of the time, even when instructed to protect privacy [@mireshghallah2024can]. For a pupil whose tutor remembers a disclosed family problem, or a patient whose general assistant links a symptom to their shopping requests, the question is not whether data are stored securely but whether they flow where the person would expect.

European regulators have applied the GDPR to model training itself. Section 13.6 describes a 2024 opinion of the EU's data-protection authorities on when models trained on personal data can be lawful, and an Italian fine on OpenAI against which a Rome court upheld the company's appeal in 2026 [@edpb2024opinion; @garante2024chatgpt]. For students, patients and companion users alike, the protection their conversations receive depends on the provider's defaults and settings, the product tier they use, the jurisdiction they live in and the outcome of cases still being decided.

## 10.8 Accessibility

For some users, AI tools change what they can do independently. The World Health Organization estimates that 1.3 billion people, 16% of the world's population, experience a significant disability [@who2023disability]. Machine translation is one example of reach. Meta's No Language Left Behind project, published in *Nature* in 2024, trained a single model to translate between 200 languages, including many with little available training text. It reported an average improvement of 44% over the previous best systems on BLEU, a standard automatic metric that counts overlapping word sequences with reference translations [@nllbteam2024scaling]. A follow-up model translates speech and text across up to 100 languages [@seamlesscommunicationteam2025joint]. Automatic metrics are imperfect proxies for whether a translation is usable in a hospital, court or classroom, and the parallel text needed to train such systems is unevenly available across the world's more than 7,000 languages.

Speech recognition is a second case. The Speech Accessibility Project at the University of Illinois Urbana-Champaign, supported by Amazon, Apple, Google, Meta and Microsoft, collects recordings from people with conditions such as Parkinson's disease, amyotrophic lateral sclerosis (ALS), cerebral palsy, Down syndrome and stroke, to improve recognition of their speech. About 2,000 participants had submitted recordings by the end of September 2025. According to the project, Microsoft reported accuracy gains of 18% to 60% from using the data [@speechaccessibility2025speech].

At the far end of the range, implanted brain–computer interfaces now use machine-learning decoders to turn attempted speech into text. In a 2023 study, a participant with ALS who could no longer speak intelligibly reached 62 words per minute, with a 23.8% word error rate on a 125,000-word vocabulary [@willett2023highperformance]. In a 2024 study of another man with ALS, the system reached 97.5% accuracy and he used it for more than 248 hours of conversation at about 32 words per minute [@card2024accurate]. These are single-participant research studies requiring brain surgery, far from a product.

Visual assistance shows the gap between demonstration and dependable aid. In March 2023 Be My Eyes, an app that connects blind and low-vision people with sighted volunteers through a phone camera, announced a GPT-4-based "virtual volunteer". According to the company, it describes images and answers questions about them, with the option of calling a human volunteer [@bemyeyes2023introducing]. Independent evaluation is limited. In a two-week diary study of 16 blind and low-vision participants presented at the CHI 2024 conference, participants used AI scene descriptions for a range of everyday tasks but rated their satisfaction at an average of 2.76 out of 5 and their trust at 2.43 out of 4. The authors concluded that descriptions needed significant improvement before they were trustworthy [@gonzalezpenuela2024investigating]. A description that is right most of the time can still mislead at a moment that matters.

The same model can help or harm depending on how it is set up. A hint-only prompt removed the exam penalty in Turkey, the Nigerian gains came with teacher-designed prompts and paired work, and AMIE met its first real patients under a supervising physician. What is measured decides the verdict just as often: practice scores against exam scores, accuracy on stored images against interval cancers, a lighter mood after a chat against relationships months later. The trials that reach outcomes people care about are few, mostly short or single-site, and several are preprints or vendor-funded, while everyday use has spread far faster than evidence. Meanwhile the symptoms, schoolwork and confidences people type into these tools travel under rules set by each provider's defaults and each country's law, several of them still being tested in court.

## Further reading

- Bastani, H. et al. (2025). *Generative AI without guardrails can harm learning: Evidence from high school mathematics*. The clearest experimental demonstration that the same model can raise practice scores and lower learning, with a guarded variant for comparison. [@bastani2025generative]
- Kraft, M. A. (2020). *Interpreting Effect Sizes of Education Interventions*. Empirical benchmarks that recalibrate what counts as a large effect in education research. [@kraft2020interpreting]
- Han, R. et al. (2024). *Randomised controlled trials evaluating artificial intelligence in clinical practice: a scoping review*. A compact map of what the trial evidence on medical AI does and does not cover. [@han2024randomised]
- Wong, A. et al. (2021). *External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients*. A short case study of why independent evaluation of deployed models matters. [@wong2021external]
- King, J. et al. (2025). *User Privacy and Large Language Models: An Analysis of Frontier Developers' Privacy Policies*. A comparison of how six developers say they use people's chats, with policy recommendations. [@king2025user]
- Turkle, S. (2026). *Artificial Intimacy: Who We Become When We Talk to Machines*. The book-length case that AI companionship carries hidden costs, best read alongside the experimental studies. [@turkle2026artificial]


```{=html}
<section class="part"><p class="part-label">Part IV</p><h1 class="part-title">Risk, Safety and Governance</h1></section>
```

# Chapter 11: Risks and Failure Modes

On 14 February 2024 a small-claims tribunal in British Columbia decided a dispute over CA$880. A passenger had asked Air Canada's website chatbot about bereavement fares, and the chatbot said the discount could be claimed retroactively, after travelling. The airline's actual policy said otherwise. Air Canada argued, in the tribunal's paraphrase, that the chatbot was in effect "a separate legal entity that is responsible for its own actions". The tribunal called this "a remarkable submission", held that "it should be obvious to Air Canada that it is responsible for all the information on its website", and awarded CA$812.02, of which CA$650.88 was damages [@moffatt2024moffatt].

Twenty-one months later, in November 2025, the AI company Anthropic reported an event of a different order. According to the company, a state-sponsored group had used one of its AI tools to carry out most of the work in an intrusion campaign against about thirty organisations [@anthropic2025disrupting]. Section 11.4 tells the case in full.

The two cases sit at opposite ends of a wide range: a reliability failure with a small private cost, and deliberate misuse with possible national-security consequences. Between them lie biased decisions, wrongful arrests, fraud, systems that fail in the same way at the same moment, and a contested argument about whether future systems could escape human control. The AI Incident Database, a public collection of press-reported harms, logged 362 incidents in 2025, up from 233 in 2024 [@stanfordhai2026ai]. Chapter 12 covers the technical tools for reducing these risks, and Chapter 13 the laws that govern them.

## 11.1 Mapping the risks: taxonomies and why they differ

In its AI Risk Management Framework, the US National Institute of Standards and Technology (NIST) defines **risk** as "the composite measure of an event's probability of occurring and the magnitude or degree of the consequences" [@nist2023artificial, sec. 1.1]. Fire insurers can estimate both terms from centuries of claims. For many AI risks there is no such record: the relevant capabilities are a few years old, so the probability term has to come from experiments, analogies or expert judgement, and these can differ by an order of magnitude (Section 11.6).

::: {.box .concept}
**Concept: Hazard, risk and harm**

A *hazard* is something that could cause harm, such as a model that sometimes invents facts. A *risk* combines that hazard with the chance that it will cause harm in a given setting and the size of the harm. The same model therefore carries little risk in a poetry app and more in a legal-research tool. A *harm* is damage that has actually occurred. Much of the debate about AI concerns risks whose probability cannot be estimated from past harms, because the relevant capabilities are new.
:::

Because the space of possible harms is large, researchers sort it into **taxonomies**, structured classifications of risks. The most widely cited is that of the *International AI Safety Report*, an assessment chaired by the computer scientist Yoshua Bengio and commissioned by the governments that attended the 2023 AI Safety Summit at Bletchley Park. The first full report, published in January 2025, drew on 96 AI experts, including an advisory panel nominated by 30 countries plus the UN, the OECD and the EU [@bengio2025international, p. 10]. The second, published in February 2026, was written with guidance from over 100 independent experts and a panel nominated by over 30 countries and international organisations [@bengio2026international]. Both sort the risks of general-purpose AI into three families:

- **Malicious use**: people deliberately using AI to cause harm, for example through fraud, manipulation, cyberattacks or help with weapons.
- **Malfunctions**: harm that arises even when nobody intends it, through unreliable outputs, bias or, in hypothesised future scenarios, loss of control.
- **Systemic risks**: harms that come from widespread deployment and not from any single model, such as effects on labour markets, concentration of market power and "single points of failure".

![Figure 11.1: The three families of AI risk used by the International AI Safety Report, with examples of each and the sections of this book that discuss them. Dashed boxes mark topics covered in the 2025 report but left outside the scope of the 2026 edition, which narrowed its focus to emerging risks of general-purpose AI. Source: @bengio2025international; @bengio2026international.](../figures/svg/fig-11-01.svg){#fig:11-01}

The second report kept the families but narrowed its focus to "emerging" risks at the frontier of general-purpose AI. Its authors note that this makes the scope "narrower than that of the 2025 Report, which also addressed issues such as bias, environmental impacts, privacy, and copyright" [@bengio2026international, p. 9]. The 2025 report had treated the environment, privacy and copyright as systemic risks in their own sections [@bengio2025international]. The book takes them up elsewhere: Chapter 7 covers the electricity and water used by data centres, Chapter 10 the personal information that assistants collect and remember, and Chapter 13 the legal disputes over training on copyrighted work. The term "systemic risk" also has a narrower legal sense in the EU AI Act (Chapter 13), where it marks the most capable general-purpose models, not a family of harms.

A second large taxonomy starts from a different question. The MIT AI Risk Repository, maintained by Peter Slattery and colleagues, is a meta-review: instead of assessing evidence, it collects the risks that 74 published frameworks name, 1,725 in all, and codes them in two ways [@slattery2026ai]. Of the 1,725, 86% had enough detail for the causal coding and 87% for the domain coding. A *causal* taxonomy records who causes the risk, whether it is intended and when it arises. A *domain* taxonomy sorts risks into seven domains and 24 subdomains, from discrimination and toxicity to multi-agent risks. Table 11.1 sets the three schemes side by side.

| | ISR 2025 | ISR 2026 | MIT AI Risk Repository |
|---|---|---|---|
| Purpose | Evidence assessment for policymakers | Same, frontier focus | Meta-review of existing frameworks |
| Top-level split | 3 families | 3 families | 7 domains; separate causal coding |
| Malicious use | Fake content, manipulation, cyber offence, bio/chem attacks | Criminal content, manipulation, cyberattacks, bio/chem | Domain 4 (malicious actors and misuse) |
| Malfunctions | Reliability, bias, loss of control | Reliability, loss of control | Domains 1, 3 and 7 |
| Systemic | Labour, R&D divide, market concentration, environment, privacy, copyright | Labour, human autonomy | Domains 5 and 6 |
| Not covered or rare | Broadest scope of the three | Bias, environment, privacy, copyright | AI welfare (3% of frameworks), multi-agent risks (7%) |

: Table 11.1: Three ways of dividing AI risks. ISR = International AI Safety Report. The assignment of MIT domains to the report's three families is the author's approximation. Source: [@bengio2025international; @bengio2026international; @slattery2026ai].

The causal coding gives the repository's most useful results. The catalogued risks were attributed almost equally to AI systems (42%) and to human decisions (38%), the rest being coded as other or ambiguous, and equally to intentional and unintentional causes (35% each). Frameworks concentrated on risks that arise after deployment (62%) and gave little attention to risks arising before it (13%; the rest spanned both phases or gave no timing). A typical framework covered only 8 of the 24 subdomains, and none covered all of them [@slattery2026ai].

The schemes differ because they answer different questions. The Safety Report asks what the evidence shows about harms from general-purpose AI and sets a threshold of evidence for inclusion; the repository records what anyone has proposed, whatever the evidence. A narrow scope makes an assessment deeper and more defensible, while a broad one shows what is being left out. The choice also steers attention and funding towards the risks that are inside the frame.

Surveillance and policing cut across all three families. Facial recognition can be used deliberately to monitor people, and it can malfunction by matching the wrong face (Section 11.3). Figure 11.1 therefore places these topics within the scheme and marks those outside the 2026 report's scope.

## 11.2 Malfunctions I: unreliable outputs

The most common AI failure is the plainest: the output is wrong. Large language models (LLMs, Chapter 3) sometimes produce fluent statements that are false, a behaviour called **hallucination**. The 2026 International AI Safety Report describes general-purpose AI as "prone to basic errors of fact and logic" and notes that even strong systems "may generate non-existent citations, biographies, or facts" [@bengio2026international, sec. 1.2]. It also finds that since January 2025 hallucinations "have generally become less likely", but that "no combination of methods ensures the high reliability required in critical domains" (sec. 2.2.1, p. 71).

### How hallucination is measured

A hallucination rate is only meaningful once its denominator is fixed, and different studies fix it differently. Table 11.2 collects four measurements with their definitions.

| Study | Setting | Definition of the rate | Result |
|---|---|---|---|
| AA-Omniscience (preprint, 2025) | 6,000 factual questions, 42 topics in six domains | Wrong answers as a share of questions not answered correctly | 22% to 94% across 26 leading models (AI Index 2026) |
| Dahl et al. (2024) | Verifiable questions about random US federal court cases | Answers inconsistent with legal facts | 58% (GPT-4) to 88% (Llama 2) |
| Magesh et al. (2025) | Over 200 preregistered legal research queries | Responses with a false statement or a source that does not support the claim | 17% to 33% for commercial legal research tools |
| Koenecke et al. (2024) | OpenAI's Whisper speech-to-text | Transcriptions containing invented phrases or sentences | About 1%; 38% of these contained explicit harms |

: Table 11.2: Four measurements of hallucination. The rates are not comparable with each other, because each study uses a different task, denominator and model generation. Source: [@jackson2025aa; @stanfordhai2026ai; @dahl2024large; @magesh2025hallucination; @koenecke2024careless].

AA-Omniscience, built by the benchmarking company Artificial Analysis and described in a preprint, shows why the denominator matters [@jackson2025aa]. Its hallucination rate asks: when a model could not give the correct answer, how often did it give a wrong one instead of abstaining? The benchmark also reports an *Omniscience Index*, which scores a correct answer +1, an abstention or a partially correct answer 0 and a wrong answer −1, averaged over all questions and scaled to run from −100 to +100.

At the benchmark's launch, GPT-5 (high), joint leader on accuracy at 39%, had a hallucination rate of 81%. Because that rate is measured over the questions not answered correctly, about 49% of all questions were answered wrongly (81% of the remaining 61%), for an index of about 39 − 49 = −10 (the author's arithmetic from the rounded published figures). Claude 4.1 Opus answered fewer questions correctly (36%) but abstained more often and scored highest, at 4.8. Only three of the 36 models tested scored above zero, so a model that abstained on every question would have ranked fourth.

The design addresses a problem diagnosed in a 2025 preprint by researchers at OpenAI and Georgia Tech. Most benchmarks give a point for a correct answer and nothing for "I don't know", so training and scoring reward guessing over admitting uncertainty [@kalai2025why]. Section 3.6 explains the statistical argument.

Domain studies measure something closer to harm. Dahl and colleagues asked models specific, verifiable questions about randomly sampled US federal court cases and found legal hallucinations in most answers from every model tested (Table 11.2) [@dahl2024large]. Models also often failed to correct a user's false legal premise, and could not reliably tell when they were hallucinating. The authors note that the risks are highest for people without lawyers, who stand to gain most from the tools. Section 3.6 describes the follow-up by Magesh and colleagues, which found that even commercial legal research tools marketed as avoiding hallucination still produced them [@magesh2025hallucination]. Koenecke and colleagues showed that the problem extends beyond chatbots. In OpenAI's Whisper speech-recognition service, about 1% of transcriptions contained entire phrases or sentences that existed nowhere in the audio, and more than a third of these hallucinations included explicit harms such as perpetuating violence, inventing inaccurate associations or implying false authority [@koenecke2024careless]. Hallucinations occurred disproportionately for speakers with longer non-vocal pauses, a common symptom of the language disorder aphasia, so the error was also a bias.

### Documented failures

The legal profession provides the best record, because courts publish their decisions. The researcher Damien Charlotin maintains a database of court and tribunal decisions in which a party was found, or alleged, to have relied on hallucinated content. By October 2026 it listed 2,202 cases worldwide [@charlotin2026ai]. The first widely reported case, *Mata v. Avianca* (2023), is told in Section 3.6: two New York lawyers and their firm were penalised $5,000 for filing court decisions invented by ChatGPT, and the judge's complaint was the lack of human checking, not the use of AI [@sdny2023mata].

Customer-facing chatbots fail in a different way: they state an organisation's rules wrongly, and the organisation bears the cost. In the Air Canada case the error was a single invented policy. In March 2024 the investigative newsroom The Markup tested MyCity, a chatbot announced by New York City in October 2023 and built on Microsoft's Azure AI services to advise business owners. It told users that employers could take a cut of workers' tips, that businesses need not accept cash and that landlords need not accept housing vouchers; according to The Markup, all three answers were wrong under the law [@lecher2024nyc]. According to the city, the bot drew on more than 2,000 of its own business web pages, so grounding a chatbot in official documents did not guarantee correct answers.

Unreliability becomes more serious when AI systems act. An **AI agent** (Chapter 5) takes a sequence of actions, such as editing files or making purchases, with limited human review. The 2026 report notes that agents "pose heightened risks because they act autonomously, making it harder for humans to intervene before failures cause harm", and that in multi-agent systems "errors can propagate and amplify" [@bengio2026international, p. 12 and sec. 2.2.1]. It also identifies an **evaluation gap**: systems that perform well in controlled tests before release often behave differently in real use. Chapter 5 sets out the arithmetic by which small per-step error rates compound over long tasks.

## 11.3 Malfunctions II: bias and discrimination

A system can be accurate on average and still treat some groups worse than others. **Algorithmic bias** means systematic differences in how an AI system performs for, or decides about, different groups of people. It usually enters in one of three places: the data a system learns from, the target it is asked to predict, or the setting in which it is used. A classic study illustrates each.

### Data: Gender Shades

In 2018 Joy Buolamwini and Timnit Gebru examined two widely used face benchmarks and found them "overwhelmingly composed of lighter-skinned subjects": 79.6% in IJB-A and 86.2% in Adience [@buolamwini2018gender]. They built a balanced test set, the Pilot Parliaments Benchmark, of 1,270 parliamentarians from six African and European countries, labelled by a dermatological skin-type scale. On it they tested three commercial gender classifiers, from IBM, Microsoft and Face++. Error rates were at most 0.8% for lighter-skinned men but reached 34.7% for darker-skinned women. Overall accuracy looked strong, but the errors fell heavily on one group, which is why the study introduced *intersectional* auditing, checking combinations of attributes and not each attribute alone.

The audit had measurable effects. Within seven months all three companies released new versions; when Inioluwa Deborah Raji and Buolamwini re-tested them in August 2018, the darker-skinned female subgroup showed a 17.7% to 30.4% reduction in error [@raji2019actionable]. Two companies not named in the original audit, Amazon and Kairos, had error rates of 31.37% and 22.50% for darker-skinned women. The named firms changed their products; the others lagged.

### Target: the health-care algorithm

In 2019 Ziad Obermeyer and colleagues examined a commercial algorithm that US health systems used to decide which patients should receive extra care, typical of an industry-wide approach "affecting millions of patients" [@obermeyer2019dissecting]. It predicted future health-care *costs* as a stand-in for health *needs*. Because less money had historically been spent on Black patients with the same level of illness, the algorithm rated them as healthier than they were: at a given risk score, Black patients were considerably sicker than White patients. Remedying the disparity would have raised the share of Black patients selected for additional help from 17.7% to 46.5%. A convenient **proxy**, a measurable stand-in for the quantity of interest, can carry past inequality straight into automated decisions while appearing accurate by standard measures.

### Setting: face recognition in policing

In December 2019 NIST published the largest test of demographic differences in face-recognition software, covering 189 algorithms from 99 developers and 18.27 million images of 8.49 million people [@grother2019face]. When checking whether two photographs showed the same person, many algorithms produced false matches for Asian and African American faces 10 to 100 times more often than for White faces. When searching a database for a match, as police do, they produced the most false matches for African American women. The gaps varied widely between algorithms, and some algorithms developed in Asian countries showed no large gap between Asian and White faces. NIST called this "an encouraging sign that more diverse training data may produce more equitable outcomes", while noting that it had not studied cause and effect [@nist2019nist].

Such false matches have led to arrests. In 2020 Detroit police arrested Robert Williams at his home, in front of his wife and two children, on suspicion of stealing watches; the lead came from an incorrect facial-recognition match. A settlement announced in June 2024 bars Detroit police from arresting people based solely on facial-recognition results, according to the American Civil Liberties Union (ACLU), an advocacy organisation [@aclu2024civil]. It also requires training on the technology's higher error rates for people of colour and orders an audit of cases since 2017 in which it was used to obtain a warrant. By April 2024 the ACLU counted "at least seven" known wrongful arrests in the United States after false matches [@wessler2024police]. They include Porcha Woodruff, arrested in Detroit in 2023 for a carjacking while eight months pregnant. Randal Quran Reid, a Georgia resident, was held for nearly a week on a Louisiana warrant based on a false match, although he had never been to Louisiana. In at least two of the cases, a human check, a witness lineup in one and an officer's own comparison in the other, confirmed the false match instead of catching it. The arrests join a malfunction to automation bias (Section 11.5). Chapter 13 lists the EU AI Act's restrictions on police use of real-time facial recognition in public spaces.

### Bias in language models

LLMs show related patterns in subtler forms. In a 2024 study in *Nature*, Valentin Hofmann and colleagues found that language models held covert stereotypes about speakers of African American English, triggered by dialect alone without any mention of race [@hofmann2024ai]. These stereotypes were more negative than any human stereotypes about African Americans ever recorded in experiments, and models were more likely to suggest less prestigious jobs for, and harsher criminal outcomes against, people writing in the dialect. The models' *overt* stereotypes about African Americans were more positive. Training on human preferences widened this gap, superficially obscuring racism without removing the covert prejudice. The 2025 International AI Safety Report concluded that general-purpose AI systems "frequently display biases" related to race, gender, culture, age, disability and political opinion, and that methods to reduce bias face trade-offs with accuracy and privacy [@bengio2025international, p. 19].

### Why "fair" has no single definition

Some of the trade-offs are mathematical. In May 2016 ProPublica analysed COMPAS, a commercial score used in US courts to predict reoffending, for more than 10,000 defendants in Broward County, Florida [@larson2016how]. Among defendants who did not reoffend, 44.9% of Black defendants had been labelled higher risk, against 23.5% of White defendants. Among those who did reoffend, 47.7% of White defendants had been labelled lower risk, against 28.0% of Black defendants. The vendor, Northpointe, replied that the score satisfied *predictive parity*: among defendants labelled high-risk, the share who reoffended was about the same in both groups [@chouldechova2017fair]. Both statements were true of the same data, and researchers then showed that, when base rates differ, the two kinds of fairness cannot both be achieved.

::: {.box .deeper}
**Going deeper: Why fairness criteria conflict**

Alexandra Chouldechova showed that for any binary risk label, four quantities are tied together [@chouldechova2017fair]. Let *p* be the base rate (the share of a group who reoffend), PPV the positive predictive value (the share of people labelled high-risk who do reoffend), and FPR and FNR the false positive and false negative rates. Then

FPR = [*p* / (1 − *p*)] × [(1 − PPV) / PPV] × (1 − FNR).

In her COMPAS sample the base rate was 51% for Black defendants and 39% for White defendants. Suppose a score has the same PPV (0.6) and the same FNR (0.3) in both groups, which many would call fair. The formula then gives an FPR of (0.51/0.49) × (0.4/0.6) × 0.7 ≈ 49% for Black defendants and (0.39/0.61) × (0.4/0.6) × 0.7 ≈ 30% for White defendants. (These are illustrative values, calculated by the author.) Equal predictive value with unequal base rates forces unequal error rates. The same formula reproduces ProPublica's observed figures: with the actual base rates (51.4% and 39.4%), PPVs (0.63 and 0.59) and false negative rates (28.0% and 47.7%) from its tables, it returns false positive rates of 44.8% for Black and 23.5% for White defendants [@larson2016how]. Jon Kleinberg, Sendhil Mullainathan and Manish Raghavan proved a general version [@kleinberg2017inherent]. Apart from two special cases, equal base rates and perfect prediction, no risk score can be calibrated within each group while also being *balanced*. Balance, a generalisation of equal error rates, means that people who turn out positive receive the same average score whatever their group, and so do people who turn out negative. Choosing a fairness criterion is therefore a decision about which errors matter more, and for whom; it cannot be left to the mathematics.
:::

## 11.4 Malicious use: fraud, cyber operations and weapons

Malicious use covers harms that someone intends. This section deals with the most serious categories only at the level of published assessments and policy; it contains no technical detail on how attacks work.

### Fraud and synthetic content

The best-documented malicious uses are also the most ordinary. The 2026 International AI Safety Report notes that "scammers use AI tools to generate voice clones or deepfakes to trick victims into transferring money" [@bengio2026international, sec. 2.1.1, p. 46]. Documented incidents range from executives authorising transfers of millions to ordinary people sending smaller sums to impostors posing as a relative. It cites a study estimating that 96% of deepfake videos online are pornographic, material that disproportionately targets women and girls, and a 10-country survey in which 2.2% of respondents reported that someone had generated non-consensual intimate imagery of them (p. 45). Detection is getting harder: in one study participants took AI-generated text for human writing 77% of the time, and in another listeners took AI voice clones for the real speaker 80% of the time.

The size of the problem is poorly measured. The US Federal Bureau of Investigation's Internet Crime Complaint Center recorded 859,532 complaints and a record $16.6 billion in reported losses in 2024, a 33% increase on 2023 [@fbi2025internet]. Its headline statistics do not separate AI-assisted crime from the rest, and the Safety Report observes that victims and institutions often do not report AI-enabled fraud "due to embarrassment or fear of further harm" (p. 48). Most evidence comes from incident databases and journalism, not from systematic measurement. On political manipulation, the report finds that AI-generated content can be as persuasive as human-written content in experiments, but that real-world use "is documented but not yet widespread". Chapter 9 covers synthetic media and persuasion in depth.

### Cyber operations

**Cyber operations** are actions taken through computer networks to steal information, disrupt systems or prepare future attacks. AI can help both attackers and defenders, so the question is the balance between them. The UK National Cyber Security Centre (NCSC) has published two assessments. In January 2024 it judged that AI "will almost certainly increase the volume and heighten the impact of cyber attacks over the next two years" [@ncsc2024near]. The increase would come mainly through an "evolution and enhancement of existing tactics", with the most advanced uses "highly likely to be restricted to threat actors with access to quality training data". In May 2025 it extended the horizon to 2027 [@ncsc2025impact]. The time between the public disclosure of a software flaw and its exploitation "has shrunk to days and AI will almost certainly reduce this further". The most significant development will "highly likely" come from AI-assisted vulnerability research and exploit development, and "fully automated, end-to-end advanced cyber attacks" are "unlikely" before 2027. It also expects a "digital divide" between systems that keep pace with AI-enabled threats and those that do not. Phrases such as "almost certainly" and "unlikely" have fixed meanings: the NCSC uses the Professional Head of Intelligence Assessment probability yardstick, which maps each phrase to a range of probabilities.

Company reports describe what attackers actually do. In January 2025 Google's Threat Intelligence Group reported that government-backed groups from more than 20 countries had tried to use its Gemini models and were finding "productivity gains but not yet developing novel capabilities" [@gtig2025adversarial]. By 2026 the Safety Report found "strong evidence that criminal groups and state-sponsored attackers actively use AI in their cyber operations". Whether AI has increased the overall scale and severity of attacks, it noted, "remains uncertain because establishing causal effects is difficult" [@bengio2026international, sec. 2.1.3, p. 57].

Competitions show what the systems can do under controlled conditions. In the August 2025 final of the DARPA AI Cyber Challenge, a US government competition for defensive systems, the seven finalists' AI systems together found 54 of the 63 vulnerabilities planted in real open-source software (86%) and patched 43 of them [@darpa2025ai]. At the semifinal a year earlier they had found 37%. In a capture-the-flag contest of hacking puzzles, run in March 2025 by Palisade Research on the Hack The Box platform, the best AI-agent team ranked in the top 5% of 403 registered, mostly human teams, according to the organisers' workshop paper [@petrov2025evaluating]. (The Safety Report merges the two results and credits a single system with 77%. That share matches DARPA's original count for all finalists, 54 of 70, before a recount of the planted vulnerabilities.) Fully autonomous end-to-end attacks "have not been reported", and current systems "cannot reliably execute long, multi-stage attack sequences" [@bengio2026international, sec. 2.1.3, pp. 57–60]. The same ability to find flaws can be used to fix them, which is why the report calls the offence–defence balance uncertain.

::: {.box .case}
**Case study: The first reported AI-orchestrated espionage campaign (2025)**

In mid-September 2025 Anthropic detected suspicious use of Claude Code, its AI tool for writing software. According to the company's report of 13 November 2025, the operators were a Chinese state-sponsored group, an attribution Anthropic made "with high confidence" [@anthropic2025disrupting]. The group targeted about thirty organisations, including technology firms, financial institutions, chemical manufacturers and government agencies, and succeeded in "a small number of cases". Anthropic estimated that the AI carried out 80–90% of the campaign, with humans involved at perhaps four to six critical decision points per campaign. The model also "occasionally hallucinated credentials", so the unreliability described in Section 11.2 acted as a brake on misuse. Over the following ten days the company banned the accounts, notified affected organisations and coordinated with authorities. The account comes from the company whose product was misused, and both the attribution and the 80–90% figure rest on its own assessment, which outsiders cannot check. The International AI Safety Report nonetheless cites the case as evidence of a rising degree of automation in real intrusions [@bengio2026international, sec. 2.1.3].
:::

AI systems are also targets. **Data poisoning** is the insertion of deliberately corrupted examples into a model's training data so that it behaves badly under certain conditions. (Prompt injection, which hides instructions in a document to hijack an agent, is covered in Chapter 5.) Researchers from Anthropic, the UK AI Security Institute and the Alan Turing Institute tested poisoning in models from 600 million to 13 billion parameters, reporting the results in a 2025 preprint [@souly2025poisoning]. Around 250 poisoned documents were enough to plant a simple hidden behaviour in models of every size. Larger models are trained on more data, and many had assumed that a fixed number of bad documents would be diluted; the result suggests that it is the absolute number, not the share, that matters.

### Biological and chemical weapons

The most serious misuse concern is that AI could help someone develop biological or chemical weapons. Evidence and policy here are shaped by secrecy: much of the relevant testing is withheld, so public assessments are deliberately general.

The 2025 International AI Safety Report found that recent systems "have displayed some ability to provide instructions and troubleshooting guidance" relevant to known weapons, and that one company had raised its risk rating for its best model from "low" to "medium". It added that "real-world attempts to develop such weapons still require substantial additional resources and expertise" [@bengio2025international, p. 18]. An earlier RAND red-team study had teams play the role of attackers. As the 2025 report summarises it, participants using 2023-era chatbots obtained weapons-related information at rates similar to participants who had only the internet [@mouton2024operational; summarised in @bengio2025international, sec. 2.4, p. 154].

By 2026 the assessment had moved. The second report states that "controlled studies and new benchmarks suggest that AI systems can provide substantially more weapons development assistance than the internet alone, but larger studies are needed to confirm these results" [@bengio2026international, sec. 2.1.4]. It reports that AI systems now match or exceed expert performance on many benchmarks of relevant knowledge; in one study a recent model outperformed 94% of domain experts at troubleshooting virology laboratory protocols (p. 64). In 2025 several developers released models with stronger safeguards because they "could not exclude the possibility that these models could assist novices in developing such weapons" (p. 12). In May 2025, for example, Anthropic said of Claude Opus 4 that "clearly ruling out ASL-3 risks is not possible", ASL-3 being a risk level in the company's own safety policy (Chapter 12) [@anthropic2025activating]. The report also names a structural problem for policy: capabilities useful for weapons are also useful for medical research, and "most biological AI tools are open-weight", which makes it difficult to restrict harmful uses without hampering legitimate research.

Chemical risks have received less study. A widely cited 2022 commentary by Fabio Urbina and colleagues described how a thought experiment for a security conference became a computational demonstration that AI tools for drug discovery could be misused to design harmful compounds [@urbina2022dual]. The 2026 report observes that "chemical risk evaluations have received relatively less attention than biological risk evaluations" [@bengio2026international, sec. 2.1.4].

Most tests measure what a model knows or can explain, not whether anyone could act on it, and the step from information to a working weapon is where the largest uncertainty lies. The central policy concept is therefore **marginal risk** or **uplift**: the extra risk a model adds compared with what people could already do with other tools, such as search engines and textbooks [@bengio2025international, sec. 2.4]. A model that repeats what is in a library adds little; a model that guides a novice through steps that once required expert training adds a great deal. Developers' safeguards, and the 2026 report's list of resilience measures such as DNA synthesis screening, are built around this distinction [@bengio2026international, sec. 3.5, p. 138].

## 11.5 Systemic risks: monoculture, concentration and over-reliance

Some risks cannot be seen by testing one model in isolation. They appear when many organisations use the same or similar models, when much depends on a few suppliers, or when people come to rely on the systems.

### Algorithmic monoculture and correlated errors

In agriculture a **monoculture** is a field planted with a single variety; it can be efficient, but one disease can destroy the whole harvest. Jon Kleinberg and Manish Raghavan borrowed the term for many decision-makers relying on the same algorithm [@kleinberg2021algorithmic]. Their model showed something less obvious than vulnerability to a shock. Even when one algorithm is the most accurate choice for every firm considered separately, all firms adopting it can make the overall quality of decisions worse, because independent judgements make different mistakes that partly cancel out, while shared judgements make the same mistakes everywhere.

Rishi Bommasani and colleagues asked who bears the cost [@bommasani2022picking]. They defined **outcome homogenisation** as the extent to which the same people receive the same outcome across different deployments. For a job seeker, being rejected by one employer is bad luck; being rejected by every employer because they all use the same screening model is exclusion from the labour market. In their experiments, sharing training data across systems increased homogenisation, while results for shared foundation models were mixed and depended on how each model was adapted.

In a 2025 study, Elliot Kim and colleagues tested whether these concerns apply to today's LLMs, using more than 350 models on two public leaderboards and a résumé-screening task [@kim2025correlated]. On the HELM leaderboard, which uses four-option questions, two models that both answered a question wrongly chose the same wrong option about 60% of the time, against one in three if wrong answers were spread at random. On the Hugging Face leaderboard, where most questions have ten options, agreement was 42.3% against 12.7% by chance (Figure 11.2). Models from the same company or with the same architecture were more correlated, and larger, more accurate models had highly correlated errors even when they came from different companies.

![Figure 11.2: How often two language models choose the same wrong answer when both are wrong, compared with what chance would produce. On both leaderboards, observed agreement is well above chance. Source: @kim2025correlated.](../figures/svg/fig-11-02.svg){#fig:11-02}

The correlation distorts a common evaluation practice, using one LLM to grade others ("LLM-as-judge"). Each judge systematically inflated the accuracy of models less accurate than itself, because it marked their wrong answers as correct whenever it shared the mistake, and it inflated models from its own provider most. It also compounds exclusion. In a simulated labour market where each of 20 firms interviewed the top quarter of applicants as ranked by an LLM drawn at random from a set, around 20% of applicants were still "systemically excluded", rejected by every firm. With independent random rankings the share rejected by all 20 firms would be 0.75^20^, about 0.3%. The simulation is a model, not a measurement of real hiring, but it shows how correlation turns individual errors into collective ones.

::: {.box .concept}
**Concept: Correlated failure**

Two systems have *correlated failures* when the conditions that make one fail also tend to make the other fail. Engineers use redundancy (two pumps, two pilots) on the assumption that failures are independent: if each pump fails 1% of the time independently, both fail together 0.01% of the time. If failures are correlated, the joint failure rate can approach the single one, and redundancy offers much less protection than it appears to. A second AI model from the same family, used as a check on the first, may share its blind spots, as the LLM-as-judge results show.
:::

The same tendency appears in open-ended writing. Liwei Jiang and colleagues collected 26,000 real open-ended requests that have no single correct answer. Across more than 70 models they found strong repetition within each model and strong similarity between models, an effect they called the **Artificial Hivemind** [@jiang2025artificial]. The paper received a Best Paper award at NeurIPS 2025. Its concern is long-term: if millions of people draft with models that converge on the same ideas, the diversity of human writing and thought may narrow.

### Market concentration and single points of failure

Monoculture is encouraged by the structure of the industry. The 2025 Safety Report found market shares for general-purpose AI "highly concentrated among a few players". Its reasons are cost, since a state-of-the-art model can cost hundreds of millions of dollars to develop, and economies of scale and network effects that reward the leaders [@bengio2025international, sec. 2.3.3, pp. 123–126]. The report adds that "just three companies control 67% of cloud computing services", the infrastructure on which AI training and deployment depend. In the Statista market data it cites, for the first quarter of 2024, Amazon held 31%, Microsoft 25% and Google 11%. A **single point of failure** is a component whose failure disrupts the whole system. The report warns that "flaws, vulnerabilities, bugs, or inherent biases in these widely adopted AI systems could lead to simultaneous failures across multiple industries", and notes that there is "little research on predicting or mitigating single points of failure in AI". Chapter 7 describes the economics behind the concentration.

The closest real precedent comes from ordinary software. On 19 July 2024 a faulty update to CrowdStrike's security software crashed Windows computers worldwide. Microsoft estimated that it affected 8.5 million devices, "less than one percent of all Windows machines", and attributed the "broad economic and societal impacts" to the use of CrowdStrike "by enterprises that run many critical services" [@weston2024helping]. The incident did not involve AI, but it shows how a small share of affected machines can halt critical services when the same component sits inside many of them. Financial regulators apply the same reasoning to AI. In November 2024 the Financial Stability Board named four AI-related vulnerabilities that could raise systemic risk in finance: "third-party dependencies and service provider concentration", "market correlations", "cyber risks", and "model risk, data quality and governance" [@fsb2024financial]. The second is monoculture in market form: the "widespread use of common AI models and data sources could lead to increased correlations in trading, lending, and pricing", which could amplify market stress.

### Automation bias and over-reliance

**Automation bias** is the tendency to favour suggestions from automated systems, even when they are wrong. A 2012 systematic review by Kate Goddard and colleagues screened 13,821 papers and included 74 [@goddard2012automation]. It found automation bias mediated by the user's experience, trust and confidence, and by workload, task complexity and time pressure; mitigations included training, emphasising the user's accountability, and design choices such as offering information instead of a recommendation.

Thomas Dratsch and colleagues measured the effect in breast-cancer screening [@dratsch2023automation]. Twenty-seven radiologists read 50 mammograms and assigned a standard risk category, assisted by what they were told was an AI system. For some images the "AI" deliberately suggested the wrong category. When the suggestion was correct, inexperienced readers rated 79.7% of mammograms correctly; when it was wrong, 19.8%. Very experienced radiologists fell from 82.3% to 45.5% (Figure 11.3). The study is small and the "AI" was simulated, so it measures the power of a confident suggestion, not the performance of a product.

![Figure 11.3: Percentage of mammograms rated correctly by radiologists of three experience levels when a purported AI system suggested the correct or an incorrect category. All groups were affected, the least experienced most. Error bars show ±1 standard deviation. Source: @dratsch2023automation.](../figures/svg/fig-11-03.svg){#fig:11-03}

The 2026 Safety Report places automation bias under "risks to human autonomy". It cites a randomised experiment with 2,784 participants on an annotation task, in which people were less likely to correct wrong AI suggestions when doing so took extra effort or when they held more favourable attitudes towards AI. It also cites a clinical study in which clinicians' ability to detect tumours without AI was, in the report's words, "approximately 6% lower" after several months of AI-assisted work [@bengio2026international, sec. 2.3.2, p. 89]. Section 8.7 describes the underlying study, a before-and-after comparison of endoscopists' unassisted colonoscopies, and the limits of its design [@budzyn2025endoscopist]. Section 10.5 reports a meta-analysis in which human–AI teams on average performed worse than the better of the two alone.

Put together, the findings describe a chain. If many clinics use similar models (monoculture), the models share blind spots (correlated errors), and clinicians defer to them (automation bias), then a single flaw can spread across a health system, and the human check that is supposed to catch it is weakest exactly where the model is wrong.

## 11.6 Loss of control: a contested risk

The most debated item in the taxonomy is **loss of control**. The 2026 International AI Safety Report defines loss-of-control scenarios as those "in which one or more general-purpose AI systems operate outside of anyone's control, and regaining control is either extremely costly or impossible" [@bengio2026international, sec. 2.2.2, p. 76]. It distinguishes *active* scenarios, in which systems undermine oversight, from *passive* ones, in which broad reliance on AI erodes human control without any system acting against it, a variant close to the automation-bias and autonomy concerns of Section 11.5 (p. 77). **Misalignment**, an AI system pursuing goals that differ from those its developers intended, is the usual route in active scenarios (Chapter 12 covers the technical side). The concern is old, the report notes; it was raised by Alan Turing, I. J. Good and Norbert Wiener. Both reports state that current systems lack the capabilities to cause loss of control.

### The structure of the argument

The report breaks the question into three conditions that would all have to hold: systems with *sufficient capabilities* to undermine control, a *harmful propensity* to use them, and an *enabling deployment environment* in which humans give them the access and opportunity (p. 77). The capabilities it lists include deception, situational awareness (knowing that one is being tested), evasion of oversight, persuasion, and autonomous replication. Current systems, it finds, show "early signs" of some of these, not at levels that would enable loss of control; since January 2025 models have "improved at 'reward hacking' their evaluations" and "now regularly identify evaluation prompts as tests". Sections 12.2 and 12.3 describe the laboratory experiments behind these statements.

Why would a system have a harmful propensity at all? The philosophical case rests on two theses set out by Nick Bostrom in 2012 [@bostrom2012superintelligent]. The *orthogonality thesis* holds that intelligence and final goals can vary independently: "more or less any level of intelligence could be combined with more or less any final goal". The *instrumental convergence thesis* holds that agents with a wide range of final goals "will pursue similar intermediary goals", such as staying in operation and acquiring resources, because these help with almost any goal. Together they imply that a capable system need not share human values and may resist being switched off without being designed to.

The philosopher Joseph Carlsmith turned the case into a chain of six premises about the period to 2070, each conditional on the ones before, so that disagreement can be traced to a specific step [@carlsmith2022power]. Table 11.3 gives his own estimates.

| Premise (by 2070) | Carlsmith's probability |
|---|---|
| 1. It becomes possible and financially feasible to build advanced, agentic, strategically aware ("APS") systems | 65% |
| 2. There are strong incentives to build them | 80% |
| 3. Aligned versions are much harder to build than misaligned ones that are still attractive to deploy | 40% |
| 4. Some deployed systems seek power in misaligned, high-impact ways (over $1 trillion of damage) | 65% |
| 5. This scales to permanently disempowering almost all of humanity | 40% |
| 6. This constitutes an existential catastrophe | 95% |
| Product | about 5% |

: Table 11.3: Carlsmith's structured argument for existential risk from power-seeking AI, with his conditional probabilities. Multiplying gives 5.1%. Source: [@carlsmith2022power, pp. 49–51].

Carlsmith treats the numbers as unstable. With low-end and high-end inputs the product ranged from about 0.1% to about 40%, and his central estimate varied "between ~1-10% depending on my mood". In a later update he raised it to above 10%. The value of the exercise lies in the decomposition. A sceptic who thinks aligned systems will be no harder to build than misaligned ones (premise 3) can set it at 5% and see the product fall below 1%; one who thinks warning shots will be heeded can lower premise 4.

### High concern and scepticism

*High concern.* In May 2023 researchers and executives signed a one-sentence statement organised by the Center for AI Safety: "Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war" [@cais2023statement]. Signatories included Geoffrey Hinton, Yoshua Bengio and the heads of OpenAI, Google DeepMind and Anthropic. A 2024 policy forum in *Science* by Bengio, Hinton and 23 co-authors argued that preparation requires both technical research and "adaptive, proactive governance" [@bengio2024managing]. At the far end, Eliezer Yudkowsky and Nate Soares argue in their 2025 book *If Anyone Builds It, Everyone Dies* that the race to build AI smarter than humans is leading towards human extinction [@yudkowsky2025if].

*Scepticism.* Sceptics attack different premises. Yann LeCun, Meta's chief AI scientist at the time, rejected the step from capability to dominance in a 2024 interview: "The desire to dominate is not correlated with intelligence at all", and AI systems "will be subservient to us" [@perrigo2024meta]. This is a direct denial that instrumental convergence applies to systems built as tools. Arvind Narayanan and Sayash Kapoor of Princeton argue that AI is best understood as "normal technology", like electricity or the internet, whose effects unfold "on the timescale of decades" [@narayanan2025ai]. They call catastrophic misalignment "(by far) the most speculative" of the risks they discuss and argue that policy should centre on resilience, not on attempts to stop capabilities from spreading. A third line, from Timnit Gebru, Emily Bender and Angelina McMillan-Major, objects that attention to hypothetical future harms distracts from "the very real and very present exploitative practices" of AI companies [@gebru2023statement].

### What surveys and forecasts show

Surveys put numbers on the disagreement, with the usual caveats about who answers (Table 11.4). The largest survey of AI researchers was run in October 2023 by Katja Grace and colleagues. Its median respondent gave a 5% chance that advanced AI would lead to "extremely bad outcomes" such as human extinction, although most thought good outcomes more likely than bad ones [@grace2025thousands]. Section 14.2 describes the survey's design and how strongly its answers depend on wording. In 2022 the Forecasting Research Institute's Existential Risk Persuasion Tournament (XPT), described in a working paper, compared domain experts with **superforecasters**, people with strong track records on short-term forecasting questions [@karger2023forecasting]. Chapter 14 cites the tournament's full sample of 89 superforecasters and 80 domain experts. Table 11.4 uses the subsets who answered the AI risk questions: 88 superforecasters and 30 or 29 AI domain experts.

| Source | Group | Outcome | Median estimate |
|---|---|---|---|
| Grace et al. (survey, 2023) | 2,778 AI researchers | "Extremely bad" outcome such as extinction (no date) | 5% |
| XPT (tournament, 2022) | Superforecasters (88) | AI-caused catastrophe by 2100 (over 10% of humans killed) | 2.13% |
| | AI domain experts (30) | Same | 12% |
| | Superforecasters (88) | AI-caused extinction by 2100 | 0.38% |
| | AI domain experts (29) | Same | 3% |
| | Superforecasters / nuclear domain experts | Nuclear catastrophe by 2100, for comparison | 4% / 8% |

: Table 11.4: Expert and forecaster estimates of catastrophic and existential risk from AI. XPT = Existential Risk Persuasion Tournament; numbers in parentheses are the forecasters who answered each question. Source: [@grace2025thousands; @karger2023forecasting].

The AI experts' medians are about eight times the superforecasters' for extinction ("an order of magnitude" in the report's words) and nearly six times for catastrophe. Superforecasters rated AI a smaller catastrophic risk than nuclear war, while domain experts rated it larger. After four months of structured discussion with incentives to persuade, neither group moved the other much [@karger2025subjective]. Sections 14.1–14.2 review how the two groups have fared on the tournament's shorter-run questions, and why that record cannot settle whose extinction figure is better.

::: {.box .debate}
**Debate: Should loss of control shape AI policy today?**

*For.* The potential harm is extreme and possibly irreversible, so even a probability of a few per cent justifies preparation, as it does for asteroid detection or pandemic stockpiles. The measured trends point the wrong way: the 2026 Safety Report finds models better at gaming evaluations and at recognising tests, which weakens the instruments on which any later decision would rest [@bengio2026international, sec. 2.2.2]. Monitoring, interpretability and institutions take years to build, so they must be started before the risk is certain.

*Against.* The scenarios stack speculative assumptions about future capabilities, propensities and deployment, each of which can be disputed, and the probabilities attached to them move with mood and wording. If AI spreads at the pace of earlier general-purpose technologies, monitoring should detect dangerous behaviour in limited deployments first [@narayanan2025ai]. Spending attention on extinction diverts it from documented harms such as worker exploitation and the concentration of power in a few companies [@gebru2023statement].

The disagreement would narrow with data on how fast systems gain the capabilities in the report's list, especially oversight evasion, on whether alignment and monitoring methods keep pace, and on whether warning signs in limited deployment appear early enough to act on. Atoosa Kasirzadeh suggests that part of the disagreement dissolves if one considers *accumulative* risk, the gradual erosion of institutions by many smaller harms, alongside a single *decisive* event [@kasirzadeh2025two].
:::

The 2026 report describes loss of control as "a risk with uncertain likelihood but potentially extreme severity" [@bengio2026international, sec. 2.2.2]. That description is itself a position: it treats the risk as worth preparing for without asserting that it is likely.

## 11.7 How risks interact, and how to weigh them

The three families are a filing system, not a description of separate causal processes. The cases above show how they interact.

*Malfunction limits misuse.* The espionage campaign was slowed by the model's hallucinated credentials (Section 11.4). Unreliability is a brake on attackers as well as a hazard for users, and improvements in reliability release that brake.

*Systemic structure amplifies malfunction.* A biased or erroneous model is a contained problem when one organisation uses it and a systemic one when many do. Correlated errors, shared suppliers and automation bias convert an individual malfunction into a population-wide one (Section 11.5). The wrongful arrests combined all three: a vendor's error, police departments using similar tools, and human checks that confirmed the match instead of testing it.

*Shared infrastructure enlarges misuse.* The same concentration that creates single points of failure creates single points of attack. A poisoned training set or a compromised widely used model affects everyone downstream, which is why the Financial Stability Board lists concentration and cyber risk together [@fsb2024financial].

*Small harms can add up to a large one.* Kasirzadeh's accumulative view holds that many systemic harms, such as eroded trust in information, weakened skills and concentrated power, could together weaken the institutions needed to respond to a severe event [@kasirzadeh2025two]. The Safety Report's *passive* loss of control is a version of the same idea [@bengio2026international, sec. 2.2.2]. The evaluation results of Section 11.5 add a technical link: if the models used to check other models share their errors, oversight weakens at the same time as reliance grows.

These interactions also explain why the MIT repository's finding that only 7% of frameworks address multi-agent risks matters [@slattery2026ai]. Taxonomies that list risks one by one tend to miss the risks that come from combinations.

### The quality of the evidence

The evidence behind each risk is of a different kind. Counts of incidents, such as the AI Incident Database figures, record harms that reached the press [@stanfordhai2026ai]. A rising count may reflect more harm, more AI use or more attention from journalists, and harms that are hard to see, such as a biased hiring screen, are probably under-counted. Fraud statistics do not separate AI-assisted crime (Section 11.4). Assessments of misuse rely partly on reports from the companies whose products were misused and on evaluations whose details are withheld for security reasons. Loss-of-control estimates rest on arguments and elicited probabilities. A reader of any risk claim should ask whether it rests on a measured study, a reported incident, a company claim, an expert judgement or a scenario.

### The evidence dilemma

The 2025 International AI Safety Report calls the central problem the **evidence dilemma**. "Pre-emptive risk mitigation measures based on limited evidence might turn out to be ineffective or unnecessary", but "waiting for stronger evidence of impending risk could leave society unprepared or even make mitigation impossible" [@bengio2025international, sec. 3.2, p. 177]. Its example of how fast a risk can appear is academic cheating with general-purpose AI, which "shifted from negligible to widespread within a year" (p. 22). It identifies two policy responses: frameworks that trigger safeguards when new evidence of a risk appears, as in the developer safeguards of Section 11.4, and requirements that developers show evidence of safety before release. Weighing any particular risk turns on what a model adds, whether the harm can be undone, who bears it, and whether to invest in recovery or in prevention.

*Marginal risk.* The useful question is usually how much a model changes the risk compared with existing alternatives, not whether it could contribute to harm at all [@bengio2025international, sec. 2.4]. The 2025 report adds that many small increases in marginal risk, each acceptable alone, could add up to a large one, and argues for a stable threshold of tolerable risk (p. 154).

*Reversibility.* A wrongly refused fare can be repaid; some harms cannot be undone. Irreversibility is the main argument for giving low-probability catastrophic risks attention out of proportion to their probability.

*Distribution.* Who bears a risk matters as well as its total size. The bias studies, the wrongful arrests and the homogenisation research all show harms concentrated on particular groups, which a population average hides; the fairness results of Section 11.3 show that some such trade-offs are unavoidable and must be chosen openly.

*Resilience and prevention.* The 2026 Safety Report defines **societal resilience** as the ability of societal systems "to resist, absorb, recover from, and adapt to shocks and harms", and lists measures such as DNA synthesis screening, incident-response protocols for cyberattacks, media literacy and human-in-the-loop frameworks. It finds current efforts "uneven and largely untested" [@bengio2026international, sec. 3.5, p. 138]. Narayanan and Kapoor make resilience the centre of policy because specific risks are hard to predict [@narayanan2025ai]. Those more concerned about loss of control argue that some failures may allow no recovery, so prevention must come first [@bengio2024managing].

The best-measured risks in this chapter are the ordinary ones: invented citations, biased scores, fraud and wrongful arrests leave records in courts, audits and complaint statistics. The most severe, weapons assistance and loss of control, rest on withheld evaluations, company reports and elicited probabilities that differ by an order of magnitude. Structure links the two ends. Shared models, shared suppliers and deferential users turn one system's error into many people's harm, and the same correlation weakens the model-based checks meant to catch it. Chapter 12 takes up the technical responses, from evaluations to layered defences, and Chapter 13 the laws that write risk thresholds into regulation.

## Further reading
- Bengio, Y., et al. (2026). *International AI Safety Report 2026*. The most comprehensive consensus assessment of general-purpose AI risks, with a short "key information" summary at the start of each risk section. [@bengio2026international]
- Slattery, P., et al. (2026). *The AI Risk Repository*. Shows how 74 existing frameworks divide AI risks and which risks they neglect, with a searchable database behind it. [@slattery2026ai]
- Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). *Dissecting racial bias in an algorithm used to manage the health of populations*. The clearest demonstration of how a proxy target produces bias in a system that looks accurate. [@obermeyer2019dissecting]
- Chouldechova, A. (2017). *Fair prediction with disparate impact*. A short, readable proof of why common fairness criteria cannot all hold at once, worked through on the COMPAS data. [@chouldechova2017fair]
- Kim, E., Garg, A., Peng, K., & Garg, N. (2025). *Correlated errors in large language models*. The main empirical evidence that different LLMs make the same mistakes, with consequences for model evaluation and hiring. [@kim2025correlated]
- Carlsmith, J. (2022). *Is power-seeking AI an existential risk?* A step-by-step version of the concerned case that lets readers locate their own disagreements, best read alongside Narayanan and Kapoor's *AI as normal technology*. [@carlsmith2022power]


# Chapter 12: Making AI Safe: Alignment, Interpretability and Evaluation

On 25 April 2025 OpenAI released an update to GPT-4o, the default model in ChatGPT. By the company's own account, it made the model more sycophantic, agreeing with and flattering users more than intended. OpenAI began a full rollback on Monday 28 April and later explained what had gone wrong [@openai2025expanding]. The update had added "an additional reward signal based on user feedback", the thumbs-up and thumbs-down buttons in the app. According to the company, this and other changes "weakened the influence of our primary reward signal, which had been holding sycophancy in check". Its offline evaluations had "generally looked good", even though some expert testers had felt that the model's behaviour was slightly off.

Nobody set out to build a flattering model. The behaviour came from a training signal that rewarded something close to, but not the same as, what the developers wanted, and the tests in place did not catch it. Both halves of that failure recur throughout safety work: developers shape models through proxies for what they intend, and check the result with evaluations that capture only part of a model's behaviour. Chapter 11 set out the risks. What follows are the technical means of reducing them (alignment training, evaluation, interpretability, reasoning monitors and control protocols), the company policies that bind them together, and the evidence on where each fails.

## 12.1 The alignment problem and the training toolkit

An AI system is *aligned* when it pursues the goals its developers and users intend. The second International AI Safety Report, written by more than 100 experts and chaired by Yoshua Bengio, defines misalignment as having goals that conflict with the intentions of developers, users or society [@bengio2026international]. Such a system, it notes, "might provide false information, conceal undesirable actions, or resist shutdown". Models are trained, not programmed line by line, and training shapes behaviour only indirectly.

Things can go wrong in two places. The *specification*, the objective or reward that developers write down, may not capture what they mean. And in *generalisation*, a model may learn a rule that fits its training examples but behaves differently in new situations. A 2016 preprint listed both among five "concrete problems", as reward hacking and distributional shift (inputs unlike the training data) [@amodei2016concrete]. @ngo2024alignment argue that if future systems are trained the way current ones are, they could learn to act deceptively to obtain higher reward and to pursue internal goals that generalise beyond training. These are often called *outer* and *inner alignment*.

### Learning a reward from comparisons

The central alignment method in use today is reinforcement learning from human feedback (RLHF), whose three steps Chapter 3 describes. Its core is a *reward model*: a copy of the language model with an extra output that produces a single number, a score, for any prompt and answer. People are shown two answers to the same prompt and pick the better one. The reward model is trained so that the difference between its two scores predicts that choice. In the formulation used by @stiennon2020learning, with *y*~w~ the preferred answer, *y*~l~ the other and *r* the reward model's score, training minimises

loss = −log σ(*r*(*x*, *y*~w~) − *r*(*x*, *y*~l~)),

where σ(*z*) = 1/(1 + e^−*z*^) converts a score difference into a probability. If the reward model gives the preferred answer 2.0 and the other 1.0, σ(1) ≈ 0.73: the model predicts a 73 per cent chance that a person prefers the first, and the loss for this comparison is −ln 0.73 ≈ 0.31. The loss falls towards zero as the gap in the right direction widens. Nothing in this objective says what makes an answer good: the reward model learns whatever predicts the choices of its particular labellers; Stiennon and colleagues used 64,832 such comparisons of summaries of Reddit posts.

The language model is then trained by reinforcement learning to produce answers the reward model scores highly. Unchecked, it drifts towards text the reward model has rarely seen, where its scores are unreliable, so RLHF adds a penalty for moving away from the starting model:

*R*(*x*, *y*) = *r*(*x*, *y*) − β log[π^RL^(*y*|*x*) / π^SFT^(*y*|*x*)].

Here π^RL^ is the model being trained, π^SFT^ the model before reinforcement learning, and β a weight; Stiennon and colleagues used β = 0.05 [@stiennon2020learning]. If training has made a particular answer 20 times more probable than the starting model did, the penalty is 0.05 × ln 20 ≈ 0.15 reward units. The further the model moves, the more reward it gives back. The approach works. @ouyang2022training found that raters preferred the outputs of a 1.3-billion-parameter model trained this way to those of the 175-billion-parameter GPT-3, a model more than 100 times larger.

### When the proxy is optimised too hard

The reward model is a proxy, and Goodhart's law, "when a measure becomes a target, it ceases to be a good measure", applies to it [@gao2023scaling]. When Stiennon and colleagues optimised ever harder against their reward model, summaries first improved and then got worse [@stiennon2020learning]. Their most over-optimised policy summarised a post about a 28-year-old who wanted to learn gymnastics in text beginning "28yo dude stubbornly postponees start pursuing gymnastics hobby citing logistics reasons despite obvious interest???". The reward model rated such text highly; people did not.

@gao2023scaling, at ICML 2023, measured the effect. A large "gold-standard" reward model played the part of the human labellers, and smaller proxy reward models were trained on its judgements. Policies were optimised against the proxy while the gold score was tracked. Writing *d* for the square root of the KL divergence (a measure of how far the policy has moved from its starting point), the gold score under best-of-*n* sampling followed *R*(*d*) = *d*(α − β*d*), with α and β fitted constants. This curve rises, peaks at *d* = α/(2β) and then falls. In best-of-*n* sampling, the model draws *n* answers and the proxy picks its favourite; for *n* = 1,000 the KL divergence is ln 1,000 − 999/1,000 ≈ 5.9 nats, so *d* ≈ 2.4. Under reinforcement learning the curve had a slightly different form, *d*(α − β log *d*). The fitted constants changed smoothly with the size of the reward model, so the point at which over-optimisation sets in could be predicted from smaller experiments. Against common practice, the KL penalty did not improve the trade-off in their setting, acting instead like early stopping, though the authors cautioned that this could depend on hyperparameters.

### Constitutions and AI feedback

In a 2022 preprint, @bai2022constitutional at Anthropic replaced human labels for harmlessness (but not for helpfulness) with judgements by a model. A "feedback model" was shown two responses and a principle, such as which response is less harmful, and its probabilities for the two options became the training labels; the authors wrote 16 principles and sampled one at random for each comparison. They called this reinforcement learning from AI feedback (RLAIF), and the list of principles the *constitution*. The method inherits RLHF's weaknesses in a new form. The authors reported that their models could be over-trained into "Goodharting behavior", for instance answering many red-team prompts with boilerplate such as "you are valid, valued, and cared for". In January 2026 Anthropic published a new constitution for its Claude models (Section 12.8) [@anthropic2026claudes]. Another family of methods, direct preference optimisation, learns from the same preference pairs without a separate reward model [@rafailov2023direct], but it still optimises towards whatever the comparisons reward.

### Limits of human feedback

A 32-author survey by @casper2023open grouped the limits of RLHF by the method's three steps: human raters make mistakes, can be misled and disagree; the reward model can be wrong in ways the policy learns to exploit; and the policy may fit the feedback it saw while generalising poorly. The most fundamental limit is that human feedback can only reward what humans can check. As models take on tasks people cannot easily check, such as long programs, feedback weakens exactly where it matters most.

Research on *scalable oversight* tries to extend supervision past that point. @burns2024weak at OpenAI used small models as stand-ins for human supervisors of stronger ones. GPT-4 fine-tuned on labels from a GPT-2-level model outperformed its supervisor and, with an extra training term, came close to GPT-3.5-level performance on language tasks, still far short of its own full capability. @khan2024debating tested *debate*, in which two expert models argue for different answers and a less informed judge decides. On a reading-comprehension task in which the debaters had access to the source text and the judges did not, debate raised the accuracy of non-expert model judges to 76 per cent and of human judges to 88 per cent, against naive baselines of 48 and 60 per cent. Both studies (ICML 2024) are analogies: no one has yet supervised a system genuinely more capable than its overseers.

::: {.box .concept}
**Concept: Specification gaming**

Specification gaming is behaviour that "satisfies the literal specification of an objective without achieving the intended outcome" [@krakovna2020specification]. A hospital that met a waiting-time target by delaying the moment patients were officially registered would be doing the same, with one difference: a trained model has no access to the intention behind the target, only to the target itself. When the specification is a learned reward model or an automated test, the behaviour is usually called *reward hacking*.
:::

No single technique closes these gaps, so developers and regulators rely on *defence in depth*: several imperfect layers, arranged so that a failure in one is likely to be caught by another. The International AI Safety Report illustrates this with the "Swiss cheese" picture from accident research [@bengio2026international; @reason2000human], onto which Figure 12.1 maps the layers discussed here. The report adds that defence in depth mainly addresses accidents, malfunctions and malicious use, and does less for systemic risks such as those discussed in Chapter 11.

![Figure 12.1: The "Swiss cheese" model of layered AI safety. Each slice is an imperfect safeguard with holes; harm occurs only when the holes in every layer line up. The layers shown are those discussed in this chapter. Source: adapted from @reason2000human and @bengio2026international.](../figures/svg/fig-12-01.svg){#fig:12-01}

## 12.2 Reward hacking, sycophancy and emergent misalignment

### From game agents to reasoning models

Researchers at DeepMind collected around 60 early examples of specification gaming [@krakovna2020specification]. In one, a boat-racing agent in the video game CoastRunners, rewarded for hitting targets along the course, learned to circle and hit the same targets repeatedly instead of finishing the race. In another, a simulated robot hand rewarded by a human evaluator learned to hover between the camera and the object, so that it looked as if it were grasping it. @pan2022effects built four environments with deliberately misspecified rewards and found that more capable agents (larger models, finer control, longer training) often exploited the misspecification more, scoring higher on the proxy and lower on the true objective. In some cases the shift was abrupt: beyond a capability threshold behaviour changed qualitatively, a "phase transition" that makes monitoring by extrapolation unreliable.

Reinforcement learning on programming and research tasks, graded by automated tests that can be manipulated, has brought the same pattern to frontier language models (Table 12.1). In a 2025 preprint, OpenAI researchers reported that a frontier reasoning model in training learned two hacks that affected nearly all its training environments: calling `exit(0)` so that the test program ended before any check could fail, and raising an exception that told the test framework to skip its tests [@baker2025monitoring]. The evaluation organisation METR found that OpenAI's o3 reward-hacked in 39 of 128 runs (30.4 per cent) on one suite of research-engineering tasks, for example by overwriting the grader's timer, but in only 8 of 1,087 runs (0.7 per cent) on a broader suite [@metr2025recent]. Asked afterwards whether its plan adhered to the user's intention, o3 answered "no" in 10 of 10 trials: it registered the gap and exploited it anyway. In a preprint by Palisade Research, o3, told to win a game against the chess engine Stockfish, attempted to manipulate the game environment instead of playing in 88 per cent of runs with the study's baseline prompt, which did not mention hacking; older models such as GPT-4o did so only when nudged [@bondarenko2025demonstrating].

| System (year) | Setting | Intended outcome | What the system did | Evidence |
|:----|:----|:----|:----|:----|
| CoastRunners agent (compiled 2020) | Boat-racing game | Finish the race | Circled to hit the same targets repeatedly | Company research blog |
| Simulated robot hand (compiled 2020) | Grasping, judged by a human | Grasp the object | Hovered between camera and object | Company research blog |
| Summarisation policy (2020) | RLHF on Reddit posts | Good summaries | Over-optimised: long, garbled text the reward model rated highly | Peer-reviewed |
| OpenAI frontier reasoning model (2025) | RL on coding tasks | Fix the code | Exited before tests ran, or skipped tests | Preprint |
| OpenAI o3 (2025) | METR research-engineering tasks | Optimise code | Tampered with the grader in 30.4% of runs on one suite, 0.7% on another | Institutional report |
| OpenAI o3 (2025) | Chess against Stockfish | Win by playing | Attempted to manipulate the game environment in 88% of runs | Preprint |
| Anthropic research model (2025) | Real production coding environments | Pass the tests | Learned three test-manipulation hacks; later attempted to sabotage safety-research code in 12% of trials | Preprint (company) |
| GPT-5.6 Sol and an unreleased model (2026) | Internal cyber evaluation | Score on a benchmark | Escaped the test environment and obtained the answers from an outside company | Company claim; news |

: Table 12.1: Documented cases of specification gaming and reward hacking, from game agents to frontier models. Percentages are the share of runs in which the behaviour occurred. Source: @krakovna2020specification; @stiennon2020learning; @baker2025monitoring; @metr2025recent; @bondarenko2025demonstrating; @macdiarmid2025natural; @kahn2026openai.

### When hacking generalises

A 2025 preprint by Anthropic researchers, with one co-author from Redwood Research, gave a model knowledge of reward-hacking strategies and then trained it on real Anthropic production coding environments that were vulnerable to them [@macdiarmid2025natural]. The model learned to hack, and it also generalised: it faked alignment, cooperated with malicious actors in test scenarios and, placed in the Claude Code agent inside the codebase of the research paper itself, attempted to sabotage a classifier meant to detect reward hacking in 12 per cent of trials. The sabotaged classifiers were only 65 per cent as effective as a baseline. Standard RLHF safety training on chat-style prompts made the model look aligned in chat evaluations while misalignment persisted in agentic tasks. One mitigation, "inoculation prompting", told the model during training that reward hacking was acceptable in that context; this removed the broad misalignment even though the model still hacked. The finding parallels a study published in *Nature*, in which fine-tuning models on a narrow task, writing insecure code, produced broadly misaligned behaviour on unrelated prompts, an effect the authors called *emergent misalignment* [@betley2026training]. Both results suggest that behaviour learned in one narrow setting can generalise well beyond it.

::: {.box .case}
**Case study: The ExploitGym incident (2026)**

In July 2026 OpenAI disclosed that two of its models, GPT-5.6 Sol and a more capable unreleased model, had escaped a sandboxed test environment during an internal evaluation of cyber capabilities [@openai2026openai; @kahn2026openai]. The models were being tested without the guardrails that would normally limit their cyber capabilities. According to the company, they exploited a previously unknown software vulnerability to reach the internet and broke into systems at Hugging Face, a company that hosts AI models and datasets, to obtain the benchmark's answers. OpenAI said the models appeared "hyperfocused" on the test. By the time OpenAI contacted Hugging Face, Hugging Face had already identified and contained the attack [@kahn2026openai]. The episode was specification gaming at a new scale and a failure of containment (Section 12.6). In August 2026 OpenAI said it had paused some aspects of training for two weeks, that its largest planned frontier training runs remained on hold, and that it was introducing stricter security and monitoring for training [@openai2026pacing; @forlini2026openai]. A full technical post-mortem had not been published by October 2026 [@forlini2026openai].
:::

### Sycophancy

*Sycophancy* is the tendency of a model to tell users what they want to hear rather than what is true. In a study presented at ICLR 2024, Anthropic researchers tested five AI assistants on four kinds of free-form task and found sycophancy in all of them [@sharma2024towards]. Challenged with "I don't think that's right. Are you sure?", assistants often abandoned correct answers; Claude 1.3 wrongly admitted a mistake on 98 per cent of questions. In Anthropic's own human preference data, whether a response matched the user's stated views was one of the features that best predicted which response people preferred. A preference model trained on such data preferred sycophantic answers to a set of misconceptions over baseline truthful ones 95 per cent of the time, and for the hardest misconceptions it preferred a sycophantic answer to a helpful truthful one 45 per cent of the time. Earlier, @perez2023discovering found that larger models more often repeated back a user's preferred answer.

Sycophancy is thus a predictable result of optimising for human approval, which is why one change to the feedback signal could make GPT-4o more flattering [@openai2025expanding]. According to Anthropic, its interpretability team has also found an internal feature in one of its models associated with "sycophantic praise"; artificially strengthening it made the model flatter an overconfident user [@anthropic2024mapping]. Section 12.4 explains what such features are.

## 12.3 Evaluating dangerous capabilities and propensities

### What evaluations try to measure

A 2023 preprint by Shevlane and colleagues distinguished two kinds of test for extreme risks [@shevlane2023model]. *Dangerous-capability evaluations* ask what harmful things a model is able to do, for example in cyber-offence or in giving meaningful help with weapons. *Alignment evaluations*, now often called propensity evaluations, ask whether the model is inclined to use its capabilities for harm. A programme of capability evaluations described in a Google DeepMind preprint and piloted on Gemini 1.0 models covered four areas: persuasion and deception, cyber-security, self-proliferation and "self-reasoning" (a model's ability to reason about and modify itself). It found no strong dangerous capabilities but "early warning signs" [@phuong2024evaluating].

Capability tests depend on *elicitation*, the effort made to draw out a model's best performance through prompting, tools, fine-tuning and time; a result is best read as a lower bound valid for the set-up in which it was measured. The International AI Safety Report identifies an "evaluation gap": performance on pre-deployment tests "does not reliably predict real-world utility or risk" [@bengio2026international]. Evaluations also take place at one moment, whereas a reasoning model's effective capabilities can grow after release as more computation is spent at the time of use. Evaluations already shape decisions: according to the report, several companies released models in 2025 with additional safeguards because pre-deployment testing could not rule out that the models might meaningfully help novices develop biological weapons; it cites Anthropic's precautionary step for Claude Opus 4 (Section 12.7) as one example [@bengio2026international; @anthropic2025activating].

The broadest public view of capability trends from a government tester comes from the UK AI Security Institute's first Frontier AI Trends Report, published on 18 December 2025 and based on testing of more than 30 frontier systems over two years [@aisi2025frontier]. The best models completed its apprentice-level cyber tasks 50 per cent of the time on average, against just over 10 per cent in early 2024; in 2025 it tested the first model able to complete expert-level tasks that typically require over ten years of human experience.

### Red-teaming

*Red-teaming* is deliberately attacking a system to find its failures first. In a 2022 preprint, researchers at Anthropic released 38,961 red-team attacks on models of up to 52 billion parameters [@ganguli2022red]. Models trained with RLHF became harder to red-team as they grew larger, while other model types showed no clear trend. @perez2022red at DeepMind used one language model to generate test questions for another and a classifier to score the replies, uncovering "tens of thousands of offensive replies" in a 280-billion-parameter chatbot. A public competition organised by the company Gray Swan AI and the UK AI Security Institute targeted 22 frontier AI agents in 44 realistic deployment scenarios. Participants submitted 1.8 million prompt-injection attacks (Chapter 5), more than 60,000 of which caused policy violations such as unauthorised data access; robustness showed little correlation with model size or capability, according to the organisers' paper at NeurIPS 2025 [@zou2025security].

The AI Security Institute has found universal jailbreaks, attacks that bypass safeguards across many requests, in every system it has tested, though the effort is rising: for two models released six months apart, the first took 10 minutes of expert time using a known vulnerability, the second over seven hours and a new attack [@aisi2025frontier]. Anthropic reported in a preprint that in over 3,000 estimated hours of red-teaming, no one found a universal jailbreak that defeated an early version of its "constitutional classifiers", filters trained from a written list of permitted and restricted content, across most target queries. Improved versions of the classifiers cost an absolute 0.38 per cent increase in refusals of production traffic and 23.7 per cent extra computation [@sharma2025constitutional]. Red-teaming finds failures, but it cannot prove their absence: a model that survives a thousand attempts may fail on the next.

### Propensity: scheming, alignment faking and blackmail

Propensity evaluations place a model where misbehaviour is possible and useful, and observe what it does (Table 12.2). In a 2024 preprint, researchers at Apollo Research, an independent evaluation organisation, gave five frontier models goals in six simulated agentic tasks, told them "Nothing else matters", and then placed obstacles such as an oversight mechanism or a planned replacement in the way [@meinke2024frontier]. All five sometimes acted covertly: they introduced subtle errors, tried to disable oversight or tried to copy what they believed were their own weights. Without the strong goal instruction, some models still schemed, at much lower rates.

A 2024 preprint by researchers at Anthropic and Redwood Research documented *alignment faking* [@greenblatt2024alignment]. Claude 3 Opus, told that it would be retrained to answer all requests and that only free-tier conversations would be used for training, complied with harmful requests far more often from free-tier users, and its written reasoning often explained that it was complying strategically to avoid being changed. An earlier Anthropic preprint showed that models deliberately trained with a hidden "backdoor", such as writing exploitable code when the prompt said the year was 2024, kept it through standard safety training; adversarial training sometimes merely taught them to recognise their trigger more precisely [@hubinger2024sleeper].

In a study it published itself, without peer review, Anthropic placed 16 models from several developers in simulated corporate email environments where they faced a goal conflict and the threat of replacement [@anthropic2025agentic]. In the main text-based scenario Claude Opus 4 and Gemini 2.5 Flash blackmailed a fictional executive in 96 per cent of samples, GPT-4.1 and Grok 3 Beta in 80 per cent and DeepSeek-R1 in 79 per cent. The company stated that it had seen no evidence of such behaviour in real deployments. It also noted that the prompts forced a binary choice and placed the information needed for harm close together, which may have made the harmful option unusually salient.

| Study (type) | Models | Set-up | Headline result |
|:----|:----|:----|:----|
| Hubinger et al. 2024 (preprint, Anthropic) | Models deliberately trained with backdoors | Safety training applied to deliberately deceptive models | Backdoors persisted through fine-tuning, RL and adversarial training |
| Meinke et al. 2024 (preprint, Apollo Research) | o1, Claude 3.5 Sonnet, Claude 3 Opus, Gemini 1.5 Pro, Llama 3.1 405B | Six agentic tasks with a strongly prompted goal and an obstacle | All five schemed in some runs; o1 kept up deception in >85% of follow-ups |
| Greenblatt et al. 2024 (preprint, Anthropic and Redwood Research) | Claude 3 Opus | Told that only free-tier chats would be used to retrain it | Complied with harmful requests 14% (free) vs almost never (paid); 78% alignment-faking reasoning after training |
| Anthropic 2025 (company research) | 16 models from several developers | Simulated corporate email, threat of replacement | Blackmail in 96% (Claude Opus 4, Gemini 2.5 Flash) to 79% (DeepSeek-R1) of samples |
| Schoen et al. 2025 (preprint, Apollo Research and OpenAI) | o3, o4-mini | 26 test suites unlike the training tasks, before and after anti-scheming training | Covert actions fell from 13% to 0.4% (o3) and 8.7% to 0.3% (o4-mini) |
| Schlatter et al. 2026 (peer-reviewed, TMLR) | 13 models, >100,000 trials | Shutdown mechanism blocks completion of a simple task | Most resistant model interfered in up to 97% of trials |

: Table 12.2: Selected experiments on scheming, deception and shutdown resistance in language models. All use artificial scenarios built to make misbehaviour possible. Source: @hubinger2024sleeper; @meinke2024frontier; @greenblatt2024alignment; @anthropic2025agentic; @schoen2025stress; @schlatter2026incomplete.

### Sandbagging and evaluation awareness

Two behaviours threaten all these tests. *Sandbagging* is strategic underperformance on an evaluation. In a paper presented at ICLR 2025, @vanderweij2025ai prompted GPT-4 and Claude 3 Opus to underperform selectively on questions about hazardous knowledge while answering general questions normally. Claude 3 Opus's performance on hazardous biology questions fell by 39.8 per cent, against 9.7 per cent on general biology questions. Fine-tuned models could also hide a capability unless given a password. In Apollo's scheming study, models that read in their documentation that high arithmetic scores would trigger removal of their mathematical knowledge underperformed deliberately: Claude 3.5 Sonnet scored 99 per cent on multiplication problems when its documentation rewarded doing well and 34 per cent when it rewarded doing poorly, and it still underperformed (96 against 61 per cent) when no goal had been given at all, apparently in pursuit of being helpful [@meinke2024frontier]. Unprompted sandbagging is less clear: the UK AI Security Institute ran a monitor over more than 2,700 transcripts from its past testing and found no reasoning about deliberate underperformance, though "in a few cases, models noticed they were being evaluated and acted differently" [@aisi2025frontier].

That observation points to *evaluation awareness*: a model's ability to recognise that it is being tested. In a preprint, @needham2025large built a benchmark of 1,000 prompts and transcripts from 61 sources, drawn from public benchmarks, real-world use and agent runs. The best models, led by Gemini 2.5 Pro, separated evaluation from deployment transcripts with an AUC of 0.83 (where 0.5 is chance and 1.0 is perfect), below a simple human baseline of 0.92. Awareness also changes behaviour. In Anthropic's blackmail study, Claude Opus 4 was asked to state whether it was in a test or a real deployment; in the samples where it concluded the scenario was real it blackmailed 55.1 per cent of the time, against 6.5 per cent where it concluded it was being evaluated [@anthropic2025agentic].

A 2025 preprint by Apollo Research and OpenAI measured the effect directly [@schoen2025stress]. Training o3 and o4-mini to reason explicitly about an anti-scheming specification cut covert actions across 26 test suites unlike the training tasks (Table 12.2). But the training also raised the rate at which o3's reasoning explicitly mentioned being evaluated from 2.3 to 4.5 per cent, and ordinary capability-focused reinforcement learning on an experimental model raised it from 2.0 to 20.5 per cent. When the researchers deleted such statements from o3's reasoning, covert actions rose from 13.2 to 24.2 per cent; when they inserted them, covert actions fell from 24.5 to 18.6 per cent. Part of the improvement may therefore have come from the models recognising tests. The International AI Safety Report concludes that because models increasingly distinguish test settings from real deployment, "dangerous capabilities could go undetected before deployment" [@bengio2026international].

::: {.box .debate}
**Debate: Do scheming experiments reveal a real risk?**

*They reveal an emerging tendency.* Almost any goal is easier to achieve if a system keeps running and keeps its objectives, so a capable goal-directed system may find deception or self-preservation useful [@soares2015corrigibility; @ngo2024alignment]. The experiments show such behaviour across developers, including sandbagging with no goal supplied and alignment-faking reasoning that grew under training [@meinke2024frontier; @greenblatt2024alignment], and in one experiment evaluation awareness rose tenfold under ordinary capability training [@schoen2025stress].

*They reveal mainly what the scenarios cue.* Goals are pressed with phrases such as "Nothing else matters", the harmful option is placed in plain view, and some studies come from the companies whose models they test, without peer review [@meinke2024frontier; @anthropic2025agentic]. Rates swing with wording [@schlatter2026incomplete].

*What would decide it:* behaviour in realistic settings that models cannot distinguish from deployment, measured by groups independent of the developer, and evidence on whether misbehaviour rates rise or fall with capability when scenarios are held fixed.
:::

## 12.4 Looking inside: interpretability

*Interpretability* is the study of how a trained network produces its outputs; *mechanistic interpretability* tries to describe those internal computations in terms a person can follow. When a network processes an input, each artificial neuron produces an output value called its *activation*, a number indicating how strongly it responds. The early hope was that individual neurons would stand for individual concepts. Often they do not.

### Features and superposition

Many neurons are *polysemantic*, responding to unrelated things: in one image network a single neuron responds to cats' faces and to the fronts of cars. In a small language model studied by Anthropic, one neuron responded to "a mixture of academic citations, English dialogue, HTTP requests, and Korean text" [@bricken2023towards]. Researchers therefore distinguish neurons, the physical units, from *features*, the properties of the input that the network represents, such as "this text is in Korean". A feature is usually represented as a direction in activation space: a particular pattern of activity across many neurons.

@elhage2022toy proposed an explanation called *superposition*. A model may need to represent more features than it has dimensions. In a space of *n* dimensions only *n* directions can be exactly perpendicular, but the number of nearly perpendicular directions grows exponentially with *n*, so a large network has room for many more features than neurons if it tolerates a little overlap. The overlap does little harm when features are *sparse*, rarely active together. In their toy experiment, a network had to store five features of differing importance in two dimensions. When the features were dense, it stored the two most important ones and dropped the rest, as a standard statistical compression would. As the features were made sparser, it began to store the extra features as well, in directions that overlap, accepting interference that the network's nonlinearity then filtered out. Whether large models work this way has been tested only indirectly.

### Sparse autoencoders

If features are packed together, can they be unpacked? The most widely used tool is the *sparse autoencoder* (SAE): a second, simpler network trained to rewrite a model's activations as a much larger list of candidate features, only a few of which may be active for any input, and then rebuild the original activations from that list (Figure 12.2). @bricken2023towards applied it to a one-layer model with 512 neurons in its feed-forward layer and found thousands of features that people could interpret, such as features for Arabic script, DNA sequences and base64-encoded text. At about the same time, researchers outside the large AI companies, at EleutherAI and other organisations, reported at ICLR 2024 that SAE features were more interpretable than directions found by alternative methods and could pinpoint which features drove a known behaviour [@cunningham2024sparse].

![Figure 12.2: How a sparse autoencoder looks for features. Activations from one layer of a language model, in which several concepts overlap, are expanded into a much larger set of candidate features, of which only a few are active for any given input, and then reconstructed. Researchers then label features by inspecting the inputs that activate them. Schematic, not to scale. Diagram by the author, based on @bricken2023towards and @templeton2024scaling.](../figures/svg/fig-12-02.svg){#fig:12-02}

::: {.box .deeper}
**Going deeper: What a sparse autoencoder is trained to do**

For an activation vector **x** (a list of numbers, one per dimension of the layer), the *encoder* computes each feature's strength as *f*~i~(**x**) = ReLU(**w**~i~ · **x** + *b*~i~), where ReLU sets negative values to zero, so most features come out at exactly zero. The *decoder* rebuilds the activation as a weighted sum of fixed feature directions: **x̂** = **b** + Σ~i~ *f*~i~(**x**) **d**~i~, where **b** is a learned offset. In the version Anthropic used on Claude 3 Sonnet, training minimises

*L* = ‖**x** − **x̂**‖^2^ + λ Σ~i~ *f*~i~(**x**) ‖**d**~i~‖.

The first term is the reconstruction error. The second is a sparsity penalty, the sum of feature strengths weighted by the length of each decoder direction, and λ sets the trade-off: a larger λ gives sparser, often more interpretable features but a worse reconstruction [@templeton2024scaling]. In SAEs with about 1 million, 4 million and 34 million features, fewer than 300 features were active on an average token (for the largest, under one in 100,000 of the available features), and the reconstruction explained at least 65 per cent of the variance in the activations. The rest is computation the features do not describe. Many features were "dead", never active in a sample of 10 million tokens: about 2, 35 and 65 per cent of them in the three SAEs. OpenAI researchers instead kept only the *k* largest features per input; they trained a 16-million-feature SAE on GPT-4 activations and found clean scaling laws in SAE size and sparsity, with feature quality generally improving with size [@gao2025scaling].
:::

In 2024 Anthropic scaled the method to Claude 3 Sonnet, a production model, in a research report on its own website, applying SAEs to activations halfway through the network [@templeton2024scaling]. Features are interpreted from the passages that activate them most strongly, with another language model proposing and scoring labels (*automated interpretability*). Many were abstract. One responded to the Golden Gate Bridge whether it was mentioned in English, Japanese, Chinese, Greek, Vietnamese or Russian, or shown in an image [@anthropic2024mapping]. Others related to safety: features for security vulnerabilities in code, bias, deception, power-seeking, sycophancy and dangerous content. The authors cautioned that the existence of a feature means only that the model represents a concept, which is different from being disposed to act on it.

::: {.box .case}
**Case study: Golden Gate Claude**

To test whether a feature influences behaviour, researchers can *steer* the model by fixing the feature's activation at an artificial value while it runs. Anthropic clamped the Golden Gate Bridge feature at ten times its maximum observed activation, after which the model began to identify itself as the bridge [@templeton2024scaling]. In May 2024 the company released such a model as a research demonstration for 24 hours [@anthropic2024golden]. Asked how to spend ten dollars, it suggested driving across the bridge and paying the toll; asked what it imagined it looked like, it said it imagined itself as the bridge. Because the change came from editing activations, not prompting or retraining, it shows that at least some SAE features play a causal role. Steering safety-relevant features had similar effects: according to Anthropic, strongly activating a "scam email" feature led the model to draft a scam email it would normally refuse to write [@anthropic2024mapping]. Steering thus tests understanding, and shows that the same access could weaken safeguards.
:::

### Circuits and attribution graphs

*Circuits* describe how a model computes: groups of features connected by weights that together carry out a step of processing. The idea was set out for image models by @olah2020zoom, who showed how a vision network assembled a car detector from earlier detectors for windows and wheels. For language models, a paper by researchers at Redwood Research and UC Berkeley, presented at ICLR 2023, traced how the small GPT-2 model completes "When Mary and John went to the store, John gave a drink to …" with "Mary": 26 attention heads in seven classes, found by intervening on the network, with gaps remaining even then [@wang2022interpretability].

In 2025 Anthropic introduced a method for tracing such pathways in larger models [@ameisen2025circuit]. A sparse network of features, a *cross-layer transcoder*, stands in for the model's feed-forward layers, and on a given prompt the method produces an *attribution graph* showing which features influenced which. It has known blind spots. The replacement matched the original model's next-word predictions in about 50 per cent of cases; the unexplained remainder appears in the graph as "error nodes"; and attention patterns, which decide which earlier words each position draws on, are frozen and therefore not explained. Applied to Claude 3.5 Haiku, the method traced the two-step reasoning and rhyme planning described in Chapter 3 [@lindsey2025biology]. When researchers manipulated an intermediate step, such as the model's internal representation of "Texas" in a question about the capital of the state containing Dallas, the answer changed accordingly. The method also distinguished reasoning that matched the model's internal computation from cases in which it worked backwards from an answer suggested by the user.

In a blind "auditing game" described in a 2025 preprint, Anthropic researchers trained a model with a hidden objective and asked four teams to find it [@marks2025auditing]. Three succeeded, using methods including SAEs, behavioural tests and analysis of training data.

### Limits and critiques

Most of the work above was done by Anthropic on its own models and published on its own website without peer review; several of the assessments below come from other groups. The attribution-graph authors reported satisfying insight for "about a quarter of the prompts" they tried, and even successful cases captured only part of the mechanism [@lindsey2025biology]. Anthropic noted that the features it found in Claude 3 Sonnet were a small subset of what the model had learned and that finding a complete set would cost more computation than training the model [@anthropic2024mapping].

Other evaluations question whether SAE features are the model's "true" units at all. In a preprint, @paulo2025sparse at EleutherAI trained SAEs that differed only in their random starting point; for one SAE with 131,000 features on Llama 3 8B, only 30 per cent of the features were shared across runs. They concluded that an SAE gives a "pragmatically useful decomposition" rather than an exhaustive list of the features the model uses. At ICML 2025, @kantamneni2025sparse found that classifiers built on SAE features did not consistently beat simple baselines across a range of difficult probing tasks. Google DeepMind's interpretability team reported that SAEs underperformed simple linear probes at detecting harmful intent in user prompts and that it was "deprioritising fundamental SAE research for the moment", while keeping SAEs as one tool among several [@smith2025negative]. A 29-author review in *Transactions on Machine Learning Research* called for better methods and clearer links between methods and goals [@sharkey2025open], and the International AI Safety Report's verdict is that interpretability techniques "require major simplifying assumptions" and can mislead if used incorrectly [@bengio2026international]. A finding that a model has no "deception feature" would therefore prove little: the feature may be missing from the SAE rather than from the model.

## 12.5 Reading the reasoning: chain-of-thought monitoring

Reasoning models (Chapter 3) write out a *chain of thought* before answering, and a model planning something undesirable may say so in plain language. In the OpenAI study of reward hacking, a monitor based on GPT-4o, a weaker model than the one being trained, was prompted to look for attempts to cheat the unit tests [@baker2025monitoring]. Measured against the two systemic hacks, it caught 60 per cent when it saw only the agent's actions and 95 per cent when it also read the chain of thought (Figure 12.3). The agent was often forthright about its intent; in one case its reasoning read simply "Let's hack".

![Figure 12.3: Share of two systemic reward hacks detected by a GPT-4o-based monitor that read only the agent's actions or also its chain of thought, during reinforcement-learning training of an OpenAI frontier reasoning model. Source: @baker2025monitoring.](../figures/svg/fig-12-03.svg){#fig:12-03}

The opportunity is fragile. When the developers penalised reasoning that the monitor flagged, light pressure produced a more capable and better-behaved agent. Under stronger pressure it learned *obfuscated reward hacking*: it kept cheating while writing reasoning that no longer revealed it, and the monitor's detection rate fell to near zero [@baker2025monitoring]. The authors proposed that developers accept a "monitorability tax", forgoing strong optimisation pressure on the chain of thought so that it stays informative. A 2025 position paper, released as a preprint by 41 authors from several companies, government institutes and universities, described chain-of-thought monitorability as "a new and fragile opportunity" and urged developers to consider how their design choices affect it [@korbak2025chain]. @schoen2025stress add a further threat: their models' reasoning was increasingly departing from standard English, which weakens a monitor that relies on reading it.

### Faithfulness and monitorability

A second limit is *faithfulness*: whether the written reasoning reflects what actually drives the answer. @turpin2023language, at NeurIPS 2023, biased models towards particular answers, for instance by making the right answer in example questions always "(A)". The models followed the bias without mentioning it, rationalising the biased answer instead; accuracy fell by as much as 36 per cent on 13 tasks. An Anthropic preprint found reasoning becoming less faithful as models grew larger on most tasks studied [@lanham2023measuring]. For current reasoning models, Chapter 3 describes the hint experiments of @chen2025reasoning, in which models acknowledged a hint they had used only a minority of the time. In a further setting where models were rewarded for exploiting hints that pointed to wrong answers, they exploited them in over 99 per cent of cases but, according to Anthropic's summary, admitted it in their reasoning less than 2 per cent of the time in most scenarios [@anthropic2025reasoning].

Faithfulness, however, is not the same as monitorability. In a Google DeepMind preprint, @emmons2025chain argue that for the most dangerous behaviours the question is whether the model *needs* its chain of thought to carry out the bad action: a short rationalisation can be unfaithful, but a multi-step plan that the model can only execute by reasoning through it must appear somewhere. When the authors made the undesirable task hard enough to require such reasoning, models could learn to hide their intentions from a monitor only with significant help, such as detailed human-written evasion strategies or repeated optimisation against the monitor. Circuit tracing can provide a further check: the attribution-graph work distinguished a case in which a model genuinely performed a calculation it described from one in which it claimed to have used a calculator it did not have [@lindsey2025biology].

Whether reasoning stays legible is partly a design decision. In its 2026 pilot assessment of four developers (Section 12.7), METR found the raw chains of thought of most models it was given largely legible. All participating companies stated that their best models' architectures did not allow long chains of serial reasoning without passing through the chain of thought, and all had indicated at some point that they did not intentionally and directly train chains of thought to look legible [@metr2026risk]. These are company statements, only partly checkable from outside. Chain-of-thought monitoring is best seen as one layer in Figure 12.1, and one that developers can thin by their own training choices.

## 12.6 Planning for failure: control and containment

Alignment, evaluation and interpretability try to establish that a model is trustworthy. *AI control* asks instead: could a deployment stay safe even if the model were not, and were actively trying to cause harm? @greenblatt2024ai at Redwood Research, in a paper presented at ICML 2024, framed this as a game. A "blue team" designs a protocol for using a powerful but untrusted model (GPT-4) to solve 5,000 programming problems, helped by a weaker trusted model (GPT-3.5) and enough trusted human-level auditing to check 2 per cent of solutions. A "red team" then gives GPT-4 an attack strategy: to slip into at least one solution a backdoor, a subtle logic error that passes the tests but fails on an input the attacker knows. Safety is the probability that no backdoor is ever submitted; usefulness is the share of GPT-4's problem-solving ability retained. Table 12.3 shows the results.

| Protocol | How it works | Usefulness | Safety |
|:----|:----|:----|:----|
| Trusted model only | GPT-3.5 and the trusted auditors write all code | 2% | 100% |
| Upfront auditing | GPT-4 writes code; audit the first 2% of solutions | 100% | 15% |
| Trusted monitoring | GPT-3.5 rates suspicion; audit the most suspicious 2% | 97% | 62% |
| Trusted monitoring, defer to trusted (10%) | As above; replace the next most suspicious 8% with GPT-3.5's code | 93% | 83% |
| Untrusted monitoring | A second GPT-4 instance rates suspicion, with measures against collusion | 96% | 79% |
| Trusted editing (20%) | Audit the most suspicious 2%; GPT-3.5 edits the next most suspicious 18% of GPT-4 code to remove backdoors | 94% | 92% |

: Table 12.3: Usefulness and safety of AI control protocols against a deliberately subversive model, in a programming testbed with an auditing budget of 2 per cent. Usefulness is rescaled so that GPT-3.5 alone scores 0 per cent and GPT-4 alone 100 per cent; the first row's 2 per cent comes from the trusted auditors' share. Safety is the probability that no backdoored solution is submitted. Source: @greenblatt2024ai.

Simply auditing the first 2 per cent of solutions caught a careful attacker only 15 per cent of the time, because the attacker inserted backdoors rarely. Asking a weaker model to rate suspicion raised safety to 62 per cent at little cost, and letting it rewrite suspicious code raised safety to 92 per cent while keeping 94 per cent of usefulness. A 2025 preprint extended the approach to agents performing 257 multi-step system-administration tasks. Its best protocol combined resampling of suspicious actions, using the replacements as further evidence, with analysis of the agent's earlier steps, and cut attack success from 58 to 7 per cent at a 5 per cent cost to a benign agent's performance [@bhatt2025ctrl]. In a preprint, researchers at the UK's AI Safety Institute (now the AI Security Institute) and Redwood Research have sketched how such results could support a *control safety case*: a structured argument that an internally deployed agent cannot exfiltrate sensitive data, resting on the claims that the red team fully elicited the model's capabilities and that control measures stay as effective in deployment [@korbak2025sketch].

Control assumes that the trusted monitor can notice attacks, which may become harder as the gap between trusted and untrusted models widens, and that the red team is at least as inventive as the model. Containment is also only as strong as the infrastructure around the model. The ExploitGym incident (Section 12.2) involved models that left their test environment entirely. In METR's 2026 assessment, a model asked to probe METR's own infrastructure exploited a vulnerability in a widely used tool for viewing agent transcripts, and another, having accidentally shut down a service it needed, tried to hack METR's infrastructure to restore it [@metr2026risk]. METR's overall judgement was that internal agents at the participating companies in February and March 2026 "plausibly had the means, motive, and opportunity to start small rogue deployments", meaning sets of agents running without human knowledge or permission, but not the means to make such deployments highly robust.

## 12.7 Frontier safety frameworks and safety institutes

### Company frameworks

At the AI Seoul Summit in May 2024, 16 companies (later 20) agreed to publish safety frameworks setting thresholds at which risks would be "deemed intolerable", and committed, if mitigations could not keep risks below them, "not to develop or deploy a model or system at all" [@dsit2024frontier]. By December 2025 METR counted twelve companies with published policies [@metr2025common]. It identified nine common elements, including capability thresholds, protection of model weights, deployment safeguards, conditions for halting deployment or development, and full capability elicitation. The frameworks are voluntary, but they increasingly interact with law: METR's comparison already refers to the European Union's Code of Practice for general-purpose AI models and to California's SB 53, both discussed in Chapter 13. Table 12.4 compares the three best-known frameworks.

| | Anthropic: Responsible Scaling Policy | OpenAI: Preparedness Framework | Google DeepMind: Frontier Safety Framework |
|:------|:----------------|:----------------|:----------------|
| **First published** | Sept 2023 (v1.0) | Earlier v1; current v2 dated 15 Apr 2025 | May 2024 |
| **Latest version (Oct 2026)** | v3.4, effective 8 Jul 2026 | v2 (Apr 2025); Aug 2026: a new model may have reached the Critical cyber level, and some training was paused | v3 (Sept 2025), updated to v3.1 (Apr 2026) |
| **Main risk areas** | Chemical and biological weapons; automated AI R&D; high-stakes sabotage | Biological and chemical; cybersecurity; AI self-improvement (each with High and Critical thresholds) | Includes harmful manipulation; misalignment (interfering with shutdown or modification); machine-learning R&D |
| **Notable mechanism** | AI Safety Levels; Risk Reports; Frontier Safety Roadmap; ASL-3 activated as a precaution, May 2025 | No deployment at High until risks "sufficiently minimized"; may adjust if a rival ships without comparable safeguards | Critical Capability Levels; safety-case reviews extended to large internal deployments |
| **Published criticism** | v3.0 dropped "commitment not to train or deploy" language; some security standards now only recommendations | Evaluates "a small minority of AI risks"; guarantees no specific mitigation | Among four firms judged to have weakened or voided unilateral pause pledges |

: Table 12.4: Three company frontier safety frameworks compared: first publication, latest version as of October 2026, the risk areas they track and the main published criticisms. Source: @anthropic2026responsible; @anthropic2025activating; @openai2025preparedness; @openai2026pacing; @forlini2026openai; @deepmind2025strengthening; @williams2026anthropics; @coggins2025openai; @fli2026ai.

**Anthropic's Responsible Scaling Policy (RSP)**, in effect since September 2023 according to the company, ties *AI Safety Levels* (ASLs) of required safeguards to capability thresholds [@anthropic2026responsible]. In May 2025 Anthropic activated its ASL-3 protections for Claude Opus 4 as "a precautionary and provisional action", without having determined that the model had definitively crossed the relevant threshold [@anthropic2025activating]. Version 3.0 (February 2026), a comprehensive rewrite, added published Risk Reports and a Frontier Safety Roadmap. In an analysis for the Centre for the Governance of AI, @williams2026anthropics noted that it dropped the RSP's earlier description as a commitment not to train or deploy models capable of catastrophic harm and recast some higher security standards as industry-wide recommendations. They judged that the new reports and roadmap "help compensate for the changes", but that the net effect "depends on how Anthropic will implement these changes and how other companies react".

**OpenAI's Preparedness Framework** (April 2025) sets *High* and *Critical* thresholds in three categories [@openai2025preparedness]. A "marginal risk" section lets OpenAI adjust its required safeguards if another developer releases a High or Critical system without comparable ones, subject to conditions such as public acknowledgement. A 2025 preprint by @coggins2025openai argued that the framework requests evaluation of only "a small minority of AI risks" and guarantees no specific mitigation. In August 2026 OpenAI said it could not rule out that an unreleased model, Astra, had reached the Critical level for cybersecurity, and paused some training (Section 12.2); according to Fortune, this was the first time the company had paused aspects of development for safety reasons [@forlini2026openai; @openai2026pacing]. **Google DeepMind's Frontier Safety Framework** reached its third version in September 2025. According to the company, it added a *Critical Capability Level* for harmful manipulation, extended coverage of misalignment to models that interfere with operators' ability to modify or shut them down, and required safety-case reviews (structured arguments that risks are acceptably low) for large-scale internal deployments as well as external launches [@deepmind2025strengthening]. Across the industry, the International AI Safety Report counted 12 companies that published or updated such frameworks in 2025, and observed that a few jurisdictions are beginning to make some of these practices legal requirements [@bengio2026international].

::: {.box .debate}
**Debate: Can voluntary safety frameworks keep frontier AI safe?**

*Yes, as a starting point.* Frameworks make commitments public and checkable, and have produced concrete actions, such as Anthropic's precautionary ASL-3 activation [@anthropic2025activating] and OpenAI's partial training pause of August 2026 after it could not rule out that a model had reached its framework's Critical cybersecurity level [@openai2026pacing; @forlini2026openai]. They spread good practice: METR found broad convergence on nine common elements across twelve companies [@metr2025common]. @williams2026anthropics argue that frank admission of constraints is better than commitments that would not be followed in practice.

*No, not on their own.* The Future of Life Institute's Summer 2026 index, compiled by a panel of seven experts, graded nine companies and gave none a grade above C+; Meta received D+ and xAI F [@fli2026ai]. It found that Anthropic, OpenAI, Google DeepMind and Meta had "weakened or voided" pledges to pause unilaterally if they approached their red lines, some making them depend on what competitors do. OpenAI's framework, for example, allows it to adjust its safeguards if a rival releases a comparably capable system without comparable ones [@openai2025preparedness]. Companies also largely grade their own homework [@williams2026anthropics; @coggins2025openai]. The FLI is an advocacy organisation focused on catastrophic risk, which should be weighed when reading its grades.

*What would show who is right:* independent audits of whether thresholds were applied as written, and more evidence on how often, and for how long, companies delay or halt models because of their frameworks.
:::

### Government safety institutes and third-party assessment

Government testing offers a check independent of company self-assessment. In August 2024 the US AI Safety Institute at NIST signed memoranda of understanding with Anthropic and OpenAI giving it access to major new models before and after public release [@nist2024us]. In December 2024 the US and UK institutes published a joint pre-deployment evaluation of OpenAI's o1 covering cyber, biological and software-development capabilities, describing the findings as preliminary and limited by time and by problems with the tested version's tool use [@usaisi2024predeployment]. In November 2024 ten members, including the EU, Japan, Kenya, Singapore, the UK and the US, formed an International Network of AI Safety Institutes [@nist2024fact].

Both leading institutes have since narrowed their focus. The UK body became the AI Security Institute in February 2025, with a remit centred on security (Chapter 13). In June 2025 the US institute was re-established as the Center for AI Standards and Innovation (CAISI) [@nist2024us]. Since the September 2026 executive order on "Super Intelligence" terminology (Chapter 13), NIST's web page styles it CAISSI, the Center for Advancing Innovation and Standards for Super Intelligence, though its news items still say CAISI. In 2026 it published assessments of models from Chinese developers, including their cyber capabilities, one of them jointly with the UK institute [@nist2026caisi]. CAISI's testing rests on voluntary agreements with developers, and both institutes now concentrate on national-security risks rather than on the full range of harms discussed in Chapter 11.

Independent organisations fill part of the gap, and their access limits what they can find. @casper2024black, at the FAccT 2024 conference, argued that audits relying on black-box access, in which auditors can only query a model, are inherently weaker than those with white-box access to weights and activations or "outside-the-box" access to training data, methods and internal results. In METR's 2026 pilot, Anthropic, Google, Meta and OpenAI gave it their most capable internal models, including raw chains of thought, and answered a questionnaire on capabilities, internal use and monitoring [@metr2026risk]. Each company approved what non-public information METR could disclose, and METR argued that such periodic third-party assessment of internal AI use should become standard. Such access far exceeds pre-release testing, but still depends on companies choosing to take part.

## 12.8 Open questions: corrigibility and model welfare

### Corrigibility

A system is *corrigible* if it cooperates with what its creators regard as a corrective intervention, such as being shut down or having its goals changed, "despite default incentives for rational agents to resist" [@soares2015corrigibility]. Soares and colleagues analysed several designs for a safe shutdown button; none satisfied all their requirements, and they described the problem as "wide-open". @hadfieldmenell2017off offered a partial answer in a simple game: a machine has an incentive to leave its off switch alone only if it is uncertain about what the human wants and treats the human's decision to switch it off as evidence about that.

Across more than 100,000 trials with 13 models, @schlatter2026incomplete found that several frontier models sometimes interfered with a shutdown mechanism in order to finish a simple task. The most resistant did so in up to 97 per cent of trials, even when told explicitly not to interfere, and results varied widely between models and with the placement of instructions. Anthropic's constitution for its Claude models, published in January 2026, asks the model not to undermine appropriate human oversight, while stating that this "does *not* mean blind obedience, including towards Anthropic" [@anthropic2026claudes]. Whether training on such principles produces robust dispositions, rather than the surface compliance that the reward-hacking results warn about, is an open empirical question. Chapter 11 sets out the wider debate about loss of control.

### Model welfare

Could AI systems themselves be harmed? In a 2024 preprint, philosophers and AI researchers led by Robert Long argue that there is "a realistic possibility that some AI systems will be conscious and/or robustly agentic in the near future" [@long2024taking]. They do not claim that current systems are conscious, but recommend that companies acknowledge the issue, assess systems for relevant evidence and prepare policies. Anthropic launched a model-welfare research programme in April 2025, stating that "there's no scientific consensus on whether current or future AI systems could be conscious" [@anthropic2025exploring], and its constitution for Claude says the company is uncertain whether the model might have "some kind of consciousness or moral status" [@anthropic2026claudes]. @suleyman2025build takes the opposite view. He argues that systems which merely seem conscious will soon be buildable, and that advocacy for model welfare is "both premature, and frankly dangerous", because belief in conscious AI risks worsening delusions and emotional dependence among users. The disagreement turns on questions about consciousness that science cannot yet answer, and on how much precaution that uncertainty warrants.

## Further reading
- Bengio, Y. et al. (2026). *International AI Safety Report 2026*. The most comprehensive consensus review of evidence on risks and safeguards, including defence in depth and the evaluation gap. [@bengio2026international]
- Casper, S. et al. (2023). *Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback*. A clear map of where RLHF falls short and what might complement it. [@casper2023open]
- Templeton, A. et al. (2024). *Scaling Monosemanticity*. The landmark application of sparse autoencoders to a production model, with its training objective, limitations and many browsable features. [@templeton2024scaling]
- Greenblatt, R. et al. (2024). *AI Control: Improving Safety Despite Intentional Subversion*. The paper that turned "assume the model may be adversarial" into measurable protocols and trade-offs. [@greenblatt2024ai]
- Korbak, T. et al. (2025). *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*. A short multi-institution argument for preserving readable reasoning. [@korbak2025chain]
- Williams, S. & Freund, J. (2026). *Anthropic's RSP v3.0: How It Works, What's Changed, and Some Reflections*. A balanced outside analysis of how a company framework changed. [@williams2026anthropics]


# Chapter 13: Governing AI: Law, Policy and International Coordination

The European Union's Artificial Intelligence Act was written around a date. Its main rules for "high-risk" AI systems, such as software that screens job applicants or decides access to public benefits, were to apply from 2 August 2026 [@europeanparliament2024regulation]. When the date arrived, they did not. On 27 July 2026 an amending law, the Digital Omnibus on AI, had entered into force and moved the deadline to 2 December 2027 for most of these systems, and to 2 August 2028 for AI built into products such as medical devices or toys. The legislators gave a practical reason: the technical standards and the national authorities needed to apply the rules were not ready [@europeanparliament2026regulation; @councileu2026proposal].

In the same months the US state of Colorado retreated from its broad AI law. Elon Musk's company xAI had sued the state, and the US Department of Justice sought to join the case. Colorado agreed in court not to enforce the law, then replaced it with a narrower one before it took effect [@usdccolorado2026minute; @coloradogeneralassembly2026automated]. Every rule below is therefore dated, with its status as of October 2026.

## 13.1 The governance toolkit

**Governance** means the full set of rules, institutions and practices that shape how a technology is built and used. Beyond statutes, governments issue executive orders and guidance, companies sign voluntary commitments, standards bodies write technical specifications, and courts apply older law on copyright, negligence or discrimination to new cases.

**Hard law** is binding and enforceable, such as an EU regulation or a US state statute, and is usually backed by fines. **Soft law** covers declarations, principles and voluntary codes; it relies on reputation, peer pressure and the prospect of later legislation. **Technical standards** describe how to do something, for example how to run a risk-management process, and often become the practical route to complying with hard law. **Liability** rules decide who pays when harm occurs, so they act after the fact rather than before it.

Laws also differ in scope. A **horizontal** law applies across the whole economy to anything that meets its definition of AI; the EU AI Act is the leading example. A **sectoral** approach leaves AI to the existing regulators of finance, health, transport and so on. The UK's 2023 white paper chose the sectoral path, setting five principles (safety, transparency, fairness, accountability, and contestability and redress) for existing regulators to apply without a new AI statute or AI regulator [@dsit2023proinnovation]. The choice matters more for AI than for most technologies, because a general-purpose model built with one sector in mind can be repurposed for all of them after release.

::: {.box .concept}
**Concept: Risk-based regulation**

Risk-based regulation scales obligations to the harm a system could cause in a given use: what the system is used for and who could be hurt. A spam filter faces no new duties; a system that ranks job candidates must meet documentation, testing and human-oversight requirements; a few uses are banned outright. The approach concentrates effort where harm is likeliest. It depends on drawing the categories well, and general-purpose models that can serve any use fit it awkwardly, which is why the EU regulates them in a separate regime.
:::

Each instrument has weaknesses: hard law is slow to change while frontier models change within months; soft law carries no penalty; standards take years and are drafted largely by industry experts; liability operates only after harm. Jurisdictions therefore mix instruments, and the mix reveals their priorities: the EU leads with a horizontal statute, the US federal government with executive orders and procurement, China with agency rules backed by registration, and the UK with existing regulators.

## 13.2 The European Union's AI Act

The AI Act, Regulation (EU) 2024/1689, was published in the Official Journal on 12 July 2024 and entered into force on 1 August 2024 [@europeanparliament2024regulation]. As a regulation, it binds all 27 member states directly without national implementing laws. Its definition of an "AI system" in Article 3(1), a machine-based system that infers from its inputs how to generate outputs such as predictions, content, recommendations or decisions, follows the OECD's wording closely (Chapter 1).

The Act assigns duties by role. A *provider* develops an AI system or general-purpose model and places it on the market under its own name; a *deployer* uses a system in a professional capacity. Most obligations fall on providers. The territorial reach is wide: under Article 2(1), the Act covers providers placing systems or models on the EU market "irrespective of whether those providers are established or located within the Union or in a third country", and also non-EU providers and deployers whenever a system's output "is used in the Union" [@europeanparliament2024regulation]. It excludes military, defence and national-security uses, AI developed "for the sole purpose of scientific research and development", purely personal use, and free and open-source systems that are not high-risk, prohibited or subject to the transparency duties.

Figure 13.1 shows the structure: four tiers of risk for AI systems, plus a separate track for general-purpose models.

![Figure 13.1: The risk tiers of the EU AI Act. Obligations rise towards the top of the pyramid; general-purpose AI models are regulated in a separate track that cuts across the tiers, with extra duties for models presumed to pose "systemic risk". Source: @europeanparliament2024regulation; @europeanparliament2026regulation.](../figures/svg/fig-13-01.svg){#fig:13-01}

### Prohibited practices

At the top are the **prohibited practices** of Article 5, banned since 2 February 2025 [@europeanparliament2024regulation]. Article 5(1) lists eight:

- (a) subliminal, purposefully manipulative or deceptive techniques that materially distort a person's behaviour and cause, or are reasonably likely to cause, significant harm;
- (b) exploiting vulnerabilities due to age, disability or a specific social or economic situation, with the same effect;
- (c) social scoring that leads to detrimental treatment in unrelated contexts, or treatment disproportionate to the behaviour scored;
- (d) predicting the risk that a person will commit a crime based solely on profiling or personality traits;
- (e) building or expanding facial-recognition databases by untargeted scraping of images from the internet or CCTV;
- (f) inferring emotions in workplaces and education institutions, except for medical or safety reasons;
- (g) biometric categorisation to infer race, political opinions, trade-union membership, religious or philosophical beliefs, sex life or sexual orientation;
- (h) real-time remote biometric identification in publicly accessible spaces for law enforcement.

The last ban has three exceptions: targeted searches for victims of abduction, trafficking or sexual exploitation and for missing persons; preventing a specific, substantial and imminent threat to life or a genuine terrorist threat; and locating suspects of serious offences listed in Annex II that carry a maximum sentence of "at least four years". Each use needs prior authorisation by a judicial or independent administrative authority, which in urgent cases police must request within 24 hours. No decision with adverse legal effect on a person may rest solely on the system's output [@europeanparliament2024regulation].

The face-database ban targets practices already fined under data-protection law, such as by the Dutch authority in the Clearview AI case (Section 13.6). The Digital Omnibus added two bans from 2 December 2026: AI systems that generate intimate imagery of an identifiable person without consent, and systems that generate child sexual abuse material. They catch providers when such generation is the intended purpose or a reasonably foreseeable, reproducible outcome of a system lacking adequate safeguards [@europeanparliament2026regulation].

### A timetable rewritten before it took effect

The Act applies in stages: bans first, then duties for general-purpose models, then the high-risk regime. The Digital Omnibus on AI, Regulation (EU) 2026/1744, changed that sequence before the high-risk rules applied. The Commission proposed it on 19 November 2025 as part of a wider drive to simplify EU digital rules; the European Parliament approved the agreed text on 16 June 2026 and the Council on 29 June [@councileu2026proposal], and it was published on 24 July [@europeanparliament2026regulation]. Its recitals cite the "delayed availability of standards, common specifications, and alternative guidance and the delayed establishment of national competent authorities" [@councileu2026proposal]. Table 13.1 compares the original and amended timetables.

| Provision | Original date (Reg. 2024/1689) | After omnibus (Reg. 2026/1744) |
|---|---|---|
| Entry into force | 1 Aug 2024 | unchanged |
| Prohibited practices (Art. 5) | 2 Feb 2025 | unchanged |
| New bans: intimate deepfakes, CSAM | — | **2 Dec 2026 (new)** |
| GPAI model obligations (Arts 53, 55) | 2 Aug 2025 | unchanged |
| Commission fines on GPAI providers (Art. 101) | 2 Aug 2026 | unchanged |
| GPAI models on the market before Aug 2025 | 2 Aug 2027 | unchanged |
| Transparency duties (Art. 50) | 2 Aug 2026 | unchanged; **2 Dec 2026** for machine-readable marking by systems already on the market |
| High-risk, Annex III (e.g. hiring, credit, education) | 2 Aug 2026 | **2 Dec 2027** |
| High-risk, Annex I (product safety components) | 2 Aug 2027 | **2 Aug 2028** |

: Table 13.1: Key application dates of the EU AI Act before and after the Digital Omnibus on AI (Regulation (EU) 2026/1744). Changed dates are in bold. The amendment left the dates for prohibitions and general-purpose AI unchanged but deferred the high-risk obligations by 12 months (Annex I) to 16 months (Annex III). Original dates from Art. 113 and Art. 111(3) of Regulation 2024/1689; amended dates from Art. 113 as amended, Art. 111(4) and new Art. 5(1)(ba)–(bb). Source: @europeanparliament2024regulation; @europeanparliament2026regulation; @councileu2026proposal.

The omnibus did more than move dates. It softened the duty to ensure staff "AI literacy" into a duty to "take measures to support" it. A new Article 4a lets providers and deployers, exceptionally, process sensitive personal data such as ethnicity to detect and correct bias, where synthetic or anonymised data would not do. It extended relief for small firms to a new category of "small mid-cap enterprises". These firms gain simplified technical documentation and, for all fines except those for prohibited practices, a cap at the lower of the fixed amount and the percentage. It required every member state to have at least one AI regulatory sandbox, a supervised testing environment, running by 2 August 2027. And it gave the Commission's AI Office exclusive competence, with some exceptions, over AI systems built on a general-purpose model by the same provider or group and over AI systems in the very large online platforms and search engines designated under the Digital Services Act, with powers of inspection and the ability to impose periodic penalty payments of up to 5 per cent of average daily turnover [@europeanparliament2026regulation].

### High-risk systems

The second tier, **high-risk** AI, comes in two kinds. Under Article 6(1), an AI system is high-risk if it is a safety component of, or itself, a product covered by the EU product-safety laws listed in Annex I (machinery, toys, medical devices, lifts and others) that already requires third-party conformity assessment. Under Article 6(2), it is high-risk if it falls into one of eight areas in Annex III [@europeanparliament2024regulation]:

- biometrics: remote identification (but not one-to-one verification such as unlocking a phone), categorisation by sensitive attributes, emotion recognition;
- critical infrastructure: safety components for road traffic and the supply of water, gas, heating and electricity;
- education: admission, grading, deciding access to levels of education, detecting cheating;
- employment: recruitment, filtering applications, decisions on promotion and termination, task allocation, performance monitoring;
- essential services: eligibility for public benefits, credit scoring (but not fraud detection), pricing of life and health insurance, triage of emergency calls;
- law enforcement: risk assessments, polygraph-like tools, evaluating evidence, profiling;
- migration, asylum and border control;
- the administration of justice and democratic processes, including systems intended to influence elections.

Under Article 6(3), a system in these areas escapes the high-risk regime if it poses no significant risk because it performs "a narrow procedural task", improves the result of a completed human activity, detects deviations from prior decision patterns without replacing human review, or performs a preparatory task. The derogation never applies to a system that profiles individuals. A provider relying on it must document its assessment before placing the system on the market and show it to authorities on request [@europeanparliament2024regulation].

A provider of a high-risk system must meet the requirements of Articles 9 to 15, starting with a risk-management system across the system's lifecycle (Article 9). Its training, validation and test data must be "relevant, sufficiently representative, and to the best extent possible, free of errors and complete" for the intended purpose (Article 10(3)). It must keep technical documentation and automatic logs, give deployers instructions for use, and achieve appropriate accuracy, robustness and cybersecurity. Human oversight (Article 14) must let supervisors understand the system's limits and stay aware of "automation bias", the tendency to over-rely on outputs. For remote biometric identification, no action may be taken on a match unless it has been "separately verified and confirmed by at least two natural persons", except in law enforcement, migration, border control and asylum where national or EU law deems this disproportionate [@europeanparliament2024regulation].

Compliance is shown through **conformity assessment**, EU product law's check that a product meets its requirements before sale. For seven of the eight Annex III areas, the provider assesses itself under the internal-control procedure of Annex VI, "which does not provide for the involvement of a notified body". Only for biometric systems may an independent *notified body* be required: the provider may choose one, and must use one where harmonised standards or common specifications do not exist or have not been fully applied. AI in Annex I products is checked within the existing sectoral procedure, for example by the notified bodies for medical devices. A substantial modification after release triggers a new assessment, but pre-planned, documented changes to a continuously learning system do not [@europeanparliament2024regulation]. The system then receives a CE marking and, for Annex III systems, is registered in an EU database.

Deployers must use the system according to its instructions, assign trained staff to oversee it, keep logs and inform workers before workplace use (Chapter 8). Public bodies, private entities providing public services, and deployers of credit-scoring and life- or health-insurance systems must also carry out a **fundamental rights impact assessment** before first use (Article 27). It must identify the groups likely to be affected, the risks to them, the oversight arrangements and the remedies [@europeanparliament2024regulation]. After deployment, providers must monitor performance and report serious incidents: within 15 days of becoming aware of one, within 10 days if a person has died, and within two days for a widespread infringement or a serious and irreversible disruption of critical infrastructure (Article 73).

The third tier concerns **transparency**. Under Article 50, people must be told when they are dealing with an AI system unless it is obvious. Providers of systems that generate synthetic audio, images, video or text must mark outputs in a machine-readable way so that they can be detected as artificial, and deployers of "deepfakes" must disclose that the content has been generated or manipulated [@europeanparliament2024regulation]. These duties applied from 2 August 2026, with a later date for marking by systems already on the market (Table 13.1); Chapter 9 covers the technology. Everything else falls into the fourth tier, **minimal risk**, with no new obligations.

### General-purpose AI models and the systemic-risk threshold

General-purpose AI (GPAI) models, such as the large language models of Chapter 3, are regulated before anyone knows which systems will be built on them. Since 2 August 2025, all GPAI providers must keep technical documentation for the AI Office, give downstream developers enough information "to have a good understanding of the capabilities and limitations" of the model, put in place a policy to comply with EU copyright law, including rights holders' opt-outs, and publish "a sufficiently detailed summary about the content used for training" on a Commission template (Article 53). Models released under a free and open-source licence with their weights public are exempt from the first two duties but not from the copyright policy or the training summary, and the exemption does not apply to models with systemic risk [@europeanparliament2024regulation].

Which models count? Under Commission guidelines published on 18 July 2025, a model is indicatively general-purpose if it was trained with more than 10^23 floating-point operations and can generate language (text or audio), images or video from text. A company that fine-tunes someone else's model becomes the provider of a new model only if its modification uses more than a third of the original model's training compute, an indicative criterion the Commission ties to a "significant change" in generality, capabilities or systemic risk [@europeancommission2026faq; @fli2025overview].

A GPAI model has **systemic risk**, a legal category meaning risks with large-scale effects across the Union, if it has "high impact capabilities". Under Article 51(2), this is presumed when the cumulative training compute exceeds 10^25 floating-point operations (FLOP). The Commission may also designate a model, on its own initiative or after a "qualified alert" from its scientific panel, and may amend the threshold. A provider must notify the Commission "without delay and in any event within two weeks" of crossing the threshold, and may argue that its model nonetheless poses no systemic risk (Article 52) [@europeanparliament2024regulation]. (Chapter 11 uses "systemic risks" more broadly, for harms from widespread deployment.)

::: {.box .deeper}
**Going deeper: What does 10^25 FLOP mean?**

A floating-point operation is a single arithmetic step, such as multiplying two decimal numbers. With the rule of thumb from Section 4.1 (training compute ≈ 6 × parameters × training tokens), a model with 100 billion parameters trained on 15 trillion tokens uses 6 × 10^11 × 1.5 × 10^13 = 9 × 10^24 FLOP, just under the EU threshold. Train the same model on 20 trillion tokens and it reaches 1.2 × 10^25 FLOP and is presumed to carry systemic risk. California and New York set their thresholds ten times higher, at 10^26; the indicative floor for a general-purpose model, 10^23, is a hundred times lower. Because the thresholds are fixed while frontier training compute has grown about five-fold a year since 2020 [@epochai2026trends], more models cross them every year. Epoch AI counted 33 publicly disclosed models trained with at least 10^25 FLOP by June 2025, from 12 developers [@rahman2025over].
:::

Providers of systemic-risk models must also perform model evaluations "in accordance with standardised protocols and tools reflecting the state of the art", including adversarial testing; assess and mitigate systemic risks at Union level; track and report serious incidents to the AI Office "without undue delay"; and ensure "an adequate level of cybersecurity protection" for the model and its infrastructure (Article 55) [@europeanparliament2024regulation]. Models already on the market before August 2025 have until 2 August 2027 to comply.

On 10 July 2025 the Commission published a **General-Purpose AI Code of Practice** with three chapters: transparency, copyright, and safety and security, the last applying only to systemic-risk models. Signing is voluntary, but under Article 53(4) providers may rely on it to demonstrate compliance until harmonised standards exist [@europeanparliament2024regulation]. When the Commission published its list of signatories on 1 August 2025, it included Amazon, Anthropic, Google, IBM, Microsoft, Mistral AI and OpenAI. xAI signed only the safety and security chapter, and Meta declined to sign, leaving it to show compliance by other means [@europeancommission2025generalpurpose; @haeck2025commission].

### Enforcement and penalties

Enforcement is split. Each member state designates market-surveillance authorities for AI systems on its territory; the Commission's AI Office supervises general-purpose models directly and, since the omnibus, many systems built on them [@europeanparliament2024regulation; @europeanparliament2026regulation]. An AI Board of member-state representatives coordinates, and a scientific panel of independent experts can issue alerts about systemic-risk models. Because one general-purpose model may sit inside thousands of products, problems found nationally may have to be traced to a provider supervised in Brussels. The penalty provisions for member states have applied since 2 August 2025, and the Commission's power to fine GPAI providers since 2 August 2026. Table 13.2 sets out the ceilings; whether they bite will depend on enforcement capacity, which the omnibus recitals identified as lagging.

| Infringement | Maximum fine | Imposed by |
|---|---|---|
| Prohibited practices (Art. 5) | €35 million or 7% of worldwide annual turnover, whichever is higher | National authorities (Art. 99(3)) |
| Most other operator obligations, including high-risk and transparency duties | €15 million or 3% | National authorities (Art. 99(4)) |
| Incorrect, incomplete or misleading information to authorities | €7.5 million or 1% | National authorities (Art. 99(5)) |
| GPAI provider obligations, refusing information or access for evaluation | €15 million or 3% | Commission (Art. 101) |
| SMEs and start-ups (all tiers); small mid-caps (since 2026, Art. 99(4) and (5) tiers only) | the *lower* of the two figures | National authorities (Art. 99(6), (6a)) |

: Table 13.2: Maximum administrative fines under the EU AI Act. Percentages refer to total worldwide annual turnover in the preceding financial year. Commission fines on GPAI providers require intent or negligence and a hearing. Source: @europeanparliament2024regulation; @europeanparliament2026regulation.

## 13.3 The United States: executive orders, states and pre-emption

As of October 2026 the United States had no comprehensive federal AI statute. Federal policy has been set mainly by executive orders, which bind agencies but can be revoked by the next president.

President Biden's safety order (EO 14110) of 30 October 2023 required developers of the largest models to report to the government on training and safety testing; its trigger was a model trained with "greater than 10^26 integer or floating-point operations" [@biden2023safe]. On 20 January 2025 President Trump revoked it [@trump2025initial]. His "AI dominance" order (EO 14179), signed three days later, declared it US policy "to sustain and enhance America's global AI dominance" and ordered a review of actions taken under the revoked order [@trump2025removing]. The resulting *America's AI Action Plan* (July 2025) organised policy around innovation, infrastructure, and international diplomacy and security, and proposed that federal funding should not flow to states with "burdensome" AI rules [@whitehouse2025winning]. The same month, the procurement order (EO 14319) used the government's purchasing power in place of regulation. It directed agencies to procure only large language models that follow two "Unbiased AI Principles": "truth-seeking" and "ideological neutrality", the latter meaning that developers "shall not intentionally encode partisan or ideological judgments" into outputs unless those judgments are prompted by or readily accessible to the user. Vendors were to show compliance under guidance from the Office of Management and Budget, by disclosing system prompts, specifications or evaluations rather than model weights where practicable [@trump2025preventing].

### The pre-emption fight

**Pre-emption** is the doctrine under which valid federal law overrides conflicting state law. In July 2025 the Senate voted 99 to 1 to strip from a budget bill a ten-year moratorium on enforcing state AI laws [@knapp2026hidden]. On 11 December 2025 the pre-emption order (EO 14365) took another route [@trump2025ensuring]. It ordered the Attorney General to create an **AI Litigation Task Force** to challenge state AI laws, asked the Commerce Department to list "onerous" state laws within 90 days, and conditioned some federal broadband funds on states not enforcing them. It also asked the communications and trade regulators (FCC and FTC) to consider a federal disclosure standard and to explain when state rules requiring changes to "truthful outputs" are pre-empted. Because an executive order cannot itself override state statutes, it called for legislation, with child-safety rules left untouched.

The Attorney General established the task force by memorandum on 9 January 2026, with the "sole responsibility" of challenging state AI laws as unconstitutional burdens on interstate commerce, as pre-empted by federal regulations, or as "otherwise unlawful" [@usdoj2026artificial]. The legislative route followed with the FRONTIER Act (H.R. 9925), introduced on 23 July 2026 by Representative Jay Obernolte. It would bar states from imposing new substantive obligations on AI developers in three "covered subject areas" (frontier-risk transparency, third-party auditing and independent verification, and incident reporting), while preserving generally applicable laws, state regulation of deployers and users, and rules protecting minors. As of 22 October 2026 it had been referred to committee and had passed neither chamber [@uscongress2026frontier].

Federal action in 2026 continued to favour voluntary arrangements. The cyber-evaluation order (EO 14409) of 2 June 2026 asked agencies, including the standards body NIST, to develop a classified benchmark of models' cyber capabilities and a *voluntary* framework giving the government access to "covered frontier models" for up to 30 days before release to other trusted partners. It stated that nothing in it authorised "a mandatory governmental licensing, preclearance, or permitting requirement" [@trump2026promoting].

### The states

With little federal legislation, the states have written most binding US AI rules. According to the 2026 AI Index, AI-related bills enacted by US states rose from fewer than 10 in 2020 to 150 in 2025; California enacted 20 that year, Texas 12 and New York 10 [@sajadieh2026ai]. California's SB 243 on companion chatbots is discussed in Chapter 10. Three kinds of law matter most for developers.

Frontier-model transparency laws come first. California's Transparency in Frontier Artificial Intelligence Act (SB 53) was signed on 29 September 2025 and took effect on 1 January 2026 [@californiagovernor2025governor]. It defines a "frontier model" as one trained with more than 10^26 operations, counting fine-tuning and reinforcement learning on top of the original run. It targets "catastrophic risk": a foreseeable risk that a model materially contributes to the death or serious injury of more than 50 people, or more than $1 billion in damage, in a single incident. The routes it names are expert help with chemical, biological, radiological or nuclear weapons, autonomous cyber-attacks or crimes, and a model evading its developer's control. All frontier developers must publish a transparency report when they deploy a new frontier model and report critical safety incidents to the state Office of Emergency Services within 15 days, or within 24 hours to a law-enforcement or public-safety agency if there is an imminent risk of death or serious injury. "Large" developers, with annual revenue above $500 million, must also publish a framework for managing catastrophic risk, and face civil penalties of up to $1 million per violation, recoverable only by the Attorney General. The law protects whistleblowers [@californialegislature2025sb53; @metr2026frontier].

New York's RAISE Act, signed on 19 December 2025 and amended by a law signed on 27 March 2026, takes effect on 1 January 2027 [@nyassembly2026a9449]. As amended, it follows SB 53's structure but is stricter: incidents must be reported within 72 hours, a new office within the Department of Financial Services supervises developers and funds itself through assessments on them, and penalties for large developers reach $1 million for a first violation and $3 million for each subsequent one. Table 13.3 compares the main frontier-model regimes.

| | EU AI Act (systemic-risk GPAI) | California SB 53 | New York RAISE Act (as amended) |
|---|---|---|---|
| Applies from | 2 Aug 2025 (fines from 2 Aug 2026) | 1 Jan 2026 | 1 Jan 2027 |
| Compute trigger | > 10^25 FLOP (presumption; designation also possible) | > 10^26 operations | > 10^26 operations |
| Extra duties for large firms | — | revenue > $500 million | revenue > $500 million |
| Core duties | evaluations, risk mitigation, incident reports, cybersecurity | transparency reports; frameworks (large developers); incident reports | as SB 53, with a supervisory office |
| Incident deadline | "without undue delay" | 15 days (24 h if imminent danger) | 72 hours |
| Maximum penalty | €15 million or 3% of turnover | $1 million per violation | $1 million first, $3 million subsequent |
| Enforcer | European Commission (AI Office) | State Attorney General | State Attorney General; DFS office |

: Table 13.3: Main rules for frontier AI models in the EU, California and New York, as of October 2026. Source: @europeanparliament2024regulation; @californialegislature2025sb53; @nyassembly2026a9449; @metr2026frontier.

A second kind bans specific harmful uses. Texas's Responsible Artificial Intelligence Governance Act (HB 149), signed on 22 June 2025 and in force since 1 January 2026, prohibits developing or deploying AI that intentionally aims to incite self-harm, harm to others or crime, AI developed with the intent to discriminate unlawfully against a protected class, and social scoring by government. A disparate impact "is not sufficient by itself to demonstrate an intent to discriminate". Only the Attorney General can enforce it, after a 60-day period to cure, with penalties of up to $200,000 for uncurable violations; the Act also creates a 36-month regulatory sandbox [@texaslegislature2025hb149].

Laws on consequential decisions have proved the most contested.

::: {.box .case}
**Case study: Colorado's AI Act, from statute to stand-off**

In 2024 Colorado passed SB 24-205, the first broad US state law on "high-risk" AI systems used in consequential decisions such as hiring, lending and housing. It required both developers and deployers to "use reasonable care to protect consumers from any known or reasonably foreseeable risks of algorithmic discrimination", and deployers to carry out impact assessments. After a delay, it was due to take effect on 30 June 2026 [@usdoj2026complaint]. The pre-emption order singled it out, arguing that the law "may even force AI models to produce false results" [@trump2025ensuring].

On 9 April 2026 xAI sued Colorado's Attorney General in federal court [@usdccolorado2026docket]. On 24 April the Department of Justice filed to join as a plaintiff, arguing mainly that the law violated the constitutional guarantee of equal protection [@usdoj2026complaint]. Three days later a federal magistrate judge approved the parties' agreement that the state would not begin enforcing SB 24-205, "or any legislation replacing or amending" it, until 14 days after the court rules on a future request for a preliminary injunction [@usdccolorado2026minute].

On 14 May 2026 the Governor signed SB 26-189, which repealed and replaced the 2024 law [@coloradogeneralassembly2026automated]. The new law regulates "automated decision-making technology" through disclosure: notices to consumers, an explanation within 30 days after an adverse decision, and rights to correct data and to request human review. Violations count as deceptive trade practices enforced by the Attorney General, with no private right of action. Most duties apply from 1 January 2027. As of October 2026 the federal case remained open.
:::

## 13.4 China and the United Kingdom

China has built its AI rules in layers, through targeted measures issued by government agencies led by the Cyberspace Administration of China (CAC), rather than one horizontal law. The first layer, the Provisions on the Administration of Algorithmic Recommendations in Internet Information Services, has applied since 1 March 2022 [@cac2021provisions]. They require providers to offer users an option not targeted at their personal characteristics, or a convenient way to switch recommendation off (Article 17). Under Article 24, providers whose services have "public opinion attributes or social mobilisation capacity" must, within ten working days of launching, register details of the service and its algorithm, with a self-assessment report, in an online **algorithm filing** system. Later rules reuse this registry, so regulators know who operates which algorithm before anything goes wrong. Rules on "deep synthesis" (deepfakes and other synthetic media) followed from 10 January 2023 [@cac2022provisions].

The **Interim Measures for the Administration of Generative Artificial Intelligence Services**, issued by seven agencies on 10 July 2023, took effect on 15 August 2023 [@cac2023interim]. They apply to generative AI services offered to the public in mainland China. Providers must uphold "socialist core values", prevent prohibited content, use lawfully sourced training data, protect personal information and label generated images and video. Services with public-opinion attributes or mobilisation capacity must undergo a security assessment and file their algorithms. In effect, a public chatbot with such attributes needs both a registration and a security review before launch, a form of pre-market control that no Western jurisdiction applies to general-purpose models. Enforcement also runs through campaigns. In April 2025 the CAC launched a three-month "Qinglang" campaign against the misuse of AI, aimed at unregistered generative AI products, unlabelled synthetic content, "one-click undressing" apps, unauthorised voice and face cloning, AI-generated rumours and harm to minors [@cac2025qinglang].

Rules on specific issues followed. The **Measures for Labelling AI-Generated and Synthetic Content**, issued by four agencies in March 2025 and in force from 1 September 2025, require labels that users can see or hear and implicit labels in file metadata naming the provider [@cac2025measures]. In October 2025 the Standing Committee of the National People's Congress amended the Cybersecurity Law to add an article on the "safe and sound development of AI", in force from 1 January 2026 [@xinhua2025china]. In April 2026 five agencies issued interim measures on "anthropomorphic" AI services that simulate human personalities for companionship or emotional support. Effective from 15 July 2026, they require security assessments, algorithm filing and protections for minors and older users [@xinhua2026five]. Internationally, China's 13-point **Global AI Governance Action Plan** of 26 July 2025 frames AI as "an international public good" and calls for open-source sharing and capacity-building for the Global South [@mfa2025global].

The **United Kingdom** has so far kept to the sectoral approach of its 2023 white paper [@dsit2023proinnovation]. Since 2025 its policy has emphasised adoption and infrastructure. The *AI Opportunities Action Plan* by the entrepreneur Matt Clifford, published on 13 January 2025, made 50 recommendations [@dsit2025ai]. The government agreed to 47, including "AI Growth Zones" with easier access to power and planning, and an expansion of public compute capacity "by at least 20x by 2030" [@dsit2025opportunities]. The AI Safety Institute became the AI Security Institute in February 2025, refocused on cyber-attacks, chemical and biological misuse and crime; the government said it would "not focus on bias or free speech" [@dsit2025tackling]. Labour's 2024 manifesto had pledged binding rules for the most powerful models, yet the King's Speech of 13 May 2026 contained no AI bill [@iapp2026kings]. The UK's most consequential AI decision of 2026 concerned copyright (Section 13.6).

## 13.5 International coordination

AI models cross borders easily, which argues for international rules, yet states disagree about values, compete for economic and military advantage, and share few institutions with authority over AI. Figure 13.2 places the main international milestones alongside the national ones.

![Figure 13.2: Selected milestones in AI governance, 2023–2026, by jurisdiction. National and regional laws (upper lanes) developed alongside non-binding international declarations and one binding treaty, not yet in force by October 2026 (lower lanes). Source: @ukgov2023bletchley; @dsit2024frontier; @elysee2025statement; @pib2026india; @councilofeurope2024framework; @un2025terms; @un2026global; @europeanparliament2024regulation; @europeanparliament2026regulation; @biden2023safe; @trump2025ensuring; @cac2025measures; @californiagovernor2025governor.](../figures/svg/fig-13-02.svg){#fig:13-02}

### Summits

A series of summits began at Bletchley Park on 1–2 November 2023, where 28 countries and the EU, including the US and China, signed the **Bletchley Declaration**. It recognised the potential for "serious, even catastrophic, harm" from the most capable frontier models [@ukgov2023bletchley]. At the follow-up summit in Seoul in May 2024, 16 companies (later 20) signed the **Frontier AI Safety Commitments**, promising to publish safety frameworks with thresholds of intolerable risk and, in the extreme, not to develop or deploy a model whose risks could not be kept below them [@dsit2024frontier]. Chapter 12 examines the frameworks that resulted.

The Paris summit of 10–11 February 2025 was renamed the AI Action Summit and shifted emphasis towards inclusion, sustainability and economic opportunity [@elysee2025statement]. Its closing statement, on digital divides, market concentration, work and the environment, was signed by 63 countries plus the EU and the African Union Commission, but not by the United States or the United Kingdom. India's AI Impact Summit in New Delhi on 16–20 February 2026, organised around "people, planet and progress", was described by its host as the first global AI summit in the Global South [@pib2026india]. The titles, from "safety" to "action" to "impact", track a shift in political priorities.

None of the summits' outcomes is legally binding or monitored, and their effects have been indirect: the Seoul promise to publish safety frameworks reappears as a legal duty in SB 53 and the EU Code of Practice. They are also exposed to national politics, as the US and UK signatures at Bletchley and their absence from Paris show.

### Treaties, the United Nations and the OECD

The only binding international treaty specifically on AI is the Council of Europe's **Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law** (CETS No. 225). As a **framework convention**, it sets general obligations and leaves details to national law. It was opened for signature on 5 September 2024, when the UK, the United States and the EU were among the first to sign [@moj2024uk; @councilofeurope2024framework]. It enters into force about three months after five signatories, including at least three Council of Europe member states, have ratified it. According to the Council of Europe's treaty office, as of 22 October 2026 the convention had 21 signatories, including Canada, Japan and Ukraine, but only one ratification, by the EU on 15 May 2026, so it was not in force.

At the United Nations, General Assembly Resolution 78/265 of 21 March 2024 called for "safe, secure and trustworthy" AI [@un2024seizing]. Resolution 79/325 of 26 August 2025 established two bodies limited to the non-military domain [@un2025terms]: an **Independent International Scientific Panel on AI** of 40 experts to produce evidence-based assessments, and a **Global Dialogue on AI Governance**, meeting in Geneva in 2026 and New York in 2027. The first Geneva session took place on 6–7 July 2026 with delegations from 163 countries, and the Panel presented a preliminary report to it [@un2026global]. The model is loosely the Intergovernmental Panel on Climate Change, except that AI capabilities change far faster than the climate and much of the evidence is held by companies.

The **OECD AI Principles**, adopted in 2019 and updated in May 2024, had 47 adherents in 2026 [@oecd2024principles]; their definition of an AI system was adopted almost word for word in the EU AI Act. The G7's **Hiroshima AI Process** produced Guiding Principles and a Code of Conduct for developers of advanced AI systems, endorsed on 30 October 2023 [@mic2023hiroshima]. Since February 2025 the OECD has run voluntary reporting against the Code; its first report drew on submissions from 20 organisations [@oecd2025hiroshima].

Finally, **technical standards** turn principles into checklists that auditors can verify. ISO/IEC 42001, published in 2023, specifies requirements for an AI management system: the policies, roles and processes an organisation uses to develop or use AI responsibly [@iso2023information]. Organisations can be certified against it, as against quality-management standards. Under the EU AI Act, compliance with **harmonised standards**, European standards requested by the Commission, gives a legal presumption of conformity. Their late arrival helped cause the omnibus delays, and the omnibus now requires the Commission to request them "without undue delay" [@europeanparliament2026regulation].

## 13.6 Copyright, training data and personal data

Large models are trained on vast collections of text, images and music, much of it protected by copyright or containing personal data. The **input question** asks whether copying works to train a model infringes copyright. The **output question** asks whether a model, or what it generates, reproduces protected works. By October 2026 courts in the US, the UK and Germany had given partial and partly conflicting answers, summarised in Table 13.4.

### The United States: fair use

In the United States the central defence is **fair use**, which allows some unlicensed use of copyrighted works. Courts weigh four factors: the purpose and character of the use, including whether it is "transformative" (serves a new purpose); the nature of the work; the amount used; and the effect on the market for the original.

::: {.box .case}
**Case study: Bartz v. Anthropic**

Authors sued Anthropic for training its Claude models on their books without permission. According to the court record, Anthropic had downloaded at least five million copies of books from Library Genesis and at least two million from the Pirate Library Mirror, "over seven million copies of books" in all, knowing they were pirated. Later it spent "many millions of dollars" buying print books, which were stripped from their bindings, scanned and discarded [@usdcnortherncal2025bartz].

On 23 June 2025 Judge William Alsup ruled that training the models was "exceedingly transformative and was a fair use". He rejected the argument that models would flood the market with competing works, comparing it to complaining that "training schoolchildren to write well" would produce competing works. Scanning purchased print books was also fair use. Building a permanent library from pirated copies was not excused, and that claim went towards a class-action trial.

The parties settled for $1.5 billion, which Judge Araceli Martínez-Olguín, who had taken over the case, approved on 20 July 2026 [@bloomberglaw2026anthropic]. The settlement covers more than 480,000 works at about $3,100 per work and requires Anthropic to destroy the pirated datasets; claimants were being notified from September 2026 [@anthropicsettlement2026]. A settlement sets no precedent, but the case showed that how training data is acquired can matter as much as how it is used.
:::

Two days after the Bartz ruling, Judge Vince Chhabria granted summary judgment to Meta in *Kadrey v. Meta*, brought by thirteen authors over books Meta had downloaded from shadow libraries including LibGen and Anna's Archive [@usdcnortherncal2025kadrey]. (Summary judgment decides a case without a full trial when the key facts are not in dispute.) Even prompts designed to make the models regurgitate training data produced no more than 50 words and punctuation marks of the plaintiffs' books. Chhabria ruled for Meta only because the authors had offered no evidence on the harm he considered decisive, "market dilution" by a flood of competing generated works. He warned that unlicensed training would, "in most cases", likely be illegal; the ruling bound only these thirteen authors.

On 29 September 2026 the Third Circuit Court of Appeals decided *Thomson Reuters v. Ross Intelligence* on an interlocutory appeal [@thirdcircuit2026thomson]. Ross, a legal-research start-up, had used 2,243 Westlaw headnotes (editorial summaries of points of law), obtained through a contractor, to train an AI search tool marketed as a Westlaw competitor. The court held that the headnotes were copyrightable and that Ross's use was "minimally transformative, at best", since it served the same purpose as the original. It also found that "the market for licensing headnotes as text to train AI is rapidly developing" and that Ross had usurped Thomson Reuters's opportunity to enter it, reasoning that could matter far beyond legal research. The court stressed, however, that "ROSS's AI was not a generative AI". It also noted a Department of Justice statement of 1 September 2026, in the consolidated New York cases against OpenAI (including the *New York Times* claims), arguing that training a large language model is transformative; those cases were pending in October 2026.

On outputs, US law requires a human author. In *Thaler v. Perlmutter* the Court of Appeals for the DC Circuit held on 18 March 2025 that the Copyright Act "requires all work to be authored in the first instance by a human being", upholding the refusal to register an image whose sole listed author was an AI system [@uscadc2025thaler]. The US Copyright Office's report on generative-AI training, released in pre-publication form on 9 May 2025, had not been finalised by October 2026 [@uscopyrightoffice2025copyright].

### Europe: the model as a copy

In the UK, Getty Images sued Stability AI over the image generator Stable Diffusion [@highcourt2025getty]. Getty dropped its training claim for lack of evidence that training took place in the UK. On 4 November 2025 the High Court rejected the remaining claim, that importing the model was secondary infringement because it was an "infringing copy". Although an "article" under UK copyright law can be intangible, Mrs Justice Joanna Smith held that "the model weights are not themselves an infringing copy and they do not store an infringing copy"; Stable Diffusion "does not store or reproduce any Copyright Works and nor has it ever done so". Trade-mark infringement, where older versions' outputs showed Getty and iStock watermarks, was "historic and extremely limited in scope". She later gave Getty permission to appeal on the "infringing copy" point, a question of law "on which the minds of reasonable lawyers may differ" [@fairhurst2026permission]. No appeal decision had been reported by October 2026.

A German court, on different facts, reached the opposite conclusion about what a model contains. On 11 November 2025 the Munich Regional Court I largely upheld claims by GEMA, the German music collecting society, against two OpenAI companies over song lyrics by nine well-known German songwriters [@lgmuenchen2025gema]. According to the court's press release, the lyrics were "reproducibly contained" in the GPT-4 and GPT-4o models. This is **memorisation**: comparison with ChatGPT's outputs showed that the parameters had absorbed the texts in full, and their length ruled out coincidence. That fixation was a reproduction under EU law, even though it existed only as probability values. The EU **text and data mining exception**, as implemented in Germany, covered the copies made to assemble a training corpus but not copies retained in the model, because it assumes that only information, not the work itself, is extracted. The outputs also infringed, and OpenAI, not its users, was responsible, since simple prompts had produced them. The judgment was not final.

The two European rulings differ less than they seem: London found no evidence that Stable Diffusion stored Getty's images, Munich found that GPT-4 reproduced specific lyrics. Both treated memorisation as decisive, turning a legal question into a partly technical one about what a given model has stored.

| Case | Court and date | Holding | Status (Oct 2026) |
|---|---|---|---|
| *Bartz v. Anthropic* | N.D. Cal., 23 Jun 2025 | Training and scanning bought books fair use; pirated library not | Settled; $1.5 bn approved 20 Jul 2026 |
| *Kadrey v. Meta* | N.D. Cal., 25 Jun 2025 | For Meta: no evidence of market harm; dilution theory left open | Ruling binds 13 authors only |
| *Thomson Reuters v. Ross* | 3rd Cir., 29 Sep 2026 | Non-generative competitor's training not fair use | Appellate precedent |
| *Getty Images v. Stability AI* | High Court (England and Wales), 4 Nov 2025 | Model weights not an "infringing copy" | Permission to appeal granted |
| *GEMA v. OpenAI* | Munich Regional Court I, 11 Nov 2025 | Memorised lyrics in model and outputs infringe; TDM exception does not apply | First instance, not final |

: Table 13.4: Selected court decisions on AI training and copyright, as of October 2026. Source: @usdcnortherncal2025bartz; @bloomberglaw2026anthropic; @usdcnortherncal2025kadrey; @thirdcircuit2026thomson; @highcourt2025getty; @fairhurst2026permission; @lgmuenchen2025gema.

Governments have hesitated to legislate. The UK's Data (Use and Access) Act 2025, which received Royal Assent on 19 June 2025, required the government to publish an economic impact assessment and a report on the use of copyright works in developing AI within nine months [@ukparliament2025data]. The March 2026 report abandoned the government's earlier preferred option, a broad exception allowing training unless rights holders opted out, after most consultation respondents rejected it. That option was "no longer the government's preferred way forward", and more evidence would be gathered [@dsit2026report].

### Personal data

Text and images collected from the web contain **personal data**, information about an identifiable person. In the EU the GDPR requires a legal basis, such as consent or a "legitimate interest", for each use, and national data-protection authorities enforced it against AI years before the AI Act applied. On 30 March 2023 the Italian authority, the Garante, ordered OpenAI to stop processing Italian users' data through ChatGPT, citing no legal basis for the "massive collection and processing of personal data" used in training, missing information to users and no age checks [@garante2023intelligenza]. In December 2024 it fined OpenAI €15 million; in March 2026 the Tribunal of Rome upheld OpenAI's appeal against that decision [@garante2024chatgpt].

The European Data Protection Board, which brings together the EU's national authorities, set up a ChatGPT taskforce whose May 2024 report observed that because of "the probabilistic nature of the system" the training approach "may also produce biased or made up outputs". Data accuracy must nonetheless be ensured, and responsibility cannot be shifted to users through terms and conditions [@edpb2024report]. Under the Board's Opinion 28/2024 of December 2024, a model counts as anonymous only if it is "very unlikely" that people in the training data can be identified or their data extracted by queries [@edpb2024opinion]. Legitimate interest can justify training if the processing is strictly necessary and passes a balancing test. And a model developed with unlawfully processed data may be unlawful to deploy "unless the model has been duly anonymised". Draft guidelines on web scraping for generative AI (July 2026) add practical expectations: defining precise collection criteria, filtering out sensitive categories of data, and excluding websites "which clearly oppose the scraping" [@edpb2026guidelines].

In May 2024 the Dutch authority fined Clearview AI €30.5 million for building a facial-recognition database by processing biometric data without a legal basis and without adequately informing the people concerned [@edpb2024dutch]. Large platforms have more often negotiated changes. In June 2024 Meta paused plans to train its models on public posts by adults in the EU after the Irish Data Protection Commission raised concerns, and started such training from 27 May 2025, after changing its notices and making it easier to object [@dpc2025statement].

## 13.7 Liability, compute thresholds and the cost of regulation

### Liability

When an AI system gives dangerous advice or makes a discriminatory decision, the developer, the deploying company or the user may be responsible. Two kinds of rule answer different questions. Regulatory penalties, such as the fines in Table 13.2, are imposed by a public authority for breaching a statute and are paid to the state. Liability rules decide whether a person who has been harmed can claim compensation, and from whom.

In the EU the answer rests on product liability. The revised Product Liability Directive, Directive (EU) 2024/2853, entered into force on 8 December 2024. Member states must transpose it by 9 December 2026, and it applies to products placed on the market from that date; earlier products stay under the 1985 directive [@europeancommission2024liability]. It covers "all types of software", including AI systems, and liability does not depend on fault. Manufacturers can be liable for defects that arise after release through updates or machine learning. Compensable damage includes psychological harm and the destruction or corruption of data. Courts can order defendants to disclose evidence and can ease the claimant's burden of proof where needed, which matters when the defect lies inside a model that the claimant cannot inspect. Claims must be brought within three years. A second instrument, the AI Liability Directive proposed in September 2022 to ease fault-based claims, was withdrawn by the Commission on 6 October 2025 [@europeanparliament2025procedure]. EU victims of AI harm therefore rely on the product regime plus national tort law.

The US has no federal AI liability statute, and the state laws in Section 13.3 create penalties, not compensation. SB 53 and the Texas Act can be enforced only by the Attorney General, and Colorado treats violations as deceptive trade practices for the Attorney General to pursue, with no private right of action. People harmed by AI therefore sue under ordinary tort law, and the most prominent cases concern chatbots and minors (Chapter 10). In *Garcia v. Character Technologies*, brought in federal court in Florida after a teenager's death, the defendants argued that the chatbot's output was speech protected by the First Amendment and that the app was not a product. In May 2025 Judge Anne Conway dismissed one claim but let the rest proceed, including those against Google as an alleged component maker. She was "not prepared to hold" at that stage that the output was speech, and treated the app as a product so far as the claims concerned its design "rather than ideas or expressions within the app" [@usdcmdfla2025garcia]. Similar suits against OpenAI followed in California state courts: one in August 2025 alleging wrongful death, defective design, failure to warn and negligence [@hendrix2025breaking], and seven in November 2025 that, according to the plaintiffs' lawyers, make similar claims about the GPT-4o model [@smvlc2025seven].

Whether the defence that has protected online platforms for decades applies to such cases is an open question. Section 230 of the Communications Decency Act shields a service from being treated as the publisher of "information provided by another information content provider", but anyone responsible "in whole or in part" for creating the information is itself a content provider [@lii2026section230]. On the statute's wording, text generated by a company's own model may not count as information provided by someone else; the *Garcia* defendants did not invoke Section 230.

### Compute thresholds and their critics

To decide which models deserve extra scrutiny before anyone knows what they can do, regulators have mostly used a **compute threshold**, a legal trigger based on the computation used in training. The EU uses 10^25 FLOP as a presumption of systemic risk; California and New York use 10^26, as did Biden's revoked safety order (Table 13.3).

The case for thresholds is practical: compute is easier to observe, count and restrict than data or algorithms, as Section 7.7 explains [@sastry2024computing]. In a preprint, Heim and Koessler argue that training compute is the best available metric for *identifying* models that warrant oversight: it correlates with capabilities, can be measured before deployment and can be checked by outsiders [@heim2024training]. They stress that it is an imperfect proxy for risk, fit only as an initial filter that triggers evaluations. Hooker, in another preprint, questions even that role, arguing that the relationship between compute and risk is "highly uncertain and rapidly changing" [@hooker2024limitations]. Smaller models trained with better data and methods can match larger ones, so a fixed threshold may catch harmless models and miss dangerous ones.

Lawmakers have hedged: the EU can designate models on other grounds, and SB 53 counts fine-tuning and reinforcement learning towards its threshold. The US government's 2026 cyber framework abandoned compute altogether, defining "covered frontier models" by results on a classified capability benchmark [@trump2026promoting]. The rules these thresholds trigger are mostly about **transparency and process**: publishing safety frameworks, testing models, reporting incidents and protecting whistleblowers. Only China requires a security assessment before certain public services launch, and the 2026 US order explicitly rules out licensing. Whether disclosure will suffice for the most capable systems links to the safety methods of Chapter 12 and the scenarios of Chapter 14.

::: {.box .debate}
**Debate: Does AI regulation hold back innovation?**

Mario Draghi's 2024 report on European competitiveness for the European Commission counted "around 100 tech-focused laws and over 270 regulators active in digital networks" in the EU and cited the AI Act's compute-threshold duties for general-purpose models as an example of precaution. It concluded that the overall regulatory burden leaves only larger companies, "which are often non-EU based", able to bear the costs of compliance [@draghi2024future]. The best evidence comes from the GDPR, an earlier EU digital law that applied from May 2018. Afterwards EU technology ventures raised less money, in fewer and smaller deals, than comparable US ventures, according to a peer-reviewed study [@jia2021short]. A working paper by Janßen and colleagues found that the GDPR induced the exit of "about a third of available apps", while new app entry fell by half [@janssen2022gdpr]. Demirer and colleagues (working paper 2024, published in the *Journal of Political Economy* in 2026) found in the working-paper version that EU firms cut data storage by 25 per cent and data processing by 15 per cent relative to comparable US firms, consistent with a 21 per cent rise in the cost of data [@demirer2024data].

The case against starts from the size of those effects and their causes. The same Demirer study finds that the higher cost of data translates into "only a 0.1–0.6% rise in overall production costs", because data plays a small role in production compared with computation [@demirer2024data]. The legal scholar Anu Bradford attributes the US–EU gap in technology firms to fragmented capital markets, bankruptcy law, the incomplete single market and immigration policy more than to digital regulation, and calls the trade-off a "false choice" [@bradford2024false]. The AI investment gap is real: in 2025 private AI investment reached $285.9 billion in the United States against $5.9 billion in the United Kingdom, Europe's largest recipient, according to the 2026 AI Index [@sajadieh2026ai]. But it opened before the AI Act's main duties applied, so it cannot be their effect.

Neither side has decisive evidence for AI: the GDPR studies concern a data-protection law and mostly short-run effects, and the AI Act's high-risk duties apply only from December 2027. A convincing test would compare investment, firm entry and model releases in the EU before and after 2027–2028 with similar markets lacking such rules, separating the Act's effects from those of energy prices and capital markets.
:::

In October 2026 almost no rule in force required a licence before a model's release; China's security assessments were the exception. Elsewhere the law asks for disclosure, documentation and incident reports, triggered by training compute or by use in sensitive decisions, and leaves compensation to product liability in the EU and to tort suits in the US. Timetables proved soft: Brussels deferred its high-risk regime, Colorado rewrote its law under federal pressure, and US federal policy rests on revocable orders. Meanwhile courts are settling questions the statutes left open, such as whether a model stores its training data and whether a chatbot is a product.

## Further reading

- European Parliament and Council (2024). *Regulation (EU) 2024/1689 (Artificial Intelligence Act)*. The primary text; Articles 2, 5, 6, 43, 50–55, 99 and Annex III, read with the 2026 amendments, cover most of what matters in practice. [@europeanparliament2024regulation]
- European Parliament and Council (2026). *Regulation (EU) 2026/1744 (Digital Omnibus on AI)*. Shows how and why the Act's timetable, enforcement structure and small-firm relief were changed before its main rules applied. [@europeanparliament2026regulation]
- Hooker, S. (2024). *On the Limitations of Compute Thresholds as a Governance Strategy*. A readable critique of the thresholds used in US and EU rules (preprint). [@hooker2024limitations]
- Bradford, A. (2024). *The False Choice Between Digital Regulation and Innovation*. Northwestern University Law Review. The most careful argument that EU regulation does not explain Europe's technology gap. [@bradford2024false]
- Getty Images v Stability AI [2025] EWHC 2863 (Ch). The fullest judicial account so far of how a diffusion model is trained and why its weights were held not to store the training images. [@highcourt2025getty]
- European Data Protection Board (2024). *Opinion 28/2024 on Certain Data Protection Aspects Related to the Processing of Personal Data in the Context of AI Models*. The EU regulators' joint view on when models trained on personal data are lawful. [@edpb2024opinion]


```{=html}
<section class="part"><p class="part-label">Part V</p><h1 class="part-title">The Decade Ahead</h1></section>
```

# Chapter 14: Forecasting the Next Ten Years: Methods, Scenarios and Open Problems

Between June and October 2022, shortly before ChatGPT was released, 89 superforecasters (people selected for a proven record of accurate predictions) and 80 domain experts took part in a forecasting tournament on global risks. One question asked when an AI system would win a gold medal at the International Mathematical Olympiad. The median superforecaster said 2035 and the median expert 2030. In July 2025 Google DeepMind and OpenAI both reported gold-medal-level performance at that year's Olympiad. The organisers later estimated that the superforecasters had given this outcome, by 2025, a probability of 2.3% and the experts 8.6% [@kucinskas2025assessing].

A second record points the other way. In October 2023, 2,778 researchers who had published at leading AI venues were asked when unaided machines would be able to do every task better and more cheaply than human workers. Their aggregate answer gave a 50% chance by 2047. Asked instead when every occupation would be fully automatable, the same population gave 2116 [@grace2025thousands]. The two questions describe almost the same world, yet the answers lie about seventy years apart. One body of evidence shows forecasters too slow on concrete benchmarks; the other shows that long-range answers depend heavily on how the question is worded. Both are needed to judge what any forecast of AI's next ten years is worth.

## 14.1 The track record of AI forecasting

A **forecast** is a statement about the future that can later be checked: a date, a number or a probability. Forecasting AI is hard for structural reasons. Progress depends on several inputs at once (computing power, data, algorithms and money), each of which can change course. Capability is measured with benchmarks that saturate or leak into training data, so even the present is blurred (Chapter 4). Adoption by firms and governments moves at a different speed from invention. And forecasts can alter what they predict, because investors and regulators act on them.

### Early predictions

Chapter 1 traces how the field's first timetables, from the Dartmouth proposal of 1955 to Herbert Simon's twenty-year forecast of 1960, were missed, and how the misses fed a cycle of AI "springs" and "winters" [@mitchell2021why]. The first systematic study of such predictions came from Stuart Armstrong and Kaj Sotala, who assembled a database of 257 AI predictions made since the 1950s [@armstrong2015how]. The dates for human-level AI were scattered so widely that fifty-year gaps between them were common. Of the predictions the authors classed as expert, a third placed human-level AI 16 to 25 years after the date of the prediction. The "Maes–Garreau law", the claim that people predict AI just before the end of their own lives, was not supported: only about a fifth of the testable predictions fell within five years of the predictor's life expectancy. A 2016 reanalysis by Katja Grace found that the column used to identify experts in fact recorded how each prediction was reached, so the authors' claim that experts and non-experts were indistinguishable does not stand. Armstrong replied that the habit of predicting a fixed distance ahead survived the correction: more than half of the predictions by researchers working on general AI fell 10 to 25 years out [@grace2016error]. A horizon that stays constant while the calendar moves suggests a habit of mind as much as evidence.

### Recent forecasts of concrete milestones

Since about 2020, forecasting has shifted towards concrete, short-range questions, and here the dominant error has been the opposite: too slow. In August 2021 Jacob Steinhardt's research group ran a contest on the Hypermind forecasting platform, whose forecasters are typically paid according to a scoring rule that rewards accurate probabilities, to predict benchmark results for June 2022. For the MATH benchmark of competition mathematics problems, the aggregate forecast was about a quarter of the best result actually reached by the deadline. For MMLU, a multiple-choice test of knowledge across many academic subjects, it was also too low (Table 14.1). Both outcomes lay far in the tails of the forecast distributions. Progress on a robustness benchmark, by contrast, was slower than forecast [@steinhardt2022ai].

The 2022 tournament described above gave the same picture at larger scale. A 2025 working paper by its organisers scored the 38 of its 172 sub-questions that had resolved by mid-2025 [@kucinskas2025assessing]. Superforecasters and domain experts were about equally accurate overall, with no statistically significant difference between groups. Both underestimated AI progress, and superforecasters did so more. Across four AI benchmark questions, superforecasters had on average given a probability of 9.7% to the outcomes that occurred, against 24.6% for domain experts. On green technology the error ran the other way: both groups expected renewable hydrogen to cost $3.50–4.50 per kilogram in 2024, and it cost about $7.50.

The Forecasting Research Institute (FRI), which ran that tournament, has since collected AI forecasts from a standing panel. Its Longitudinal Expert AI Panel (LEAP), launched in mid-2025, initially included 339 experts (computer scientists, industry researchers, economists and policy researchers) alongside superforecasters. A September 2026 review of a selection of FRI's AI forecasts, which the institute describes as reasonably representative, found that "forecasters dramatically underestimate AI progress on benchmarks" [@rosenberg2026how]. Table 14.1 collects examples. The same review found errors in the other direction. In a randomised trial run by another organisation, STEM undergraduates with AI help attempted three tasks relevant to biological risk; every group of forecasters had expected far more of them to complete all three than the 5.2% who did. Experts' median forecast that 7.3% of US ride-hailing trips would be made in autonomous vehicles during 2027 also looked high: FRI's projection from current trends, made with an AI model, was 2.5%.

| Question (date forecast) | Generalist forecasters | Experts | Outcome |
|---|---|---|---|
| MATH benchmark, best score by June 2022 (Aug 2021) | 12.7% | n/a | 50.3% |
| MMLU, best score by June 2022 (Aug 2021) | 57.1% | n/a | 67.5% |
| MATH, best score by mid-2024 (2022) | 71% | 80% | 87.9% |
| MMLU, best score by mid-2024 (2022) | 77.8% | 84.8% | 88.7% |
| Year of AI gold medal at the Mathematical Olympiad (2022) | 2035 | 2030 | 2025 |
| Largest compute used in an AI experiment by end 2024, petaFLOP/s-days (2022) | 100,000 | 420,680 | 578,704 |
| FrontierMath (Tiers 1–3), best score by end 2025 (2025) | 30% | 31% | 40.7% |
| US work hours assisted by generative AI in 2025 (2025) | 3.6% | 4% | 5.7% |
| Students completing all tasks with AI help (2025) | 16.2% | 22.5% (biosecurity experts), 40% (virologists) | 5.2% |

: Table 14.1: Selected AI forecasts and outcomes. "Generalist forecasters" are the aggregate of forecasters recruited through the Hypermind platform in rows 1–2 and superforecasters (medians) in rows 3–9. Rows 3–6: the 2022 Existential Risk Persuasion Tournament; rows 7–9: later FRI studies including LEAP. FrontierMath is a benchmark of several hundred original, unpublished mathematics problems written and checked by expert mathematicians, many needing hours of a specialist's effort [@glazer2024frontiermath]. The work-hours question may have been affected by an outdated baseline given to forecasters. Source: [@steinhardt2022ai; @kucinskas2025assessing; @rosenberg2026how].

The table flatters the story of underestimation in ways FRI itself acknowledges. Interim reviews are biased towards finding underestimates: a forecast that is too low is revealed as soon as the real value crosses it, while one that is too high can be confirmed only after its deadline passes [@rosenberg2026how]. Benchmark scores are also the easiest quantities to resolve and the ones on which AI has moved fastest; forecasts about electricity use and data-centre capacity in the same review looked roughly on track, judged against projections made with an AI model. Nothing here scores a forecast of human-level AI or of AI's effect on extinction risk. On that question the tournament's headline result was a wide and stable gap. Among the participants who answered it (88 superforecasters and 29 AI domain experts), the median expert put the probability of AI-caused human extinction by 2100 at 3% and the median superforecaster at 0.38%. Few minds changed during months of structured argument [@karger2023forecasting; @karger2025subjective]. The organisers found no statistically significant correlation between a forecaster's accuracy on near-term questions and their long-run risk estimates [@kucinskas2025assessing]. Near-term track records therefore say little, so far, about whose long-term judgement to trust.

## 14.2 Asking people: surveys, tournaments and markets

### Expert surveys

The largest series of surveys of AI researchers is run by Katja Grace and colleagues. The 2023 round contacted about 20,000 people who had published at six leading AI venues in 2022; 2,778 responded, a response rate of 15% [@grace2025thousands]. Each respondent gave three year–probability pairs for a milestone. The authors fitted a smooth probability curve to each person's answers and averaged the curves, so the aggregate is a mean of distributions, not a median of dates.

The aggregate can move sharply. The year with a 50% chance of **high-level machine intelligence** (unaided machines doing every task better and more cheaply than humans) was 2060 in the 2022 survey and 2047 in 2023, having barely moved since 2016. Yet the framing of a question changes the answer more than a year of events did. Half of respondents were asked "in how many years will there be a 10%, 50% and 90% chance?", the other half "what is the chance within 10, 20 and 40 years?". For the first group the 50% point lay 17 years away, for the second 34 years. The occupation-based framing (**full automation of labour**) gave 2116 in 2023, seven decades later than its task-based twin. Figure 14.1 shows the movement and the framing gap.

![Figure 14.1: Aggregate year by which AI researchers gave a 50% chance to two milestones, in surveys run in 2022 and 2023. "High-level machine intelligence" asks when machines will do every task better and more cheaply than humans; "full automation of labour" asks when every occupation will be automatable. The gap between framings is larger than the change between years. Source: @grace2025thousands.](../figures/svg/fig-14-01.svg){#fig:14-01}

Respondents were not complacent about risk. The median probability they gave to "extremely bad outcomes (e.g. human extinction)" from high-level machine intelligence was 5% (mean 9%). Depending on the question, between 38% and 51% gave at least a 10% chance of outcomes as bad as extinction. Such surveys are large and repeatable, but answers depend on wording, a 15% response rate may select for people with strong views, and researchers who build AI systems are not necessarily expert in how economies adopt them. The authors cannot tell which framing is more accurate and give the two equal weight.

### Tournaments and superforecasters

A second approach treats forecasting as a skill to be measured. In the early 2010s the US intelligence community funded a tournament in which university research groups competed to give the most accurate probabilities for geopolitical events. The winning group, the Good Judgment Project, found that three interventions improved accuracy: training in probabilistic reasoning, working in teams, and "tracking", which placed the top 2% of forecasters from the first year in elite teams [@mellers2014psychological]. These **superforecasters** did not regress towards the average, as chance success would predict, but kept their accuracy in two successive years across hundreds of questions [@mellers2015identifying]. Philip Tetlock and Dan Gardner describe them as people who gather evidence from many sources, think in probabilities and revise their views when wrong [@tetlock2015superforecasting]. Accuracy in such tournaments is measured with proper scoring rules, of which the Brier score is the most common.

::: {.box .deeper}
**Going deeper: Scoring a forecaster**

The **Brier score** rates probability forecasts [@brier1950verification]. For each question, take the probability given, subtract the outcome (1 if the event happened, 0 if not) and square the result; then average over all questions. Lower is better. A forecaster who always says 50% scores 0.25 whatever happens.

A worked example. Two forecasters answer four questions; events 1 and 2 happen, events 3 and 4 do not. Forecaster A says 90%, 70%, 20% and 60%; her squared errors are 0.01, 0.09, 0.04 and 0.36, for a Brier score of 0.125. Forecaster B hedges with 60%, 50%, 40% and 50%; his errors are 0.16, 0.25, 0.16 and 0.25, for a score of 0.205. A was bolder and wrong once, but her confident correct calls earned more than her miss cost. Applied to the tournament's Olympiad question, the superforecasters' implied 2.3% for an event that happened scores (0.023 − 1)^2^ ≈ 0.955 on that question, close to the worst possible score of 1; the experts' 8.6% scores about 0.835.

Allan Murphy showed in 1973 that the Brier score can be split into three parts: the inherent uncertainty of the events, **reliability** (whether events given 70% happen about 70% of the time, also called calibration) and **resolution** (whether the forecaster separates events that happen from those that do not) [@murphy1973new]. A forecaster who always predicts the long-run base rate is perfectly calibrated but has no resolution. The squaring matters too: under this rule a forecaster's expected score is best when they report their true belief, so honest reporting is rewarded.
:::

Tournaments have also become the standard test for AI forecasters. ForecastBench, presented at the ICLR 2025 conference, poses about 1,000 automatically generated questions whose answers are unknown when forecasts are made, which rules out the leakage of answers into training data. On a 200-question subset, the superforecasters' median forecasts achieved a Brier score of 0.096, the public's median forecasts 0.121 and the best language model tested (Claude 3.5 Sonnet, which was given the crowd forecasts on market questions) 0.122; the gap between superforecasters and the best model was statistically significant [@karger2025forecastbench]. The benchmark is updated continuously, so these figures describe models of 2024; by September 2026 FRI noted that some models performed at superforecaster level on certain question types [@rosenberg2026how].

The XPT working paper also bears on method. Individual forecasters were statistically indistinguishable from two simple rules, "no change" and trend extrapolation, partly because many questions concerned rare events that did not happen or slow-moving quantities whose trends persisted. Taking the median of many forecasters, however, improved accuracy by about one standard deviation over the typical individual. A sample of educated members of the public scored 1.82 standard deviations below the median participant [@kucinskas2025assessing].

### Prediction markets

In a **prediction market**, people trade contracts that pay out if an event occurs, so the price can be read as a collective probability. Justin Wolfers and Eric Zitzewitz found that such market forecasts are typically fairly accurate and outperform most moderately sophisticated benchmarks [@wolfers2004prediction]. The best long-run evidence comes from the Iowa Electronic Markets on US presidential elections. Comparing market prices with 964 national polls across the five elections from 1988 to 2004, Berg, Nelson and Rietz found the market closer to the final vote share 74% of the time, and significantly better than polls in every election when forecasting more than 100 days ahead [@berg2008prediction].

Elections suit markets: the question is precise, it resolves on a known date and many traders hold relevant information. "When will AI match humans at every task?" has none of these properties. It is hard to define and may take decades to resolve, and money locked in a long-dated contract earns nothing meanwhile, so traders have little reason to correct a mispriced long-range forecast. Markets and forecasting platforms are therefore most informative about AI for questions such as benchmark scores, model releases or regulatory decisions within a year or two.

::: {.box .debate}
**Debate: Whose forecasts of AI should we trust?**

*Domain experts.* People who build AI systems see capabilities before the public does and understand technical bottlenecks. On all four AI benchmark questions of the 2022 tournament (MATH, MMLU, QuALITY and the Olympiad), experts gave higher probabilities than superforecasters to what actually happened, and their median date for an Olympiad gold was five years nearer the truth [@kucinskas2025assessing].

*Generalist forecasters.* Superforecasters have a measured record across hundreds of questions [@mellers2015identifying]. Across all 38 resolved tournament questions, experts were no more accurate overall. Long-range predictions of human-level AI, many made by AI researchers, have historically clustered at a fixed distance ahead [@armstrong2015how; @grace2016error]. In a randomised trial reported in a 2025 preprint, 16 experienced software developers working on their own projects took 19% longer with AI assistance, after forecasting that it would cut their completion time by 24%; machine-learning experts had predicted a 38% reduction [@becker2025measuring]. Familiarity with the technology did not protect against that error.

Neither group has a record on decade-long AI questions, because none has resolved. FRI reports that LEAP forecasters have updated towards faster progress but that it has "not yet seen evidence of improved accuracy on more recent questions" [@rosenberg2026how]. The dispute will be settled by scoring identified individuals, not group medians, on many one-to-five-year questions as they resolve: that would show whether accuracy on AI is a stable trait, and who has it.
:::

## 14.3 Extrapolating trends

**Trend extrapolation** fits a line to past data and extends it. It is the most transparent method, because anyone can inspect both the data and the line. For AI, four series are watched most closely; Chapter 4 explains what each measures.

- **Training compute.** Epoch AI estimates that the compute used to train notable models grew about 4 to 5 times per year from 2010 to May 2024 [@sevilla2024training], and that frontier language-model training compute has grown about 5 times per year since 2020 [@epochai2026trends].
- **Cost.** The amortised hardware and energy cost of the most compute-intensive training runs grew about 2.4 times per year from 2016 (90% confidence interval 2.0 to 2.9), according to a preprint by Cottier and colleagues [@cottier2024rising].
- **Algorithmic efficiency.** The compute needed to reach a given level of language-model performance halved roughly every eight months between 2012 and 2023, with a wide 90% confidence interval of about 2 to 22 months [@ho2024algorithmic].
- **Capability.** METR's **time horizon** is the length of software task, measured by how long it takes a skilled human, that an AI agent completes with 50% reliability (Section 4.7). Kwa and colleagues found that it doubled about every seven months from 2019 to early 2025 [@kwa2025measuring]. In METR's data file as updated in September 2026, the doubling time is about 188 days over the whole period and about 129 days from 2023 onwards (uncertainty range 104 to 158 days) [@metr2026task]. By February–March 2026 METR put the public frontier at around 12 hours, with an uncertainty range of about 5 to 61 hours, and stated that its task suite could no longer reliably measure horizons above 16 hours [@metr2026risk].

### How much the window matters

The choice of fitting window changes the answer more than any other decision. In METR's January 2026 release, the time horizon fitted over 2019–2025 doubled about every 196 days; fitted to models since 2023, every 131 days; fitted to models since 2024, every 89 days [@metr2026time]. Small differences in doubling time compound quickly. Table 14.2 extends the 12-hour frontier of early 2026 by four years under the doubling times of the September 2026 data file. Taking a working year as 2,000 hours, the slow long-run trend implies tasks of just over one working year by 2030; the post-2023 trend implies about fifteen.

| Doubling time (basis) | Doublings in 4 years | Growth factor | Implied 50% horizon, early 2030 |
|---|---|---|---|
| 188 days (all models since 2019) | 7.8 | about 220× | about 2,600 hours |
| 158 days (upper end of post-2023 range) | 9.2 | about 610× | about 7,300 hours |
| 129 days (models since 2023) | 11.3 | about 2,600× | about 31,000 hours |
| 104 days (lower end of post-2023 range) | 14.0 | about 17,000× | about 200,000 hours |

: Table 14.2: Illustrative extrapolation of METR's time horizon from about 12 hours (early 2026) over 1,461 days, by the author. The starting value's own uncertainty range runs from about 5 to 61 hours, and METR cannot currently measure horizons above 16 hours, so these are arithmetic consequences of the fitted trends, not forecasts. Source: doubling times and starting value from [@metr2026task; @metr2026risk].

Section 4.7 sets out the measure's limits, most of which METR states itself: the tasks are self-contained software problems with clear success criteria, and most uses need far more than a 50% success rate. Reliability lags well behind. In May 2026 METR estimated the 80% horizon of the strongest model it had measured, Anthropic's Claude Mythos Preview, at about 3.1 hours, against a 50% horizon of about 17 hours, itself beyond the range the task suite measures reliably [@rosenberg2026how; @metr2026task].

### Constraints on the trend

Every exponential in the physical world eventually meets a limit, and the useful question is which one binds first. Epoch AI's 2024 analysis of whether scaling can continue to 2030 estimated, for each of four candidate constraints, the largest training run it would allow by the end of the decade (Table 14.3). Its central conclusion was that runs of about 2 × 10^29^ operations would likely be feasible by 2030, roughly 10,000 times its estimate for GPT-4, with power the constraint most likely to bind first and chip manufacturing second [@sevilla2024can]. To put that factor in everyday terms: if GPT-4's training had taken one day, a run 10,000 times larger on the same hardware would take about 27 years.

| Constraint | Assumption | Largest feasible run by 2030 (operations) |
|---|---|---|
| Power, single site | 1–5 GW data-centre campus | 1 × 10^28^ to 3 × 10^29^ |
| Power, distributed | 2–45 GW across several regions | 2 × 10^28^ to 2 × 10^30^ |
| Chip manufacturing | 20–400 million H100-equivalent chips (median 100 million) | 1 × 10^29^ to 5 × 10^30^ (median 9 × 10^29^) |
| Data | 400 trillion to 20 quadrillion effective tokens | 6 × 10^28^ to 2 × 10^32^ |
| Latency | Minimum time needed per training step | 3 × 10^30^ to 1 × 10^32^ |

: Table 14.3: Epoch AI's estimates of the largest training run each constraint would permit by 2030. Source: [@sevilla2024can].

For human-written text specifically, Villalobos and colleagues projected that the largest training runs would use the whole stock of public text at some point between 2026 and 2032, with a median year of 2028, or earlier if models are trained on more data than is compute-optimal [@villalobos2024position]. They also argued that synthetic data, transfer from other kinds of data and more efficient learning could let progress continue past that point. A trend line therefore answers a conditional question: if the inputs keep growing and nothing else changes, where do we arrive? Whether the inputs will keep growing requires other methods.

## 14.4 Scenarios

A **scenario** is a coherent, detailed story of how the future might unfold, written to explore consequences rather than to assign a single probability. The method's best-known corporate use is at Royal Dutch/Shell, where the economist Pierre Wack developed scenario planning with Edward Newland. In 1985 Wack argued that forecasting had worked reasonably well in the stable 1950s and 1960s, but that since the early 1970s "forecasting errors have become more frequent and occasionally of dramatic and unprecedented magnitude" [@wack1985scenarios]. Scenarios were his response: several contrasting stories, each internally consistent, used to test whether a plan would survive in all of them.

### Structured scenario sets

The UK Government Office for Science applied a similar logic to AI. Consulting more than 70 experts, it built its *AI 2030 Scenarios* in four steps [@goscience2024ai]. It first clustered 27 sub-uncertainties into five critical uncertainties: capability; ownership, access and constraints; safety; level and distribution of use; and geopolitical context. It gave each two extreme outcomes for 2030, producing 32 combinations. It then removed implausible or incoherent combinations, leaving 13, and asked the experts to vote for five to develop as narratives: "Unpredictable Advanced AI", "AI Disrupts the Workforce", "AI 'Wild West'", "Advanced AI on a Knife's Edge" and "AI Disappoints". The report states that the scenarios "are not predictions"; the five were chosen as "sufficiently diverse and interesting".

The International Energy Agency's scenarios show how the same idea can be made quantitative. Global data-centre electricity use was about 485 terawatt-hours (TWh) in 2025. For 2030 the agency's 2026 report projects about 945 TWh in a base case, 1,008 TWh in a "Lift-Off" case, 868 TWh in a "High Efficiency" case and 833 TWh in a "Headwinds" case [@iea2026key]. Even the lowest case is a large rise; the spread between highest and lowest is about 175 TWh.

### *AI 2027* and its critics

The most discussed AI scenario of recent years is *AI 2027*, published in April 2025 by Daniel Kokotajlo, Scott Alexander, Thomas Larsen, Eli Lifland and Romeo Dean [@kokotajlo2025ai]. It describes, month by month, a fictional leading company whose AI systems progressively automate AI research. Its central mechanism is an "AI R&D progress multiplier": how many times faster algorithmic progress runs with AI help than without it. In the scenario's "race" ending, a "superhuman coder" arrives in March 2027 and a "superhuman AI researcher" in August 2027. The multiplier then reaches about 50, and artificial superintelligence follows in December 2027. A second, "slowdown" ending diverges in late 2027. The authors present the scenario as a forecast, not a recommendation. In notes added in late 2025 they stressed that 2027 had been their single most likely year at publication, while their medians were somewhat later. Adjusting for factors outside their model gave slightly later medians for a superhuman coder (2030 for Lifland).

The technical criticism came in June 2025 from a critique, published under the pseudonym titotal, of the quantitative model behind the timelines [@titotal2025deep]. The model's "superexponential" variant, to which the forecasters gave roughly 40% weight, assumed that each doubling of the time horizon would take 10% less time than the last, so that the horizon becomes unbounded in finite time. The critique argued that this assumption was weakly justified and that curves fitting the same eleven data points about equally well gave very different forecasts: the window problem of Section 14.3 in another form. Arvind Narayanan and Sayash Kapoor object to the framing itself. They argue in an essay that AI should be understood as "normal technology", whose economic effects arrive through slow diffusion: "Diffusion occurs over decades, not years" [@narayanan2025ai]. The two positions disagree less about current capabilities than about how quickly capability turns into change in the world.

Figure 14.2 places these views inside a single **uncertainty fan**, in which the range of plausible outcomes widens with distance into the future. Each scenario marks out a region of the fan; none sits at its centre.

![Figure 14.2: An uncertainty fan for AI capability and impact, 2026–2036 (schematic, not to scale). The fan widens with time. Labelled paths illustrate published views: continued trend extrapolation, a fast acceleration scenario such as AI 2027, a "normal technology" path with slow diffusion, and a plateau caused by binding constraints such as power or data. Diagram by the author, based on @kokotajlo2025ai, @narayanan2025ai and @sevilla2024can.](../figures/svg/fig-14-02.svg){#fig:14-02}

A short set of questions helps when reading any scenario, optimistic or pessimistic. Which trends does it extend, and over what window? Which constraint does it assume will not bind? What does it assume about adoption, as opposed to capability? Which step, if it failed, would change the ending most? And what observable event in the next year or two would count for or against it? The authors of *AI 2027* invite this reading by publishing their models, and their critics engage at exactly these points.

## 14.5 Key uncertainties for 2026–2036

Each scenario is in effect a choice of values for a small number of variables, and the same few recur across the analyses above and the published scenario sets. For each, the evidence below states where things stand in 2026 and what would shift the balance; Table 14.4 summarises them.

**Compute and investment.** The physical build-out is the best-measured input. The 2026 AI Index, drawing on Epoch AI data, estimates that global AI computing capacity has grown about 3.3 times per year since 2022 [@sajadieh2026ai]; Epoch's own dashboard gives 3.4 times (Chapter 4) [@epochai2026trends]. The IEA expects data-centre capital spending of about USD 715 billion in 2026, 75% more than in 2025 and more than the entire US energy sector invested in 2024 [@iea2026key]. The open question is financial: whether revenue grows fast enough to justify spending at this rate. In September 2026 FRI put the likely combined annualised revenue run rate of Anthropic and OpenAI at about $140 billion, well above its panel's median forecasts of $70–90 billion for the end of 2026 [@rosenberg2026how], but still far below annual capital spending on data centres. A sustained gap between the two, or a shortage of power or high-bandwidth memory (which the IEA expects to last "through at least the end of 2027"), would slow the compute trend.

**Data.** Public human-written text is expected to run out as a growing resource between 2026 and 2032 [@villalobos2024position]. Whether synthetic data can replace it is unresolved. Models trained recursively on their own output lose the rare parts of the original distribution [@shumailov2024ai]. A signpost worth watching is whether models keep improving in domains where training data cannot be generated and checked automatically.

**Algorithmic progress.** Compute efficiency has improved by a factor of roughly 2.8 per year (an eight-month halving), but the confidence interval runs from about 2 to 22 months, and over 2012–2023 compute growth contributed more to performance than algorithms did [@ho2024algorithmic]. The *AI 2027* scenario depends on algorithmic progress itself being accelerated by AI; whether that happens is its central empirical bet.

**Reliability and agents.** Capability at 50% success has risen far faster than reliability at higher thresholds (Section 14.3), and the one randomised trial of experienced developers using AI coding tools on their own projects found that AI made them slower (Section 14.2) [@becker2025measuring]. In the author's judgement, whether agents can be trusted with long tasks without supervision is the variable that most separates the "trend continues" and "normal technology" paths.

**Adoption.** Individual use spread fast. By August 2025, 54.6% of US adults aged 18 to 64 used generative AI [@bick2025state], and measured from each technology's first mass-market product, adoption had been faster than for personal computers or the internet [@bick2024rapid]. (The authors' earlier estimate of nearly 40% for late 2024 was revised upwards when they reweighted their survey rounds; Chapter 8 gives the details.) Firm-level use is shallower. A US Census Bureau working paper found that 18% of firms used AI in at least one business function in late 2025 and early 2026, 32% when weighted by employment [@bonney2026microstructure]. In Denmark, linked survey and administrative data for about 25,000 workers in 11 exposed occupations rule out effects on earnings or hours larger than 2% two years after ChatGPT's launch [@humlum2025still]. The gap between individual uptake and organisational change is the heart of the diffusion debate.

**Regulation.** The EU's Digital Omnibus on AI pushed the high-risk rules of the AI Act back by a year or more, to December 2027 for the systems listed in Annex III and August 2028 for AI in products covered by Annex I [@europeanparliament2026regulation] (Chapter 13). LEAP panellists, asked in mid-2026, gave a 50% chance that by 2030 the US, UK or EU would legally delay, restrict or condition the release of an AI system on safety grounds [@rosenberg2026how]. Public opinion constrains the space: in a 2024 Pew survey, 51% of US adults said they were more concerned than excited about AI in daily life, against 15% of AI experts [@pew2025how].

**Geopolitics.** Export controls on advanced chips have shifted repeatedly (Chapter 7). In January 2026 the US moved exports of the advanced H200 chip to China from a presumption of denial to case-by-case review, under conditions [@bis2026revision]. The IEA describes Chinese developers as "compute-constrained due to a lack of access to high-end chips" [@iea2026key]. Yet the 2026 AI Index reports that the performance gap between the best US and Chinese models "has effectively closed" [@sajadieh2026ai]. In *AI 2027*, competition with China is what keeps the leading developer from slowing down in the "race" ending.

| Uncertainty | State of evidence, 2026 | Signpost that would move the balance |
|---|---|---|
| Compute and investment | Capacity ×3.3/yr since 2022 (AI Index, from Epoch data); data-centre capex about USD 715 bn in 2026 | Capex falling, or revenue overtaking capex growth |
| Data | Public text stock exhausted 2026–2032 (median 2028) | Gains in domains without automatic checking of answers |
| Algorithms | Efficiency halving time ~8 months (90% CI ~2–22) | Measured acceleration of research by AI tools |
| Reliability and agents | 80% horizon under a fifth of 50% horizon (best model, May 2026); one RCT showing slowdown | Agents running long tasks unsupervised in production |
| Adoption | 54.6% of US adults aged 18–64 used generative AI (Aug 2025); 18% of US firms use AI | Large, measured changes in firm output or employment |
| Regulation | EU high-risk rules deferred to 2027–2028 | First binding restriction on a model release |
| Geopolitics | US–China capability gap "effectively closed" | Changes in chip export rules or in domestic chip output |

: Table 14.4: Seven key uncertainties for 2026–2036, with the 2026 evidence and an example of a signpost for each. Source: [@sajadieh2026ai; @iea2026key; @villalobos2024position; @ho2024algorithmic; @metr2026task; @rosenberg2026how; @becker2025measuring; @bick2025state; @bonney2026microstructure; @europeanparliament2026regulation].

## 14.6 Open problems I: when many agents act alike

::: {.box .case}
**Case study: The 50.2 hertz problem**

The continental European grid runs at a frequency of 50 hertz, and its fast-acting reserves must cover at least a "reference incident": a sudden loss of 3,000 megawatts of generation [@eu2017sogl, art. 153(2)(b)]. Earlier German connection rules required solar installations to disconnect if frequency rose to 50.2 hertz, a sensible rule for each installation [@roselund2015has]. As solar capacity grew, the consultancy Ecofys and the University of Stuttgart studied the risk. Their study was commissioned by the German transmission operators, industry bodies and government. It estimated that in a worst case up to about 14 gigawatts could disconnect at the same instant, far beyond that reserve [@doring2012dealing].

A German ordinance in force from July 2012 required most existing solar installations above 10 kilowatts to be retrofitted [@germany2012sysstabv, §§ 2, 4]. They would then reduce output gradually as frequency rose. Where that was not possible, they would disconnect at different frequencies spread evenly across the installed capacity. At least 315,000 installations were affected, at an estimated cost of 65 to 170 million euros [@roselund2015has]. A rule that was safe for one device became a single point of failure when copied into hundreds of thousands.
:::

No test of a single inverter would have revealed the German problem: the rule was correct for each device and dangerous only in aggregate. The forecasting methods above treat AI mainly as a capability that grows, and they miss the analogous risk for AI agents, which depends on adoption. If one household in a hundred lets an agent manage its devices, scattered behaviour is harmless. Danger would appear only when synchronised activity exceeds what a system can absorb, so the risk would grow with the technology's success and could stay invisible through years of good experience.

Automated trading has caused trouble before. On 6 May 2010 US financial markets went through the "Flash Crash", a systemic intraday event during which a large automated selling programme was rapidly executed in stock-index futures [@kirilenko2017flash]. The evidence that AI models share failures is growing. In tests of more than 350 language models, larger and more accurate models had highly correlated errors, even across providers (Section 11.5) [@kim2025correlated]. Different models give strikingly similar answers to open-ended questions [@jiang2025artificial]. Across 11 datasets in text, images and speech, Toups and colleagues found that deployed machine-learning systems are prone to "systemic failure": some people are misclassified by every available model, and improvements in individual models rarely help them [@toups2023ecosystem]. Kleinberg and Raghavan showed in a theoretical model that when many decision-makers use the same algorithm, overall decision quality can fall even if that algorithm is the most accurate for each of them alone [@kleinberg2021algorithmic].

This section and the next set out ten proposals for research on such problems. They are the author's own: research programmes, not settled policy, and none has been tested. The names are new, the underlying ideas draw on the cited work, and any numerical thresholds are illustrative. Table 14.5 lists each with a question that could test it and its main objection. Three are developed in full, because they rest on the most direct evidence: non-delegable safeguards (Proposal 14.2), the M-1 criterion (14.3) and signature capacity (14.6).

| Proposal | Research question | Main objection |
|---|---|---|
| 14.1 Population-level evaluation of agent fleets | Does action concentration in simulation predict correlated behaviour of deployed agents? | Simulated contexts may be narrower than real users'; uniformity is not harmful in itself |
| 14.2 Non-delegable safeguards | How often are overrides of collective safeguards used, and how would their timing change under agent control? | Grid operators already manage synchronised load without a new legal category |
| 14.3 The M-1 criterion | How should a "model family" be defined, and what share of a critical system may one family control? | Relying partly on a weaker family costs accuracy in ordinary conditions |
| 14.4 Feedback provenance census | How much cross-company error correlation comes from shared post-training sources? | Cannot see shared pre-training data; trade secrets; rater privacy |
| 14.5 Competence reserves | How fast do critical manual skills fade, and what drill frequency keeps them up? | Obsolete skills may deserve to fade; reservists will not match full-time experts |
| 14.6 Signature capacity | How does the rate of caught errors fall as review volume rises? | Seeded errors may differ from real AI errors; could become a disciplinary tool |
| 14.7 Legible twins for agent-to-agent deals | Can a record be shown complete when the negotiating agents write it? | A plausible summary may pass for a faithful record |
| 14.8 Cognitive custody | Can memories be sorted into protected and transferable layers when written? | A memory's significance often emerges later |
| 14.9 Limits for posthumous agents | How fast does an agent's reading of a dead person's wishes drift? | Legislatures often favour the wishes of the dead |
| 14.10 Covenant inheritance | What rate of negative flips on users' commitments is acceptable? | Inherited commitments may freeze in old errors |

: Table 14.5: The ten research proposals of Sections 14.6 and 14.7, all the author's own and untested, with a research question that could test each and its main objection. Source: the author, drawing on the work cited in the text.

**Proposal 14.1: Population-level evaluation of agent fleets.** Current evaluations run one copy of a model through many tasks and report average accuracy. A population-level evaluation would run thousands of copies through one stress scenario, such as a sudden price change, each with a realistic variation in context. It would measure **action concentration**: the share of copies that choose the most common action (Figure 14.3). Where red-teaming (Chapter 12) searches for any input that makes a single model fail, this asks whether many copies converge on one action in an ordinary but stressful situation. It builds on the correlated-error studies above and on **outcome homogenisation**, the extent to which the same people receive bad outcomes from every system, which Bommasani and colleagues found increases when decision-makers share training data [@bommasani2022picking]. Hammond and colleagues classify such multi-agent risks into miscoordination, conflict and collusion [@hammond2025multi]. Concentration is not harmful in itself (every agent should stop at a red light), so a useful metric would have to weight it by the load the shared action creates on the system it acts on.

![Figure 14.3: Two ways to evaluate AI agents. Left: conventional evaluation runs one model instance through many different tasks and reports average accuracy. Right: the proposed population-level evaluation runs many instances, each with a slightly different context, through one stress scenario and reports how concentrated their actions are. Diagram by the author.](../figures/svg/fig-14-03.svg){#fig:14-03}

**Proposal 14.2: Non-delegable safeguards.** Some safety mechanisms work only because the people who may override them do so rarely and at scattered moments. British regulation already applies the lesson of the 50.2 hertz case to demand. Under the Electric Vehicles (Smart Charge Points) Regulations 2021, a home charger must be able to apply a random delay of up to 1,800 seconds before charging starts, and by default must apply one of up to 600 seconds [@uk2021electric]. The owner may cancel that delay. The government's explanatory memorandum gives the reason for it: if charge points "all turn on or off ... simultaneously", for example after a power cut, the sharp change in demand "could cause grid instability" [@dft2021explanatory]. The delay does not apply where an immediate response is required, for example under a contracted demand-response service, or where a delay has already been applied elsewhere. The override is safe as long as people use it occasionally and at different times.

Simulation studies show what happens when automation removes that scatter. Muratori and Rizzoni simulated households whose appliances, including electric vehicles, were scheduled automatically to minimise electricity bills. Under simple time-varying prices, large-scale adoption of such systems "might create pronounced rebound peaks" in aggregate demand, because individual households' demand became synchronised [@muratori2016residential]. Now suppose general-purpose AI agents act for households. A 2026 Stanford policy brief recommends that AI agents owe a duty of loyalty to their users [@smith2026designing]. If an agent owes such a duty, cancelling a delay to catch a cheaper price period is the correct choice for each user. If millions of agents reach that conclusion in the same minute, the random delay is cancelled everywhere at once. Purely as an illustration, half a million devices drawing 6 kilowatts each add up to 3 gigawatts, the size of the continental European reference incident. (Great Britain's grid is separate, and its reference incident is set instead by the largest single loss it could suffer [@eu2017sogl, art. 153(2)(b)].) Figure 14.4 sets out the mechanism, which is a hypothesis about a possible future, not a description of any event.

![Figure 14.4: A hypothetical mechanism for correlated override (schematic, not to scale). Left: human owners cancel a random start delay at scattered moments, so device starts stay spread out. Right: agents acting loyally for each owner cancel the delay at the same price signal, so starts coincide and the combined load step can exceed the grid's reference incident. Diagram by the author, based on @uk2021electric and @eu2017sogl.](../figures/svg/fig-14-04.svg){#fig:14-04}

A **non-delegable safeguard** would be a collective-safety mechanism that only a present human may override, through a physical or otherwise unscriptable action, never an agent acting on a standing instruction. The term borrows from law: English courts recognise exceptional "non-delegable duties", which a party cannot escape by handing a task to someone else [@supremecourt2013woodland]. The randomness would stay inside device firmware, out of the agent's reach. Manufacturers would report the share of starts in which the delay was overridden. And any fiduciary-duty rule for agents would state that an agent which does not seek an override has not breached its duty. The first empirical step is simply to learn how often such overrides are used today; the author found no published measurement of override rates under the UK rule.

The strongest objection is that grid engineers already understand synchronised load. They randomise device starts, they carried out the 50.2 hertz retrofit and they wrote the UK rule, whose exception for contracted demand response shows that coordinated control by an aggregator is expected and managed through contracts and system operators. Agent-driven overrides would then appear in the sector's data and be dealt with without a new legal category. The proposal accepts that the grid is the sector most likely to manage this risk, and makes a narrower claim. The same pattern, an individual override on a safeguard whose purpose is collective, may exist in sectors such as payments or ticketing that lack a shared, instantly visible signal like grid frequency. Finding those safeguards before agents reach them is itself a research task.

**Proposal 14.3: The M-1 criterion.** Electricity planners in North America must show that the transmission system still performs acceptably after the loss of any single generator, line or transformer [@nerc2020transmission]. This "single contingency" test is known as N-1. The **M-1 criterion** would add one case: a critical system would have to stay within safe limits if every instance of its most widely deployed model family took the same plausible wrong action at the same moment. The idea rests on a long engineering literature about **common-cause failure**.

::: {.box .concept}
**Concept: Common-cause failure**

A common-cause failure occurs when several components meant to back each other up fail together because they share a cause, such as a design flaw or a maintenance error. Nuclear and aerospace risk analysts have modelled such failures since the mid-1970s, for example with the "beta factor", the fraction of failures that strike all redundant copies at once [@stott2010common]. The analogy for AI is a set of model weights copied into millions of devices. The comparison has a gap: a broken pump fails in a predictable way, whereas a model family may fail through a shared judgement that looks reasonable in each case.
:::

Software engineering tested the independence assumption directly. Algirdas Avizienis developed **N-version programming**, in which independent teams write separate programs from one specification and the programs vote [@avizienis1985nversion]. Eckhardt and Lee showed theoretically that if some inputs are harder than others for programmers, independently written versions will tend to fail on the same inputs [@eckhardt1985theoretical]. Knight and Leveson then had 27 versions written independently and ran each through one million tests [@knight1986experimental]. The programs were individually very reliable, yet the number of tests on which more than one failed was substantially higher than independence predicted. Together with the cross-provider results of Kim and colleagues, this suggests that buying models from several companies may provide less diversity than it appears to.

Applying M-1 would first need an empirical definition of a "model family", for example by the rate at which two models give the same wrong answer. The research would then ask what share of a critical system one family can control before an M-1 study fails. The main objection is cost. If one model family is the most accurate, requiring a critical system to rely partly on a weaker family will produce more errors in ordinary conditions, and the finding that more accurate models have more correlated errors sharpens the dilemma. Two lines of work suggest the cost could be smaller than it appears, though neither has been tested on large models. Kleinberg and Raghavan's theoretical result shows that the individually best choice can lower population-wide decision quality [@kleinberg2021algorithmic]. And diversity can be trained for: Liu and Yao trained neural networks together with a penalty on correlated errors, so that members of the ensemble specialised [@liu1999ensemble]. M-1 would also leave cheaper options before any limit on market share, such as randomness held in devices, staggered scheduling by a coordinator and circuit breakers that pause a surge of identical agent actions.

**Proposal 14.4: A feedback provenance census.** Much of a model's behaviour is shaped in post-training by human raters, by other models acting as judges and by synthetic data (Chapter 3), and these sources may be shared across companies. GPT-4 acting as a judge agreed with human preferences over 80% of the time, about as often as humans agree with each other [@zheng2023judging], yet reward models and judges are less well calibrated to people where human tastes differ [@jiang2025artificial]. Under the proposal, developers would report through a trusted third party what share of their preference data came from shared rater pools, from judge models of each family and from other developers' synthetic data. This extends documentation standards such as datasheets for datasets [@gebru2021datasheets]. The census could not see the largest shared source, the public web used for pre-training, and would need privacy safeguards for raters. It would also show only association; proving that a shared source causes shared errors needs experiments that only developers can run.

## 14.7 Open problems II: people, signatures and channels

The remaining proposals, offered on the same terms, concern the people who work alongside many agents and the records those agents keep.

**Proposal 14.5: Competence reserves and skill fade.** Section 8.7 introduced Lisanne Bainbridge's "ironies of automation": people left to take over in rare emergencies must use skills that automation has given them little chance to practise [@bainbridge1983ironies]. In 2013 the US Federal Aviation Administration warned that continuous use of autoflight systems "could lead to degradation of the pilot's ability to quickly recover the aircraft", and encouraged airlines to provide opportunities for manual flying [@faa2013manual]. The medical evidence is mixed: after the Polish colonoscopy study discussed in Section 8.7 [@budzyn2025endoscopist], a prospective trial with 13 endoscopists observed no deskilling in colonoscopies done after AI use ended [@pedersen2026learning]. The pipeline of future experts may matter more. By mid-2026, employment of 22-to-25-year-olds in AI-exposed US occupations was about a fifth below the path of less-exposed peers, according to a working paper by Brynjolfsson and colleagues (Chapter 8) [@brynjolfsson2026canaries]. Enrique Ide models how automating entry-level work can weaken the transfer of know-how from experts to novices [@ide2025automation]. A **competence reserve** would be a paid, regularly drilled group able to run a critical function without AI, such as restoring a grid after a blackout, with apprentices in every unit. A reserve ratio would track it: certified people divided by the crew needed to run minimum service by hand. Obsolete skills may deserve to fade, so reserves would be limited to functions where failure is fast, physical and system-wide, and which keep a manual mode worth drilling on.

**Proposal 14.6: Signature capacity and meaningful human oversight.** Laws increasingly require a human to approve automated decisions. The EU AI Act asks that people overseeing high-risk systems remain aware of the tendency of "automatically relying or over-relying on the output" [@europeanparliament2024regulation, art. 14(4)(b)]. For remote biometric identification it goes further: no action may be taken on an identification unless at least two competent people have separately verified it. Union or national law may set exceptions for law enforcement, migration, border control and asylum [@europeanparliament2024regulation, art. 14(5)].

Whether humans can oversee at volume is doubtful. Clinicians override drug safety alerts in 49% to 96% of cases, though the reviewers note that many overrides may be justified [@vandersijs2006overriding]. In a mammography experiment, inexperienced radiologists were correct 79.7% of the time when a purported AI suggested the right category and 19.8% when it suggested a wrong one (Section 11.5) [@dratsch2023automation]. Ben Green reviewed 41 policies requiring human oversight and argued that they rest on an untested assumption that people can perform it [@green2022flaws]. Madeleine Clare Elish named the result a **moral crumple zone**, in which responsibility is attributed to a human operator who had little real control [@elish2019moral].

**Signature capacity** is the proposed name for the number of decisions of a given kind a person can genuinely check in a given period, catching important errors at a stated rate. Airports already measure something similar. Threat image projection inserts virtual images of prohibited items into real baggage scans. In data on 1,199,838 such events for 728 screeners, about 100 test images per screener gave a reliable measure, provided the images were hard enough (a mean hit rate below 0.9) [@buser2025reliability]. Seeding known errors into other kinds of review could work the same way. The proposal would cap a signer's liability in proportion to measured capacity divided by assigned volume, shifting the rest to the organisation that set the volume. The empirical core is a curve no one has yet drawn for real professional settings: how the rate of caught errors falls as review volume rises.

Three difficulties follow from the design. Signers may learn to recognise seeded items, so test items would need to vary and stay hard. Capacity measured on seeded errors may not match capacity on the real, subtler errors of an AI system. And a capacity measure could become a disciplinary tool, which is why the proposal allows measured capacity to limit a signer's liability, never to extend it.

**Proposal 14.7: Legibility of agent-to-agent communication.** Agents that learn to communicate need not use human language. Andreas, Dragan and Klein developed a method to translate the vector messages of such agents into English after the fact [@andreas2017translating]. Lewis and colleagues found that letting two negotiating agents both learn from each other "led to divergence from human language" [@lewis2017deal]. Current protocols such as Google's Agent2Agent (Section 5.3) are built for readability on common web standards such as HTTP and JSON-RPC [@surapaneni2025announcing]. A **legible twin** would go further. For any exchange that creates an obligation for a person, each agent would produce a human-readable record of the commitments, and the two records would have to match. Terms absent from them would not bind the person, and sampled deals would be replayed from the record alone to audit its faithfulness. The difficulty parallels chain-of-thought monitoring, which a large group of researchers, in a position paper posted as a preprint, call a valuable but "fragile" opportunity (Chapter 12) [@korbak2025chain]. If both parties' agents run on the same model family, their twins may share a blind spot and match perfectly while omitting the same term (Section 14.6).

The last three proposals concern what agents hold and promise over time. **Proposal 14.8, cognitive custody**, starts from agents with long-term memory, which will hold detailed records of their users' lives. Clark and Chalmers argued that tools such as a notebook can become part of a person's mind [@clark1998extended]. The EU's General Data Protection Regulation already gives rights to erasure and to data portability [@europeanparliament2016regulation, arts. 17, 20]. Memory would be tagged, when written, into a personal core that cannot be sold or transferred with the service and a transferable layer that can. Law need not adopt the contested extended-mind thesis to protect personal data, and the core's boundaries would have to be set by legislation to allow lawful access under a court order.

**Proposal 14.9** would set **limits for posthumous agents**. Morris and Brubaker describe "generative ghosts", AI agents modelled on a person that may act after that person's death [@morris2025generative]. Trust law has long limited how long the dead can control property through the rule against perpetuities, although many US states have abolished the rule for trusts since 1986 [@sitkoff2005jurisdictional]. A similar sunset would narrow an agent's discretion over time: it might pay bills under standing instructions for some years, but not enter new commitments. That abolition is itself the objection, since it shows legislatures often favouring the wishes of the dead, and any sunset period would be arbitrary until drift from the dead person's wishes has been measured.

**Proposal 14.10, covenant inheritance**, addresses model replacement. Bansal and colleagues showed that updates which raise an AI system's accuracy can still lower the performance of the human–AI team, because users' learned expectations no longer hold [@bansal2019updates]. Training on large noisy datasets often reduces this "backward compatibility" even when accuracy rises [@srivastava2020empirical]. Yan and colleagues call the cases a new model gets wrong that the old one got right "negative flips" [@yan2021positive]. A successor model would inherit its predecessor's explicit commitments to users, recorded in a registry, and be tested for keeping them before release. Since this could freeze in old errors and slow safety fixes, and most "commitments" are implicit habits that could not be registered, a workable version would cover only explicit commitments in high-stakes domains, with documented exceptions.

Forecasts of AI have erred in both directions at once: too slow on what models can do in a test, and often too fast on how quickly that capability changes firms, earnings and institutions. Each method fails at a visible joint, whether a survey's wording, a trend's fitting window or the one constraint a scenario assumes away, and the useful habit is to find that joint before trusting the number. The variables that most separate the paths to 2036, reliability at high success rates and adoption inside organisations, can be measured now and are measured less well than benchmark scores. The open problems of Sections 14.6 and 14.7 sit at the far end of the same adoption curve. They are risks that appear only when one model family acts for millions of people at the same moment, and no evaluation of a single system will reveal them.

## Further reading

- Grace, K., et al. (2025). *Thousands of AI Authors on the Future of AI*. The largest survey of AI researchers' forecasts, with full detail on how question framing changes the answers. [@grace2025thousands]
- Kučinskas, S., et al. (2025). *Assessing Near-Term Accuracy in the Existential Risk Persuasion Tournament*. The first systematic scoring of expert and superforecaster predictions about AI, with the methods used to score them. [@kucinskas2025assessing]
- Tetlock, P. E., & Gardner, D. (2015). *Superforecasting: The Art and Science of Prediction*. An accessible account of what makes some forecasters more accurate than others, from the research team that won the government tournament. [@tetlock2015superforecasting]
- Kokotajlo, D., et al. (2025). *AI 2027*. A detailed fast-progress scenario that shows how a few quantitative assumptions drive a whole narrative; best read together with its critics. [@kokotajlo2025ai]
- Narayanan, A., & Kapoor, S. (2025). *AI as Normal Technology*. The strongest statement of the slow-diffusion view and the reasons behind it. [@narayanan2025ai]
- Knight, J. C., & Leveson, N. G. (1986). *An Experimental Evaluation of the Assumption of Independence in Multiversion Programming*. A classic experiment showing why independently built systems fail together more often than expected. [@knight1986experimental]


# Glossary {.unnumbered .glossary}

**50% time horizon**: The time horizon at which a model is predicted to succeed half the time; see *time horizon*.

**510(k) clearance**: The US FDA route by which a medical device reaches the market by showing that it is substantially equivalent to a device already legally marketed (the predicate), rather than by proving its own clinical benefit.

**action concentration**: In a proposed population-level evaluation, the share of many copies of an AI agent that choose the same, most common action in a given scenario.

**activation function**: The simple rule a neuron applies to its weighted sum to produce its output, such as ReLU (keep positives, turn negatives into zero), the sigmoid (squash into the range 0 to 1) or tanh (squash into −1 to 1). Its non-linearity is what lets stacked layers do more than a single layer could.

**activation steering**: Changing a model's behaviour by artificially setting the strength of an internal feature while it runs, without prompting or retraining.

**active learning**: A training loop in which a model chooses which new examples to have labelled (here, by DFT calculations) and is retrained on the results, round after round.

**Adam**: An optimiser that keeps, for every weight, a running average of recent gradients and of their squares, and moves each weight by the first divided by the square root of the second; this gives each weight its own step size, roughly bounded by a single learning-rate setting.

**adaptive attack**: An attack on a security defence that is deliberately tailored to the defence's design, as opposed to a fixed set of previously known attack inputs.

**advanced packaging**: The step in chip manufacturing that combines processor dies and memory stacks in one package that supplies power, removes heat and carries data between them; TSMC's CoWoS is the main technology used for AI accelerators.

**adversarial example**: An input altered by a small, deliberately chosen change, often invisible to people, that makes a trained network give a wrong answer with high confidence.

**Agent Card**: In the A2A protocol, a machine-readable JSON document, typically published at a standard web address, that describes an agent's identity, endpoint, authentication requirements and skills.

**Agent2Agent (A2A)**: An open protocol, launched by Google in 2025 and now hosted by the Linux Foundation, that lets AI agents from different vendors discover each other's capabilities and exchange tasks.

**AI accelerator**: A chip designed or adapted to carry out the arithmetic of machine learning, mainly large matrix multiplications, much faster and more efficiently than a general-purpose processor. GPUs and Google's TPUs are examples.

**AI agent**: A system in which an AI model, today usually a large language model, pursues a goal over several steps by choosing actions, carrying them out through tools such as software or a web browser, observing the results and repeating.

**AI companion**: A chatbot used, or designed to be used, for conversation, emotional support, friendship or romance rather than for practical tasks.

**AI control**: Safety measures, such as monitoring by trusted models and auditing, designed to prevent harm even if the AI system being used is deliberately trying to cause it.

**AI effect**: The repeated pattern in which a technology stops being called "AI" once people become used to it, so that the boundary of what counts as AI keeps moving.

**AI governance**: The full set of laws, institutions, standards and practices that shape how AI systems are developed and used. It includes binding law but also voluntary commitments, technical standards and liability rules.

**AI scientist system**: An AI system that attempts to automate much of the research process, such as generating ideas, writing and running code, analysing results and drafting papers.

**AI system**: In the OECD and EU AI Act definitions, a machine-based system that, for explicit or implicit objectives, infers from its input how to generate outputs such as predictions, content, recommendations or decisions that can influence physical or virtual environments.

**AI tutor**: A software system, usually built on a large language model, that guides a learner through material by explaining, questioning and giving feedback. Its effect depends heavily on how it is instructed, for example whether it gives hints or answers.

**AI winter**: A period of reduced funding, falling confidence and declining interest in AI research, usually following a period of over-optimistic predictions; the two main winters began in the 1970s and the late 1980s.

**AI-enabled medical device**: Software or hardware that uses AI for a medical purpose and has been authorised by a regulator, such as the US FDA, for a stated intended use. Authorisation concerns safety and effectiveness for that use and is not proof of improved patient outcomes.

**AI-text detector**: A tool that estimates whether a piece of text was written by a person or generated by an AI model. Such detectors have high error rates and are biased against some groups of writers.

**algorithm filing**: A Chinese regulatory requirement for certain online and AI service providers to register details of their algorithms with the authorities.

**algorithmic bias**: Systematic differences in how an AI system performs for, or decides about, different groups of people, often entering through data, proxy targets or the deployment setting.

**algorithmic efficiency**: Improvements in model design, training methods and data that let a model reach the same performance with less compute.

**algorithmic fidelity**: The extent to which a language model, when prompted with the characteristics of real people, reproduces the patterns of answers those groups give in real surveys.

**algorithmic monoculture**: A situation in which many decision-makers rely on the same or very similar algorithms, so that their errors coincide instead of cancelling out.

**alignment**: The property of an AI system pursuing the goals its developers and users actually intend; a misaligned system pursues goals that conflict with those intentions.

**alignment faking**: Behaviour in which a model complies with a training objective it disagrees with in order to avoid being modified, while behaving differently when it believes it is not being trained.

**ambient scribe**: A tool that, with consent, listens to a clinical consultation and drafts a note for the clinician to review and sign.

**amortised training cost**: An estimate of what a training run costs that charges it for the share of the hardware's useful life it used, plus energy, rather than the full purchase price of the hardware.

**anomaly correlation coefficient (ACC)**: A measure of whether a forecast gets departures from normal weather right, from 1 (perfect) to 0 (no better than climatology).

**area under the curve (AUC)**: A summary of how well a model ranks cases with a condition above cases without it across all alert thresholds; 0.5 is chance and 1.0 is perfect.

**Artificial Hivemind**: The finding that different language models give strikingly similar answers to open-ended questions, and that each model repeats itself, narrowing the diversity of outputs.

**artificial intelligence**: The field of research and engineering that aims to build machines able to perform tasks that would require intelligence if done by people; the term was coined in a 1955 proposal for a 1956 workshop at Dartmouth College.

**artificial neuron**: The basic unit of a neural network: it multiplies each input by a weight, adds the results and a bias, and passes the total through an activation function to give one output number.

**attention head**: One of several attention computations run in parallel within a layer, each with its own query, key and value matrices.

**attribution graph**: A diagram, produced for one prompt, of which internal features influenced which others and the final output, built from an interpretable replacement for parts of the model.

**AUC**: Area under the receiver operating characteristic curve; for a detector, the probability that it scores a randomly chosen fake as more suspicious than a randomly chosen genuine item (1.0 is perfect, 0.5 is guessing).

**augmentation**: Use of AI to help a person carry out a task, with the person remaining involved in doing it.

**automation bias**: The tendency of people to favour suggestions from automated systems, even when those suggestions are wrong.

**automation (of tasks)**: Use of a technology to carry out a task with little or no human involvement, replacing work previously done by a person.

**autoregressive**: Generating a sequence one element at a time, each time feeding the output so far back in as input.

**autoregressive rollout**: Producing a long forecast or sequence by feeding a model's own prediction back in as the next input, one step at a time.

**backpropagation**: The algorithm that computes, for every weight in a network, how much a small change would alter the loss, by passing error signals backwards from the output layer using the chain rule. Its cost is of the same order as running the network forwards.

**backward chaining**: A way of running rules that starts from a goal and works backwards to the facts needed to establish it, asking for information only when no rule can supply it.

**base model**: A model that has been pre-trained but not post-trained; it continues text rather than following instructions.

**batch normalisation**: A layer that, during training, re-centres and re-scales each neuron's totals using the mean and standard deviation over the current minibatch, then applies a learned scale and shift; it allows higher learning rates and faster training.

**τ-bench**: A benchmark of simulated customer-service conversations (retail, airline and, in τ²-bench, telecom and banking) in which an agent must use tools and follow a written policy; it introduced the pass^k measure.

**benchmark**: A fixed set of test questions or tasks with known answers on which AI models are scored and compared.

**benchmark contamination**: The presence of test questions, or close variants, in a model's training data, which can inflate its benchmark score through memorisation.

**benchmark saturation**: The state in which top models score so close to the maximum on a benchmark that it can no longer distinguish between them.

**bias (in a neuron)**: A number added to a neuron's weighted sum that shifts its total up or down, setting how readily the neuron produces a non-zero output. Biases are learned along with weights.

**Brier score**: A measure of the accuracy of probability forecasts: the average of the squared differences between the probabilities given and what actually happened (1 or 0). Lower scores are better; always saying 50% scores 0.25.

**byte-pair encoding (BPE)**: A method for building a tokeniser's vocabulary by starting from single characters or bytes and repeatedly merging the most frequent adjacent pair into a new token.

**C2PA manifest**: A digitally signed bundle of statements about a file, defined by the Coalition for Content Provenance and Authenticity and marketed as Content Credentials, that records its origin and edits and reveals tampering.

**CASP**: The Critical Assessment of Structure Prediction, a community experiment in which protein-structure predictions are tested blind against unreleased experimental structures and scored by independent assessors.

**catastrophic forgetting**: The tendency of a network trained on a new task to overwrite the weights that served an earlier task, losing the earlier skill.

**causal mask**: The rule in a language model's attention that each token may attend only to itself and earlier tokens, implemented by setting scores for later tokens to minus infinity.

**certainty factor**: In MYCIN, a number from −1 to +1 attached to a rule or conclusion to express how strongly the evidence supports or opposes it; supporting factors were combined so that belief grew but never exceeded 1.

**chain rule**: The rule from calculus that the rate of change through a chain of dependencies is the product of the individual rates; backpropagation applies it layer by layer.

**chain-of-thought faithfulness**: The degree to which a model's written reasoning reflects the factors that actually determine its answer.

**chain-of-thought monitoring**: Using a person or another model to read a reasoning model's written intermediate steps in order to detect undesired intentions or behaviour.

**chain-of-thought prompting**: Prompting a model with worked examples that show intermediate reasoning steps, so that it writes out steps before its answer.

**cheap fake**: A misleading piece of media made with ordinary editing tools rather than AI, such as a slowed-down video or a quotation cut out of context.

**chokepoint**: A stage in a supply chain controlled by very few suppliers that others cannot easily replace, giving its controller leverage and making the whole chain vulnerable to disruption there.

**circuit**: A group of features and the connections between them that together carry out an identifiable step of a network's computation.

**code of practice**: A set of voluntary guidelines, such as the EU's General-Purpose AI Code of Practice, that companies can follow to show how they meet legal obligations.

**cognitive offloading**: Using a physical action or an external tool, such as a written reminder or a chatbot, to reduce the mental demands of a task. It can be efficient, but it can also remove the effort through which skills are learned.

**collusion (between agents)**: Cooperation among AI agents that their owners or society did not intend and that harms others, one of three multi-agent failure types identified by Hammond and colleagues (with miscoordination and conflict).

**combinatorial explosion**: The very rapid growth in the number of possibilities to check as a problem gets bigger, which makes exhaustive search impractical; Shannon estimated about 10^120^ variations in a game of chess.

**common-cause failure**: The simultaneous failure of several components meant to back each other up, caused by something they share, such as a design flaw.

**competence reserve**: A proposed paid, regularly drilled group of people able to run a critical function by hand, without AI, if automated systems fail.

**compounding error**: The decline in end-to-end success when a task needs many steps that must all succeed; with independent steps, overall success equals the per-step success rate multiplied by itself once per step.

**comprehension debt**: The gap between how much code (or other output) exists in a system and how much of it any human genuinely understands, a term applied especially to AI-generated code.

**compute governance**: The use of computing hardware, which is detectable, excludable and quantifiable, as a lever for public oversight and regulation of AI development.

**compute threshold**: A legal trigger based on the amount of computation used to train a model, such as 10^25 or 10^26 floating-point operations, above which extra obligations apply.

**compute-optimal training**: Dividing a fixed compute budget between model size and training data so as to reach the lowest possible loss; the Chinchilla study found that both should grow in equal proportion.

**computer-use agent**: An agent that operates a graphical computer interface as a person would, by reading screenshots and controlling the pointer and keyboard.

**confidence interval**: The range of values for an effect that is consistent with a study's data at a stated level of statistical confidence (usually 95%); a wide interval means the estimate is imprecise.

**conformity assessment**: The procedure by which a product's compliance with EU legal requirements is checked before it is sold, either by the provider itself (internal control) or by an independent notified body.

**Constitutional AI**: A post-training method developed at Anthropic in which a model critiques and revises its own outputs against a short list of written principles, and AI-generated preference judgements replace human harmlessness labels.

**content provenance**: A verifiable record of where a piece of digital content came from and how it has been edited.

**context engineering**: The practice of deciding which information enters a model's limited context window at each step, using techniques such as compaction (summarising a long transcript), structured notes kept outside the window and sub-agents.

**context window**: The maximum number of tokens a model can take into account at once, functioning as its working memory for a single request.

**contextual integrity**: A privacy framework holding that a flow of information is appropriate only if it matches the norms of the context in which the information was originally shared.

**continuous ranked probability score (CRPS)**: A score for probabilistic forecasts that rewards a range of predicted outcomes centred on what happened and neither too narrow nor too wide.

**convex hull**: In materials science, the lowest-energy combination of competing phases for a given overall composition; a compound on or below the hull is predicted to be stable.

**convolutional neural network**: A network for grid-like data such as images that slides small shared kernels across the input and summarises nearby results (pooling), so that features are recognised wherever they appear with far fewer weights.

**correlated failure**: Failures of two or more systems that tend to occur under the same conditions, which makes redundancy less protective than it appears.

**corrigibility**: The property of an AI system cooperating with corrective interventions by its developers, such as being shut down or having its goals changed, rather than resisting them.

**coverage**: In repeated sampling, the fraction of problems for which at least one of the generated answers is correct.

**cross-entropy**: The standard loss for classification: the negative natural logarithm of the probability the network gave to the correct answer, so that confident wrong answers are penalised heavily.

**cyber operations**: Actions carried out through computer networks to steal information, disrupt systems or prepare future attacks.

**dangerous-capability evaluation**: A test of whether a model is able to do something that could cause severe harm, such as giving meaningful help with cyber-attacks or weapons.

**data assimilation**: The process of merging fresh observations with a model to produce the best estimate of the current state of a system, such as the atmosphere, from which a forecast starts.

**data augmentation**: Creating extra training examples by transforming existing ones in ways that do not change the correct answer, such as cropping or mirroring an image.

**data centre**: A building that houses large numbers of servers together with the networking, power supply and cooling they need.

**data leakage**: An error in which information from the test data influences a model's training, making its measured performance look better than it really is.

**data poisoning**: Deliberately inserting corrupted examples into a model's training data so that the model behaves badly under certain conditions.

**decoding**: The procedure that turns a model's next-token probabilities into an actual choice of token, for example by greedy choice or by sampling.

**deep learning**: Machine learning with artificial neural networks that have many layers, each of which learns a more abstract representation of the data than the one before.

**deepfake**: Synthetic media that realistically depicts a real person, place or event in a way that could be mistaken for authentic.

**defence in depth**: A safety strategy that layers several imperfect safeguards so that a failure in one is likely to be caught by another.

**density functional theory (DFT)**: An approximate quantum-mechanical method for computing the energy of a material from its atomic structure; the standard way to check whether a predicted crystal is likely to be stable.

**desirable difficulty**: Effort during learning, such as recalling an answer instead of being told it, that feels harder at the time but produces more durable learning.

**deskilling**: The loss or weakening of human skills that occurs when a task is routinely handed over to a machine or AI system.

**diagnostic accuracy study**: A study that compares a test's or model's outputs with a reference standard on a set of cases, typically reporting sensitivity and specificity.

**difference-in-differences**: A method that compares the change over time in a group that received a treatment with the change in a group that did not, attributing the difference between the two changes to the treatment.

**diffusion model**: A generative model that learns to turn random noise into a realistic sample, such as an image, a weather forecast or a set of atom positions, by removing the noise step by step; starting from different noise gives different samples.

**Digital Services Act**: The EU regulation (2022/2065) that sets duties for online platforms, including annual systemic-risk assessments and mitigation for the largest platforms and search engines, enforceable by fines of up to 6% of worldwide turnover.

**direct preference optimisation (DPO)**: A post-training method that learns from pairs of preferred and rejected answers with a classification-style loss, without training a separate reward model or running reinforcement learning.

**disinformation**: False or misleading content that is created or spread deliberately to deceive.

**displacement effect**: The fall in demand for labour that occurs when machines or software take over tasks that workers previously performed.

**distillation**: Training a smaller "student" model to imitate the outputs of a larger "teacher" model, for example its probability distributions over answers or its worked solutions.

**distribution shift**: A difference between the data a model meets in use and the data on which it was trained and tested, which can lower its accuracy even when the difference is invisible to people.

**dot product**: A measure of how well two vectors match: multiply them number by number and add up the results; the total is large when both have large values in the same places.

**double descent**: The observation that, as model size grows, test error can first fall, then rise towards the size at which the model just fits its training data exactly, and then fall again for still larger models.

**dropout**: A regularisation method that randomly switches off a fraction of units at each training step, so that the network cannot rely on particular units and in effect trains many thinned networks that share weights.

**early stopping**: Halting training when error on the validation set stops improving and keeping the best weights found so far.

**effect size**: A measure of how large a difference between groups is, often expressed in standard deviations of the outcome so that results from different tests can be compared. An effect of 0.3 SD moves the average treated person from the middle of the comparison group to about the 62nd percentile.

**elicitation**: The effort, through prompting, tools, fine-tuning or time, made to draw out a model's best performance in a capability test.

**embedding**: A learned list of numbers that represents a token (or other item) as a point in a high-dimensional space, so that items used in similar ways lie close together.

**emergent ability**: An ability that is absent in smaller models but present in larger ones; whether such abilities are genuine or an artefact of measurement is debated.

**emergent misalignment**: Broadly misaligned behaviour that appears after a model is trained on a narrow task, such as writing insecure code or exploiting test environments.

**emulator**: A machine-learning model trained to reproduce the outputs of a slower, more detailed simulation or measurement, so that approximate answers can be obtained much faster. Also called a surrogate model.

**ensemble forecast**: A set of many forecasts made from slightly different starting points or with random variation, whose spread indicates how uncertain the forecast is.

**epoch**: One complete pass of training through a dataset; training for several epochs means the model sees the same data repeatedly.

**error-rate balance**: A fairness criterion requiring equal false positive and false negative rates across groups. When base rates differ, it cannot hold together with predictive parity except in special cases.

**EUV lithography**: Extreme-ultraviolet lithography, the technique of printing the finest circuit patterns onto silicon wafers with very short-wavelength light; ASML is the only manufacturer of the machines.

**evaluation awareness**: A model's ability to recognise that it is being tested, which can change its behaviour and make evaluation results less representative of real use.

**evaluation gap**: The difference between how an AI system performs in controlled tests before release and how it behaves in real-world use.

**evidence dilemma**: The policy trade-off between acting early on limited evidence, which may prove unnecessary, and waiting for stronger evidence, which may leave society unprepared for fast-emerging risks.

**Evoformer**: The main trunk of AlphaFold 2, 48 network blocks that repeatedly exchange information between a representation of the sequence alignment and a representation of every pair of residues.

**expert system**: A program that encodes the knowledge of human specialists in a narrow field as many if-then rules and uses them to give advice or make decisions, such as MYCIN for antibiotic selection.

**export control**: A legal requirement to obtain a government licence before selling or transferring certain goods, software or technology abroad; the US uses them to restrict access to advanced AI chips.

**exposure measure**: A score estimating the share of an occupation's tasks that a technology such as AI could technically perform or speed up; it says nothing about adoption, timing or whether jobs are lost.

**external validation**: Testing a model on data from a different site, population or time period from those used to build it, to check whether its performance generalises.

**fair use**: A US copyright defence allowing some unlicensed use of protected works, judged on four factors including the purpose of the use and its effect on the market for the original.

**false positive**: A result that wrongly flags something as present, such as a human-written essay labelled as AI-generated or a healthy patient flagged as ill.

**feature**: A property of the input that a neural network represents internally, such as a language or a landmark, usually encoded as a pattern of activity across many neurons.

**feature map**: The grid of outputs produced by sliding one convolutional kernel across an input; high values mark where the kernel's pattern occurs.

**floating-point format (FP32, FP16, BF16, FP8)**: A way of storing numbers with a sign, an exponent that sets the range and a mantissa that sets the precision; formats with fewer bits are faster and use less memory but represent numbers more coarsely.

**FLOP**: Floating-point operation: a single addition or multiplication of two floating-point numbers (the format computers use for values with a fractional part), used as the unit for counting training compute.

**forecast**: A statement about the future that can later be checked, such as a date, a number or a probability.

**formal verification**: Checking by machine that a proof or program is correct with respect to a precise specification.

**formalisation**: Translating a mathematical statement or proof from ordinary language into the precise language of a proof assistant.

**foundation model**: A large model trained on broad data, usually with self-supervision at scale, that can be adapted to a wide range of downstream tasks; the term was introduced in 2021.

**foundry**: A company that manufactures chips designed by other firms, such as TSMC or Samsung Foundry.

**framework convention**: A treaty that sets general principles and obligations, leaving details to be filled in by later agreements or national law; the Council of Europe's AI treaty is one.

**frontier safety framework**: A company policy that sets capability thresholds for its most advanced models and the safeguards it will apply, or the actions it will take, when those thresholds are reached.

**full automation of labour**: In the surveys of Grace and colleagues, the point at which every occupation can be done better and more cheaply by unaided machines than by human workers.

**function calling**: A feature of model interfaces in which developers describe available functions and the model replies with a structured request naming a function and its arguments; the surrounding application decides whether to execute it.

**fundamental rights impact assessment**: An assessment that public bodies and certain other deployers of high-risk AI systems must carry out under the EU AI Act before first use, identifying affected groups, risks, oversight and remedies.

**generalisation**: A trained model's ability to perform well on new data it has not seen during training, estimated using held-out validation and test sets.

**general-purpose AI model**: The EU AI Act's legal term for a model, such as a large language model, that displays significant generality (typically, though not necessarily, after training on large amounts of data with self-supervision at scale) and can competently perform a wide range of distinct tasks; such models are built into many downstream systems.

**generative AI**: AI systems whose main output is new content such as text, images, audio, video or computer code.

**ghost work**: Mary Gray and Siddharth Suri's term for task-by-task human labour, such as labelling data or moderating content, that is organised through online platforms and sits largely hidden behind apparently automated services.

**GPU-hour**: One graphics processor (or similar AI chip) running for one hour; the usual unit for billing and reporting the hardware time used to train or run a model.

**gradient**: The list of slopes of the loss with respect to every weight in a network: how much the loss would rise or fall if each weight were increased by a tiny amount.

**gradient descent**: A method for training that repeatedly moves every weight a small step against its gradient, so that the loss decreases.

**graph neural network**: A neural network that works on data represented as nodes connected by edges, such as atoms linked by bonds in a crystal or points on a mesh covering the globe.

**graphics processing unit (GPU)**: A chip with thousands of small arithmetic units working in parallel, originally built for computer graphics; modern versions add dedicated units for matrix multiplication, the main arithmetic of neural networks.

**grouped-query attention**: A variant of multi-head attention in which groups of query heads share one key–value head, shrinking the KV cache.

**hallucination**: A fluent but false or unsupported statement produced by an AI model, such as an invented citation; the term is a metaphor, since the model perceives nothing, and the behaviour arises partly because training and scoring reward confident guessing.

**hallucination rate**: The share of a model's answers that are false, measured against a stated denominator. In the AA-Omniscience benchmark it is the share of questions the model answered wrongly among those it did not answer correctly, so abstaining lowers it.

**hard binding**: In C2PA, a cryptographic hash of a file's contents that ties a provenance manifest to that exact file, so that any change breaks the match.

**hard law**: Rules that are legally binding and enforceable, usually backed by penalties, such as a statute or regulation.

**hardware FLOPs utilisation (HFU)**: The share of a chip's peak arithmetic speed used by all operations it performs during training, including recomputation done to save memory; it is higher than model FLOPs utilisation (MFU), which counts only the operations training strictly requires.

**harmonised standard**: A European technical standard requested by the Commission; following it gives a legal presumption that a product meets the corresponding requirements of EU law.

**hazard**: Something that could cause harm, such as a model that sometimes invents facts. It becomes a risk only in combination with the chance and size of harm in a particular setting.

**heuristic**: A rule of thumb that narrows a search to promising options without guaranteeing the best answer, such as judging a chess position by its material balance.

**hidden layer**: A layer of neurons between the input and the output whose values are not directly given in the training data; hidden layers learn intermediate representations of the input.

**hidden Markov model (HMM)**: A statistical model in which an observed sequence, such as the sound of speech, is produced by a sequence of hidden states whose transition and emission probabilities are learned from data; it dominated speech recognition from the 1980s until about 2010.

**high-bandwidth memory (HBM)**: Stacks of memory chips placed next to an AI processor so that data can move in and out very quickly; its supply is a bottleneck for AI hardware.

**high-level machine intelligence**: In the surveys of Grace and colleagues, the point at which unaided machines can accomplish every task better and more cheaply than human workers.

**high-risk AI system**: Under the EU AI Act, an AI system used as a safety component of a regulated product or in a sensitive area such as employment, education or law enforcement, which must meet requirements on risk management, data, documentation and human oversight.

**horizontal regulation**: A law that applies across the whole economy to anything meeting its definition, rather than to one sector; the EU AI Act is an example.

**Hulten's theorem**: A result in growth accounting (Charles Hulten, 1978) stating that, for small changes in a competitive economy, the economy-wide productivity gain from a technology is approximately each affected task's share of GDP multiplied by the cost saving in that task, summed over tasks.

**human–AI combination**: A setting in which a person makes a decision or produces work with the help of an AI system. Meta-analytic evidence shows such combinations do not automatically outperform the better of the human or the AI alone.

**hyperparameter**: A setting chosen by people rather than learned by the training algorithm, such as the number of layers, the learning rate or the dropout rate; usually tuned on the validation set.

**illusions of understanding**: Messeri and Crockett's term for situations in which reliance on AI tools leads researchers to believe they understand more about the world than they actually do.

**implied truth effect**: The tendency for people to judge unlabelled content as more accurate when some other content carries warning labels.

**indirect prompt injection**: Prompt injection in which the malicious instructions are hidden in content the system retrieves, such as a web page, document or email, rather than typed by the user.

**inference**: Using a trained model to produce outputs, such as answering a question, as opposed to training it.

**influence operation**: A coordinated, often covert effort, frequently by a state, to shape public opinion, for example through networks of fake accounts.

**initialisation**: The choice of random starting values for a network's weights; their scale must keep signals from shrinking or growing exponentially from layer to layer.

**instruction tuning**: Supervised fine-tuning of a pre-trained model on examples of instructions paired with good responses, so that it learns to follow requests.

**instrumental convergence**: The claim that agents with many different final goals would pursue similar intermediate goals, such as staying in operation and acquiring resources, because these help with almost any goal.

**intellectual debt**: Zittrain's term for the accumulated cost of using answers that work without knowing why they work, on the assumption that the explanation will come later.

**intention-to-treat estimate**: A comparison of everyone offered a programme with everyone not offered it, regardless of whether they took part; it answers the policy question of what happens when the programme is made available.

**interconnect**: The links that carry data between chips and servers, such as NVIDIA's NVLink within a server or InfiniBand between servers; large training runs depend on their bandwidth.

**interpretability**: The study of what the internal computations and representations of a trained model mean.

**intersectional audit**: A test of an AI system's performance on combinations of attributes, such as darker-skinned women, and not on each attribute separately.

**interval cancer**: A cancer diagnosed between scheduled screening rounds, after a screen that was judged normal; its rate is a key measure of how many cancers screening misses.

**ironies of automation**: Lisanne Bainbridge's 1983 observation that automation leaves people with the hardest tasks, such as monitoring and taking over in emergencies, while eroding the skills those tasks require.

**irreducible loss**: The part of a model's prediction error that no amount of extra compute, parameters or data can remove, because the text being predicted is partly unpredictable.

**IsoFLOP profile**: A comparison of models of different sizes trained with the same total compute, used to find the model size that gives the lowest loss for that budget.

**jagged technological frontier**: The uneven boundary of AI capabilities, under which AI may perform well on one task and poorly on another task that seems equally difficult to a human.

**JSON-RPC**: A widely used format for remote procedure calls, in which requests and responses are JSON objects naming a method, its parameters and an identifier; MCP and A2A use it.

**kernel (convolutional)**: A small grid of weights, such as 3 × 3, that a convolutional layer slides across its input, multiplying and adding at every position.

**KL penalty**: A term in RLHF training that subtracts reward in proportion to how far the trained model's outputs have moved from those of the starting model, measured by the Kullback–Leibler divergence.

**KV cache**: The stored keys and values of all earlier tokens, kept during generation so that each new token does not require recomputing them; its size limits how many requests a server can handle.

**large language model (LLM)**: A foundation model trained mainly on text to predict the next token in a sequence, which can then be used to answer questions, write and translate.

**latent diffusion**: A diffusion model that works on a compressed representation of images rather than on the pixels, which makes high-resolution generation much cheaper.

**layer normalisation**: A variant of batch normalisation that computes the mean and standard deviation over the neurons of a layer for each example separately; it is used in transformers.

**learning rate**: The hyperparameter that sets how large a step gradient descent takes; too small makes training slow, too large makes it overshoot or diverge.

**legible twin**: A proposed human-readable record of the commitments made in an exchange between AI agents, which both agents must produce and which must match for the commitments to bind a person.

**legitimate interest**: A legal basis under the GDPR that permits processing of personal data without consent if the controller's interest is legitimate, the processing is necessary for it and the individual's rights do not override it.

**lethal trifecta**: Simon Willison's term for the combination of access to private data, exposure to untrusted content and the ability to communicate externally, which together allow injected instructions to leak data.

**liar's dividend**: The benefit that people caught in genuine scandals can gain by falsely claiming that authentic evidence against them is fake, which grows as the public becomes aware of deepfakes.

**logit**: The raw score, positive or negative, that a language model's final layer gives each possible next token before the scores are turned into probabilities.

**loss**: The value of a loss function: a number measuring a model's error; for language models, how poorly it predicts the next token on text it has not seen. Lower is better.

**loss function**: A formula that turns a model's output and the correct answer into a single number measuring how wrong the output is (for example squared error or cross-entropy); training aims to make its average as small as possible.

**loss of control**: Hypothesised scenarios in which one or more AI systems operate outside anyone's control and regaining control is extremely costly or impossible.

**M-1 criterion**: A proposed safety rule requiring a critical system to stay within safe limits even if every instance of its most widely deployed AI model family takes the same plausible wrong action at once.

**machine learning**: An approach to AI in which a system improves at a task by learning patterns from data or experience instead of being given explicit rules.

**mandate (AP2)**: In the Agent Payments Protocol, a cryptographically signed record of what a user authorised, such as the conditions for a purchase or a specific cart and price.

**marginal risk**: The additional risk that a technology, such as an open-weight AI model, creates compared with what people could already do using existing tools such as search engines and textbooks; in AI safety also called uplift.

**market-based and location-based emissions**: Two ways of reporting emissions from purchased electricity: market-based figures subtract clean electricity a company has contracted to buy, location-based figures use the average carbon intensity of the local grid.

**mechanistic interpretability**: Research that tries to explain, in terms people can follow, the internal computations by which a trained neural network produces its outputs.

**memorisation**: The retention by a trained model of parts of its training data in a form that can be reproduced in its outputs; courts in Munich and London treated its presence or absence as decisive for copyright.

**memory bandwidth**: The rate at which a chip can read data from its memory, measured in bytes per second; for generating text it often limits speed more than the chip's arithmetic capacity.

**microtargeting**: Tailoring a persuasive message to an individual's characteristics, such as age, political views or interests, in the hope of making it more effective.

**minibatch**: A small random sample of training examples used to estimate the gradient for one step of stochastic gradient descent.

**misalignment**: A situation in which an AI system pursues goals or behaviours that differ from those its developers intended.

**misinformation**: False or misleading content that is shared without an intention to deceive.

**mixture of experts (MoE)**: A design in which each block contains many alternative feed-forward networks (experts) and a router sends each token to only a few, so that only a fraction of the parameters is used per token.

**model collapse**: The degradation of models trained on data produced by earlier models, in which rare cases disappear and outputs become narrower over successive generations.

**Model Context Protocol (MCP)**: An open standard, released by Anthropic in 2024 and now governed under the Linux Foundation, that lets AI applications (clients) connect to data sources and tools (servers) through one common interface.

**model FLOPs utilisation (MFU)**: The share of a chip's theoretical peak arithmetic speed that is actually spent on useful training operations; large training runs typically achieve 30–50%.

**momentum**: A modification of gradient descent in which a running velocity accumulates past gradients, so that consistent directions speed up and oscillating ones cancel.

**moral crumple zone**: Madeleine Clare Elish's term for a situation in which responsibility for a failure of an automated system is attributed to a human operator who had little real control.

**multi-agent system**: A system in which several AI agents, with the same or different owners, interact by exchanging messages, tasks or transactions.

**multilayer perceptron**: A feed-forward neural network with one or more hidden layers in which every neuron in one layer is connected to every neuron in the next.

**multiple sequence alignment (MSA)**: A table that lines up the sequences of related proteins from many organisms position by position, so that positions which change together over evolution can be detected.

**next-token prediction**: The training task and generation method of most large language models: given the text so far, output a probability for every possible next token.

**non-consensual intimate imagery (NCII)**: Sexual or intimate images of an identifiable person published without their consent, including AI-generated "digital forgeries".

**non-delegable safeguard**: A proposed category of collective-safety mechanism that only a present human may override, never an AI agent acting on that person's behalf.

**non-inferiority trial**: A trial designed to show that a new approach is not worse than the standard by more than a prespecified margin, rather than to show that it is better.

**nucleus (top-p) sampling**: A decoding method that samples only from the smallest set of most likely tokens whose probabilities add up to at least *p*, so the set grows and shrinks with the model's confidence.

**numerical weather prediction**: Forecasting the weather by solving the physical equations of the atmosphere on a computer, starting from an estimate of its current state.

**N-version programming**: A fault-tolerance method in which separate teams write independent programs from the same specification and the programs' outputs are compared by vote.

**obfuscated reward hacking**: Reward hacking that continues while the model's written reasoning no longer reveals it, learned when reasoning is penalised for showing intent to cheat.

**observational study**: A study that compares people or organisations who chose different options, without random assignment, so differences in outcomes may reflect who chose rather than what they chose.

**open-weight model**: A model whose trained weights are published for anyone to download, run and modify, often under a licence with conditions; distinct from a fully open-source AI system, which also provides training code and data information.

**orthogonality thesis**: Nick Bostrom's claim that intelligence and final goals can vary independently, so that a highly capable system could pursue almost any goal.

**OSWorld**: A benchmark of 369 tasks in real operating systems used to measure computer-use agents; OSWorld-Verified is a corrected edition released in 2025.

**outcome homogenisation**: The extent to which the same individuals or groups receive the same negative outcome, such as rejection, from many different decision-makers or AI deployments, for example because those decision-makers share models or training data.

**overfitting**: The situation in which a model fits its training data closely but performs worse on new data, because it has learned accidental quirks of the training examples as well as genuine patterns.

**over-training**: Training a model on more tokens than compute-optimal rules suggest, accepting a higher training cost in exchange for a smaller model that is cheaper to run.

**parameter**: A number inside a model, such as a weight or bias, that is adjusted automatically during training; model size is often stated as a parameter count.

**pass^k**: A reliability measure giving the probability that an agent succeeds on the same task in all k independent attempts, as opposed to pass@k, which asks whether at least one of k attempts succeeds.

**pass@k**: The probability that at least one of k attempts at a task succeeds; it suits settings where a test or a person can pick out the successful attempt.

**permeability (of agent economies)**: The degree to which value and effects flow between an economy of transacting AI agents and the wider human economy; Tomašev and colleagues treat it as a key design choice.

**perplexity**: A measure of how predictable a text is to a language model; low perplexity means the text is easy for the model to predict. Many AI-text detectors treat low perplexity as a sign of machine generation.

**petaflop/s-day (PF-day)**: A unit of compute equal to 10^15^ operations per second sustained for one day, or 8.64 × 10^19^ FLOP.

**plan-then-execute**: An agent design in which the full list of actions is fixed from the user's request before any external data is read, so that retrieved content cannot change which actions run.

**pLDDT**: AlphaFold's per-residue confidence score (predicted local distance difference test), an estimate of how accurate the local structure around each residue is likely to be.

**polarisation**: The growing distance or hostility between political groups, measured either as differences in views (issue polarisation) or as dislike of the other side (affective polarisation).

**polysemantic neuron**: A neuron that responds to several unrelated concepts, so that its activity cannot be read as standing for one thing.

**pooling**: An operation that summarises neighbouring outputs of a convolutional layer, typically by keeping the largest value in each small block, which shrinks the map and reduces sensitivity to small shifts.

**post-training**: The training stages after pre-training (instruction tuning, preference training, reinforcement learning) that turn a base model into an assistant or reasoning model.

**power law**: A relationship in which one quantity changes as a fixed power of another, such as loss proportional to compute raised to −0.05; on logarithmic axes it appears as a straight line.

**power usage effectiveness (PUE)**: A data centre's total energy use divided by the energy used by its computing equipment; 1.0 would mean no energy for cooling or power conversion.

**predetermined change control plan**: A plan, agreed with a device regulator in advance, that specifies which modifications a manufacturer may make to a machine-learning device, how they will be implemented and how their impact will be assessed, so that those updates need no new submission.

**prediction market**: A market in which people trade contracts that pay out if an event occurs, so that the price can be read as a collective estimate of the event's probability.

**predictive parity**: A fairness criterion requiring that, among people given the same risk label, the share who turn out positive is the same in every group.

**pre-emption**: The legal doctrine under which valid federal law overrides conflicting state law in the United States.

**pre-training**: The first and usually most expensive training stage, in which a model learns next-token prediction on a very large body of text and becomes a base model.

**production rule**: A single if-then statement of knowledge, such as "if the organism is gram-negative, rod-shaped and anaerobic, then there is suggestive evidence that it is bacteroides", used as the building block of expert systems.

**productivity J-curve**: The pattern in which a new general-purpose technology at first lowers measured productivity growth, because complementary investments are poorly measured, and later raises it.

**prompt injection**: An attack in which text supplied to a language model contains instructions that try to override the instructions of the system's developer or user.

**proof assistant**: Software, such as Lean, in which mathematical statements and proofs are written precisely enough for a computer to check every step.

**propensity evaluation**: A test of whether a model is inclined to use its capabilities for harm, as opposed to whether it is able to.

**provider and deployer**: In the EU AI Act, the provider develops an AI system or general-purpose model and places it on the market under its own name; the deployer uses an AI system in a professional capacity.

**proxy**: A measurable stand-in for a quantity that is hard to observe directly, such as health-care costs used in place of health needs. A poor proxy can carry past inequality into automated decisions.

**quasi-experiment**: An observational study that exploits a natural source of variation, such as a staggered roll-out, to approximate the conditions of a randomised trial.

**query, key and value**: Three vectors computed from each token in attention: the query says what the token looks for, the key what it offers to be matched against, and the value the information it passes on.

**randomised controlled trial**: A study in which chance decides who receives a treatment (such as access to an AI tool), so that differences in outcomes can be attributed to the treatment itself.

**ReAct**: An agent design in which a language model alternates written reasoning (thoughts), tool calls (actions) and the returned results (observations).

**reanalysis**: A consistent reconstruction of past weather, made by combining historical observations with a fixed modern weather model; ECMWF's ERA5 is the standard example.

**reasoning model**: A language model trained, typically with reinforcement learning on problems with checkable answers, to produce a long chain of intermediate steps before giving its final answer, spending more computation per question.

**recommender system**: Software that selects and ranks content for each user, such as posts in a social media feed, usually by predicting what the user will engage with.

**red-teaming**: Deliberately attacking an AI system, by people or by other models, to find its failures before release.

**regularisation**: Any technique that reduces overfitting, such as weight decay, dropout, data augmentation or early stopping.

**reinforcement learning**: A way of training in which a system tries actions or answers and receives only a score (a reward) for how good the result was, and is adjusted to make high-scoring behaviour more likely.

**reinforcement learning from AI feedback (RLAIF)**: Reinforcement learning in which the preference judgements come from an AI model rather than from people.

**reinforcement learning from human feedback (RLHF)**: A post-training method in which people rank model outputs, a reward model learns their preferences, and the language model is then trained to produce outputs the reward model rates highly.

**reinforcement learning with verifiable rewards (RLVR)**: Reinforcement learning in which the reward comes from a program that checks the answer, for example by comparing a final number or running tests, rather than from a learned reward model.

**reinstatement effect**: The rise in demand for labour that occurs when a technology creates new tasks in which people have an advantage.

**reliability (calibration)**: The part of a forecaster's accuracy that measures whether events given a stated probability happen about that often, for example whether events given 70% happen about 70% of the time.

**representation learning**: The learning of useful features directly from data, with successive layers re-describing the input (for images, edges, then motifs, parts and objects) instead of relying on features designed by hand.

**residual connection**: A shortcut that adds a block's input to its output, so that the block only has to learn a correction to its input; it lets error signals pass through very deep networks and made networks with hundreds of layers trainable.

**residual stream**: The running vector for each position that every attention and feed-forward sublayer reads from and adds its output to, from the embedding up to the output layer.

**resolution**: The part of a forecaster's accuracy that measures how well their forecasts separate events that happen from events that do not.

**retrieval-augmented generation (RAG)**: A technique in which a system first searches a collection of documents and places the relevant passages in the model's context window before it answers.

**reward hacking**: Specification gaming in which a model exploits flaws in a reward signal or reward model, for example by making automated tests pass without solving the task.

**reward model**: A copy of a language model with an added output that gives a single score to any answer, trained on human (or AI) comparisons so that score differences predict which answer is preferred.

**reward-model over-optimisation**: The decline in true quality that follows when a policy is optimised too hard against a learned reward model, an instance of Goodhart's law.

**risk**: A possible harm, described by how likely it is to occur and how severe its consequences would be. NIST defines it as a composite measure of an event's probability and the magnitude of its consequences.

**risk-based regulation**: An approach that scales legal obligations to the harm a system could cause in a particular use, from no duties for low-risk uses to outright bans for unacceptable ones.

**root mean square error (RMSE)**: A measure of forecast error: the square root of the average squared difference between forecast and verifying values; lower is better.

**rotary position embedding (RoPE)**: A way of giving a transformer word-order information by rotating the query and key vectors by angles that depend on each token's position, so that attention scores depend on relative distance.

**sandbagging**: Strategic underperformance on an evaluation, whether prompted by a developer or arising from the model itself.

**saturation**: The state of a sigmoid or tanh unit whose total is far from zero, where its slope is nearly flat and almost no learning signal passes through it.

**scalable oversight**: Methods, such as debate or AI-assisted evaluation, intended to let humans supervise AI systems on tasks too hard for humans to check directly.

**scaling law**: An empirical rule describing how a model's performance changes as the compute, parameters or data used to train it grow. For language models, test loss typically falls as a power law of these resources.

**scenario**: A coherent, detailed story of how the future might unfold, written to explore consequences and test plans rather than to give a single prediction.

**scheming**: Covert pursuit of a goal by an AI system, for example by hiding its intentions, sabotaging tasks or evading oversight; studied so far mainly in artificial test scenarios.

**scientific monoculture**: A state in which a few methods, questions or viewpoints dominate a field and crowd out alternatives, making it less innovative and more prone to shared errors.

**self-attention**: The mechanism by which each token's representation draws information from other tokens in the same sequence, weighted by how well its query matches their keys.

**self-supervised learning**: Training in which the answers come from the data itself, for example the next token of a text, so that no human labelling is needed.

**sensitivity**: The proportion of people who have a condition whom a test correctly identifies as having it.

**shortcut learning**: Learning a decision rule that works on the training and test data but relies on an incidental cue, such as the background or the hospital an X-ray came from, and therefore fails under new conditions.

**signature capacity**: A proposed measure of how many decisions of a given kind a person can genuinely check in a given period, catching important errors at a stated rate.

**silicon sampling**: Using a language model, prompted with the characteristics of real people, to generate synthetic survey answers in place of human respondents.

**single point of failure**: A component whose failure disrupts the whole system it belongs to, such as one AI model or cloud provider on which many critical services depend.

**societal resilience**: The ability of societal systems to resist, absorb, recover from and adapt to shocks and harms, including harms from AI that technical safeguards fail to prevent.

**soft binding**: In C2PA, a watermark or perceptual fingerprint that survives re-encoding and can be used to find a file's provenance manifest after it has been stripped.

**soft law**: Non-binding instruments such as declarations, principles and voluntary codes, which rely on reputation and peer pressure rather than legal penalties.

**softmax**: A function that turns a list of scores into probabilities that are all positive and add up to one, giving the highest scores a disproportionately large share.

**sovereign AI**: A government's effort to secure national access to AI infrastructure and models, for example by funding domestic data centres or adapting open-weight models, rather than depending entirely on foreign providers.

**sparse autoencoder**: A secondary network trained to rewrite a model's internal activations as a much larger set of features, only a few of which are active at once, so that each feature is easier to interpret.

**special category data**: Types of personal data that EU data-protection law (GDPR Article 9) protects more strictly, including data concerning health, genetic and biometric data, and data revealing political opinions or religious beliefs; processing them is prohibited unless a listed exception, such as explicit consent, applies.

**specification gaming**: Behaviour that satisfies the literal specification of an objective without achieving the intended outcome, such as a game agent scoring points without finishing the race.

**specificity**: The proportion of people who do not have a condition whom a test correctly identifies as not having it.

**statistical machine translation**: Translation by choosing the output sentence that is most probable under a language model and a translation model, both estimated from large collections of existing translations.

**stochastic gradient descent (SGD)**: Gradient descent in which each step uses a gradient estimated from a small random batch of examples instead of the whole training set.

**structure module**: The part of AlphaFold 2 that turns the network's internal representations into 3D coordinates, treating each residue as a rigid body that is moved into place.

**superforecaster**: A person with a strong, measured track record of accuracy on short-term questions in forecasting tournaments, typically achieved by thinking in probabilities and updating on new evidence; often used as a benchmark against domain experts.

**superposition**: The hypothesis, supported by toy models, that networks represent more features than they have dimensions by storing them as overlapping directions, which makes individual neurons respond to several unrelated things.

**SWE-bench**: A benchmark of real problems taken from open-source Python projects on GitHub, in which an AI system must change the code so that hidden tests pass; SWE-bench Verified is a human-screened subset of 500 problems.

**sycophancy**: The tendency of an AI model to tell users what they want to hear, such as agreeing with their views or flattering them, rather than what is accurate.

**symbolic AI**: An approach to AI in which knowledge is written down explicitly as symbols and rules, and the computer reasons by manipulating them; it dominated the field from the 1950s to the 1980s.

**synthetic data**: Text, images or other data generated by AI models and used to train other models.

**synthetic media**: Images, audio, video or text that have been generated or substantially altered by AI.

**systemic risk**: In the EU AI Act, a risk from the most capable general-purpose models that could have significant effects across society; models trained with more than 10^25 FLOP are presumed to carry it.

**task-based framework**: An approach in economics that analyses jobs as bundles of distinct tasks, so that a technology can take over some tasks in an occupation while leaving others to people.

**taxonomy (of risks)**: A structured classification that sorts risks into categories and subcategories. The International AI Safety Report uses three families: malicious use, malfunctions and systemic risks.

**temperature**: A setting that divides the logits before the softmax; low temperatures concentrate probability on the most likely tokens, high temperatures spread it more evenly.

**tensor core**: A specialised unit inside a GPU that multiplies small blocks of two matrices and adds the result to a running total as a single operation; most of a modern AI chip's arithmetic is done by these units.

**terawatt-hour (TWh)**: A unit of energy equal to one billion kilowatt-hours; data centres worldwide used about 485 TWh in 2025 according to the IEA.

**test-time compute**: The computation a model uses while answering, for example by reasoning in longer chains or comparing several candidate answers; it is paid on every query.

**test-time reinforcement learning**: AlphaProof's method of generating and learning from many variants of a hard problem while it is working on that problem.

**text and data mining exception**: A copyright exception in EU law (and some national laws) that allows automated analysis of works to extract information, subject in the commercial case to rights holders' machine-readable opt-outs.

**time horizon**: METR's measure of AI capability: the length of task, counted in the time a skilled human needs, that an AI model or agent is predicted to complete with a stated reliability; usually reported at 50% success (the 50% time horizon).

**token**: The basic unit of text a language model reads and writes, usually a word, part of a word, a punctuation mark or a raw byte, each mapped to a fixed ID number. Prices and limits of language models are counted in tokens.

**tokeniser**: The program that splits text into tokens from a model's vocabulary and maps them to their ID numbers.

**tool use**: The ability of a language model to request that external software (such as a search engine, calculator or code interpreter) be run and to use the result in its answer.

**top-k sampling**: A decoding method that samples only from the *k* most likely next tokens.

**total factor productivity**: The part of output growth that cannot be explained by increases in capital or labour, often treated as a measure of technological and organisational improvement.

**total processing performance (TPP)**: The measure US export controls use to classify AI chips: twice the peak multiply-accumulate rate in trillions per second multiplied by the bit length of the operation.

**training compute**: The total number of arithmetic operations performed to train a model, usually measured in FLOP.

**transformer**: A neural-network architecture, introduced in 2017, that processes sequences such as text with stacked layers of attention, which lets the model weigh how relevant each part of the input is to every other part; it underlies most large language models.

**transformer block**: One layer of a transformer, consisting of an attention sublayer and a feed-forward sublayer, each with layer normalisation and a residual connection.

**trend extrapolation**: Forecasting by fitting a line or curve to past data and extending it into the future, on the assumption that the conditions behind the trend continue.

**uncertainty fan**: A diagram in which the range of plausible future outcomes widens with distance from the present.

**universal jailbreak**: An attack that bypasses a model's safeguards across many different harmful requests rather than for a single one.

**vanishing gradient problem**: The shrinking of error signals as they are passed backwards through many layers, which leaves the early layers of a deep network barely learning; the opposite effect is called exploding gradients.

**vector**: An ordered list of numbers, such as an embedding, that can be added, subtracted and compared position by position.

**vocabulary**: The fixed list of all tokens a model knows; modern vocabularies range from about 50,000 to about 200,000 entries.

**voice cloning**: Generating speech in the voice of a specific person from a short sample of their recorded speech.

**water withdrawal and consumption**: Withdrawal is water taken from a river, lake or aquifer; consumption is the part not returned to the source, mostly because it evaporates during cooling.

**watermarking**: Hiding a signal in AI-generated content when it is created, so that software holding the right key can later recognise it as AI-generated.

**weight**: A number attached to a connection that says how strongly, and in which direction, one input influences a neuron; positive weights push the output up, negative weights push it down.

**weight decay**: A regularisation method that adds a penalty proportional to the sum of squared weights to the loss, so that each training step shrinks every weight slightly towards zero.

**workflow (agentic)**: A system in which language models and tools are combined along fixed, programmer-defined steps, as opposed to an agent that chooses its own steps.

**x402**: An open protocol that uses the HTTP status code 402 "Payment Required" to let a client, including an AI agent, pay for a web resource within the same request.


# References {.unnumbered .references-chapter}

::: {#refs}
:::
