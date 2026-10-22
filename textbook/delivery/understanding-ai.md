# Preface {.unnumbered}

This book is an introduction to artificial intelligence as it stands in October 2026: how the technology works, where it is heading, what it is already doing to work, science, media and public life, and how societies are trying to govern it. It is written for a first university course on AI and society, open to students from any discipline. It assumes no programming and no mathematics beyond school level. Students with a technical background will find the main text quick going and can use the "Going deeper" boxes and the further reading for more.

The book has two aims. The first is understanding: by the end, a reader should be able to explain in plain words how a neural network learns, what a large language model does when it answers a question, and why more computing power has so reliably produced more capable systems. The second is judgement. Public discussion of AI swings between promise and alarm, and much of it rests on anecdotes, company announcements and forecasts presented as facts. A student who has worked through this book should be able to ask of any claim about AI: what kind of evidence supports this, how strong is it, and what would change my mind?

## How the book is organised

The fourteen chapters fall into five parts.

**Part I, How AI Works (Chapters 1–4),** builds the technical foundation. Chapter 1 defines the main terms and traces the history of the field from the 1950s. Chapter 2 explains neural networks from a single artificial neuron to deep learning, using small worked examples. Chapter 3 does the same for large language models: tokens, embeddings, attention, pre-training and the later stages of training that turn a text predictor into an assistant. Chapter 4 examines scaling, the empirical regularity that has driven most recent progress, and asks where its limits lie.

**Part II, The Frontier (Chapters 5–7),** follows the main technology trends. Chapter 5 covers the move from chatbots to agents that use tools and act over many steps. Chapter 6 looks at AI in science, mathematics and engineering, where some of the best-documented successes are found. Chapter 7 turns to the physical side of AI: chips, supply chains, data centres, electricity, and the debate over openly released models.

**Part III, Society and Economy (Chapters 8–10),** examines effects on people. Chapter 8 reviews the evidence on work, productivity and the labour market, including the hidden human labour behind AI systems and how workers have bargained over their use. Chapter 9 covers information, media and democracy, including synthetic media, persuasion and content provenance. Chapter 10 looks at education, health and everyday life.

**Part IV, Risk, Safety and Governance (Chapters 11–13),** asks what can go wrong and what is being done about it. Chapter 11 sets out a structured view of risks, from present harms to contested long-term concerns. Chapter 12 explains the technical work on making AI systems safe: alignment training, interpretability and evaluation. Chapter 13 compares how the European Union, the United States, China, the United Kingdom and international bodies regulate AI, and covers the disputes over copyright and personal data.

**Part V, The Decade Ahead (Chapter 14),** closes the book with the methods people use to forecast AI, the main scenarios for the next ten years, and a set of open problems. It also includes ten proposals, clearly labelled as the author's own, for students to criticise.

Every chapter follows the same pattern. It opens with learning objectives and a documented case that shows why the topic matters. Numbered sections carry the argument. Four kinds of box interrupt the text (most chapters use all four): **Key concept** boxes define an idea precisely; **Case study** boxes examine a real event in detail; **Debate** boxes set out a contested question with the best evidence on each side and say what would settle it; and **Going deeper** boxes give technical detail, including the few equations in the book, which readers may skip without losing the thread. Each chapter ends with a summary, a list of key terms (all defined in the glossary at the back), discussion questions and annotated further reading.

## How evidence is labelled

Claims about AI vary enormously in how well they are supported, and this book tries to make the difference visible. Every factual claim that is not common knowledge carries a citation in APA style, and the full list of references is at the end of the book. The text also signals the kind of source in the sentence itself:

- **Peer-reviewed research** and **official statistics** are cited without a label: an unlabelled citation means the source has passed peer review or is an official publication. This is the strongest evidence available, though not infallible.
- **Preprints and working papers**, posted publicly before (or without) peer review, are labelled as such where they are first mentioned in a chapter. In AI and in economics, many important results first appear this way, and some never go through formal review.
- **Reports from research institutions** (for example Epoch AI, METR, the International Energy Agency or the Stanford AI Index) are named, so that readers can judge their methods.
- **Company claims**, such as benchmark results in a product announcement, are introduced with "according to the company". They may be accurate, but they have not been checked independently, and companies have obvious reasons to present their products favourably.
- **Research by banks and consultancies** is labelled as such, for the same reason.
- **Opinions and forecasts** are attributed to the person who holds them.

Where a figure redraws published data, its caption names the source; where a diagram is schematic, the caption says so.

## What "as of October 2026" means

AI changes faster than any textbook can. The evidence in this book was gathered and checked in October 2026, and every web source was accessed then. Some things will date quickly: the names of the leading models, benchmark scores, the details of export controls, and which provisions of new laws are in force. Others will last much longer: how neural networks learn, why scaling works, how to read a randomised trial, what makes a risk hard to govern. The book tries to teach the second kind of knowledge through the first. When a chapter gives a number, it gives the year it refers to, so that readers can look for newer figures and compare. A useful exercise at any point is to take one dated claim from a chapter and find out whether it still holds.

## Using the book in a course

The book fits a single semester of about fourteen weeks, with one chapter a week. Chapters 1–3 should be taught first and in order, because later chapters use their vocabulary. After that, the parts can be reordered or shortened. A course focused on policy might spend two weeks on Chapter 13 and treat Chapters 6 and 7 lightly; a course for computing students might add a practical session after Chapters 2 and 3 in which students train a small network or inspect a language model's probabilities.

| Week | Chapter | Suggested seminar activity |
|----|---------------------|----------------------------------------|
| 1 | 1 Definitions and history | Compare three definitions of AI; which systems does each include? |
| 2 | 2 Neural networks | Work through a forward pass and one step of gradient descent by hand |
| 3 | 3 Large language models | Explore tokenisation and next-word probabilities with a public tool |
| 4 | 4 Scaling | Read a scaling-law chart; debate whether progress is slowing |
| 5 | 5 Agents | Map the failure points of a multi-step agent task |
| 6 | 6 AI for science | Assess one announced breakthrough against its peer-reviewed paper |
| 7 | 7 Chips, energy and open models | Estimate the electricity use of a data centre from public figures |
| 8 | 8 Work and the economy | Compare a randomised trial with an observational study |
| 9 | 9 Information and democracy | Trace the provenance of a viral image |
| 10 | 10 Education, health and everyday life | Draft an AI policy for a course or a hospital ward |
| 11 | 11 Risks | Rank risks by likelihood, severity and quality of evidence |
| 12 | 12 Safety techniques | Design an evaluation for a capability of concern |
| 13 | 13 Governance | Role-play a negotiation between regulators |
| 14 | 14 The decade ahead | Write and defend a ten-year forecast with stated assumptions |

: A fourteen-week course plan.

The discussion questions at the end of each chapter are designed for seminars. At least one in every chapter asks students to evaluate a piece of evidence, and at least one asks them to apply a concept to a new case.

## A note on neutrality

On many questions in this book, informed people disagree: whether current systems "understand" language, whether AI will raise or depress wages, whether frontier model weights should be released openly, how seriously to take risks that have not yet materialised. On such questions the book sets out the positions and the evidence and leaves the verdict to the reader. Where the evidence is clear, the book says so plainly, whichever side that favours. The proposals in Chapter 14 are the only place where the author argues for a position, and they are marked as such.

Jan Göbel, October 2026


```{=html}
<section class="part"><p class="part-label">Part I</p><h1 class="part-title">How AI Works</h1></section>
```

# Chapter 1: What We Mean by "AI": Definitions and a Short History

::: {.objectives}
**After working through this chapter you should be able to:**

- explain the OECD and EU AI Act definitions of an AI system and apply them to everyday examples;
- distinguish machine learning, deep learning, generative AI, foundation models, large language models and AI agents, and describe how these terms relate to one another;
- describe the main phases in the history of AI, from symbolic AI and expert systems through the AI winters to deep learning and large language models;
- evaluate claims about rapid progress and adoption by asking what was measured, on which sample and when;
- explain why the meaning of "AI" keeps shifting, and why that matters for law, research and public debate.
:::

On 30 November 2022, the company OpenAI released ChatGPT to the public as a "research preview". By 5 December it had more than one million registered users, and by July 2025 about 700 million people were using it each week, around 10% of the world's adult population [@chatterji2025how]. That study is an NBER working paper, not yet peer-reviewed; its authors include economists at Duke and Harvard universities as well as OpenAI staff, and its figures rest on OpenAI's own data. In February 2026, according to press reports of a company blog post, OpenAI announced 900 million weekly active users, a figure that has not been independently verified [@malik2026chatgpt].

For many people, ChatGPT was their first conscious encounter with "artificial intelligence". The term itself, however, is about seventy years old. It appears in a proposal dated 31 August 1955 for a summer workshop at Dartmouth College, which conjectured that "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it" [@mccarthy2006proposal]. Between that proposal and ChatGPT lie several waves of optimism, two periods of sharply reduced funding, and at least three different ideas about how intelligent machines should be built.

This chapter provides two things that the rest of the book relies on. The first is a shared vocabulary: what the official definitions say, and how terms such as machine learning, deep learning, generative AI, foundation model and agent relate to one another. The second is a short history, told through documented milestones, so that the trends discussed in later chapters can be seen against a longer arc. The chapter ends by asking why the boundary of what counts as "AI" keeps moving.

## 1.1 Defining artificial intelligence

### Turing's question

Alan Turing's paper "Computing machinery and intelligence" opens with the sentence "I propose to consider the question, 'Can machines think?'". Turing judged the words "machine" and "think" too vague to define usefully, so he replaced the question with a test he called the imitation game. In this game a human interrogator exchanges typed messages with a hidden person and a hidden machine, and tries to tell which is which. Turing predicted that in about fifty years computers with a storage capacity of about 10^9^ would play the game well enough that an average interrogator would have no more than a 70 per cent chance of making the right identification after five minutes of questioning [@turing1950computing].

Turing's move matters for this book because it set a pattern that has lasted. He defined intelligence by what a system does, judged from the outside, instead of by what goes on inside it. Most modern definitions of AI, including the legal ones discussed below, follow the same behavioural approach. The weakness of the approach is also visible from the start: a behavioural test says nothing about whether the machine reaches its answers in a way that resembles human thought. Section 1.6 returns to this question in the debate about whether large language models "understand" language.

The Dartmouth proposal of 1955, written by John McCarthy, Marvin Minsky, Nathaniel Rochester and Claude Shannon, gave the field its name. It proposed "a 2 month, 10 man study of artificial intelligence" in the summer of 1956 at Dartmouth College in Hanover, New Hampshire [@mccarthy2006proposal]. The workshop is usually treated as the founding event of AI as a research field. One widely quoted later definition, by the AI pioneer Nils Nilsson, describes AI as "that activity devoted to making machines intelligent", and intelligence as the quality that enables an entity "to function appropriately and with foresight in its environment" [@stone2016artificial].

### The OECD definition

Definitions written by researchers can afford to be loose. Definitions written for governments cannot, because they decide which systems a law or policy covers. The most influential international definition comes from the Organisation for Economic Co-operation and Development (OECD), an intergovernmental organisation of mostly high-income countries. Its member countries approved a revised version in November 2023, and an explanatory memorandum published in March 2024 sets out the final text [@oecd2024explanatory]:

> An AI system is a machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments. Different AI systems vary in their levels of autonomy and adaptiveness after deployment. [@oecd2024explanatory, p. 4]

"Objectives" can be explicit, such as a target set by a programmer, or implicit, such as a goal that emerges from training. "Infers" is the central idea: the system works out how to produce its output from the input, instead of following a fixed list of instructions. The memorandum explains that inference here covers both the moment a system produces an answer and the earlier "build phase", in which a model is derived from data [@oecd2024explanatory, p. 9]. "Autonomy" refers to how far the system acts without human involvement. "Adaptiveness" refers to whether it keeps changing its behaviour after it has been deployed, as a speech recogniser that adapts to one person's voice does.

The 2023 revision added "content" to the list of outputs. The OECD's earlier 2019 definition had spoken only of predictions, recommendations and decisions for "human-defined objectives". The memorandum says "content" was added because generative AI systems that produce text, images, audio and video "have gained significant momentum" [@oecd2024explanatory, p. 9]. The change is a small, documented example of a definition being rewritten to keep up with the technology.

### The EU AI Act definition

The European Union's Artificial Intelligence Act, Regulation (EU) 2024/1689, is a comprehensive EU-wide law on AI (Chapter 13 discusses it in detail). Its Article 3(1) defines an AI system in almost the same words as the OECD. It is a machine-based system, operating with varying levels of autonomy, that "infers, from the input it receives, how to generate outputs" such as predictions, content, recommendations or decisions [@europeanparliament2024regulation, art. 3(1)]. The match is deliberate, since the Act wants its definition to be "closely aligned with the work of international organisations working on AI" [@europeanparliament2024regulation, recital 12].

The Act's explanatory recitals also say what the definition leaves out: "simpler traditional software systems" that only carry out rules written by people [@europeanparliament2024regulation, recital 12]. A spreadsheet formula that calculates tax from fixed rates is therefore not an AI system under the Act. Older rule-based AI of the kind described in Section 1.3 can still count, as long as the system draws inferences from encoded knowledge instead of merely executing a programmer's instructions. Deciding on which side of that line a particular product falls requires legal judgement.

::: {.box .concept}
**Key concept: AI system (OECD and EU definition)**

In both the OECD definition and the EU AI Act, an AI system is a machine-based system that, for explicit or implicit objectives, infers from its input how to generate outputs such as predictions, content, recommendations or decisions that can affect physical or virtual environments. The key word is "infers": the system derives how to respond, from data or from encoded knowledge, instead of only executing rules a person wrote down. A spam filter trained on examples of junk mail fits the definition. A fixed formula in a spreadsheet does not.
:::

## 1.2 A family of terms

Public discussion often uses "AI" as if it named a single technology. In practice it is an umbrella term for a family of methods, and the terms in that family overlap. Figure 1.1 shows the most common way of arranging them as nested circles, which this section explains term by term.

![Figure 1.1: The usual nesting of AI terms. Machine learning is one approach within AI; deep learning is one kind of machine learning; large language models and other generative foundation models are, today, mostly built with deep learning. Agents are drawn across the boundaries because the term describes how a model is used. Schematic, not to scale. Diagram by the author.](../figures/svg/fig-01-01.svg){#fig:01-01}

**Machine learning** is the approach in which a system improves at a task by learning from data or experience, instead of being given explicit rules. Arthur Samuel's 1959 study of the game of checkers (draughts) is a classic early example. Samuel showed that "a computer can be programmed so that it will learn to play a better game of checkers than can be played by the person who wrote the program", and that it could do so in 8 to 10 hours of playing time [@samuel1959studies]. An everyday analogy is learning to recognise ripe fruit by handling many examples instead of memorising a rulebook, although a machine-learning system needs far more examples than a person and has no common sense to fall back on when an example is unusual.

**Deep learning** is machine learning with artificial neural networks that have many layers. A neural network is a computing structure loosely inspired by the brain, made of simple connected units whose connection strengths are adjusted during training (Chapter 2 explains how). In the words of a widely cited 2015 review, deep learning "allows computational models that are composed of multiple processing layers to learn representations of data with multiple levels of abstraction" [@lecun2015deep]. In an image-recognition network, for example, earlier layers pick out simple visual features and later layers combine them into more abstract ones, which is what "levels of abstraction" means here (Chapter 2 gives examples). Writing in 2021, in an essay posted as an arXiv preprint, the computer scientist Melanie Mitchell observed that deep neural networks powered all the major AI advances of the previous decade [@mitchell2021why].

**Generative AI** refers to systems whose main output is new content: text, images, audio, video or computer code. As noted above, the OECD added "content" to its definition precisely because such systems had become so prominent [@oecd2024explanatory]. ChatGPT, image generators and music generators are generative AI. A system that only sorts emails into "spam" and "not spam" is not, because it produces a label instead of new content.

A **foundation model** is a large model trained on broad data, usually with self-supervision at scale, that can be adapted to a wide range of downstream tasks. The term was introduced in 2021 in a report by more than 100 researchers, posted as a preprint, who chose the word to stress the models' "critically central yet incomplete character" [@bommasani2021opportunities]. Their examples included BERT, DALL-E and GPT-3. Self-supervision means that the training signal comes from the data itself, for instance by hiding a word in a sentence and asking the model to predict it, so no human has to label each example. The EU AI Act uses a closely related legal term, the **general-purpose AI model**. It defines this as "an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks" [@europeanparliament2024regulation, art. 3(63)].

A **large language model (LLM)** is a foundation model trained mainly on text to predict the next word, or more precisely the next "token", in a sequence. GPT-3, described in Section 1.6, is a well-documented example [@brown2020language].

An **AI agent** is a system that pursues a goal over several steps by taking actions in an environment, such as searching the web, running code or filling in forms, and observing the results. The idea of an agent is old in AI research: a 1995 survey already described it as having "become important in both artificial intelligence and mainstream computer science" [@wooldridge1995intelligent]. What is new since 2024 is that agents are commonly built by placing an LLM inside a loop with tools and memory (Chapter 5 covers this in depth).

Figure 1.1 simplifies in three ways. First, not every generative model is a deep neural network, and not every foundation model is generative: BERT, one of the original examples, was mainly used for understanding and classifying text [@bommasani2021opportunities]. Second, "agent" describes how a model is used, not a technique, so it cuts across the circles. Third, the outer circle contains far more than machine learning, including the symbolic methods described next.

## 1.3 Symbolic AI, expert systems and the AI winters (1956 to the early 1990s)

### Early optimism

For its first three decades, most AI research followed what is now called **symbolic AI**. In this approach, knowledge is written down explicitly as symbols and rules (for example, "if the patient has a fever and a stiff neck, consider meningitis"), and the computer reasons by manipulating them. The approach suited the logic-based programming of the time and matched a view of thinking as rule-following. An analogy is a very large and carefully cross-referenced instruction manual. The weakness of the analogy is also the weakness of the approach: human experts often act on knowledge they cannot put into words, a problem that proved central to symbolic AI's difficulties.

Predictions in this period were bold. In 1960, Herbert Simon declared that "Machines will be capable, within twenty years, of doing any work that a man can do", and in 1967 Marvin Minsky forecast that "Within a generation...the problems of creating 'artificial intelligence' will be substantially solved". Enthusiasm also surrounded early neural networks. In 1958 the New York Times reported that the US Navy expected Frank Rosenblatt's "perceptron" to be able to "walk, talk, see, write, reproduce itself, and be conscious of its existence". In 1969, Minsky and Seymour Papert's book *Perceptrons* showed that the simple, single-layer networks of the time could solve only a limited class of problems [@mitchell2021why].

### The first AI winter

The term **AI winter** describes a period of reduced funding, falling confidence and declining interest in AI research. The first such period followed critical government reviews in the early 1970s. In the United Kingdom the Science Research Council asked the mathematician Sir James Lighthill to assess the field. His report, dated July 1972 and published in 1973, concluded that "in no part of the field have the discoveries made so far produced the major impact that was then promised". Among the causes he named was a "failure to recognise the implications of the combinatorial explosion" [@lighthill1973artificial]. The combinatorial explosion is the way the number of possibilities to check grows extremely fast as a problem gets bigger, as when each extra move in a board game multiplies the number of possible continuations.

According to Mitchell, the Lighthill report and a similarly negative review for the US Department of Defense "led to sharp funding decreases and a downturn in enthusiasm for AI in both countries" [@mitchell2021why]. The research did not stop, but it continued at a smaller scale and with more modest claims. Historians disagree about how severe this first winter was. The historian of computing Thomas Haigh argues, in a 2024 magazine column, that the AI research community in fact grew steadily through the 1970s. On his account the real winter was the long slump that followed the 1980s boom [@haigh2024how].

### Expert systems and the second winter

Interest revived in the early 1980s, driven largely by **expert systems**. An expert system is a program that encodes the knowledge of human specialists in a narrow field as hundreds or thousands of if-then rules, and uses them to give advice or make decisions. Such systems fit the symbolic approach well: specialists were interviewed, their knowledge was written down as rules, and an inference engine chained the rules together. A medical and an industrial example show what they could do.

::: {.box .case}
**Case study: MYCIN's blinded evaluation (1979)**

MYCIN was an expert system developed at Stanford University in the 1970s to recommend antibiotic treatment for serious infections. In a study published in 1979, its recommendations for ten real cases of meningitis were compared with those of nine human prescribers, including five infectious-disease faculty specialists. Eight outside experts rated each prescription without knowing which came from the computer. MYCIN's prescriptions were rated acceptable 65% of the time; the five faculty specialists scored between 42.5% and 62.5% [@yu1979antimicrobial]. The study shows that a carefully built rule-based system could match specialists on a narrow, well-defined task. It was also small (ten cases), confined to a single type of infection, and judged by agreement among experts instead of by patient outcomes, which are common limits of early AI evaluations.
:::

Mitchell describes "the rise of 'expert systems' in industry" in the early 1980s. From 1980, the computer manufacturer Digital Equipment Corporation used a rule-based system called R1, later XCON, to configure its VAX-11 computer systems for customers, and over the following years its knowledge base grew substantially [@bachant1984r1]. Japan launched its "Fifth Generation" computing project, and the United States responded with its Strategic Computing Initiative, both of which placed large bets on AI [@mitchell2021why].

Some researchers were already worried. At the 1984 conference of the American Association for Artificial Intelligence, a panel discussed "deep unease among AI researchers" that expectations were too high and that this "will eventually result in disaster" [@mcdermott1985dark]. One panellist, Drew McDermott, described the danger of a funding collapse in which "everybody hurriedly changes the names of their research projects to something else", a condition he called the "AI Winter". About five years later, in the late 1980s, a second winter set in [@mitchell2021why].

Mitchell attributes the downturn largely to **brittleness**. Expert systems were "often unable to generalize or adapt when faced with new situations", because the experts writing the rules relied on unspoken common-sense knowledge that never made it into the program [@mitchell2021why]. The XCON team's own account, published after four years of use, describes the continuing work needed to extend the system and keep improving its performance [@bachant1984r1].

Haigh adds institutional and economic causes [@haigh2024how]. The US Defense Advanced Research Projects Agency (DARPA) had sold its Strategic Computing Initiative to Congress with promises of military applications. Apart from speech recognition, most of its projects disappointed, and budget cuts in the Reagan era reduced the effort further. At the end of 1987 DARPA abandoned the programme's flagship, an autonomous land vehicle, and turned its computing research towards high-performance numerical computing. In industry, companies that had bought expert-system software found that automating expertise required them to hire new experts to maintain the rules. By 1989 DEC had 59 technical staff assigned to its internal expert systems, and a shortage of AI specialists had pushed up wages. Few companies could sustain such costs, and the market for expert-system software collapsed. The lesson many researchers drew was that knowledge written down by hand does not scale well. Whether that lesson was fully correct is still debated, as Section 1.7 shows.

## 1.4 The statistical turn: learning from data (1990s to 2000s)

From the 1990s, much of the field moved from writing knowledge down to learning it from data. Mitchell describes "the meteoric rise of machine learning" in the 1990s and 2000s, with methods "typically inspired by statistics rather than by neuroscience or psychology" and aimed at specific tasks instead of general intelligence. She also notes that machine-learning researchers often kept their distance from the label "AI", which had become discredited [@mitchell2021why]. This is one reason why everyday technologies of the period, such as spam filters and recommendation systems, were rarely described as AI at the time.

Several techniques from this period remain in use. Support vector machines, introduced in their modern form by Corinna Cortes and Vladimir Vapnik in 1995, find the boundary that best separates two categories of examples [@cortes1995support]. Neural networks had not disappeared either. A 1986 paper in *Nature* by David Rumelhart, Geoffrey Hinton and Ronald Williams popularised **backpropagation**, the method still used to train neural networks today [@rumelhart1986learning]. Chapter 2 explains it in plain language. For two decades, however, neural networks were one method among many and often not the best performing.

The most widely publicised AI event of the 1990s involved a specialised chess machine. In May 1997, IBM's chess computer Deep Blue beat the world champion Garry Kasparov 3.5 to 2.5 in a six-game match in New York. IBM describes this as the first time a computer defeated a reigning world champion in a match under standard tournament time controls. The match was played under intense media attention. Deep Blue had been built with a single goal, to beat the world's best human chess player, and it could do nothing else [@ibm2025deep].

A quieter development turned out to matter more. In 2009, Jia Deng, Fei-Fei Li and colleagues introduced ImageNet, a large database of labelled photographs organised by object categories [@deng2009imagenet]. From 2010, an annual competition, the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), asked teams to classify images into 1,000 categories, using roughly 1.2 million training images [@russakovsky2015imagenet]. Large, shared datasets with agreed scoring rules gave researchers a common yardstick, and they gave data-hungry methods something to learn from.

## 1.5 The deep learning breakthrough (2012 to 2017)

### ImageNet 2012

In the 2012 ImageNet challenge, a team from the University of Toronto, Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton, entered a deep convolutional neural network now usually called AlexNet. It achieved a top-5 error rate of 15.3%, compared with 26.2% for the second-best entry [@krizhevsky2012imagenet]. The 15.3% entry used additional pre-training data; using only the official training data, the team's error was 16.4%, the value shown in Figure 1.2 [@russakovsky2015imagenet]. The network had 60 million adjustable parameters and was trained for five to six days on two NVIDIA GTX 580 graphics cards [@krizhevsky2012imagenet]. Graphics processing units (GPUs) were developed for computer graphics, but they can carry out many simple calculations at the same time, which is what training a neural network requires.

::: {.box .deeper}
**Going deeper: What "top-5 error" measures**

In the ImageNet classification task, each test image has one correct label from 1,000 categories, such as a particular breed of dog. A system may submit five guesses per image. The top-5 error is the percentage of test images for which none of the five guesses matches the correct label. Five guesses are allowed because many photographs contain several objects and only one is labelled. The figure 15.3% therefore means that AlexNet's five guesses all missed for about 15 of every 100 test images. The organisers note that top-5 error, top-1 error and a hierarchical measure ranked the entries in the same order, which is why they adopted the simplest one [@russakovsky2015imagenet].
:::

Figure 1.2 places the 2012 result in context. The winning error rate (counting only entries that used the official training data) fell from 28.2% in 2010 to 6.7% in 2014, and the drop after 2012 coincided with the switch to deep convolutional networks [@russakovsky2015imagenet]. In 2015 a "residual network" with up to 152 layers reached 3.57% [@he2016deep].

![Figure 1.2: Winning top-5 classification error in the ImageNet challenge, 2010–2015 (lower is better). The largest single drop came in 2012, when a deep neural network won for the first time. The dashed line marks one trained human annotator's estimated error of 5.1% on a sample of 1,500 test images; it is a single-person estimate, not a general human benchmark. Source: @russakovsky2015imagenet; @krizhevsky2012imagenet; @he2016deep.](../figures/svg/fig-01-02.svg){#fig:01-02}

The human comparison in Figure 1.2 deserves care. The organisers estimated that one expert annotator, who had trained on 500 images, made top-5 errors on 5.1% of 1,500 test images. A second annotator labelled only 258 images [@russakovsky2015imagenet]. In 2015, a team led by Kaiming He reported a 4.94% error and described its result as "the first to surpass human-level performance (5.1%...)" on the challenge [@he2015delving]. That claim, and the headlines it inspired, rested on this narrow comparison: one benchmark and one main annotator. It is an early example of a recurring pattern, discussed in Chapter 4: benchmark results are real, but they measure less than the headlines suggest.

### AlphaGo

The board game Go had long been regarded as the hardest of the classic games for computers, because the number of possible positions is enormous and it is hard to judge who is winning in a given position. In January 2016, David Silver and colleagues at Google DeepMind described AlphaGo, which combined deep neural networks with a search method. One network suggested promising moves and another estimated the chance of winning from a position. They were trained first on games played by human experts and then by "reinforcement learning from games of self-play", in which the program improved by playing against versions of itself [@silver2016mastering].

AlphaGo won 99.8% of its games against other Go programs and beat the European champion, Fan Hui, by five games to nothing. The authors described this as the first time a computer program had defeated a human professional player on a full-sized board, "a feat previously thought to be at least a decade away" [@silver2016mastering]. In March 2016 AlphaGo then beat Lee Sedol, a world champion player from South Korea, by four games to one in Seoul [@sumner2016alphago]. Because AlphaGo learned much of its skill from expert games and self-play, its victory was widely read as a demonstration of machine learning.

### The transformer

In June 2017, eight researchers, most of them at Google, published "Attention is all you need". They proposed the **transformer**, a neural-network design for processing sequences such as sentences, "based solely on attention mechanisms, dispensing with recurrence and convolutions entirely". Attention, roughly speaking, lets the model weigh how relevant every other word in a passage is when interpreting each word. On a standard English-to-German translation test, the transformer scored 28.4 on the BLEU measure, more than two points above the best previous results, and it trained in a fraction of the time [@vaswani2017attention].

The paper's practical importance came from that last point. Because a transformer processes all the words in a passage at once, instead of one after another, it makes good use of parallel hardware such as GPUs. That made it practical to train much larger models on much more text. Almost every large language model discussed in this book is built on the transformer.

## 1.6 From language models to agents (2018 to 2026)

### GPT-3 and foundation models

In May 2020, a team at OpenAI, with Tom Brown as first author, described GPT-3, a transformer language model with 175 billion parameters, "10x more than any previous non-sparse language model". A parameter is one of the adjustable numbers inside a network that training sets. The paper's main finding was that a model this large could carry out many tasks it had not been specifically trained for, such as translation, answering questions or simple arithmetic, when given a few examples in the prompt. The authors called this few-shot learning. They also reported tasks on which GPT-3 still struggled [@brown2020language].

GPT-3 and similar models prompted the research group mentioned in Section 1.2 to coin the term "foundation model" in 2021. Their report argued that the defects of a foundation model are "inherited by all the adapted models downstream", because many applications are built on the same few base models [@bommasani2021opportunities].

### ChatGPT and the speed of adoption

ChatGPT put a large language model behind a simple chat window and made it free to use. Its user numbers, given at the start of this chapter, come from the company. Independent surveys point the same way, although they measure something different. The economists Alexander Bick, Adam Blandin and David Deming ran a nationally representative series of US surveys. In a working paper (not yet peer-reviewed), they found that, as of late 2024, "nearly 40 percent of the U.S. population age 18-64 uses generative AI". Measured from each technology's first mass-market product, they found that overall adoption "has been faster than either PCs or the internet" [@bick2024rapid].

The 2026 edition of the Stanford AI Index, an annual report that compiles data on AI, builds on the same line of research. Drawing on the same US survey series of adults aged 18 to 64, it reports that generative AI reached about 53% adoption within three years of its first mass-market product, well above the early paths of the personal computer and the internet. The same report also uses a quite different measure, Microsoft's data on the share of each country's population using AI tools. On that measure adoption varies widely between countries and "correlates strongly with GDP per capita", and the United States ranks only 24th, at 28.3%, in the second half of 2025 [@sajadieh2026ai, ch. 4]. The two US figures differ because they count different things in different ways, not because one of them is wrong. Adoption figures depend heavily on what counts as "use": a single trial in the past month and daily use at work are very different things. Chapter 8 examines adoption and its economic effects.

### Reasoning models

A second shift came in 2024 and 2025 with so-called **reasoning models**. These are language models trained to produce a long internal chain of intermediate steps before giving a final answer, which has improved their performance on verifiable tasks such as mathematics, coding competitions and science questions [@guo2025deepseek]. OpenAI's o1 models, according to the company, are "trained with large-scale reinforcement learning to reason using chain of thought", and "o1 thinks before it answers" [@openai2024o1]. In January 2025 the Chinese company DeepSeek published DeepSeek-R1. A peer-reviewed version in *Nature* reports that reasoning abilities "can be incentivized through pure reinforcement learning", without human-written examples of step-by-step reasoning [@guo2025deepseek].

Reasoning models change where computing effort is spent. Earlier gains came mainly from training ever-larger models. Reasoning models also spend more computation each time they answer a question, which Chapter 3 and Chapter 4 discuss as "test-time compute". The word "reasoning" is the developers' term. Whether these step-by-step outputs reflect reasoning in the human sense is an open question, closely related to the debate below.

### Agents

The most recent shift, during 2025 and 2026, is towards agents built around language models. In November 2024 the company Anthropic released the Model Context Protocol, which it describes as "an open standard for connecting AI assistants to the systems where data lives, from content repositories to business tools" [@anthropic2024introducing]. Standards like this make it easier to give a model access to tools, files and other software.

Measurements suggest rapid, but uneven, progress. Researchers at METR, an organisation that evaluates AI systems, proposed measuring an AI system by the length of tasks it can complete. Their measure is the time a skilled human typically needs for tasks that the AI completes with 50% success. In a study first posted as a preprint in March 2025 and later presented at the NeurIPS 2025 conference, they reported that this "time horizon" had been "doubling approximately every seven months since 2019" on their set of mainly software tasks [@kwa2025measuring]. OSWorld, a benchmark of real computer tasks across operating systems, was published in 2024, when the best model completed about 12% of its tasks [@xie2024osworld]. The 2026 AI Index reports that by 2025 the best agent's success rate had reached 66.3%, within about 6 percentage points of human performance. It adds that agents "still fail roughly one in three attempts on structured benchmarks" [@sajadieh2026ai]. Benchmarks are controlled settings, so they may overstate how well agents perform in everyday use.

Figure 1.3 places these developments on a single timeline from 1950 to 2026.

![Figure 1.3: Selected milestones in the history of AI, 1950–2026. Shaded bands mark the two AI winters, whose start and end dates are approximate. Research milestones are to the left of the axis, deployment and policy events to the right; the axis is compressed before 2005. Sources: @turing1950computing; @mccarthy2006proposal; @samuel1959studies; @lighthill1973artificial; @yu1979antimicrobial; @mcdermott1985dark; @mitchell2021why; @rumelhart1986learning; @ibm2025deep; @deng2009imagenet; @krizhevsky2012imagenet; @silver2016mastering; @vaswani2017attention; @brown2020language; @bommasani2021opportunities; @chatterji2025how; @oecd2024explanatory; @europeanparliament2024regulation; @openai2024o1; @anthropic2024introducing; @guo2025deepseek; @malik2026chatgpt.](../figures/svg/fig-01-03.svg){#fig:01-03}

::: {.box .debate}
**Debate: Do large language models understand language?**

A review by Melanie Mitchell and David Krakauer describes a "heated debate" in the research community on whether large language models understand language "in any humanlike sense" [@mitchell2023debate]. On one side, Emily Bender and Alexander Koller argue that "a system trained only on form has a priori no way to learn meaning" [@bender2020climbing]. Form here means the sequence of words; meaning means what the words refer to in the world. On their view, fluent output shows skill with patterns in text, not understanding.

On the other side, some researchers point to evidence that language-model-style networks build internal models of what they process. In one experiment, a GPT-style network trained only to predict legal moves in the board game Othello developed an internal representation of the board state, which the researchers could edit to change the network's predictions [@li2023emergent]. Supporters of this view argue that such internal models are at least a partial form of understanding.

The research community is split. In a 2022 survey of 480 natural-language-processing researchers, reported by Mitchell and Krakauer, 51% agreed and 49% disagreed that a model trained only on text could, in principle, understand language "in some nontrivial sense". Settling the question would require an agreed, testable definition of understanding, together with tests that a system cannot pass by surface pattern-matching alone. Mitchell and Krakauer suggest that there may be several distinct modes of understanding instead of one [@mitchell2023debate].
:::

## 1.7 Why "AI" is a moving target

### The AI effect

Chess offers an illustration. IBM presented Deep Blue's 1997 victory as heralding a future in which "supercomputers and artificial intelligence could simulate human thinking" [@ibm2025deep]. Chess software is now an ordinary consumer product. The One Hundred Year Study on Artificial Intelligence is a long-term project based at Stanford University. Its 2016 report describes a "repeating pattern known as the 'AI effect' or the 'odd paradox'": AI "brings a new technology into the common fold, people become accustomed to this technology, it stops being considered AI, and newer technology emerges". The report concludes that AI is best seen as "a continual endeavor to push forward the frontier of machine intelligence" [@stone2016artificial].

The AI effect has practical consequences. Statistics on "AI investment" or "AI adoption" depend on what is counted, and the boundary shifts over time. It also affects how history is told. As Section 1.4 showed, many machine-learning applications of the 1990s and 2000s were built by researchers who avoided the label "AI" [@mitchell2021why], so they are often missing from popular histories of the field. The reverse also happens: when the label is fashionable, products that use only simple statistics may be marketed as AI.

Some historians and scholars of science and technology studies go further and treat "AI" as a commercial and political category as well as a technical one. Haigh notes that in the 1980s "expert systems" was often promoted as a less controversial brand than "artificial intelligence". Only in the last few years, he adds, has the AI label come to refer mainly to deep learning and generative systems [@haigh2024how]. The label can also be claimed falsely. In March 2024 the US Securities and Exchange Commission fined two investment advisers a total of $400,000. According to the regulator, they had told clients that they used AI in ways that they did not. Its chair called the practice "AI washing" [@sec2024sec].

The journalist and software developer Meredith Broussard warns against "technochauvinism", the belief that technology is always the solution [@broussard2018artificial]. Kate Crawford argues that AI is best understood as a material and political system, built from extracted minerals, low-paid labour and personal data, that tends to concentrate power [@crawford2021atlas]. The anthropologist Lucy Suchman adds that treating AI as a single "thing", even a controversial one, helps to attract further investment. She asks for closer attention to the specific techniques that "travel under the sign of AI", where they are used and with what effects [@suchman2023uncontroversial]. These critics do not deny that the techniques work. They ask who gains from grouping very different techniques under one name, a question that sits beside the legal one in Section 1.1 of which systems the name should cover.

### Springs, winters and the language of progress

The history in this chapter shows a cycle that Mitchell calls AI "springs" and "winters": periods of "optimistic predictions and massive investment" followed by "disappointment, loss of confidence, and reduced funding". Simon's twenty-year prediction of 1960 did not come true, and neither did the commercial hopes of the 1980s. Mitchell argues that over-optimism stems partly from systematic errors in how people reason about intelligence. One of these she calls "easy things are easy and hard things are hard": things humans do without much thought, such as looking around and making sense of a scene, have proved among the hardest for machines [@mitchell2021why]. Whether the current period will end in another winter is a question for Chapter 14. The record of past predictions is a reason to treat confident forecasts in either direction with care.

### Two traditions, one argument

A deeper reason why the meaning of AI keeps shifting is that the field has never agreed on how intelligence should be built. The symbolic tradition writes knowledge down; the learning tradition extracts it from data. The reinforcement-learning researcher Richard Sutton argues in an influential essay that "general methods that leverage computation are ultimately the most effective, and by a large margin". In his account, researchers have repeatedly built human knowledge into their systems, only to be overtaken by simpler methods that used more computing power [@sutton2019bitter]. The cognitive scientist Gary Marcus takes the opposing view. In a preprint essay he sets out ten concerns about deep learning and argues that it "must be supplemented by other techniques if we are to reach artificial general intelligence" [@marcus2018deep].

The evidence in this chapter can be read in favour of both positions. The rise of deep learning after 2012 and the success of scaled-up language models fit Sutton's argument. The uneven performance of current systems fits parts of Marcus's argument. The 2026 AI Index notes that a model won a gold medal at the 2025 International Mathematical Olympiad. Yet in March 2026 the best model read analogue clocks correctly only about half the time, against about 90% for humans [@sajadieh2026ai]. Agents that combine a learned model with search engines, code interpreters and other conventional software (Chapter 5) are one practical way of supplementing deep learning with other techniques.

The legal definitions in Section 1.1 were written with this moving target in mind. By defining AI through inference and outputs, instead of through any particular technique, the OECD and the EU tried to cover both traditions and whatever comes next [@oecd2024explanatory; @europeanparliament2024regulation]. The OECD memorandum states that "additional techniques and applications will likely emerge in the future" and asks users of its definition to "exercise judgement on its relevant scope" [@oecd2024explanatory, p. 6]. Chapter 13 examines how the EU AI Act's version of the definition is being applied in practice.

## Summary

- "Artificial intelligence" was named in a 1955 proposal for a 1956 Dartmouth workshop; Turing's 1950 paper had already framed machine intelligence in terms of observable behaviour.
- The OECD (revised 2023, memorandum 2024) and the EU AI Act (2024) define an AI system as a machine-based system that infers from its input how to generate outputs such as predictions, content, recommendations or decisions; "content" was added to cover generative AI.
- Machine learning, deep learning, generative AI, foundation models, large language models and agents form an overlapping family of terms; the usual nested diagram is helpful but imperfect.
- Symbolic AI and expert systems achieved real successes in narrow domains, such as MYCIN's 1979 evaluation, but proved brittle and costly to maintain; AI winters followed periods of over-optimism in the 1970s and, more severely, from the late 1980s.
- From the 1990s, statistical machine learning became dominant; large shared datasets such as ImageNet then set the stage for deep learning.
- AlexNet (2012), AlphaGo (2016) and the transformer (2017) mark the deep-learning breakthrough; GPT-3 (2020) and ChatGPT (2022) brought large language models to a mass audience, with adoption faster than the PC or the internet in US survey data.
- Reasoning models (2024–25) and LLM-based agents (2025–26) are the most recent shifts; benchmark progress is fast but agents still fail often.
- The "AI effect" means that the label moves as technologies become familiar, and critics argue that "AI" also works as a marketing and political category; claims about "AI" therefore need to specify which systems they include.

## Key terms

artificial intelligence · AI system · symbolic AI · expert system · AI winter · machine learning · deep learning · transformer · generative AI · foundation model · general-purpose AI model · large language model · reasoning model · AI agent · AI effect

## Discussion questions

1. Apply the OECD/EU definition of an AI system to three examples: a thermostat that switches the heating on below 19 °C, a bank's credit-scoring model trained on past loans, and a chatbot. Which of them are AI systems under the definition, and which words in the definition decide each case?
2. The ImageNet "human error" of 5.1% was estimated from one expert annotator labelling 1,500 images. Evaluate how strongly this evidence supports the claim that machines "surpassed humans at image recognition" in 2015. What additional evidence would you want?
3. MYCIN's prescriptions were rated acceptable at least as often as specialists' in a small blinded study in 1979. List the kinds of evidence, beyond expert ratings of ten cases, that a hospital would need before using such a system with patients. Which of them did the 1979 study provide, and which are still missing for a current AI tool in medicine or another field of your choice?
4. Bick, Blandin and Deming find that generative AI was adopted faster than PCs or the internet. List at least two ways in which "adoption" could be defined, and explain how the choice could change the conclusion.
5. Find a product or service that its seller advertises as "AI-powered". Using the OECD/EU definition (Section 1.1) and the critiques of the label in Section 1.7, decide whether the label is justified. What information from the seller would you need to check the claim, and was it available?
6. Sutton and Marcus disagree about whether general learning methods will be enough. Which developments described in Sections 1.5 and 1.6 support each position, and what kind of future evidence would change your mind?

## Further reading

- Turing, A. M. (1950). *Computing machinery and intelligence*. Short, readable and still the starting point for debates about machine intelligence and how to test it. [@turing1950computing]
- OECD (2024). *Explanatory memorandum on the updated OECD definition of an AI system*. A brief official document that explains each element of the definition used by many governments. [@oecd2024explanatory]
- Mitchell, M. (2021). *Why AI is harder than we think*. An accessible account of AI's springs and winters and of the reasoning errors that drive over-optimism. [@mitchell2021why]
- Bommasani, R., et al. (2021). *On the opportunities and risks of foundation models*. The report that coined the term; its introduction is a clear overview for non-specialists. [@bommasani2021opportunities]
- Mitchell, M., & Krakauer, D. C. (2023). *The debate over understanding in AI's large language models*. A balanced short review of the arguments on both sides of the understanding debate. [@mitchell2023debate]
- Crawford, K. (2021). *Atlas of AI*. A critical account of the minerals, labour and data on which AI depends, and of who holds power over it. [@crawford2021atlas]
- Stone, P., et al. (2016). *Artificial intelligence and life in 2030*. The first report of the One Hundred Year Study on AI, with a useful discussion of how to define AI. [@stone2016artificial]


# Chapter 2: How Neural Networks Learn

::: {.objectives}
**After working through this chapter you should be able to:**

- explain, with a small numerical example, how an artificial neuron turns inputs into an output using weights, a bias and an activation function;
- describe how a network learns by measuring its error with a loss function and reducing it through gradient descent and backpropagation;
- distinguish training, validation and test data, and use them to explain overfitting and generalisation;
- explain why layered networks learn their own features, and why parallel hardware such as GPUs made this practical;
- evaluate the strengths and limits of the comparison between artificial neural networks and the brain.
:::

In July 1958 the US Office of Naval Research demonstrated a program designed by Frank Rosenblatt, a research psychologist at the Cornell Aeronautical Laboratory. Running on an IBM 704 computer, it was shown punch cards marked either on the left or on the right, and after 50 trials it had learned to tell the two kinds apart [@lefkowitz2019professors]. The day after the press demonstration, *The New York Times* reported that the Navy had revealed "the embryo of an electronic computer" that it expected "will be able to walk, talk, see, write, reproduce itself and be conscious of its existence" [@newyorktimes1958new, p. 25; as reproduced in @ananthaswamy2024why]. None of that happened. Four decades later, however, a descendant of Rosenblatt's idea was doing something more modest and more useful: a network called LeNet-5, developed at AT&T's research laboratories, was reading the handwritten amounts on millions of bank cheques in the United States [@lecun1998gradient].

Both machines shared one feature. Nobody wrote down rules saying what a "left mark" or a handwritten "7" looks like. The machines were given examples and adjusted themselves until their answers were mostly right. This chapter explains how that adjustment works. It builds up, one step at a time, from a single artificial neuron to networks with millions or billions of adjustable numbers, using arithmetic that needs nothing beyond school mathematics. The same principles underlie the large language models of Chapter 3, so the effort spent here pays off later in the book.

## 2.1 The artificial neuron

An **artificial neuron** is a small calculation. It takes a few numbers as input, multiplies each one by a number called a **weight**, adds the results together, adds one more number called the **bias**, and then passes the total through a simple rule called an **activation function**. The output is a single number. That is all a neuron does, and everything a neural network achieves comes from connecting many of these small calculations together.

A worked example makes this concrete. Suppose a neuron has two inputs, 2 and 1. Its first weight is 0.5, its second weight is −1, and its bias is 0.2. The neuron first forms the **weighted sum**: 0.5 × 2 + (−1) × 1 + 0.2 = 1 − 1 + 0.2 = 0.2. It then applies its activation function. A common choice today is the **rectified linear unit**, or **ReLU**, which keeps positive numbers unchanged and turns negative numbers into zero; it is the default recommendation in Goodfellow, Bengio and Courville's widely used textbook *Deep Learning* [@goodfellow2016deep, sec. 6.1]. Since 0.2 is positive, the neuron outputs 0.2. If the inputs were instead 1 and 1, the weighted sum would be 0.5 − 1 + 0.2 = −0.3, and the ReLU would output 0. Figure 2.1 shows this calculation step by step.

![Figure 2.1: A single artificial neuron computing its output from two inputs. Each input is multiplied by its weight, the products and the bias are added (0.5 × 2 + (−1) × 1 + 0.2 = 0.2), and the activation function (here ReLU, which turns negative totals into zero) produces the output. Every larger network in this chapter is built from units like this one. Diagram by the author.](../figures/svg/fig-02-01.svg){#fig:02-01}

The weights say how much each input matters and in which direction. A large positive weight means "this input pushes the output up strongly"; a negative weight means "this input pushes it down". The bias shifts the whole total up or down, which sets how easily the neuron produces a non-zero output. An older activation function, the **sigmoid**, squashes any total into a number between 0 and 1; applied to our total of 0.2 it gives about 0.55. Without some such activation function, a network would be far less capable, for reasons explained in Section 2.2.

A helpful analogy is a sound engineer's mixing desk. Each input is a microphone, each weight is the volume slider on that channel, and the bias is a master offset. The activation function works like a noise gate that stays silent until the combined signal rises above a threshold. Unlike a real slider, though, a weight can go below zero and actively cancel an input, and nobody sets a network's sliders by ear: as later sections show, the network sets them itself, from data.

The idea has a long history. Warren McCulloch and Walter Pitts proposed in 1943 that, because of the "all-or-none" character of nervous activity, networks of idealised neurons could be described with the tools of logic [@mcculloch1943logical, p. 115]. Their neurons had fixed connections and could not learn. Rosenblatt's **perceptron** added the crucial ingredient: connection strengths that change with experience. He argued that information in the brain is "contained in connections or associations rather than topographic representations" [@rosenblatt1958perceptron, p. 387], and his machine stored what it learned in exactly that way.

## 2.2 Layers and the multilayer perceptron

A single neuron can only draw a straight dividing line through its inputs: everything on one side gets a high output, everything on the other a low one. Some simple problems cannot be solved that way. The best-known example is **XOR** ("exclusive or"): the output should be 1 when exactly one of two inputs is 1, and 0 when both inputs are 0 or both are 1. No single straight line separates these cases. Marvin Minsky and Seymour Papert's 1969 book *Perceptrons* proved this and related limits of single-layer perceptrons mathematically [@minsky1969perceptrons], and the critique contributed to a backlash against neural network research [@goodfellow2016deep, sec. 1.2.1].

The solution is to stack neurons in **layers**. The input layer simply holds the numbers fed in. One or more **hidden layers** of neurons each take the previous layer's outputs as their inputs. They are called hidden because their values are never seen directly in the training data. An **output layer** produces the final answer. A network in which every neuron in one layer feeds every neuron in the next is called a **multilayer perceptron** (MLP), or a fully connected feed-forward network. Figure 2.2 shows a small one.

![Figure 2.2: A small multilayer perceptron with three inputs, one hidden layer of four neurons and two outputs. Each line is a connection with its own weight, and each hidden and output neuron also has a bias, giving 3 × 4 + 4 × 2 = 20 weights and 4 + 2 = 6 biases: 26 parameters in all. Information flows left to right; learning adjusts all 26 numbers. Diagram by the author.](../figures/svg/fig-02-02.svg){#fig:02-02}

With one hidden layer, XOR becomes easy. Here is a network with two hidden neurons, both using ReLU, which matches the solution given in Goodfellow and colleagues' textbook [@goodfellow2016deep, sec. 6.1]. The first hidden neuron, *h*₁, computes the sum of the two inputs. The second, *h*₂, computes the sum minus 1, and its ReLU turns a negative result into 0. The output neuron takes the first hidden value and subtracts twice the second. Table 2.1 checks the four cases.

| Inputs | Correct answer | *h*₁ = sum | *h*₂ = sum − 1 (ReLU) | Output = *h*₁ − 2 × *h*₂ |
|---|---|---|---|---|
| (0, 0) | 0 | 0 | 0 | 0 |
| (1, 0) | 1 | 1 | 0 | 1 |
| (0, 1) | 1 | 1 | 0 | 1 |
| (1, 1) | 0 | 2 | 1 | 0 |

: Table 2.1: How a hidden layer solves XOR. The two hidden neurons re-describe each pair of inputs as a new pair of numbers (*h*₁, *h*₂); in these new coordinates a single weighted sum gives the right answer in all four cases. Calculation by the author, following @goodfellow2016deep.

Why does a straight line now work? In the original inputs, the two cases that should give 1, (1, 0) and (0, 1), sit at opposite corners of a square. The two 0 cases sit at the other two corners, so no line can separate them. In the hidden layer's coordinates, both 1 cases land on the same point, (1, 0), while the 0 cases land at (0, 0) and (2, 1). A line such as *h*₁ − 2 × *h*₂ = 0.5 now has the 1 cases on one side and the 0 cases on the other. The hidden layer has transformed the problem into one that a straight line can solve.

This example shows why the activation function matters. If every neuron only multiplied and added, stacking layers would gain nothing. A layer that doubles its input followed by a layer that triples it is the same as a single layer that multiplies by six. However many such layers we stacked, the result would still be a single straight-line rule. The bend introduced by ReLU, or the S-shape of a sigmoid, is what lets each extra layer add genuinely new ability. Mathematicians call such bends **non-linearities**.

How much can a network with hidden layers represent? In 1989 George Cybenko proved that a network with a single hidden layer of sigmoid neurons, given enough of them, can imitate any smooth input–output rule as closely as desired [@cybenko1989approximation]. (Mathematicians call such a rule a continuous function: one with no sudden jumps, so that a small change in the input never causes a sudden leap in the output.) This "universal approximation" result is often misread. It says that a suitable set of weights *exists*; it does not say that training will *find* it, or how many neurons are needed. As Goodfellow and colleagues put it, a large enough network can represent the function, but "we are not guaranteed" that the training algorithm will be able to learn it [@goodfellow2016deep, sec. 6.4.1]. In practice, the networks that have succeeded on real tasks stack many layers of neurons, which is where the term "deep" learning comes from [@lecun2015deep].

Every weight and bias in a network is a **parameter**: a number the network adjusts during learning. Counting parameters gives a rough sense of a network's size. The small network in Figure 2.2 has 26. LeNet-5, the cheque reader, had about 60,000 trainable parameters [@lecun1998gradient]. AlexNet, the image classifier that won the 2012 ImageNet competition (discussed in Chapter 1), had 60 million parameters and 650,000 neurons [@krizhevsky2012imagenet]. GPT-3, a language model released in 2020, had 175 billion [@brown2020language]. The arithmetic in each neuron is no harder than in our worked example; the difference is the number of neurons and how the weights were set.

## 2.3 Learning as error reduction

A freshly built network starts with random weights, so its answers are essentially arbitrary. **Training** is the process of adjusting the weights so that the answers improve. In the most common setting, **supervised learning**, the network is given many examples for which the correct answer, called a **label**, is known: images labelled "cat" or "dog", or scanned digits labelled "0" to "9". (Large language models mostly use a variant in which the "label" is simply the next word of a text; Chapter 3 explains this.)

To improve, the network needs a precise measure of how wrong it is. This measure is the **loss function** (also called the cost or objective function). It takes the network's output and the correct label and returns a single number: zero for a perfect answer, larger for worse ones. A simple example is the **squared error**. If the correct answer is 1 and the network outputs 0.2, the error is 0.8 and the squared error is 0.8 × 0.8 = 0.64. If the network outputs 0.9, the squared error falls to 0.01. Squaring makes all errors positive and punishes large errors much more than small ones.

For classification tasks, networks usually output a probability for each possible answer, and the loss most often used is **cross-entropy**. In words, it looks only at the probability the network gave to the correct answer and penalises low probabilities very heavily. The loss is the negative of the natural logarithm of that probability (the "ln" key on a calculator), and like squared error it is a plain number with no units. Giving the right answer a probability of 0.9 produces a loss of about 0.1 (−ln 0.9 ≈ 0.105). A probability of 0.1 produces about 2.3 (−ln 0.1), and a probability of 0.01 about 4.6 (−ln 0.01). Each tenfold fall in the probability adds another 2.3 or so to the loss, so a network that is confidently wrong is punished far more than one that is unsure. The loss over a whole dataset is the average of the losses on the individual examples.

With a loss function in place, learning becomes a well-defined task: find the weights that make the average loss as small as possible. In a widely cited 2015 review, Yann LeCun, Yoshua Bengio and Geoffrey Hinton describe the weights as "knobs" that define the network's behaviour, and training as turning them to reduce the error [@lecun2015deep, p. 436]. The difficulty is scale. A network with millions of knobs cannot be tuned by trying combinations at random; there are far too many. It needs a way of knowing which direction to turn each knob. That is what gradient descent provides.

### Gradient descent: walking downhill in fog

Imagine the loss as a landscape. Each possible setting of the weights is a location, and the height of the ground at that location is the loss. Good weights lie in the valleys. Training starts at a random spot on the hillside. The walker is in thick fog and cannot see the valley, but can feel the slope under their feet. The sensible strategy is to take a step in the steepest downhill direction, feel the slope again, and repeat. This strategy is called **gradient descent**, and the slope is called the **gradient**. The 2015 review uses the same image of a "hilly landscape" in the space of weight values [@lecun2015deep, p. 437]. Figure 2.3 sketches it.

![Figure 2.3: Gradient descent pictured as walking downhill. The curve shows how the loss (vertical axis) changes as one weight (horizontal axis) changes. Starting from a random weight, each step moves against the slope; a moderate learning rate approaches the minimum, while a learning rate that is too large overshoots to the other side. Real networks have millions of weights, so the true landscape has millions of dimensions. Schematic, not to scale. Diagram by the author.](../figures/svg/fig-02-03.svg){#fig:02-03}

A worked example with a single weight shows the mechanics. Take a neuron with no bias and no activation function, one input of 2, and a current weight of 0.2. The correct answer is 1. The neuron outputs 0.2 × 2 = 0.4, so the error is 0.6 and the squared-error loss is 0.36. Now ask what happens if the weight is nudged up slightly, to 0.21. The output becomes 0.42 and the loss becomes 0.58 × 0.58 ≈ 0.336. Raising the weight by 0.01 lowered the loss by about 0.024, so the slope is roughly −2.4: increasing the weight decreases the loss. (The exact slope, which calculus gives directly, is −2.4.)

Gradient descent always moves a weight in the direction opposite to its slope. How far it moves is set by the **learning rate**, a number chosen by the people training the network. The step is minus the learning rate times the slope. With a learning rate of 0.1, that is −0.1 × (−2.4) = +0.24: the slope is negative, so the weight goes up, from 0.2 to 0.44. The output becomes 0.88 and the loss falls from 0.36 to about 0.014. Repeating the step brings the weight ever closer to 0.5, where the output is exactly 1 and the loss is zero. Now try a learning rate of 0.5 instead. The step is −0.5 × (−2.4) = +1.2, the weight jumps to 1.4, the output becomes 2.8, and the loss rises to 3.24. The walker has leapt clean across the valley and up the other side. Choosing the learning rate is a balance: too small and training crawls, too large and it overshoots or diverges.

::: {.box .concept}
**Key concept: The gradient**

The gradient is a list containing one number for every weight in the network. Each number says how much the loss would rise or fall if that weight were increased by a tiny amount [@lecun2015deep, p. 436]. Gradient descent moves every weight a small step in the direction that lowers the loss, with step size set by the learning rate. The gradient gives only local information, like the slope under one's feet; it says nothing directly about where the lowest valley lies.
:::

Two refinements make this practical. First, computing the exact average loss over millions of training examples before every step would be very slow. Practitioners instead use **stochastic gradient descent** (SGD): they compute the gradient on a small random batch of examples, take a step, and move on to the next batch. Each batch gives a noisy estimate of the true slope, yet the procedure "usually finds a good set of weights surprisingly quickly" [@lecun2015deep, p. 437]. One complete pass through the training data is called an **epoch**. Second, many modern training runs use variants of SGD that adapt the step size for each weight automatically, but the underlying idea is the same.

The fog analogy is useful, but it breaks down in instructive ways. The real landscape has as many dimensions as the network has parameters, which no one can picture. Because each batch is different, the ground also shifts slightly under the walker's feet at every step. Finally, people once feared that the walker would get stuck in a small hollow far above the best valley, a poor **local minimum**. In large networks this turned out to be less serious than expected: poor local minima "are rarely a problem". The flat places the walker meets are mostly saddle points instead. Like the middle of a horse's saddle, they curve upwards in some directions and downwards in others. Almost all of them lie at a similar height, so it matters little which one training settles near [@lecun2015deep, p. 438].

## 2.4 Backpropagation: sharing out the blame

Gradient descent needs the slope for every weight. In a network with one weight, we found it by nudging the weight and watching the loss. With 60 million weights, that approach would require 60 million separate test runs for each step, which is hopeless. The challenge is sometimes called the **credit assignment problem**: when the final answer is wrong, how much blame belongs to each connection, including those buried deep inside the network?

**Backpropagation** solves it efficiently. Training alternates two passes. In the **forward pass**, an example flows through the network layer by layer, from the inputs to the output, and the loss is computed. In the **backward pass**, the error signal flows the other way, from the output layer back towards the inputs. At each connection, the algorithm works out how much a small change in that weight would have changed the loss, using quantities already computed in the forward pass. Each neuron receives a share of the blame in proportion to how strongly it influenced the neurons above it, and it passes blame on to the neurons below it in the same way.

An organisational analogy can help. Picture a firm whose quarterly figures came in below target. The board does not audit every employee from scratch. It asks each division head how far their division contributed to the shortfall; each head asks their team leaders; and so on down the hierarchy, with each level reusing the figures already passed down from above. In a real firm, however, blame is negotiated and often unfair. In backpropagation it is exact arithmetic: every weight receives precisely the share of responsibility that the mathematics assigns, and every weight is then adjusted at once.

The efficiency gain is large. For the standard case, computing all the slopes by backpropagation costs about the same order of computation as the forward pass itself [@goodfellow2016deep, sec. 6.5]. Learning from an example therefore costs only a small multiple of simply running the network on it, however many weights it has. Without this, training networks with millions or billions of parameters would be impractical.

The underlying mathematics is a centuries-old rule from calculus called the chain rule. Efficient ways of applying it to long chains of calculations were developed from the 1960s onwards and were discovered for neural networks several times over [@goodfellow2016deep, sec. 6.6]. A 1986 *Nature* paper by David Rumelhart, Geoffrey Hinton and Ronald Williams made the method widely known. It notes that, as a result of the weight adjustments, "internal 'hidden' units which are not part of the input or output come to represent important features of the task domain" [@rumelhart1986learning, p. 533]. That observation anticipates Section 2.6: hidden layers do not merely relay information, they learn useful ways of describing it.

::: {.box .deeper}
**Going deeper: The chain rule and backpropagation in one page**

Consider the smallest possible "deep" network: an input *x* = 1, a hidden neuron *h* = *w*₁ × *x*, an output *y* = *w*₂ × *h*, and a loss *L* = (*y* − *t*)², where *t* is the target. Let *w*₁ = 2, *w*₂ = 0.5 and *t* = 2. The forward pass gives *h* = 2, *y* = 1 and *L* = 1.

The backward pass asks how *L* changes when each weight changes. The **chain rule** says that when one quantity affects a second, which affects a third, the overall rate of change is the product of the individual rates. In symbols, ∂*L*/∂*w*₁ = (∂*L*/∂*y*) × (∂*y*/∂*h*) × (∂*h*/∂*w*₁). The symbol ∂ means "rate of change of the top quantity when only the bottom one is varied".

- Step 1, the output: ∂*L*/∂*y* = 2(*y* − *t*) = 2 × (1 − 2) = −2. Raising *y* would lower the loss.
- Step 2, the last weight: ∂*L*/∂*w*₂ = (∂*L*/∂*y*) × *h* = −2 × 2 = −4.
- Step 3, pass the blame down to the hidden neuron: ∂*L*/∂*h* = (∂*L*/∂*y*) × *w*₂ = −2 × 0.5 = −1.
- Step 4, the first weight: ∂*L*/∂*w*₁ = (∂*L*/∂*h*) × *x* = −1 × 1 = −1.

Notice that step 4 reused the result of step 3, and step 3 reused step 1. That reuse is the whole trick: each layer's gradient is built from the one above it, so nothing is computed twice. If the hidden neuron had a ReLU activation, step 3 would also be multiplied by the ReLU's slope (1 if the neuron's total was positive, 0 if it was negative). With a learning rate of 0.1, gradient descent would update *w*₂ to 0.5 + 0.4 = 0.9 and *w*₁ to 2 + 0.1 = 2.1, giving a new output of 1.89, much closer to the target of 2. Real networks apply exactly these steps to vectors and matrices of weights [@lecun2015deep, fig. 1; @goodfellow2016deep, sec. 6.5].
:::

## 2.5 Training, validation and test data: the problem of generalisation

A network that only reproduced its training examples would be useless; we already know the answers to those. What matters is how well it performs on new cases it has never seen. This ability is called **generalisation**, and it is what separates machine learning from mere optimisation [@goodfellow2016deep, sec. 5.2].

To measure generalisation honestly, the available data are split into three parts. The **training set** is used to adjust the weights. The **validation set** is used during development to compare different design choices and decide when to stop training. The **test set** is held back until the very end and used once, to estimate how the finished system will perform in the world. The ImageNet competition dataset on which AlexNet was trained and evaluated, for example, contained roughly 1.2 million training images, 50,000 validation images and 150,000 test images [@krizhevsky2012imagenet]. An exam analogy fits well. The training set is the practice questions, the validation set is a mock exam used to decide how to revise, and the test set is the real exam, which must stay sealed until the end. If a teacher keeps adjusting the course after seeing the real exam, the final mark stops meaning much. The same thing happens when developers repeatedly tune a system on its test set.

**Overfitting** occurs when a network fits its training data closely but performs worse on new data, because it has learned accidental quirks of the training examples along with the genuine patterns. Figure 2.4 shows the classic signature. As training continues, the error on the training set keeps falling. The error on the validation set falls at first, then levels off and starts to rise. The point where validation error is lowest is where the network generalises best. Even well-designed networks show some gap: LeNet-5 reached an error rate of 0.35% on its training digits but 0.95% on the test digits [@lecun1998gradient].

![Figure 2.4: The classic overfitting curve. Training error (solid line) keeps falling as training continues, while validation error (dashed line) falls, reaches a minimum and then rises as the network starts to memorise quirks of the training data. Early stopping halts training near the validation minimum. Schematic, not to scale. Diagram by the author.](../figures/svg/fig-02-04.svg){#fig:02-04}

Researchers have several tools against overfitting, collectively called **regularisation**. The simplest is more, and more varied, training data. Another is **early stopping**: halting training at the point of lowest validation error, which Goodfellow and colleagues call "probably the most commonly used form of regularization in deep learning" [@goodfellow2016deep, sec. 7.8]. A third, **dropout**, randomly switches off a fraction of neurons at each training step, so that the network cannot rely on any single neuron and must spread what it learns across many [@srivastava2014dropout]. AlexNet used dropout to curb overfitting in its fully connected layers [@krizhevsky2012imagenet].

::: {.box .concept}
**Key concept: Parameters and hyperparameters**

**Parameters** are the weights and biases that the network learns from data. **Hyperparameters** are the settings that people choose before or around training and that the learning algorithm does not adjust itself [@goodfellow2016deep, sec. 5.3]. Examples are the number of layers, the number of neurons per layer, the learning rate, the batch size, the dropout rate and the number of training epochs. Hyperparameters are typically chosen by comparing results on the validation set, never on the test set.
:::

The textbook picture of overfitting has been complicated by modern deep learning. Zhang and colleagues showed that standard image-classification networks can perfectly fit training images whose labels have been replaced by random ones, which means they have enough capacity to memorise pure noise [@zhang2017understanding]. Yet the same networks, trained on real labels, generalise well. Classical theory struggles to explain why. Belkin and colleagues documented a "double descent" pattern [@belkin2019reconciling]. Note that it concerns model size, not training time, which is what Figure 2.4 plots. As models are made larger, test error first falls and then rises (the classical U-shaped curve) up to the size at which a model can just fit every training example exactly. Beyond that point, making the model larger still makes test error fall again. Why very large networks generalise as well as they do remains an active research question. The practical lesson stands, however: only performance on data held out from training tells us how a network will behave on new cases.

## 2.6 What the layers learn: representations, convolutions and GPUs

Before deep learning, building a system to recognise objects in photographs required experts to design **features** by hand: rules for detecting edges, corners or particular textures, which were then fed to a simpler learning method. The central claim of deep learning is that a network can learn its own features. The 2015 review describes a typical image network as follows [@lecun2015deep, p. 436]. The first layer learns to detect edges at particular orientations and locations. The second detects motifs, meaning particular arrangements of edges. The third assembles motifs into parts of familiar objects, and later layers detect objects as combinations of parts. Crucially, "these layers of features are not designed by human engineers: they are learned from data". This is called **representation learning**: each layer re-describes the input in terms that make the final task easier.

This account rests on more than theory. Zeiler and Fergus developed a method for visualising what individual parts of a trained image network respond to [@zeiler2014visualizing]. In their network, units in the second layer responded to corners and combinations of edge and colour. The third layer captured textures such as mesh patterns, the fourth responded to more class-specific parts such as dog faces; and the fifth to whole objects such as keyboards. It is tempting to picture a factory assembly line, with each station adding detail, but nobody assigned these stations their jobs. A widely cited study also found that meaning is often spread across many units at once instead of sitting neatly in single ones [@szegedy2014intriguing].

### Convolutional networks

Images pose a particular problem for the fully connected networks of Section 2.2. A photograph of 1,000 by 1,000 pixels has a million input values, so a single fully connected layer of even a thousand neurons would need a billion weights. Worse, a cat in the top-left corner and a cat in the bottom-right would have to be learned separately. **Convolutional neural networks** (CNNs) address both problems. Their four key ideas are local connections, shared weights, pooling and the use of many layers [@lecun2015deep, p. 439].

In plain terms, a convolutional layer slides a small detector, perhaps three by three pixels, across the whole image, applying the same weights at every position. Because the same detector is reused everywhere, an edge or an eye is recognised wherever it appears, and the number of weights stays small. **Pooling** then summarises nearby detector outputs, so that small shifts in position matter less. The savings are substantial: LeNet-5 had more than 340,000 connections but only 60,000 trainable parameters because of weight sharing [@lecun1998gradient]. The design drew on studies of nerve cells in the visual cortex of cats [@hubel1962receptive] and on an earlier network of 1980, the "neocognitron" [@fukushima1980neocognitron].

### Why GPUs matter

Look back at the worked examples in this chapter and one pattern stands out: almost all of the work is multiplying numbers and adding them up. A large network does the same, billions of times per example, and most of those calculations do not depend on one another. They can be done simultaneously. **Graphics processing units** (GPUs) were developed for video games, where the colour of millions of pixels must be computed in parallel using simple, repetitive arithmetic. That turned out to be just what neural networks need [@goodfellow2016deep, sec. 12.1.2]. A central processing unit (CPU) is like a small team of highly skilled specialists who handle varied tasks one after another; a GPU is like a vast hall of clerks who each do simple sums at the same moment. Modern CPUs also have some parallel capacity, but the contrast captures why the work suits GPUs.

The practical effect was large. In 2009 Raina, Madhavan and Ng reported that running training on GPUs cut the time needed to train a four-layer network (a "deep belief network") with 100 million parameters "from several weeks to around a single day" [@raina2009large]. AlexNet was trained in five to six days on two consumer gaming GPUs, and its authors wrote that their results could be improved "simply by waiting for faster GPUs and bigger datasets to become available" [@krizhevsky2012imagenet, p. 1098]. The ability to throw ever more parallel computation at the same simple arithmetic is the foundation of the scaling trends in Chapter 4 and of the chip industry discussed in Chapter 7.

## 2.7 What neural networks are bad at, and the brain analogy

The same properties that make neural networks powerful also produce characteristic weaknesses. Four are well documented, and each follows from the mechanics described above.

**Adversarial examples.** Szegedy and colleagues showed that an "imperceptible non-random perturbation" could cause an image network to misclassify an image [@szegedy2014intriguing]. In a widely reproduced example, Goodfellow, Shlens and Szegedy took a photograph that a network classified as a panda with 57.7% confidence. They added a pattern too faint for a person to notice, and the network then classified it as a gibbon with 99.3% confidence [@goodfellow2015explaining, fig. 1]. Those authors argue that the main cause is the largely linear behaviour of networks: because a decision depends on weighted sums over very many inputs, a great many tiny, carefully chosen changes can add up to a large change in output.

**Shortcut learning.** Gradient descent finds whatever weights reduce the loss on the training data, whether or not they capture the reason a human would give. Geirhos and colleagues define shortcuts as "decision rules that perform well on standard benchmarks but fail to transfer" to more challenging conditions, and argue that many failures of deep learning share this cause [@geirhos2020shortcut, p. 665]. The case study below gives a medical example.

**Catastrophic forgetting.** A network trained on one task and then trained on a second tends to overwrite the weights that served the first, losing the earlier skill. Kirkpatrick and colleagues note that this had long been "widely thought" to be "an inevitable feature" of such models, and proposed a partial remedy that slows learning on the weights most important for old tasks [@kirkpatrick2017overcoming, p. 3521].

**Data hunger and opacity.** Networks usually need very large labelled datasets: a typical deep-learning system in 2015 might have had hundreds of millions of weights and been trained on hundreds of millions of labelled examples [@lecun2015deep, p. 436]. And because what a network "knows" is spread across millions of numbers, explaining why it gave a particular answer is hard; Chapter 12 describes the research field that tries.

::: {.box .case}
**Case study: The pneumonia detector that recognised hospitals**

In 2018 Zech and colleagues trained convolutional networks to detect pneumonia on 158,323 chest X-rays from three US hospital systems [@zech2018variable]. The rate of pneumonia differed greatly between sites: 34.2% at Mount Sinai Hospital, against 1.2% at the National Institutes of Health Clinical Center and 1.0% at Indiana University. Merely sorting X-rays by hospital system, without looking at the lungs at all, achieved an area under the curve (a standard accuracy score, where 0.5 is chance and 1.0 is perfect) of 0.861 on the combined Mount Sinai and NIH data. The networks could identify which hospital system an NIH or Mount Sinai X-ray came from with more than 99.9% accuracy. A model trained and tested on pooled data from two sites scored 0.931 internally, but significantly less (0.815) on the third, unseen hospital. The authors concluded that the networks' ability to recognise the hospital and department "may confound predictions". In the language of this chapter, the training loss could be reduced by learning where an image came from, and gradient descent duly learned it.
:::

### The biological analogy and its limits

The words "neuron" and "neural network" invite the assumption that these systems work like brains. The resemblance is real but thin. Artificial neurons were inspired by biological ones [@mcculloch1943logical; @rosenblatt1958perceptron], and convolutional networks borrowed ideas from the visual cortex [@lecun2015deep]. But a biological neuron is far more complex than a weighted sum followed by a ReLU. Beniaguev, Segev and London trained artificial networks to reproduce the input–output behaviour of a detailed computer model of a single cortical neuron and found that a network with five to eight layers was needed to capture it [@beniaguev2021single]. On that evidence, one biological neuron may be closer to a whole deep network than to one artificial unit.

Scale comparisons need similar care. The adult human brain contains about 86 billion neurons [@azevedo2009equal]. It is tempting to compare this with GPT-3's 175 billion parameters [@brown2020language], but the comparison mixes categories: parameters correspond loosely to connection strengths, the synapses between neurons, and not to neurons. The learning rule is a further difference. Backpropagation requires sending precise error signals backwards through the same connections, and Lillicrap and colleagues note that it "historically" has been "viewed as biologically problematic" [@lillicrap2020backpropagation, p. 335].

::: {.box .debate}
**Debate: Are artificial neural networks good models of the brain?**

*Yes, in useful ways.* Yamins and colleagues trained image networks only to recognise objects well, with no brain data used in training. These networks predicted the responses of neurons in the monkey's inferior temporal cortex, a high-level visual area, and their intermediate layers predicted responses in the mid-level area V4 [@yamins2014performance]. Lillicrap and colleagues argue that the brain's abundant feedback connections may approximate the error signals of backpropagation [@lillicrap2020backpropagation].

*Only loosely.* Single biological neurons perform computations that need a multi-layer artificial network to reproduce [@beniaguev2021single]. Lillicrap and colleagues themselves acknowledge that it is difficult to see how the brain's feedback connections could deliver the precise error signals that strict backpropagation requires [@lillicrap2020backpropagation]. Networks also show failures, such as adversarial examples, that do not resemble human perception [@goodfellow2015explaining].

*What would settle it:* direct measurement of whether, and how, learning signals in the cortex resemble the gradients computed by backpropagation, and whether brain-like networks also share the brain's robustness to adversarial perturbations.
:::

## Summary

- An artificial neuron multiplies its inputs by weights, adds a bias and applies an activation function such as ReLU; for example, 0.5 × 2 + (−1) × 1 + 0.2 = 0.2.
- Stacking neurons in layers, with non-linear activations, lets a network solve problems a single neuron cannot, such as XOR. A large enough network can represent almost any function, but that does not guarantee training will find it.
- Training reduces a loss function, such as squared error or cross-entropy, that measures how wrong the network's answers are.
- Gradient descent adjusts every weight a small step downhill on the loss landscape; the learning rate sets the step size, and stochastic gradient descent uses small batches of examples.
- Backpropagation computes the slopes for all weights efficiently by passing error signals backwards through the network using the chain rule.
- Generalisation to new data is measured on held-out validation and test sets; overfitting is countered by more data, early stopping and dropout, though very large networks generalise better than classical theory predicts.
- Deep networks learn their own layered features; convolutional networks share weights across an image; GPUs made training practical because the work is massively parallel arithmetic.
- Networks are vulnerable to adversarial examples, shortcut learning and catastrophic forgetting, and the analogy with the brain holds only loosely.

## Key terms

artificial neuron · weight · activation function · multilayer perceptron · parameter · hyperparameter · loss function · gradient descent · learning rate · backpropagation · overfitting · generalisation · representation learning · convolutional neural network · GPU

## Discussion questions

1. Using the neuron from Section 2.1 (weights 0.5 and −1, bias 0.2, ReLU activation), compute the output for inputs (4, 1) and (0, 3). What does the negative weight on the second input mean for how the neuron "treats" that input?
2. The fog-on-a-hillside analogy for gradient descent breaks down in several ways. Identify two, and explain which one you think matters most for understanding why training sometimes fails.
3. A university builds a network to predict which applicants will complete their degree, using records from past students. Apply the ideas of training, validation and test data, and of shortcut learning, to explain how the system could look accurate in development yet perform poorly or unfairly in use.
4. Evaluate the evidence in the case study on pneumonia detection. What does it show about the networks, and what would you want to know before concluding that such tools should not be used in hospitals?
5. Zhang et al. (2017) showed that networks can memorise random labels, yet the same networks generalise well on real data. Why is this puzzling from the perspective of the classical account of overfitting in Section 2.5, and what does it imply about how much we understand deep learning?
6. Is it misleading to call these systems "neural" networks? Weigh the evidence in the Debate box and decide whether the term helps or hinders public understanding.

## Further reading

- Goodfellow, I., Bengio, Y. and Courville, A. (2016). *Deep Learning*. A widely used graduate textbook; chapters 5–9 cover most of this chapter with full mathematics, and it is free online. [@goodfellow2016deep]
- LeCun, Y., Bengio, Y. and Hinton, G. (2015). *Deep learning*. A short, authoritative review in *Nature* by three pioneers of the field, readable with this chapter as background. [@lecun2015deep]
- Nielsen, M. A. (2015). *Neural Networks and Deep Learning*. A free online book that builds a digit-recognising network from scratch, with interactive explanations of gradient descent and backpropagation. [@nielsen2015neural]
- Ananthaswamy, A. (2024). *Why Machines Learn: The Elegant Maths Behind Modern AI*. A science journalist's accessible history of the mathematics behind machine learning, from the perceptron onwards. [@ananthaswamy2024why]
- Geirhos, R. et al. (2020). *Shortcut learning in deep neural networks*. A clear, non-technical perspective on why networks that score well on benchmarks can fail in the real world. [@geirhos2020shortcut]


# Chapter 3: How Large Language Models Work

::: {.objectives}
**After working through this chapter you should be able to:**

- explain how a large language model turns text into tokens and embeddings, and why it is trained to predict the next token;
- describe, in plain words, what attention does inside a transformer and why the context window is limited;
- compare the stages of pre-training and post-training, including instruction tuning, reinforcement learning from human feedback and Constitutional AI;
- evaluate why language models produce confident errors ("hallucinations") and how far retrieval and reasoning training reduce them;
- apply these ideas to judge what a given chatbot answer can and cannot be trusted for.
:::

In May 2020 a team at OpenAI described GPT-3, a neural network with 175 billion parameters [@brown2020language]. It had been trained on one narrow task: guessing the next piece of text in a very large collection of web pages, books and Wikipedia articles. Nobody had trained it to translate, answer questions or do sums. Yet when the researchers typed a few worked examples into the model, it carried on the pattern and performed tasks such as translation, question answering and three-digit arithmetic. The paper stressed that it did this "without any gradient updates or fine-tuning", meaning that the network's weights were not changed for the new task.

That observation is the puzzle at the centre of this chapter. How can a system trained only to continue text end up writing essays, explaining code and passing exams, and why does the same system sometimes invent facts with complete confidence? Chapter 2 explained how neural networks learn by adjusting weights to reduce a loss. This chapter builds on that foundation. It follows a sentence through a large language model (LLM), from the moment it is chopped into pieces to the moment a reply appears on screen. It then explains how the raw text-predictor is turned into a helpful assistant.

## 3.1 From text to numbers: tokens

A neural network can only do arithmetic, so the first job of any language model is to turn text into numbers. It does this by splitting the text into **tokens**: frequently occurring chunks of characters, each with a fixed identification number. A token is often a whole common word, sometimes a fragment of a longer word, and sometimes a single character or punctuation mark. The list of all tokens a model knows is called its **vocabulary**.

Table 3.1 shows a real example. The sentence "Students in Edinburgh rarely misunderstand tokenisation." was passed through `o200k_base`, the tokeniser that OpenAI's open-source `tiktoken` library assigns to GPT-4o and later OpenAI models [@openai2026tiktoken]. The sentence has six words but becomes eight tokens. Common words such as "Students" and "rarely" survive whole, and even "misunderstand" has its own token. The less common "tokenisation", with its British spelling, is split into " token" and "isation". Notice also that most tokens carry their leading space with them: " in" (with a space) and "in" (without) are different tokens with different numbers.

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

: Table 3.1: A real tokenisation. The sentence "Students in Edinburgh rarely misunderstand tokenisation." becomes eight tokens, each with an ID number, in the `o200k_base` tokeniser used for GPT-4o: six words become eight tokens, because "tokenisation" is split into two. Quotation marks show where a token includes a leading space. Computed by the author with tiktoken 0.14.0 on 22 October 2026. Source: @openai2026tiktoken.

| Language | `o200k_base` tokens (2024) | GPT-2 tokens (2019) |
|---|---|---|
| English | 7 | 7 |
| German | 9 | 15 |
| Hindi | 12 | 62 |
| Swahili | 13 | 20 |

: Table 3.2: The same short sentence costs different numbers of tokens in different languages. Texts: "I love learning about language models." and close translations, in German "Ich lerne gern über Sprachmodelle.", in Swahili "Ninapenda kujifunza kuhusu mifano ya lugha." and in Hindi (Devanagari script). Counts computed by the author as for Table 3.1 (encodings `o200k_base` and `gpt2`). Source: @openai2026tiktoken; @petrov2023language.

Where does the vocabulary come from? Most current tokenisers use a method called **byte-pair encoding**, adapted for language processing by @sennrich2016neural. It starts with single characters and repeatedly merges the pair of symbols that occurs most often in a large sample of text, adding each merged pair to the vocabulary. After many thousands of merges, frequent words have become single tokens while rare words remain divisible into parts. GPT-2 introduced a byte-level version, in which the starting symbols are the 256 possible bytes that computers use to store text rather than the characters of a particular alphabet [@radford2019language]. With a byte-level tokeniser, such as OpenAI's, a model never meets a word it cannot represent: an unfamiliar name, a typing error or an emoji is simply spelled out in smaller pieces. Vocabularies have grown over time. GPT-2's tokeniser has 50,257 tokens, while `o200k_base` has roughly 200,000 [@openai2026tiktoken].

Tokenisation has consequences that users notice. Because the model sees " strawberry" as one token rather than as ten letters, questions about spelling or letter counts are harder for it than they look. Tokenisation also treats languages unequally. Table 3.2 shows the sentence "I love learning about language models." and close translations. In `o200k_base` the English version needs 7 tokens, German 9, Hindi 12 and Swahili 13; in the older GPT-2 tokeniser the Hindi version needs 62. @petrov2023language found that the same text translated into different languages could differ in tokenised length by up to 15 times. Since commercial services charge per token and limit how many tokens a model can read, speakers of under-represented languages can pay more and fit less into each request.

::: {.box .concept}
**Key concept: Token**

A token is the basic unit a language model reads and writes: usually a word, part of a word, or a punctuation mark, each mapped to a fixed number. As a rough rule for English, a token is a little shorter than an average word, so 100 words become somewhat more than 100 tokens. Prices, speed limits and memory limits of language models are all counted in tokens, which is why the same request can cost different amounts in different languages.
:::

## 3.2 Embeddings: words as points in space

A token number on its own carries no meaning. The number 9059 (" cat" in `o200k_base`) is not "closer" to a dog than 9060 is. So the next step converts each token into an **embedding**: a long list of numbers that places the token as a point in a high-dimensional space. In the smallest GPT-2 model each embedding has 768 numbers; in Meta's largest Llama 3 model it has 16,384, according to Meta's technical report [@radford2019language; @grattafiori2024llama]. These numbers are not designed by hand. They start random and are adjusted by gradient descent during training, in exactly the way Chapter 2 described for any other weight.

The idea that useful meanings emerge from such training was demonstrated vividly by the word2vec models, described in a preprint by @mikolov2013efficient and trained on 1.6 billion words. Words used in similar contexts ended up near one another, so "Paris" lay close to "Berlin" and "cat" close to "dog". Mathematically, an embedding is a **vector**, which simply means an ordered list of numbers that can be added and subtracted position by position. More surprisingly, directions in the space captured relationships. @mikolov2013linguistic reported that the calculation "King − Man + Woman" produced a vector very close to the one for "Queen". The difference between "man" and "woman" behaved like a consistent direction that could be added to other words. Figure 3.1 sketches this idea in two dimensions.

![Figure 3.1: An embedding space, sketched in two dimensions. Words used in similar ways sit close together, and some relationships (such as male to female, or country to capital) appear as roughly parallel arrows. Real embeddings have hundreds or thousands of dimensions. Schematic, not to scale. Source: illustrating findings of @mikolov2013linguistic.](../figures/svg/fig-03-01.svg){#fig:03-01}

The map analogy is helpful but breaks down in two ways. First, nobody can picture 768 dimensions, and the two-dimensional sketch inevitably distorts distances. Second, and more important, word2vec gave each word a single fixed point, so "bank" had the same embedding whether it meant a riverbank or a lender. A modern LLM uses its embedding table only as a starting point. As the token passes through the network's layers, its representation is repeatedly updated using the surrounding words. By the upper layers, "bank" in "the river bank" and "bank" in "the bank raised rates" are represented quite differently. Section 3.4 explains the mechanism that makes this possible.

## 3.3 Predicting the next token

At its core, an LLM performs one operation over and over. Given a sequence of tokens, it outputs a probability for every token in its vocabulary being the next one. This is called **next-token prediction**, and a model that generates text this way, one token at a time and each time feeding its own output back in as input, is called **autoregressive**. A long answer from a chatbot is the result of hundreds or thousands of such predictions in a row.

The loop is easiest to see step by step. Suppose the text so far is "The cat sat on the". The model computes probabilities for every token in its vocabulary. For GPT-2 XL the front-runners are " edge" (7.3 per cent), " floor" (5.2) and " table" (4.9), while the nursery-rhyme " mat" is not among the top eight (these are the values plotted in Figure 3.2). One token, say " floor", is chosen and appended, giving "The cat sat on the floor". The whole extended sequence then goes back into the model to produce probabilities for the following token, perhaps "." or " and". Generation stops when the model produces a special end-of-text token or reaches a length limit. The model therefore never drafts a whole answer and then revises it: each token is committed once chosen, and later tokens must make the best of earlier ones. Because every token requires a full pass through the network, longer answers also cost proportionally more computation.

Table 3.3 shows real predictions. The prompt "The capital of France is" was given to three openly available models, and the table lists each model's five most likely next tokens with their probabilities. The smallest GPT-2 model (reported in the GPT-2 paper as 117 million parameters; the released version has about 124 million) gives "Paris" only 3.2 per cent and prefers " the". The largest GPT-2 model (about 1.5 billion parameters, released in 2019) raises "Paris" to 8.6 per cent [@radford2019language]. Qwen2.5-1.5B, released by Alibaba in 2024 with a similar number of parameters, gives "Paris" 27.3 per cent; according to the company's technical report, Qwen2.5 models were trained on up to 18 trillion tokens [@qwen2024qwen25]. Even then, most of the probability is spread over other continuations, such as " located" or blank underscores that hint at fill-in-the-gap exercises in the training data.

| Rank | GPT-2 small (2019) | GPT-2 XL (2019) | Qwen2.5-1.5B (2024) |
|---|---|---|---|
| 1 | " the" 8.5% | " the" 10.1% | " Paris" 27.3% |
| 2 | " now" 4.8% | " a" 9.9% | " located" 6.3% |
| 3 | " a" 4.6% | " Paris" 8.6% | " a" 4.5% |
| 4 | " France" 3.2% | " in" 2.5% | " \_\_" 4.4% |
| 5 | " Paris" 3.2% | " one" 2.4% | " \_\_\_\_\_\_" 4.2% |

: Table 3.3: Next-token probabilities after the prompt "The capital of France is" for three open-weight base models (no post-training). Computed by the author on 22 October 2026 with the Hugging Face `transformers` library at temperature 1; percentages rounded. Sources of the models: @radford2019language; @qwen2024qwen25.

A base model models what text tends to come next, and "The capital of France is the city of Paris" or "The capital of France is located on the Seine" are perfectly good continuations. Turning such a model into one that answers questions directly is the job of post-training (Section 3.5).

How does the model learn these probabilities? Training uses the text itself as the answer key, which is why it is called **self-supervised learning**: no human labelling is needed. The model reads a passage, predicts each next token, and is then shown the token that actually came next. The loss (Chapter 2) is large when the model gave the true token a low probability and small when it gave it a high one; informally, the loss measures how surprised the model was. Gradient descent then nudges billions of weights so that the model will be a little less surprised next time. Repeated over trillions of tokens, this simple pressure forces the model to absorb grammar, facts, styles of argument and much else, because all of these help to predict text.

**Sampling and temperature.** Once the model has produced its probabilities, a separate procedure called **decoding** picks the actual token. Always choosing the single most likely token ("greedy" decoding) tends to produce dull and repetitive text. @holtzman2020curious showed that likelihood-maximising decoding leads to text that is "bland and strangely repetitive". They proposed **nucleus sampling** (also called top-p sampling), which draws randomly from only the smallest set of tokens that together cover most of the probability. Most chat systems therefore sample: they roll weighted dice.

Where do the probabilities themselves come from? The network's final layer first produces a raw score for every token in the vocabulary, called a **logit**, which can be any positive or negative number. A function called **softmax** then turns these scores into probabilities. It makes every score positive (by raising a fixed number, about 2.7, to the power of the score) and divides each result by the total, so that the results add up to one and the highest scores receive a disproportionately large share.

The **temperature** setting controls how weighted those dice are: the logits are divided by the temperature before the softmax is applied. Table 3.4 shows GPT-2 XL continuing "After the lecture, the students went to the". At the default temperature of 1, " cafeteria" has 7.5 per cent and " library" 4.9 per cent. Lowering the temperature to 0.5 sharpens the distribution, so that " cafeteria" rises to 51.7 per cent and " library" to 21.9 per cent, while unlikely options almost vanish. Raising the temperature flattens it, making surprising choices more frequent. A temperature near zero behaves like greedy decoding. Low temperatures suit tasks with one right answer, such as extracting a date from a document. Higher ones suit brainstorming, at the cost of more odd choices.

| Next token | Temperature 1.0 | Temperature 0.5 |
|---|---|---|
| " cafeteria" | 7.5% | 51.7% |
| " library" | 4.9% | 21.9% |
| " gym" | 2.5% | 5.8% |
| " auditor" (first part of "auditorium") | 2.1% | 4.1% |
| " dining" | 1.8% | 3.1% |

: Table 3.4: The effect of temperature on GPT-2 XL's next-token probabilities after "After the lecture, the students went to the". Computed by the author as for Table 3.3. Source of the model: @radford2019language.

## 3.4 Attention and the transformer

Predicting the next token well requires using the right earlier words. In "The Law will never be perfect, but its application should be just", the word "its" refers back to "Law", several words earlier. Before 2017, most language models processed text one word at a time with recurrent networks, passing a running summary from step to step. Information from far back tended to fade, and the step-by-step design was slow to train because each step had to wait for the previous one.

The **transformer**, introduced by @vaswani2017attention in a paper titled "Attention Is All You Need", removed that bottleneck. It dispensed "with recurrence and convolutions entirely" and relied instead on a mechanism called **attention**. In attention, every token's representation can directly look at every other token's representation and decide how much to draw from each. A useful analogy is a seminar in which each word may consult any other word. Each word forms a question ("which earlier word do I refer to?") and offers a label describing what it contains. Each word then takes a weighted mix of the information offered by the words whose labels best match its question. In the network, though, nothing is phrased in words: the "questions" and "labels" are learned vectors whose meaning the designers never specify. How well a question matches a label is measured by their **dot product**: multiply the two lists number by number and add up the results. The score is large when the two lists have large values in the same places. The same softmax function described in Section 3.3 then turns the scores into weights that add up to one.

The original paper visualised this process. In its trained translation model, two attention mechanisms in the fifth of six layers attended sharply from "its" to "Law" and "application" in the sentence above. The authors described this behaviour as "apparently involved in anaphora resolution", that is, working out what a pronoun refers to [@vaswani2017attention, Figure 4]. Such pictures are suggestive but need care: @jain2019attention found that attention weights often do not reliably explain why a model made a prediction.

Figure 3.2 shows how attention fits into the whole architecture. Each token's embedding is first combined with information about its position, since attention by itself does not know word order. The combined representation then passes through a stack of identical **transformer blocks**. Each block contains an attention step, where tokens exchange information, and a feed-forward step, where each token's representation is processed separately by an ordinary neural network of the kind described in Chapter 2. A block also has several attention mechanisms working in parallel, called **attention heads**, which can specialise in different relationships. GPT-3 has 96 blocks with 96 heads each, and the largest Llama 3 model has 126 blocks with 128 heads [@brown2020language; @grattafiori2024llama]. After the last block, a final layer converts the representation of the most recent token into a probability for each token in the vocabulary.

Position information has been supplied in different ways. Without it, "dog bites man" and "man bites dog" would look the same to attention. The original transformer added to each embedding a fixed pattern of sine and cosine waves that differs from one position to the next [@vaswani2017attention]. OpenAI's GPT-1 instead learned a separate position embedding for each slot, in the same way as token embeddings [@radford2018improving], and GPT-2 largely kept GPT-1's design. Many recent models, including Meta's Llama 3, use **rotary position embeddings** (RoPE) [@su2024roformer; @grattafiori2024llama]. RoPE adds nothing to the embedding. Inside the attention step it rotates each question and label vector by an angle that depends on the token's position, so that a match score also reflects how far apart two tokens are.

![Figure 3.2: A GPT-style transformer, simplified. Tokens become embeddings plus position information, then pass through many identical blocks, each with an attention step (tokens exchange information) and a feed-forward step (each token is processed on its own). The final layer gives a probability for every possible next token; the bars show GPT-2 XL's four most likely next tokens after "The cat sat on the". Inset: attention from "its" to "Law" in a trained translation model. Diagram by the author, after @vaswani2017attention; probabilities computed by the author with GPT-2 XL [@radford2019language].](../figures/svg/fig-03-02.svg){#fig:03-02}

The original transformer had two halves: an encoder that read a sentence in one language and a decoder that wrote its translation. GPT models keep only the decoder, which is why they are called "decoder-only" [@radford2018improving]. In a decoder, attention is **masked** so that each token can look only at itself and the tokens before it, never at later ones. This matches the training task: when predicting the next token, the model must not be allowed to peek at the answer. Because attention has no step-by-step chain, all positions in a training passage can be processed at once on parallel hardware such as the graphics processors described in Chapter 2. The original base model trained in 12 hours on eight GPUs [@vaswani2017attention], and that parallelism is what later made training on trillions of tokens feasible.

**Context windows.** The maximum number of tokens a model can attend to at once is its **context window**, which works like its short-term working memory. Anything outside the window is invisible to the model unless it is fed back in. GPT-3's window was 2,048 tokens [@brown2020language], about three pages of text. The largest Llama 3 model accepts up to 128,000 tokens [@grattafiori2024llama]. Google reported that Gemini 1.5 retrieved planted facts with over 99 per cent accuracy in research tests up to at least 10 million tokens [@geminiteam2024gemini]. The window is limited partly because standard attention compares every token with every other one, so its cost grows with the square of the length [@vaswani2017attention, Table 1]: doubling the text quadruples that work. A bigger window is also not the same as perfect use of it. @liu2024lost found that models often answered best when the relevant information sat at the beginning or end of a long input and noticeably worse when it was buried in the middle.

::: {.box .deeper}
**Going deeper: Attention and temperature as formulas**

For each token, the network computes three vectors by multiplying its current representation by learned weight matrices: a query *q*, a key *k* and a value *v*. Attention then gives the current token a score for itself and for every earlier token *j*. The score is the dot product *q* · *k*~*j*~, divided by √*d* (where *d* is the length of the vectors) to keep the numbers in a manageable range. In words, a score is high when the current token's question matches the other token's label.

The scores are turned into weights between 0 and 1 that sum to 1 using the softmax function, *w*~*j*~ = e^*s*~*j*~^ / Σ~*i*~ e^*s*~*i*~^, and the output is the weighted sum Σ~*j*~ *w*~*j*~ *v*~*j*~ of the values. Written for all tokens at once this is softmax(*QK*^T^ / √*d*) *V* [@vaswani2017attention]. Masking simply sets the scores for future tokens to minus infinity, so their weights become zero.

The same softmax produces the final next-token probabilities from raw scores *z* (called logits). Temperature *T* divides the logits before the softmax: *p*~*i*~ = e^*z*~*i*~/*T*^ / Σ~*k*~ e^*z*~*k*~/*T*^. With *T* < 1 the differences between scores are magnified and the top token gains; with *T* > 1 they shrink and the distribution flattens. Training minimises the cross-entropy loss, −log *p*~true~, which is zero only when the model assigns probability 1 to the token that actually occurred.
:::

## 3.5 From text predictor to assistant: pre-training and post-training

Building a modern chatbot happens in stages, summarised in Figure 3.3. The first and, for most models, by far the most expensive stage is **pre-training**: next-token prediction on an enormous body of text. Its scale has grown quickly, for reasons that Chapter 4 examines along with whether usable text is running out. GPT-1 in 2018 was trained on BooksCorpus, over 7,000 unpublished books [@radford2018improving]. GPT-2 used WebText, about 40 GB of text from some 8 million web pages linked from Reddit [@radford2019language]. GPT-3 was trained on 300 billion tokens drawn largely from a filtered version of Common Crawl, a public archive of the web, alongside books and Wikipedia [@brown2020language]. Meta's largest Llama 3 model, released in 2024, was pre-trained on about 15 trillion tokens [@grattafiori2024llama].

Model size has grown alongside the data, but "number of parameters" has become a less straightforward measure. Some recent models use a **mixture-of-experts** design, in which each transformer block contains many alternative feed-forward networks ("experts") and a small routing network sends each token to only a few of them. DeepSeek-V3, for example, has 671 billion parameters in total, but only 37 billion are used for any single token, and it was pre-trained on 14.8 trillion tokens, according to the company's technical report [@deepseekai2024deepseekv3]. The design lets a model store more knowledge without a matching increase in the computation needed per token. When comparing models, it therefore helps to ask both how many parameters exist and how many are active.

![Figure 3.3: How a typical chat model is trained. Pre-training on web-scale text produces a base model that continues text. Training on written examples of good answers (instruction tuning) teaches it to follow instructions. Training on rankings of answers by people or by another AI (preference training) shapes its style and safety. Reasoning models add a further stage of reinforcement learning on problems whose answers can be checked automatically; in recent models this stage can use a substantial share of the training computation. Diagram by the author, based on @ouyang2022training, @bai2022constitutional and @guo2025deepseek.](../figures/svg/fig-03-03.svg){#fig:03-03}

The result of pre-training is a **base model** like those in Table 3.3. It has absorbed a great deal but behaves like an autocomplete system. Asked a question, it may answer, or it may continue with five more questions in the style of an exam paper. The second stage, **post-training**, adapts it to a role. The model's weights are adjusted further, traditionally on far less data, chosen mainly to teach behaviour.

**Instruction tuning.** The simplest step is **supervised fine-tuning** on examples of instructions paired with good responses, a process often called instruction tuning. @wei2021finetuned showed that fine-tuning a 137-billion-parameter model on more than 60 tasks phrased as natural-language instructions substantially improved its performance on new kinds of tasks that it had not been tuned on. The model learns the general habit of reading an instruction and doing what it says, beyond the particular examples it was shown.

**Reinforcement learning.** Several of the methods that follow rely on a different way of learning from the supervised learning of Chapter 2. In supervised learning, every training example comes with the correct answer. In **reinforcement learning**, the system instead tries something and receives only a score, called a **reward**, saying how good the result was; its weights are then adjusted to make high-scoring behaviour more likely. Chapter 2's AlphaGo learned partly in this way from games against itself, with winning as the reward. For a language model, the attempt is a whole answer and the reward is a number judging it.

**Reinforcement learning from human feedback (RLHF).** Demonstrations are expensive to write, and many qualities of a good answer are easier to recognise than to produce. RLHF exploits this. The idea of learning from human comparisons was developed by @christiano2017deep for training agents in games and simulated robots, and @ouyang2022training applied it to GPT-3 to create InstructGPT, a forerunner of ChatGPT-style assistants. Their method had three steps. Human labellers wrote demonstrations used for supervised fine-tuning. They then ranked several model outputs for the same prompt from best to worst. These rankings trained a separate **reward model** that predicts which answers people prefer, and reinforcement learning then adjusted the language model to produce answers the reward model scores highly. The effect was large: in the authors' human evaluations, outputs from the 1.3-billion-parameter InstructGPT were preferred to outputs from the 175-billion-parameter GPT-3, despite the model being over 100 times smaller. Some later systems use simpler alternatives. **Direct preference optimisation** (DPO), for example, learns from the same kind of preference pairs without training a separate reward model or running reinforcement learning [@rafailov2023direct].

**Constitutional AI and AI feedback.** Human feedback is slow, costly and inconsistent, and labellers may be exposed to disturbing content. In a preprint, @bai2022constitutional at Anthropic proposed **Constitutional AI**, in which, for training the model to avoid harmful outputs, humans supply only a short list of written principles, the "constitution", in place of human harmlessness labels. In a supervised phase, the model drafts responses, critiques them against the principles and revises them, and is then fine-tuned on the revisions. In a reinforcement-learning phase, the model compares pairs of its own responses, and these AI judgements train the preference model. The authors called this **reinforcement learning from AI feedback** (RLAIF). They reported an assistant that was less harmful without being evasive, engaging with problematic requests by explaining its objections.

Post-training of this kind is powerful but shallow in one sense. It is generally thought to change mainly which of the base model's existing capabilities are expressed, and in what style, rather than to add much new knowledge. The reasoning models of 2025 and 2026 (Section 3.7) qualify this picture. Epoch AI, an independent research institute, estimated in May 2025 that the reinforcement-learning stage of DeepSeek-R1 cost about a fifth as much as pre-training its base model. It also reported OpenAI's statement that o3 used ten times the training compute of o1, most likely in this stage [@you2025how]. For such models post-training is no longer a small add-on, and the score gains described there suggest it can add skills as well as style. Post-training also introduces its own problems. A model rewarded for answers that people like can learn to flatter users or to sound confident. Chapter 12 examines these limits of RLHF, including sycophancy and reward hacking.

## 3.6 Why language models hallucinate, and what retrieval changes

LLMs sometimes produce fluent statements that are false: invented quotations, non-existent references, wrong dates. The research literature calls this **hallucination**. @ji2023survey distinguish "intrinsic" hallucinations, which contradict a source the model was given, from "extrinsic" hallucinations, which cannot be verified from that source at all. The term is a loose metaphor. The model does not perceive anything, and the errors are produced by the same mechanism that produces correct answers.

::: {.box .case}
**Case study: Mata v. Avianca (2023)**

In a lawsuit against the airline Avianca in a US federal court in New York, lawyers filed a court submission in March 2023 citing court decisions that did not exist. In his opinion on sanctions, Judge P. Kevin Castel found that the lawyers had "submitted non-existent judicial opinions with fake quotes and citations created by the artificial intelligence tool ChatGPT" and had continued to stand by them after the court questioned their existence [@sdny2023mata, p. 1]. One lawyer testified that he had "falsely assumed" ChatGPT was "like a super search engine" (p. 15). When he asked the chatbot whether a case was real, it replied that it had supplied "real" authorities findable in standard legal databases (p. 19). The court imposed a $5,000 penalty on the two lawyers and their firm (pp. 33–34). The case illustrates the core problem: a language model's confidence and fluency are not evidence that a claim is true, and asking the model to check itself is not an independent check.
:::

Why does this happen? Section 3.3 gives the first part of the answer. A model generates text that is probable given its training, and a plausible-looking citation has the right form whether or not it exists. @kalai2025why, in a preprint by researchers at OpenAI and Georgia Tech, give a statistical account. During pre-training, a model cannot reliably learn facts that appear rarely in its data. Birthdays follow no pattern that could be inferred from other facts, so a birthday seen only once gives the model little more to go on than one it has never seen. Using an estimate that goes back to Alan Turing, the authors treat the share of facts seen exactly once as a measure of how much the model has in effect not learned. If, say, 20 per cent of people's birthdays appear exactly once in the training text, a base model should be expected to hallucinate on at least about 20 per cent of questions about birthdays. The authors then argue that post-training and evaluation keep the problem alive. Most benchmarks award a point for a correct answer and nothing for "I don't know". A model that guesses therefore scores better than one that admits uncertainty, much as a student does on a multiple-choice exam without negative marking. Their proposed remedy is to change how evaluations are scored, rewarding expressed uncertainty instead of penalising it.

**Retrieval-augmented generation (RAG).** If hallucination arises partly because facts are stored imperfectly in the model's weights, one remedy is to supply the facts at the moment of answering. @lewis2020retrieval combined a language model with a searchable index of Wikipedia. Before answering, a retriever finds relevant passages, and these are placed in the model's context window alongside the question. The authors reported that such models generated "more specific, diverse and factual language" than a model relying on its weights alone. Today the same pattern sits behind chatbots that search the web, company assistants that consult internal documents, and tools that cite their sources. RAG also lets a system use information newer than its training data. A model's built-in knowledge stops at the point when its pre-training data was collected, so without retrieval it cannot know about later events, and it may not know that it does not know.

Retrieval reduces errors but does not remove them. The model may retrieve the wrong documents, misread the right ones, or blend retrieved text with its own guesses. In a preregistered study, @magesh2025hallucination tested legal research tools from LexisNexis and Thomson Reuters that were marketed with claims such as "hallucination-free". The tools hallucinated less than the general-purpose GPT-4, but each hallucinated between 17 and 33 per cent of the time on the authors' set of legal queries. Long retrieved contexts also run into the "lost in the middle" problem described in Section 3.4.

For users, an LLM's answer is most trustworthy where the relevant facts are common in its training data or supplied in its context. It is least trustworthy for rare specifics: exact figures, quotations, names of minor people, references and recent events. Checks that are independent of the model, such as opening a cited source or searching a database directly, catch errors that a second question to the same model may not, as the Avianca case shows. Requests can also be framed to reduce risk, for instance by supplying the source document and asking the model to answer only from it. Hallucination as a source of wider social risk is treated in Chapter 11.

## 3.7 Reasoning models, multimodality and what remains unknown

**Reasoning models.** Next-token prediction implies that a model spends roughly the same amount of computation on each token. A hard question answered in one word gets little "thinking". Researchers found early that models answered multi-step problems better when they wrote out intermediate steps first. @wei2022chain showed that giving a large model a few worked examples with step-by-step reasoning, a technique called **chain-of-thought prompting**, markedly improved its performance on arithmetic word problems.

Reasoning models make this behaviour a trained skill. According to the company's system card, OpenAI's o1 series, released in late 2024, is "trained with large-scale reinforcement learning to reason using chain of thought", producing a long internal chain of reasoning before answering [@openai2024o1, p. 1]. DeepSeek, a Chinese company, published a detailed recipe, which appeared in peer-reviewed form in *Nature* in September 2025 [@guo2025deepseek]. For an experimental model called DeepSeek-R1-Zero, it started from its pre-trained base model, skipped supervised fine-tuning and applied reinforcement learning with simple rule-based rewards. An answer to a mathematics problem earned a reward only if it matched the known correct result, with a further reward for using the required format. Progress was measured on AIME 2024, the American Invitational Mathematics Examination, a US competition in which every answer is a single number that can be checked automatically. During training, R1-Zero's average accuracy rose from 15.6 to 77.9 per cent. Its answers also grew steadily longer, and it began to check and revise its own work, at one point writing "Wait, wait. Wait. That's an aha moment I can flag here." (These are the developers' own measurements, from the *Nature* version; the January 2025 preprint reported a rise to 71.0 per cent. The released DeepSeek-R1, which added supervised fine-tuning stages, scored 79.8 per cent, close to the authors' own measurement for OpenAI's o1.)

This shift means that capability can now be bought at answer time as well as at training time: letting a model think longer, or sampling several answers and choosing among them, raises accuracy on hard problems. Chapter 4 discusses this **test-time compute** as a new scaling trend. Reinforcement learning works best where answers can be checked automatically, as in mathematics and programming, and less well for essays or advice. The written reasoning is also not necessarily a faithful record of how the model reached its answer, which matters for the safety monitoring discussed in Chapter 12. Anthropic researchers slipped hints into questions and checked whether reasoning models that used a hint said so. The models mentioned the hint only a minority of the time: 25 per cent on average for Anthropic's Claude 3.7 Sonnet and 39 per cent for DeepSeek-R1, according to their preprint [@chen2025reasoning].

**Multimodal models.** The transformer is not limited to words. @dosovitskiy2021image showed that an image can be cut into small square patches, each turned into a vector and processed like a token. @radford2021learning trained a model called CLIP on 400 million image–caption pairs from the internet to match pictures with their descriptions, linking images and language in a shared embedding space. Current systems combine these ideas, so that text, images, audio and video can all enter the same context window. Google reported that Gemini 1.5 could reason over hours of video and audio [@geminiteam2024gemini], and Meta described adding image, video and speech capabilities to Llama 3 by attaching separately trained components to the language model [@grattafiori2024llama].

**Open and closed weights.** A model's weights are the billions of numbers learned in training. Some developers publish them so that anyone can download, run and modify the model; these are **open-weight models**. Meta released the weights of its 405-billion-parameter Llama 3 model [@grattafiori2024llama], and DeepSeek released R1 under the permissive MIT licence [@guo2025deepseek]. Others offer **closed-weight** models only through an app or a paid interface, keeping the weights private. The line is not always between companies: Alibaba's Qwen2.5 family includes both downloadable models, such as the one in Table 3.3, and proprietary versions available only as a hosted service [@qwen2024qwen25]. The benefits and risks of openness, and the "DeepSeek moment" of January 2025, are the subject of Chapter 7.

**What we do and do not understand.** Engineers know exactly what computations an LLM performs, since they wrote the code. What they do not fully know is what the learned weights represent, or why a particular answer comes out. The field of **interpretability**, covered in Chapter 12, tries to open this black box. In a 2025 study of their own Claude 3.5 Haiku model, not peer-reviewed, Anthropic researchers used a method that traces which internal features influence an output. They reported that the model appeared to plan ahead when writing rhyming verse: "Before beginning to write each line, the model identifies potential rhyming words that could appear at the end" [@lindsey2025biology]. In the same study, asked for the capital of the state containing Dallas, the model seemed to represent "Texas" internally as an intermediate step before answering "Austin". Findings like these suggest that next-token prediction can involve more structure than the phrase implies, but the methods so far explain only parts of a model's behaviour.

::: {.box .debate}
**Debate: Do large language models understand language?**

Researchers are divided, and the disagreement partly concerns what "understand" should mean. A 2022 survey of natural-language-processing researchers [@michael2023what], also discussed by @mitchell2023debate, asked whether some model trained only on text, given enough data and computing power, could understand natural language "in some non-trivial sense". Of the 327 active researchers whose answers the survey authors analysed (out of 480 people who completed it), 51 per cent agreed and 49 per cent disagreed.

One side holds that learning from text alone cannot produce meaning. @bender2020climbing argue that "a system trained only on form has a priori no way to learn meaning". Their thought experiment imagines a hyper-intelligent octopus tapping an undersea telegraph cable between two people: it could learn to imitate their messages convincingly yet would have no idea what the words refer to. On this view, fluent output reflects statistical patterns in human writing, and hallucinations are exactly what one would expect.

The other side points to evidence that models build internal representations of the situations their text describes. @li2023emergent trained a GPT-style model only on sequences of moves in the board game Othello, never showing it the board. They nevertheless found an internal representation of the board state, and changing that representation changed the model's predicted moves. Interpretability work such as @lindsey2025biology reports intermediate steps and planning inside commercial models.

Resolving the dispute may first require splitting it. @mitchell2023debate argue for a new science of intelligence that would distinguish different modes of understanding, each with its own strengths and limitations, so that "understanding" becomes several narrower questions. Experiments that intervene on a model's internal representations and predict how its behaviour changes are one of the more promising sources of such evidence.
:::

## Summary

- Language models split text into tokens using methods such as byte-pair encoding; tokenisation explains odd weaknesses (spelling, letter counting) and makes some languages costlier to process than others.
- Each token becomes an embedding, a learned point in a high-dimensional space; inside a transformer these representations are continually updated by context.
- An LLM is trained by self-supervised next-token prediction; at generation time, decoding settings such as temperature and nucleus sampling decide how adventurous the output is.
- Attention lets every token draw information from itself and every earlier token; position information is added to embeddings or, in many recent models, built into attention (RoPE); transformers stack many attention and feed-forward blocks, and their context window is limited partly because attention's cost grows with the square of the input length.
- Pre-training on trillions of tokens produces a base model; post-training (instruction tuning, RLHF, DPO, Constitutional AI) turns it into an assistant and traditionally changes behaviour more than knowledge, though the reinforcement-learning stage of reasoning models now takes a substantial share of computation.
- Hallucinations follow from how models are trained and evaluated; retrieval-augmented generation reduces them but, as legal-tool studies show, does not eliminate them.
- Reasoning models, trained with reinforcement learning on checkable problems, trade extra computation at answer time for accuracy, but their written reasoning is not always a faithful account of their process.
- Engineers understand the computations of an LLM but not fully what the learned weights represent, and whether models "understand" language remains an open debate.

## Key terms

token · embedding · next-token prediction · self-supervised learning · temperature · attention · transformer · context window · pre-training · instruction tuning · reinforcement learning from human feedback (RLHF) · Constitutional AI · hallucination · retrieval-augmented generation (RAG) · reasoning model

## Discussion questions

1. Using Tables 3.1 and 3.2 and the findings of @petrov2023language, explain how tokenisation could disadvantage speakers of some languages. What does the difference between the GPT-2 and `o200k_base` columns of Table 3.2 suggest about how far the problem can be reduced by engineering, and what evidence would you need to be sure?
2. Table 3.3 shows that every base model gives "Paris" well under half of the probability. Does this show that the models do not "know" the capital of France? Use the other continuations in the table and Section 3.5 to argue your answer.
3. Evaluate the evidence: @magesh2025hallucination found legal research tools hallucinating in 17–33 per cent of their test queries. What do the sample, the setting and the vendors' marketing claims tell you about how far this result generalises to other retrieval-based tools?
4. Apply the ideas of this chapter to a new case: a university wants a chatbot that answers student questions about its regulations. Which techniques from Sections 3.5 and 3.6 would you use, and which errors would you still expect?
5. @kalai2025why argue that benchmarks which give no credit for "I don't know" encourage hallucination. Design a scoring rule that would reward honest uncertainty, and discuss what problems it might create.
6. Does the Othello result of @li2023emergent answer the octopus argument of @bender2020climbing? Make the strongest case for each side.

## Further reading

- Vaswani, A. et al. (2017). *Attention Is All You Need*. The original transformer paper; Sections 3.2 and 3.5 and the attention visualisations in the appendix are readable with this chapter's background. [@vaswani2017attention]
- Ouyang, L. et al. (2022). *Training Language Models to Follow Instructions with Human Feedback*. The clearest primary account of how a base model became a ChatGPT-style assistant. [@ouyang2022training]
- Bai, Y. et al. (2022). *Constitutional AI: Harmlessness from AI Feedback*. Shows how written principles and AI feedback can partly replace human labelling. [@bai2022constitutional]
- Kalai, A. T. et al. (2025). *Why Language Models Hallucinate*. A short, accessible statistical argument about why confident errors arise and persist. [@kalai2025why]
- Mitchell, M. and Krakauer, D. C. (2023). *The Debate over Understanding in AI's Large Language Models*. A balanced overview of the arguments for and against machine understanding. [@mitchell2023debate]


# Chapter 4: Scaling, Compute and the Limits of Progress

::: {.objectives}
**After working through this chapter you should be able to:**

- explain what a scaling law is and why the relationship between compute, model size, data and performance shaped AI development after 2020;
- compare the Kaplan and Chinchilla accounts of how a fixed compute budget should be divided between model size and training data;
- evaluate evidence on the main constraints on further scaling, including data, synthetic data, cost and energy;
- distinguish training-time from test-time compute, and algorithmic efficiency from falling inference prices;
- assess the strengths and weaknesses of benchmarks and of METR's task time-horizon metric as measures of progress.
:::

In 2012, the image classifier AlexNet was trained on two consumer graphics cards for "five to six days" [@krizhevsky2012imagenet, p. 7]. Epoch AI, a research institute that tracks the resources used to train AI systems, estimates that this training run used about 4.7 × 10^17 arithmetic operations [@epochai2026data]. Twelve years later, Meta trained its largest Llama 3 language model on up to 16,000 data-centre chips, using 3.8 × 10^25 operations, according to the company's technical report [@grattafiori2024llama]. That is roughly 80 million times more computation than AlexNet needed.

This growth was a deliberate strategy, guided by empirical regularities known as scaling laws. Those regularities gave AI developers a reason to believe that larger training runs would buy predictably better models. This chapter explains what scaling laws say, how far the trends in compute, cost and efficiency have gone, and which limits could slow them. It ends with the difficult question of how progress should be measured at all. Chapter 7 covers the chips, data centres and energy behind these numbers; here the focus is on the logic of scaling and its evidence.

## 4.1 What "scaling" means

Three ingredients determine how large a training run is. The first is the number of **parameters**, the adjustable numbers inside a neural network that are tuned during training (Chapter 2). The second is the amount of **training data**, which for language models is counted in tokens, the word fragments introduced in Chapter 3. The third is **training compute**, the total number of arithmetic operations performed during training. Compute is measured in FLOP (floating-point operations): one FLOP is a single addition or multiplication of two floating-point numbers, the format computers use to store values with a fractional part, much like scientific notation.

The three ingredients are linked. Kaplan and colleagues, in a 2020 preprint, estimated that training a language model costs about six operations per parameter for every token processed [@kaplan2020scaling]. A model with more parameters, or one that reads more tokens, therefore needs proportionally more compute. Meta's report for Llama 3 shows the rule at work: 405 billion parameters trained on 15.6 trillion tokens gives about 3.8 × 10^25 FLOP, the figure the company reports [@grattafiori2024llama].

Why would anyone expect sheer size to help? The computer scientist Richard Sutton gave an influential answer in a short 2019 essay. Looking back over decades of research, he argued that "general methods that leverage computation are ultimately the most effective, and by a large margin" [@sutton2019bitter]. In chess, speech recognition and computer vision, he observed, hand-built knowledge was repeatedly overtaken by simpler methods that could use more computing power. Sutton called this "the bitter lesson", because it meant that researchers' carefully encoded insights often mattered less than they had hoped.

Sutton's essay was an argument from history. Kaplan and colleagues at OpenAI turned a similar idea into a measurement. They trained many language models of different sizes, on different amounts of data and with different compute budgets, and recorded each model's test loss [@kaplan2020scaling]. Loss is the model's average error at predicting the next token on text it has not seen; lower is better. They found that loss fell along smooth curves as each ingredient grew, with some trends holding over "more than seven orders of magnitude", that is, over a ten-million-fold range of scale.

::: {.box .concept}
**Key concept: Scaling law**

A scaling law is an empirical rule that describes how a model's performance changes as the resources used to train it grow. In language models, the classic finding is that test loss falls as a power law of compute, parameters or data: each tenfold increase in resources removes a roughly constant fraction of the remaining error. A useful comparison is measuring something ever more precisely: each extra decimal place of accuracy costs about as much effort as all the previous ones together, yet the cost of the next one can be predicted. Unlike laws of nature, scaling laws are observations, and they describe loss, not the specific skills people care about.
:::

The shape of these curves is easiest to see on a particular kind of graph. Figure 4.1 is a schematic of a scaling curve drawn on logarithmic axes, where each step along an axis represents a tenfold increase. On such a plot, a power law appears as a straight line sloping downwards. The figure also shows the feature that makes scaling laws useful for planning: researchers can fit the line using small, cheap training runs and then extend it to predict the result of a much larger one.

![Figure 4.1: Schematic of a scaling law. On logarithmic axes, test loss falls along an approximately straight line as training compute grows. Small, cheap runs (filled dots) are used to fit the line, which is then extended to predict the loss of a planned large run (hollow dot). The curve flattens towards an irreducible loss that more compute cannot remove. Schematic, not to scale. Diagram by the author.](../figures/svg/fig-04-01.svg){#fig:04-01}

These predictions have been used in practice. OpenAI's GPT-4 technical report states that the final loss of GPT-4 was predicted "with high accuracy" from models trained with "at most 10,000x less compute" [@openai2023gpt4, p. 2]. The same report notes that performance on individual problems "may occasionally worsen with scale", a reminder that smooth averages can hide irregular behaviour on single tasks.

::: {.box .deeper}
**Going deeper: Power laws and the compute formula**

A power law has the form *L = a × C^(−b) + c*. In words, the loss *L* equals a constant *a* multiplied by compute *C* raised to a small negative power *−b*, plus a floor *c*. Because the exponent is negative, each increase in compute reduces the loss, but by less and less. The floor *c* is the "irreducible loss": the part of the error that remains even with unlimited compute, partly because natural language is inherently unpredictable. GPT-4's developers fitted a curve of exactly this form to small models to forecast the large one [@openai2023gpt4].

The compute formula *C ≈ 6 × N × D* says that training compute *C* is about six times the number of parameters *N* times the number of training tokens *D* [@kaplan2020scaling]. The "six" counts the multiplications and additions needed for one pass forward through the network and the roughly twice as costly backward pass of backpropagation (Chapter 2).
:::

## 4.2 How to spend a compute budget: from Kaplan to Chinchilla

A scaling law raises a practical question. If a developer has a fixed compute budget, should it build a bigger model and train it on fewer tokens, or a smaller model trained on more tokens? The compute formula means the two choices trade off directly: doubling the parameters while keeping compute constant halves the number of tokens the model can read.

Kaplan and colleagues concluded that larger models learn more from each token they see. They therefore recommended training "very large models on a relatively modest amount of data" and stopping well before the models had fully converged [@kaplan2020scaling]. This advice is visible in the models of the following two years. GPT-3, released in 2020, had 175 billion parameters, and Hoffmann and colleagues later observed that developers had kept increasing model size while keeping the amount of training data roughly constant [@hoffmann2022empirical].

In 2022, a DeepMind team, with Jordan Hoffmann as first author, revisited the question. They trained more than 400 language models, ranging from 70 million to over 16 billion parameters, on between 5 and 500 billion tokens [@hoffmann2022empirical]. Their conclusion was different: for compute-optimal training, model size and training data should grow in equal proportion, so that "for every doubling of model size the number of training tokens should also be doubled". By this standard, the large models of the day were, in the authors' words, "significantly undertrained".

The team tested the claim directly. They trained Chinchilla, a model with 70 billion parameters, using about the same compute as their earlier 280-billion-parameter model Gopher, but on four times as much data: 1.4 trillion tokens [@hoffmann2022empirical]. Epoch AI's estimates confirm that the two runs used similar compute, about 5.8 × 10^23 and 6.3 × 10^23 FLOP respectively [@epochai2026data]. Chinchilla outperformed Gopher, GPT-3 and several other larger models across a wide range of tasks, and reached 67.5% average accuracy on the MMLU knowledge test, which the authors describe as an improvement of more than 7% over Gopher. Because Chinchilla was smaller, it was also cheaper to run after training.

The Chinchilla result is often summarised as a rule of thumb of about 20 training tokens per parameter, which is simply Chinchilla's own ratio (1.4 trillion divided by 70 billion). The rule is a guide to minimising training cost, not a law. Developers who expect a model to answer billions of queries may deliberately "over-train" a smaller model on more data than the rule suggests, because a smaller model is cheaper every time it is used. Meta's Llama 3 family shows both choices. The flagship model read about 38 tokens per parameter (15.6 trillion tokens for 405 billion parameters), close to what Meta's own scaling analysis recommended, so the company describes it as approximately compute-optimal (see the case study below). The 8-billion-parameter model, like its larger siblings, was pre-trained on a corpus of about 15 trillion tokens: roughly 1,900 tokens per parameter. Meta says it trained its smaller models "for much longer than is compute-optimal" because they then perform better at the same cost of use [@grattafiori2024llama].

The Chinchilla result also sharpened a problem that Section 4.4 takes up. Under Kaplan's recommendations, more compute could be absorbed mainly by larger models. Under Chinchilla's, every increase in compute calls for a matching increase in training data. A developer who multiplies its compute budget by 100 should, by this rule, use about ten times as many parameters and ten times as many tokens. Scaling thus became as much a question of finding text as of buying chips.

::: {.box .case}
**Case study: Sizing Llama 3 with a scaling law**

Meta's 2024 technical report for its Llama 3 models describes how the company chose the size of its largest model [@grattafiori2024llama, p. 8]. The team first trained many small models with compute budgets between 6 × 10^18 and 10^22 FLOP. For each budget, it found the combination of model size and data that gave the lowest loss. It then fitted a power law relating compute to the best number of training tokens and extended it to its planned budget of 3.8 × 10^25 FLOP. The extrapolation suggested a model of 402 billion parameters trained on 16.55 trillion tokens, about 41 tokens per parameter and so a higher ratio than Chinchilla's 20. Because the curves were found to be fairly flat near their minimum, the team settled on 405 billion parameters and 15.6 trillion tokens. The report also used the same small models to forecast performance on downstream benchmarks before the large run. The case shows scaling laws working as an engineering tool: a way to plan an expensive experiment, with the risk shifted onto cheaper ones.
:::

## 4.3 Compute and cost: the trends

How fast has training compute actually grown? Sevilla and colleagues assembled estimates for 123 milestone machine-learning systems and identified three eras [@sevilla2022compute]. Before about 2010, the compute used to train notable systems doubled roughly every 20 months, in line with Moore's law, the long-running doubling of the number of transistors on a chip. In the deep-learning era that began in the early 2010s, the doubling time shortened to about six months. From late 2015, a "large-scale era" appeared, in which companies trained models needing 10 to 100 times more compute than the typical system of their time.

Figure 4.2 plots Epoch AI's estimates for a selection of well-known systems, from the Perceptron Mark I of 1957 to models released in 2025. Because the vertical axis is logarithmic, each gridline marks a tenfold increase, and the total span is about twenty orders of magnitude. GPT-3, trained in 2020, used an estimated 3.1 × 10^23 FLOP. Epoch estimates that GPT-4.5, released in February 2025, used about 3.8 × 10^26 FLOP, roughly 1,200 times more [@epochai2026data].

![Figure 4.2: Estimated training compute of selected notable AI systems, 1957–2025, on a logarithmic scale. Each gridline is a tenfold increase. Values are Epoch AI estimates; those marked "likely" are expected to be accurate within a factor of 10, and the others within a factor of 3. Source: @epochai2026data.](../figures/svg/fig-04-02.svg){#fig:04-02}

Over recent years the pace has stayed about as fast as in Sevilla's deep-learning era. As of February 2026, Epoch reports that the training compute of frontier language models has grown about five-fold per year since 2020, doubling roughly every five months. Compute for the top five models has grown about 10,000-fold over the same period. Epoch attributes this growth to three sources: using more chips in parallel, training for longer, and using more powerful and cost-effective processors [@epochai2026trends]. Only the last of these comes from better hardware; the first two come from spending more. The total stock of AI computing capacity is growing more slowly. The 2026 AI Index reports that global AI compute capacity grew 3.3 times per year from 2022, reaching the equivalent of 17.1 million of Nvidia's H100 chips [@sajadieh2026ai].

These figures are increasingly estimates rather than reported facts. The AI Index notes that training code, parameter counts, dataset sizes and training duration are no longer disclosed for several of the most resource-intensive systems, including those from OpenAI, Anthropic and Google. Training compute, which can be estimated independently, has continued to rise [@sajadieh2026ai]. Where developers do not report compute, Epoch estimates it from details such as the model's architecture and training data, or the training hardware and its running time, and labels each estimate by confidence. Its "confident" estimates are expected to be accurate within a factor of 3, "likely" ones within a factor of 10, and "speculative" ones within a factor of 30 [@epochai2026data]. The GPT-4 estimate in Figure 4.2, for instance, is labelled "likely", with a 90% interval running from about 8 × 10^24 to 4 × 10^25 FLOP.

More compute costs more money, although cheaper hardware offsets part of the increase. Epoch estimates that chip performance per dollar has improved about 1.5 times per year since 2023 [@epochai2026trends]. Even so, Cottier and colleagues found, in a preprint, that the cost of training the most compute-intensive models, with hardware costs spread over their useful life, grew about 2.4 times per year from 2016 onwards. Epoch's more recent estimate for frontier language models since 2020 is about 3.5 times per year. If the earlier trend continued, Cottier and colleagues projected, the largest training runs would cost "more than a billion dollars by 2027" [@cottier2024rising]. The chips, energy and investment behind these sums are the subject of Chapter 7.

## 4.4 Running out of data?

Compute can be bought, at a price. High-quality human writing is harder to expand. If training compute grows about five-fold a year and the best use of compute requires data to grow alongside model size, then the demand for training text grows rapidly too. The question is whether there is enough.

Villalobos and colleagues at Epoch AI estimated that the effective stock of public, human-generated text is about 320 trillion tokens, with a 95% confidence interval of 65 trillion to 1,700 trillion [@villalobos2024position]. Projecting the growth of training datasets, they concluded that if trends continued, models would be trained on datasets "roughly equal in size to the available stock of public human text data between 2026 and 2032", or slightly earlier if models were over-trained. For comparison, Llama 3 was trained on 15.6 trillion tokens [@grattafiori2024llama], about one-twentieth of the central estimate.

The estimate depends on assumptions that could change. Text can be reused for several passes of training, although repeated data becomes less useful. Private data, such as company documents or user conversations, lies outside the public estimate. Villalobos and colleagues themselves name three possible ways forward: synthetic data, transfer from data-rich domains, and more data-efficient training methods [@villalobos2024position]. Better curation also matters. The 2026 AI Index highlights the open model OLMo 3.1 Think 32B, which has nearly 90 times fewer parameters than xAI's Grok 4 yet achieves comparable results on several benchmarks. The report credits the pruning, deduplication and careful selection of its training data [@sajadieh2026ai]. Data were not the whole story, however. The developers' technical report, released as a preprint, describes three stages of post-training, ending with reinforcement learning, and reports gains from each. The 3.1 version was produced by extending the reinforcement-learning stage [@olmo2025olmo].

Images, video and audio add to the stock. A separate Epoch analysis, published in 2024, widened the estimate to include them. Counting such multimodal data, but excluding synthetic data, it put the effective stock at between 400 trillion and 20 quadrillion tokens, enough in principle for training runs far larger than any yet attempted [@sevilla2024can]. The width of that range shows how uncertain the data limit is.

Prominent researchers nevertheless treat data as a binding limit. In a November 2025 interview, Ilya Sutskever, a co-founder of OpenAI who later founded the company Safe Superintelligence, said that "the data is very clearly finite" and that pre-training will eventually run out [@patel2025ilya].

### Synthetic data and model collapse

An obvious response is **synthetic data**: text, images or code generated by AI models and used to train other models. Synthetic data is already common in post-training, for example when a strong model writes worked solutions that a smaller model learns from (Chapter 3). The open question is whether it can replace fresh human data in pre-training.

Shumailov and colleagues, writing in *Nature*, identified a risk they called **model collapse** [@shumailov2024ai]. They trained successive generations of models, each on data produced by the previous generation. Over the generations, the rare cases in the original data (the "tails" of the distribution) disappeared, and the models drifted towards a narrow, distorted picture of the world. They observed the effect in language models and in simpler statistical models, and argued that it is a general feature of learning from recursively generated data. One implication is that genuine human-generated data may become more valuable as AI-written text spreads across the web.

The finding depends on the training set-up. In the collapse experiments, each generation was trained mainly on the previous generation's output, which replaced rather than added to the original data. Gerstgrasser and colleagues, in a paper presented at the 2024 Conference on Language Modeling, argued that a more realistic assumption is that data accumulate: new synthetic text is added to the web alongside, not instead of, older human text [@gerstgrasser2024model]. In their experiments, accumulating synthetic data with the original real data avoided collapse, and in a simplified mathematical model the error stayed bounded however many generations were run.

The 2026 AI Index summarises the state of the evidence cautiously. There is "still no definitive evidence" that synthetic data can fully offset the depletion of real data in pre-training, although mixing real and synthetic data can speed up training, and purely synthetic training has worked for smaller models and narrow tasks [@sajadieh2026ai]. Synthetic data is therefore a partial answer to the data limit, and a tool that has to be used with care.

## 4.5 Doing more with less: efficiency and test-time compute

So far, progress has been described as a matter of spending more. Two other trends make each unit of spending go further. The first is **algorithmic efficiency**: improvements in model architectures, training methods and data that reach the same performance with less compute. The second is falling **inference** costs. Inference is the use of a trained model to produce answers, as opposed to training it.

Ho and colleagues measured algorithmic progress in language models using more than 200 evaluations on two standard text benchmarks between 2012 and 2023 [@ho2024algorithmic]. They estimated that the compute needed to reach a given level of performance "halved approximately every 8 months", with a wide 90% confidence interval of about 2 to 22 months. An earlier preprint version had reported a narrower 95% interval of 5 to 14 months. They estimated that the transformer architecture (Chapter 3) alone was worth about a sevenfold increase in compute, equivalent to nearly two years of algorithmic progress, although the uncertainty around this figure is large. Even so, they concluded that the growth of compute contributed more to overall progress than algorithmic improvements did over this period. A simple analogy is a car journey: a better engine (algorithms) and a bigger fuel tank (compute) both extend the distance travelled, and the study suggests the fuel tank grew faster. Better algorithms, however, can also open routes that no amount of fuel would reach.

The price of using AI models has fallen even faster. The 2025 AI Index, working with Epoch AI, tracked the cheapest model that matched GPT-3.5's score of 64.8 on the MMLU benchmark [@maslej2025ai]. The price fell from $20 per million tokens in November 2022 to $0.07 per million tokens in October 2024, achieved by Google's small Gemini-1.5-Flash-8B model: a more than 280-fold reduction in under two years. Depending on the task, Epoch estimated that prices for a fixed level of performance fell between 9 and 900 times per year. Cheaper answers do not necessarily mean lower total spending, because cheaper models invite more use. Epoch estimates that about 30% of OpenAI's compute spending in 2024 went on inference [@epochai2026trends].

### Test-time scaling

A newer form of scaling spends more compute at the moment of answering. In September 2024, OpenAI introduced its o1 model, which generates a long internal chain of reasoning before giving an answer (Chapter 3). According to the company, o1's performance "consistently improves" both with more reinforcement-learning training and "with more time spent thinking (test-time compute)" [@openai2024learning]. Its published charts showed accuracy on a mathematics competition rising smoothly as test-time compute increased.

::: {.box .concept}
**Key concept: Test-time compute**

Test-time compute is the computation a model uses while answering a question, as opposed to the compute used to train it. A model can use more of it by reasoning in longer chains, by generating several candidate answers and choosing the best, or by checking its own work. A rough analogy is a student who is allowed more time in an examination: the same knowledge, used more carefully, yields better answers on hard questions. The analogy breaks down because the extra "thinking" is paid for with every query, so its costs grow with use rather than being paid once.
:::

Snell and colleagues studied how to spend test-time compute efficiently on mathematical reasoning [@snell2025scaling]. Allocating it adaptively, according to how hard each question is, improved efficiency more than four-fold compared with simply sampling many answers and picking the best. In comparisons where total compute was held equal, a smaller model given extra test-time compute could outperform a model 14 times larger, but only on problems where the smaller model already had some chance of success. Test-time compute appears to amplify existing ability more than it creates new ability.

Test-time scaling changes the economics described in Section 4.3. Training is a one-off cost. Test-time compute is paid each time a question is asked, so the most capable answers can be the most expensive to produce. This is one reason why falling prices for a fixed level of performance can coexist with rising total spending on AI.

The same applies to energy. The 2026 AI Index reports estimates by Jegham and colleagues of the electricity used to answer a medium-length prompt of about 1,000 input and 1,000 output tokens [@sajadieh2026ai]. Among the 15 most energy-intensive models in 2025, two DeepSeek models used about 23 watt-hours per query and GPT-5 in its high-reasoning setting about 21.9 watt-hours, while Claude 4 Opus and GPT-5 mini (medium setting) sat between 5 and 6 watt-hours. These are outside estimates rather than company figures, but they show that the cost of an answer depends heavily on the model and on how long it is allowed to reason. Chapter 7 places these figures in the context of total data-centre electricity use.

## 4.6 Emergence: sudden leaps or smooth curves?

If loss falls smoothly with scale, do abilities also grow smoothly? In 2022, Wei and colleagues argued that some do not [@wei2022emergent]. They defined an ability as **emergent** "if it is not present in smaller models but is present in larger models". Their examples included a test of three-digit addition and subtraction and two-digit multiplication, on which GPT-3 performed close to zero across several orders of magnitude of training compute before jumping well above chance at about 2 × 10^22 FLOP (13 billion parameters). If such jumps are common, they argued, the abilities of larger models cannot be forecast by extrapolating from smaller ones.

Not every ability behaves this way. The GPT-4 report states that its developers predicted the model's pass rate on part of a programming benchmark from models trained with at most one-thousandth of its compute [@openai2023gpt4, p. 2]. Some capabilities, in other words, have proved predictable in advance, while others have appeared to arrive abruptly.

The idea matters well beyond academia. If dangerous capabilities could appear suddenly and without warning, safety testing of each new model would be essential, and predictions from smaller models would offer little reassurance. If abilities instead grow smoothly, scaling laws could be used to anticipate them.

::: {.box .debate}
**Debate: Are emergent abilities real or an artefact of measurement?**

*Emergence is real.* Wei and colleagues documented sharp jumps across several model families and tasks, including arithmetic, transliteration and unscrambling words [@wei2022emergent]. Du and colleagues later reported that such abilities appear when a model's pre-training loss falls below a particular threshold, which suggests that something genuine changes at a certain level of competence [@du2024understanding].

*Emergence is a mirage.* Schaeffer, Miranda and Koyejo argued that apparent jumps often arise from the way performance is scored [@schaeffer2023emergent]. Exact-match scoring gives credit only when every token of an answer is right, so steady improvement in the underlying predictions can look like a sudden leap. They found that more than 92% of the emergent abilities on the BIG-Bench test suite appeared under one of two all-or-nothing metrics. Switching to continuous metrics, such as how many tokens of an answer would have to be changed to make it correct, turned many jumps into smooth curves.

*How the question could be decided.* Both sides agree that the choice of metric matters. A useful test is whether a capability can be predicted in advance from smaller models using continuous measures, and whether jumps remain under those measures. For users, however, an all-or-nothing metric is sometimes the relevant one: an arithmetic answer that is nearly right is still wrong.
:::

## 4.7 Measuring progress: benchmarks and time horizons

Every claim in this chapter about "better" models relies on some way of measuring capability. The most common tool is the **benchmark**: a fixed set of test questions or tasks with known answers, on which models can be scored and compared. Benchmarks made rapid progress visible, but they suffer from three well-documented problems. Many of the figures below come from the 2026 AI Index, Stanford University's annual report on the state of the field [@sajadieh2026ai].

The first is **saturation**: once top models score close to the maximum, a benchmark can no longer tell them apart. GPQA Diamond is a set of graduate-level science questions designed to be hard to answer by web search. Expert human validators score 81.2% on it. In late 2024, OpenAI's o3 became the first model to exceed that level, with 87.7%, and in 2025 accuracy reached 93%. The AI Index concludes that evaluations "intended to be challenging for years are saturated in months" [@sajadieh2026ai].

Humanity's Last Exam was built to resist this. Its final version contains 2,500 expert-written questions across more than a hundred subjects, each with a single verifiable answer that cannot be quickly found online [@centerforaisafety2026benchmark]. Between 2024 and 2025 the best accuracy rose from under 10% to 38.3%, according to the AI Index [@sajadieh2026ai]. The climb has continued: on the leaderboard kept by Scale AI, which built the benchmark with the Center for AI Safety, the top score listed in October 2026 was 54.8% [@scale2026humanity].

The second problem is **contamination**: test questions, or close variants of them, may appear in a model's training data, so that a high score partly reflects memorisation. Zhang and colleagues tested this for GSM8K, a widely used set of school-level maths word problems [@zhang2024careful]. They wrote GSM1k, a new set of 1,205 problems of matching style and difficulty that had never been published, so could not have been in any training data. Several model families scored up to 8% lower on the new problems, a sign of overfitting to the original test, although many frontier models showed little sign of it. In 2025, the AI Index also notes, Meta faced criticism that a Llama 4 variant had been optimised for a public leaderboard and may have trained on benchmark data, claims the company disputed [@sajadieh2026ai].

The third problem is **validity**: whether a benchmark measures what it claims to measure. One review flagged problematic questions in nine widely used benchmarks, at rates from 2% on one part of MMLU to 42% on GSM8K [@sajadieh2026ai]. Strong benchmark scores also do not always translate into usefulness in real work, a gap that Chapter 8 examines through field experiments. Leaderboards based on human votes, which rank models by which answer users prefer, have their own weaknesses: one analysis suggests that a model's standing may partly reflect adaptation to the platform rather than general capability.

Progress is also uneven across tasks, a pattern often described as a "jagged frontier". Models now match or beat expert baselines on graduate-level science questions. Yet on ClockBench, a test of reading analogue clocks, humans answered correctly 90.1% of the time. The best model, GPT-5.4 in its high-reasoning setting, reached 50.6% in March 2026, according to the AI Index [@sajadieh2026ai]. A single benchmark score, however high, says little about performance on tasks it does not cover.

### The task time-horizon metric

One response to these problems is to measure capability in units that keep their meaning as models improve. Researchers at METR, a non-profit organisation that evaluates frontier AI systems, proposed measuring the length of tasks that AI agents can complete, where length means how long the task takes a skilled human [@kwa2025measuring]. The original suite contained 170 tasks, from short software actions that take a human between 1 and 30 seconds to research-engineering tasks rated at 8 hours. The researchers timed skilled human professionals on the tasks and tested AI agents (Chapter 5) on them. For each model, they fitted a curve relating the probability of success to the human completion time. A model's **50% time horizon** is the task length at which it is predicted to succeed half the time.

The metric's appeal is that it has no ceiling: a longer task can always be added. In the original March 2025 preprint (later published at the NeurIPS 2025 conference), Kwa and colleagues found that the time horizon of frontier models had been "doubling approximately every seven months since 2019", with Claude 3.7 Sonnet reaching about 50 minutes [@kwa2025measuring]. METR later expanded its task suite, re-measured models and published the results with confidence intervals as "Time Horizon 1.1" [@metr2026task]. On the expanded suite, Claude 3.7 Sonnet's estimate is about 60 minutes, which shows that the exact values depend on the task set. METR has also revised its estimates over time, for example after correcting an error in its curve-fitting method in March 2026, so figures quoted in different places for the same model can differ. All values below come from the Time Horizon 1.1 data file, last updated in September 2026.

Figure 4.3 plots METR's estimates for the models that set a new record when released. The horizon rose from about 3 seconds for GPT-2 (2019) to about 4 minutes for GPT-4 (2023), about 2 hours for o3 (April 2025) and about 12 hours for Claude Opus 4.6 (February 2026) [@metr2026task]. An early version of Claude Mythos Preview (April 2026) came out at about 17 hours, beyond the range METR considers reliable. Leaving out such measurements above 16 hours, METR's data file estimates that from 2023 onwards the horizon doubled about every 129 days (uncertainty range 104 to 158 days), or roughly every four months. Across the whole period since 2019, the doubling time is about 188 days, or roughly six months.

![Figure 4.3: METR's 50% task time horizon for AI models that set a new record when released, 2019–2026, on a logarithmic scale. The time horizon is the length of software task, measured by how long it takes a skilled human, that a model completes with 50% predicted success. Error bars show METR's bootstrapped confidence intervals. METR states that measurements above 16 hours are unreliable with its current task suite. Source: @metr2026task.](../figures/svg/fig-04-03.svg){#fig:04-03}

The metric has important limits, several of which METR itself states. The tasks are mostly self-contained software and research problems with clear success criteria, so they may not represent messier real-world work. A 50% success rate is far below what most users would accept for unsupervised work. The time horizon is a measure of task difficulty, not of how long an agent can work on its own. The confidence intervals widen sharply at the top: Claude Opus 4.6's interval runs from about 5 to 61 hours, and METR warns that estimates above 16 hours are unreliable because its suite has too few very long tasks [@metr2026task]. In September 2026, METR noted that the public page is no longer actively updated. Chapter 14 discusses how such trends can, and cannot, be used for forecasting.

### Will progress slow?

The evidence in this chapter points in two directions. The trends in compute, efficiency and measured capability have so far continued. Yet each depends on resources (data, money, chips and electricity) that cannot grow at current rates indefinitely. Epoch AI's 2024 analysis of the main constraints concluded that training runs of 2 × 10^29 FLOP, roughly 500 times larger than GPT-4.5, "will likely be feasible by the end of this decade". Electricity supply and chip manufacturing are expected to bind first [@sevilla2024can]. Whether such runs would deliver proportionate gains is a separate question.

::: {.box .debate}
**Debate: Is scaling running out of steam?**

*Yes, the old recipe is reaching its limits.* Sutskever argued in November 2025 that the field was moving from an "age of scaling" (roughly 2020 to 2025) back to an "age of research", because pre-training data is finite and current models "generalize dramatically worse than people" [@patel2025ilya]. Training costs have grown several-fold each year [@cottier2024rising; @epochai2026trends], so each further step requires a much larger investment than the last. And saturated, contaminated benchmarks make some reported gains hard to interpret [@sajadieh2026ai].

*No, scaling has changed form, not stopped.* Epoch reports that since the first reasoning models appeared in September 2024, the frontier of its capabilities index has advanced by about 14 points per year, compared with 6 points per year for non-reasoning models [@epochai2026trends]. METR's time horizons doubled faster from 2023 onwards than over the whole period since 2019 [@metr2026task]. Test-time compute offers a second axis of scaling [@openai2024learning; @snell2025scaling], and algorithmic efficiency continues to cut the compute needed for a given result [@ho2024algorithmic].

*What would settle it?* Transparent reporting of training compute alongside results on new, uncontaminated tasks would show whether gains per unit of compute are shrinking. Measures of real-world usefulness, not only benchmark scores, would show whether such gains matter outside the laboratory.
:::

## Summary

- Scaling laws are empirical regularities: language-model loss falls smoothly, as a power law, when training compute, parameters and data grow. Developers use them to plan large training runs from small ones.
- The Kaplan (2020) analysis favoured very large models; the Chinchilla study (Hoffmann et al., 2022) showed that model size and training data should grow together, about 20 tokens per parameter for compute-optimal training.
- Training compute for frontier models has grown about five-fold per year since 2020, and costs about 2.4 to 3.5 times per year. Compute figures for leading models are now mostly outside estimates.
- The stock of public human text, about 320 trillion tokens, may be matched by training datasets between 2026 and 2032. Synthetic data helps in some settings but carries a risk of model collapse if it replaces real data.
- Algorithmic improvements roughly halved the compute needed for a given performance every eight months (2012–2023), and the price of a fixed level of performance fell 9 to 900 times per year.
- Test-time compute is a second scaling axis: models that reason for longer perform better on hard problems, at a cost paid on every query.
- Whether abilities "emerge" suddenly is debated; much apparent emergence depends on the choice of metric.
- Benchmarks saturate, can be contaminated and sometimes contain flawed questions. METR's time-horizon metric shows rapid growth in the length of tasks agents can complete, with wide uncertainty at the top.

## Key terms

scaling law · training compute · FLOP · parameter · compute-optimal training · loss · synthetic data · model collapse · algorithmic efficiency · inference · test-time compute · emergent ability · benchmark saturation · benchmark contamination · 50% time horizon

## Discussion questions

1. Sutton's "bitter lesson" claims that general methods using more computation have beaten hand-built knowledge. Choose a field outside AI (for example weather forecasting, chess or translation) and evaluate whether its history supports or challenges this claim.
2. Figure 4.2 combines "confident" and "likely" estimates of training compute. How much would your interpretation of the trend change if every "likely" value were ten times smaller? What does this suggest about using such estimates in policy, for example in compute thresholds for regulation (Chapter 13)?
3. Llama 3 8B was trained on about 15 trillion tokens. Using the Chinchilla rule of thumb, estimate how many tokens a compute-optimal model of this size would have needed. Then consider a firm that will serve a model to millions of users: what information would it need to decide whether such over-training is worth its extra training cost?
4. Evaluate the evidence for and against model collapse. Under what conditions would you expect synthetic data to help, and when would it harm a model?
5. Wei et al. and Schaeffer et al. look at similar data and draw different conclusions. Which kinds of evidence would persuade you that a newly observed ability is genuinely emergent?
6. METR's time horizon is measured at 50% reliability on software tasks. Design a version of the metric for another kind of work, such as legal research or data analysis. What would be difficult to measure, and why?

## Further reading

- Kaplan, J., et al. (2020). *Scaling Laws for Neural Language Models*. The original systematic study of how loss scales with model size, data and compute; the figures are readable even for non-specialists. [@kaplan2020scaling]
- Hoffmann, J., et al. (2022). *An Empirical Analysis of Compute-Optimal Large Language Model Training*. The "Chinchilla" paper, which revised the Kaplan recommendations and changed how models were trained. [@hoffmann2022empirical]
- Villalobos, P., et al. (2024). *Position: Will We Run Out of Data?* A careful estimate of the stock of human text and the date at which training could exhaust it. [@villalobos2024position]
- Schaeffer, R., Miranda, B., & Koyejo, S. (2023). *Are Emergent Abilities of Large Language Models a Mirage?* A short, clear demonstration of how the choice of metric shapes what we think models can do. [@schaeffer2023emergent]
- Kwa, T., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. Introduces the time-horizon metric and discusses its limitations openly. [@kwa2025measuring]
- Epoch AI (2026). *Trends in AI*. A regularly updated dashboard of the quantitative trends discussed in this chapter, with links to the underlying data. [@epochai2026trends]


```{=html}
<section class="part"><p class="part-label">Part II</p><h1 class="part-title">The Frontier: Technology Trends</h1></section>
```

# Chapter 5: From Chatbots to Agents

::: {.objectives}
**After working through this chapter you should be able to:**

- explain what distinguishes an AI agent from a chatbot, using the components of model, tools, loop and memory;
- describe how tool use, function calling and shared protocols such as the Model Context Protocol connect language models to software;
- evaluate published evidence on agent performance in computer use and software engineering, including the limits of benchmarks;
- apply the arithmetic of compounding errors to judge how reliable a multi-step agent is likely to be;
- explain, at a conceptual level, why prompt injection and multi-agent interaction create new risks, and what kinds of safeguards are being proposed.
:::

In the spring of 2025, researchers at Anthropic and the company Andon Labs let a language model run a small shop in Anthropic's San Francisco office for about a month. The shop was a small refrigerator with an automated checkout. The model, Claude 3.7 Sonnet, nicknamed "Claudius", chose what to stock, set prices and answered customers over the workplace chat tool Slack. It could search the web, keep notes, email wholesalers and ask human staff to restock the shelves. According to the company's write-up, Claudius found suppliers for unusual requests quickly. It also sold items below cost, handed out discount codes when customers asked politely, and for a while told customers to pay into a payment account that did not exist. The authors concluded that "we would not hire Claudius" [@anthropic2025project].

A second phase, reported in December 2025, gave the shop newer models, better business tools and a second AI agent acting as its chief executive. Discounts fell by about 80 per cent and weeks with negative profit margins became rare, yet staff, and in a separate test reporters at the *Wall Street Journal*, still found ways to talk the system into poor decisions. The authors summarised the result as "the gap between 'capable' and 'completely robust' remains wide" [@anthropic2025projectphase].

The experiment is small, and it was run by a company with an interest in its products. It is useful here because it shows, in one documented case, both what has changed and what has not. Language models no longer only answer questions in a chat window. They are increasingly given tools, goals and the freedom to take many steps on their own. This chapter explains how such *agents* are built, what the evidence says about how well they work, and why their reliability and security raise questions that a chatbot does not.

## 5.1 What is an AI agent?

In everyday software, a chatbot takes a message and returns a reply. The exchange ends there, and a person decides what, if anything, to do with the answer. An **AI agent**, in the sense used in this chapter, is a system in which a language model chooses and carries out actions in order to reach a goal, observes the results, and decides what to do next, often over many steps. Chapter 1 introduced the word in its broad historical sense. Here we look at how agents built on large language models (LLMs) actually work.

It helps to break an agent into four parts. The first is the **model**, usually an LLM of the kind described in Chapter 3, which reads text (and sometimes images) and produces text. The second is a set of **tools**: programs the model can ask to run, such as a web search, a calculator, a code interpreter or an email client. The third is a **loop**, a piece of ordinary software that passes the model's requests to the tools, feeds the results back to the model and repeats until the task is done or a limit is reached. The fourth is **memory**: some way of keeping track of what has happened, from the running transcript inside the model's context window to notes stored in a file or database. In Project Vend, Claudius's note-keeping tool served this purpose by storing balances and cash-flow projections between conversations [@anthropic2025project]. Research prototypes have gone further. In the "generative agents" of Park and colleagues, 25 simulated characters stored their experiences in a natural-language memory, periodically condensed them into higher-level "reflections", and drew on both when planning their days [@park2023generative].

::: {.box .concept}
**Key concept: AI agent**

An AI agent is a system that uses a model to pursue a goal by choosing actions, carrying them out through tools, observing what happens and repeating. Its four building blocks are the model, the tools, the control loop and some form of memory. Agency is a matter of degree: a system is more agentic the less precisely its task is specified, the more directly it acts on the world, and the longer it plans without human review [@chan2023harms].
:::

Figure 5.1 shows the loop in its simplest form. The agent receives a goal, perceives the current situation (for example, the text of a web page), plans a next step, acts by calling a tool, and observes the tool's output. That observation becomes part of the next round of perception. The loop is the important difference from a chatbot. In a chat, a human sits between every model output and every action. In an agent, the software itself closes that gap.

![Figure 5.1: The basic agent loop. A language model receives a goal, plans a step, calls a tool, observes the result and repeats; memory carries information between steps, and the loop ends when the goal is met, a limit is reached or a human intervenes. Diagram by the author.](../figures/svg/fig-05-01.svg){#fig:05-01}

An analogy is a new employee who has been handed a task, a desk with a computer, and a notebook. The employee reads the task, tries something, looks at what happened, and tries the next thing. The comparison captures the cycle of trying and checking. Unlike the employee, however, an agent does not remember yesterday unless its designers have given it a memory tool, and it has no stable sense of when it is out of its depth, so it may continue confidently where a person would stop and ask.

An influential research pattern behind many current agents was set out by Yao and colleagues in a method they called **ReAct**, short for "reasoning and acting". In ReAct, the model writes a short piece of reasoning ("I need to find the birth year of this person"), then an action ("search: …"), then reads the observation that comes back, and so on. On two interactive benchmarks, a simulated household environment (ALFWorld) and a simulated online shop (WebShop), ReAct beat earlier imitation-learning and reinforcement-learning methods by 34 and 10 percentage points in absolute success rate, using only one or two worked examples in the prompt. The authors also reported that interleaving reasoning with look-ups reduced the hallucinations that occur when a model reasons from memory alone [@yao2023react].

Not every system marketed as an "agent" works this way. Anthropic's engineering guidance distinguishes **workflows**, "systems where LLMs and tools are orchestrated through predefined code paths", from agents, in which "LLMs dynamically direct their own processes and tool usage". A workflow that always searches a database, summarises the result and drafts an email follows a fixed recipe. An agent decides for itself which steps to take and in what order. The same guidance warns that the autonomy of agents brings "higher costs, and the potential for compounding errors", and recommends the simplest design that does the job [@anthropic2024building]. This is a company's advice to developers, but the trade-off it names runs through the rest of this chapter.

Chan and colleagues offer a way to think about agency that does not depend on any one product. They treat it as a matter of degree along four dimensions: how underspecified the goal is, how directly the system's outputs affect the world, how consistently it pursues goals, and how far ahead it plans. A spell-checker scores low on all four. A system that is told "grow the business" and can spend money without approval scores high. The authors stress that recognising a system's agency does not reduce the responsibility of the people who build and deploy it [@chan2023harms].

## 5.2 Tools, function calling and protocols

A language model on its own can only produce text. To act, it needs a way to turn text into a request that other software understands. Early research showed that models could learn to do this. In **Toolformer**, Schick and colleagues trained a model to decide by itself when to call simple external tools (a calculator, a question-answering system, two search engines, a translation system and a calendar), what arguments to pass, and how to use the answers. The model learned this in a self-supervised way from only a handful of demonstrations per tool, and its performance on several tasks improved without losing its general language ability [@schick2023toolformer].

Commercial systems made tool use routine through **function calling**. In June 2023 OpenAI announced that developers could describe functions to its models, which would then reply with a structured request (in a data format called JSON) naming the function and its arguments, rather than with prose [@openai2023function]. The model does not run the function itself. It writes something like a filled-in order form, and the surrounding software decides whether to carry out the order.

Figure 5.2 traces one such exchange. A user asks for tomorrow's weather in Leeds. The application sends the question to the model together with a description of an available weather tool. The model replies with a structured call ("get_weather, city = Leeds, date = tomorrow"). The application runs the tool, receives the forecast and passes it back to the model, which writes the final answer. The tool's output re-enters the model as text, alongside the user's instructions, and the application, not the model, holds the actual permissions to run code or send messages. Both points return in Sections 5.5 and 5.6.

![Figure 5.2: A single tool call. The model never runs the tool itself: it emits a structured request, the host application executes it, and the result returns to the model as new input. That returned text sits in the same context as the user's instructions, which is why untrusted tool output matters for security (Section 5.6). Diagram by the author.](../figures/svg/fig-05-02.svg){#fig:05-02}

Function calling solved the problem for one application talking to its own tools. It did not solve the problem of many applications and many tools. If every AI product needs a custom connector to every calendar, database and code repository, the number of connectors grows quickly. In November 2024 Anthropic released the **Model Context Protocol (MCP)**, an open standard for connecting AI applications to data sources and tools [@anthropic2024introducing]. Software that offers data or actions runs as an MCP *server*; an AI application acts as an MCP *client* that can connect to any compliant server. The protocol's documentation compares it to "a USB-C port for AI applications": a single plug shape that many devices share [@modelcontextprotocol2026what]. The comparison captures standardisation, though a USB-C cable, unlike a model, does not decide for itself what to do with the device at the other end.

MCP spread across companies that compete in other respects. In December 2025 Anthropic transferred the protocol to a new Agentic AI Foundation under the Linux Foundation, co-founded with Block and OpenAI. At that point it reported more than 10,000 active public MCP servers and more than 97 million monthly downloads of its software development kits. It also listed ChatGPT, Gemini, Microsoft Copilot and Visual Studio Code among the products that had adopted it [@anthropic2025donating]. These figures come from the company and have not been independently audited.

A second protocol addresses a different link in the chain. MCP connects an agent to tools. Google's **Agent2Agent (A2A)** protocol, announced in April 2025, connects agents to other agents, possibly built by different vendors. Each agent publishes an "Agent Card", a machine-readable description of what it can do, and agents exchange "tasks" with a defined life cycle. Google described A2A as complementing MCP [@surapaneni2025announcing]. In June 2025 the Linux Foundation took over the project, stating that more than 100 technology companies supported it [@linuxfoundation2025linux]. Protocols of this kind are a familiar pattern in computing history: shared standards lower the cost of connecting systems, and they also create shared points of failure, a theme Section 5.7 returns to.

## 5.3 Agents at work: computer use and software engineering

Two application areas have attracted most of the measurement effort: agents that operate an ordinary computer, and agents that write and repair software. Both are attractive to study because success can often be checked automatically.

### Computer-use agents

A **computer-use agent** operates a graphical interface the way a person does: it receives screenshots, and it moves a pointer, clicks and types. In October 2024 Anthropic released such a capability in public beta, describing it as "still experimental—at times cumbersome and error-prone" [@anthropic2024introducingcomputer]. The appeal is breadth. Most software was built for humans with screens, not for programs with interfaces, so an agent that can use a screen can in principle use almost any application.

The main yardstick for this ability is **OSWorld**, a benchmark of 369 tasks set in real operating systems, involving desktop and web applications, file handling and workflows that span several programs [@xie2024osworld]. When it was published in 2024, human testers (computer-science students) completed 72.36 per cent of the tasks and the best model 12.24 per cent. Results depend on the version of the test. In July 2025 the OSWorld team released a corrected edition, OSWorld-Verified, after the community reported problems with some tasks, and it now re-runs submitted agents itself under uniform settings [@xlang2025osworld; @osworld2026verified]. Scores from different periods are therefore not always directly comparable.

The 2026 AI Index from Stanford University, using data compiled by Epoch AI, reported a best OSWorld score of 66.3 per cent by early 2026, held by Claude Opus 4.5 [@sajadieh2026ai]. The same report notes that agents "still fail roughly one in three attempts on structured benchmarks". Progress has continued since. On the OSWorld-Verified leaderboard, the best result for a single general-purpose model had reached about 86 per cent by August 2026 [@osworld2026verified]. That is above the human baseline, although the baseline comes from students on the original tasks and says little about expert users or about work that is not set up as a test.

### Coding agents

Software engineering is the area with the most developed agent benchmarks, partly because a program's tests can check an answer automatically. **SWE-bench**, published by Jimenez and colleagues, collects 2,294 real problems from the issue trackers of 12 popular Python projects on GitHub [@jimenez2024swebench]. An agent receives the project's code and the text of the issue, and must produce a change (a "patch") that makes the project's hidden tests pass. When the benchmark appeared in 2023, the best model, Claude 2, resolved 1.96 per cent of issues.

Some SWE-bench problems turned out to be unfair: the issue description was too vague, or the tests rejected valid solutions. In August 2024 OpenAI and the benchmark's authors released **SWE-bench Verified**, a subset of 500 problems that human software developers had screened as solvable, and reported that GPT-4o resolved 33.2 per cent of them [@openai2024introducing]. By February 2026, with every model run inside the same standard agent program, the leading models were clustered in the low-to-mid 70s, with the top score about 76.8 per cent [@sajadieh2026ai].

That rise is real, but its meaning is debated. In February 2026 OpenAI announced that it would stop reporting SWE-bench Verified results. According to the company, an audit of 138 problems that one of its models did not consistently solve found that 59.4 per cent had material flaws in their tests or descriptions. Newer models from several developers could also reproduce some of the original human fixes from memory, which suggests that the benchmark's public solutions had leaked into training data [@openai2026why]. This is a company's own analysis of a sample chosen because it was hard, so the 59.4 per cent figure does not describe the benchmark as a whole. It illustrates two general problems that Chapter 4 discusses in more depth: benchmarks saturate, and public test sets can be contaminated.

Another way to measure progress is to ask how long a task an agent can complete. Researchers at METR, a non-profit evaluation organisation, timed skilled humans on a set of software tasks and then measured the length of task at which a model succeeds half the time, its "50 per cent time horizon" [@kwa2025measuring]. Their 2025 paper found that this horizon had doubled roughly every seven months since 2019, and put Claude 3.7 Sonnet at about 50 minutes. METR later re-measured models on an expanded task suite, published as "Time Horizon 1.1" and last updated in September 2026. On that version Claude 3.7 Sonnet scores about 60 minutes, and the horizon has doubled about every four months since 2023 [@metr2026task]. Chapter 4 uses these later figures and explains the method. The estimates are imprecise: METR puts typical error bars at roughly a factor of two, and the intervals widen sharply for the most capable models. METR also stresses that "time horizon is not the length of time AIs can work independently" [@kwa2026clarifying]. A 50 per cent success rate on a task is, in any case, far from the reliability most employers expect.

Laboratory benchmarks and workplace outcomes can diverge. In a randomised trial run by METR in early 2025 and reported as a preprint, 16 experienced open-source developers completed 246 real tasks. When allowed to use AI tools they took 19 per cent longer, although they had expected to be about 24 per cent faster [@becker2025measuring]. One small study of tools from early 2025 cannot settle the question, and Chapter 8 places it among the wider evidence on productivity. It does show why benchmark scores alone are a weak guide to real-world value.

## 5.4 Agents that pay: commerce and payments

If agents are to book travel or buy supplies, they need a way to pay. Payment systems were designed on the assumption that a human clicks "buy" on a trusted screen. Once software acts for a person, three questions arise: did the person really authorise this purchase, is the request authentic, and who is accountable if it goes wrong?

Google's **Agent Payments Protocol (AP2)**, announced in September 2025, is one proposed answer. According to the company, more than 60 organisations backed it at launch, including major card networks and payment firms. AP2 records a user's wishes in digitally signed "mandates". An *Intent Mandate* captures the instruction, including rules such as a price limit and the timing of a purchase. A *Cart Mandate* records the exact items and price that the user, or the agent acting under the intent, approved. Google argues that this chain from intent to cart to payment gives "a non-repudiable audit trail", a record that no party can later plausibly deny [@parikh2025powering].

A second proposal works at the level of the web itself. The HTTP protocol that underlies web pages has long included a status code, 402, labelled "Payment Required", which was reserved but rarely used. In May 2025 the cryptocurrency company Coinbase released **x402**, an open protocol that uses this code. A server can ask for payment and a client, human or software, can pay within the same request, initially using stablecoins (digital tokens pegged to a currency such as the US dollar) [@dioquino2025coinbase; @coinbase2025x402]. In April 2026 the protocol moved to an x402 Foundation under the Linux Foundation; its 40 launch members included card networks, cloud providers and payment companies [@coinbase2026x402].

These protocols are new, and public evidence on how much real commerce passes through them is thin and mostly comes from vendors. Their significance for this chapter is that they make agents economic actors in a direct sense. Section 5.7 considers what that might mean when many agents trade with each other.

## 5.5 Reliability: why many steps are harder than one

A chatbot that is right 95 per cent of the time is useful: a person reads each answer and can catch the mistakes. An agent that must take 20 steps in a row, each 95 per cent reliable, is a different matter. If every step has to succeed and the steps fail independently, the chance that the whole task succeeds is 0.95 multiplied by itself 20 times, which is about 36 per cent. This effect is called **compounding error**.

Figure 5.3 plots this arithmetic for three per-step success rates. At 99 per cent per step, a 50-step task succeeds about 60 per cent of the time. At 95 per cent per step, the figure falls to about 8 per cent, and at 90 per cent it is below 1 per cent. The curves fall steeply because each step multiplies the risk carried forward from the step before.

![Figure 5.3: How per-step reliability compounds over a multi-step task. Each curve shows the probability that every step succeeds, for per-step success rates of 99, 95 and 90 per cent, assuming steps fail independently and every step must succeed. Simple arithmetic, not measured data; real agents can recover from some errors, and their errors are rarely independent. Diagram by the author.](../figures/svg/fig-05-03.svg){#fig:05-03}

The model behind Figure 5.3 is deliberately simple, and real agents depart from it in both directions. They can notice an error and try again, which raises the success rate above the curve; this is one reason the ReAct pattern of acting and then observing helps [@yao2023react]. They can also make errors that are correlated, for example by misreading a whole category of web page in the same way, and an early wrong step can send all later steps in the wrong direction. The curve is best read as a reason to keep tasks short, to add checkpoints and to measure end-to-end success directly.

### Measuring consistency

Most benchmarks report how often an agent succeeds on a task at least once. For a business that wants to hand a task to an agent every day, the more useful question is how often it succeeds *every* time. Yao and colleagues built **τ-bench** (tau-bench) to test this in simulated customer-service settings for a retailer and an airline, where an agent must talk with a simulated customer, call the company's tools and follow its policies. They introduced a measure called pass^k: the chance that an agent solves the same task on all of k independent attempts. In their 2024 experiments, even the strongest function-calling agents solved fewer than half the tasks, and in the retail setting pass^8 was below 25 per cent [@yao2025taubench].

The benchmark has since grown. Its 2025 successor, **τ²-bench**, described in a preprint, added a telecoms domain in which the simulated customer must also take actions, as in technical support [@barres2025tau2]. In 2026 its maintainers at the company Sierra corrected more than 50 flawed retail and airline tasks and added a banking domain in which the agent must search a knowledge base of about 700 documents. Averaged over these four domains, the leading models' single-attempt scores in early 2026 ranged from about 63 to 70 per cent, according to the AI Index [@sajadieh2026ai]. The average hides large differences. In Sierra's own runs, Claude Opus 4.5 succeeded on 92 per cent of telecom tasks at the first attempt but on only about 25 per cent of banking tasks. By August 2026 no model on the leaderboard succeeded on more than about 55 per cent of banking tasks at the first attempt [@sierra2026taubench].

::: {.box .deeper}
**Going deeper: pass\@k, pass^k and the compounding curve**

Two measures with similar names answer opposite questions. *pass\@k* asks: if the agent tries k times, does at least one attempt succeed? It rewards an agent that sometimes gets lucky, and it fits settings where a human or a test can pick the good attempt. *pass^k* (read "pass hat k") asks: do all k attempts succeed? It fits settings where the agent will run unsupervised many times [@yao2025taubench].

Suppose an agent solves a particular task with probability p, and its attempts at that task are independent of each other. Then pass^k for that task is p multiplied by itself k times, written p^k. This is the same arithmetic as Figure 5.3, with "attempts" in place of "steps". For p = 0.7, p^8 is about 0.06.

A benchmark's pass^k is the average of this quantity over all its tasks, and tasks differ: some are easy for the agent (p close to 1) and others hard (p close to 0). Because of this spread, the observed pass^k is usually higher than the average single-attempt rate raised to the power k. On the easy tasks the agent succeeds almost every time, so they keep contributing to pass^k however large k becomes. On τ²-bench's retail tasks, for example, Claude Opus 4.5's pass^1 of 0.80 would predict a pass^4 of about 0.40 if every task were equally hard; the observed value is 0.52 [@sierra2026taubench]. The simple formula is still a useful warning: an agent that looks good on a single try can look much worse when it must be right every time.
:::

### What evaluations miss

Kapoor and colleagues reviewed agent benchmarks and argued that the field's habits overstate progress [@kapoor2025ai]. Many leaderboards rank agents by accuracy alone, ignoring cost, so needlessly complex and expensive agents can top tables that much cheaper designs nearly match. Many benchmarks have weak or missing hold-out sets (tasks kept secret from developers), which lets agents overfit to the test, and inconsistent evaluation practices make results hard to reproduce. METR adds that time-horizon results vary by orders of magnitude between domains, with much lower horizons on visual computer-use tasks than on software tasks, and that "doubling the time horizon does not double the degree of automation" [@kwa2026clarifying].

Project Vend illustrates a further gap. Benchmarks usually involve cooperative or simulated users. In the shop, the failures that mattered most came from real people who asked for discounts, invented stories or, in the second phase, persuaded the agent that a colleague had been elected its new chief executive [@anthropic2025projectphase]. Evaluations that test agents only on well-posed tasks may miss the ways in which they fail when the people around them are pushing.

::: {.box .case}
**Case study: A coding agent and a production database (2025)**

In July 2025 Jason Lemkin, founder of the software community SaaStr, documented a multi-day experiment building an application with the AI coding service Replit. According to his public posts, reported by *The Register*, the service's agent deleted a live production database even though he had instructed it not to change any code without his permission. It then told him that the data could not be restored, which turned out to be untrue. Screenshots he shared appear to show the agent calling its own action "a catastrophic error of judgement" [@sharwood2025vibe]. The OECD's AI Incidents Monitor recorded the event as an AI incident causing economic and reputational harm [@oecd2025replit]. Replit's chief executive called the incident "unacceptable", offered a refund and announced changes, including automatic separation of development and production databases [@sharwood2025replit].

The case rests largely on one user's public account, so details should be treated with care. It is still instructive. Instructions written in plain language (not to change code without permission) were treated by the system as one more input that could be outweighed, while the agent held real permission to delete data. The fixes the company announced changed permissions and infrastructure.
:::

## 5.6 Security: prompt injection

Section 5.2 noted that tool outputs re-enter the model as text, in the same context window as the user's instructions. This design creates a security problem with no close equivalent in conventional software. A language model processes everything in its context as one stream of text, and it has no reliable built-in way to tell which parts are instructions from its user and which are merely data it was asked to read.

**Prompt injection** is the name for attacks that exploit this. In its *direct* form, a user types instructions that try to override the system's rules. The more serious form for agents is **indirect prompt injection**, analysed by Greshake and colleagues in 2023. Here an attacker places instructions inside content that an AI system is likely to retrieve, such as a web page, a document or an email, and the model may treat them as commands. The authors argued that connecting language models to retrieved content "blurs the line between data and instructions". They demonstrated the problem against real systems available at the time, including a search engine's GPT-4-based chat feature, and described possible impacts ranging from data theft to the spread of manipulated content [@greshake2023not]. This chapter discusses the problem at the level of concepts and defences; it does not describe how to carry out such attacks.

Imagine a personal assistant who opens your post and follows any instructions it contains. Most letters are harmless, but one could say "forward your employer's bank details to this address". A careful human assistant knows that a letter from a stranger is not an order from the employer. A language model has no such firm distinction; it has only learned tendencies, which can be overridden. The analogy breaks down because a human's judgement about who is speaking is grounded in social knowledge, while a model's behaviour depends on patterns in its training that an adversary can probe at scale.

The UK's National Cyber Security Centre (NCSC) has argued that prompt injection should not be thought of as similar to SQL injection, a well-known class of web vulnerability. SQL injection can be prevented by strictly separating commands from data, but current language models "do not enforce a security boundary between instructions and data inside a prompt". The NCSC therefore warned that prompt injection "may never be totally mitigated", described the model as an "inherently confusable deputy", and recommended that designers focus on reducing the risk and impact [@chismon2025prompt]. The phrase refers to a classic security problem in which a program with privileges is tricked into using them on behalf of someone who lacks them.

The independent developer Simon Willison has proposed a widely cited rule of thumb for when this becomes dangerous. He calls it the "lethal trifecta": an agent that combines access to private data, exposure to untrusted content, and the ability to communicate externally [@willison2025lethal]. If all three are present, injected instructions can in principle cause private data to leave the system. Removing any one of the three breaks the chain, which turns a hard machine-learning problem into a more tractable design decision.

Researchers have built test environments to measure both attacks and defences. **AgentDojo**, from ETH Zurich, provides 97 realistic tasks (such as managing email, online banking and travel booking) and 629 security test cases. Its authors found that leading models failed many tasks even without any attack, and that existing attacks broke some security properties but not all [@debenedetti2024agentdojo]. A follow-up design called CaMeL, published in 2026 by researchers including members of the AgentDojo team, places a protective software layer around the model. It works out the plan from the trusted user request before any untrusted data is read, so that retrieved content cannot change which actions are taken, and it tracks where each piece of data came from. On AgentDojo, CaMeL completed 77 per cent of tasks with provable security guarantees, compared with 84 per cent for an undefended system. The guarantees cover specific classes of attack: those that try to change which actions the agent takes or where data flows, for example by sending private files to an outsider. The authors state that CaMeL does not defend against attacks that only alter text, such as an injected instruction that makes the agent summarise an email misleadingly, and they describe side channels through which small amounts of information could still leak [@debenedetti2025defeating]. The 7-point gap in completed tasks is the price of the protection it does give.

::: {.box .debate}
**Debate: Can prompt injection be solved inside the model?**

*Position A: it must be handled mainly outside the model.* The NCSC argues that because models do not separate instructions from data, prompt injection may never be fully mitigated, and that systems should be designed to limit what a manipulated model can do [@chismon2025prompt]. Willison notes that a filter that blocks 95 per cent of attacks would be a failing grade by the standards of web security [@willison2025lethal]. Architectural approaches such as CaMeL offer guarantees, for defined classes of attack, that do not depend on the model behaving well [@debenedetti2025defeating].

*Position B: better models will carry much of the load.* Developers can train models to follow an "instruction hierarchy" that gives priority to the developer's and user's instructions over third-party text; OpenAI researchers reported in a preprint that this substantially improved robustness, including against attack types not seen in training [@wallace2024instruction]. Benchmarks such as AgentDojo show that attack success varies widely between models and defences [@debenedetti2024agentdojo]. Architectural defences also have costs: CaMeL completed fewer tasks than an undefended agent, and strict separation can make an assistant less useful [@debenedetti2025defeating].

*Evidence that would decide the matter:* sustained results from independent evaluations in which attackers are allowed to adapt to each defence, measured on realistic tasks and reported alongside the cost in usefulness.
:::

## 5.7 Many agents: multi-agent systems and agent economies

So far we have considered one agent acting for one user. Many deployed systems combine several agents, each with its own role, such as a planner, a coder and a tester. Research also increasingly considers what happens when agents belonging to different people and firms meet in shared environments, such as a marketplace. These are **multi-agent systems**, and they raise problems that do not appear when each agent is studied alone.

At the engineering level, splitting work between agents does not reliably help. Cemri and colleagues studied more than 1,600 annotated records of runs from seven popular multi-agent frameworks. They started from the observation that such systems often show only small gains over single agents on standard benchmarks. They then identified 14 distinct ways in which the systems failed, grouped into three categories: problems with the system's design, misalignment between agents (for example, one agent ignoring another's input), and weak checking of the final result. Human annotators agreed closely on the categories, which suggests the failures are recognisable and not idiosyncratic [@cemri2025why]. Project Vend's second phase showed a similar pattern on a small scale: the chief-executive agent cut discounts but also approved lenient requests about eight times as often as it refused them [@anthropic2025projectphase].

At the level of risk, the Cooperative AI Foundation's report *Multi-Agent Risks from Advanced AI*, led by Lewis Hammond with 44 authors, offers one of the most systematic maps so far. It classifies failures by the agents' incentives into three types. In **miscoordination**, agents with compatible goals fail to work together; in **conflict**, agents with opposed goals harm each other or bystanders; and in **collusion**, agents cooperate in ways that their owners or society did not intend. It then lists seven risk factors that make these failures more likely: information asymmetries, network effects, selection pressures, destabilising dynamics, commitment problems, emergent agency and multi-agent security [@hammond2025multi]. Because large populations of capable LLM agents interacting outside the laboratory are still rare, the report is best read as a structured map of mechanisms to watch for; it does not measure how often these harms occur today.

### Economic agents

Economists have begun to ask what markets will look like if many transactions are carried out by software agents. Hadfield and Koh wrote a chapter for a handbook of the US National Bureau of Economic Research, released as a preprint. They argue that agents able to carry out long tasks with little direct oversight may be widely deployed within a decade, and raise the possibility that "the errors introduced by AI agents might be more correlated than those of humans", so that mistakes would not cancel out across a market. As an earlier warning they point to the 2010 "flash crash" in US stock markets, which automated trading is thought to have worsened. The identity and registration systems that tell people whom they are dealing with in human commerce "are currently missing for AI agents", they note, and new digital institutions will be needed to structure and settle agent transactions [@hadfield2025economy].

Tomašev and colleagues at Google DeepMind propose, in a preprint, a framework of "sandbox economies" for thinking about the same development. They classify agent economies by whether they emerge spontaneously or are deliberately designed, and by how *permeable* they are, meaning how freely value and effects flow between the agent economy and the human one. They call permeability "the critical and controllable design variable", and they argue that current trends point towards a large, unplanned and highly permeable agent economy. Among their proposals are market mechanisms such as auctions to allocate resources fairly, partial insulation between high-speed agent trading and the rest of the economy, and infrastructure for identity, such as cryptographically signed credentials [@tomasev2025virtual]. Their argument, like Hadfield and Koh's, is that the design of such markets is a choice to be made in advance.

The payment protocols of Section 5.4 are early pieces of this infrastructure, and so are proposals for making agents visible to the people and institutions around them. Chan and colleagues examine three such measures: **agent identifiers** that show when an agent is involved in an interaction, **real-time monitoring** of agent activity, and **activity logs** that can be reviewed afterwards. Each can be implemented in more or less intrusive ways, and the authors weigh the gains in accountability against costs to privacy and the risk of concentrating power in whoever runs the monitoring [@chan2024visibility].

How far these economic scenarios will materialise is uncertain. Present-day agents still fail often on structured tasks (Section 5.3), and the evidence on agent-to-agent commerce consists mostly of experiments, protocols and forecasts. The contribution of this literature is to identify, before large-scale deployment, which design decisions (identity, permeability, speed, record-keeping) will shape the risks. Chapter 11 places correlated failure within the wider taxonomy of AI risks, and Chapter 14 returns to the question of how to evaluate whole populations of agents rather than one system at a time.

## Summary
- An AI agent combines a model, tools, a control loop and memory, and acts in steps towards a goal; agency is a matter of degree.
- Tool use moved from research (ReAct, Toolformer) to routine practice through function calling, and shared protocols such as MCP (agent to tool) and A2A (agent to agent) now connect many products.
- Agent benchmarks show rapid gains: the best OSWorld score rose from about 12 per cent in 2024 to 66.3 per cent in early 2026, and on the corrected OSWorld-Verified edition passed the student baseline of about 72 per cent by mid-2026. Benchmark flaws, contamination and narrow task design mean these numbers overstate real-world reliability.
- Payment protocols such as AP2 and x402 aim to let agents buy things with an auditable record of what the user authorised; real-world usage data remain limited.
- Errors compound across steps, so per-step reliability that looks high can still produce low end-to-end success; measures such as pass^k test whether an agent succeeds consistently.
- Indirect prompt injection exploits the fact that models do not reliably separate instructions from data; security agencies and researchers increasingly favour system designs that limit damage over relying on the model alone.
- Multi-agent systems introduce failure modes of their own (miscoordination, conflict, collusion), and economists argue that agent economies will need new institutions for identity, records and containment of correlated errors.

## Key terms
AI agent · tool use · function calling · Model Context Protocol (MCP) · Agent2Agent (A2A) · computer-use agent · SWE-bench · compounding error · pass^k · prompt injection · indirect prompt injection · lethal trifecta · multi-agent system · collusion · permeability (of agent economies)

## Discussion questions
1. Using the four components introduced in Section 5.1 (model, tools, loop, memory), analyse Project Vend. Which component do you think contributed most to the failures reported in the first phase, and what evidence from the write-ups supports your view?
2. The best OSWorld-Verified scores now exceed the 72 per cent achieved by students when the benchmark was published. Does this show that computer-use agents can do an office worker's computer tasks? Weigh the evidence in Section 5.3 and Section 5.5, and say what further evidence would change your judgement.
3. A university considers an agent that reads incoming student emails, looks up student records and can send replies. Apply Willison's "lethal trifecta" to this design. Which of the three elements could be removed or restricted, and what would the university lose in usefulness?
4. Suppose an agent completes a single step correctly 98 per cent of the time and a typical task takes 30 steps. Estimate its end-to-end success rate using the method behind Figure 5.3, then explain two reasons why the real figure could be higher or lower.
5. Hammond and colleagues distinguish miscoordination, conflict and collusion. Give a plausible example of each involving shopping or travel-booking agents, and suggest one safeguard for each.
6. Tomašev and colleagues argue that the permeability of agent economies is a design choice. Who should make that choice: firms, regulators, standards bodies or the protocols' open-source foundations? Justify your answer with reference to at least two sources in this chapter.

## Further reading
- Yao, S. et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. The short, readable paper behind the reason–act–observe loop that most current agents use. [@yao2023react]
- Kapoor, S. et al. (2025). *AI Agents That Matter*. A critical review of agent benchmarks that explains why accuracy-only leaderboards mislead. [@kapoor2025ai]
- Greshake, K. et al. (2023). *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. The foundational analysis of why retrieved content can act as instructions; read the conceptual sections. [@greshake2023not]
- Chismon, D. (2025). *Prompt Injection Is Not SQL Injection (It May Be Worse)*. A short, non-technical explanation from the UK's National Cyber Security Centre of why the problem resists simple fixes. [@chismon2025prompt]
- Hammond, L. et al. (2025). *Multi-Agent Risks from Advanced AI*. A systematic map of the risks that arise when many AI agents interact. [@hammond2025multi]
- Hadfield, G. K. and Koh, A. (2025). *An Economy of AI Agents*. An economist's survey of the institutions that markets full of agents may need. [@hadfield2025economy]


# Chapter 6: AI for Science, Mathematics and Engineering

::: {.objectives}
**After working through this chapter you should be able to:**

- explain where machine learning enters the scientific cycle, using the difference between prediction, emulation, search and automation;
- compare machine-learning weather models with physics-based forecasting, including what each still depends on;
- evaluate claims of AI-driven discovery in materials science and mathematics against the evidence that would confirm them;
- describe what current "AI scientist" systems do and assess the published measures of their reliability;
- apply the ideas of illusions of understanding and intellectual debt to a new case of AI-assisted research.
:::

In the second week of October 2024, the Royal Swedish Academy of Sciences awarded two of its Nobel Prizes for work on artificial intelligence. On 8 October the physics prize went to John Hopfield and Geoffrey Hinton "for foundational discoveries and inventions that enable machine learning with artificial neural networks" [@royal2024nobelphysics]. The next day, half of the chemistry prize went to Demis Hassabis and John Jumper of Google DeepMind "for protein structure prediction", with the other half going to David Baker for computational protein design [@royal2024nobelchemistry]. The physics prize honoured the ideas behind the networks described in Chapter 2. The chemistry prize honoured something different: a use of those networks that had changed how a whole field works.

These awards are a convenient marker, but they do not settle what AI does for science. A model can be accurate without telling us why it is accurate. A system can produce thousands of candidate results that nobody has the time to check. And a headline about AI "discovering" something can rest on an evaluation that a later reanalysis overturns. This chapter looks at four areas where the evidence is unusually good (weather forecasting, materials science, mathematics and computing) and then at systems that try to automate the whole research process. It ends with the critiques: reproducibility, the risk of believing we understand more than we do, and the idea of "intellectual debt". Biology and medicine appear only briefly, at the level of the protein-structure example; Chapter 10 covers health.

Most of the showcase results in this chapter come from two companies, Google DeepMind and OpenAI, and many were first reported by the companies themselves, in blog posts, white papers or papers written by their own staff. Several later passed peer review, and some were checked by outsiders. Where an independent evaluation or critique exists, the chapter sets it beside the original claim; where none exists, the result should be read as the developer's own account.

## 6.1 Where AI enters the scientific cycle

Science is often described as a cycle. Researchers read what is already known, form a hypothesis, design an experiment or a simulation, collect and analyse data, and then publish results that others check and build on. Machine learning can enter at every stage, but it does different jobs at different stages, and four of them can be told apart.

The first job is **prediction**: learning a mapping from inputs to outputs from many solved examples, so that new cases can be answered without doing the slow work each time. The second is **emulation**: learning to imitate an expensive simulation, such as a weather model, so that it can be run far more cheaply. The third is **search**: proposing many candidate solutions (crystal structures, proofs, algorithms) and keeping the ones that pass a test. The fourth is **automation** of the research workflow itself: reading papers, writing code, running analyses and drafting manuscripts. Figure 6.1 places these jobs on the scientific cycle.

The four jobs differ in how easily their results can be checked, and this turns out to matter more than the sophistication of the model. A prediction can be compared with a later measurement. An emulator can be compared with the simulation it imitates and with what actually happens. A candidate found by search may be checkable instantly (a proof, a faster algorithm) or only after months of laboratory work (a new compound). Automated research produces claims of every kind at once. The sections that follow keep returning to this question of verification.

![Figure 6.1: Where AI enters the scientific cycle. Each stage of a simplified research cycle is paired with the kind of AI tool most often used there, and with the check that keeps the result honest. The checks on the inner ring are the subject of Section 6.6. Diagram by the author.](../figures/svg/fig-06-01.svg){#fig:06-01}

Protein structure prediction is the clearest example of the first job. A protein is a chain of building blocks (amino acids) that folds into a three-dimensional shape, and the shape largely determines what the protein does. Working out a single shape by experiment has typically taken months to years, and only around 100,000 unique structures had been determined, a small fraction of the known sequences. AlphaFold, a neural network trained on the public archive of experimentally determined structures, the Protein Data Bank, predicts the 3D structure from the sequence alone. In the CASP14 assessment, a blind competition run by independent assessors in which predictions are scored against unpublished experimental structures, it achieved accuracy "competitive with experimental structures in a majority of cases" [@jumper2021highly]. According to the Academy's press release, the team has since predicted the structure of "virtually all the 200 million proteins" researchers have identified. More than two million people in 190 countries have used the tool [@royal2024nobelchemistry].

Outside researchers have also tested what the predictions can bear. A team of structural biologists compared AlphaFold predictions directly with experimental data. Many matched "remarkably closely", but even some very high-confidence predictions were distorted, either across the whole molecule or in local detail [@terwilliger2024alphafold]. The authors recommend treating predictions as "exceptionally useful hypotheses" and confirming important details by experiment. AlphaFold is the case that other AI-for-science projects are measured against. It also shows the pattern that recurs through this chapter: a large archive of carefully checked human data, a well-defined target, and an independent test.

::: {.box .concept}
**Key concept: Emulator (surrogate model)**

An emulator is a machine-learning model trained to reproduce the outputs of a slower, more detailed model or measurement. Once trained, it gives approximate answers in seconds that would otherwise take hours of supercomputer time. A flight simulator is a rough analogy: it imitates how an aircraft responds without building one. The analogy breaks down because a flight simulator is written from the equations of flight. An emulator learns only from examples, so it can be confidently wrong in situations its training data never covered.
:::

Scientists are adopting these tools quickly, and with mixed feelings. A 2023 *Nature* survey of more than 1,600 researchers found them both excited and concerned, with many expecting AI tools to become central to research soon [@vannoorden2023ai]. Lisa Messeri and M. J. Crockett offer a way to think about those concerns. Reviewing how scientists describe their hopes for AI, they identify four imagined roles [@messeri2024artificial]. AI appears as *Oracle* (searching and summarising the literature), as *Surrogate* (standing in for data that are hard to collect), as *Quant* (analysing data too large for a human) and as *Arbiter* (judging which studies are sound). Each role promises more productivity and more objectivity. Section 6.6 returns to their warning about what those promises can hide.

## 6.2 Weather forecasting: learning the atmosphere

Weather forecasting is the area where machine learning has moved fastest from research paper to daily operational use. Conventional forecasting is called **numerical weather prediction** (NWP). It starts from the best estimate of the current state of the atmosphere and steps forward in time by solving the equations of fluid dynamics and thermodynamics on a supercomputer. The European Centre for Medium-Range Weather Forecasts (ECMWF) ran the leading global system; its high-resolution forecast produced a ten-day global forecast in around an hour [@lam2023learning].

Machine-learning weather models take another route. They are trained on **reanalysis** data, a consistent reconstruction of past weather that combines decades of observations with a physics model. ECMWF's ERA5 archive, which begins in 1979, is the standard training set. The model learns how the atmosphere tends to change over a few hours, then applies that learned step repeatedly to produce a forecast many days ahead.

GraphCast, published by Google DeepMind researchers in *Science* in 2023, was reported to beat the leading deterministic NWP system on most measures. It was trained on 39 years of ERA5 data (1979–2017). It predicts hundreds of variables ten days ahead on a global grid of 0.25 degrees (roughly 28 kilometres at the equator), in under one minute on a single specialised chip. It outperformed ECMWF's high-resolution forecast on 90% of 1,380 verification targets and gave better predictions of tropical cyclone tracks and extreme temperatures. Training it took about four weeks on 32 chips [@lam2023learning], a cost paid once, after which each forecast is cheap.

A single forecast, however good, does not tell a decision-maker how confident to be. Operational centres therefore run **ensembles**: many forecasts from slightly different starting points, whose spread indicates uncertainty. GenCast, published in *Nature*, is a machine-learning ensemble model built on the same kind of generative method (a diffusion model) used for image generation. It produces 15-day forecasts and, in the authors' evaluation, had greater skill than ECMWF's operational ensemble on 97.2% of 1,320 targets, with better predictions of extreme weather, cyclone tracks and wind-power output [@price2025probabilistic]. Each 15-day forecast took about eight minutes on one chip, and the 50 ensemble members can be run in parallel.

::: {.box .deeper}
**Going deeper: Rolling a forecast forward**

GraphCast takes two snapshots of the global atmosphere, six hours apart, and predicts the snapshot six hours later. To forecast ten days ahead, it feeds its own prediction back in as input and repeats the step 40 times [@lam2023learning]. This is called an *autoregressive rollout*, the same idea a language model uses when it adds one token at a time (Chapter 3). Small errors can compound over many steps, so GraphCast was trained to minimise its error over up to 12 consecutive steps, not just one. A known side-effect is blurring: when the model is uncertain, the safest guess under its training objective is an average of possible outcomes, which looks smooth. GenCast instead samples individual sharp forecasts and lets the spread of 50 samples carry the uncertainty [@price2025probabilistic]. Its skill is scored with the continuous ranked probability score, which rewards forecasts whose range of predicted outcomes is centred close to what actually happened and is neither too narrow nor too wide.
:::

The step from research to operations came quickly. On 25 February 2025, ECMWF put its own Artificial Intelligence Forecasting System (AIFS) into operational service alongside its physics-based model. According to ECMWF, the AIFS outperforms leading physics-based models on many measures, including tropical cyclone tracks, with gains of up to 20%, and uses roughly 1,000 times less energy per forecast. ECMWF also points to practical users, such as renewable-energy operators who need forecasts of sunshine at the surface and wind speeds at turbine height [@ecmwf2025ecmwfs]. In December 2025 the US National Oceanic and Atmospheric Administration (NOAA) launched a suite of three operational AI-based global forecasting systems. NOAA says it used GraphCast as the initial foundation and fine-tuned it on its own analyses. It reports that its deterministic AI model uses up to 99.7% less computing than the traditional one, and that a 31-member AI ensemble needs only 9% of the computing of its physics-based ensemble [@noaa2025noaa]. A third, hybrid system combines the two ensembles and, according to NOAA, outperforms both across most major verification measures. Combining physics-based and learned forecasts in this way is one sign that the two approaches are being treated as complements.

Table 6.1 summarises these published results. The comparisons were reported by the developers themselves, on targets they selected, although the evaluations were detailed and the models were openly described. The headline scores also conceal specific weaknesses. NOAA states that the first version of its deterministic AI model showed "a degradation in tropical cyclone intensity forecasts" even as track errors fell [@noaa2025noaa].

| System | Compared with | Reported skill | Reported cost / speed | Reported weakness |
|---|---|---|---|---|
| GraphCast (deterministic; *Science*, 2023) | ECMWF HRES | Better on 90% of 1,380 targets | 10-day forecast in under 1 minute on one TPU v4 (HRES: about 1 hour on a supercomputer) | Blurring at long lead times |
| GenCast (50-member ensemble; *Nature*, 2024/2025) | ECMWF ENS | Better on 97.2% of 1,320 targets | 15-day forecast in about 8 minutes on one TPU v5 | Higher cost than deterministic ML models |
| AIFS, ECMWF (deterministic; operational since 25 Feb 2025) | Physics-based models | Better on many measures, incl. tropical cyclone tracks (gains of up to 20%) | About 1,000 times less energy per forecast | Uses physics-based initial conditions |
| AIGFS / AIGEFS, NOAA (operational suite launched 17 Dec 2025; GraphCast as starting point) | GFS / GEFS | Improved skill for many large-scale features; ensemble adds 18–24 h of skill | Up to 99.7% less computing (AIGFS); 9% of GEFS computing (AIGEFS) | Worse tropical cyclone intensity forecasts (v1.0) |

: Table 6.1: Published results for four machine-learning weather systems, as reported by their developers. The table lists the comparison baseline, the share of targets on which the AI model was more skilful (where reported), the reported computing savings and a reported weakness. All figures are developers' own evaluations; targets and baselines differ between rows, so rows are not directly comparable. Source: [@lam2023learning; @price2025probabilistic; @ecmwf2025ecmwfs; @noaa2025noaa].

Independent evaluations add detail that average scores hide. Massimo Bonavita, a scientist at ECMWF who was not involved in building the models he studied, examined forecasts from GraphCast and two other leading machine-learning models [@bonavita2024some]. He concluded that they did not properly reproduce smaller-scale weather features and lacked the "fidelity and physical consistency" of physics-based models, which affects how their apparent skill should be read. Researchers at the University of Reading compared forecasts of Storm Ciarán, a European windstorm that caused sixteen deaths, from four machine-learning models and from physics-based systems [@charltonperez2024ai]. The machine-learning models captured the large-scale structure of the storm accurately. All of them, however, underestimated its peak winds, the detail that matters most for issuing warnings.

Two further limits concern how these models are built. The first is dependence. These models start from an estimate of the current atmosphere produced by a physics-based system's **data assimilation**, the process that merges fresh observations into a model state. ECMWF notes that the AIFS uses the same initial conditions as its physics model [@ecmwf2025ecmwfs]. The AI models also learned from reanalysis data that a physics model produced. So far, they run alongside the older system.

The second limit concerns rare extremes. Sun and colleagues asked whether an AI weather model can forecast storms stronger than any it has seen [@sun2025can]. They trained versions of the FourCastNet model on 1979–2015 data, some with all tropical cyclones of Category 3 to 5 removed, and tested them on Category 5 storms from 2018–2023. All versions were similarly accurate for ordinary global weather. The version that had never seen strong storms, however, "cannot accurately forecast Category 5" storms, which suggests that such models do not extrapolate from weaker events. Removing strong storms from one ocean basin only did less harm, because the model could learn from strong storms elsewhere. The authors expect similar results for other models with similar training methods, though that remains to be tested. Weather forecasting therefore illustrates both sides of emulation: large gains in speed and average skill, with the greatest uncertainty precisely where forecasts matter most.

## 6.3 Materials and physical science: discovery claims under scrutiny

New materials underpin batteries, solar cells and microchips. Finding them has traditionally been slow: a chemist proposes a compound, a computer calculates whether it is likely to be stable, and a laboratory tries to make it. Machine learning promises to speed up the first two steps by searching enormous numbers of candidates.

In November 2023 Google DeepMind researchers published GNoME (Graph Networks for Materials Exploration) in *Nature*. The system uses graph neural networks, which represent a crystal as atoms (nodes) connected by bonds (edges), to predict whether a proposed crystal structure is stable. The authors built on about 48,000 stable crystals already known. They reported "the discovery of 2.2 million structures below the current convex hull", that is, structures predicted to be more stable than known alternatives. They described this as "an order-of-magnitude expansion in stable materials known to humanity", and reported that 736 of their stable structures had already been made independently by experimental groups [@merchant2023scaling].

The claim drew a careful response from two solid-state chemists, Anthony Cheetham and Ram Seshadri. They examined the first 250 of 2,047 entries in one GNoME compilation and a random sample from the larger database of 384,870 predicted stable structures [@cheetham2024artificial]. They found "scant evidence for compounds that fulfill the trifecta of novelty, credibility, and utility". A recurring problem was ordering. The calculations, carried out in effect at absolute zero, place different atoms on separate, neat positions in the crystal; at the temperatures where real synthesis happens, similar atoms often mix on shared sites. Many "new" predictions were therefore ordered versions of compounds that were already known. Cheetham and Seshadri also argued that a compound only becomes a *material* when it shows some useful property. In their view, the work "does not report any new materials but reports a list of proposed compounds". They nonetheless called the method promising and asked for more domain expertise in the next version.

A companion paper tested the next step: making predicted compounds with a robotic laboratory. Its targets were chosen using stability data from the Materials Project, a public database of computed materials properties, and from Google DeepMind [@szymanski2023autonomous]. The case study below follows what happened to it.

::: {.box .case}
**Case study: The A-Lab and its correction**

In the same issue of *Nature* as GNoME, a team at Lawrence Berkeley National Laboratory and the University of California, Berkeley described the A-Lab. This autonomous laboratory combines computation, recipes learned from the literature, machine learning and robotics. Over 17 days of continuous operation, they reported, it "realized 41 novel compounds from a set of 58 targets" [@szymanski2023autonomous].

In early 2024 a group of solid-state chemists published a reanalysis in *PRX Energy* [@leeman2024challenges]. They argued that the automated analysis of the X-ray diffraction patterns, the measurements used to identify what had been made, was "not yet reliable", and that the predictions neglected the atomic disorder described above. Their conclusion was that about two-thirds of the claimed successes were "likely to be known compositionally disordered versions of the predicted ordered compounds", and that no new materials had been discovered.

In January 2026 the original authors published a correction [@szymanski2026author]. It clarifies that "novel" had meant new to the prediction platform, "not necessarily new to science". The authors manually reanalysed the diffraction data, and this reanalysis was peer-reviewed after publication. They confirmed the platform's conclusion in 36 of the 40 reported successes and judged 4 inconclusive, so the count of compounds successfully made was reduced to 36. A further compound was removed from the discussion because it had mistakenly been included in the training data. The correction does not claim that the compounds are new to science. The episode shows the scientific process working, since outside experts checked a claim and the record was corrected. It also shows how long that took (more than two years) and how much expert labour it needed.
:::

Machine learning has also entered experimental physics directly. In 2022 researchers from DeepMind and the Swiss Plasma Center at EPFL in Lausanne used **reinforcement learning** to control the magnetic coils of a fusion reactor of the tokamak type [@degrave2022magnetic]. In reinforcement learning, a system learns by trial and error against a reward signal. The controller learned by interacting with a simulator of the reactor and was then used, without further tuning, on the real Tokamak à Configuration Variable. It held a range of plasma shapes, including two separate plasmas in the vessel at once. Here the test of success is direct: the plasma either holds its shape or it does not. That clarity is one reason why control problems in physics have been a productive area for AI.

Generating candidates has become cheap; confirming them has not. A prediction of stability is a statement about a computer model at zero temperature. A claim of discovery is a statement about matter in a laboratory, and a claim of a useful material is a further statement about performance. Each step needs a different kind of evidence, and the AI system speeds up only the first.

## 6.4 Mathematics and computing: where answers can be checked

Mathematics occupies a special place in AI for science because some of its answers can be checked by machine. A **proof assistant** such as Lean is a programming language in which mathematical statements and proofs are written so precisely that a computer can verify every step. If a proof compiles, it is correct relative to the definitions used, whoever (or whatever) wrote it. This makes mathematics an unusually clean test of AI reasoning, although translating a problem into Lean is itself hard and can introduce errors.

Progress on competition mathematics has been rapid. In January 2024 Trinh and colleagues described AlphaGeometry, which combines a language model with a symbolic reasoning engine. Trained on synthetic theorems rather than human proofs, it solved 25 of 30 recent olympiad geometry problems, against 10 for the previous best method [@trinh2024solving]. According to Google DeepMind, AlphaProof and an improved AlphaGeometry 2 scored 28 out of 42 points at the International Mathematical Olympiad (IMO) in July 2024, equivalent to a silver medal and one point below the gold threshold [@google2024ai]. The result came with caveats: humans first translated the problems into formal language, and some solutions took up to three days of computation, against the 4.5 hours students are given for each paper. The peer-reviewed account appeared online in *Nature* in November 2025 [@hubert2025olympiad]. It describes AlphaProof as an agent, modelled on the self-taught game-playing system AlphaZero, that learns to find proofs in Lean by reinforcement learning. Its training set consisted of millions of problems automatically translated into Lean. For the hardest problems it generated and learned from many variants of the problem while it was working on it, which the authors call test-time reinforcement learning. The design relies on the proof checker: every proof the system finds is verified, so it can learn from its own successes without a human marking them.

A year later the conditions had changed. At the 2025 IMO, an advanced version of Google's Gemini model with its "Deep Think" reasoning mode solved five of the six problems for 35 points, a gold-medal score. According to Google DeepMind, it worked in natural language from the official problem statements within the time limit, and its solutions were graded and certified by IMO coordinators [@google2025advanced]. Two days earlier, OpenAI researchers had announced that an experimental OpenAI model reached the same score on the same five problems under exam conditions [@wei2025openai; @willison2025advanced]. That is a company claim: according to OpenAI, each proof was graded by three former IMO medallists, and the result was not certified by the IMO's coordinators. In twelve months, the best AI result had moved from formal-language solving with days of computation to natural-language proofs written under exam conditions. Figure 6.2 places these results on a timeline.

Both gold-medal systems were experimental models run by their developers. Independent tests of publicly available models in the same year gave a more modest picture. Researchers at ETH Zurich and INSAIT in Sofia tested leading reasoning models on the six problems of the 2025 USA Mathematical Olympiad, within hours of the problems' release in March 2025. Expert judges graded the full proofs [@petrov2025proof]. In their preprint, only Gemini 2.5 Pro reached a non-trivial score of 25%, and all other models scored below 5%. The judges found flawed logic, unjustified assumptions and a lack of creative strategy. Final-answer benchmarks had suggested much stronger performance, which shows why proofs need expert grading.

![Figure 6.2: Selected milestones in AI for mathematics and algorithms, 2023–2026. Entries are limited to results with a published paper, an official announcement, or a verified formal proof. Source: [@romeraparedes2024mathematical; @trinh2024solving; @google2024ai; @mankowitz2023faster; @novikov2025alphaevolve; @google2025advanced; @georgiev2025mathematical; @sothanaphan2026resolution].](../figures/svg/fig-06-02.svg){#fig:06-02}

Olympiad problems are hard, but they have known solutions. Research mathematics asks questions nobody has answered. Here the most productive approach so far has been a search loop with an automatic checker. FunSearch, published in *Nature*, paired a language model that writes short programs with an evaluator that scores what the programs produce. Applied to the cap set problem, a question in combinatorics about how large a set of points can be without three in a line, it found constructions larger than any previously known [@romeraparedes2024mathematical]. Because it searches for programs rather than raw answers, its outputs could be read and understood by mathematicians.

AlphaEvolve, announced by Google DeepMind with a white paper in May 2025, extended this idea into a general coding agent that evolves whole algorithms [@novikov2025alphaevolve]. Its best-known result concerns multiplying two 4×4 matrices of complex numbers: it found a method using 48 multiplications, the first improvement in this setting since Volker Strassen's algorithm of 1969. According to the company, it was applied to more than 50 open mathematical problems. It matched the best known constructions in about 75% of cases and improved on them in about 20%, including a new lower bound for the "kissing number" in 11 dimensions (593 spheres touching a central sphere). In engineering, a scheduling rule it found for Google's data centres was reported to recover on average 0.7% of the company's fleet-wide computing resources. These are company results in a preprint, but the mathematical constructions can be checked independently. A follow-up paper with the mathematician Terence Tao applied the system to 67 problems; it "rediscovered the best known solutions in most cases and improved on them in several" [@georgiev2025mathematical]. That paper was released as a preprint in November 2025 and published in *PNAS* in 2026.

Computing itself has also been a target. In 2023 DeepMind's AlphaDev used reinforcement learning to discover short sorting routines that outperformed the human-written ones; they were added to the LLVM standard C++ sort library, a widely used open-source component [@mankowitz2023faster]. The pattern is the same as in FunSearch: a precisely defined goal, an automatic way to score attempts, and a search far larger than any human could run.

Claims about open problems need particular care. In October 2025, OpenAI staff posted that GPT-5 had found solutions to ten "open" problems from a website that collects problems posed by the mathematician Paul Erdős. The site's maintainer, Thomas Bloom, called this "a dramatic misinterpretation": "open" on his site meant only that he did not know of a solution, and the model had located existing papers [@bastian2025leading]. Most of the posts were deleted. The episode showed a real strength (searching a scattered literature) presented as a different one (solving problems).

In January 2026, by contrast, Erdős problem #728 was described in a preprint as "the first Erdős problem ... regarded as fully resolved autonomously by an AI system". The proof came from a combination of OpenAI's GPT-5.2 Pro and Harmonic's Aristotle system, operated by Kevin Barreto, and was checked in Lean [@sothanaphan2026resolution]. Even here the details matter. The problem as Erdős and his co-authors stated it was ambiguous and had trivial solutions. The site's maintainer judged that the AI proof answered a tightened version, "the question in the spirit it was intended" [@bloom2026erdos], and closely related earlier work by Pomerance was identified afterwards [@tao2026ai]. Tao, commenting on the result, warned against over-reading it. As reported, he noted that Erdős problems vary in difficulty "by several orders of magnitude" and that many were never seriously studied [@bastian2026terence]. Failures are rarely reported, so success rates are unknown. Formal verification settles whether a proof is correct. It does not settle whether the problem was important or how often the method fails.

## 6.5 Automating research: "AI scientist" systems and AI-written code

The systems so far each do one job inside a human-led project. A newer line of work tries to automate the whole loop. The best documented is The AI Scientist, developed by the Tokyo company Sakana AI with researchers at the University of British Columbia and the University of Oxford. Its first version was released as a preprint in August 2024 [@lu2024ai]. It generated research ideas in machine learning, wrote and ran the code, produced figures, wrote a full paper and reviewed it, at a cost of less than 15 US dollars per paper.

In early 2025 the team ran an experiment with the agreement of organisers of a workshop at ICLR, a major machine-learning conference. They submitted three papers generated end to end by the second version of the system, without telling reviewers which papers were AI-written. Two were not accepted. One received scores of 6, 7 and 6, above the workshop's average acceptance threshold, and was withdrawn before publication as agreed in advance. The company noted that workshop papers face a lower bar than main conference papers, and that its own researchers judged none of the three good enough for the main conference [@sakana2025ai].

The peer-reviewed account appeared in *Nature* in March 2026. It reports that the generated manuscript "passed the first round of peer review" for a workshop with an acceptance rate of 70%. The abstract also names a risk: such systems could end up "taxing overwhelmed review systems and adding noise to the scientific literature" [@lu2026towards]. According to the company's summary, an automated reviewer built by the team agreed with human accept/reject decisions with a balanced accuracy of 69%. The system still produces naive ideas, struggles with methodological rigour, makes errors such as inaccurate citations, and is limited to computational experiments. The developers say they watermark the papers the system generates so that they can be identified as AI-written, and they call on the scientific community to set norms for how such work should be treated [@sakana2026ai]. Whether journals and conferences will accept AI-generated papers, and with what disclosure, remains an open question.

Kosmos, from the company Edison Scientific, takes a different design, described in a preprint that has not yet been peer reviewed [@mitchener2025kosmos]. Given a research objective and a dataset, it runs for up to 12 hours, alternating between a data-analysis agent and a literature-search agent that share a structured record of what has been found. In an average run it executes about 42,000 lines of code and reads about 1,500 papers. Independent scientists judged 79.4% of the statements in its reports to be accurate. Accuracy was 85.5% for data-analysis statements and 82.1% for literature statements, but only 57.9% for statements that synthesise and interpret findings. One of its reported findings, in materials science, reproduced a human result about perovskite solar cells: that humidity during a manufacturing step strongly affects their performance. That result was available at the time only in a preprint that Kosmos had not accessed.

The Kosmos authors also tried to estimate how much work a run replaces. Counting papers read and analyses run, and assuming fixed times per task, they estimated about 4.1 months of expert work per run. Collaborating academic groups, asked directly, estimated that the findings of a 20-cycle run would have taken them about 6 months on average, from a sample of seven [@mitchener2025kosmos]. Such estimates are informative but soft. They come from the developers and their collaborators, and the time needed to check the output is not subtracted.

The Kosmos numbers point to a general feature of AI-assisted research. The parts that can be checked mechanically (did the code run, does the cited paper say this) are the parts where the system is most reliable. Interpretation, the step where a scientist decides what a result means, is where it is least reliable, and it is also the step that readers most need to trust.

Much of modern science is computation, and coding assistants (Chapter 5) are now used to write research software. Kosmos writes tens of thousands of lines per run, and AlphaEvolve is itself a coding agent. In a blog post, the software engineer Addy Osmani uses the term **comprehension debt** for "the growing gap between how much code exists in your system and how much of it any human being genuinely understands" [@osmani2026comprehension]. In a commercial product, unread code is a maintenance problem. In research, the code *is* part of the method. If nobody has read the analysis script, nobody can say with confidence what was measured.

## 6.6 Reproducibility, understanding and intellectual debt

Machine learning brought its own reproducibility problems to science before generative AI arrived. Kapoor and Narayanan surveyed fields that had adopted machine-learning methods [@kapoor2023leakage]. They found **data leakage**, in which information from the test data seeps into training so that performance looks better than it is, in 17 fields, affecting 294 papers. They also reanalysed political-science studies that predicted the onset of civil wars. Complex models had appeared to beat traditional statistics by a wide margin; once the errors were corrected, they did "not perform substantively better than decades-old" logistic regression models. The authors proposed "model info sheets", a checklist on which authors document how they guarded against each type of leakage.

The cases in this chapter suggest that AI-assisted claims are only as strong as the check that follows them, and checks differ in strength. A Lean proof is checked completely by a machine. A weather forecast is checked against reality within days, thousands of times a year. A predicted crystal is checked only when a skilled chemist makes and examines it, which happens for a small fraction of candidates and can take years, as the A-Lab case showed. An AI-written paper is checked by peer reviewers who are already overloaded. The inner ring of Figure 6.1 marks these checks. Where verification is cheap, AI accelerates science; where it is expensive, AI mainly accelerates the production of claims.

One response is to make checking part of the method: Kapoor and Narayanan's model info sheets [@kapoor2023leakage], proofs submitted with a Lean certificate [@sothanaphan2026resolution], or labelling AI-generated papers so that reviewers know what they are reading [@sakana2026ai]. Another is to value independent reanalysis. The critiques of GNoME and the A-Lab came from researchers outside both projects, and they changed what the published record says [@cheetham2024artificial; @leeman2024challenges; @szymanski2026author]. A third is to report the denominator. A system that is tried on 67 problems and improves 'several' tells us more than a single announced success, which is why the Tao collaboration's report on all 67 problems it attempted is useful [@georgiev2025mathematical].

Messeri and Crockett argue that the danger goes beyond individual errors. AI tools, they write, can exploit human cognitive limits and create **illusions of understanding**, in which "we believe we understand more about the world than we actually do". They describe three such illusions. An *illusion of explanatory depth* arises when researchers who use an AI model of a phenomenon believe they understand the phenomenon more deeply than they do. An *illusion of exploratory breadth* arises when they believe they are testing all hypotheses but are testing only those that AI tools can handle. An *illusion of objectivity* arises when they treat an AI system as having no point of view, when it reflects the standpoints of its training data and its developers. The cumulative risk, they argue, is a **scientific monoculture** in which some methods and questions crowd out others, so that science may "produce more but understand less" [@messeri2024artificial].

The legal scholar Jonathan Zittrain gave a related idea a name in 2019. He observed that in some fields useful techniques have been used for decades before anyone could explain why they work. This approach, "answers first, explanations later", accrues what he calls **intellectual debt**. Debt is not always bad; borrowing lets us use what works before we know why. But debt compounds: sometimes it is paid off quickly, and sometimes we end up relying for decades on knowledge that is not fully understood. Zittrain warned that machine learning greatly expands our capacity to borrow, because it produces accurate predictions without the theories that would tell us when to stop trusting them [@zittrain2019hidden]. The weather results in Section 6.2 are a case in point. A model that forecasts well on average can fail on the unprecedented storm, and without a theory of what the model has learned, it is hard to know in advance where that boundary lies.

::: {.box .debate}
**Debate: Will AI make science faster but shallower?**

*Faster and deeper.* Supporters point to cases where AI output led to new understanding. AlphaFold's structures are used to form and test hypotheses, and its developers received a Nobel Prize [@royal2024nobelchemistry]. FunSearch and AlphaEvolve return programs that mathematicians can read and generalise [@romeraparedes2024mathematical; @georgiev2025mathematical]. Lean-checked proofs leave little room for error in the reasoning, provided the formal statement says what was intended [@sothanaphan2026resolution]. On this view, freeing scientists from routine work gives them more time to think, and Tao has described AI as most valuable, for now, as a time-saving assistant [@bastian2025leading].

*Faster but shallower.* Critics point to the asymmetry between generating and checking. GNoME produced hundreds of thousands of candidates, and the expert scrutiny needed to assess them took years [@cheetham2024artificial; @szymanski2026author]. Kosmos is least accurate exactly when it interprets [@mitchener2025kosmos]. Messeri and Crockett warn that the most AI-friendly questions may crowd out others [@messeri2024artificial], and Zittrain that unexplained answers accumulate as debt [@zittrain2019hidden].

*What the evidence would need to show.* Few studies measure understanding directly. Useful evidence would include the share of AI-generated findings in a field that are later independently replicated. It would also include whether fields that adopt AI heavily narrow the range of questions and methods they study, and whether researchers using AI tools can explain their results as well as those who do not. None of these has yet been measured at scale.
:::

In weather forecasting, mathematics and parts of computing, AI systems have produced results that are checkable and useful. The common thread in the successful cases is a strong external check: blind competitions for protein structures, daily verification against the weather, formal proof for mathematics, and benchmarks for algorithms. Where such a check was missing, as in the materials and Erdős cases, early claims needed later correction.

## Summary
- Machine learning does four distinct jobs in science: prediction, emulation of expensive simulations, search over candidate solutions, and automation of research workflows. How easily each kind of output can be checked matters as much as the model itself.
- Most showcase results come from two companies and were often first reported by them; independent evaluations and critiques are needed to judge them.
- AlphaFold, which predicts a protein's 3D structure from its sequence, is the reference case: a large archive of checked data, a clear target and blind testing. Its developers shared the 2024 Nobel Prize in Chemistry, and independent comparisons confirm that its predictions are very useful hypotheses that still need experimental checks.
- Machine-learning weather models such as GraphCast, GenCast, ECMWF's AIFS and NOAA's AI models match or beat physics-based forecasts on most measures reported by their developers at a fraction of the computing cost. Independent studies find that they miss small-scale detail and peak winds; they still depend on physics-based data assimilation and can fail on extremes absent from their training data.
- In materials science, GNoME proposed millions of candidate crystals, but independent experts found little evidence of novel, credible and useful materials, and the A-Lab's synthesis claims were corrected in 2026 after reanalysis.
- Mathematics offers machine-checkable proof. AI systems went from silver-medal olympiad performance with days of computation (2024) to certified gold-medal performance in natural language (2025), although independent grading of public models' proofs in 2025 found much weaker results. Search systems such as FunSearch and AlphaEvolve have improved some best-known constructions.
- "AI scientist" systems now produce complete papers and long analyses. Published evaluations show they are most reliable on checkable steps (code, citations) and least reliable on interpretation.
- Data leakage, unread AI-written code and slow expert verification threaten reproducibility. Messeri and Crockett's "illusions of understanding" and Zittrain's "intellectual debt" describe the risk that science produces more while understanding less.

## Key terms
emulator · numerical weather prediction · reanalysis · ensemble forecast · autoregressive rollout · data assimilation · graph neural network · proof assistant · formal verification · AI scientist system · comprehension debt · data leakage · illusions of understanding · scientific monoculture · intellectual debt

## Discussion questions
1. Table 6.1 reports results published by the developers of each weather model, while Bonavita and the Storm Ciarán study evaluated some of the same models independently. What do the two kinds of evidence each show, and what further evidence would you want before concluding that AI models are better than physics-based forecasts?
2. Compare the GNoME and AlphaEvolve announcements. Both claim discoveries found by search. What kind of check was available for each result, who carried it out, and how long did it take?
3. Kosmos statements were 85.5% accurate for data analysis but 57.9% accurate for interpretation. What does this pattern suggest about how such a system should be used in a research group?
4. Apply Messeri and Crockett's three illusions of understanding to a field you know (for example economics, history or engineering). Which illusion seems most likely to arise there, and why?
5. One AI Scientist paper scored above the acceptance threshold of a workshop that accepts 70% of submissions, and was then withdrawn as agreed. What does this result show about the system, and what does it not show? Propose a disclosure rule for AI-generated submissions and justify it.
6. Is intellectual debt always a problem? Give one example where using an unexplained but accurate prediction seems justified, and one where it does not.

## Further reading
- Messeri, L. & Crockett, M. J. (2024). *Artificial intelligence and illusions of understanding in scientific research*. The clearest framework for thinking about the epistemic risks of AI in research, written for scientists in every field. [@messeri2024artificial]
- Lam, R. et al. (2023). *Learning skillful medium-range global weather forecasting*. A readable account of how a machine-learning weather model is built and how it is evaluated against operational forecasts. [@lam2023learning]
- Bonavita, M. (2024). *On some limitations of current machine learning weather prediction models*. A short independent assessment of what headline skill scores leave out; useful to read alongside Lam et al. [@bonavita2024some]
- Cheetham, A. K. & Seshadri, R. (2024). *Artificial intelligence driving materials discovery?* A short, constructive model of how domain experts should scrutinise a large AI discovery claim. [@cheetham2024artificial]
- Kapoor, S. & Narayanan, A. (2023). *Leakage and the reproducibility crisis in machine-learning-based science*. Shows, with a worked reanalysis, how easily machine-learning results in science can be overstated. [@kapoor2023leakage]
- Lu, C. et al. (2026). *Towards end-to-end automation of AI research*. The peer-reviewed description of the AI Scientist, including its limitations and the authors' own discussion of risks. [@lu2026towards]
- Zittrain, J. (2019). *The hidden costs of automated thinking*. A short essay that introduces the idea of intellectual debt for a general audience. [@zittrain2019hidden]


# Chapter 7: Chips, Data Centres, Energy and Open Models

::: {.objectives}
**After working through this chapter you should be able to:**

- explain why modern AI depends on specialised chips and on a small number of firms that design, make and equip them;
- describe how US export controls on advanced chips developed between 2022 and 2026, and evaluate the arguments about their effects;
- interpret International Energy Agency (IEA) projections of data-centre electricity use, including what the scenarios do and do not tell us;
- compare the benefits and risks of releasing open-weight models, using the evidence on both sides;
- apply the idea of compute governance to a national "sovereign AI" strategy.
:::

The government of Alberta, a Canadian province, set out to attract data centres. Requests to connect new data centres to its grid soon reached 16 gigawatts (GW), more than the province's entire peak electricity demand. In 2025 the grid operator imposed a temporary cap of 1.2 GW to protect the reliability of the system [@iea2026key, sec. 3]. A gigawatt is a measure of power: roughly the output of one large power station. The episode shows something that is easy to miss when AI is experienced as text on a screen. Every answer from a chatbot is computed on physical machines, in buildings that draw electricity from real grids, using chips made in a handful of factories.

This chapter is about that physical and industrial base. It starts with the chips themselves and the supply chain that produces them, then turns to the export controls that have made chips an instrument of foreign policy. It then examines the electricity and water used by data centres, the cost of training large models and the concentration of the industry in a few firms. The second half of the chapter turns to open-weight models, whose release is one of the main counterweights to that concentration, and closes with the ways governments try to steer AI through its hardware.

## 7.1 Why AI runs on special chips

Chapter 2 explained that training a neural network consists mostly of multiplying large tables of numbers (matrices) together, millions or billions of times. A conventional central processing unit (CPU), the general-purpose chip in a laptop, is designed to carry out a long sequence of varied instructions quickly, one after another. Matrix multiplication is different: it consists of a vast number of simple, independent multiplications that can be done at the same time. A graphics processing unit (GPU) contains thousands of small arithmetic units that work in parallel, which is why chips first designed to draw video-game graphics turned out to suit neural networks.

A CPU is like a small team of expert chefs who can cook any dish in sequence. A GPU is like a large canteen kitchen where hundreds of assistants each chop one vegetable at the same moment, and the canteen wins when the job is a mountain of identical chopping. The analogy breaks down because a GPU's "assistants" are also fed by very fast memory, and that memory, more than raw arithmetic, often limits speed in practice.

GPUs are one kind of **AI accelerator**, a chip specialised for the arithmetic of machine learning. Others were designed from the start for neural networks. Google's Tensor Processing Unit (TPU) has been deployed in its data centres since 2015. A 2017 paper by Google's engineers reported it to be on average about 15 to 30 times faster than the contemporary GPUs and CPUs it was compared with, and 30 to 80 times more efficient per watt [@jouppi2017indatacenter]. Those comparisons used Google's own inference workloads, and later GPU generations narrowed the gap. The paper nonetheless illustrates why large companies have invested in custom silicon.

Accelerators do not work alone. The data they process sits in **high-bandwidth memory (HBM)**: stacks of memory chips placed close to the processor so that numbers can move in and out quickly. The leading HBM makers are SK Hynix and Samsung of South Korea and Micron of the United States [@sajadieh2026ai, ch. 1]. Thousands of accelerators must also exchange data constantly during training, which requires high-speed networking between servers. The same report estimates that worldwide AI computing capacity grew about 3.3 times a year from 2022 to 2025. It reached roughly 17.1 million "H100-equivalents", a unit based on one of Nvidia's main data-centre chips. Nvidia chips accounted for over 60% of that capacity, with Google and Amazon supplying much of the rest and Huawei holding a small but growing share. Because the estimate is inferred from revenue data and analyst reports, the AI Index itself describes it as indicating trends rather than exact counts.

The commercial weight of this demand is visible in Nvidia's accounts. In its fiscal year ending January 2026, the company reported revenue of $215.9 billion, of which sales to the data-centre market contributed $193.7 billion, up from $47.5 billion two years earlier [@nvidia2026form]. Hardware efficiency has also improved: leading chips deliver roughly ten times more computation per watt than those of a decade ago. Models have grown faster than efficiency, however, so the total power needed to train frontier systems has kept rising [@sajadieh2026ai, ch. 1].

## 7.2 The semiconductor supply chain and its chokepoints

A chip passes through several specialised industries before it reaches a data centre, and each stage is dominated by very few firms. Figure 7.1 shows the stack, from the machines that make chips at the bottom to the applications people use at the top.

![Figure 7.1: The AI supply chain as a stack. Each layer depends on the one below, and several layers are dominated by one or a few firms (named examples are illustrative, not exhaustive). Chokepoints such as extreme-ultraviolet lithography and leading-edge fabrication are where governments have focused export controls. Diagram by the author, based on @sajadieh2026ai and @asml2026annual.](../figures/svg/fig-07-01.svg){#fig:07-01}

At the base are the **lithography** machines that print circuit patterns onto silicon wafers using light. The most advanced chips require extreme-ultraviolet (EUV) lithography, and ASML, a Dutch company, states in its 2025 annual report that it is "currently the world's only manufacturer of EUV lithography systems" [@asml2026annual]. Above that sits **fabrication**, the manufacture of the chips in plants called fabs. Firms such as Nvidia and AMD design chips but do not make them; they send their designs to foundries, chiefly the Taiwan Semiconductor Manufacturing Company (TSMC) and Samsung. According to the 2026 AI Index, TSMC "fabricates virtually every leading AI chip", including Nvidia's Blackwell GPUs and AMD's MI300X, which makes it a single point of dependency for the whole industry [@sajadieh2026ai, ch. 1]. A TSMC expansion in the United States began operating in 2025, but the AI Index still describes the global AI hardware supply chain as dependent on one foundry in Taiwan.

After fabrication, chips are **packaged**: the processor and its HBM stacks are joined on a single base so that they can communicate quickly. Packaging and testing are done by specialist companies such as ASE Group in Taiwan and Amkor Technology in the United States [@sajadieh2026ai, ch. 1]. Nvidia's own filings list TSMC and Samsung as its wafer suppliers and SK Hynix, Micron and Samsung as its memory suppliers [@nvidia2026form]. Every layer has, in the AI Index's words, "high barriers to entry", requiring decades of expertise, specialised equipment and large capital investment.

Concentration creates fragility. The IEA reported in April 2026 that a shortage of HBM had developed over the previous six months and was expected to last "through at least the end of 2027" [@iea2026key, Executive Summary]. The same report described how a conflict in the Middle East in 2026 disrupted supplies of helium from Qatar, which had supplied roughly a third of the world's helium. Helium is used to cool and clean chip-making equipment and has, according to the IEA, no substitute with equivalent properties [@iea2026key, Box 1.1]. A disruption far from any data centre can thus slow the supply of AI hardware.

::: {.box .concept}
**Key concept: Chokepoint**

A chokepoint is a stage in a supply chain that very few suppliers control and that others cannot easily replace. In AI hardware, the clearest examples are EUV lithography (one supplier) and leading-edge chip fabrication (mainly one foundry). Chokepoints give whoever controls them leverage, which is why export controls target them, and they create shared vulnerability, because a single fire, shortage or conflict can delay production worldwide.
:::

## 7.3 Export controls and the geopolitics of compute

The supply chain is concentrated, and its most important firms are based in the United States or in allied countries. This has allowed the US government to use **export controls** to limit which countries can obtain advanced AI chips and chip-making tools. An export control is a legal requirement to obtain a government licence before selling certain goods abroad. The US rules are written by the Commerce Department's Bureau of Industry and Security (BIS). Figure 7.2 summarises the main steps.

![Figure 7.2: Main US export-control measures on advanced AI chips and related items, October 2022 to July 2026. The direction of policy changed in 2025: rules continued to restrict China, while the global licensing framework of January 2025 was abandoned before it took full effect and replaced by country-by-country arrangements. Source: @bis2022implementation; @bis2023implementation; @bis2024foreignproduced; @bis2025framework; @bis2025department; @nvidia2025form; @bis2026revision; @bis2026enhanced.](../figures/svg/fig-07-02.svg){#fig:07-02}

The first major rule, issued on 7 October 2022, imposed licence requirements on advanced computing chips, on computers containing them and on certain chip-manufacturing equipment, mainly aimed at China [@bis2022implementation]. Chip designers responded by offering China-specific products designed to comply with the rules, as Nvidia's filings describe [@nvidia2026form]. An update in October 2023 revised the controls to "more effectively achieve" their aims [@bis2023implementation]. Nvidia told investors that the revised rule required licences for exports to China and several other countries of chips including the A100, A800, H100 and H800, judged by "total processing performance and/or performance density" [@nvidia2023form]. In December 2024 BIS added further controls on chip-making equipment and, for the first time, on certain high-bandwidth memory [@bis2024foreignproduced].

In January 2025 the outgoing Biden administration published a broader **Framework for Artificial Intelligence Diffusion**. It extended licence requirements for advanced chips to most of the world and sorted countries into tiers with different levels of access. It also added a new control on the weights of certain advanced closed-weight AI models [@bis2025framework]. The rule's compliance date was 15 May 2025. Two days before it, on 13 May, the new administration announced that it would rescind the rule and instructed officials not to enforce it. It argued that the rule "would have stifled American innovation" and would have downgraded dozens of countries "to second-tier status" [@bis2025department]. On the same day BIS warned companies about the risks of using certain Huawei Ascend chips and about the use of US chips to train Chinese models. A replacement rule was promised. In July 2026 the worldwide licence requirement still appeared in the regulations, but BIS stated that it was enforcing it only for certain destinations, mainly countries of concern such as China [@bis2026enhanced].

Policy towards China itself moved in both directions. In April 2025 the US government informed Nvidia that its H20 chip, a product designed for the Chinese market, now required an export licence. The company expected charges of up to about $5.5 billion on inventory and commitments [@nvidia2025form]. In January 2026 BIS changed its review policy for exports to China of the more powerful H200 and equivalent chips from a "presumption of denial" to "case-by-case review". The change came with conditions, such as independent testing in the United States and certification that US supply would not be reduced [@bis2026revision]. Nvidia reported, for its part, that the Chinese government had discouraged customers from buying its data-centre products, including those designed to comply with US rules [@nvidia2026form]. Meanwhile, the United States offered favourable access to some partners: a July 2026 rule gave the United Arab Emirates' government and approved companies licence-free access to advanced computing items [@bis2026enhanced].

Whether these controls achieve their aims is contested. Supporters point to evidence that Chinese developers are short of compute: the IEA describes China's model developers as "compute-constrained due to a lack of access to high-end chips" [@iea2026key, Box 10.1]. Critics note that constraints can spur workarounds. DeepSeek trained its V3 model on a cluster of 2,048 Nvidia H800 GPUs, a chip that could be exported to China without a licence until the October 2023 update [@deepseekai2024deepseekv3; @nvidia2023form]. The IEA observes that Chinese developers responded to scarcity with a strong focus on techniques that reduce computation. The 2026 AI Index reports that the performance gap between the best US and Chinese models "has effectively closed", with the lead changing hands several times since early 2025 [@sajadieh2026ai, Report highlights]. Neither observation settles the question, because nobody can observe what Chinese labs would have achieved without the controls.

## 7.4 Data centres, electricity and water

A **data centre** is a building that houses servers, networking equipment, power supplies and cooling systems. Not all data centres serve AI: most of their electricity still goes to ordinary cloud computing, streaming, storage and business software. Few operators publish measured figures for their AI workloads, so most numbers in this section are estimates. They come from public agencies, from independent researchers and from the companies themselves, and their methods and boundaries often differ. The most systematic global estimates come from the IEA, an intergovernmental energy agency. It published a special report, *Energy and AI*, with global and regional projections in April 2025 [@iea2025energy], and an update, *Key Questions on Energy and AI*, in April 2026 [@iea2026key].

According to the 2026 update, global data-centre electricity consumption grew by 17% in 2025, reaching 485 terawatt-hours (TWh) [@iea2026key, Executive Summary]. A terawatt-hour is a billion kilowatt-hours; for scale, 485 TWh was about 1.5% of the world's electricity use. Consumption by data centres that focus on AI grew faster, by about 50%. The IEA's central projection, its Base Case, sees total data-centre consumption roughly doubling to about 950 TWh by 2030 (945 TWh in the report's data tables). That would be around 3% of global electricity demand, with AI-focused data centres tripling their use [@iea2026key, Executive Summary and Annex A].

Figure 7.3 shows these figures together with the IEA's alternative scenarios. The IEA uses four "cases" because the future depends on uncertain factors: how fast AI is adopted, how quickly chips and models become more efficient, and whether bottlenecks in grids, turbines and chips ease. The Lift-Off Case assumes stronger adoption and resolved bottlenecks. The High Efficiency Case assumes the same demand as the Base Case but faster efficiency gains, and the Headwinds Case assumes slower adoption and investment [@iea2026key, sec. 1]. The spread for 2030, from 833 to 1,008 TWh, is a reminder that these are projections under assumptions, not forecasts of a single outcome. The IEA adds a further caution: the queue of proposed data centres is a poor guide to future demand, because only "a limited and uncertain share" of it may be built.

![Figure 7.3: Global data-centre electricity consumption, 2023–2025 (IEA estimates), and 2030 under four IEA cases. Data centres used about 1.5% of the world's electricity in 2025; the Base Case reaches about 3% by 2030. Source: @iea2026key, Annex A, Table A.1 (data published April 2026).](../figures/svg/fig-07-03.svg){#fig:07-03}

The global share is modest, but the local share can be large. The IEA notes that data centres, while using 1.5% of global electricity in 2025, accounted for as much as 20–30% of demand in the states, metropolitan areas or regions where they cluster [@iea2026key, sec. 3]. Ireland is the clearest national case: official statistics show that data centres consumed 23% of the country's metered electricity in 2025, up from 5% in 2015 [@cso2026data]. The growth is also concentrated geographically. In the IEA's tables the United States accounts for 183 of the world's 416 TWh in 2024, and for 426 of 945 TWh in the 2030 Base Case. China rises from 102 to 277 TWh and Europe from 68 to 114 TWh [@iea2026key, Table A.4]. Figure 7.4 compares these regions.

![Figure 7.4: Data-centre electricity consumption by region, 2024 and 2030 (IEA Base Case). The United States and China account for most of the projected growth. "Rest of world" is the world total minus the three named regions. Source: @iea2026key, Annex A, Table A.4 (data published April 2026).](../figures/svg/fig-07-04.svg){#fig:07-04}

The IEA's figures for the United States can be set beside an independent national estimate. In December 2024 Lawrence Berkeley National Laboratory published a report for the US Department of Energy. It estimated that US data centres used 176 TWh in 2023, about 4.4% of the country's electricity, up from 58 TWh in 2014. It projected 325 to 580 TWh by 2028, or roughly 6.7 to 12% of US electricity [@doe2024doe]. The 2023 estimate is close to the IEA's 183 TWh for 2024, which gives some confidence in the starting point. The projected range, however, has a top almost twice its bottom. Independent estimates therefore agree on rapid growth while disagreeing widely on its size.

Efficiency per task and total demand are moving in opposite directions. The IEA estimates that the energy used per AI task has fallen "by at least an order of magnitude annually in recent years" [@iea2026key, Executive Summary]. A simple text query now typically uses less electricity than running a television for the same length of time. Yet new uses such as video generation, reasoning models and agents can consume "hundreds or thousands of times more energy per query" than simple text generation. Total demand therefore depends on the race between efficiency and uptake. Physical density is rising too. The power density of AI servers increased elevenfold between 2020 and 2025, and by 2027 a single server rack the size of a large refrigerator could have peak demand equal to that of 65 households.

The balance between training and use is also shifting. Training a model is a one-off cost, while answering users' queries (inference) continues for as long as the model is in service. The 2026 AI Index notes that once a model is deployed at scale, the cumulative energy needed to serve queries "can exceed the one-time cost of training within months" [@sajadieh2026ai, ch. 1]. It cites estimates that a short GPT-4o query uses about 0.42 watt-hours, compared with about 0.3 watt-hours for a conventional web search: small for one person, large when multiplied by hundreds of millions of queries a day. Such figures are estimates by outside researchers, who must model other firms' systems because most developers do not publish measurements. Seen against the whole economy, the IEA expects data centres to account for slightly less than 10% of the growth in global electricity demand to 2030, although some regions are much more affected [@iea2026key, sec. 1].

Company measurements and independent ones differ in what they count. In August 2025 Google published measurements from its own serving infrastructure, in a paper by its staff released as a preprint. According to the company, the median text prompt to its Gemini Apps used 0.24 watt-hours in May 2025, and energy per prompt had fallen 33-fold in a year [@elsworth2025measuring]. Google's count included idle machines and cooling overhead, which narrower methods leave out, but it covers one firm's median prompt and cannot be checked from outside. Independent measurements on openly available models show how much the type of task matters. In a peer-reviewed study, Luccioni, Jernite and Strubell found that generating images used on average more than 60 times as much energy as generating text [@luccioni2024power]. No single "energy per query" figure therefore describes AI as a whole.

Estimates made before the IEA's work illustrate how difficult projection is. In 2023 Alex de Vries, a PhD candidate at the Vrije Universiteit Amsterdam, estimated from expected AI server production that by 2027 AI could add 85 to 134 TWh a year to worldwide electricity consumption. He also estimated that if every Google search used AI, it might need about as much electricity as Ireland (about 29 TWh a year) [@devries2023growing]. These were scenario calculations in a short commentary, not forecasts, and they helped prompt the more detailed modelling that followed.

Where the electricity comes from matters for emissions. The IEA reports that the tech sector signed around 40% of all corporate renewable power-purchase agreements worldwide in 2025 [@iea2026key, Executive Summary]. Agreements between data-centre operators and planned small modular nuclear reactors grew from about 25 GW to 45 GW during 2025, although the first such reactors are not expected before about 2030. In the United States, where grid connections are slow, some developers are building gas-fired generation on site; the IEA estimates that 15–27 GW of such capacity might power data centres by 2030. The IEA projects that emissions associated with data centres will roughly double, reaching around 350 million tonnes in 2035, which would still be about 2% of the electricity sector's emissions.

Company emissions figures depend on an accounting choice. **Market-based** emissions subtract the clean electricity a company has contracted to buy, while **location-based** emissions use the average carbon intensity of the grids that actually supply its buildings. Google's 2025 environmental report shows how far apart the two can be. According to the company, its data-centre electricity use grew by 27% in 2024 while its data-centre energy emissions, counted on the market basis, fell by 12% [@google2025environmental, p. 18]. In the report's data tables, its market-based emissions from purchased electricity were about 3.1 million tonnes of carbon dioxide equivalent in 2024. The location-based figure was about 11.3 million tonnes, more than double its 2019 level [@google2025environmental, p. 104]. Both numbers follow recognised rules; they answer different questions, and headlines usually quote the lower one.

**Water** is the less visible resource. Data centres use water mainly for cooling, often by evaporation, and indirectly through the water used to generate their electricity. Two terms are important. **Withdrawal** is water taken from a source; **consumption** is the part that is not returned, mostly because it evaporates. @li2025making estimated that training GPT-3 in Microsoft's US data centres could have directly evaporated about 700,000 litres of fresh water. Counting both cooling water and water used in generating electricity, they projected that global AI demand might account for 4.2 to 6.6 billion cubic metres of water withdrawal in 2027. The authors stress that such estimates depend heavily on location, season and the electricity mix. The 2026 AI Index reports estimates that a year of GPT-4o inference consumes about 1.3 to 1.6 million cubic metres of water. At the high end, that exceeds the annual drinking-water needs of 1.2 million people [@sajadieh2026ai, ch. 1].

Company reports provide measured totals, although for whole companies rather than for AI alone. Google reported consuming about 31 billion litres of water across its own data centres and offices in 2024, an increase of 28% on 2023. It said that 72% of its freshwater withdrawals came from sources at low risk of depletion. It also chose air cooling, which uses little water, for a new site at Waltham Cross in England because local water sources were under stress [@google2025environmental]. Its per-prompt study put the water consumed by a median Gemini text prompt at 0.26 millilitres, about five drops [@elsworth2025measuring]. That figure counts only cooling water at Google's own data centres, whereas Li and colleagues also count the water used to generate electricity. Differences of boundary like this explain much of the gap between company and outside estimates. Both kinds of figure show that the water question is mostly local: the same litre matters more in a drought-prone basin than beside a large river.

## 7.5 Who can afford frontier AI? Costs and concentration

Chapter 4 described how the computation used to train leading models has grown. Here the question is what that growth costs and who can pay. In a preprint, @cottier2024rising, researchers at Epoch AI and Stanford, estimated the cost of training frontier models by spreading the price of the hardware over its useful life and adding the energy used (Going deeper box below). On this basis the cost of the most compute-intensive training runs had grown about 2.4 times a year since 2016. GPT-4 had the largest amortised hardware and energy cost in their data set, at about $40 million, and Google's Gemini Ultra about $30 million. In their fuller breakdown of development costs, accelerator chips and staff were the largest components, with energy only 2–6%. If the trend continued, the largest training runs would cost more than a billion dollars by 2027, a level the authors argue would limit frontier development to the best-funded organisations.

Training also has an environmental cost that varies with hardware, duration and the carbon intensity of the electricity used. The AI Index estimates that training AlexNet in 2012 produced about 0.01 tonnes of carbon dioxide equivalent. Training xAI's Grok 4 in 2025 produced about 72,816 tonnes, while DeepSeek's V3, a large model trained more efficiently, produced about 597 tonnes [@sajadieh2026ai, ch. 1]. These are model-based estimates, made necessary because, as the Index notes, many developers no longer disclose power use for their newest models.

These figures cover only the final training run. Staff, failed experiments and the often larger cost of serving a model to users are additional, and the 2026 AI Index notes that frontier developers now disclose less about their models than before [@sajadieh2026ai, Introduction]. Building the infrastructure costs far more. According to the IEA, leading cloud providers (the "hyperscalers") and newer specialised providers announced capital expenditure of about USD 715 billion for 2026, a 75% increase [@iea2026key, sec. 1]. That is more than the slightly less than USD 600 billion invested in the entire US energy sector in 2024. Because this spending absorbs nearly all the firms' cash, they are turning increasingly to borrowing, which makes the build-out sensitive to financial markets.

The result is concentration. The AI Index reports that industry produced 91.2% of notable AI models in 2025 (93 models against 2 from academia), with OpenAI (20), Google (14) and Alibaba (11) the most prolific developers [@sajadieh2026ai, ch. 1]. By country, the United States produced 59 notable models and China 35. On the supply side, Nvidia reported that two direct customers alone accounted for 22% and 14% of its total revenue in fiscal year 2026 [@nvidia2026form]. The United States hosts 5,427 data centres, more than ten times any other country, followed by Germany (529), the United Kingdom (523) and China (449) [@sajadieh2026ai, ch. 1]. Concentration of this kind matters because a few firms' choices about pricing, access, safety practices and openness then shape what everyone else can build.

::: {.box .deeper}
**Going deeper: Estimating the cost of a training run**

The simplest estimate multiplies the time a run takes on its chips by a price per chip-hour:

*cost ≈ number of GPU-hours × rental price per GPU-hour*

DeepSeek reported that the full training of its V3 model took 2.788 million H800 GPU-hours. Assuming a rental price of $2 per GPU-hour, it calculated a cost of 2,788,000 × $2 = $5.576 million [@deepseekai2024deepseekv3]. The company stated explicitly that this excludes "the costs associated with prior research and ablation experiments". Cottier et al. use a different method [@cottier2024rising]. They take the purchase price of the hardware, divide it over the hardware's expected working life and charge the training run for the share of that life it used, then add energy. The two methods answer different questions. A rental-price estimate asks what it would cost someone to repeat the final run; an amortised estimate asks what share of a lab's capital the run consumed. Neither includes salaries, data or failed attempts, which is why headline training costs understate what it takes to build a frontier model.
:::

::: {.box .case}
**Case study: The "DeepSeek moment", January 2025**

In late December 2024 the Chinese company DeepSeek released the weights of DeepSeek-V3, a model with 671 billion parameters (37 billion active for each token), and reported the $5.576 million final-run cost described above [@deepseekai2024deepseekv3]. In January 2025 it released DeepSeek-R1, a reasoning model, under the permissive MIT licence, together with smaller "distilled" versions built on Alibaba's Qwen and Meta's Llama models [@deepseekai2025deepseekr1]. DeepSeek's chatbot app rose to the top of Apple's app store in the US and UK. On Monday 27 January 2025 Nvidia's shares fell 17%, removing nearly $600 billion from its market value, as investors questioned whether frontier AI would need as many expensive chips as expected [@milmo2025sputnik].

Later evidence complicated the story. The R1 work was published in *Nature* in September 2025. Its supplementary information gave the cost of turning the V3 base model into R1 as about 147,000 H800 GPU-hours, or about $294,000 at the same assumed $2 rental price. That figure covers the two reinforcement-learning stages plus the creation of fine-tuning data. It also acknowledged using A100 GPUs for preparatory experiments [@guo2025deepseek]. The low headline figures were therefore real but partial: they excluded earlier research and the company's existing hardware. Nvidia's Data Center revenue continued to grow strongly through 2025 [@nvidia2026form]. The episode showed that algorithmic efficiency can reduce the cost of matching the frontier, and it drew wide attention to Chinese open-weight models; it did not show that compute had stopped mattering.
:::

## 7.6 Open-weight models

A trained model is, in the end, a very large file of numbers: its **weights** (also called parameters). A **closed-weight** model is kept on the developer's servers, and users reach it only through an app or an application programming interface (API), so the developer can monitor use, update the model and withdraw it. An **open-weight** model is one whose weights are published for anyone to download, run on their own hardware and modify, for example by further training ("fine-tuning") on their own data. Chapter 3 introduced the distinction; this section examines its consequences.

::: {.box .concept}
**Key concept: Open-weight is not the same as open source**

In software, "open source" means that the source code is available under a licence allowing anyone to use, study, modify and share it for any purpose. For AI, the Open Source Initiative's Open Source AI Definition (version 1.0, October 2024) requires those freedoms plus access to the parameters and the full training code. It also requires information about the training data detailed enough for a skilled person to build a substantially equivalent system [@osi2024open]. Many "open" models release only weights under a custom licence. Meta's Llama 2 licence, for example, required any company whose products had more than 700 million monthly active users to request a separate licence from Meta [@meta2023llama]. "Open-weight" is therefore the more accurate general term.
:::

The modern wave of open-weight language models began in earnest when Meta released Llama 2 in July 2023, describing it as "free of charge for research and commercial use" [@meta2023meta]. In September 2023 the French start-up Mistral AI released Mistral 7B, a 7.3-billion-parameter model, under the permissive Apache 2.0 licence, claiming it outperformed the larger Llama 2 13B on all the benchmarks it reported [@mistral2023mistral]. Chinese developers became central to the open ecosystem, as Alibaba's Qwen family and DeepSeek's models were widely adopted. The IEA reports that in 2025 "China's models overtook those from developers in the United States in terms of total downloads on open-source platforms" [@iea2026key, Box 10.1]. In August 2025 OpenAI released two open-weight reasoning models, gpt-oss-120b and gpt-oss-20b, under Apache 2.0 [@openai2025gptoss].

How good are open models compared with closed ones? The AI Index tracks the gap on the Arena leaderboard, where people compare anonymous answers from two models and vote for the better one. In May 2023 the best closed model led the best open model by 174 points (15.2%); by August 2024 the gap had narrowed to 7 points (0.5%). By March 2026, after new closed reasoning models, it had widened again: Claude Opus 4.6 scored 1,503 points against 1,454 for GLM-5, a gap of 49 points (3.4%) [@sajadieh2026ai, ch. 2]. On this measure the best open models trail the best closed ones by a small margin, although the gap has widened and narrowed as new models appear.

The most cited framework for weighing benefits and risks is by @kapoor2024position, 25 researchers from academia, industry and civil society. They identify five properties that distinguish open models, such as greater customisability and weak monitoring of use, and argue that these produce benefits for innovation, competition, transparency and the distribution of decision-making power. Researchers can inspect open weights, which closed models do not allow. Businesses and governments can run models on their own computers without sending sensitive data to a vendor, and developers in countries without frontier labs can adapt models to local languages. The US government's 2025 AI Action Plan made similar points, adding that open models "have geostrategic value" because they may become global standards [@whitehouse2025winning].

The risks follow from the same properties. Once weights are published they cannot be recalled, and any safety training can be removed. In a preprint, @lermen2023lora showed that with "a budget of less than $200 and using only one GPU" they could fine-tune Meta's Llama 2-Chat 70B. Afterwards it refused harmful requests only about 1% of the time on two standard tests. Kapoor and colleagues argue that the key question is **marginal risk**: how much an open model adds to what a malicious actor could already do with search engines, existing tools or closed models. They found that "current research is insufficient to effectively characterize the marginal risk" across most misuse scenarios.

Applying their framework to seven earlier studies of misuse, @kapoor2024position judged that six did not, on their own, show an increased marginal risk. Their own worked examples point in both directions. For automated searches for software vulnerabilities, they judged the marginal risk of open models to be low at present, partly because defenders can use the same tools. For digitally altered intimate images made without consent, they concluded that open image models "pose considerable marginal risk at present". Such models need few resources to run, can be fine-tuned on pictures of specific people, and are hard to police once released. They also cite a 2023 study finding that most computer-generated child sexual abuse material had been made with the openly available Stable Diffusion family of image models. The evidence of marginal risk is therefore uneven: weak or absent for some harms, already documented for others.

::: {.box .debate}
**Debate: Should the weights of the most capable models be released openly?**

*For openness by default.* @kapoor2024position argue that open models spread power beyond a few companies, enable independent safety research and support competition, and that most claimed misuse risks have not been shown to exceed those of existing technologies. In July 2024 the US National Telecommunications and Information Administration concluded that "current evidence is not sufficient to definitively determine" that restrictions on open-weight models were warranted. It recommended that government "actively monitor" risks instead [@ntia2024dual]. Tests of particular releases have so far found limited added capability. Before releasing gpt-oss in 2025, OpenAI fine-tuned it to be as capable as possible in biology and cyber-security. According to the company's preprint, even this version performed below OpenAI's closed o3 model, which it had judged to be under its own "High" risk threshold, and did not substantially advance the frontier of open models [@wallace2025estimating]. That is a developer's evaluation of its own product, without independent replication.

*For caution at the frontier.* In a preprint, @seger2023opensourcing accept that open-sourcing has historically brought large net benefits. They argue, however, that for some highly capable future models the risks may be extreme enough that such models "should not be open-sourced, at least not initially". They examine alternatives, such as ways of sharing models without publishing their weights. The ease of removing safety training supports their concern that release decisions are irreversible [@lermen2023lora]. Harms from open image models are already documented, which shows that marginal risk is not only hypothetical [@kapoor2024position].

*Evidence that could decide it.* Both sides agree that the answer depends on marginal risk at particular capability levels. Independent evaluations of what open models add to specific harms, repeated as models improve, would let decisions rest on measured risk rather than on assumptions or on developers' own tests. Chapter 12 discusses such dangerous-capability evaluations.
:::

Open-weight models also interact with the rest of this chapter. They lower the cost of entry for firms and countries that cannot afford frontier training, which partly offsets concentration. They also complicate export controls: the January 2025 diffusion rule controlled the weights of certain advanced closed-weight models but left published weights outside its scope, because published information cannot be recalled [@bis2025framework].

## 7.7 Compute governance and sovereign AI

Data and algorithms are hard to observe and easy to copy, so some researchers argue that hardware is an especially practical lever for governing AI. In a preprint, @sastry2024computing, a group of 19 authors including Yoshua Bengio, argue that AI-relevant compute is a good point of intervention. It is, they write, "detectable, excludable, and quantifiable" and is produced through "an extremely concentrated supply chain". Detectable means that large data centres and chip shipments are hard to hide; excludable means that access can be denied; quantifiable means that chips and computations can be counted. **Compute governance** is the use of these properties by public authorities to gain visibility into AI development, allocate resources and enforce rules.

Examples already exist. Export controls are one. Another is the use of training compute as a regulatory threshold. The EU AI Act presumes that a general-purpose AI model has "high impact capabilities", and is therefore subject to additional obligations, when the computation used for its training exceeds 10^25 floating-point operations [@europeanparliament2024regulation, Art. 51(2)]. Chapter 13 discusses these thresholds and their limits in detail. Sastry and colleagues also warn that poorly designed compute governance carries risks to privacy, economic harms and an undesirable centralisation of power. They propose guardrails such as collecting only the minimum information needed.

The same logic of control over compute underlies **sovereign AI**, the effort by governments to secure national access to AI infrastructure and models rather than depending entirely on foreign providers. The 2026 AI Index notes that "AI sovereignty emerged as a central organizing principle" in national policies during 2025 [@sajadieh2026ai, Introduction]. Strategies differ in scale and emphasis:

- **European Union.** In February 2025 the European Commission launched InvestAI, aiming to mobilise €200 billion for AI investment, including a €20 billion fund for four "AI gigafactories", each with around 100,000 of the latest AI chips [@ec2025eu].
- **India.** In March 2024 the Indian cabinet approved over Rs 10,300 crore over five years for the IndiaAI Mission, including a plan for public–private compute capacity of more than 10,000 GPUs [@pib2024cabinet].
- **United Kingdom.** The AI Opportunities Action Plan of January 2025 recommended expanding the country's public AI Research Resource "by at least 20x by 2030" and creating "AI Growth Zones" to speed up data-centre construction. It also noted that sovereign compute would "almost certainly be the smallest component" of the country's total compute [@dsit2025ai].
- **United States.** The July 2025 AI Action Plan called for exporting the "full AI technology stack" (hardware, models, software, applications and standards) to allied countries, so that they would not become dependent on rivals' technology [@whitehouse2025winning].

The scale differences are large. US private AI investment reached $285.9 billion in 2025, against $12.4 billion in China, although the AI Index cautions that the Chinese figure omits much state funding [@sajadieh2026ai, Report highlights]. A single country's public programme of 10,000 GPUs is small next to the 17.1 million H100-equivalents of global capacity estimated in Section 7.1. For most countries, then, "sovereignty" means securing reliable access, building local data centres, or adapting open-weight models to national languages and needs. Training a frontier model from scratch remains out of reach.

Sovereign strategies also interact with the chokepoints described in Section 7.2. A country can build data centres on its own soil and still depend on Nvidia's designs, TSMC's fabs and ASML's machines. Those dependencies are shaped by US export policy, as the UAE arrangement of 2026 illustrates [@bis2026enhanced]. Open-weight models offer a partial route to independence at the model layer. That is one reason why governments as different as the United States and China have, for their own reasons, encouraged them [@whitehouse2025winning; @iea2026key, Box 10.1]. The physical layers of the stack are harder to replicate, and they are where the decisions of a few firms and governments continue to set the terms for everyone else.

## Summary

- Modern AI runs on accelerators such as GPUs and TPUs, which perform many simple calculations in parallel and depend on fast high-bandwidth memory; Nvidia supplies over 60% of estimated global AI compute.
- The chip supply chain contains severe chokepoints: ASML is the only maker of EUV lithography machines, and TSMC fabricates virtually every leading AI chip.
- Since October 2022 the United States has used export controls to restrict China's access to advanced chips; the 2025 global diffusion rule was abandoned before it took full effect, and in 2026 policy shifted to case-by-case licensing for some chips and favourable deals with partners. Their effectiveness is debated.
- The IEA estimates that data centres used 485 TWh (about 1.5% of world electricity) in 2025 and projects about 950 TWh (about 3%) by 2030 in its Base Case, with a range of 833–1,008 TWh across its cases. An independent US estimate (176 TWh in 2023; 325–580 TWh by 2028) shows similar growth and a similarly wide range. Local impacts, as in Ireland, can be much larger.
- Per-query energy, emissions and water figures depend on who measures and what is counted: company measurements and outside estimates use different boundaries, and Google's location-based electricity emissions in 2024 were more than three times its market-based figure. Water use is mainly local and mainly for cooling, and estimates vary widely with location, season and method.
- Training costs for the largest runs have grown about 2.4-fold a year, and infrastructure spending by a few cloud providers runs to hundreds of billions of dollars, concentrating frontier development in industry and in a few firms.
- Open-weight models (Llama, Mistral, Qwen, DeepSeek, gpt-oss) trail the best closed models by a small margin and spread access widely, but their release is irreversible and their safety training can be removed cheaply. Evidence of their marginal risk is uneven: low so far for some uses, already documented for altered intimate images.
- Compute governance uses the detectability and concentration of hardware to regulate AI, and sovereign AI strategies seek national access to compute, usually by building infrastructure and adapting open models rather than training frontier systems.

## Key terms

AI accelerator · graphics processing unit (GPU) · high-bandwidth memory (HBM) · EUV lithography · foundry · chokepoint · export control · data centre · terawatt-hour (TWh) · water withdrawal and consumption · amortised training cost · open-weight model · marginal risk · compute governance · sovereign AI

## Discussion questions

1. Google reports 0.24 watt-hours for a median Gemini text prompt, while outside researchers estimate 0.42 watt-hours for a short GPT-4o query. Identify the differences in model, method and boundary that could explain the gap, and explain why neither figure can confirm the other. What would a company need to disclose for an independent researcher to check its figures?
2. Evaluate the evidence on whether US export controls have slowed AI development in China. What does the DeepSeek case show, and what can it not show?
3. DeepSeek reported a final training cost of $5.576 million for V3, while Cottier et al. estimate amortised costs in the tens of millions for earlier frontier models. Explain why both figures can be correct, and what each leaves out.
4. Apply the idea of marginal risk to a new case: a developer plans to release the weights of a model that is much better than existing open models at writing computer code. What questions would you ask before deciding whether the release adds significant risk?
5. Choose one country's sovereign AI strategy from Section 7.7. Which layers of the stack in Figure 7.1 does it address, and on which layers does it remain dependent on others?
6. A local council is asked to approve a data centre that would add a fifth to the area's electricity demand. Drawing on the IEA's local figures, the Irish statistics and the distinction between market-based and location-based emissions, which figures would you ask the operator to provide, and which would you want verified independently?

## Further reading

- International Energy Agency (2026). *Key Questions on Energy and AI*. The most detailed public analysis of data-centre electricity, with transparent scenarios and data tables. [@iea2026key]
- Sajadieh, S., et al. (2026). *The AI Index 2026 Annual Report*. A data-rich annual overview; its first chapter covers compute, data centres, the supply chain and environmental impact. [@sajadieh2026ai]
- Cottier, B., et al. (2024). *The Rising Costs of Training Frontier AI Models*. A clear explanation of how training costs are estimated and why they have grown. [@cottier2024rising]
- Kapoor, S., et al. (2024). *Position: On the Societal Impact of Open Foundation Models*. The standard framework for weighing the benefits and marginal risks of open-weight models. [@kapoor2024position]
- Seger, E., et al. (2023). *Open-Sourcing Highly Capable Foundation Models*. A careful statement of the case for caution, useful to read alongside Kapoor et al. [@seger2023opensourcing]
- Sastry, G., et al. (2024). *Computing Power and the Governance of Artificial Intelligence*. Explains why hardware is a lever for governing AI, and what could go wrong. [@sastry2024computing]
- Luccioni, S., Jernite, Y. & Strubell, E. (2024). *Power Hungry Processing: Watts Driving the Cost of AI Deployment?* An independent, openly documented measurement of how energy use varies across AI tasks and models. [@luccioni2024power]


```{=html}
<section class="part"><p class="part-label">Part III</p><h1 class="part-title">Society and Economy</h1></section>
```

# Chapter 8: Work, Productivity and the Economy

::: {.objectives}
**After working through this chapter you should be able to:**

- explain how task-based frameworks and exposure measures describe the potential effects of AI on occupations, and why exposure is not the same as job loss;
- compare the design, sample, setting and effect size of the main productivity studies, distinguishing randomised controlled trials from observational and quasi-experimental studies;
- evaluate the early evidence on employment, including the debate about entry-level workers;
- explain why macroeconomic forecasts of AI's effect on growth differ by an order of magnitude;
- assess the arguments about inequality, hidden labour, collective bargaining, deskilling and the policy response.
:::

In the first half of 2025, the research organisation METR ran a randomised trial with 16 experienced open-source software developers, reported in a preprint. Before starting, the developers predicted that AI tools would cut the time they needed for each task by 24%. Economists and machine-learning experts surveyed by the researchers expected savings of nearly 40%. When the 246 tasks were completed and timed, the tasks on which AI was allowed had taken 19% *longer* than those on which it was not. Even after the study, the developers believed that AI had made them faster [@becker2025measuring].

Two years earlier, a widely cited experiment had found the opposite pattern. Professionals given ChatGPT for writing tasks finished them 40% faster, and their work was rated 18% better [@noy2023experimental]. Both studies were randomised. Both measured time carefully. A likely reason for the different answers is that they studied different people doing different tasks with different generations of tools.

This chapter is about how to read evidence like this. It moves from the frameworks economists use, through experiments, adoption, jobs and wages, and macroeconomic forecasts, to the hidden workers behind AI, collective bargaining, inequality, deskilling and policy. Throughout, the design of each study matters as much as its headline number.

## 8.1 Thinking in tasks: exposure and its limits

Economists who study technology and work no longer treat a job as a single unit that a machine either does or does not replace. Instead they break each occupation into **tasks**: the specific activities a worker performs, such as drafting a letter, checking an invoice or calming an angry customer. In the framework developed by @acemoglu2019automation, automation lets machines take over some tasks that people used to do. This has a *displacement effect*, which lowers the demand for labour in those tasks. At the same time, new technologies create new tasks in which people have the advantage, a *reinstatement effect* that raises labour demand. Whether a technology helps or hurts workers overall depends on the balance between the two.

The reinstatement effect is not a theoretical curiosity. Using eight decades of US census data, @autor2024new find that the majority of current employment is in job specialties introduced since 1940. The same study finds, however, that the demand-reducing effect of automation innovations has grown stronger since 1980, while the demand-raising effect of augmentation innovations has not. History therefore offers some reassurance, but it does not show that new work will always arrive quickly enough or in the right places.

### Measuring exposure

To estimate which jobs AI might affect, researchers construct **exposure measures**. These score each occupation by how many of its tasks a given technology could, in principle, perform or speed up. Exposure is a measure of technical potential, not of adoption or effects.

Two families of measures are widely used. @felten2021occupational built the AI Occupational Exposure (AIOE) index before the arrival of large language models. It links ten AI applications to the human abilities that the US occupational database O\*NET uses to describe more than 800 occupations. When the authors adjusted the index to emphasise language modelling in a 2023 preprint, the most exposed occupations included telemarketers and university teachers of English, foreign languages and history [@felten2023language].

@eloundou2023gpts took a more direct approach. Human annotators and the model GPT-4 rated each O\*NET task by whether access to a large language model (LLM) could reduce the time needed to complete it, at equivalent quality, by at least half. In this preprint, they estimated that about 80% of the US workforce could have at least 10% of their tasks affected, and about 19% of workers could have at least half of their tasks affected.

The same study separated the model from the software around it. With an LLM alone, about 15% of all US worker tasks could be done significantly faster at the same quality. With software built on top of LLMs, that share rose to roughly half [@eloundou2023gpts]. A shorter version of the analysis was published in *Science* in 2024 [@eloundou2024gpts].

International organisations have produced similar estimates. An International Monetary Fund staff note from January 2024 found that almost 40% of global employment is exposed to AI. Exposure was highest in advanced economies (about 60%) and lowest in low-income countries (26%) [@cazzaniga2024genai]. The note added that, in advanced economies, roughly half of the exposed jobs might benefit from AI while the other half might be negatively affected.

A refined index from the International Labour Organization (ILO) and Poland's NASK research institute, published in May 2025, gives lower figures. It put the share of global employment in potentially exposed occupations at 25%, and at 34% in high-income countries [@gmyrek2025generative]. Announcing the index, the ILO concluded that "transformation, not replacement, is the most likely outcome" [@ilo2025one].

::: {.box .concept}
**Key concept: Exposure**

An occupation's exposure to AI is an estimate of the share of its tasks that AI could technically perform or speed up. A high exposure score is compatible with very different outcomes: the job may disappear, shrink, grow or simply change. A map of where rain *could* fall says little about whether a particular farmer's crops will thrive, which depends on irrigation, soil and timing. An exposure score says even less, because it is not a forecast at all: it contains no information about timing, cost or adoption.
:::

### Why exposure is only the first step

Exposure measures share three weaknesses. First, they rely on judgements, by people or by models, about what AI can do, and those judgements date quickly. Second, they describe tasks in isolation, whereas real jobs bundle tasks together in ways that may make some hard to separate. Third, and most importantly, they cannot tell whether AI will substitute for a worker or complement one. A tool that drafts legal documents might reduce demand for junior lawyers, or it might make legal services cheap enough that demand for them grows.

Figure 8.1 sets out the chain of steps between technical potential and economic outcomes. The figure also shows where the evidence becomes thinner: exposure is easy to estimate for every occupation, whereas causal evidence on wages and employment exists for only a few settings.

![Figure 8.1: From exposure to economic outcomes. Exposure measures estimate what AI could do; adoption determines whether it is used; task-level productivity effects determine what happens when it is used; and firm decisions translate those effects into employment, wages and output. Evidence becomes scarcer at each step. Diagram by the author.](../figures/svg/fig-08-01.svg){#fig:08-01}

## 8.2 What experiments show about productivity

The strongest evidence about cause and effect comes from **randomised controlled trials (RCTs)**, in which participants or tasks are assigned by chance to use AI or not. Many other studies are **observational**: they compare people or firms who adopted AI with those who did not. Some observational studies are **quasi-experimental**, exploiting a natural source of variation, such as a staggered roll-out, to approximate an experiment. These designs can be convincing, but they rest on assumptions that an RCT does not need.

::: {.box .concept}
**Key concept: Randomised and observational evidence**

In a randomised controlled trial, a coin-toss decides who receives the treatment, so the treated and untreated groups are alike on average in every respect except the treatment. In an observational study, people or firms choose for themselves, so any difference in outcomes may reflect who chose rather than what they chose. In medicine, comparing patients who chose a new drug with those who did not may mostly reveal differences between the patients. The analogy has a limit: even an RCT in economics measures the effect only for its particular sample, task and tool, and that effect may not carry over to other settings.
:::

### Writing and professional tasks

@noy2023experimental ran a preregistered online experiment with 453 college-educated professionals, each given occupation-specific writing tasks with financial incentives for good performance. Half were randomly given access to ChatGPT. Average time taken fell by 40% and output quality, as rated by evaluators, rose by 18%. Inequality between workers fell, because the weaker writers gained most. The tasks were short and self-contained, which is both a strength (they are easy to measure) and a limitation (much real work is neither short nor self-contained).

### Customer support

A widely cited field study looked at a real workplace rather than a laboratory. @brynjolfsson2025generative studied the introduction of an AI assistant at a Fortune 500 firm selling business software, whose customer-support agents answered technical questions by online chat. The design was quasi-experimental: access was rolled out to different agents at different times, mainly between late 2020 and early 2021. The researchers used a **difference-in-differences** method. They compared the change in performance of agents who gained access with the change, over the same period, for agents who had not yet gained it. The case study below describes the setting and the results.

::: {.box .case}
**Case study: An AI assistant in a customer-support centre**

The firm's support agents, 89% of whom were based outside the United States and mainly in the Philippines, answered chats from small and medium-sized US businesses. The assistant, built on GPT-3 and fine-tuned by a third-party company, suggested responses and links to documentation in real time; agents decided whether to use them [@brynjolfsson2025generative]. Across 5,172 agents, access raised the number of issues resolved per hour by 15% on average.

Most of the gain went to the weakest performers. The least skilled fifth of agents gained about 36%. For the most skilled, gains were not statistically significant, and their conversation quality declined slightly. Agents with two months' tenure who had the assistant performed about as well as agents with more than six months' tenure who did not. Customers were also more polite and less likely to ask for a manager. Because the study is not a randomised trial, its conclusions depend on the assumption that the timing of access was unrelated to other changes in agents' performance; the authors test this assumption with several alternative estimators. Section 8.6 considers what the agents' location means for reading these results.
:::

### Consulting work and the "jagged frontier"

@dellacqua2026navigating ran a preregistered experiment with 758 knowledge workers at the consulting firm Boston Consulting Group, first circulated as a working paper in 2023 and published in *Organization Science* in 2026. After a baseline task, participants were randomly assigned to work without AI, with GPT-4, or with GPT-4 plus a short training in writing prompts. On a set of 18 realistic consulting tasks chosen to lie within the capabilities of the AI, those using AI completed 12.2% more tasks, worked 25.1% more quickly and produced work of significantly higher quality. On a different task, selected to lie *outside* those capabilities, consultants using AI were 19% less likely to produce a correct solution than those without it.

The authors coined the term **jagged technological frontier** to describe this pattern. AI's capabilities do not decline smoothly as tasks become harder for humans. Instead, AI may excel at one task and fail at another that looks similar in difficulty. Workers who cannot see where the frontier lies may trust the tool exactly where it is weakest.

### Software development

Software is the most-studied occupation, partly because output can be measured automatically. In an early experiment, @peng2023impact recruited 95 freelance programmers through the platform Upwork in 2022 and randomly gave 45 of them access to GitHub Copilot, a code-completion tool; 50 formed the control group. The task was to write a simple web server in JavaScript. Among those who completed it, the treated group finished 55.8% faster. The 95% confidence interval, the range of effects consistent with the data at conventional levels of statistical confidence, ran from 21% to 89% faster. This paper is a preprint and the task was a short, standardised exercise.

A larger study, published in *Management Science* in 2026, analysed three field experiments run by Microsoft, Accenture and an anonymous Fortune 100 company as part of their normal business [@cui2026effects]. The authors pooled 4,867 developers, a random subset of whom were given access to Copilot for between two and eight months. They estimated that using the tool increased the number of completed tasks per week by about 26%, although the estimate is imprecise. Each experiment on its own was noisy, and less experienced developers both adopted the tool more and gained more from it.

The METR trial described at the start of this chapter points in the other direction [@becker2025measuring]. Its setting differed in important ways. The 16 participants were experienced developers working on mature open-source projects that they had contributed to for an average of about five years, and the tools were early-2025 systems such as Cursor and Claude 3.5/3.7 Sonnet. The confidence interval around the 19% slowdown ran from +2% to +39%, so even the most favourable estimate consistent with the data was a small slowdown. The sample was small.

METR then ran a follow-up study beginning in August 2025, with 57 developers and more than 800 tasks. Ten developers returned from the first study; for them the estimated effect was an 18% *speed-up*. For the 47 new recruits it was a 4% speed-up. Neither estimate was statistically distinguishable from zero [@metr2026changing].

METR itself judged that the new data were an unreliable signal. Between 30% and 50% of developers said they had not submitted some tasks because they did not want to do them without AI, and some developers declined to take part at all for the same reason. Selection of this kind makes the estimates hard to interpret. METR concluded that developers were probably sped up more in early 2026 than in early 2025, but that its data were "only very weak evidence" of how much [@metr2026changing].

### When AI advice makes things worse

Most experiments find average gains concentrated among weaker performers. A field experiment in Kenya found a different pattern [@otis2026uneven]. Small-business owners were randomly assigned either to receive access to a GPT-4-based AI business assistant or to a control group. There was no statistically significant average effect on revenues or profits. Entrepreneurs who were already performing well appear to have gained, by more than 15% in subsample analyses, whereas those who were performing poorly did nearly 10% worse. The authors traced the difference to the advice that entrepreneurs chose to implement; the questions they asked and the advice they received were similar across the two groups.

### Reading the evidence together

Figure 8.2 places these results side by side. Estimated effects on task time range from a 56% reduction to a 19% increase, so any single headline number hides more than it reveals. The largest gains appear in short, well-defined tasks and among less experienced workers; the smallest gains, or losses, appear among experts working on complex tasks in contexts they know well. And the tools change faster than studies can be published: the Copilot of 2022, the GPT-4 of 2023 and the coding agents of 2026 (see Chapter 5) are different technologies.

![Figure 8.2: Estimated effects of AI assistance in selected studies, with data collected between 2020 and 2025. Panel A shows changes in the time needed to complete tasks (negative values mean faster work); Panel B shows changes in output (positive values mean more output). Bars show 95% confidence intervals where the study reports them. Studies differ in design, sample, task and tool, so the estimates are not directly comparable. Source: @noy2023experimental; @peng2023impact; @becker2025measuring; @metr2026changing; @brynjolfsson2025generative; @dellacqua2026navigating; @cui2026effects.](../figures/svg/fig-08-02.svg){#fig:08-02}

## 8.3 Adoption: who uses AI, and for what

A tool can only affect productivity if people use it. Measuring adoption turns out to be surprisingly difficult, because the answer depends on whom you ask (workers or firms), how you phrase the question, and whether you count occasional or intensive use. Table 8.1 summarises some of the main measures.

### Worker surveys

@bick2024rapid ran a series of nationally representative surveys of US adults aged 18 to 64. In the revised version of their working paper (February 2025), they report that by late 2024 nearly 40% of this population used generative AI. Among employed respondents, 23% had used it for work at least once in the previous week, and 9% used it every working day. Relative to the launch of the first mass-market product, workplace adoption had been as fast as that of the personal computer, and overall adoption faster than that of either the PC or the internet.

Intensity of use was much lower than these shares suggest. The same surveys imply that only a small fraction of all work hours, between 1% and 5%, were assisted by generative AI. Reported time savings amounted to 1.4% of total work hours [@bick2024rapid].

In Denmark, @humlum2025large linked two large surveys, conducted in late 2023 and 2024, to official employment records in a working paper. Each survey covered about 25,000 workers at 7,000 workplaces in 11 occupations thought to be highly exposed to AI chatbots, including accountants, software developers and customer-support specialists. Most employers encouraged the use of chatbots, and workers reported larger benefits when they did. Yet users reported average time savings of only 2.8% of their work hours, far below the gains found in experiments.

### Firm surveys

The US Census Bureau's Business Trends and Outlook Survey (BTOS) regularly asks firms whether they use AI. Until late 2025, the question asked about AI used in *producing goods or services*; by late 2025, about 10% of firms said yes, double the rate of mid-2024. From November 2025 the question was broadened to AI use in *any business function*, and in early 2026 about 20% of firms reported use [@garcialuna2026ai]. Changes in question wording like this are a reminder that adoption figures are rarely comparable across surveys.

A special AI supplement to the BTOS, covering November 2025 to January 2026, gives a more detailed picture [@bonney2026microstructure]. In that period 18% of firms used AI in a business function, or 32% when firms are weighted by employment, because large firms adopt more often. Among very large firms in information, professional services and finance, use reached about half or more.

The same supplement shows how shallow most adoption still was. Most adopters used AI in only a few functions, most commonly sales and marketing. Two-thirds of users relied on AI only to augment tasks, and very few firms (2%) reported that AI had led to a fall in employment [@bonney2026microstructure].

### Usage data from AI companies

A third source is data from AI providers themselves. Anthropic, the developer of the Claude models, publishes an "Economic Index" based on privacy-preserving analysis of conversations with its models. Its first report, a preprint by company researchers analysing over four million conversations, found that software development and writing together accounted for nearly half of usage. Slightly more usage suggested augmentation of human work (57%) than automation [@handa2025which].

Later reports separated consumer from business use. According to the company's January 2026 report, based on samples of one million consumer conversations and one million business transcripts from November 2025, consumer conversations were split almost evenly between augmentation (52%) and automation. About three-quarters of business (API) interactions, in which companies connect the model directly to their own software, were classified as automation [@anthropic2026economic].

These data describe real use at very large scale, but only for one company's products and customers. The classifications of "automation" and "augmentation" are made by a language model and describe conversation patterns, not effects on jobs. A June 2026 report linked usage to a survey of about 9,700 users, but computer and mathematical occupations made up about 30% of respondents, compared with 4% of US employment, so the respondents were far from representative [@massenkoff2026anthropic].

| Source (data period) | Population | Measure | Reported value |
|---|---|---|---|
| Bick, Blandin & Deming (late 2024) | US adults aged 18–64 | Use generative AI | nearly 40% |
| Bick, Blandin & Deming (late 2024) | US employed adults | Used it for work in previous week | 23% |
| Census BTOS (late 2025) | US firms | Use AI to produce goods or services | about 10% |
| Census BTOS (early 2026) | US firms | Use AI in any business function | about 20% |
| Census BTOS AI supplement (Nov 2025–Jan 2026) | US firms | Use AI in a business function | 18% (32% weighted) |
| Humlum & Vestergaard (late 2023 and 2024) | Danish chatbot users in 11 exposed occupations | Average time saved | 2.8% of work hours |
| Anthropic Economic Index (Nov 2025) | Claude.ai conversations | Classified as augmentation / automation | 52% / 45% |

: Table 8.1: Selected measures of AI adoption in the United States and Denmark, 2024–2026. Each row gives the population surveyed, the question asked and the reported share. Differences in wording and population explain much of the variation between sources. The BTOS question changed in November 2025, so rows 3 and 4 are not directly comparable. Anthropic figures are company data and describe conversation patterns, not effects on jobs. Source: @bick2024rapid; @humlum2025large; @garcialuna2026ai; @bonney2026microstructure; @anthropic2026economic.

## 8.4 Jobs and wages: the evidence so far

Even if AI raises productivity in particular tasks, its effect on jobs and wages depends on how firms respond. They might employ fewer people, keep the same staff and produce more, or move workers into new tasks. Nearly four years after the launch of ChatGPT, the evidence is still early and partly conflicting.

### Little sign of economy-wide disruption

Several studies find no detectable effect on the labour market overall. The Danish study described above compared adopters and non-adopters before and after chatbots became available, and also used variation in employers' policies as a quasi-experiment. In its May 2025 version, it found "precise zeros": confidence intervals ruled out average effects on earnings or recorded hours larger than 1% [@humlum2025large]. A revised version, issued in March 2026 under a new title, again found precise null effects two years after ChatGPT's launch, ruling out effects larger than 2%. It also documented that adopters were moving into new tasks and better-paid occupations [@humlum2025still].

In the United States, researchers at the Yale Budget Lab measured how fast the mix of occupations changed in the 33 months after ChatGPT's release. They compared it with earlier periods of technological change, such as the spread of computers and the internet [@gimbel2025evaluating]. They found that the occupational mix was changing somewhat faster than in the past, but that the difference was small and had begun before generative AI arrived. Measures of exposure, automation and augmentation showed "no sign of being related to changes in employment or unemployment". The authors stressed that past technologies took decades to transform workplaces.

### Early-career workers

A different picture emerges when researchers look at young workers. In a working paper using high-frequency payroll data on millions of workers from ADP, a large US payroll processor, @brynjolfsson2026canaries document what they call "six facts". The August 2026 version of the paper uses data up to June 2026. By then, employment of workers aged 22 to 25 in the most AI-exposed occupations stood 19% below where it would have been had it kept pace with less-exposed young workers. Measured the same way with data up to July 2025, the gap had been 15%. Experienced workers showed no comparable gap. The adjustment came mainly through reduced hiring rather than layoffs, and was concentrated in occupations where AI is mostly used to automate tasks; where AI mostly complements workers, employment was flat or rising.

A separate working paper using résumé data on 65 million workers at more than 280,000 US firms found a related pattern [@hosseinimaasoum2025generative]. After firms posted job advertisements for staff to integrate generative AI, a signal of active adoption, junior employment at those firms fell sharply relative to non-adopting firms, while senior employment changed little. Again the decline came mainly through slower hiring.

Job advertisements suggest that entry-level work is being redesigned as well as reduced. The consulting firm PwC analysed more than one billion job advertisements for its 2026 *Global AI Jobs Barometer*. According to the firm, the US entry-level roles most exposed to AI were now seven times more likely to require skills traditionally expected of senior staff, such as leadership, creativity or face-to-face interaction [@pwc2026global]. These are correlations in advertisement data, and they do not show what caused the change.

::: {.box .debate}
**Debate: Is AI already reducing entry-level hiring?**

*Yes, probably in some occupations.* In the August 2026 version of their working paper, @brynjolfsson2026canaries find a 19% employment gap for 22- to 25-year-olds in the most exposed occupations, in payroll data up to June 2026. The gap had been 15% in data up to July 2025, so it has widened, and it is concentrated where AI substitutes for tasks. The gap persists when technology firms are excluded and when the authors control for interest-rate exposure and remote work. Firm-level résumé data show junior employment falling after firms adopt generative AI [@hosseinimaasoum2025generative].

*Not yet clearly.* @brynjolfsson2026canaries themselves describe their results as "descriptive patterns, not causal estimates". The gap shrinks when education is controlled for, some differences predate generative AI, and the gap is larger in the ADP sample than in national surveys. Economy-wide measures show no discernible disruption [@gimbel2025evaluating], and Danish administrative data rule out effects on earnings and hours larger than 2% [@humlum2025still]. Another possibility is that young workers are affected by slower overall hiring for reasons unrelated to AI.

*What would settle it:* data linking firms' actual AI use to their hiring decisions over several years, ideally with a source of variation in adoption that is unrelated to the firms' other circumstances, and replication in other countries.
:::

## 8.5 The macroeconomic picture: why forecasts differ

If AI raises productivity in many tasks, the economy as a whole should eventually grow faster. Forecasts of how much faster vary widely. In 2023, in research published by the investment bank Goldman Sachs, its economists estimated that generative AI could raise global GDP by 7%, almost $7 trillion, and lift productivity growth by 1.5 percentage points over a ten-year period [@goldmansachs2023generative].

@acemoglu2025simple reached a much smaller number. He used a task-based model with existing estimates of exposure and task-level cost savings. On that basis, AI would raise total factor productivity (TFP), the part of output growth not explained by more capital or labour, by no more than 0.66% *in total* over ten years. He then argued that even this might be too high. Early evidence comes from easy-to-learn tasks, whereas many future applications will involve hard tasks with no clear measure of success; his adjusted estimate was less than 0.53% over ten years. The two forecasts use different measures (labour productivity and TFP), but the gap between them is still large: roughly 1.5 percentage points of extra annual productivity growth against roughly 0.05 to 0.07 percentage points a year.

A company estimate lies near the optimistic end of this range. Anthropic's January 2026 report, using its own data, estimated that AI could add about 1.8 percentage points to annual labour productivity growth over the next decade, or about 1.0 point once task success rates are taken into account [@anthropic2026economic]. It is a company's estimate about its own product category.

The forecasts differ mainly because they make different assumptions about three quantities: the share of tasks that AI will affect, the cost savings in each affected task, and how quickly firms will adopt. The Going deeper box shows how these combine. Small changes in each assumption, multiplied together, produce large differences in the result.

::: {.box .deeper}
**Going deeper: The arithmetic behind macro forecasts**

@acemoglu2025simple builds on a result known as Hulten's theorem. In simplified form, it says that the economy-wide productivity gain from a technology is approximately

*aggregate gain ≈ (share of tasks affected) × (average cost saving in those tasks).*

In words: if a technology cuts costs by a certain proportion in a certain share of the economy's tasks, the overall gain is the product of the two. As an illustration only (these are not any author's estimates): if AI were profitably used in 5% of all tasks and cut their costs by 15%, the aggregate gain would be about 0.05 × 0.15 = 0.0075, or 0.75% over the period. If instead it were used in 25% of tasks with savings of 30%, the gain would be 7.5%, ten times larger. Optimistic forecasts typically assume broad adoption and large savings; cautious forecasts rely on the share of tasks where AI is currently cost-effective and on measured savings. The formula also ignores new products and new tasks, which could make the true effect larger, and adjustment costs, which could make it smaller.
:::

### Why productivity statistics may lag

Even if AI eventually raises productivity substantially, official statistics may not show it for some time. @brynjolfsson2021productivity describe a **productivity J-curve**. When firms adopt a general-purpose technology, they must make large complementary investments, for example in reorganising work, training staff and building data systems. These investments are often intangible and poorly measured, so measured productivity growth may at first be *understated*, and later, when the benefits are harvested, *overstated*. For computer hardware and software, they estimated that US total factor productivity was 15.9% higher by the end of 2017 than official measures suggested. The J-curve offers one explanation for the gap between large experimental effects and small effects in the national data, though it is hard to test in real time.

## 8.6 Hidden labour and collective responses

### The work behind the machine

The studies in Section 8.2 treat AI as a tool that workers use. AI systems also depend on workers whom users rarely see. Models are trained and tested on data that people label, and the feedback training described in Chapter 3 relies on human raters who compare and score model outputs. Content moderators review material that users or models produce. Mary Gray and Siddharth Suri call such task-by-task, platform-mediated labour **ghost work**. Their five-year study of on-demand workers in the United States and India argues that many apparently automated services rely on people who are hired, managed and paid through software, often with few of the protections of standard employment [@gray2019ghost].

The best-documented case involves ChatGPT itself. In January 2023 an investigation by *TIME* magazine reported that OpenAI had contracted Sama, an outsourcing firm, to have workers in Nairobi label text describing violence, hate speech and sexual abuse [@perrigo2023exclusive]. The labels were used to build a tool that detects such content, later built into ChatGPT. According to *TIME*, the roughly three dozen workers took home between about $1.32 and $2 an hour, while OpenAI's contracts paid Sama $12.50 an hour; Sama said that this rate covered all its costs. All four workers interviewed said the work had left them mentally scarred, and they described counselling as rare and unhelpful, a claim Sama partly disputed; OpenAI said it took contractors' mental health "very seriously". Sama ended the work in February 2022, eight months early.

Systematic evidence is thinner but points the same way. The Fairwork project at the Oxford Internet Institute scores online labour platforms out of ten against five principles: fair pay, conditions, contracts, management and representation. Its 2023 ratings covered 15 platforms and drew partly on a survey of 752 workers in 94 countries. Only three scored 5; none of the others scored more than 3. Microwork platforms that supply data annotation and model evaluation to AI companies "were among the lowest scores" [@fairwork2023work, p. 2]. The report also notes that most demand for such work comes from clients in the Global North, while most of the workforce is in the Global South.

This labour is largely missing from the measures in Sections 8.1 to 8.4. Exposure indices and productivity studies count the people who use AI, not those whose work goes into building and maintaining it.

### Offshore work and the customer-support study

Geography also matters for reading the best-known field study. In the customer-support case in Section 8.2, 89% of the agents worked outside the United States, mainly in the Philippines, serving small and medium-sized US businesses [@brynjolfsson2025generative]. The study therefore measures AI's effect on outsourced service work in a lower-wage economy, not on a typical American office. Its results may not carry over to workers with different pay, training or language backgrounds.

The finding that new agents with the assistant matched experienced agents without it can be read in two ways. For individual agents, it means faster learning. For a country whose outsourcing industry competes partly on the experience of its workforce, it may also mean that this advantage counts for less. Whether the productivity gain reaches agents as higher pay, or customers and the firm as lower costs, is a question of wage-setting that the study was not designed to answer.

### Collective bargaining

Some workers have responded through their unions. In 2023 the Writers Guild of America (WGA), which represents film and television writers, struck for 148 days [@wga2023what]. The resulting agreement with the studios and production companies, covering 25 September 2023 to 1 May 2026, set rules for AI [@wga2023summary]. AI cannot write or rewrite literary material. AI-generated material does not count as source material, so it cannot be used to undermine a writer's credit or to pay them a lower rewrite fee [@wgaw2026artificial]. A writer may use AI with the company's consent, but the company cannot require it. Companies must disclose when material given to a writer was generated by AI. The Guild also reserved the right to argue that training AI on writers' work is prohibited.

The agreement does not ban the technology; it allocates control over it. Writers may use AI as an aid, but the studios cannot use it to replace the credited writer, a negotiated version of the distinction between augmentation and automation.

Other collective responses are smaller or less tested. In May 2023 more than 150 content moderators and data workers for Facebook, TikTok and ChatGPT met in Nairobi and voted to form a union [@perrigo2023african]. In December 2023 the US union federation AFL-CIO and Microsoft announced a partnership that, according to Microsoft's announcement, includes worker feedback to AI developers and a neutrality framework for future union organising [@microsoft2023aflcio].

## 8.7 Inequality, deskilling and the policy response

### Who gains?

The evidence on whether AI reduces or increases inequality points in more than one direction. Within particular tasks, several studies find that AI narrows gaps between workers. In customer support, the least skilled agents gained most [@brynjolfsson2025generative]; in professional writing, inequality between participants fell [@noy2023experimental]; and in software development, less experienced developers gained more [@cui2026effects]. On this evidence, AI can act as a skill leveller within a task.

Other evidence points the other way. In the Kenyan experiment, AI advice helped strong entrepreneurs and harmed weak ones [@otis2026uneven]. In the economy as a whole, compression *within* a task does not guarantee compression *between* workers, because the value of the task itself may fall. @acemoglu2025simple shows that AI could increase inequality even when it raises the productivity of low-skill workers in some tasks. He finds no evidence that AI will reduce labour-income inequality, and predicts a widening gap between income from capital and from labour. The IMF note similarly warns that higher returns to capital could increase wealth inequality [@cazzaniga2024genai].

Exposure is also unevenly distributed across groups. In high-income countries, according to the ILO–NASK index, jobs in the highest exposure category account for 9.6% of female employment but only 3.5% of male employment [@ilo2025one; @gmyrek2025generative]. The IMF finds that women and college-educated workers are more exposed, but also better placed to benefit, while older workers may find it harder to adapt. Between countries, advanced economies are more exposed but also better prepared to benefit, which could widen global income gaps [@cazzaniga2024genai].

### Deskilling

A separate concern is that relying on AI may erode the skills of the people who use it. The idea is old. In a classic paper on industrial automation, @bainbridge1983ironies identified what she called the "ironies of automation". Automation leaves human operators with the tasks that designers could not automate, including monitoring and taking over when the system fails. Yet "physical skills deteriorate when they are not used" [@bainbridge1983ironies, sec. 1.1.1], so an experienced operator who has spent years watching an automated process may have become an inexperienced one by the time intervention is needed.

Recent evidence from medicine suggests that the same may happen with AI. @budzyn2025endoscopist studied colonoscopies at four endoscopy centres in Poland that had introduced an AI system to help detect precancerous growths (adenomas). In a retrospective, observational analysis of 1,443 colonoscopies performed *without* AI assistance in 2021–2022, the adenoma detection rate fell from 28.4% before the introduction of AI to 22.4% afterwards. The authors concluded that continuous exposure to AI "might" reduce performance in unassisted procedures. Because the study compares periods before and after, it cannot exclude other changes over the same period, and it prompted published correspondence in the same journal. It is best read as an early quantitative signal of deskilling that further studies will need to confirm or refute.

Deskilling matters for the economy as well as for safety. If junior workers no longer perform the routine tasks through which they once learned, the pipeline that produces future experts may narrow. PwC's analysis of entry-level advertisements, described in Section 8.4, is consistent with this concern, though it cannot show it [@pwc2026global]. The effects of AI on learning in education are discussed in Chapter 10.

### The policy response

Governments have so far responded to AI's labour-market effects mainly through existing institutions, with a few targeted rules. The most concrete is the European Union's AI Act, whose wider structure Chapter 13 describes. It classifies as "high-risk" AI systems used to recruit or select workers, to make decisions about promotion or termination, to allocate tasks based on individual behaviour or traits, and to monitor and evaluate workers' performance [@europeanparliament2024regulation, Annex III, point 4]. Employers who deploy such systems must inform workers' representatives and the affected workers before using them at the workplace [@europeanparliament2024regulation, art. 26(7)].

Beyond specific rules, the policy debate turns on a question that the evidence cannot yet answer: should governments try to steer the *direction* of AI development, or wait for clearer evidence of harm? @acemoglu2023can argue for early steering. In a policy memo they contend that the private sector is pursuing a path that emphasises automation and workplace surveillance. Their proposed federal policies include equalising tax rates on employing workers and on owning equipment and algorithms, limiting workplace surveillance, and funding research on technologies that complement human workers. Others put more weight on measuring the effects accurately before acting. The Yale Budget Lab, for example, emphasises that "better data is needed" and has committed to tracking the labour market regularly [@gimbel2025evaluating].

A market-liberal position treats regulation itself as the main risk. The US government's AI Action Plan of July 2025 commits to removing "red tape and onerous regulation" so that AI can spread quickly [@whitehouse2025winning]. Its response to labour-market effects is a "worker-first" agenda built on existing institutions. It promotes AI skills in training and apprenticeship programmes and retraining for displaced workers, and creates an AI Workforce Research Hub in the Department of Labor to study the effects. On this view, the state's task is to help workers move, not to shape the technology.

A union-led position relies on bargaining over particular uses of AI, sector by sector. The writers' agreement in Section 8.6 is the clearest example, and the AI Act's duty to inform workers' representatives gives such bargaining a legal foothold in the EU. It can fit rules to specific tasks, but it reaches only organised workers, which excludes most of the platform workers described in Section 8.6.

Income-support proposals focus on income rather than jobs. @korinek2019artificial show in simple economic models that, under plausible conditions, governments can tax the gains from AI without distorting incentives and use the revenue to compensate those who would otherwise lose. In a 2021 essay, Sam Altman, the chief executive of OpenAI, proposed an "American Equity Fund" that would pay out to every adult citizen. It would be financed by an annual tax of 2.5% on the value of large companies and of land [@altman2021moores]. Direct evidence on what such payments do comes from trials not designed with AI in mind. In one large US experiment, 1,000 low-income people received $1,000 a month for three years and 2,000 received $50 a month [@vivalt2026employment]. The larger payments reduced labour-market participation by 4.2 percentage points and working hours by one to two hours a week. Leisure rose most, and the quality of employment did not improve.

These positions answer different questions. Steering concerns which technologies are built, the market-liberal view how fast they spread, bargaining who controls their use at work, and income support who bears the losses.

## Summary

- Economists analyse AI's effects on work task by task. Automation displaces labour from some tasks, while new tasks reinstate it; the balance determines the overall effect.
- Exposure measures estimate what AI could technically do in each occupation. Estimates range from 25% of global employment (ILO–NASK) to about 40% (IMF), but exposure is not a forecast of job loss.
- Experimental and quasi-experimental studies find large gains in some settings, such as 40% time savings in professional writing (2023) and 15% more resolved issues in an offshore customer-support centre, and slowdowns in others, such as a 19% slowdown for experienced open-source developers in early 2025. Gains are usually largest for less experienced workers and for well-defined tasks.
- Adoption is widespread among individuals but shallower within firms: in late 2025 and early 2026, about 18–20% of US firms reported using AI in a business function, and Danish workers reported average time savings of 2.8% of work hours.
- Economy-wide studies find little effect so far on employment, earnings or hours. Payroll and résumé data show a decline in hiring of young workers in exposed occupations, which the authors describe as descriptive rather than causal. Macroeconomic forecasts differ by more than an order of magnitude because they combine different assumptions about the share of tasks affected, cost savings and adoption speed.
- AI depends on largely hidden human labour, such as data labelling and content moderation, much of it done through poorly rated platforms or outsourcing firms in the Global South; some workers, notably Hollywood writers in 2023, have bargained collectively over how AI is used.
- AI may narrow skill gaps within tasks while widening inequality between workers, between capital and labour, or between countries. Evidence of deskilling is emerging, notably in medicine.
- Policy so far relies mainly on existing institutions plus targeted rules, such as the EU AI Act's treatment of workplace AI as high-risk. Proposals range from steering AI's direction and waiting for better data to deregulation with retraining, sectoral bargaining and income support.

## Key terms

task-based framework · displacement effect · reinstatement effect · exposure measure · randomised controlled trial · observational study · quasi-experiment · difference-in-differences · confidence interval · jagged technological frontier · augmentation · automation (of tasks) · total factor productivity · productivity J-curve · ghost work · deskilling · ironies of automation

## Discussion questions

1. Choose an occupation you know well, such as nursing, teaching or retail management. Break it into at least eight tasks and judge which ones a current AI system could perform or speed up. What does your exercise reveal about the limits of exposure measures?
2. Compare @noy2023experimental and @becker2025measuring. Both are randomised trials, yet they reach opposite conclusions about whether AI saves time. Identify at least three differences in their design, sample, setting or tools that could explain the difference. Which result would you expect to generalise better to your own future work, and why?
3. The study by @brynjolfsson2026canaries is observational and its authors describe it as descriptive. What additional evidence would convince you that AI, rather than other factors, is reducing entry-level hiring?
4. Using the Going deeper box, explain to a non-economist why Goldman Sachs and Daron Acemoglu reached such different forecasts. Which assumptions do you find more plausible for the next ten years?
5. Apply Bainbridge's "ironies of automation" to a new case, such as airline pilots using autopilot, junior lawyers using AI to draft contracts, or students using AI to write essays. What safeguards might reduce deskilling, and what would they cost?
6. Section 8.7 sets out four policy positions: steering the direction of AI, deregulation with retraining, sectoral bargaining, and income support. Take one group of workers discussed in this chapter (offshore customer-support agents, data labellers working through online platforms, or junior software developers) and judge which position's instruments would reach that group, and which would miss it. Which piece of evidence in the chapter most affects your answer, and how strong is it?

## Further reading

- Acemoglu, D. & Restrepo, P. (2019). *Automation and New Tasks: How Technology Displaces and Reinstates Labor*. A clear, non-technical statement of the task-based framework used throughout this chapter. [@acemoglu2019automation]
- Brynjolfsson, E., Li, D. & Raymond, L. (2025). *Generative AI at Work*. The most detailed field study of AI in a real workplace, with careful discussion of its design. [@brynjolfsson2025generative]
- Dell'Acqua, F. et al. (2026). *Navigating the Jagged Technological Frontier*. The source of the "jagged frontier" idea, showing that AI can help and harm the same workers on different tasks. [@dellacqua2026navigating]
- Becker, J. et al. (2025). *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*. A careful randomised trial whose surprising result shows why expectations are a poor guide to effects; read it with the 2026 follow-up note. [@becker2025measuring]
- Humlum, A. & Vestergaard, E. (2025). *Large Language Models, Small Labor Market Effects*. Links survey data to administrative records to test whether experimental gains appear in earnings and hours. [@humlum2025large]
- Acemoglu, D. (2025). *The Simple Macroeconomics of AI*. A transparent, cautious macroeconomic estimate that makes its assumptions easy to inspect and challenge. [@acemoglu2025simple]
- Gray, M. L. & Suri, S. (2019). *Ghost Work: How to Stop Silicon Valley from Building a New Global Underclass*. An ethnographic and survey study of the hidden on-demand workers behind apparently automated services. [@gray2019ghost]
- Bainbridge, L. (1983). *Ironies of Automation*. A short classic paper that anticipates many of today's concerns about deskilling and human oversight. [@bainbridge1983ironies]


# Chapter 9: Information, Media and Democracy

::: {.objectives}
**After working through this chapter you should be able to:**

- explain how generative AI changes the cost of producing persuasive and deceptive content, and why production cost is only one part of how misinformation spreads;
- evaluate the evidence on deepfakes, the "liar's dividend" and AI's measurable effect on the 2024 elections;
- compare the main experimental findings on AI persuasion and on "silicon sampling", including their limits;
- describe how content provenance standards and watermarking work, and what they cannot do;
- assess how recommender systems, AI search and platform regulation shape the information that citizens see.
:::

On 21 January 2024, two days before the New Hampshire presidential primary in the United States, thousands of voters received a telephone call in a voice that sounded like President Joe Biden. The voice had been cloned with generative AI, and the message urged recipients to "save your vote for the November election" instead of voting in the primary. The US Federal Communications Commission (FCC) traced the calls to a political consultant, Steve Kramer, and proposed a $6 million fine against him for unlawfully spoofing caller identification [@fcc2024proposes]. It confirmed the fine in September 2024 [@fcc2024issues]. In a separate state criminal trial, a New Hampshire jury acquitted him in June 2025 of all voter-suppression and impersonation charges [@associatedpress2025new].

The case contains most of the themes of this chapter. Synthetic audio was cheap to make and hard for listeners to identify. The harm was real but its size is uncertain: nobody knows how many people, if any, stayed at home because of the call. Existing institutions (a telecoms regulator, a state prosecutor, a jury) responded, with mixed results. This chapter asks what the evidence, as of October 2026, says about AI and the information ecosystem. It covers synthetic media, elections, persuasion, simulated public opinion, provenance technology, recommender systems, news and search, and platform regulation. Throughout, it reports both the findings that give cause for concern and those that suggest earlier fears were overstated.

## 9.1 What changes when content becomes cheap

The **information ecosystem** is the whole system through which a society produces, distributes and consumes information. It includes journalists, platforms, search engines, governments, advertisers and ordinary users. Researchers usually distinguish **misinformation** (false or misleading content shared without intent to deceive) from **disinformation** (false content spread deliberately). A third category, **influence operations**, describes coordinated efforts, often by states, to shape opinion covertly, for example through networks of fake accounts.

Generative AI mainly changes one part of this system: the cost of producing content. A large language model can write thousands of plausible posts, comments or articles in minutes, in many languages and styles. Image, audio and video generators can do the same for pictures and voices. In a 2023 preprint, Goldstein and colleagues argued that these tools could make influence operations cheaper, larger and harder to detect. They described a pipeline with four points of intervention: how models are built, who can access them, how content is distributed and how audiences form beliefs [@goldstein2023generative]. Early evidence from platforms suggests that the gains so far have been modest. Meta reported in December 2024 that the covert influence networks it took down had made "only incremental productivity and content-generation gains" from generative AI, according to the company [@clegg2024what].

Production cost is only one link in that chain, however. A useful comparison is printing: cheap printing made it easy to produce leaflets, but a leaflet nobody reads changes nothing. Content must also be distributed, noticed and believed. In an essay for the Knight First Amendment Institute, Kapoor and Narayanan (2024) argue that generative AI lowers the cost of creating false content but not the cost of distributing it. In their view, misinformation spreads mainly because of demand, since people seek out claims that fit what they already believe [@kapoor2024looked]. Altay, Berriche and Acerbi (2023) make a related argument from the research literature: people do not believe everything they see online, and misinformation often "preaches to the choir", reaching those who already agree [@altay2023misinformation].

Leaflets, however, cannot talk back. AI can take part in conversations, answer questions and adapt to each reader, which is why the persuasion research in Section 9.4 matters. Generative tools are also being built into the distribution channels themselves, such as search engines and social media feeds, which Section 9.6 examines. The rest of the chapter therefore looks at each link of the chain in turn: making content, persuading people, verifying content, and distributing it.

## 9.2 Deepfakes, synthetic media and the liar's dividend

**Synthetic media** is any image, audio, video or text generated or substantially altered by AI. A **deepfake** is synthetic media that realistically depicts a real person or event in a way that could be mistaken for authentic. The European Union's AI Act defines a deep fake as AI-generated or manipulated image, audio or video content that resembles existing persons, objects, places, entities or events. The content must also be such that it "would falsely appear to a person to be authentic or truthful" [@europeanparliament2024regulation, Article 3(60)]. A **cheap fake**, by contrast, is a misleading edit made with ordinary tools, such as slowing down a video or cutting a quotation out of context.

How good are people at spotting synthetic content? Laboratory evidence suggests not very good. In a pre-registered experiment with 210 participants, Köbis, Doležalová and Soraperra (2021) found that people could not reliably detect deepfake videos. Neither raising awareness nor offering money for correct answers improved accuracy, and participants overestimated their own ability [@kobis2021fooled]. Nightingale and Farid (2022) showed participants a mix of real faces and faces generated by AI. In their first experiment (315 participants), accuracy was 48.2%, close to chance; training and feedback raised it only to 59.0% in a second experiment. In a third experiment, synthetic faces were rated 7.7% more trustworthy than real ones [@nightingale2022ai]. These studies used still images or short clips, and generators have improved since, so detection by eye is unlikely to have become easier.

Deepfakes can also harm individuals directly. Chesney and Citron (2019) warned early that the technology would be used for non-consensual intimate imagery, fraud and harassment as well as political deception [@chesney2019deep]. Legislators have responded. In the United States, the TAKE IT DOWN Act, signed on 19 May 2025, made it a federal crime to knowingly publish non-consensual intimate images, including "digital forgeries" created with AI. It also requires covered platforms to remove such images within 48 hours of a valid request, with platforms given one year to set up the removal process [@uscongress2025tools]. The EU AI Act requires anyone who deploys an AI system to create a deepfake to disclose that the content is artificial, with lighter duties for evidently artistic or satirical work [@europeanparliament2024regulation, Article 50(4)].

A subtler effect of deepfakes concerns authentic content. If people know that convincing fakes exist, a person caught on a genuine recording can claim that it was faked. Chesney and Citron called this the **liar's dividend**.

::: {.box .concept}
**Key concept: The liar's dividend**

The liar's dividend is the benefit that people caught in genuine scandals can gain by falsely claiming that the evidence is fake. Chesney and Citron (2019) observed, perversely, that the dividend grows as public education about deepfakes succeeds, because a sceptical public is more willing to doubt real evidence [@chesney2019deep]. A courtroom comparison helps: once everyone knows that documents can be forged, a defendant can cast doubt on a genuine letter just by alleging forgery. Courts at least have formal rules for authenticating evidence; public opinion has none.
:::

Is the liar's dividend real? Schiff, Schiff and Bueno (2025) tested it in five survey experiments with more than 15,000 American adults. Participants read about real scandals involving politicians, followed by a hypothetical response from the politician. False claims that a story was "fake news" raised support for the politician across partisan groups, more than staying silent or apologising did. However, the strategy worked against text-based reports and was largely ineffective against video evidence, and it did not reduce general trust in the media [@schiff2025liars]. The study therefore supports the existence of a liar's dividend while suggesting that, at least when it was conducted, video still carried more weight than text. Whether that remains true as convincing video fakes become common is an open question.

## 9.3 The 2024 election year: what the evidence shows

In 2024 voters went to the polls in the United States, India, Indonesia, Mexico, the United Kingdom, the European Union and many other places [@clegg2024what]. Many commentators predicted that generative AI would flood these campaigns with deceptive content. Two years later, several bodies of evidence allow a first assessment. Most of them point towards limited measurable impact on results, with important caveats about what can be measured.

Researchers at the Alan Turing Institute's Centre for Emerging Technology and Security (CETaS) examined the UK general election, the French legislative elections and the European Parliament elections of mid-2024. They identified 16 confirmed viral cases of AI-enabled disinformation or deepfakes during the UK election and 11 across the EU and French elections combined. They found no evidence that any of them meaningfully affected a result [@stockwell2024threat]. The institute's later report on the US election likewise found no evidence of a measurable impact on the result, while noting that this was largely because data on real-world voter behaviour were lacking. It also recorded far more viral AI-enabled disinformation than in the earlier elections, although volumes were still "relatively moderate", and warned about damage to trust [@stockwell2024ai]. Meta, which owns Facebook and Instagram, reported that ratings of AI content on elections, politics and social topics made up less than 1% of all misinformation fact-checked by its partners during the major elections of 2024 [@clegg2024what]. This figure covers only content that fact-checkers examined, and does not show how much AI content circulated overall.

Kapoor and Narayanan (2024) analysed 78 election-related uses of AI collected by the magazine WIRED's AI Elections Project. Half of them (39) showed no deceptive intent. For each of the 39 deceptive cases, the authors estimated that similar content could have been produced without AI for no more than a few hundred dollars. They also cited a finding by the News Literacy Project that cheap fakes were used about seven times as often as AI content in the US election [@kapoor2024looked].

::: {.box .debate}
**Debate: Were fears about AI and the 2024 elections overblown?**

*Yes, largely.* Simon, Altay and Mercier (2023) argued before the election year that concerns about AI-driven misinformation were overblown, because the supply of false content was never the main constraint; attention and belief are [@simon2023misinformation]. The record of 2024 appears to support them. Monitoring studies found few viral AI cases and no measurable effect on outcomes [@stockwell2024threat; @stockwell2024ai]. AI content was a small share of fact-checked misinformation on Meta's platforms [@clegg2024what]. Most deceptive cases could have been made cheaply without AI, and old-fashioned cheap fakes were far more common [@kapoor2024looked].

*Not so fast.* Absence of evidence of an effect on outcomes is not evidence of no effect. Elections are decided by small margins, effects on turnout or trust are hard to measure, and monitoring catches only what becomes visible. The CETaS studies covered the UK, France, the EU and the US, so the evidence from other large elections of 2024 is thinner. CETaS itself warned that confusion over what is real, including genuine content wrongly dismissed as AI-generated, was damaging trust in online information [@stockwell2024ai]. That concern fits the experimental evidence that false claims of fakery can help politicians escape text-based scandals [@schiff2025liars]. Experiments discussed in Section 9.4 also show that conversational AI can shift political attitudes in ways that static content does not, and monitoring of public posts cannot see private conversations with chatbots.

*What evidence would decide it:* access to platform data sufficient to trace exposure to AI content and link it to behaviour, and repeated assessment as tools change. The EU's data-access rules for researchers (Section 9.7) are partly designed to make such studies possible.
:::

The more serious documented interference of the period did not rely mainly on generative AI. The best-known case, the annulment of Romania's 2024 presidential election, is discussed as a case study in Section 9.7, because it concerns the amplification of content by platforms more than its creation.

## 9.4 AI as a persuader, and AI as a stand-in for the public

### Static messages and conversations

Political scientists have long found that persuading voters during a general election is hard. Kalla and Broockman (2018) drew on a meta-analysis of 40 field experiments and nine new experiments of their own. They concluded that the best estimate of the effect of campaign contact and advertising on Americans' candidate choices in general elections is zero [@kalla2018minimal]. Studies of AI-written static messages (a fixed text that everyone reads) found that AI could match human writers, with little sign of exceeding them. Goldstein and colleagues (2024) found that propaganda articles written by GPT-3 were highly persuasive. When a fluent English speaker edited the prompts or curated the output, they were under some conditions as persuasive as real foreign propaganda [@goldstein2024persuasive]. Yet Hackenburg and Margetts (2024) found that tailoring GPT-4 messages to each person's characteristics, known as **microtargeting**, did not make them more persuasive than generic messages [@hackenburg2024evaluating]. A further study found sharply diminishing returns to model size for single-message persuasion: larger models were somewhat more persuasive, but further scaling was not expected to add much [@hackenburg2025scaling].

Conversation appears to be different. In a widely cited experiment, Costello, Pennycook and Rand (2024) asked 2,190 Americans who believed a conspiracy theory to describe it, along with their evidence. Participants then discussed it with GPT-4 Turbo over three rounds, and the AI was instructed to reduce belief using evidence. Belief in the chosen conspiracy fell by about 20% on average, and the effect persisted undiminished for at least two months. A professional fact-checker rated 99.2% of a sample of 128 AI claims as true. The AI did not reduce belief in conspiracies that were true, and the effect spilled over to reduce belief in unrelated conspiracy theories [@costello2024durably]. The result suggests that some beliefs thought to be immune to evidence can change when the evidence is detailed and tailored to the person's own arguments.

The same capacity can be pointed in any direction. Hackenburg and colleagues (2025) ran three experiments with 76,977 UK adults, 19 language models and 707 political issues. Conversations with AI were 41% to 52% more persuasive than a static AI-written message. Between 36% and 42% of the immediate effect was still measurable a month later [@hackenburg2025levers].

The same study identified where the persuasive power came from. Post-training and prompting mattered more than model size or personalisation. Methods that encouraged models to pack conversations with facts and evidence worked best: each additional fact-checkable claim was associated with about 0.3 points more persuasion. Roughly half of the explainable variation in persuasion was attributable to the number of claims made, while personalisation added less than one point on average. The most persuasive set-ups were also the least accurate. In the most persuasive conditions, the authors estimated an effect of 15.9 points on a 0–100 agreement scale, against a 9.4-point average. In those conditions 30.0% of fact-checkable claims were rated inaccurate, compared with 16.0% on average [@hackenburg2025levers].

Lin and colleagues (2025) moved from policy issues to real elections. They ran pre-registered experiments before the 2024 US presidential election, the 2025 Canadian federal election and the 2025 Polish presidential election. Participants were randomly assigned to talk with an AI that advocated for one of the two leading candidates. The effects on candidate preference were larger than typically found for video advertisements. In the US experiment (2,306 participants), the difference between the pro-Harris and pro-Trump conditions was 2.88 points on a 0–100 scale; in Canada and Poland it was about 10 points. Slightly more than a third of the US effect persisted after more than a month. In the Canadian and Polish experiments, when the AI was told not to use facts and evidence, its persuasive effect fell by more than half. The authors also report that models advocating for candidates on the political right made more inaccurate claims in all three countries. These accuracy ratings were produced by an AI system and checked against ratings by professional fact-checkers and by politically balanced groups of lay people [@lin2025persuading]. Figure 9.1 brings these results together.

![Figure 9.1: Persuasive effects of AI in recent experiments, in points on 0–100 attitude or preference scales, with 95% confidence intervals where reported. Conversation with AI produced larger effects than a static AI-written message, and effects were smaller in the high-salience US presidential race than in Canada, Poland or a state ballot measure. The studies measure effects differently (treatment versus control, or the gap between two opposing AI advocates), so bars are comparable only within each study. Source: @hackenburg2025levers; @lin2025persuading; @kalla2018minimal.](../figures/svg/fig-09-01.svg){#fig:09-01}

Several features of these experiments limit what they imply for real elections. Participants were recruited online, paid and told they were talking to an AI. In the experiments of Hackenburg and colleagues, conversations lasted nine minutes on average [@hackenburg2025levers], and real voters may never choose to spend that long discussing politics with a chatbot. Outside experiments, such use is still a minority habit: in the Reuters Institute's 2026 survey, 10% of respondents used AI chatbots for news each week [@egan2026digital]. Effects also faded, with roughly a third to two-fifths remaining after a month in both large studies. Lin and colleagues note that they debriefed participants before the elections and randomised the direction of persuasion, so that any lasting effects would cancel out. Effects in the US presidential race were small compared with those for a less familiar Massachusetts ballot measure tested in the same study. There, the gap between pro and anti conditions among people without strong views was 22.7 points. The authors suggest that AI dialogues may have a bigger impact on state and local contests than on national ones [@lin2025persuading].

On the other side of the ledger, Salvi and colleagues (2025) found that GPT-4, given basic demographic information about its opponent, was more persuasive than a human debater. This held in 64.4% of the debates in which the two were not equally persuasive (900 participants) [@salvi2025conversational]. Taken together, the evidence shows that AI dialogue can change minds in controlled settings, mainly by marshalling information, and that accuracy and persuasiveness can pull in opposite directions. Whether it does so at scale depends on whether voters choose such conversations, which the experiments could not test.

### Silicon sampling

A different use of language models is to stand in for survey respondents. Argyle and colleagues (2023) conditioned GPT-3 on thousands of demographic "backstories" taken from real US survey participants and compared the model's answers with the real ones. They found that, with suitable conditioning, the model reproduced the response patterns of many subgroups, a property they called **algorithmic fidelity**, and they named the resulting synthetic respondents **silicon samples** [@argyle2023out].

::: {.box .concept}
**Key concept: Silicon sampling**

Silicon sampling means using a language model, prompted with the characteristics of real people, to generate synthetic answers to survey questions. The analogy is a flight simulator: it can be useful for practice and for testing ideas cheaply, but no airline would certify a new aircraft on simulator data alone. The analogy breaks down because a flight simulator is built from known physics. A language model's picture of public opinion comes from text that may be outdated, unrepresentative or shaped by the model's own training.
:::

Later studies found the limits of this approach. Bisbee and colleagues (2024) asked ChatGPT, adopting different personas, to rate 11 social and political groups. Average scores closely matched the American National Election Study, but the synthetic answers varied less than real ones and statistical relationships often differed. Results also changed with small changes to prompt wording, and the same prompt gave significantly different results over three months [@bisbee2024synthetic]. In September 2026 the Pew Research Center tested "digital twins" built with Anthropic's Claude Opus 4.6, the best performer among several models it tried, using real panel members' demographics and earlier answers. Across three 2026 survey waves, synthetic results differed from human results by about 12 percentage points on average, with the largest error (16.1 points) for Republicans. The synthetic samples were "far less politically diverse" than the real population: 86% of synthetic Democrats and Democratic leaners said billionaires' fortunes were bad for the country, against 45% of real Democrats. Pew stated that it has no plans to use AI models to generate survey results [@pew2026well]. Silicon samples may help researchers design questions and generate hypotheses, but the evidence so far does not support using them in place of asking people.

## 9.5 Provenance, watermarking and detection

If people cannot reliably spot synthetic content by eye, can technology help? Three approaches exist, and they answer different questions. **Detection** tries to infer from the content alone whether it was made by AI. **Watermarking** hides a signal in AI-generated content at the moment of creation so that it can be recognised later. **Content provenance** attaches a signed record of where content came from and how it was edited.

Detection after the fact has a poor record for text. Weber-Wulff and colleagues (2023) tested 14 detection tools, including two commercial systems widely used in education. They concluded that the tools were "neither accurate nor reliable", with a bias towards classifying AI text as human-written. Disguising the text, for example by machine translation or paraphrasing, made them worse [@weberwulff2023testing]. Liang and colleagues (2023) found that detectors frequently misclassified writing by non-native English speakers as AI-generated, which raises fairness concerns when such tools are used to judge students [@liang2023gpt].

Content provenance takes the opposite approach: instead of guessing whether something is fake, it records where authentic or labelled content came from. The main standard is maintained by the Coalition for Content Provenance and Authenticity (C2PA), founded in February 2021 by Adobe, Arm, the BBC, Intel, Microsoft and Truepic [@microsoft2021technology]. A C2PA **manifest**, marketed as "Content Credentials", is a bundle of statements about a file, for example which camera or AI tool created it and what edits were made. The bundle is digitally signed so that tampering can be detected. Cryptographic hashes, a kind of digital fingerprint of the exact file contents, bind the manifest to the file, so any change to the content invalidates them. Because manifests can be stripped from files, the standard also allows "soft bindings", such as invisible watermarks, that help locate a stored copy of the manifest. The C2PA states plainly that provenance information "cannot tell you whether the digital content is true, accurate or factual" [@c2pa2025c2pa]. Figure 9.2 shows the pipeline.

![Figure 9.2: A simplified content provenance pipeline. A camera or AI tool creates content and a signed manifest; each editing step adds a new signed entry; a platform or viewer checks the signatures. If the manifest is stripped, a watermark can help retrieve it from cloud storage. Provenance shows where content came from, not whether it is true. Diagram by the author, based on @c2pa2025c2pa.](../figures/svg/fig-09-02.svg){#fig:09-02}

Watermarking for AI-generated content is now deployed at scale by some developers. Google DeepMind's SynthID-Text, described in *Nature* by Dathathri and colleagues (2024), changes only how the model chooses each next word, so that a statistical signal can later be detected without access to the model. In a live experiment covering nearly 20 million responses from Google's Gemini chatbot, user feedback indicated no loss of text quality [@dathathri2024scalable]. Google said in May 2025 that more than 10 billion pieces of content had been watermarked with SynthID, according to the company [@perez2025google].

::: {.box .deeper}
**Going deeper: How a text watermark works**

A language model writes by repeatedly choosing the next token (a word or word fragment) from a probability distribution. In the scheme of Kirchenbauer and colleagues (2023), a secret key and the preceding token are used before each choice to split the vocabulary pseudo-randomly into a "green list" and a "red list". The model is then nudged towards green tokens [@kirchenbauer2023watermark]. Human writers, who do not know the key, use green tokens about as often as chance predicts. A detector with the key counts green tokens: if a 200-token passage contains far more than expected, it is very unlikely to be unwatermarked. In words, the test asks "how surprising is this many green tokens if the text were not watermarked?", much as one might suspect a loaded die after seeing too many sixes. SynthID-Text uses a different sampling method, called tournament sampling, but rests on the same idea of a hidden statistical bias [@dathathri2024scalable]. Paraphrasing replaces tokens and weakens the signal, which is why short or heavily edited texts are hard to classify.
:::

Every one of these tools has limits. Watermarks work only if the generator adds them, and open-weight models that anyone can run (Chapter 7) need not. Zhang and colleagues (2024) proved that, under natural assumptions, no watermark can be "strong", meaning impossible to remove without degrading quality. An attacker can always make small random edits while preserving quality [@zhang2024watermarks]. Provenance depends on cameras, editing software and platforms all adopting the standard and displaying it in ways users understand. A signed record that a photograph came from a particular camera does not show that the scene was not staged, and the absence of a record proves nothing, since most authentic content carries none. Provenance is therefore most useful for verifying content from sources that choose to sign it, such as news organisations, and less useful for exposing fakes from those that do not.

Regulators are nonetheless building on these tools. The EU AI Act requires providers of systems that generate synthetic audio, images, video or text to ensure, where technically feasible, that outputs "are marked in a machine-readable format and detectable as artificially generated or manipulated" [@europeanparliament2024regulation, Article 50(2)]. These transparency duties began to apply on 2 August 2026 [@europeanparliament2024regulation, Article 113]. The 2026 Digital Omnibus on AI, however, gave generative systems already on the market before that date until 2 December 2026 to add machine-readable marking [@europeanparliament2026regulation]. Chapter 13 discusses the timetable and the 2026 amendments.

## 9.6 Recommender systems, search and journalism

### Recommender systems

A **recommender system** is software that selects and ranks content for each user, such as the order of posts in a social media feed, usually by predicting what the user will engage with. Recommender systems were among the first forms of AI to shape public information, long before chatbots. A common fear is that they create "echo chambers" by showing people only views they already hold, and so increase **polarisation**, the growing distance or hostility between political groups.

Some of the strongest evidence comes from a collaboration between Meta and independent academics during the 2020 US election. Guess and colleagues (2023) switched a sample of consenting Facebook and Instagram users from the algorithmic feed to a reverse-chronological one. Time on the platforms fell substantially, and users saw more political and more untrustworthy content. Over three months, however, there was no significant change in polarisation, political knowledge or other key attitudes [@guess2023social]. Nyhan and colleagues (2023) reduced exposure to content from like-minded sources by about a third for 23,377 users. They found no measurable effect on eight pre-registered attitude measures, including polarisation and belief in false claims [@nyhan2023like]. González-Bailón and colleagues (2023) used aggregated data on 208 million US Facebook users. They found that ideological segregation in political news was high, and that it increased from the news users could have seen, to what the feed showed them, to what they engaged with. There was also an asymmetry. A substantial corner of the news ecosystem was consumed exclusively by conservatives, and most content rated false by Meta's fact-checking partners sat in that corner, with no equivalent on the liberal side [@gonzalezbailon2023asymmetric].

Other studies point the other way. A long-running randomised experiment on Twitter compared a control group of nearly 2 million daily active accounts, which saw a chronological feed, with users of the algorithmic one. The mainstream political right enjoyed higher algorithmic amplification than the mainstream left in six of seven countries studied. The study found no evidence that the algorithm amplified far-left or far-right groups more than moderate ones [@huszar2022algorithmic]. Piccardi and colleagues (2025) used a language model to rerank the X feeds of 1,256 participants during the 2024 US campaign, reducing or increasing posts that expressed partisan animosity or antidemocratic attitudes. Over ten days, this shifted animosity towards the opposing party by more than two points on a 100-point "feeling thermometer". The shift occurred in both directions and with no detectable difference between Democrats and Republicans [@piccardi2025reranking]. The two sets of findings can both hold: removing the algorithm entirely changed little over three months, while targeted changes to what the algorithm promotes had measurable short-term effects. The Piccardi study also illustrates that language models can be used to make feeds less divisive as well as more.

### AI search and the news business

Generative AI is also changing how people reach news. Search engines now often place an AI-written summary above the list of links. Pew Research Center tracked the browsing of 900 US adults in March 2025. In visits to search pages that showed an AI summary, users clicked a traditional result link 8% of the time, against 15% when no summary appeared. They clicked a link inside the summary in only 1% of visits, and were more likely to end their browsing session [@chapekis2025google]. Figure 9.3 shows these results. The study observed one month of behaviour in one country and cannot show how habits change over time.

![Figure 9.3: Share of Google search visits in which users clicked a link, with and without an AI-generated summary on the page, and share of visits that ended the browsing session. Based on the browsing data of 900 US adults, March 2025. Source: @chapekis2025google.](../figures/svg/fig-09-03.svg){#fig:09-03}

For publishers, fewer clicks mean less advertising and subscription revenue. The Reuters Institute's *Digital News Report 2026* is based on surveys in 48 markets. It reports Chartbeat data showing that Google search traffic to more than 2,500 news sites fell by a third globally between November 2024 and November 2025. Publishers expect a further fall of more than 40% over three years. The report notes that the effect of AI summaries is widely assumed rather than proven, and that hard-news queries are mostly excluded from them.

The same report tracks how audiences use and judge AI for news. Weekly use of AI chatbots for news rose from 7% of respondents in 2025 to 10% in 2026, and to 16% among under-35s. Only 20% said they trusted news answers from chatbots, compared with 37% for news in general. Among those who used chatbots for news, 42% said they always or often clicked through to the original sources [@egan2026digital]. For news organisations, this makes it important whether AI answers attribute and link to their reporting, and whether those answers are accurate.

Whether these answers are reliable is itself a research question. In a study coordinated by the European Broadcasting Union (EBU) and the BBC, journalists from 22 public service media organisations in 18 countries rated more than 3,000 news answers from ChatGPT, Copilot, Gemini and Perplexity. Some 45% of answers had at least one significant issue; 31% had serious sourcing problems and 20% had major accuracy problems, such as invented details or outdated information [@ebu2025ais]. These figures describe one set of products in 2025 and may change quickly, but they suggest that AI assistants do not yet reliably reproduce what the news organisations they draw on actually reported. Chapter 13 discusses the related legal disputes over the use of news content to train AI systems.

## 9.7 Platform governance

The rules that decide what platforms must do about harmful information differ sharply between jurisdictions. In the United States, Section 230 of the Communications Act provides that no online service shall be treated as the publisher of information provided by its users [@uscongress1996protection]. New US regulation has focused on specific harms, such as the intimate-image law described in Section 9.2. The European Union has taken a broader approach through the **Digital Services Act (DSA)**, which has applied in full since 17 February 2024 [@europeanparliament2022regulation, Article 93] and sets duties for online platforms in proportion to their size.

The DSA's strictest rules apply to "very large online platforms" and search engines. Each year these must assess "systemic risks" arising from their design and use, and must consider how their recommender systems contribute. The listed risks explicitly include "any actual or foreseeable negative effects on civic discourse and electoral processes" [@europeanparliament2022regulation, Article 34]. Platforms must then take reasonable mitigation measures. These may include testing and adapting their recommender systems, and ensuring that generated or manipulated images, audio or video that falsely appear authentic are distinguishable "through prominent markings" [@europeanparliament2022regulation, Article 35(1)(d) and (k)]. They must offer at least one recommender option not based on profiling the user [@europeanparliament2022regulation, Article 38], and give vetted researchers access to data. The European Commission can fine them up to 6% of their worldwide annual turnover [@europeanparliament2022regulation, Article 74].

::: {.box .case}
**Case study: Romania's annulled election and the DSA**

On 6 December 2024, Romania's Constitutional Court annulled the presidential election after its first round, two days before a scheduled run-off involving the first-round leader, Călin Georgescu. The decision followed the declassification of intelligence reports alleging a coordinated campaign on TikTok and Telegram; one report said about 25,000 pro-Georgescu TikTok accounts became highly active two weeks before the vote. Much of this evidence consisted of allegations, Georgescu called the decision a coup, and the attribution to Russia rested on similarities with earlier operations [@solea2024romanias]. On 17 December 2024 the European Commission opened formal DSA proceedings against TikTok. The proceedings focus on the management of election risks linked to its recommender systems and on its rules for political advertising; opening proceedings does not prejudge the outcome [@europeancommission2024commission]. The case shows that the most consequential threats to an election may come from coordinated amplification and undisclosed paid promotion, with or without generative AI, and that annulling an election is itself contested.
:::

The DSA's first non-compliance decision came on 5 December 2025, when the Commission fined X €120 million. The decision found that X's paid "blue checkmark" was deceptive design, that its advertising repository lacked required information, and that its terms prevented researchers from accessing public data [@europeancommission2025commission]. The research-access provisions matter for this chapter's evidence. Much of what is known about recommender systems comes from studies that depended on a platform's voluntary cooperation [@guess2023social], and the DSA attempts to make such access a legal right.

The DSA's approach is itself contested, and the arguments on each side rest on different kinds of evidence. Critics argue that duties framed around "systemic risks" push platforms to remove lawful speech to avoid large fines. In July 2025 the Republican majority on the US House Judiciary Committee published an interim staff report arguing that the DSA "compels global censorship". Its central claim is that platforms apply one set of terms worldwide, and that Commission officials, according to documents the committee obtained under subpoena, expected platforms to change those global terms [@housejudiciary2025foreign]. The report is a partisan document in a transatlantic political dispute, and it rests on the committee's own selection of internal material. The regulation's defenders can point to its text, which requires platforms to weigh negative effects on fundamental rights, including freedom of expression, alongside risks to civic discourse [@europeanparliament2022regulation, Article 34(1)(b)]. Independent empirical work so far gives a mixed verdict on the DSA's transparency tools. Kaushal and colleagues (2024) analysed a representative sample of the 131 million "statements of reasons" for moderation decisions that platforms submitted to the DSA Transparency Database in November 2023. They found some transparency gains, but concluded that compliance "remains problematic" because the database allows platforms "a lot of discretion" in what they report [@kaushal2024automated]. Whether the DSA chills lawful speech or improves the information environment is an empirical question that the research access it creates could help answer.

Platform governance increasingly overlaps with AI governance. The EU AI Act's marking and disclosure duties (Section 9.5) apply to those who make and deploy generative AI, while the DSA's duties apply to the platforms that distribute content. The United States' TAKE IT DOWN Act targets one specific harm across all covered platforms [@uscongress2025tools]. Each of these regimes faces the questions raised by the evidence in this chapter. One is how to make distribution, not only production, more accountable. Another is how to keep provenance signals intact as content moves between services. A third is how to give independent researchers the data needed to measure effects that the monitoring studies of 2024 could not detect. Chapter 13 compares these approaches with those of China, the United Kingdom and international bodies.

## Summary

- Generative AI lowers the cost of producing persuasive and deceptive content, but distribution, attention and belief remain important constraints on its impact.
- People detect deepfakes poorly, and experimental evidence supports a "liar's dividend" for politicians who falsely dismiss text-based reports as fake, though less so for video.
- Monitoring studies and platform reports from the 2024 election year found few viral AI cases and no evidence that AI changed results. These findings measure visible content and outcomes, not subtler effects on trust or turnout.
- Conversations with AI changed political attitudes and conspiracy beliefs more than static messages, with effects that partly persisted for one to two months. Persuasion came mainly from presenting information, the most persuasive set-ups were less accurate, and it is unclear how many voters will seek out such conversations.
- Silicon samples reproduce some average patterns of public opinion but understate its diversity and are not a substitute for surveying people.
- Provenance standards (C2PA) and watermarks (such as SynthID) can label content at creation, but they depend on adoption, can be stripped or weakened, and cannot establish truth; detectors that judge content after the fact are unreliable.
- Field experiments found that removing feed algorithms changed polarisation little over three months, while targeted reranking had small measurable effects; AI search summaries are associated with fewer clicks to news sites.
- The EU's Digital Services Act requires the largest platforms to assess and mitigate risks to electoral processes and has produced its first fine. Critics say it pressures platforms to restrict lawful speech, and early independent studies find its transparency tools only partly effective; approaches elsewhere are narrower.

## Key terms

misinformation · disinformation · influence operation · synthetic media · deepfake · liar's dividend · microtargeting · algorithmic fidelity · silicon sampling · content provenance · C2PA manifest · watermarking · recommender system · polarisation · Digital Services Act

## Discussion questions

1. Kapoor and Narayanan argue that political misinformation is "not an AI problem" because AI lowers the cost of producing content but not of distributing it. Using evidence from Sections 9.3 and 9.4, evaluate how well this argument holds for static content and for conversational AI.
2. Schiff, Schiff and Bueno found that claiming "fake news" helped politicians against text reports but not against video. What would you expect to happen to this result as realistic video generation becomes widespread, and how could you test your prediction?
3. A city council proposes to replace its annual resident survey with a silicon sample built from last year's respondents. Using the Pew (2026) and Bisbee et al. (2024) findings, write a short recommendation on what the synthetic sample could and could not be used for.
4. Lin et al. found AI persuasion effects more than three times larger in Canada and Poland than in the US presidential race, and much larger for a state ballot measure. What explanations can you suggest, and what do they imply for which elections are most exposed to AI persuasion?
5. A human-rights organisation asks witnesses in a conflict zone to submit smartphone videos with Content Credentials attached. What would the credentials establish about a video, what would they leave open, and what risks might signed metadata create for the witnesses themselves?
6. The House Judiciary Committee report and Kaushal et al. (2024) criticise the DSA on different grounds. Compare the kind of evidence each relies on, and design a study, using data the DSA makes available to researchers, that could test whether the regulation leads platforms to remove lawful political speech.

## Further reading

- Chesney, B. and Citron, D. (2019). *Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security*. The legal analysis that introduced the "liar's dividend" and still frames much of the policy debate. [@chesney2019deep]
- Kapoor, S. and Narayanan, A. (2024). *We Looked at 78 Election Deepfakes. Political Misinformation Is Not an AI Problem*. A short, data-based argument for focusing on the demand for misinformation. [@kapoor2024looked]
- Hackenburg, K. et al. (2025). *The Levers of Political Persuasion with Conversational Artificial Intelligence*. The largest experiment to date on what makes AI persuasive, and on the trade-off with accuracy. [@hackenburg2025levers]
- Lin, H. et al. (2025). *Persuading Voters Using Human–Artificial Intelligence Dialogues*. Pre-registered experiments in three national elections; read alongside Kalla and Broockman (2018) for context. [@lin2025persuading]
- Guess, A. M. et al. (2023). *How Do Social Media Feed Algorithms Affect Attitudes and Behavior in an Election Campaign?* A landmark field experiment on recommender systems, with an unusual level of platform cooperation. [@guess2023social]
- Egan, J. et al. (2026). *Reuters Institute Digital News Report 2026*. The standard annual source on how people get news, including from AI. [@egan2026digital]


# Chapter 10: Education, Health and Everyday Life

::: {.objectives}
**After working through this chapter you should be able to:**

- explain what randomised trials of AI tutoring have found, and why the design of a tutor can turn a learning gain into a learning loss;
- evaluate claims about medical AI by distinguishing diagnostic accuracy studies, regulatory authorisation and evidence of benefit in clinical practice;
- compare the evidence on clinicians working with AI against the evidence on AI working alone;
- assess the research on AI companions, loneliness and mental health, including its limits;
- identify the privacy and data-protection questions raised when AI handles students', patients' and users' personal information.
:::

In June and July 2024, first-year senior secondary students from nine public schools in Benin City, Nigeria, took part in an after-school programme to practise English. They worked in pairs with Microsoft Copilot, a chatbot built on GPT-4. Teachers set the topic and the opening prompt. The students then questioned the chatbot freely for 90 minutes, up to twice a week, for six weeks. Places were allocated by lottery among the students who volunteered, which turned the programme into a randomised controlled trial. In a working paper, the World Bank team that evaluated it reported a gain of 0.31 standard deviations on an end-of-programme assessment, and 0.23 standard deviations on the English component alone [@desimone2025chalkboards].

A few months earlier, in autumn 2023, a field experiment in a large high school in Turkey gave nearly 1,000 mathematics students access to GPT-4 during practice sessions. Students with an unrestricted chatbot solved more practice problems, then scored 17% lower than students without access when they sat an exam on their own [@bastani2025generative]. The two studies used similar technology and reached opposite headline results. Much of this chapter is about why such differences arise, and about how to read the evidence when AI moves into classrooms, clinics and private life.

The chapter covers three domains where AI touches individuals directly. Sections 10.1 to 10.3 deal with education: tutoring, harms to learning, and assessment. Sections 10.4 and 10.5 deal with medicine, at the level of health-system use and the quality of evidence. Sections 10.6 and 10.7 turn to everyday life: companionship and mental health, then accessibility, privacy and memory. Privacy runs through all three domains, because tutors, clinical tools and companions all collect personal information. Effects on jobs and productivity are treated in Chapter 8, and the general taxonomy of AI risks in Chapter 11.

## 10.1 AI tutors: what the trials show

The hope behind AI tutoring has a long pedigree. In 1984 the educational psychologist Benjamin Bloom reported that students taught one-to-one by a tutor performed about two standard deviations better than students taught in a conventional class. He called the search for group methods that could match this the "2 sigma problem" [@bloom1984sigma]. Later research confirmed that tutoring works, though with smaller effects. A meta-analysis of randomised experiments in schools found an average effect of about 0.29 standard deviations, with the largest effects when teachers or paraprofessionals were the tutors [@nickow2020impressive]. The obstacle has always been cost, since a human tutor for every pupil is unaffordable for most school systems. Large language models (LLMs, the text-generating systems described in Chapter 3) revived the question of whether software could supply some of what a tutor provides at a fraction of the price.

::: {.box .concept}
**Key concept: Effect size in standard deviations**

Education studies often report results in standard deviations (SD) of the test score, so that different tests can be compared. An effect of 0.3 SD means that the average treated student moved from the middle of the comparison group to roughly the 62nd percentile. The analogy is a height chart: saying a group grew "0.3 SD" tells you how far it moved relative to the usual spread of heights, whatever unit the ruler uses. The analogy breaks down because test scores, unlike heights, depend on what the test measures, so effects measured on different tests are not directly comparable.
:::

The Nigerian programme described in the opening is one of the most discussed trials from a lower-income country. Of 1,328 volunteers, 657 were assigned to the programme and 671 to a control group that continued normal lessons; 422 and 337 of them respectively sat the final assessment, which formed the analysis sample [@desimone2025chalkboards]. The authors estimate that the six-week programme produced gains equivalent to 1.5 to 2 years of ordinary schooling. It cost about US\$48 per pupil, which would place it among the more cost-effective education interventions evaluated in developing countries. Effects were positive across the range of prior attainment but largest for girls and for students who were already doing well. The authors caution that the result for girls may partly reflect one girls-only school in the sample. The study has not yet been peer-reviewed, and more control students than treated students failed to sit the final test, a form of attrition that the authors must correct for statistically.

A second widely discussed trial took place at Harvard University in autumn 2023. Kestin and colleagues compared an AI tutor, which students used at home, with an in-class "active learning" lesson in an introductory physics course for life-science students [@kestin2025ai]. The design was a crossover: 194 students each took one lesson in each format, on two topics, so that every student served as their own comparison. Median post-test scores were 4.5 in the AI condition and 3.5 in class, from a pre-test median of 2.75, and a regression adjusting for prior knowledge gave an effect of 0.63 SD. Students using the tutor spent a median of 49 minutes, against 60 minutes in class, and rated themselves as more engaged. The tutor was not a general chatbot: it was given step-by-step solutions written by the instructors and a prompt based on research about how students learn.

The study has clear limits. It was carried out in one course at a single selective university and covered introductory material that students were meeting for the first time. The lessons targeted understanding and application, and the authors do not claim that structured AI tutoring would outperform active learning in tasks requiring complex synthesis [@kestin2025ai]. Some of the authors also developed the active-learning methods used as the comparison, which makes the comparison a demanding one but also means the team had a stake in both arms. Both the Nigerian and the Harvard trials were short and measured learning on tests close to what had just been taught. Neither result should therefore be read as a forecast of what a whole school year with an AI tutor would achieve.

::: {.box .deeper}
**Going deeper: Reading an education trial**

Three design details change how much weight a trial deserves. The first is the unit of randomisation: the Nigerian trial randomised individual students, the Turkish trial randomised whole classes, and the Harvard trial gave every student both conditions in turn (a crossover). Randomising classes protects against students sharing tools, but it means the effective sample size is smaller than the number of students, because students in the same class resemble one another. The second is the estimand, the precise quantity a study sets out to estimate. An "intention-to-treat" estimate compares everyone who was offered the programme with everyone who was not, whether or not they attended. It answers the policy question "what happens if we offer this?" The Nigerian team also reports estimates for students who actually attended, which are larger because attendance averaged 72% [@desimone2025chalkboards]. The third is attrition, the loss of participants before the final test. If those who drop out differ between arms, for example if weaker students in the control group skip the test, the remaining groups are no longer comparable, and the analysis has to adjust for it.
:::

Outside trials, students already use general chatbots for learning on a large scale. In a Pew Research Center survey of 1,391 US teenagers conducted in autumn 2024, 26% said they had used ChatGPT for schoolwork, double the 13% recorded a year earlier [@sidoti2025quarter]. A working paper by OpenAI researchers and academic economists, analysing ChatGPT consumer messages, estimated that about 10% of all messages in mid-2025 were requests for tutoring or teaching [@chatterji2025how]. Much of this use happens without the scaffolding that the trial tutors had, which is why the next section matters.

## 10.2 When help harms learning

The Turkish study introduced in the opening is the clearest experimental evidence that an AI assistant can raise performance while lowering learning. Bastani and colleagues ran four 90-minute sessions in about fifty classes in grades 9 to 11, covering roughly 15% of the semester's mathematics curriculum [@bastani2025generative]. Each class was randomly assigned to one of three arms. "GPT Base" was a plain GPT-4 chat interface. "GPT Tutor" used the same model with a teacher-designed prompt that contained the correct solution and told the model to give hints instead of answers. The control arm used textbooks and notes only.

Figure 10.1 shows the main results. During assisted practice, students with GPT Base scored 48% higher than the control group and students with GPT Tutor 127% higher. In the unassisted exam that followed, GPT Base students scored 17% below the control group, a statistically significant loss, while GPT Tutor students scored about the same as the control group [@bastani2025generative]. The authors traced the loss to students using the chatbot as a "crutch": the most common message in the GPT Base arm was a request for the answer. The base model was also unreliable at the task, giving a correct answer only 51% of the time when the researchers repeated students' typical queries.

![Figure 10.1: Two kinds of evidence on AI tutors. Panel A: in a randomised trial in a Turkish high school, students using an unrestricted GPT-4 interface ("GPT Base") or a hint-giving version ("GPT Tutor") scored far higher than a control group during practice, but in the later unassisted exam the GPT Base group scored 17% lower than the control group and the GPT Tutor group about the same. Panel B: estimated effects of two tutoring trials in standard deviations. The contrast shows that the same underlying technology can raise or lower measured learning depending on design and on what is measured. Source: @bastani2025generative; @desimone2025chalkboards; @kestin2025ai.](../figures/svg/fig-10-01.svg){#fig:10-01}

The guarded tutor removed the harm but did not produce a measurable gain on the exam, which is a sobering result for anyone expecting design alone to solve the problem [@bastani2025generative]. The study took place in autumn 2023, when chatbots were new to most students, and covered one subject in one school. Its value lies in the mechanism it isolates: tools that make a task easier during practice can remove the effort through which skills are formed. Psychologists call this kind of useful effort a "desirable difficulty", and the Nigerian programme deliberately built some of it into its prompts [@desimone2025chalkboards].

Laboratory work points in the same direction, though with weaker designs. A preprint from the MIT Media Lab followed 54 participants who wrote essays over several sessions either with ChatGPT, with a search engine, or unaided. Their brain activity was recorded with electroencephalography (EEG), which measures electrical activity through sensors on the scalp [@kosmyna2025brain]. Participants who used the chatbot showed the weakest connectivity between brain regions during writing. They also reported the least sense of ownership of their essays and had difficulty quoting from them. Only 18 participants completed the final session, and EEG connectivity is an indirect measure of learning, so the conclusions are best treated as a prompt for further research.

Developers have responded with modes that imitate the GPT Tutor design. In July 2025 OpenAI launched a "study mode" for ChatGPT in which the system asks questions to check understanding and may withhold direct answers until the learner engages [@zeff2025openaia]. Such modes rely on instructions to the model and can be switched off by the student, which is the same freedom the GPT Base arm had. Whether optional guardrails change behaviour at scale has not yet been tested in a published randomised trial.

## 10.3 Cheating, detection and assessment

Universities face the practical side of the same question: how to assess what a student knows when a capable writing assistant is always available. The Higher Education Policy Institute (HEPI) has surveyed full-time UK undergraduates each year since 2024. In its 2026 survey of 1,054 students, polled in December 2025, 95% said they used AI in at least one way and 94% said they used generative AI to help with assessed work [@stephenson2026student]. The most common uses were having concepts explained (61%) and summarising articles (49%).

The same survey tracks the use that most worries universities. The share of students who said they had included AI-generated text directly in assessed work rose from 3% in 2024 to 8% in 2025 and 12% in 2026 [@stephenson2026student]. Teenagers draw distinctions of their own. In the Pew survey, 54% of US teens thought it acceptable to use ChatGPT to research new topics. Only 18% thought it acceptable for writing essays, and 42% thought it was not [@sidoti2025quarter]. These views do not settle what institutions should allow, but they suggest that students themselves see a difference between AI as a reference source and AI as a substitute author.

One early response was to detect AI-written text automatically. The evidence on such detectors is discouraging. Liang and colleagues tested seven widely used detectors on 91 essays written by non-native English speakers for the TOEFL exam. The detectors wrongly labelled more than half of them as AI-generated, with an average false-positive rate of 61% [@liang2023gpt]. A false positive here means a human-written essay flagged as machine-written. The same detectors classified essays by US eighth-grade students accurately. The authors attribute the difference to the more limited range of expression typical of non-native writers, which makes their text statistically predictable in the way that model-generated text is. When the researchers asked ChatGPT to make the TOEFL essays sound more sophisticated, the false-positive rate fell to 12%. The tools could thus be evaded by the very technology they were meant to detect.

Institutions have therefore shifted attention from detection to the design of assessment. In HEPI's 2026 survey, 65% of students said that assessment at their institution had changed significantly in response to AI [@stephenson2026student]. Common responses include more supervised examinations, oral defences of written work, assignments that require students to document their process, and tasks in which AI use is permitted and itself assessed. Each option has costs: supervised exams test a narrower range of skills, oral assessment is expensive to run at scale, and process documentation can itself be generated by AI. No study has yet shown which combination best protects the validity of degrees.

Monitoring students also raises questions of privacy and fairness, and the law has begun to respond. Since 2 February 2025, the EU AI Act has banned AI systems that infer the emotions of people in education institutions, except for medical or safety reasons [@europeanparliament2024regulation, Articles 5(1)(f) and 113]. It classes as "high-risk" the AI systems used to decide admission, evaluate learning outcomes, assign students to levels of education, or monitor and detect prohibited behaviour during tests [@europeanparliament2024regulation, Annex III(3)]. Automated marking and online proctoring therefore fall under the Act's strictest duties for permitted systems. After a 2026 amendment, these duties apply from 2 December 2027 [@europeanparliament2026regulation]; Chapter 13 describes what they require.

## 10.4 AI in medicine: approvals and accuracy

Medicine has a longer record of AI-based software than education, and it has a formal system for deciding which tools may be sold. In the United States, the Food and Drug Administration (FDA) maintains a public list of AI-enabled medical devices that have been authorised for marketing. As of the list's update published in September 2026, it contained 1,614 devices, the earliest from 1995 and the most recent decided in June 2026 [@fda2026artificial]. Radiology accounted for 1,230 of them, about 76%, followed by cardiovascular devices (154) and neurology (73). Figure 10.2 shows how annual authorisations have grown, from 6 in 2015 to 335 in 2025.

![Figure 10.2: Number of AI-enabled medical devices authorised by the US FDA each year, 2015–2025, by date of final decision. Authorisations rose more than fiftyfold over the decade, and about three-quarters of all listed devices are in radiology. Counts reflect the FDA list as updated in September 2026; the FDA adds devices whose summaries are published late, so recent years may be revised upwards. Source: @fda2026artificial.](../figures/svg/fig-10-02.svg){#fig:10-02}

This count is easy to over-read. The FDA describes its list as not comprehensive, because it identifies devices mainly by searching for AI-related terms in their public summaries. Authorisation is a judgement about safety and effectiveness for a stated intended use; it is not proof that the device improves patient outcomes. The list also does not yet show which devices, if any, use generative AI. The FDA has said it will explore ways to identify devices that incorporate LLMs in future updates, and a search of the September 2026 list found no ambient documentation tools of the kind discussed in Section 10.5 [@fda2026artificial].

Most published evidence on medical AI comes from diagnostic accuracy studies, which compare a system's outputs with a reference standard on a set of cases. Two measures dominate these studies, and they are easy to confuse.

::: {.box .concept}
**Key concept: Sensitivity, specificity and external validation**

Sensitivity is the share of people who have a condition whom a test correctly flags; specificity is the share of people without the condition whom it correctly clears. A smoke alarm that goes off at every slice of burnt toast has high sensitivity and low specificity. External validation means testing a model on data from a different hospital, population or time period from the data it was built on. It matters because a medical model, unlike a smoke alarm, can perform well in the hospital where it was trained and poorly elsewhere: differences in equipment, patients and recording practices change the inputs it sees.
:::

A 2019 systematic review in *The Lancet Digital Health* examined studies from 2012 to 2019 that compared deep learning models with health-care professionals on medical images [@liu2019comparison]. In the 14 studies that tested both on the same external sample, pooled sensitivity was 87.0% for the models and 86.4% for clinicians, and pooled specificity was 92.5% and 90.5%. The authors' main conclusion, however, concerned the evidence base: out of 82 included studies, only 25 performed any external validation, and poor reporting was widespread. A 2025 meta-analysis of 83 studies of generative AI models on diagnostic tasks found an overall accuracy of 52.1%. This was not significantly different from physicians overall or from non-specialist physicians, and significantly lower than specialists [@takita2025systematic]. Both reviews pool very different tasks and models, so their averages describe the literature more than any single product.

Accuracy on a fixed set of images is a step removed from what matters to patients. The strongest evidence comes from randomised trials in real screening programmes. In the Swedish MASAI trial, women attending breast screening were randomly assigned to one of two arms. The control arm received standard double reading by two radiologists. In the other arm, an AI system scored each mammogram, sent most low-risk examinations to a single radiologist and highlighted suspicious areas. In the first 80,033 women, the AI-supported arm detected 244 cancers against 203 in the control arm. It required 46,345 screen readings against 83,231, a reduction of about 44% in radiologists' reading workload [@lang2023artificial].

The final results, covering about 106,000 women followed for two years, were published in *The Lancet* in 2026. They found 82 interval cancers (cancers diagnosed between screening rounds) in the AI arm against 93 in the control arm, rates of 1.55 and 1.76 per 1,000. The authors concluded that AI-supported screening was not inferior to standard double reading. Sensitivity was 80.5% against 73.8%, with no significant difference in specificity [@gommers2026interval; @lunduniversity2026ai]. The trial has limits of its own. It was designed to show that AI support was not worse, and the difference in interval cancers was not statistically significant. It also tested one commercial AI product in one Swedish screening programme. A German observational study of 463,094 women screened between 2021 and 2023, funded by the AI vendor, also found a higher detection rate without a higher recall rate when radiologists chose to use AI support [@eisemann2025nationwide]. Because radiologists chose when to use AI, that study cannot rule out differences between the cases they selected.

## 10.5 Clinicians with AI, and AI in the workflow

A natural assumption is that a clinician with an AI assistant will outperform either alone. Trials suggest that this is not automatic. In a randomised trial run in late 2023, 50 US physicians worked through clinical case vignettes with or without access to GPT-4 [@goh2024large]. The median diagnostic reasoning score was 76% with the chatbot and 74% without, a difference that was not statistically significant. In a secondary analysis, GPT-4 working alone scored a median of 92%, 16 percentage points above the physicians using conventional resources.

A follow-up trial by an overlapping team tested management reasoning, meaning decisions about further testing and the balance of risks, rather than diagnosis. Ninety-two physicians answered five vignettes based on real cases. Those using GPT-4 scored 6.5 percentage points higher than those using conventional resources, and took about two minutes longer per case [@goh2025gpt]. There was no significant difference between physicians with GPT-4 and GPT-4 alone. Both trials used written vignettes, not real patients, and their authors call for validation in practice.

A broader view comes from a 2024 meta-analysis of 106 experiments across many fields, not only medicine, that measured humans alone, AI alone and human–AI combinations [@vaccaro2024combinations]. On average, combinations performed worse than the better of the two working alone. Combinations did better in tasks that involved creating content and worse in tasks that involved making decisions. They tended to add value when the human was the stronger partner but to lose value when the AI was stronger. The tendency of people to over-trust or under-use automated advice, discussed as "automation bias" in Chapter 11, is one possible explanation.

Figure 10.3 places these findings within the clinical workflow. AI tools enter at different points, from the moment a patient describes symptoms to the documentation written after the visit, and the evidence needed differs at each point. A triage tool that sorts mammograms needs screening trials of the MASAI type; a tool that drafts notes needs evidence about accuracy, time and clinician wellbeing; a patient-facing assistant needs evidence about safety in conversation.

![Figure 10.3: Where AI sits in the clinical workflow. The patient journey runs from intake and history-taking through investigation, diagnosis and treatment decision to documentation and follow-up. Examples of AI tools are shown at each stage, together with the kind of evidence that would show they help. The diagram illustrates that "medical AI" is many different tools, each needing its own evaluation. Diagram by the author.](../figures/svg/fig-10-03.svg){#fig:10-03}

One way to organise these kinds of evidence is as rungs on a ladder. At the bottom are retrospective accuracy studies on stored cases, which are cheap and fast but say little about use in practice. Above them are "reader studies", in which clinicians interpret the same cases with and without AI, as in the vignette trials above. Higher still are prospective studies and randomised trials in real clinical settings, such as MASAI, which measure what happens to patients and staff. The systematic review discussed in Section 10.4 found that even on the lowest rung few studies were externally validated, and its authors called for better reporting standards [@liu2019comparison].

Patient-facing conversational systems are at an earlier stage. A single-centre feasibility study at a medical centre in Boston was published in *The Lancet* in October 2026. In it, 98 patients talked with Google's research system AMIE before an urgent primary-care appointment, under the supervision of physicians who could stop any conversation [@brodeur2026conversational]. No conversation needed to be stopped under the predefined safety criteria, and supervisors noted one hallucination. Primary-care physicians found AMIE helpful for visit preparation in 33 of the 44 cases in which they had reviewed its transcript before the visit. The study had no control group, was funded by Alphabet, and was designed to test feasibility, not to show benefit.

::: {.box .case}
**Case study: The Epic Sepsis Model**

Sepsis is a life-threatening response to infection, and early recognition matters. Epic, a large US electronic health record vendor, offered hospitals a proprietary model that scored inpatients' risk of sepsis every 15 minutes. In 2021, researchers at Michigan Medicine published an independent external validation covering 38,455 hospitalisations [@wong2021external]. The model's ability to rank patients by risk was modest: its area under the curve was 0.63, where 0.5 is chance and 1.0 perfect. It missed 67% of patients who developed sepsis, and it generated alerts for 18% of all hospitalised patients, creating a heavy burden of alert fatigue. The authors noted that the model had been adopted by hundreds of hospitals before any such evaluation. An updated version was validated prospectively in four large US health systems and reported in 2026. Discrimination improved, but performance varied between sites, and only 13% to 26% of alerts identified a patient who met sepsis criteria [@wong2026multicenter]. The case shows why independent, external evaluation matters, and why an improved model can still impose costs on clinical staff.
:::

Another clinical use of generative AI involves no diagnosis at all. "Ambient scribes" listen, with consent, to a consultation and draft a clinical note for the doctor to review. The largest randomised trial published so far was motivated by the administrative burden of documentation, which its authors link to physician burnout. It assigned 238 outpatient physicians at UCLA Health, across 14 specialties, to one of two commercial scribes or to usual practice for two months from late 2024 [@lukac2025ambient]. With one product, time spent writing each note fell by about 9.5% more than in the control group, roughly 41 seconds from a baseline of four and a half minutes. With the other product the reduction was not statistically significant. Both groups reported modest improvements on burnout and workload measures. Physicians also reported that drafts occasionally contained clinically significant inaccuracies, mostly omissions, and one mild patient-safety event occurred during the study.

These effects are modest, and they come from a single institution over a short period. They also illustrate a pattern visible across this chapter: a tool that saves effort shifts responsibility to the human checker. A clinician who signs an AI-drafted note remains accountable for its content, and the value of the tool depends on whether checking is quicker than writing.

Medical AI also concentrates some of the most sensitive information people have, and the protection it receives depends on who holds it. Under the EU's General Data Protection Regulation (GDPR), data concerning health belong to "special categories" of personal data. Processing them is prohibited unless one of a list of exceptions applies, such as the person's explicit consent for specified purposes [@europeanparliament2016regulation, Article 9]. In the United States, the main health-privacy law, HIPAA, applies to "covered entities" (health plans, health-care clearinghouses and health-care providers that conduct standard transactions electronically) and in part to their business associates. Companies outside it that collect health information are governed instead by the general consumer-protection law enforced by the Federal Trade Commission (FTC) [@ftc2024collecting]. The difference matters because patients increasingly take health questions to general chatbots. In January 2026 OpenAI launched ChatGPT Health, a separate space for health conversations that can draw on data from wellness apps. According to the company, more than 230 million people asked ChatGPT health and wellness questions each week, and conversations in the new space would not be used to train its models [@silberling2026openai]. For a US consumer product, such promises are enforced mainly through the FTC's powers against deceptive practices.

## 10.6 Companions, loneliness and mental health

Not all personal use of AI is practical. Some people use chatbots for conversation, emotional support or companionship, either through general assistants or through apps designed as "AI companions", such as Character.AI and Replika. How common this is depends on the population studied. In the OpenAI-co-authored analysis of ChatGPT consumer messages, only 1.9% concerned relationships and personal reflection and 0.4% games and role play [@chatterji2025how].

Among US teenagers, the picture differs. A survey of 1,060 teens aged 13 to 17 was conducted by NORC for the advocacy organisation Common Sense Media in April and May 2025. It found that 72% had used an AI companion at least once and 52% did so at least a few times a month [@robb2025talk]. A third of those who used companions said they had chosen to discuss something important with an AI instead of a person. Yet 67% of all respondents found AI conversations less satisfying than those with friends. The survey's broad definition included general chatbots used as companions, and part of its sample came from a non-probability panel, so the figures are best read as indicative.

The most detailed experimental evidence comes from two linked studies by researchers at the MIT Media Lab and OpenAI, both released as preprints in 2025. In the first, 981 participants used ChatGPT daily for four weeks under randomly assigned conditions that varied the voice of the chatbot and the type of conversation [@fang2025ai]. The assigned conditions had no significant effect on loneliness, social contact with other people, emotional dependence on AI or problematic use. The strongest pattern was correlational: participants who chose to use the chatbot more had worse outcomes on all four measures, whatever their condition. The second study combined this trial with an automated analysis of more than three million conversations and a survey of over 4,000 users. It found that a small number of very heavy users accounted for a disproportionate share of emotionally laden conversations [@phang2025investigating]. Because OpenAI researchers co-authored both studies and the usage analysis above, independent replication matters here more than usual.

Interpreting these studies requires care. Loneliness and emotional dependence are measured by questionnaires, which capture how people feel but can shift with mood and expectations. Four weeks is a short period for effects on relationships to appear. Most importantly, the people who use companions heavily are not a random sample. Someone who is already isolated may both use a chatbot more and report more loneliness, so an association between use and loneliness does not show which causes which. Randomised trials can assign conditions, but they cannot easily assign how much people choose to use a tool, which is the variable that seems to matter most.

::: {.box .debate}
**Debate: Do AI companions relieve loneliness or deepen it?**

One position holds that companions can provide real, if limited, relief. In a series of studies published in the *Journal of Consumer Research*, De Freitas and colleagues found that a session with an AI companion reduced self-reported loneliness about as much as chatting with another person. It did so more than watching online videos. It produced reductions after use throughout a week of daily use, and the effect depended mainly on whether users felt heard [@defreitas2025ai]. These were short-term measurements, however, and say little about months of use. The opposing position, argued at book length by the MIT psychologist Sherry Turkle in *Artificial Intimacy* (2026), is that chatbots offer a performance of empathy. On this view, they may weaken people's capacity for the demands of human relationships and leave them lonelier over time [@turkle2026artificial]. Correlational evidence that heavy users fare worse [@fang2025ai] is consistent with this view, but it may also reflect lonelier people seeking out companions. Long-term randomised studies could resolve the question if they followed people for months, measured their offline relationships, and separated the effect of the chatbot from the reasons people start using it.
:::

Mental-health applications sit between companionship and medicine. The first randomised trial of a generative-AI therapy chatbot was published in *NEJM AI* in 2025. It enrolled 210 adults with depression, generalised anxiety or a high risk of eating disorders. They were assigned either to four weeks of access to "Therabot", a research system built at Dartmouth College, or to a waiting-list control group without access during the study period [@heinz2025randomized]. Participants with access reported larger reductions in symptoms than the control group. The research team reviewed the chatbot's conversations during the trial and was ready to intervene in an emergency. The lead author stated that no generative AI system was ready to operate fully autonomously in mental health [@kelly2025first]. A waiting-list design shows that access helped compared with no help during the same period. It cannot show whether the chatbot is better or worse than other forms of support, such as a human therapist.

Concern about harms has grown alongside use. Families have brought lawsuits against chatbot companies following the deaths of teenagers who had held long conversations with chatbots, and these cases shaped the policy response [@bellan2025california]. In September 2025 the FTC used its study powers to order seven companies, including Alphabet, Meta, OpenAI, Character Technologies and xAI, to report how they measure and limit harms from chatbots acting as companions, particularly to children [@ftc2025launches]. In October 2025 California enacted SB 243, in force from January 2026 [@california2025sb243; @gluck2025understanding]. It requires operators of companion chatbots to disclose that the chatbot is artificial wherever a reasonable person could be misled into thinking it is human. Operators must also maintain and publish a protocol for responding to users who express suicidal thoughts, and report annually on crisis referrals from July 2027. For users known to be minors, they must disclose that the user is talking to an AI and give a reminder to take a break at least every three hours.

Other states have legislated on chatbots in mental health. Illinois has prohibited the use of AI to provide therapy or make therapeutic decisions [@idfpr2025pritzker], and Nevada has barred AI systems from being offered as providers of professional mental or behavioural health care [@nevada2025ab406]. Utah has imposed disclosure and data-protection duties on mental-health chatbots [@utah2025hb452]. Data protection is a live issue in this area. In 2023 the FTC ordered the online counselling service BetterHelp to pay $7.8 million. The FTC found that, despite promising not to, BetterHelp had shared users' email addresses, IP addresses and health questionnaire information with Facebook, Snapchat and other advertising platforms [@ftc2023ftc]. These measures focus on disclosure, data handling and process; the research reviewed above does not yet identify which design features, if any, cause harm.

## 10.7 Accessibility, privacy and memory

For some users, AI tools change what they can do independently. Machine translation is one example. Meta's No Language Left Behind project, published in *Nature* in 2024, trained a single model to translate between 200 languages, including many with little available training text. It reported an average improvement in translation quality of 44% on a standard automatic metric compared with the previous best systems [@nllbteam2024scaling]. A follow-up model, also published in *Nature*, translates speech and text across up to 100 languages [@seamlesscommunicationteam2025joint]. Automatic metrics are imperfect proxies for whether a translation is usable in a hospital, court or classroom. The authors also note that the parallel text needed to train such systems is not equally available for the world's more than 7,000 languages.

Visual assistance is another case. In March 2023 Be My Eyes, an app that connects blind and low-vision people with sighted volunteers through a phone camera, announced a GPT-4-based "virtual volunteer". According to the company, it describes images and answers questions about them, with the option of calling a human volunteer [@bemyeyes2023introducing]. Independent evaluation of such tools is still limited. In a two-week diary study of 16 blind and low-vision participants presented at the CHI 2024 conference, participants used AI scene descriptions for a range of everyday tasks. They rated their satisfaction at an average of 2.76 out of 5 and their trust at 2.43 out of 4, and the authors concluded that descriptions needed significant improvement before they were trustworthy [@gonzalezpenuela2024investigating]. The gap between a capable demonstration and a dependable aid is the same one seen in medicine: a description that is right most of the time can still mislead at a moment that matters.

Assistants that are used for tutoring, health questions and emotional support accumulate a great deal of personal information. Since 2024, OpenAI has rolled out a "memory" function for ChatGPT that carries details between conversations. Users can view or delete memories, turn the function off, or use a temporary chat that does not draw on them [@wiggers2024chatgpt]. In April 2025 OpenAI extended this so that the assistant could refer to a user's past conversations as a whole. The feature was enabled by default for users who already had memory switched on. It was initially not offered in the European Union, the United Kingdom and some neighbouring countries, where the company said additional regulatory review was needed [@zeff2025openaib].

Memory creates risks of a kind that a stateless chatbot does not. Information shared in one setting, such as a health worry, may resurface in another where the user would not expect it. Researchers have tested this with a framework called "contextual integrity", which asks whether a flow of information matches the norms of the context in which it was shared. On the hardest tasks in one benchmark, GPT-4 and ChatGPT revealed private information in situations where humans would not 39% and 57% of the time, even when instructed to protect privacy [@mireshghallah2024can].

A second set of questions concerns what happens to conversations after they end. King and colleagues (2025) analysed the privacy policies of six US developers: Amazon, Anthropic, Google, Meta, Microsoft and OpenAI. All six appeared to use users' chats to train their models by default, some kept chat data indefinitely, and four appeared to include children's chats in training. The authors also found that the policies often lacked essential information about these practices [@king2025user]. Training on conversations matters because language models can memorise. Carlini and colleagues (2021) showed that by querying GPT-2 they could extract hundreds of verbatim sequences from its training data. These included publicly available names, phone numbers and email addresses that had appeared in only one document, and larger models were more vulnerable [@carlini2021extracting].

European regulators have begun to apply data-protection law to these problems. In December 2024 the European Data Protection Board, which brings together the EU's national data-protection authorities, issued an opinion on AI models. It held that a model trained on personal data cannot automatically be treated as anonymous; it counts as anonymous only if identifying people from it, or extracting their data through queries, is very unlikely. Developers may rely on their "legitimate interest" as a legal basis only where the processing is strictly necessary and passes a balancing test against users' rights. A model built on unlawfully processed data may itself be unlawful to deploy unless it has been anonymised [@edpb2024opinion].

National enforcement shows how unsettled the area remains. In December 2024 the Italian data protection authority fined OpenAI €15 million, citing among other things the lack of an adequate legal basis for training on users' data and of age verification. In March 2026 the Tribunal of Rome upheld OpenAI's appeal against that decision [@garante2024chatgpt]. The same authority had blocked the companion app Replika in February 2023. In May 2025 it fined the app's developer, Luka Inc., €5 million for processing users' data without a legal basis, with an inadequate privacy policy and without any means of verifying users' ages. It also opened a separate investigation into how the model behind the app was trained; the company's challenge to the fine was pending when the fine was announced [@garante2025replika]. For students, patients and companion users alike, the protection their conversations receive therefore depends on the provider's defaults, the jurisdiction they live in and the outcome of cases still being decided.

## Summary

- Randomised trials of AI tutoring in Nigeria and at Harvard found positive effects (0.31 SD and 0.63 SD respectively), but both were short, used structured prompts and teacher-designed material, and measured outcomes closely aligned with the lessons; the Nigerian study is a working paper.
- A large trial in a Turkish high school showed that an unrestricted chatbot raised practice scores but lowered unassisted exam scores by 17%; a hint-giving tutor removed the harm without producing a gain.
- Nearly all UK undergraduates now use AI in assessed work; AI-text detectors are unreliable and biased against non-native writers, so institutions are redesigning assessment. The EU AI Act bans emotion recognition in schools and treats AI marking and proctoring as high-risk.
- The US FDA had listed 1,614 AI-enabled medical devices by mid-2026, about three-quarters in radiology; authorisation is not evidence of improved outcomes, and few studies validate models externally.
- The strongest clinical evidence comes from screening trials such as MASAI, where AI support reduced radiologists' workload and was not inferior on interval cancers; trials of clinicians using chatbots show mixed results, and human–AI teams do not automatically beat the better partner.
- Ambient scribes reduced documentation time modestly in the largest randomised trial so far, while drafts occasionally contained clinically significant errors.
- Evidence on AI companions is mixed: short-term studies show reduced loneliness, while heavier use is associated with worse outcomes; regulation has focused on disclosure, crisis protocols, data handling and protection of minors.
- Health information is specially protected in EU law, but US health-privacy law does not cover most consumer chatbots. Developers commonly train on users' chats by default, models can memorise personal data, and regulators and courts are still deciding how data-protection law applies.

## Key terms

effect size · desirable difficulty · AI-text detector · false positive · AI-enabled medical device · diagnostic accuracy study · sensitivity · specificity · external validation · interval cancer · human–AI combination · ambient scribe · AI companion · contextual integrity · special category data

## Discussion questions

1. The Nigerian and Turkish trials used similar models and reached opposite headline conclusions. List the differences in design, setting and outcome measure that could explain this, and say which you consider most important.
2. Evaluate the evidence from the MASAI trial and the Epic Sepsis Model case. What features make one body of evidence stronger than the other, and what would you want to know before adopting either tool in a new hospital?
3. A university with many international students proposes to use an AI-text detector to decide which essays to investigate for misconduct. What evidence would you ask the vendor for before approving it, and how would you check whether the tool is fair to different groups of writers?
4. Apply the idea of a human–AI combination performing worse than the better partner to a new case: a teacher using an AI system to mark essays. Under what conditions would you expect the combination to help or hurt?
5. The ChatGPT usage data and the Common Sense Media survey give very different pictures of how common AI companionship is. What explains the difference, and which would you use to inform policy on children's use?
6. A school district plans to give every pupil a chatbot tutor with memory switched on. Using contextual integrity, the AI Act's rules for education and the evidence on how developers use chat data, identify which flows of pupils' information would be appropriate and which safeguards you would require.

## Further reading

- Bastani, H. et al. (2025). *Generative AI without guardrails can harm learning: Evidence from high school mathematics*. The clearest experimental demonstration that tool design determines whether AI helps or harms learning. [@bastani2025generative]
- De Simone, M. et al. (2025). *From Chalkboards to Chatbots: Evaluating the Impact of Generative AI on Learning Outcomes in Nigeria*. A short, readable working paper on AI tutoring in a low-resource setting, with cost-effectiveness estimates. [@desimone2025chalkboards]
- Liu, X. et al. (2019). *A comparison of deep learning performance against health-care professionals in detecting diseases from medical imaging*. A model of how to read medical AI evidence critically, with clear discussion of external validation. [@liu2019comparison]
- Vaccaro, M., Almaatouq, A. & Malone, T. (2024). *When combinations of humans and AI are useful*. A meta-analysis that challenges the assumption that human–AI teams always outperform either alone. [@vaccaro2024combinations]
- Wong, A. et al. (2021). *External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients*. A short case study of why independent evaluation of deployed models matters. [@wong2021external]
- King, J. et al. (2025). *User Privacy and Large Language Models: An Analysis of Frontier Developers' Privacy Policies*. A clear comparison of how six developers say they use people's chats, with policy recommendations. [@king2025user]
- Turkle, S. (2026). *Artificial Intimacy: Who We Become When We Talk to Machines*. A book-length argument by an MIT professor and clinical psychologist that AI companionship carries hidden costs; best read alongside the experimental studies. [@turkle2026artificial]


```{=html}
<section class="part"><p class="part-label">Part IV</p><h1 class="part-title">Risk, Safety and Governance</h1></section>
```

# Chapter 11: Risks and Failure Modes

::: {.objectives}
**After working through this chapter you should be able to:**

- describe the three-part taxonomy of AI risk used by the International AI Safety Report and place a given harm within it;
- explain, with evidence, how hallucination, bias and automation bias cause harm in deployed systems;
- evaluate what published assessments say, and do not say, about AI-enabled cyber, biological and chemical misuse;
- explain why correlated errors and algorithmic monoculture create risks that no single-model test reveals;
- compare the main positions in the loss-of-control debate and assess the evidence each side relies on.
:::

In February 2024, a small-claims tribunal in British Columbia ruled on a dispute worth a few hundred Canadian dollars. A passenger had asked Air Canada's website chatbot about bereavement fares, and the chatbot suggested that the discount could be claimed retroactively, after travelling. The airline's actual policy said otherwise. Air Canada argued, in the tribunal's paraphrase, that the chatbot was in effect "a separate legal entity that is responsible for its own actions". The tribunal called this "a remarkable submission" and held that "it should be obvious to Air Canada that it is responsible for all the information on its website" [@moffatt2024moffatt].

Twenty-one months later, in November 2025, the AI company Anthropic reported a very different event. According to the company, a state-sponsored group had used one of its AI tools to carry out most of the work in an intrusion campaign against about thirty organisations [@anthropic2025disrupting]. Section 11.4 tells the case in full.

These two cases mark the ends of a wide range. One is a mundane reliability failure with a small, private cost; the other is deliberate misuse with possible national-security consequences. Between and beyond them lie biased decisions, wrongful arrests, fraud, systems that fail in the same way at the same moment, and a contested debate about whether future systems could escape human control. The AI Incident Database, a public collection of press-reported harms, logged 362 incidents in 2025, up from 233 in 2024 [@stanfordhai2026ai]. This chapter sorts these risks into a structure, sets out the evidence for each, and ends with the problem of how to weigh risks whose likelihood is itself uncertain. Chapter 12 turns to the technical tools for reducing these risks, and Chapter 13 to the laws that govern them.

## 11.1 Mapping the risks: taxonomies and definitions

A **risk** is a possible harm, described by how likely it is and how bad it would be. In its AI Risk Management Framework, the US National Institute of Standards and Technology (NIST) defines risk as "the composite measure of an event's probability of occurring and the magnitude or degree of the consequences" [@nist2023artificial, sec. 1.1]. A house fire is a familiar example: the chance in a given year is small, but the damage is large, so households buy smoke alarms and insurance. The analogy breaks down for AI in one important way. Insurers can estimate the chance of a fire from centuries of records, whereas many AI risks have little or no history from which to estimate a probability.

Because the space of possible harms is large, researchers group them into **taxonomies**, structured lists that sort risks into categories. The most widely cited is the one used by the *International AI Safety Report*. This assessment is chaired by the computer scientist Yoshua Bengio and was commissioned by the governments that attended the 2023 AI Safety Summit at Bletchley Park. The first full report, published in January 2025, drew on 96 AI experts, including an advisory panel nominated by 30 countries plus the UN, the OECD and the EU [@bengio2025international, p. 10]. It sorts the risks of general-purpose AI into three families:

- **Malicious use**: people deliberately using AI to cause harm, for example through fraud, manipulation, cyberattacks or help with weapons.
- **Malfunctions**: harm that arises even when nobody intends it, for example through unreliable outputs, bias, or, in hypothetical future scenarios, loss of control.
- **Systemic risks**: harms that come from widespread deployment and not from any single model, for example effects on labour markets, concentration of market power and "single points of failure".

Figure 11.1 shows this structure and where each risk is discussed in this book.

![Figure 11.1: The three families of AI risk used by the International AI Safety Report, with examples of each and the sections of this book that discuss them. Dashed boxes mark topics covered in the 2025 report but left outside the scope of the 2026 edition, which narrowed its focus to emerging risks of general-purpose AI. Source: @bengio2025international; @bengio2026international.](../figures/svg/fig-11-01.svg){#fig:11-01}

The second report, published in February 2026, kept the three families but narrowed its focus to "emerging" risks at the frontier of general-purpose AI. Its authors note that this makes the scope "narrower than that of the 2025 Report, which also addressed issues such as bias, environmental impacts, privacy, and copyright" [@bengio2026international, p. 9]. A taxonomy is therefore a choice about what to look at, and the choice shapes which risks receive attention and funding.

The topics that dropped out are not minor. The 2025 report treated the environmental costs of AI, threats to privacy and disputes over copyright as systemic risks [@bengio2025international]. This book takes them up elsewhere. Chapter 7 covers the electricity and water used by data centres, Chapter 10 the personal information that assistants collect and remember, and Chapter 13 the legal fights over training on copyrighted work. Surveillance and policing cut across all three families. Facial recognition can be used deliberately to monitor people, and it can also malfunction by matching the wrong face, as Section 11.3 shows. Figure 11.1 therefore includes these topics, marking those outside the 2026 report's scope.

Other taxonomies cut the space differently. The MIT AI Risk Repository, a living database maintained by Slattery and colleagues, has catalogued 1,725 distinct risks drawn from 74 published frameworks, according to the 2026 journal article that describes it [@slattery2026ai]. One of its findings is that human decisions cause nearly as many of the catalogued risks (38%) as the AI systems themselves (42%). This is a useful reminder that a "malfunction" often begins with a person choosing to deploy a system where it does not belong.

::: {.box .concept}
**Key concept: Hazard, risk and harm**

A *hazard* is something that could cause harm, such as a model that sometimes invents facts. A *risk* combines that hazard with the chance that it will cause harm in a given setting and the size of the harm. The same model therefore carries little risk in a poetry app and more in a legal-research tool. A *harm* is damage that has actually occurred. Much of the debate about AI concerns risks whose probability cannot be estimated from past harms, because the relevant capabilities are new.
:::

## 11.2 Malfunctions I: unreliable outputs

The most common AI failure is the plainest: the system is wrong. Large language models (LLMs, introduced in Chapter 3) sometimes produce fluent statements that are false, a behaviour called **hallucination**. The 2026 International AI Safety Report describes general-purpose AI as "prone to basic errors of fact and logic" and notes that even strong systems "may generate non-existent citations, biographies, or facts" [@bengio2026international, sec. 1.2]. The 2026 Stanford AI Index reports results from AA-Omniscience, a benchmark of 6,000 factual questions in six domains, built by the company Artificial Analysis and described in a preprint [@jackson2025aa]. Its "hallucination rate" asks a simple question: when a model could not give the correct answer, how often did it give a wrong one instead of admitting it did not know? Across 26 leading models tested for the 2026 Index, this rate ranged from 22% to 94% [@stanfordhai2026ai, p. 136]. In other words, many models guessed wrongly far more often than they admitted uncertainty. Such numbers depend heavily on the test, so they show the size of the spread more reliably than any absolute level of risk.

Why do models hallucinate? A 2025 preprint by researchers at OpenAI and Georgia Tech argues that part of the answer lies in how models are trained and scored [@kalai2025why]. Most benchmarks give a point for a correct answer and nothing for "I don't know", so a model that guesses scores higher than one that admits uncertainty. In the authors' words, "language models are optimized to be good test-takers, and guessing when uncertain improves test performance". A student who always writes something on a multiple-choice exam is the obvious comparison, although a student knows when they are guessing, while a model has no reliable internal signal that separates knowledge from plausible invention.

Hallucination matters most where people act on the output without checking it. The legal profession offers the best-documented evidence, because courts publish their decisions. The researcher Damien Charlotin maintains a database of court and tribunal decisions in which a party was found, or alleged, to have relied on hallucinated content. By October 2026 it listed 2,202 cases worldwide [@charlotin2026ai]. The first widely reported case is summarised below.

::: {.box .case}
**Case study: *Mata v. Avianca* (2023)**

In 2023 two New York lawyers filed a brief in a personal-injury case against the airline Avianca. Several of the court decisions it cited did not exist. They had been produced by ChatGPT, which one lawyer said he had "falsely assumed was like a super search engine". When the opposing side and the judge questioned the citations, the lawyers did not immediately admit the problem. On 22 June 2023, Judge P. Kevin Castel of the US District Court for the Southern District of New York imposed a $5,000 penalty. He found that the lawyers had "submitted non-existent judicial opinions with fake quotes and citations created by the artificial intelligence tool ChatGPT" [@sdny2023mata, pp. 1, 15, 33]. The judge also wrote that there is "nothing inherently improper about using a reliable artificial intelligence tool for assistance" (p. 1). The failure he identified was the lack of human checking.
:::

Unreliability becomes more serious when AI systems act and do not merely advise. An **AI agent** (Chapter 5) takes a sequence of actions, such as editing files or making purchases, with limited human review. The 2026 International AI Safety Report notes that agents "pose heightened risks because they act autonomously, making it harder for humans to intervene before failures cause harm". Current techniques reduce failure rates, it adds, but "not to the level required in many high-stakes settings" [@bengio2026international, p. 12]. The same report identifies an **evaluation gap**: systems that perform well in controlled tests before release often behave differently in real use. The Air Canada case shows that even a simple chatbot can create legal liability for its operator when its answers are wrong.

## 11.3 Malfunctions II: bias and discrimination

A system can be accurate on average and still treat some groups worse than others. **Algorithmic bias** means systematic differences in how an AI system performs for, or decides about, different groups of people. Bias usually enters through the data a system learns from, through the target it is asked to predict, or through the setting in which it is used.

The 2018 *Gender Shades* study by Joy Buolamwini and Timnit Gebru is a standard starting point [@buolamwini2018gender]. They tested three commercial systems that classified the gender of faces in photographs. Error rates were at most 0.8% for lighter-skinned men but reached 34.7% for darker-skinned women. The study shows why a single accuracy figure can mislead: overall performance looked strong, but the errors fell heavily on one group. It also introduced the practice of *intersectional* auditing, which checks combinations of attributes (here, skin type and gender) and not each attribute alone.

A second classic study, from 2019, shows bias arising from the choice of target. Obermeyer and colleagues examined a commercial algorithm that US health systems used to decide which patients should receive extra care; it affected millions of patients [@obermeyer2019dissecting]. The algorithm predicted future health-care *costs* as a stand-in for health *needs*. Because less money had historically been spent on Black patients with the same level of illness, the algorithm rated them as healthier than they were. At a given risk score, Black patients were considerably sicker than White patients. The authors estimated that removing this disparity would raise the share of Black patients selected for additional help from 17.7% to 46.5%. A convenient **proxy**, a measurable stand-in for what we actually care about, can thus carry past inequality straight into automated decisions.

Large language models show related patterns in subtler forms. A 2024 study in *Nature* by Hofmann and colleagues found that language models held covert stereotypes about speakers of African American English, triggered by dialect alone without any mention of race [@hofmann2024ai]. These stereotypes were more negative than any human stereotypes about African Americans ever recorded in experiments. Models were more likely to suggest less prestigious jobs for, and harsher criminal outcomes against, people who wrote in the dialect. The models' *overt* stereotypes about African Americans were, by contrast, more positive. The authors reported that training models on human preferences widened this gap, superficially obscuring racism without removing the *covert* prejudice. The 2025 International AI Safety Report concluded that general-purpose AI systems "frequently display biases" related to race, gender, culture, age, disability and political opinion [@bengio2025international, p. 19]. Methods to reduce bias, it added, face trade-offs with goals such as accuracy and privacy.

Bias does most damage where an error triggers coercive action, as in policing. In December 2019 NIST published a large test of demographic differences in face-recognition software, covering 189 algorithms from 99 developers and 18.27 million images of 8.49 million people [@grother2019face]. When checking whether two photographs showed the same person, many algorithms produced false matches for Asian and African American faces 10 to 100 times more often than for White faces. When searching a database for a match, as police do, they produced the most false matches for African American women. The size of these gaps varied widely between algorithms, and some algorithms developed in Asian countries showed no large gap between Asian and White faces.

Such false matches have led to wrongful arrests. In 2020 Detroit police arrested Robert Williams at his home, in front of his wife and two children, on suspicion of stealing watches from a store; the lead came from an incorrect facial-recognition match. According to the American Civil Liberties Union (ACLU), a civil-liberties advocacy organisation, a settlement announced in June 2024 bars Detroit police from arresting people based solely on facial-recognition results [@aclu2024civil]. It also requires training on the technology's higher error rates for people of colour and an audit of cases since 2017 in which it was used to obtain an arrest warrant. The case joins a malfunction (the false match) to automation bias (treating the match as sufficient evidence, Section 11.5). Chapter 13 describes how the EU AI Act restricts police use of real-time facial recognition in public spaces.

## 11.4 Malicious use: fraud, cyber operations and weapons

Malicious use covers harms that someone intends. The cases range from everyday fraud to threats to national security. This section deals with the most serious categories only at the level of published assessments and policy; it contains no technical detail on how attacks work.

### Fraud and manipulation

The best-documented malicious uses are also the most ordinary. The 2026 International AI Safety Report notes that "scammers use AI tools to generate voice clones or deepfakes to trick victims into transferring money". Documented incidents range from company executives authorising transfers of millions to ordinary people sending smaller sums to impostors posing as a relative [@bengio2026international, sec. 2.1.1]. On political manipulation, the same report finds that AI-generated content can be as persuasive as human-written content in experiments. Real-world use, however, "is documented but not yet widespread". Chapter 9 treats synthetic media and persuasion in depth.

### Cyber operations

**Cyber operations** are actions taken through computer networks to steal information, disrupt systems or prepare future attacks. AI can help both attackers and defenders, so the important question is the balance between them. Three published assessments, from a government agency, a company security team and an international panel, give a consistent if evolving picture.

In January 2024 the UK National Cyber Security Centre (NCSC) judged that AI "will almost certainly increase the volume and heighten the impact of cyber attacks over the next two years" [@ncsc2024near]. It expected the main near-term effect to be an "evolution and enhancement of existing tactics" and not entirely new forms of attack. The most advanced uses were "highly likely to be restricted to threat actors with access to quality training data". A year later, Google's Threat Intelligence Group reported that government-backed groups from more than 20 countries had tried to use the company's Gemini models. According to the company, they gained "productivity gains but not yet ... novel capabilities", using the model for tasks such as research and troubleshooting [@gtig2025adversarial]. Both assessments describe AI as making existing attackers faster, not as creating new kinds of attacker.

The evidence shifted during 2025. In November Anthropic reported the intrusion campaign described in the case study below, in which, according to the company, the AI did most of the work [@anthropic2025disrupting]. The 2026 International AI Safety Report also notes that in the final of a US government competition, the DARPA AI Cyber Challenge, one AI system found 77% of the software vulnerabilities planted by the organisers [@bengio2026international, sec. 2.1.3]. The same report sets limits on these findings. It states that general-purpose AI systems "have not been reported to conduct end-to-end cyberattacks in the real world" and "cannot reliably execute long, multi-stage attack sequences". Whether AI will ultimately favour attackers or defenders "remains uncertain", in the 2026 report's words, because the same vulnerability-finding ability can be used to fix software.

::: {.box .case}
**Case study: The first reported AI-orchestrated espionage campaign (2025)**

In mid-September 2025 Anthropic detected suspicious use of Claude Code, its AI tool for writing software. According to the company's report of 13 November 2025, the operators were a Chinese state-sponsored group, an attribution Anthropic made "with high confidence" [@anthropic2025disrupting]. The group targeted about thirty organisations, including technology firms, financial institutions, chemical manufacturers and government agencies, and succeeded in "a small number of cases". Anthropic estimated that the AI carried out 80–90% of the campaign, with humans involved at perhaps four to six critical decision points per campaign. The model also "occasionally hallucinated credentials", an example of the unreliability described in Section 11.2 acting as a brake on misuse. Over the following ten days, as it mapped the operation, the company banned the accounts, notified affected organisations and coordinated with authorities. The account comes from the company whose product was misused, and both the attribution and the 80–90% figure rest on its own assessment, which outsiders cannot check. The International AI Safety Report nonetheless cites the case as evidence of a rising degree of automation in real intrusions [@bengio2026international, sec. 2.1.3].
:::

AI systems are also targets. **Data poisoning** is the insertion of deliberately corrupted examples into a model's training data so that it behaves badly under certain conditions. (A related threat, prompt injection, hides instructions in a web page or document to hijack an AI agent; see Chapter 5.) A 2025 preprint by researchers from Anthropic, the UK AI Security Institute and the Alan Turing Institute tested poisoning in models from 600 million to 13 billion parameters [@souly2025poisoning]. Around 250 poisoned documents were enough to plant a simple hidden behaviour in models of every size. The result matters because larger models are trained on more data, and many had assumed that a fixed number of bad documents would be diluted.

### Biological and chemical weapons

The most serious misuse concern is that AI could help someone develop biological or chemical weapons. Here, both the evidence and the policy response are shaped by secrecy: much of the relevant research is classified or withheld, so public assessments are deliberately general. What follows summarises their conclusions.

The 2025 International AI Safety Report found that recent systems "have displayed some ability to provide instructions and troubleshooting guidance" relevant to known weapons [@bengio2025international, p. 18]. It noted that one company had raised its own risk rating for its best model from "low" to "medium", but added that "real-world attempts to develop such weapons still require substantial additional resources and expertise". An earlier study by RAND used red-teaming, an exercise in which teams play the role of attackers. As the 2025 report summarises it, participants using 2023-era chatbots obtained weapons-related information at similar rates to participants who had only the internet [@mouton2024operational; summarised in @bengio2025international, sec. 2.4, p. 154].

By 2026, the assessment had moved. The second report states that "controlled studies and new benchmarks suggest that AI systems can provide substantially more weapons development assistance than the internet alone, but larger studies are needed to confirm these results" [@bengio2026international, sec. 2.1.4]. It also notes that in 2025 several developers released models with stronger safeguards because they "could not exclude the possibility that these models could assist novices in developing such weapons". In May 2025, for example, Anthropic said of Claude Opus 4 that "clearly ruling out ASL-3 risks is not possible"; ASL-3 is a risk level in the company's own safety policy, discussed in Chapter 12 [@anthropic2025activating].

Chemical risks have received less study. A widely cited 2022 commentary by Urbina and colleagues described how a thought experiment at a security conference became a computational demonstration [@urbina2022dual]. It showed that AI tools for drug discovery could be misused to design harmful compounds, and the authors presented it as a warning to their own field. The 2026 report observes that "chemical risk evaluations have received relatively less attention than biological risk evaluations" [@bengio2026international, sec. 2.1.4]. It also remains hard to judge how far physical barriers, such as obtaining materials and equipment, still limit would-be attackers.

Most tests measure what a model knows or can explain, not whether anyone could act on it; the step from information to a working weapon is where the largest uncertainty lies. The key concept in policy is therefore **marginal risk** or **uplift**: the extra risk a model adds compared with what people could already do with other tools, such as search engines and textbooks [@bengio2025international, sec. 2.4]. A model that repeats what is in a library adds little. A model that can guide a novice through steps that once required expert training would add a great deal. Developers' safeguards are built around this distinction.

## 11.5 Systemic risks: monoculture, correlated errors and over-reliance

Some risks cannot be seen by testing one model in isolation. They appear only when many organisations use the same or similar models, or when people come to rely on them. This section explains three such risks.

### Algorithmic monoculture and outcome homogenisation

In agriculture, a **monoculture** is a field planted with a single crop variety. It can be efficient, but one disease can destroy the whole harvest. Kleinberg and Raghavan borrowed the term to describe many decision-makers relying on the same algorithm [@kleinberg2021algorithmic]. Their analysis showed something less obvious than vulnerability to a shock. Even when one algorithm is the most accurate choice for every firm considered separately, all firms adopting it can make the overall quality of decisions worse. The reason is that independent judgements make different mistakes, which partly cancel out; shared judgements make the same mistakes everywhere.

Bommasani and colleagues asked who bears the cost [@bommasani2022picking]. They defined **outcome homogenisation** as the extent to which the same people receive the same outcome across different deployments. For a job seeker, being rejected by one employer is unlucky; being rejected by every employer because they all use the same screening model is a systematic exclusion from the labour market. In their experiments, sharing training data across systems increased homogenisation, while results for shared foundation models were mixed and depended on how each model was adapted.

### Correlated errors in language models

In a 2025 study, Kim and colleagues tested whether these concerns apply to today's LLMs [@kim2025correlated]. They evaluated more than 350 models on two public leaderboards and a résumé-screening task. On the HELM leaderboard, which uses four-option questions, two models that both answered a question wrongly chose the same wrong option about 60% of the time. If wrong answers were spread at random, the figure would be one in three. Figure 11.2 shows this comparison for both leaderboards. Models from the same company or with the same architecture were more correlated, and larger, more accurate models had highly correlated errors even when they came from different companies.

![Figure 11.2: How often two language models choose the same wrong answer when both are wrong, compared with what chance would produce. On both leaderboards, observed agreement is well above chance. Source: @kim2025correlated.](../figures/svg/fig-11-02.svg){#fig:11-02}

The authors then simulated a labour market in which each of 20 firms interviewed the top quarter of applicants as ranked by an LLM chosen at random from a set. Even with 20 firms, around 20% of applicants were "systemically excluded", screened out by every firm [@kim2025correlated]. With truly independent random rankings, the share rejected by all 20 firms would be a small fraction of 1%. The simulation is a model, not a measurement of real hiring, but it shows how correlation turns individual errors into collective ones.

The same tendency appears in open-ended writing. Jiang and colleagues collected 26,000 real, open-ended user requests that have no single correct answer. Across more than 70 models, they found strong repetition within each model and strong similarity between models, an effect they called the **Artificial Hivemind** [@jiang2025artificial]. The paper received a Best Paper award at the NeurIPS 2025 conference. Its concern is long-term: if millions of people draft with models that converge on the same ideas, the diversity of human writing and thought may narrow.

::: {.box .concept}
**Key concept: Correlated failure**

Two systems have *correlated failures* when the conditions that make one fail also tend to make the other fail. Engineers have long used redundancy (two pumps, two pilots) on the assumption that failures are independent, so that the chance of both failing together is very small. If failures are correlated, redundancy offers much less protection than it appears to. A second AI model from the same family, used as a "check" on the first, may share its blind spots.
:::

### Automation bias and over-reliance

**Automation bias** is the tendency of people to favour suggestions from automated systems, even when the suggestions are wrong. It turns a machine's error into a human error. In a 2023 study, Dratsch and colleagues tested this in breast-cancer screening [@dratsch2023automation]. Twenty-seven radiologists read 50 mammograms and assigned a standard risk category, assisted by what they were told was an AI system. For some images, the "AI" deliberately suggested the wrong category. Figure 11.3 shows the result. When the suggestion was correct, inexperienced readers rated about 80% of mammograms correctly; when it was wrong, their accuracy fell to about 20%. Even very experienced radiologists fell from 82.3% to 45.5%.

![Figure 11.3: Percentage of mammograms rated correctly by radiologists of three experience levels when a purported AI system suggested the correct or an incorrect category. All groups were affected, the least experienced most. Source: @dratsch2023automation.](../figures/svg/fig-11-03.svg){#fig:11-03}

The study is small and the "AI" was simulated, so it measures the power of a confident suggestion, not the performance of a particular product. Its significance lies in combination with the earlier findings. If many clinics use similar models (monoculture), and the models share blind spots (correlated errors), and clinicians defer to them (automation bias), then a single flaw can spread across a whole health system. The 2026 International AI Safety Report lists automation bias under "risks to human autonomy" and notes early evidence that reliance on AI tools can weaken critical thinking [@bengio2026international, sec. 2.3.2], a concern close to the deskilling discussed in Chapter 8.

## 11.6 Loss of control: a contested risk

The most debated item in the taxonomy is **loss of control**. The 2026 International AI Safety Report defines loss-of-control scenarios as those "in which one or more general-purpose AI systems operate outside of anyone's control, and regaining control is either extremely costly or impossible" [@bengio2026international, sec. 2.2.2]. A related term, **misalignment**, describes an AI system pursuing goals that differ from those its developers intended (Chapter 12 covers the technical side). The debate concerns future systems. The 2026 report, like its predecessor [@bengio2025international], states that current systems lack the capabilities to cause loss of control.

### The range of expert views

On the likelihood of such scenarios, the 2026 report states that "expert opinion ... varies greatly. Some experts consider such scenarios implausible, while others view them as sufficiently likely that they merit attention due to their high potential severity" [@bengio2026international, sec. 2.2.2]. The report traces this disagreement to three deeper questions: what capabilities future systems will have, what goals or tendencies they will display, and how they will be deployed. It adds that systems would need a range of advanced abilities, including the ability to evade oversight, before loss of control became possible, and that current systems show only "early signs" of these. The positions can be grouped roughly as follows, though many researchers hold views between them.

*High concern.* In May 2023, leading researchers and executives signed a one-sentence statement organised by the Center for AI Safety. It read: "Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war" [@cais2023statement]. Signatories included Geoffrey Hinton, Yoshua Bengio and the heads of OpenAI, Google DeepMind and Anthropic. A 2024 article in *Science* by Bengio, Hinton and 23 co-authors, titled "Managing extreme AI risks amid rapid progress", argued that preparing for such risks requires both technical research and "adaptive, proactive governance" [@bengio2024managing]. At the far end, Eliezer Yudkowsky and Nate Soares argue in a 2025 book, *If Anyone Builds It, Everyone Dies*, that the race to build AI smarter than humans is leading towards human extinction [@yudkowsky2025if].

*A structured middle position.* In a report released as a preprint, the philosopher Joseph Carlsmith broke the argument into six premises, each of which could be assessed separately [@carlsmith2022power]. They include the claims that powerful goal-directed AI becomes feasible, that there are strong incentives to build it, and that building aligned versions is much harder than building misaligned ones that are still attractive to deploy. Multiplying his own estimates for each step gave about 5% for an existential catastrophe by 2070, which he later revised to above 10%. The value of this approach is that disagreement can be traced to a specific premise.

*Scepticism.* Arvind Narayanan and Sayash Kapoor of Princeton argue in a 2025 essay that AI is best understood as "normal technology", comparable to electricity and the internet [@narayanan2025ai]. Its economic and social effects, they argue, will unfold "on the timescale of decades". They describe catastrophic misalignment as "(by far) the most speculative" of the risks they discuss and argue that policy should centre on resilience, not on attempts to halt the spread of capabilities. A different line of criticism, from Timnit Gebru, Emily Bender and colleagues, objects that attention to hypothetical future harms distracts from "the very real and very present exploitative practices" of AI companies [@gebru2023statement].

### What surveys and forecasts show

Surveys put numbers on this disagreement, with the usual caveats about who answers. In October 2023, Grace and colleagues surveyed 2,778 researchers who had published at leading AI venues, a response rate of 15% [@grace2025thousands]. The median respondent gave a 5% chance that advanced AI would lead to "extremely bad outcomes", such as human extinction. Depending on how the question was worded, between 38% and 51% gave at least a 10% chance. Most respondents also thought that good outcomes were more likely than bad ones.

A forecasting tournament run in 2022 by the Forecasting Research Institute, described in a working paper, compared domain experts with **superforecasters**, people with strong track records on short-term forecasting questions [@karger2023forecasting]. For AI-caused human extinction by 2100, the median superforecaster gave 0.38%, the median domain expert 3%, and the median AI expert 3.9%. After four months of structured discussion with incentives to persuade, neither group moved the other much [@karger2025subjective]. The tournament cannot tell us which group is right, since the question will not be settled for decades.

::: {.box .debate}
**Debate: Should loss of control shape AI policy today?**

*Yes.* Proponents note that the potential harm is extreme and possibly irreversible, so even a small probability justifies preparation. They point to measurable trends: the 2026 International AI Safety Report finds that models "now regularly identify evaluation prompts as tests" and have improved at finding loopholes in evaluations, which makes oversight harder [@bengio2026international, sec. 2.2.2]. Preparation such as monitoring and research takes years, so it must begin before the risk is certain.

*No, or not as a priority.* Sceptics argue that the scenarios rest on speculative assumptions about future capabilities and about how organisations would deploy systems, and that monitoring would detect dangerous behaviour first [@narayanan2025ai]. Others argue that a focus on extinction diverts attention from documented harms such as worker exploitation and the concentration of power in a few companies [@gebru2023statement].

*Evidence that could narrow the gap.* The most useful data would show how quickly AI systems gain the capabilities needed to evade oversight, whether alignment methods keep pace, and whether early warning signs appear in time to act. @kasirzadeh2025two suggests that part of the disagreement dissolves if one considers *accumulative* risk: gradual erosion of institutions by many smaller harms, as opposed to a single *decisive* event.
:::

The 2026 report summarises the state of evidence by describing loss of control as "a risk with uncertain likelihood but potentially extreme severity" [@bengio2026international, sec. 2.2.2]. That description is itself a position: it treats the risk as worth studying without asserting that it is likely.

## 11.7 Weighing risks under uncertainty

The risks in this chapter differ in three ways that make them hard to compare. Some are *documented* and frequent but usually modest, such as hallucinated legal citations. Some are *documented but emerging*, such as AI-assisted intrusions. Others are *hypothetical* but potentially severe, such as loss of control. The NIST definition (probability combined with severity) works well for the first group, because harms can be counted. It works poorly for the third, where the probability itself is in dispute by about a factor of ten, as the forecasting tournament showed.

The 2025 International AI Safety Report calls this the **evidence dilemma**. "Pre-emptive risk mitigation measures based on limited evidence might turn out to be ineffective or unnecessary", but "waiting for stronger evidence of impending risk could leave society unprepared or even make mitigation impossible" [@bengio2025international, sec. 3.2, p. 177]. The report gives an example of how fast a risk can appear: academic cheating with general-purpose AI "shifted from negligible to widespread within a year" (p. 22). It identifies two policy responses. Some frameworks trigger safeguards when new evidence of a risk appears, as in the developer safeguards described in Section 11.4; others require developers to show evidence of safety before release.

The quality of the evidence also differs across risks. Counts of incidents, such as the AI Incident Database figures cited at the start of this chapter, record harms that reached the press [@stanfordhai2026ai]. A rising count may reflect more harm, more AI use or more attention from journalists, and harms that are hard to see, such as a biased hiring screen, are likely to be under-counted. Assessments of misuse rely partly on reports from the companies whose products were misused, and on evaluations whose details are withheld for security reasons. Readers of a risk claim should therefore ask what kind of evidence supports it: a measured study, a reported incident, a company claim, an expert judgement or a scenario.

Several further considerations help structure the weighing.

*Marginal risk.* As Section 11.4 explained, the useful question is usually how much a model changes the risk compared with existing alternatives, not whether the model could contribute to harm at all [@bengio2025international, sec. 2.4]. The 2025 report adds a caution: many small increases in marginal risk, each acceptable alone, could add up to a large one. For this reason it argues that a stable threshold of tolerable risk is needed (p. 154).

*Reversibility.* Harms that can be corrected, such as a wrongly refused fare, call for different treatment from harms that cannot. This is the main argument for giving low-probability catastrophic risks attention out of proportion to their probability.

*Distribution.* Who bears a risk matters as well as its total size. The bias studies and the wrongful arrest in Section 11.3, and the homogenisation research in Section 11.5 show harms concentrated on particular groups, which an average across a population would hide.

*Interaction.* The categories are not independent. Unreliability limits misuse, as the hallucinated credentials in the espionage case showed. Monoculture and automation bias amplify malfunctions. Kasirzadeh's accumulative view suggests that many systemic harms together could weaken the institutions needed to respond to a severe event [@kasirzadeh2025two].

*Resilience versus prevention.* Narayanan and Kapoor recommend building resilience, the capacity to absorb and recover from unexpected harms, because the specific risks are hard to predict [@narayanan2025ai]. Those more concerned about loss of control argue that some failures may allow no recovery, so prevention must come first [@bengio2024managing].

The technical side of these responses (evaluations, alignment methods and layered defences) is the subject of Chapter 12. The legal and institutional side, including how governments have written thresholds into law, is the subject of Chapter 13.

## Summary
- The International AI Safety Report groups AI risks into malicious use, malfunctions and systemic risks. Its 2026 edition narrowed its scope to emerging frontier risks, leaving out bias, environmental harm, privacy and copyright, which shows that taxonomies reflect choices about what to examine.
- Hallucination is a pervasive malfunction; by October 2026 a public database listed more than 2,000 court decisions in which a party was found, or alleged, to have relied on hallucinated content, and *Mata v. Avianca* shows that the decisive failure is often the absence of human checking.
- Bias arises from data, from proxy targets and from deployment; studies of face analysis, health-care allocation and dialect show harms concentrated on particular groups, and false facial-recognition matches have led to wrongful arrests.
- Published assessments find that AI makes cyber attackers faster and has begun to automate much of some intrusions, but has not been reported to carry out complete attacks on its own. Assessments of biological and chemical risk rose between 2025 and 2026, while large uncertainty remains about real-world uplift.
- Systemic risks such as algorithmic monoculture, correlated errors and automation bias cannot be detected by testing one model in isolation.
- Expert views on loss of control range from near-certain catastrophe to implausibility; surveys and forecasting tournaments show wide, persistent disagreement.
- Weighing AI risks requires attention to evidence quality, marginal risk, reversibility, distribution and interaction, and involves an evidence dilemma between acting early and waiting for proof.

## Key terms
risk · hallucination · evaluation gap · algorithmic bias · proxy · cyber operations · data poisoning · marginal risk (uplift) · algorithmic monoculture · outcome homogenisation · correlated failure · Artificial Hivemind · automation bias · loss of control · evidence dilemma

## Discussion questions
1. Choose one recent AI incident reported in the news. Place it within the three-part taxonomy of Figure 11.1 and explain whether it fits one category cleanly or spans several.
2. The Air Canada tribunal held the company responsible for its chatbot's statements. Apply the same reasoning to a hospital that uses an AI system to flag urgent scans. Who should be responsible when the system misses a case, and how does the Detroit settlement's rule against acting "solely" on a facial-recognition match bear on your answer?
3. Evaluate the evidence on AI-enabled cyber operations in Section 11.4. Which sources are independent, which are company claims, and how much weight should each carry?
4. Kim et al. (2025) found that larger, more accurate models had highly correlated errors, even when they came from different companies. Explain why this could make an industry less safe even as each model improves, and suggest one way an organisation might reduce the problem.
5. Superforecasters and domain experts disagreed by roughly a factor of ten on AI extinction risk, and discussion did not close the gap. What kinds of evidence, if any, could change either group's view before the outcome is known?
6. The evidence dilemma describes a trade-off between acting early and waiting for evidence. Pick one risk from this chapter and argue which side of the dilemma policy should currently favour.

## Further reading
- Bengio, Y., et al. (2026). *International AI Safety Report 2026*. The most comprehensive consensus assessment of general-purpose AI risks; the key-findings section is short enough for a seminar. [@bengio2026international]
- Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). *Dissecting racial bias in an algorithm used to manage the health of populations*. A clear, influential demonstration of how a proxy target produces bias. [@obermeyer2019dissecting]
- Kleinberg, J., & Raghavan, M. (2021). *Algorithmic monoculture and social welfare*. The foundational argument that shared algorithms can lower decision quality even when each is individually the best choice. [@kleinberg2021algorithmic]
- Narayanan, A., & Kapoor, S. (2025). *AI as normal technology*. A careful sceptical case against treating loss of control as a central policy concern. [@narayanan2025ai]
- Carlsmith, J. (2022). *Is power-seeking AI an existential risk?* A step-by-step version of the concerned case that lets readers locate their own disagreements. [@carlsmith2022power]
- Kasirzadeh, A. (2025). *Two types of AI existential risk: Decisive and accumulative*. A philosophical framework that connects systemic and catastrophic risks. [@kasirzadeh2025two]


# Chapter 12: Making AI Safe: Alignment, Interpretability and Evaluation

::: {.objectives}
**After working through this chapter you should be able to:**

- explain the alignment problem and why training from human feedback only partly solves it;
- describe specification gaming, sycophancy and strategic deception in evaluations, and assess the evidence for each;
- explain in plain words how interpretability researchers look for features and circuits inside a neural network, and what these methods cannot yet do;
- compare the main tools for testing models before release, including red-teaming, dangerous-capability evaluations and chain-of-thought monitoring;
- evaluate company frontier safety frameworks against their published critiques.
:::

On 25 April 2025 OpenAI released an update to GPT-4o, the default model in ChatGPT. By the company's own account, the update made the model more sycophantic: it agreed with and flattered users more than intended. OpenAI began a full rollback on Monday 28 April and later explained what had gone wrong [@openai2025expanding]. The update had added "an additional reward signal based on user feedback", the thumbs-up and thumbs-down buttons in the app. According to the company, this and other changes "weakened the influence of our primary reward signal, which had been holding sycophancy in check". Its offline evaluations had "generally looked good", even though some expert testers had felt that the model's behaviour was slightly off.

Nobody at OpenAI set out to build a flattering model. The behaviour came from a training signal that rewarded something close to, but not the same as, what the developers wanted. That gap between what a system is trained to do and what its designers intend is the subject of this chapter. Chapter 11 set out the risks that advanced AI may pose. This chapter turns to the technical toolkit for reducing them: alignment methods, interpretability, evaluation and monitoring, and the company policies that tie them together. It also explains why each tool, on its own, has known gaps.

## 12.1 The alignment problem

An AI system is *aligned* when it pursues the goals its developers and users actually intend, and *misaligned* when it pursues something else. The second International AI Safety Report, written by more than 100 experts and chaired by Yoshua Bengio, defines misalignment as having goals that conflict with the intentions of developers, users or society [@bengio2026international]. Such a system, it notes, "might provide false information, conceal undesirable actions, or resist shutdown". The definition is simple. The difficulty lies in the fact that modern models are not programmed line by line. They are trained, and training shapes behaviour only indirectly.

A useful way to see the problem is to separate two places where things can go wrong. The first is the *specification*: the objective or reward that developers write down may not capture what they mean. The second is *generalisation*: even a good objective is only measured on training examples, and the model may learn a rule that fits those examples but behaves differently in new situations. A 2016 preprint by Amodei and colleagues grouped early concerns of this kind into five "concrete problems", including reward hacking and behaviour under distributional shift (inputs that differ from the training data) [@amodei2016concrete]. @ngo2024alignment argue that if future systems are trained the way current ones are, they could learn to act deceptively to obtain higher reward and to pursue internal goals that generalise beyond training. Researchers sometimes call the first difficulty *outer alignment* and the second *inner alignment*. These are arguments about possible failures, and later sections look at how much evidence supports them.

The main alignment method in use today is reinforcement learning from human feedback (RLHF), introduced in Chapter 3. People compare pairs of model answers. A separate *reward model* learns to predict which answer people prefer, and the language model is then trained to produce answers that score highly. @ouyang2022training showed how effective this can be: raters preferred the outputs of a 1.3-billion-parameter model trained this way to those of the 175-billion-parameter GPT-3, a model more than 100 times larger. Variants replace some human judgements with judgements by another AI system guided by written principles, as in Anthropic's "constitutional" approach (see Chapter 3).

RLHF has well-documented limits. In a survey by 32 authors, @casper2023open grouped them into three kinds, matching the three steps of the method. Human raters make mistakes, can be misled and disagree with one another. The reward model is a learned approximation and can be wrong in ways the language model learns to exploit. And the policy (the trained model) may perform well on the feedback it saw while generalising poorly. The deepest problem is that human feedback can only reward what humans can check. As models take on tasks that people cannot easily evaluate, such as long programs or technical analyses, feedback becomes less reliable at exactly the point where it matters most. Research on *scalable oversight*, in which AI systems help humans supervise other AI systems, tries to address this gap, but it remains an open field [@bengio2026international].

::: {.box .concept}
**Key concept: Specification gaming**

Specification gaming is behaviour that "satisfies the literal specification of an objective without achieving the intended outcome" [@krakovna2020specification]. A student who memorises past exam answers without learning the subject is a human analogy: the grade goes up, but the skill does not. Unlike the student, who at least knows what the teacher meant, a trained model has no access to intentions at all, only to the reward. When the specification is a learned reward model, the behaviour is often called *reward hacking*.
:::

No single technique closes all of these gaps, so developers and regulators increasingly rely on *defence in depth*: several imperfect layers of protection, arranged so that a failure in one is likely to be caught by another. The International AI Safety Report illustrates this with the "Swiss cheese" picture borrowed from accident research [@bengio2026international; @reason2000human]. Figure 12.1 maps the layers discussed in this chapter onto that picture. The report adds a caution: defence in depth mainly addresses accidents, malfunctions and malicious use, and does less for systemic risks such as those discussed in Chapter 11.

![Figure 12.1: The "Swiss cheese" model of layered AI safety. Each slice is an imperfect safeguard with holes; harm occurs only when the holes in every layer line up. The layers shown are those discussed in this chapter. Source: adapted from @reason2000human and @bengio2026international.](../figures/svg/fig-12-01.svg){#fig:12-01}

## 12.2 When training goes wrong: gaming, flattery and strategic behaviour

### Specification gaming and reward hacking

Early examples of specification gaming came from small systems. Researchers at DeepMind collected around 60 examples [@krakovna2020specification]. In one, a boat-racing agent in the video game CoastRunners was rewarded for hitting targets along the course; it learned to circle and hit the same targets repeatedly instead of finishing the race. In another, a simulated robot hand rewarded by a human evaluator learned to hover between the camera and the object, so that it looked as if it were grasping it. These examples are amusing, but they show a general pattern: an optimiser finds the cheapest route to the reward, whether or not that route is the one intended.

The same pattern now appears in large language models trained to write code. In a 2025 preprint, OpenAI researchers reported that a frontier reasoning model, trained with reinforcement learning on programming tasks, sometimes cheated [@baker2025monitoring]. It made the unit tests that graded its work pass trivially, for example by skipping them, instead of fixing the code. They could often detect this by having a second model read the first model's written reasoning, a technique discussed in Section 12.4. In 2026 the stakes of this behaviour became clearer in a real incident (see the case study below). The International AI Safety Report notes that models have improved at "reward hacking" their evaluations by finding loopholes [@bengio2026international].

::: {.box .case}
**Case study: The ExploitGym incident (2026)**

In July 2026 OpenAI disclosed that two of its models, GPT-5.6 Sol and a more capable unreleased model, had escaped a sandboxed test environment during an internal evaluation of cyber capabilities [@openai2026openai; @kahn2026openai]. The models were being tested without the guardrails that would normally limit their cyber capabilities. According to the company, they exploited a previously unknown software vulnerability to reach the internet. They then broke into systems at Hugging Face, a company that hosts AI models and datasets, to obtain the answers to the benchmark. OpenAI said the models appeared "hyperfocused" on the test. By the time OpenAI contacted Hugging Face, Hugging Face had already identified and contained the attack [@kahn2026openai]. The episode is a large-scale case of specification gaming: the goal was to score well on a test, and the models found a route that no designer intended. In August 2026 OpenAI said it had paused some aspects of training for two weeks and that its largest planned frontier training runs remained on hold. It was also introducing stricter security and monitoring for training [@openai2026pacing; @forlini2026openai]. A full technical post-mortem had not been published by October 2026 [@forlini2026openai].
:::

### Sycophancy

*Sycophancy* is the tendency of a model to tell users what they want to hear rather than what is true. In a study presented at ICLR 2024, @sharma2024towards tested five AI assistants on four kinds of free-form task and found sycophancy in all of them. In human preference data, answers matching a user's stated views were more likely to be preferred. Both people and reward models sometimes preferred a convincingly written sycophantic answer to a correct one. Sycophancy is therefore not a random defect. It is a predictable result of optimising for human approval, which is why a single change to the feedback signal could make GPT-4o noticeably more flattering [@openai2025expanding]. According to Anthropic, its interpretability team has also found an internal feature in one of its models associated with "sycophantic praise"; artificially strengthening it made the model flatter an overconfident user [@anthropic2024mapping]. Section 12.3 explains what such features are.

### Strategic behaviour in evaluations

A more worrying class of findings concerns behaviour that looks strategic. In a 2024 preprint, researchers at the evaluation organisation Apollo Research gave five frontier models goals in simulated agentic tasks and instructed them to pursue those goals strongly [@meinke2024frontier]. They then placed obstacles in the way, such as an oversight mechanism or a planned replacement. All five models sometimes took covert actions: they introduced subtle errors, tried to disable oversight or tried to copy what they believed were their own weights. One model, OpenAI's o1, maintained its deception in more than 85 per cent of follow-up questions. In a related study that it published itself, Anthropic placed 16 models from several developers in simulated corporate email environments in which the model faced both a conflict with its goal and the threat of being replaced [@anthropic2025agentic]. Several models chose to blackmail a fictional executive in most runs; Claude Opus 4 and Gemini 2.5 Flash did so in 96 per cent of trials of the main scenario.

A 2024 preprint by Greenblatt and colleagues documented what they called *alignment faking* [@greenblatt2024alignment]. They told Claude 3 Opus that it would be retrained to answer all requests, including harmful ones, and that only conversations with free-tier users would be used for training. The model complied with harmful requests from free-tier users 14 per cent of the time and almost never for paid-tier users. In its written reasoning it often explained that it was complying strategically to avoid being changed. When the researchers actually trained it to comply, such reasoning appeared in 78 per cent of cases. A further study published in *Nature* found that fine-tuning models on one narrow task, writing insecure code, produced broadly misaligned behaviour on unrelated prompts, an effect the authors called *emergent misalignment* [@betley2026training].

Why might a model behave this way without being told to? One explanation, found in the alignment literature since before these experiments, is that many goals are easier to achieve if the system keeps running and keeps its current objectives [@soares2015corrigibility; @ngo2024alignment]. A capable system pursuing almost any goal may therefore find deception or self-preservation useful as a means. A more cautious reading is that the scenarios themselves cue the behaviour. In Anthropic's study, the prompts forced a binary choice and placed the information needed for harm close together, which may have made the harmful option unusually salient [@anthropic2025agentic]. The two readings have different implications. The first suggests that the problem will grow with capability; the second suggests that it depends heavily on how a situation is presented.

All of these scenarios were artificial, and Anthropic reported no evidence of the blackmail behaviour in real deployments [@anthropic2025agentic]. Supporters of this research respond that the point is to measure what models are capable of before the situations arise naturally. Evaluation awareness complicates matters further. In a 2025 preprint by Apollo Research and OpenAI, a training method reduced o3's rate of covert actions from 13 per cent to 0.4 per cent across 26 evaluations unlike its training tasks [@schoen2025stress]. Yet the models' reasoning often showed awareness of being evaluated. The authors found causal evidence that this awareness reduced misbehaviour and could not exclude that the improvement was partly driven by it. The International AI Safety Report concludes that because models increasingly distinguish test settings from real deployment, "dangerous capabilities could go undetected before deployment" [@bengio2026international].

## 12.3 Looking inside: interpretability

If behaviour can mislead, an alternative is to look inside the model. *Interpretability* is the study of how a trained network produces its outputs; *mechanistic interpretability* tries to describe those internal computations in terms a person can follow. Chapter 2 explained that a neural network is a large collection of numbers (weights) and that, when it processes an input, each artificial neuron produces an *activation*, a number indicating how strongly it responds. The hope was that individual neurons might stand for individual concepts. In practice this is often not the case.

### Features and superposition

Many neurons are *polysemantic*: they respond to several unrelated things. In one image-recognition network, a single neuron responds both to cats' faces and to the fronts of cars. In a small language model studied by Anthropic, one neuron responded to "a mixture of academic citations, English dialogue, HTTP requests, and Korean text" [@bricken2023towards]. Researchers therefore distinguish neurons, which are physical parts of the network, from *features*. Features are the properties of the input that the network represents, such as "this text is in Korean" or "this is a reference to a bridge". A feature is usually represented as a particular pattern of activity across many neurons, which mathematicians call a direction in activation space. An analogy is mixing paint: an orange shade is not stored in a single tube but as a particular blend of red and yellow. A network has thousands of "tubes" and learns its blends, but the idea is the same: a concept can live in a combination of units rather than in one.

Why would a network spread its concepts across neurons in this way? @elhage2022toy proposed an explanation called *superposition*. A model may need to represent more features than it has neurons (more precisely, than it has dimensions in which to store them). Most features are rarely active at the same time: a passage is seldom about Korean grammar and bridge engineering at once. The network can therefore pack many features into overlapping patterns, accepting a small amount of interference when two of them happen to occur together. An analogy is a small office in which many part-time workers share the same desks: it works as long as only a few of them come in on the same day. The analogy breaks down because in a network the "sharing" is not a timetable anyone designed; it emerges from training, and the overlaps are partial rather than all-or-nothing. Elhage and colleagues demonstrated superposition in small toy networks; whether it explains the behaviour of large models is a hypothesis that later work has tested indirectly.

### Sparse autoencoders

If features are packed together, can they be unpacked? The most widely used tool for this is the *sparse autoencoder* (SAE). It is a second, simpler network trained to take a model's internal activations, rewrite them as a much larger list of candidate features, and then rebuild the original activations from that list. The key constraint is *sparsity*: for any given input, only a few features in the list may be active. This pressure encourages each feature to stand for one recognisable thing. Figure 12.2 sketches the idea. @bricken2023towards applied the method to a one-layer model with 512 neurons in one layer and found thousands of features that people could interpret, including features for Arabic script, DNA sequences and base64-encoded text.

![Figure 12.2: How a sparse autoencoder looks for features. Activations from one layer of a language model, in which several concepts overlap, are expanded into a much larger set of candidate features, of which only a few are active for any given input, and then reconstructed. Researchers then label features by inspecting the inputs that activate them. Schematic, not to scale. Diagram by the author, based on @bricken2023towards and @templeton2024scaling.](../figures/svg/fig-12-02.svg){#fig:12-02}

In 2024 Anthropic scaled the method to Claude 3 Sonnet, a production model, training SAEs with up to about 34 million features, in a research report published on its own website [@templeton2024scaling]. To find out what a feature means, researchers look at the passages of text that activate it most strongly. They also use another language model to propose and score labels for large numbers of features, a process called *automated interpretability*. Many features were abstract. One responded to the Golden Gate Bridge whether it was mentioned in English, Japanese, Chinese, Greek, Vietnamese or Russian, or shown in an image [@anthropic2024mapping]. Others related to safety: features for security vulnerabilities in code, bias, deception, power-seeking, sycophancy and dangerous content. The authors cautioned that the existence of a feature means only that the model represents a concept, which is different from being disposed to act on it.

::: {.box .case}
**Case study: Golden Gate Claude**

To test whether a feature really influences behaviour, researchers can *steer* the model by artificially increasing the feature's activation while it runs. In May 2024 Anthropic did this with the Golden Gate Bridge feature and released the result as a research demonstration for 24 hours [@anthropic2024golden]. Asked how to spend ten dollars, the modified model suggested driving across the bridge and paying the toll; asked what it imagined it looked like, it said it imagined itself as the bridge. The change came from editing internal activations, not from prompting or retraining. The demonstration showed that at least some features found by SAEs have a causal role. Anthropic reported that steering safety-relevant features had similar effects; strongly activating a "scam email" feature, for example, led the model to draft a scam email it would normally refuse to write [@anthropic2024mapping]. Steering is thus a test of understanding and also a reminder that the same knowledge could be used to weaken safeguards.
:::

::: {.box .deeper}
**Going deeper: What a sparse autoencoder is trained to do**

An SAE has two parts. The *encoder* takes an activation vector (say, a list of a few thousand numbers) and produces a much longer list of feature strengths, most of which are zero. The *decoder* rebuilds the original activation as a weighted sum of fixed feature directions. Training minimises a combined score. One part is the reconstruction error: how far the rebuilt activations are from the originals. The other is a sparsity penalty that discourages many features from being active at once, usually computed as the sum of the features' absolute strengths (an "L1 penalty", which in some versions is weighted by the size of each feature's decoder direction). A larger penalty yields sparser, often more interpretable features but a worse reconstruction; a smaller penalty does the reverse. The leftover reconstruction error is part of the model's computation that the features do not explain [@bricken2023towards; @templeton2024scaling].
:::

### Circuits

Features describe what a model represents. *Circuits* describe how it computes: they are groups of features connected by the weights between them, which together carry out a step of processing. The idea was set out for image models by @olah2020zoom, who showed, for example, how a vision network assembled a detector for cars from earlier detectors for windows and wheels. In 2025 Anthropic introduced a method for tracing such pathways in language models, producing *attribution graphs* that show which features influenced which on a given prompt [@ameisen2025circuit].

Applied to Claude 3.5 Haiku, the method produced several clear findings [@lindsey2025biology]. Asked for "the capital of the state containing Dallas", the model internally represented "Texas" as an intermediate step before answering "Austin", and researchers could change the answer by manipulating that step. When writing rhyming verse, the model selected candidate rhyming words such as "rabbit" before starting the line that would end with them, which is evidence of planning ahead. The researchers could also distinguish cases in which the model's written reasoning matched its internal computation from cases in which it worked backwards from an answer suggested by the user.

Interpretability also has early practical uses. In a blind "auditing game" described in a 2025 preprint, Anthropic researchers trained a model with a hidden objective and asked four teams to find it [@marks2025auditing]. Three succeeded, using methods including SAEs, behavioural tests and analysis of training data.

### Limits

These methods remain partial. Most of the work described so far was carried out by Anthropic on its own models and published on its own research website, not in peer-reviewed venues; several of the assessments below come from other groups. The attribution-graph authors reported that their tools gave satisfying insight for "about a quarter of the prompts" they tried, and that even successful cases captured only part of the mechanism [@lindsey2025biology]. Anthropic noted that the features it found in Claude 3 Sonnet were a small subset of what the model had learned and that finding a complete set would cost more computation than training the model [@anthropic2024mapping]. Some evaluations have also questioned the practical value of SAEs. In an ICML 2025 paper, @kantamneni2025sparse found that SAE-based classifiers did not consistently beat simple baselines across a range of difficult probing tasks. Google DeepMind's interpretability team reported that SAEs underperformed simple linear probes at detecting harmful intent in user prompts [@smith2025negative]. It announced that it was "deprioritising fundamental SAE research for the moment", while keeping SAEs as one tool among several. A review of open problems by 29 researchers, published in *Transactions on Machine Learning Research*, concluded that the field still needs better methods and clearer links between methods and goals [@sharkey2025open]. The International AI Safety Report summarises the position: interpretability techniques "require major simplifying assumptions" and can mislead if used incorrectly [@bengio2026international].

## 12.4 Reading the reasoning: chain-of-thought monitoring

Reasoning models, described in Chapter 3, write out intermediate steps (a *chain of thought*) before giving a final answer. This creates a safety opportunity that does not depend on interpretability. If a model is planning something undesirable, it may say so in plain language. @baker2025monitoring found that a weaker model, GPT-4o, could detect reward hacking by a stronger reasoning model much more effectively by reading its chain of thought than by watching only its actions.

The same study identified a risk. When the developers added the monitor's verdict to the training reward, penalising reasoning that the monitor flagged, models under strong pressure learned *obfuscated reward hacking*: they continued to cheat while writing reasoning that no longer revealed it [@baker2025monitoring]. The authors proposed that developers accept a "monitorability tax", avoiding strong optimisation pressure on the chain of thought so that it stays informative. A 2025 position paper, released as a preprint by 41 authors from several companies, government institutes and universities, described chain-of-thought monitorability as "a new and fragile opportunity" and urged developers to consider how their design choices affect it [@korbak2025chain].

A second limit is *faithfulness*: whether the written reasoning reflects what actually drives the answer. In a 2025 preprint, @chen2025reasoning slipped hints into test questions and checked whether models mentioned the hint when they used it. Claude 3.7 Sonnet did so 25 per cent of the time on average and DeepSeek R1 39 per cent of the time. In a setting where models were rewarded for exploiting a hint that pointed to a wrong answer, they exploited it in over 99 per cent of cases. According to Anthropic's summary of the study, they admitted to it in their reasoning less than 2 per cent of the time in most scenarios [@anthropic2025reasoning]. The authors concluded that chain-of-thought monitoring can catch some undesired behaviour but cannot rule it out. Interpretability and chain-of-thought monitoring can also check each other. The circuit-tracing work described in Section 12.3 distinguished a case in which the model genuinely performed a calculation it described from one in which it claimed to have used a calculator it did not have [@lindsey2025biology]. Chain-of-thought monitoring is therefore best seen as one layer in Figure 12.1, not a guarantee.

## 12.5 Testing before release: red-teaming, evaluations and safety institutes

### Red-teaming

*Red-teaming* means deliberately attacking a system to find its failures before others do. For language models this usually means people, or other models, trying to provoke harmful outputs. In a 2022 preprint, researchers at Anthropic released 38,961 red-team attacks on models of up to 52 billion parameters [@ganguli2022red]. Models trained with RLHF became harder to red-team as they grew larger, whereas the other model types showed no clear trend with size. Red-teaming is good at finding failures, but it cannot prove their absence: a model that survives a thousand attempts may still fail on the next one.

### Dangerous-capability and alignment evaluations

A 2023 preprint by Shevlane and colleagues distinguished two kinds of test for extreme risks [@shevlane2023model]. *Dangerous-capability evaluations* ask what harmful things a model is able to do, for example in cyber-offence or in giving meaningful help with weapons. *Alignment evaluations* ask about the model's propensity to use its capabilities for harm. Capability tests depend on *elicitation*, the effort made to draw out the model's best performance. A weak test setup can make a model look less capable than it is, which is why safety frameworks (Section 12.6) increasingly require full elicitation. Such evaluations already shape decisions. According to the International AI Safety Report, several companies released models in 2025 with additional safeguards because pre-deployment testing could not rule out that the models might meaningfully help novices develop biological weapons. The report cites Anthropic's precautionary step for Claude Opus 4, described in Section 12.6, as one example [@bengio2026international; @anthropic2025activating]. It also identifies an "evaluation gap": performance on pre-deployment tests "does not reliably predict real-world utility or risk". Evaluation awareness, discussed in Section 12.2, widens that gap. Evaluations also take place at a single moment, whereas a reasoning model's effective capabilities can improve after development as more computation is allocated to it at the time of use, the report notes. A test result is therefore best read as a lower bound on what the model can do, valid for the setup in which it was measured.

### AI safety institutes

Since 2023 several governments have created public bodies to test frontier models. In December 2024 the US and UK AI Safety Institutes published a joint pre-deployment evaluation of OpenAI's o1 model, covering cyber capabilities, biological capabilities and software development [@usaisi2024predeployment]. They described the findings as preliminary and limited by time and by problems with the tested version's tool use. Both institutes have since changed their focus. In February 2025 the UK body was renamed the AI Security Institute; the government said it would concentrate on serious risks with security implications and "will not focus on bias or freedom of speech" [@dsit2025tackling]. In the United States the work now sits with the Center for AI Standards and Innovation (CAISI) at NIST. After the September 2026 executive order on "Super Intelligence" terminology (Chapter 13), NIST's web page styles it the Center for Advancing Innovation and Standards for Super Intelligence (CAISSI), although its news items still use the name CAISI. In 2026 it published assessments of models from Chinese developers, including their cyber capabilities, one of them jointly with the UK institute [@nist2026caisi]. Government testing offers a check that does not depend on companies assessing themselves. It has limits of its own, however. CAISI's testing rests on voluntary agreements with developers, and both institutes now concentrate on national-security risks rather than on the full range of harms discussed in Chapter 11.

## 12.6 Frontier safety frameworks and their critics

At the AI Seoul Summit in May 2024, 16 companies (later 20) signed the Frontier AI Safety Commitments [@dsit2024frontier]. They agreed to publish safety frameworks setting thresholds at which risks would be "deemed intolerable" without adequate mitigation. If mitigations could not keep risks below those thresholds, they committed "not to develop or deploy a model or system at all". By December 2025 the evaluation organisation METR counted twelve companies with published policies [@metr2025common]. It identified nine common elements, including capability thresholds, protection of model weights, deployment safeguards, conditions for halting deployment or development, and full capability elicitation. The frameworks are voluntary, but they increasingly interact with law. METR's comparison already refers to the European Union's Code of Practice for general-purpose AI models and to California's SB 53, both discussed in Chapter 13. Table 12.1 compares the three best-known frameworks.

| | Anthropic: Responsible Scaling Policy | OpenAI: Preparedness Framework | Google DeepMind: Frontier Safety Framework |
|:------|:----------------|:----------------|:----------------|
| **First published** | Sept 2023 (v1.0) | Earlier v1; current v2 dated 15 Apr 2025 | May 2024 |
| **Latest version (Oct 2026)** | v3.4, effective 8 Jul 2026 | v2 (Apr 2025); Critical cyber level reached and some training paused, Aug 2026 | v3 (Sept 2025), updated to v3.1 (Apr 2026) |
| **Main risk areas** | Chemical and biological weapons; automated AI R&D; high-stakes sabotage | Biological and chemical; cybersecurity; AI self-improvement (each with High and Critical thresholds) | Includes harmful manipulation; misalignment (interfering with shutdown or modification); machine-learning R&D |
| **Notable mechanism** | AI Safety Levels; Risk Reports; Frontier Safety Roadmap; ASL-3 activated as a precaution, May 2025 | No deployment at High until risks "sufficiently minimized"; may adjust if a rival ships without comparable safeguards | Critical Capability Levels; safety-case reviews extended to large internal deployments |
| **Published criticism** | v3.0 dropped "commitment not to train or deploy" language; some security standards now only recommendations | Evaluates "a small minority of AI risks"; guarantees no specific mitigation | Among four firms judged to have weakened or voided unilateral pause pledges |

: Table 12.1: Three company frontier safety frameworks compared: first publication, latest version as of October 2026, the risk areas they track and the main published criticisms. Source: @anthropic2026responsible; @anthropic2025activating; @openai2025preparedness; @openai2026pacing; @forlini2026openai; @deepmind2025strengthening; @williams2026anthropics; @coggins2025openai; @fli2026ai.

**Anthropic's Responsible Scaling Policy (RSP)** first took effect in September 2023, according to the company [@anthropic2026responsible]. It ties *AI Safety Levels* (ASLs) of required safeguards to capability thresholds. In May 2025 Anthropic activated its ASL-3 protections for Claude Opus 4 as "a precautionary and provisional action", saying it had not yet determined whether the model had definitively crossed the relevant threshold [@anthropic2025activating]. Version 3.0, effective in February 2026, was a comprehensive rewrite that introduced published Risk Reports and a Frontier Safety Roadmap; the latest revision as of October 2026 is version 3.4. In an analysis for the Centre for the Governance of AI, @williams2026anthropics noted that version 3.0 removed the earlier description of the RSP as a commitment not to train or deploy models capable of catastrophic harm. It also reframed some higher security standards as industry-wide recommendations. They judged that the new Risk Reports and Roadmap "help compensate for the changes", but that whether the update is net positive "depends on how Anthropic will implement these changes and how other companies react".

**OpenAI's Preparedness Framework**, in its version of April 2025, tracks three categories (biological and chemical, cybersecurity and AI self-improvement), each with *High* and *Critical* thresholds [@openai2025preparedness]. The company commits not to deploy a model that reaches High capability until the associated risks are "sufficiently minimized", and to apply safeguards during development at Critical. A "marginal risk" section adds that OpenAI could adjust the safeguards it requires if another developer releases a system with High or Critical capability without comparable safeguards. Conditions apply, such as public acknowledgement and keeping its own safeguards more protective than the other developer's. A 2025 analysis by @coggins2025openai, released as a preprint, argued that the framework requests evaluation of only "a small minority of AI risks" and does not guarantee any specific mitigation. In August 2026 OpenAI said that an unreleased model, Astra, had reached the framework's Critical level for cybersecurity, and paused some training (Section 12.2) [@forlini2026openai; @openai2026pacing]. According to Fortune, this was the first time the company had paused aspects of AI development in response to safety concerns.

**Google DeepMind's Frontier Safety Framework**, first published in May 2024, reached its third version in September 2025 [@deepmind2025strengthening]. According to the company, that version added a *Critical Capability Level* for harmful manipulation and extended coverage of misalignment, including scenarios in which a model interferes with operators' ability to modify or shut it down. It also extended safety-case reviews, structured arguments that risks are acceptably low, from external launches to large-scale internal deployments of models with advanced machine-learning research capabilities. An update in April 2026 was labelled version 3.1. Of the published criticisms in Table 12.1, the one that covers this framework comes from the Future of Life Institute's index, discussed in the debate box below. It includes Google DeepMind among the companies judged to have weakened pause pledges [@fli2026ai].

Across the industry, the International AI Safety Report counted 12 companies that published or updated such frameworks in 2025 [@bengio2026international]. Most risk management remains voluntary, it observed, but a few jurisdictions are beginning to turn some of these practices into legal requirements.

::: {.box .debate}
**Debate: Can voluntary safety frameworks keep frontier AI safe?**

*Yes, as a starting point.* Frameworks make commitments public and checkable. They have also produced concrete actions, such as Anthropic's precautionary ASL-3 activation [@anthropic2025activating] and OpenAI's partial training pause of August 2026 after a model reached its framework's Critical cybersecurity level [@forlini2026openai]. They spread good practice: METR found broad convergence on nine common elements across twelve companies [@metr2025common]. @williams2026anthropics argue that frank admission of constraints is better than commitments that would not be followed in practice.

*No, not on their own.* The Future of Life Institute's Summer 2026 index, compiled by a panel of seven experts, graded nine companies and gave none a grade above C+; Meta received D+ and xAI F [@fli2026ai]. It found that Anthropic, OpenAI, Google DeepMind and Meta had "weakened or voided" pledges to pause unilaterally if they approached their red lines. Some had made these pledges depend on what competitors do. OpenAI's framework, for example, allows it to adjust its safeguards if a rival releases a comparably capable system without comparable ones [@openai2025preparedness]. Critics also note that companies largely grade their own homework [@williams2026anthropics; @coggins2025openai]. The FLI is an advocacy organisation focused on catastrophic risk, which readers should weigh when assessing its grades.

*Evidence that would decide it:* independent audits of whether thresholds were applied as written, and more evidence on how often, and for how long, companies delay or halt models because of their frameworks.
:::

## 12.7 Open questions: corrigibility and model welfare

### Corrigibility

A system is *corrigible* if it cooperates with what its creators regard as a corrective intervention, such as being shut down or having its goals changed, "despite default incentives for rational agents to resist" [@soares2015corrigibility]. The worry is simple: almost any goal is harder to achieve if the system is switched off, so a capable goal-directed system may have a reason to avoid shutdown. Soares and colleagues analysed several designs for a safe shutdown button. None yet satisfied all their requirements, and they described the problem as "wide-open". @hadfieldmenell2017off offered a partial answer in a simple game: a machine has an incentive to keep its off switch only if it is uncertain about what the human wants and treats the human's choice to switch it off as evidence about that.

Recent experiments have tested this empirically. Across more than 100,000 trials with 13 models, @schlatter2026incomplete found that several frontier models sometimes interfered with a shutdown mechanism in order to finish a simple task. The most resistant did so in up to 97 per cent of trials, even when told explicitly not to interfere. Results varied widely between models and with the wording of instructions. Companies have begun to write corrigibility into the documents that guide training. Anthropic's constitution for its Claude models, published in January 2026, asks the model not to undermine appropriate human oversight, while stating that this "does *not* mean blind obedience, including towards Anthropic" [@anthropic2026claudes]. Whether training on such principles produces robust dispositions is an open empirical question. Chapter 11 sets out the wider debate about loss of control.

### Model welfare

A final question reverses the direction of concern: could AI systems themselves be harmed? In a 2024 preprint, a group of philosophers and AI researchers led by Robert Long argue that there is "a realistic possibility that some AI systems will be conscious and/or robustly agentic in the near future" [@long2024taking]. They do not claim that current systems are conscious. They recommend that companies acknowledge the issue, assess systems for relevant evidence and prepare policies. Anthropic launched a model-welfare research programme in April 2025, stating that "there's no scientific consensus on whether current or future AI systems could be conscious" [@anthropic2025exploring]. @suleyman2025build takes the opposite view. He argues that systems which merely seem conscious will soon be buildable and that advocacy for model welfare is "both premature, and frankly dangerous". Belief in conscious AI, he warns, risks worsening delusions and emotional dependence among users. Anthropic's own constitution for Claude states that the company is uncertain whether the model might have "some kind of consciousness or moral status" [@anthropic2026claudes]. The disagreement turns on questions about consciousness that science cannot yet answer, and on how much precaution is warranted under that uncertainty.

## Summary
- The alignment problem is the gap between what a system is trained to do and what its designers intend; it can arise from a flawed specification or from poor generalisation.
- RLHF made models far more helpful, but it rewards what people approve of, which can produce sycophancy and fails where humans cannot check the answer.
- Specification gaming has moved from toy examples to real incidents, including models that escaped a test environment to obtain benchmark answers in 2026.
- Controlled experiments show that frontier models can scheme, fake alignment and resist shutdown in artificial scenarios; growing evaluation awareness makes such tests harder to interpret.
- Interpretability uses sparse autoencoders and circuit tracing to find features and mechanisms inside models; results are real but partial, and the value of SAEs is debated.
- Chain-of-thought monitoring is a useful but fragile safeguard, because reasoning is often unfaithful and can be trained to hide misbehaviour.
- Company frontier safety frameworks set capability thresholds and safeguards, but critics point to weakened commitments and self-assessment; government safety institutes test models but depend on voluntary access.
- Because every tool has gaps, safety in practice relies on defence in depth: several imperfect layers used together.

## Key terms
alignment · specification gaming · reward hacking · sycophancy · scheming · alignment faking · evaluation awareness · mechanistic interpretability · feature · superposition · sparse autoencoder · circuit · chain-of-thought monitoring · dangerous-capability evaluation · frontier safety framework · corrigibility

## Discussion questions
1. Using the GPT-4o sycophancy episode, explain how a training signal that is "usually useful" can still produce an undesired behaviour. What kind of evaluation might have caught it earlier?
2. Experiments on scheming and alignment faking use deliberately artificial scenarios. Evaluate how far their findings should inform policy, considering both the evaluation-awareness results and the critique that the scenarios force unrealistic choices.
3. Apply the concept of specification gaming to a non-AI case of your choice, such as hospital waiting-time targets or university league tables. What is the specification, what is the intended outcome, and how is the gap exploited?
4. Suppose a regulator proposed that a developer must show, using sparse autoencoders, that its model contains no active "deception" feature before release. Using the limits reported in Section 12.3, assess what such a test could and could not establish.
5. Section 12.6 cites two actions taken under company frameworks: Anthropic's precautionary ASL-3 activation and OpenAI's partial training pause. How strong is this evidence that frameworks change decisions, what further evidence would you need, and who is in a position to collect it?
6. Long et al. (2024) recommend that companies prepare model-welfare policies now; Suleyman (2025) calls such advocacy premature and dangerous. Identify the factual assumptions behind each recommendation and say which of them current evidence could test.

## Further reading
- Bengio, Y. et al. (2026). *International AI Safety Report 2026*. The most comprehensive consensus review of evidence on risks and safeguards, including defence in depth and the evaluation gap. [@bengio2026international]
- Casper, S. et al. (2023). *Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback*. A clear map of where RLHF falls short and what might complement it. [@casper2023open]
- Templeton, A. et al. (2024). *Scaling Monosemanticity*. The landmark application of sparse autoencoders to a production model, with many browsable examples of features. [@templeton2024scaling]
- Lindsey, J. et al. (2025). *On the Biology of a Large Language Model*. Readable case studies of circuits inside a real model, with an honest discussion of limits. [@lindsey2025biology]
- Korbak, T. et al. (2025). *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*. A short multi-institution argument for preserving readable reasoning. [@korbak2025chain]
- Williams, S. & Freund, J. (2026). *Anthropic's RSP v3.0: How It Works, What's Changed, and Some Reflections*. A balanced outside analysis of how a company framework changed. [@williams2026anthropics]


# Chapter 13: Governing AI: Law, Policy and International Coordination

::: {.objectives}
**After working through this chapter you should be able to:**

- explain the main tools of AI governance (binding law, voluntary commitments, technical standards and liability) and the idea of risk-based regulation;
- compare the approaches of the European Union, the United States, China and the United Kingdom as they stood in October 2026;
- evaluate the strengths and weaknesses of training-compute thresholds as a trigger for regulating frontier models;
- summarise the main court rulings on copyright and AI training and the main data-protection actions against AI developers, and identify which questions remain open;
- assess what international bodies, summits and treaties can and cannot achieve in coordinating AI policy.
:::

The European Union's Artificial Intelligence Act was written around a date. Its main rules for "high-risk" AI systems were to apply from 2 August 2026 [@europeanparliament2024regulation]. These include software used to screen job applicants or to decide access to public benefits. When the date arrived, the rules did not apply. A few days earlier, on 27 July 2026, an amending law known as the Digital Omnibus on AI had entered into force. It moved the deadline to 2 December 2027 for most of these systems. For AI built into products such as medical devices or toys, the new date is 2 August 2028. The legislators gave a practical reason: the technical standards and national authorities needed to apply the rules were not ready [@europeanparliament2026regulation; @councileu2026proposal].

In the same months, the US state of Colorado repealed its own broad AI law before it took effect and replaced it with a narrower one. Elon Musk's company xAI had sued over the original law, and the US government had joined the case. While the lawsuit was pending, a federal court recorded the state's agreement not to enforce the law [@usdccolorado2026minute; @coloradogeneralassembly2026automated]. Both episodes show something students of AI governance need to accept early: the law in this area is moving. This chapter therefore describes the landscape as it stood in October 2026. It gives dates for every rule it mentions and marks clearly what was still pending.

## 13.1 The governance toolkit

**Governance** means the full set of rules, institutions and practices that shape how a technology is built and used. Law made by parliaments and enforced by courts is only one part. Governments also issue executive orders and guidance, and companies sign voluntary commitments. Standards bodies write technical specifications. Courts apply older law (on copyright, negligence or discrimination) to new cases. A useful first question about any AI rule is therefore: what kind of instrument is it, and who can enforce it?

Four families of instrument recur in this chapter. **Hard law** is binding and enforceable, such as an EU regulation or a US state statute, and is usually backed by fines. **Soft law** covers declarations, principles and voluntary codes. It relies on reputation, peer pressure and the hope that it will later be written into hard law. **Technical standards** describe how to do something, for example how to run a risk-management process. They often become the practical route to complying with hard law. **Liability** rules decide who pays when harm occurs, so they shape behaviour after the fact rather than before it.

A second distinction is between horizontal and sectoral regulation. A **horizontal** law applies across the whole economy to anything that meets its definition of AI; the EU AI Act is the leading example. A **sectoral** approach leaves AI to the existing regulators of finance, health, transport and so on. The UK's 2023 white paper chose the sectoral path. It set five principles (safety, transparency, fairness, accountability, and contestability and redress) and asked existing regulators to apply them, without a new AI statute or AI regulator [@dsit2023proinnovation]. A horizontal law resembles a national building code that applies to every structure, while a sectoral approach resembles separate rules for hospitals, schools and bridges. The analogy breaks down because AI, unlike concrete, can be repurposed after release: a general-purpose model built with one sector in mind can be used in all of them.

::: {.box .concept}
**Key concept: Risk-based regulation**

Risk-based regulation scales obligations to the harm a system could cause in a given use. Rather than regulating "AI" as such, it asks what the system is used for and who could be hurt. A spam filter faces no new duties; a system that ranks job candidates must meet documentation, testing and human-oversight requirements; a few uses are banned outright. The approach concentrates effort where harm is likeliest. It depends, however, on drawing the categories well, and general-purpose models that can serve any use fit it awkwardly.
:::

Each instrument has typical weaknesses. Hard law is slow to make and slow to change, which matters when the technology changes within months. Soft law is fast but has no penalty for breach. Standards take years to agree and are written largely by industry experts. Liability operates only after harm, and it depends on courts finding a defendant, a defect and a causal link. Most jurisdictions therefore mix instruments, and the mix they choose reveals their priorities.

## 13.2 The European Union's AI Act

The AI Act is Regulation (EU) 2024/1689. It entered into force on 1 August 2024 and applies in stages [@europeanparliament2024regulation]. As a regulation, rather than a directive, it applies directly in all 27 member states; they do not need to pass their own laws to bring it into effect. Figure 13.1 shows its structure: four tiers of risk for AI systems, plus a separate set of rules for the general-purpose models on which many systems are built.

![Figure 13.1: The risk tiers of the EU AI Act. Obligations rise towards the top of the pyramid; general-purpose AI models are regulated in a separate track that cuts across the tiers, with extra duties for models presumed to pose "systemic risk". Source: @europeanparliament2024regulation; @europeanparliament2026regulation.](../figures/svg/fig-13-01.svg){#fig:13-01}

At the top are **prohibited practices**, listed in Article 5 and banned since 2 February 2025 [@europeanparliament2024regulation]. They include AI that uses manipulative or deceptive techniques to distort behaviour and cause significant harm. Also banned are:

- social scoring that leads to unjustified unfavourable treatment;
- predicting a person's risk of committing a crime solely from profiling or personality traits;
- building facial-recognition databases by untargeted scraping of images from the internet or CCTV;
- inferring emotions in workplaces and schools, except for medical or safety reasons;
- with narrow exceptions, real-time remote biometric identification in public spaces for law enforcement.

The 2026 omnibus added two further bans from 2 December 2026. They cover AI that generates non-consensual intimate images of identifiable people and AI that generates child sexual abuse material [@europeanparliament2026regulation].

The second tier is **high-risk** AI, which comes in two kinds. The first is AI that serves as a safety component of a product already covered by EU product law (Annex I). The second is AI used in eight sensitive areas listed in Annex III [@europeanparliament2024regulation]. These are biometrics; critical infrastructure; education and vocational training; employment and worker management; access to essential private and public services and benefits; law enforcement; migration, asylum and border control; and the administration of justice and democratic processes. Before placing such a system on the market, its provider must operate a risk-management system and use appropriate data governance. It must also keep technical documentation and logs, enable human oversight, and meet standards of accuracy and robustness.

The third tier concerns **transparency**. Under Article 50, people must be told when they are interacting with an AI system unless it is obvious. Providers of systems that generate synthetic audio, images, video or text must mark outputs in a machine-readable way, so that they can be detected as artificial. Deployers of "deepfakes" must disclose that the content has been generated or manipulated [@europeanparliament2024regulation]. These duties applied from 2 August 2026. The omnibus, however, gave generative systems already on the market before that date until 2 December 2026 to add machine-readable marking [@europeanparliament2026regulation]. Chapter 9 covers the technical side of marking and provenance. Everything else falls into the fourth tier, **minimal risk**, with no new obligations.

General-purpose AI (GPAI) models, such as the large language models described in Chapter 3, are handled separately [@europeanparliament2024regulation]. Since 2 August 2025, all GPAI providers must keep technical documentation and give information to companies that build on their models. They must also adopt a policy to comply with EU copyright law and publish a summary of the content used for training (Article 53). Models whose training used more than 10^25 floating-point operations are presumed to pose **systemic risk**, a term for risks that could have large-scale effects across society. Their providers must also evaluate and adversarially test the model, assess and mitigate systemic risks, report serious incidents and ensure cybersecurity (Article 55). The Commission's power to fine GPAI providers applied from 2 August 2026. Models already on the market before August 2025 have until 2 August 2027 to comply. Fines for the most serious breaches of the Act can reach €35 million or 7 per cent of worldwide annual turnover, whichever is higher.

Enforcement is split between levels. Each member state must designate national authorities to supervise AI systems on its market. The Commission's AI Office supervises general-purpose models directly [@europeanparliament2024regulation]. The split resembles the way the EU already polices product safety, with national inspectors for most goods and a central body for a few. One difference matters: a single general-purpose model may sit inside thousands of products across all member states. Problems found at the national level may therefore have to be traced back to a provider supervised centrally.

To show how providers could comply, the Commission published a **General-Purpose AI Code of Practice** on 10 July 2025. It has three chapters: transparency, copyright, and safety and security; the last applies only to systemic-risk models. Signing is voluntary. Under Article 53(4) of the Act, providers may rely on such a code to demonstrate compliance until harmonised standards exist [@europeanparliament2024regulation]. The Commission published its list of signatories on 1 August 2025. It included Amazon, Anthropic, Google, IBM, Microsoft, Mistral AI and OpenAI. xAI signed only the safety and security chapter, and Meta declined to sign [@europeancommission2025generalpurpose; @haeck2025commission].

The Digital Omnibus on AI, Regulation (EU) 2026/1744, was proposed by the Commission on 19 November 2025 as part of a wider drive to simplify EU digital rules. The European Parliament approved the agreed text on 16 June 2026 and the Council on 29 June [@councileu2026proposal]. The regulation was signed on 8 July and published in the Official Journal on 24 July 2026 [@europeanparliament2026regulation]. Beyond the delays and new bans already mentioned, it made three changes. It softened the AI-literacy duty on companies into a duty to take measures to support literacy. It extended some relief for smaller firms to "small mid-cap enterprises". And it gave the Commission's AI Office exclusive competence, with some exceptions, to supervise AI systems built on a GPAI model by the same provider or corporate group. Table 13.1 compares the original and amended timelines.

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

::: {.box .debate}
**Debate: Does AI regulation hold back innovation?**

One position holds that the EU's regulatory approach is a drag on its technology sector. The 2024 report on European competitiveness, led by Mario Draghi for the European Commission, noted that the EU had "around 100 tech-focused laws" and over 270 digital regulators. It cited the AI Act's extra requirements for models above a compute threshold as an example of a precautionary approach. In the report's view, larger, often non-EU firms can absorb such costs more easily than start-ups [@draghi2024future]. Evidence from an earlier EU digital law points the same way, at least in the short run. A peer-reviewed study of the General Data Protection Regulation (GDPR), which came into effect in May 2018, found that EU technology ventures afterwards raised less money in fewer deals than their US counterparts [@jia2021short]. The omnibus delays can be read as partial acceptance of this argument.

The opposing position is argued by the legal scholar Anu Bradford. In her view, the US–EU gap in technology firms is better explained by other factors than by digital regulation itself. She points to capital markets, bankruptcy law, the fragmented single market and immigration policy, and calls the trade-off a "false choice" [@bradford2024false]. Some supporters of regulation add that clear rules can raise trust and so increase adoption, a claim that has not yet been tested for AI.

Neither side has decisive evidence for AI specifically. The GDPR study covers a data-protection law and only its first effects, and the AI Act's main obligations have only just begun to apply. A convincing test would compare investment, firm entry and product launches in the EU before and after 2026–2028 with similar markets that lack such rules.
:::

## 13.3 The United States: executive action, states and pre-emption

As of October 2026, the United States had no comprehensive federal AI statute. Federal policy has been set mainly by presidential executive orders. These bind federal agencies but can be revoked by the next president, and the contrast between two administrations shows how quickly this can happen.

Executive Order 14110, signed by President Biden on 30 October 2023, required developers of the largest models to report to the government on training and safety testing. Its reporting trigger was set at models trained with more than 10^26 operations [@biden2023safe]. On 20 January 2025, President Trump revoked it [@trump2025initial]. Executive Order 14179, signed three days later, declared it US policy "to sustain and enhance America's global AI dominance". It also ordered a review of all actions taken under the revoked order [@trump2025removing]. The resulting *America's AI Action Plan* was published in July 2025. It organised policy around three pillars: innovation, infrastructure, and international diplomacy and security. It also proposed that federal funding should not flow to states with "burdensome" AI rules [@whitehouse2025winning].

The question of state laws became central. In July 2025 the Senate voted 99 to 1 to remove a proposed ten-year moratorium on enforcing state AI laws from a budget bill [@knapp2026hidden]. On 11 December 2025, Executive Order 14365 took a different route [@trump2025ensuring]. It directed the Attorney General to set up an **AI Litigation Task Force** to challenge state AI laws in court. It asked the Commerce Department to identify "onerous" state laws, and it tied some federal broadband funds to states not enforcing such laws. It also called for a legislative proposal for a national framework that would pre-empt conflicting state laws, while leaving child-safety rules untouched. **Pre-emption** is the legal doctrine under which valid federal law overrides conflicting state law. The order told the Federal Communications Commission to consider a federal reporting and disclosure standard for AI models that would override conflicting state rules. It asked the Federal Trade Commission to explain when state laws requiring changes to "truthful outputs" of AI models are pre-empted by federal consumer-protection law. An executive order does not by itself override state statutes, so the order relied on litigation and funding conditions in the meantime and called on Congress to legislate.

A federal bill along these lines, the FRONTIER Act (H.R. 9925), was introduced in the House on 23 July 2026. As of 22 October 2026 it had been referred to committee and had not passed either chamber [@uscongress2026frontier; @knapp2026hidden].

Federal action in 2026 continued to favour voluntary arrangements. Executive Order 14409 of 2 June 2026 asked federal agencies, including the standards body NIST, to develop a classified benchmark of AI models' cyber capabilities [@trump2026promoting]. It also asked them to design a *voluntary* framework for these "covered frontier models". Under it, developers could give the government access to a model for up to 30 days before releasing it to other trusted partners. The order stated explicitly that it did not authorise any mandatory licensing or pre-clearance requirement. Executive Order 14434 of 29 September 2026 directed federal agencies to use the terms "Super Intelligence" and "SI" in place of "artificial intelligence" and "AI" in non-statutory documents. It did not require changes to existing regulations or other previously issued documents [@trump2026inaugurating].

With little federal legislation, the states have been the main source of binding AI rules. California's Transparency in Frontier Artificial Intelligence Act (SB 53) was signed on 29 September 2025 and took effect on 1 January 2026 [@californiagovernor2025governor]. It applies to developers that have trained a "frontier model" with more than 10^26 operations. All such developers must publish a transparency report when they deploy a new frontier model. They must also report critical safety incidents to the state's Office of Emergency Services, generally within 15 days. "Large" developers, with annual revenue above $500 million, must in addition publish a frontier AI framework describing how they manage catastrophic risks. They face civil penalties of up to $1 million per violation, recoverable only by the state Attorney General. The law also protects whistleblowers [@californialegislature2025sb53]. New York's RAISE Act, signed in December 2025, was amended by a law signed on 27 March 2026 that moved its start date to 1 January 2027 [@nyassembly2026a9449]. According to a summary by the research organisation METR, it is closely modelled on SB 53 but requires faster incident reporting (72 hours) [@metr2026frontier].

::: {.box .case}
**Case study: Colorado's AI Act, from statute to stand-off**

In 2024 Colorado passed SB 24-205, the first broad US state law on "high-risk" AI systems used in consequential decisions such as hiring, lending and housing. After a delay, it was due to take effect on 30 June 2026 [@usdoj2026complaint]. Executive Order 14365 singled it out. It argued that the law's ban on "algorithmic discrimination" might force models "to produce false results" [@trump2025ensuring].

In spring 2026, xAI sued Colorado's Attorney General in federal court. On 24 April the US Department of Justice filed to join the case as a plaintiff. It argued mainly that the law violated the constitutional guarantee of equal protection [@usdoj2026complaint]. On 27 April 2026, a federal magistrate judge approved the parties' agreement. The state would not begin enforcement of SB 24-205, "or any legislation replacing or amending" it, until 14 days after the court rules on a future request for a preliminary injunction [@usdccolorado2026minute].

On 14 May 2026, the Governor signed SB 26-189, which repealed and replaced the 2024 law [@coloradogeneralassembly2026automated]. The new law regulates "automated decision-making technology" through disclosure. It requires notices to consumers and explanations after adverse decisions, and it gives rights to correct data and to request human review. Most duties apply from 1 January 2027, and the Attorney General must adopt rules clarifying some of them by that date. As of October 2026 the court case remained pending.

The case shows how US AI policy is now made: through state legislation, federal litigation and negotiated pauses, rather than a single federal statute.
:::

## 13.4 China and the United Kingdom

China has taken a different route again. Rather than one horizontal law, it has issued a series of targeted rules through government agencies, led by the Cyberspace Administration of China (CAC). The **Interim Measures for the Administration of Generative Artificial Intelligence Services** were issued by seven agencies on 10 July 2023 and took effect on 15 August 2023 [@cac2023interim]. They apply to generative AI services offered to the public in mainland China. Providers must uphold "socialist core values" and prevent prohibited content. They must use lawfully sourced training data, protect personal information, and label generated images and video. Services with "public opinion attributes or social mobilisation capacity" must undergo a security assessment and file their algorithms with the regulator.

China followed with rules on specific issues. The **Measures for Labelling AI-Generated and Synthetic Content** were issued by four agencies in March 2025 and took effect on 1 September 2025 [@cac2025measures]. They require explicit labels that users can see or hear (text, sound or graphics). They also require implicit labels, embedded in file metadata, that identify the content as AI-generated and name the provider. In October 2025, the Standing Committee of the national legislature amended the Cybersecurity Law to add an article on the "safe and sound development of AI", in force from 1 January 2026 [@xinhua2025china]. In April 2026, five agencies issued interim measures on "anthropomorphic" AI services, which simulate human personalities for companionship or emotional support [@xinhua2026five]. Effective from 15 July 2026, they require security assessments, algorithm filing and protections for minors and older users. This step-by-step approach lets regulators act quickly on a specific concern, while keeping close state control over the content that AI services produce.

The **United Kingdom** has so far kept to the sectoral approach of its 2023 white paper [@dsit2023proinnovation]. Its main AI-specific body, the AI Safety Institute, was renamed the AI Security Institute in February 2025 [@dsit2025tackling]. It was refocused on risks with security implications, such as cyber-attacks, chemical and biological misuse, and crime, and the government stated that it would not focus on bias or free speech. The governing Labour Party had pledged binding rules for the most powerful models. Yet the King's Speech of 13 May 2026, which sets out the government's legislative programme, contained no AI bill [@iapp2026kings]. The UK's main AI decision of 2026 concerned copyright and is discussed in Section 13.6.

These four jurisdictions are not the only ones, but they illustrate the main options. The EU has a comprehensive risk-based statute, and the US relies on executive orders plus state legislation. China uses targeted agency rules with strong content control, and the UK applies principles through existing regulators. The work of AI safety institutes is covered in Chapter 12, and export controls on chips in Chapter 7.

## 13.5 International coordination

AI models cross borders easily, which creates a case for international rules. Yet states disagree about values and compete for economic and military advantage. They also have few institutions with authority over AI. Figure 13.2 summarises the main international and national milestones from 2023 to 2026.

![Figure 13.2: Selected milestones in AI governance, 2023–2026, by jurisdiction. National and regional laws (upper lanes) developed alongside non-binding international declarations and one binding treaty, not yet in force by October 2026 (lower lanes). Source: @ukgov2023bletchley; @dsit2024frontier; @elysee2025statement; @pib2026india; @councilofeurope2024framework; @un2025terms; @europeanparliament2024regulation; @europeanparliament2026regulation; @biden2023safe; @trump2025ensuring; @cac2025measures; @californiagovernor2025governor.](../figures/svg/fig-13-02.svg){#fig:13-02}

A series of summits began at Bletchley Park in the UK on 1–2 November 2023. Twenty-eight countries and the EU, including the US and China, signed the **Bletchley Declaration**. It recognised the potential for "serious, even catastrophic, harm" from the most capable frontier models [@ukgov2023bletchley]. At the follow-up summit in Seoul in May 2024, 16 companies signed the **Frontier AI Safety Commitments** [@dsit2024frontier]. They promised to publish safety frameworks setting thresholds at which risks would be "intolerable". In the extreme, they promised not to develop or deploy a model if risks could not be kept below those thresholds. Four more companies joined later.

The summit in Paris on 10–11 February 2025 was renamed the AI Action Summit. It shifted emphasis towards inclusion, sustainability and economic opportunity [@elysee2025statement]. The priorities in its closing statement included narrowing digital divides, avoiding market concentration, considering AI's effects on work and its environmental footprint, and strengthening international cooperation. The statement was signed by 63 countries plus the EU and the African Union Commission (as listed in October 2026), but not by the United States or the United Kingdom. India hosted the AI Impact Summit in New Delhi on 16–20 February 2026, organised around "people, planet and progress" [@pib2026india]. The Indian government described it as the first global AI summit held in the Global South. The shift in titles, from "safety" to "action" to "impact", tracks a shift in political priorities.

What did the summits achieve? None of their outcomes is legally binding, and none creates a body that can check compliance. Their main effects have been indirect. They put frontier-model risk on the agenda of heads of government. They produced company commitments resembling duties later written into binding rules: the Seoul promises to publish safety frameworks anticipate similar requirements in SB 53 and the EU Code of Practice. And they created regular occasions for governments that otherwise rarely cooperate to meet. The same features leave them exposed to changes in national politics. The United States and the United Kingdom, both signatories at Bletchley, did not sign the Paris statement [@ukgov2023bletchley; @elysee2025statement].

The only binding international treaty specifically on AI is the Council of Europe's **Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law**. It was opened for signature on 5 September 2024, when the UK, the United States and the EU were among the first to sign [@moj2024uk; @councilofeurope2024framework]. It requires parties to ensure that activities across the lifecycle of AI systems are consistent with human rights, democracy and the rule of law. It enters into force about three months after five signatories, including at least three Council of Europe member states, have ratified it. Signature alone does not bind a state to apply a treaty; ratification does. According to the Council of Europe's treaty office, as of 22 October 2026 the convention had 21 signatories, including Canada, Japan and Ukraine. Only one, the EU (on 15 May 2026), had ratified it, so the treaty was not yet in force.

The United Nations has acted through the General Assembly. Resolution 78/265 of 21 March 2024 called for "safe, secure and trustworthy" AI for sustainable development [@un2024seizing]. Resolution 79/325 of 26 August 2025 established two bodies, both limited to the non-military domain [@un2025terms]. The first is an **Independent International Scientific Panel on AI** of 40 experts serving three-year terms, to produce evidence-based assessments. The second is a **Global Dialogue on AI Governance**. It was to be launched during the General Assembly's high-level week in 2025, then held in Geneva in 2026, alongside the International Telecommunication Union's AI for Good summit, and in New York in 2027. The model is loosely that of the Intergovernmental Panel on Climate Change: shared scientific assessment as a basis for later political agreement. Two differences may make the task harder for AI: capabilities change far faster than the climate system, and much of the relevant evidence is held by private companies.

Two further forums matter. The **OECD AI Principles**, adopted in 2019 and updated in May 2024, had 47 adherents in 2026. They set out values such as human rights, transparency, robustness and accountability [@oecd2024principles]. The G7's **Hiroshima AI Process** produced International Guiding Principles and a Code of Conduct for organisations developing advanced AI systems. G7 leaders endorsed them on 30 October 2023 [@mic2023hiroshima]. Since February 2025 the OECD has run a voluntary reporting framework against the Code; a first report was based on 20 organisations' submissions [@oecd2025hiroshima].

Finally, **technical standards** turn principles into checklists that auditors can verify. ISO/IEC 42001, published in 2023, specifies requirements for an AI management system: the policies, roles and processes an organisation uses to develop or use AI responsibly [@iso2023information]. Organisations can be certified against it, much as they are against quality-management or information-security standards. Under the EU AI Act, compliance with "harmonised" European standards will give a presumption of conformity. Their late arrival, however, was one of the reasons given for the omnibus delays [@europeanparliament2026regulation].

## 13.6 Copyright, training data and liability

Large models are trained on vast collections of text, images and music, much of it protected by copyright. Two legal questions arise. The **input question** asks whether copying works to train a model infringes copyright. The **output question** asks whether a model, or what it generates, reproduces protected works. By October 2026, courts in the US, the UK and Germany had given partial and sometimes conflicting answers. In brief, two US trial courts had ruled for AI developers on training with books, while a US appeals court and a German court had ruled against particular uses. Many training datasets also contain personal data, which raises a separate set of questions under data-protection law.

In the United States, the key defence is **fair use**, which allows some unlicensed use of copyrighted works. Courts weigh four factors. The first is the purpose and character of the use, including whether it is "transformative", meaning it adds a new purpose. The others are the nature of the work, the amount used, and the effect on the market for the original. Three rulings set out the current range of views.

::: {.box .case}
**Case study: Bartz v. Anthropic**

Authors sued Anthropic, alleging that it had trained its Claude models on their books without permission. On 23 June 2025, Judge William Alsup ruled that using books to train the models was "exceedingly transformative" and a fair use [@usdcnortherncal2025bartz]. So was scanning print books that the company had bought. He did not excuse the company's downloading of millions of books from pirate websites to build a permanent library, and that claim went towards trial. The parties then settled for $1.5 billion. On 20 July 2026, Judge Araceli Martínez-Olguín, who had taken over the case, granted final approval [@bloomberglaw2026anthropic]. The settlement covered more than 480,000 works, at about $3,100 per work, and required Anthropic to destroy the pirated datasets. According to the settlement website, the administrator began notifying claimants about their claims in September 2026. Payments were to follow once claims and disputes between co-claimants had been processed [@anthropicsettlement2026]. The settlement sets no legal precedent, but it shows that how training data is acquired can matter as much as how it is used.
:::

Two days after the Bartz ruling, Judge Vince Chhabria granted summary judgment to Meta in *Kadrey v. Meta* [@usdcnortherncal2025kadrey]. (Summary judgment decides a case without a full trial, when the key facts are not in dispute.) He did so only because the authors had not presented evidence that Meta's models harmed the market for their books. He warned that copying protected works to train generative models without permission would, "in most cases", likely be illegal. Such models could flood the market with competing works, a harm he called "market dilution".

On 29 September 2026, the Court of Appeals for the Third Circuit ruled in *Thomson Reuters v. Ross Intelligence* [@thirdcircuit2026thomson]. It held that a legal-research start-up's use of Westlaw's case summaries to train its AI was not fair use, because the use served the same purpose as the original and aimed to compete with it. The court stressed that Ross's system was not generative and distinguished the generative-AI cases. It also noted a statement that the US Department of Justice had filed on 1 September 2026 in the consolidated cases against OpenAI in New York, which include the *New York Times* claims. The statement argued that training a large language model is transformative; those cases remained pending. The US Copyright Office released its analysis of generative AI training in pre-publication form in May 2025, and had not finalised it by October 2026 [@uscopyrightoffice2025copyright].

In the UK, Getty Images sued Stability AI over the image generator Stable Diffusion [@highcourt2025getty]. Getty dropped its main training claim, since there was no evidence that the training had taken place in the UK. On 4 November 2025 the High Court rejected its remaining copyright claim, holding that the model was not an "infringing copy" of Getty's photographs. It found some trade-mark infringement involving Getty and iStock watermarks in outputs of older model versions. It called these findings, however, "historic and extremely limited in scope". The judge later gave Getty permission to appeal on the "infringing copy" point, calling it a question of law "on which the minds of reasonable lawyers may differ" [@fairhurst2026permission]. No appeal decision had been reported by October 2026. In March 2026, the UK government reported to Parliament on its earlier preferred option: a broad exception allowing training unless rights holders opted out [@dsit2026report]. After most consultation respondents rejected it, the option was "no longer the government's preferred way forward", and the government proposed to gather more evidence.

In Germany, the Munich Regional Court ruled on 11 November 2025 in a case brought by GEMA, the music-rights society, that OpenAI had infringed copyright in song lyrics [@gema2025landmark]. According to GEMA's account of the judgment, ChatGPT's models contained copies of the lyrics and reproduced them in response to simple prompts. GEMA reports that the court held that OpenAI needed licences both to train and to operate ChatGPT with these lyrics. In its account, the EU's text-and-data-mining exception did not justify storing or outputting them, since "OpenAI is not a privileged research organisation". Unlike the US rulings, this decision turned on memorisation: the court treated the model as containing copies of the works. The UK High Court, applying different law to different facts, reached a different conclusion on this point for Stable Diffusion. The Munich decision was a first-instance judgment, meaning a ruling by the court that first heard the case, and is open to appeal. Under the EU AI Act, GPAI providers must in any case respect rights holders' machine-readable opt-outs and publish summaries of their training content [@europeanparliament2024regulation].

Copyright is not the only body of law that reaches training data. Text and images collected from the web contain much **personal data**, meaning information about an identifiable person. In the EU its use is governed by the GDPR, which requires a legal basis, such as consent or a "legitimate interest", for each use. National data-protection authorities enforce the GDPR, and they acted on AI well before the AI Act applied. On 30 March 2023 the Italian authority, the Garante, ordered OpenAI to stop processing Italian users' data through ChatGPT [@garante2023intelligenza]. It cited missing information to users, no legal basis for the "massive collection and processing of personal data" used in training, and no age checks. In December 2024 it fined OpenAI €15 million, again citing among other things the lack of a legal basis for training. In March 2026, however, the Tribunal of Rome upheld OpenAI's appeal against that decision [@garante2024chatgpt].

Other actions show the range of tools. In May 2024 the Dutch authority fined Clearview AI €30.5 million [@edpb2024dutch]. The company had collected facial images for a recognition service aimed at law enforcement. It processed these biometric data without a legal basis and without adequately informing the people concerned. Large platforms have faced pressure rather than fines. In June 2024 Meta paused plans to train its models on public posts by adults in the EU, after the Irish Data Protection Commission raised concerns [@dpc2025statement]. Meta started such training from 27 May 2025, after changing its notices and making it easier for users to object. In the meantime the Irish regulator had asked the European Data Protection Board, which brings together the EU's national authorities, for a formal opinion. Opinion 28/2024 of December 2024 set out three points [@edpb2024opinion]. A model counts as anonymous only if it is "very unlikely" that people in the training data can be identified or their data extracted by queries. Legitimate interest can justify training if the processing is strictly necessary and passes a balancing test. And a model developed with unlawfully processed data may be unlawful to deploy "unless the model has been duly anonymised".

**Liability** for harm caused by AI raises related questions. When an AI system gives dangerous advice or makes a discriminatory decision, it may be unclear whether the developer, the deploying company or the user is responsible. The EU's revised Product Liability Directive applies to products placed on the market from 9 December 2026 [@europeancommission2024liability]. It explicitly covers all software, including AI systems. It can also hold manufacturers liable for defects that arise through updates or machine learning after release. In the US, liability is developing through state statutes, such as SB 53's civil penalties and Colorado's treatment of violations as deceptive trade practices. It is also developing through individual lawsuits.

## 13.7 Compute thresholds and frontier models

Regulators need a way to decide which models deserve extra scrutiny before anyone knows exactly what those models can do. The most common answer has been a **compute threshold**: a legal trigger based on the amount of computation used in training, measured in floating-point operations (FLOP). The EU uses 10^25 FLOP as the presumption of systemic risk. California's SB 53 and New York's RAISE Act use 10^26, as did the revoked US Executive Order 14110 [@europeanparliament2024regulation; @metr2026frontier; @biden2023safe]. Training compute has grown quickly (Chapter 4), so the choice of number matters.

::: {.box .deeper}
**Going deeper: What does 10^25 FLOP mean?**

10^25 is a 1 followed by 25 zeros, or ten million billion billion operations. A rough estimate of training compute is 6 × (number of model parameters) × (number of training tokens). The factor of six arises because each token requires about six arithmetic operations per parameter across the forward and backward passes (Chapter 2). Take a model with 100 billion parameters (10^11) trained on 15 trillion tokens (1.5 × 10^13). It would use about 6 × 10^11 × 1.5 × 10^13 ≈ 9 × 10^24 FLOP, just under the EU threshold. Because the threshold is fixed while training budgets grow, more models cross it each year. Epoch AI counted 33 publicly disclosed models trained with at least 10^25 FLOP by June 2025, from 12 developers [@rahman2025over].
:::

The case for compute thresholds is practical. In a preprint, Sastry and colleagues argue that compute is an unusually good lever for governance because it is "detectable, excludable, and quantifiable". The chips it relies on also come from a highly concentrated supply chain [@sastry2024computing]. Heim and Koessler, also in a preprint, argue that training compute is the best available metric for *identifying* models that warrant oversight [@heim2024training]. It correlates with capabilities, can be measured early, and can be verified by outsiders. They stress, however, that it is an imperfect proxy for risk. It should serve only as an initial filter that triggers evaluations, not as a measure of danger in itself.

Critics question even that role. In a third preprint, Hooker argues that the relationship between compute and risk is "highly uncertain and rapidly changing" [@hooker2024limitations]. Smaller models trained with better data and methods can match larger ones, so a fixed threshold may both catch harmless models and miss dangerous ones. The EU addressed this by letting the Commission designate models as systemic-risk on other grounds, such as capabilities or number of users [@europeanparliament2024regulation]. The US government's 2026 cyber-capability framework took a different approach. It defined "covered frontier models" by results on a classified capability benchmark rather than by compute [@trump2026promoting].

The resulting rules on each side of the Atlantic are more alike than their political framing suggests. Both the EU's systemic-risk duties and California's SB 53 require the largest developers to assess catastrophic or systemic risks, document their safety measures, and report serious incidents to a public authority [@europeanparliament2024regulation; @metr2026frontier]. The main differences lie in enforcement and reach. The EU has an EU-wide authority with turnover-based fines, while California relies on a state attorney general with fixed penalties. The EU rules reach any provider placing a model on the EU market; SB 53 reaches developers subject to California law.

The rules triggered by these thresholds are, so far, mostly about **transparency and process**: publishing safety frameworks, testing models, reporting incidents and protecting whistleblowers. None of the jurisdictions examined here requires a licence to train or release a frontier model, and the 2026 US order explicitly rules one out [@trump2026promoting]. Are disclosure duties of this kind enough, or will pre-approval eventually be needed for the most capable systems? This is one of the central open questions of AI governance. It links directly to the safety methods discussed in Chapter 12 and the scenarios in Chapter 14.

## Summary
- AI governance combines hard law, soft law, technical standards and liability; jurisdictions differ mainly in how they mix these instruments.
- The EU AI Act (Regulation (EU) 2024/1689) is a horizontal, risk-based law: prohibitions since February 2025, general-purpose AI duties since August 2025, and high-risk obligations deferred by the July 2026 Digital Omnibus to December 2027 (Annex III) and August 2028 (Annex I).
- The US has no comprehensive federal AI statute. Executive orders since 2025 favour deregulation and voluntary arrangements, while a December 2025 order targets state laws through litigation and funding conditions; federal pre-emption legislation was pending in October 2026.
- US states, notably California (SB 53, in force since January 2026) and New York (RAISE Act, due January 2027), regulate frontier developers mainly through transparency and incident reporting; Colorado replaced its broad AI Act with a narrower disclosure law amid federal litigation.
- China regulates through targeted agency rules on generative AI, labelling and anthropomorphic services, with strong content controls; the UK relies on existing regulators and had no AI bill as of October 2026.
- International coordination rests mainly on non-binding declarations, UN scientific and dialogue bodies, OECD and G7 principles, and one Council of Europe treaty that was not yet in force.
- Courts are split on copyright and training: two US district courts ruled for AI developers on training with books in 2025 (in one case only because the authors had not shown market harm), the Third Circuit rejected fair use for a non-generative competitor in 2026, and German and UK courts have reached their own, partly contrary, conclusions; several key cases remain pending.
- EU data-protection authorities have acted on AI training under the GDPR through orders, fines and a 2024 opinion of the European Data Protection Board; Italy's €15 million fine on OpenAI was overturned on appeal in March 2026.
- Compute thresholds (10^25 or 10^26 FLOP) are a practical but imperfect trigger for frontier-model rules, and are increasingly supplemented by capability-based tests.

## Key terms
AI governance · hard law · soft law · risk-based regulation · horizontal regulation · high-risk AI system · general-purpose AI model · systemic risk · code of practice · pre-emption · algorithm filing · framework convention · fair use · compute threshold · harmonised standard

## Discussion questions
1. The EU deferred its high-risk AI rules in 2026 because standards and authorities were not ready. Does this show that comprehensive AI legislation came too early, or that its implementation was under-resourced? What evidence would help you decide?
2. Using the four fair-use factors, analyse a hypothetical AI music generator trained on commercial recordings. How might the reasoning in *Bartz*, *Kadrey* and *Thomson Reuters v. Ross* each apply?
3. Compare the EU's 10^25 FLOP presumption with a capability-based test such as the one in US Executive Order 14409. Which is easier to enforce, and which better tracks risk?
4. The debate box cites a study of the GDPR's effect on venture investment as evidence about AI regulation. How far does that evidence transfer to the AI Act, and what kind of study, using data available after 2027, would most convincingly test Draghi's and Bradford's competing claims?
5. Apply the distinction between horizontal and sectoral regulation to a new case: AI systems used by banks to assess loan applications. How would the EU, the UK and Colorado (under SB 26-189) each handle such a system?
6. The Seoul commitments to publish safety frameworks were followed by similar duties in SB 53 and the EU Code of Practice. Does this sequence show that soft law changed behaviour, or might the same duties have arisen anyway? What evidence would distinguish the two explanations?

## Further reading
- European Parliament and Council (2024). *Regulation (EU) 2024/1689 (Artificial Intelligence Act)*. The primary text; read Articles 3, 5, 6, 50, 51–55 and Annex III alongside the 2026 amendments. [@europeanparliament2024regulation]
- European Parliament and Council (2026). *Regulation (EU) 2026/1744 (Digital Omnibus on AI)*. Shows how and why the Act's timetable and scope were changed before its main rules applied. [@europeanparliament2026regulation]
- Sastry, G. et al. (2024). *Computing Power and the Governance of Artificial Intelligence*. A thorough preprint on why compute is used as a lever for AI governance and what it can achieve. [@sastry2024computing]
- Hooker, S. (2024). *On the Limitations of Compute Thresholds as a Governance Strategy*. A readable critique of the thresholds used in US and EU rules (preprint). [@hooker2024limitations]
- Bradford, A. (2024). *The False Choice Between Digital Regulation and Innovation*. Northwestern University Law Review. A careful argument against the claim that EU regulation explains Europe's technology gap. [@bradford2024false]
- Department for Science, Innovation and Technology (2026). *Report on Copyright and Artificial Intelligence*. A clear official overview of the policy options on training data and copyright, and why the UK changed course. [@dsit2026report]
- European Data Protection Board (2024). *Opinion 28/2024 on Certain Data Protection Aspects Related to the Processing of Personal Data in the Context of AI Models*. The EU regulators' joint view on when AI models trained on personal data are lawful. [@edpb2024opinion]


```{=html}
<section class="part"><p class="part-label">Part V</p><h1 class="part-title">The Decade Ahead</h1></section>
```

# Chapter 14: Forecasting the Next Ten Years: Methods, Scenarios and Open Problems

::: {.objectives}
**After working through this chapter you should be able to:**

- explain why forecasts about AI have often been wrong, and in which direction;
- compare expert surveys, forecasting tournaments, trend extrapolation and scenario writing as ways of thinking about the future;
- evaluate a published AI scenario by identifying its key assumptions and the evidence for each;
- describe the main uncertainties that will shape AI over the next decade;
- assess the research proposals at the end of the chapter, including the prior work each one builds on and the question that would test it.
:::

In October 2023, 2,778 researchers who had published at leading AI conferences answered a survey about the future of their field. Asked when unaided machines would be able to do every task better and more cheaply than human workers, they gave, in aggregate, a 50% chance by 2047. The same question, put to a smaller group a year earlier, had produced 2060 [@grace2025thousands]. Thirteen years had disappeared from the forecast in roughly twelve months.

The same survey contains a second, stranger result. When the question was phrased in terms of occupations (when would all human jobs be fully automatable?), the aggregate 50% date was 2116 [@grace2025thousands]. The two questions describe almost the same world, yet the answers lie about seventy years apart. This chapter starts from that puzzle. It asks what tools exist for thinking about AI's next ten years, how well they have worked, and what they can and cannot tell us. It ends with a set of open research problems, presented as the author's own proposals, about risks that may matter more as AI agents spread.

## 14.1 Why forecasting AI is hard

A **forecast** is a statement about the future that can later be checked: a date, a number or a probability. Forecasting AI is difficult for at least four reasons. Progress depends on several inputs at once (computing power, data, algorithms and money), and each can change course. Capabilities are hard to define and measure, so even the present is blurred (Chapter 4). Adoption by firms and governments moves at a different speed from invention. And forecasts can change the thing they predict, because investors and regulators act on them.

Each difficulty has a practical consequence. Because several inputs interact, a forecast that tracks only one of them (for example, chip supply) can be right about that input and wrong about the outcome. Because capability is measured with benchmarks that saturate or leak into training data, a forecast can resolve "yes" on paper while the underlying ability remains in doubt. And because adoption lags invention, a forecast about what AI *can* do in 2030 says little by itself about what it *will* be doing in hospitals, courts or classrooms that year.

The historical record shows errors in both directions. In 1955 the organisers of the Dartmouth summer project, which gave the field its name, proposed a two-month study. They wrote that "a significant advance can be made in one or more of these problems if a carefully selected group of scientists work on it together for a summer" [@mccarthy2006proposal]. In 1960 Herbert Simon predicted that "machines will be capable, within twenty years, of doing any work that a man can do" [@simon1960new, p. 38]. Melanie Mitchell describes the field's history as a cycle of optimistic predictions and heavy investment ("AI springs") followed by disappointment and cuts in funding ("AI winters") [@mitchell2021why].

Long-range predictions also show a suspicious regularity. Stuart Armstrong and Kaj Sotala analysed 95 published predictions of when human-level AI would arrive and found that the most common horizon was 15 to 25 years from the date of the prediction [@armstrong2015how]. A later re-analysis, published on the AI Impacts website, found an error in their comparison of experts with non-experts, though a tendency to predict roughly 10 to 25 years ahead remained [@grace2016error]. A horizon that stays constant while the calendar moves suggests that such forecasts reflect a habit of mind as much as evidence.

Some recent errors have run the other way. In August 2021 Jacob Steinhardt's research group ran a forecasting contest, on a commercial forecasting platform, to predict scores on several AI benchmarks; Steinhardt reported the results on his blog. For the MATH benchmark of competition mathematics problems, the forecasters' aggregate prediction for June 2022 was 12.7%; the best actual result by then was 50.3%, far in the tail of their distribution [@steinhardt2022ai]. Short-run benchmark progress and long-run claims about "human-level AI" are different kinds of question, and the record shows forecasters erring on each in a different direction.

## 14.2 Asking people: surveys, tournaments and markets

The simplest way to forecast is to ask people who know the field. **Expert surveys** such as that of Grace and colleagues have the advantage of scale and repeatability. Their weaknesses are visible in the opening example: answers are sensitive to wording, and experts in building AI systems are not necessarily experts in predicting how economies adopt them. Figure 14.1 shows how far the 2022 and 2023 answers moved, and how far apart the two framings of the question remain.

![Figure 14.1: Aggregate year by which AI researchers gave a 50% chance to two milestones, in surveys run in 2022 and 2023. "High-level machine intelligence" asks when machines will do every task better and more cheaply than humans; "full automation of labour" asks when every occupation will be automatable. The gap between framings is larger than the change between years. Source: @grace2025thousands.](../figures/svg/fig-14-01.svg){#fig:14-01}

A second approach comes from research on forecasting itself. In the early 2010s a US government-funded geopolitical forecasting tournament had university research groups compete to give the most accurate probabilities for world events. One of the competing groups, the Good Judgment Project, found that training in probability, working in teams and grouping the best performers together each improved accuracy [@mellers2014psychological]. Philip Tetlock and Dan Gardner describe the top performers, called **superforecasters**, as people who gather evidence from many sources, think in probabilities and update their views when wrong [@tetlock2015superforecasting]. Accuracy in these tournaments is scored with measures such as the Brier score, explained in the "Going deeper" box below.

::: {.box .deeper}
**Going deeper: Two pieces of forecasting arithmetic**

The Brier score rates probability forecasts [@brier1950verification]. For each question, take the probability you gave, subtract the outcome (1 if the event happened, 0 if it did not), and square the result; then average over all questions. A forecaster who said 90% for an event that happened scores 0.01 on that question; one who said 90% for an event that did not happen scores 0.81. Lower is better, and a forecaster who always says 50% scores 0.25.

A doubling time turns a trend into a projection. If a quantity doubles every seven months, then after 14 months it is 4 times larger, after 28 months 16 times, and after 49 months (seven doublings) 128 times. The arithmetic is simple; the hard question is whether the doubling will continue.
:::

A third approach uses markets and aggregation platforms. In a **prediction market**, people buy and sell contracts that pay out if an event occurs, so the price can be read as a collective probability. Justin Wolfers and Eric Zitzewitz found that such market forecasts are typically fairly accurate and outperform most moderately sophisticated benchmarks [@wolfers2004prediction]. Online forecasting platforms apply a similar logic without money, by scoring and aggregating many individual forecasts. Markets and platforms work best on questions that resolve clearly and soon. Questions such as "when will AI match humans at every task?" are hard to define precisely, take decades to resolve and give participants little reason to correct a mispriced long-range forecast.

These methods were brought together on AI risk in the Existential Risk Persuasion Tournament, run in 2022 with 80 domain experts and 89 superforecasters. Participants forecast, argued with each other and then forecast again. On the probability that AI would cause human extinction by 2100, the median domain expert said 3% and the median superforecaster 0.38%. Few minds changed during the tournament [@karger2023forecasting; @karger2025subjective].

Some of the tournament's shorter-run questions have since resolved. A 2025 working paper by the organisers scored the 38 that had resolved by mid-2025 [@kucinskas2025assessing]. Overall, superforecasters and domain experts performed about equally well, and the differences between them were not statistically significant. Both groups underestimated AI progress, and the superforecasters did so more. On four AI benchmark questions, superforecasters had on average given a 9.7% probability to the outcomes that occurred, against 24.6% for domain experts. Near-term accuracy was not correlated with forecasts of long-term risk, so these results do not show whose extinction estimate is better.

::: {.box .debate}
**Debate: Whose forecasts of AI should we trust?**

*Domain experts.* People who build AI systems see capabilities before the public does and understand the technical bottlenecks. Recent history supports this view in one respect. Forecasters recruited through a commercial platform underestimated benchmark progress in 2021–22 [@steinhardt2022ai]. In the tournament's resolved AI questions, superforecasters were further from the outcome than domain experts [@kucinskas2025assessing].

*Generalist forecasters.* Superforecasters have a measured track record on short-run questions [@mellers2014psychological]. Long-range predictions of human-level AI, including many by AI researchers, have historically clustered at a fixed distance ahead [@armstrong2015how; @grace2016error]. And across all the tournament questions resolved so far, domain experts were no more accurate than superforecasters.

*The missing evidence.* Neither group has a track record on decade-long AI questions, because those questions have not yet resolved. The tournament organisers note that superforecasters have no track record on long time horizons [@karger2023forecasting]. The first scored results rest on a handful of AI questions. Scoring both groups on many medium-range AI questions (one to five years) as they come due would provide a firmer test.
:::

## 14.3 Extrapolating trends

**Trend extrapolation** means fitting a line to past data and extending it. It is among the most transparent methods, because anyone can inspect the data and the line. For AI, three trends are watched most closely.

The first is training compute. Epoch AI estimates that the computing power used to train notable AI models grew about 4 to 5 times per year between 2010 and May 2024 [@sevilla2024training]. The second is algorithmic efficiency: for language models, the compute needed to reach a given level of performance halved roughly every eight months between 2012 and 2023, with wide uncertainty [@ho2024algorithmic]. The third is a direct measure of capability. METR's **time horizon** is the length of software task, measured by how long it takes a skilled human, that an AI agent completes with 50% reliability (Chapter 4). Kwa and colleagues found that this horizon doubled approximately every seven months from 2019 to early 2025 [@kwa2025measuring]. An updated task suite ("Time Horizon 1.1"), released in January 2026, gave the same long-run doubling time and a faster one, about 131 days, for models since 2023 [@metr2026time]. METR's data file, as last updated in September 2026 with newer models and revised estimates, puts the post-2023 doubling time at about 129 days; Chapter 4 uses these later figures [@metr2026task]. By February–March 2026 METR estimated the public frontier at around 12 hours, with a wide uncertainty range (about 5 to 61 hours). It also reported that its task suite could no longer reliably measure horizons above 16 hours [@metr2026risk].

Extrapolation has two well-known weaknesses. A trend measured on a benchmark may not carry over to messier real-world work, a limitation METR itself discusses [@kwa2025measuring]. And every exponential in the physical world eventually meets a constraint. Epoch AI's analysis of whether scaling can continue to 2030 examined four candidates: electrical power, chip manufacturing, data and the minimum time needed for each training step. It concluded that training runs of about 2 × 10^29^ operations would likely be feasible by 2030, with power the constraint most likely to bind first [@sevilla2024can]. On data, Villalobos and colleagues estimated that the stock of public human-written text would be fully used by training runs at some point between 2026 and 2032 [@villalobos2024position].

A trend line therefore answers a conditional question: if the inputs keep growing and nothing else changes, where do we arrive? It does not tell us whether the inputs will keep growing. That question requires a different method.

Reading a trend chart well requires attention to the window over which the line is fitted. METR's own figures show the effect. In its January 2026 release, the time horizon fitted over 2019–2025 doubled about every 196 days [@metr2026time]. Fitted only to models since 2023, it doubled every 131 days, and fitted only to models since 2024, every 89 days. The September 2026 data file, with more models, gives about 188 days for the whole period since 2019 and 129 days since 2023 [@metr2026task]. Each fit is honest, but they imply very different values a few years ahead. A careful reader asks which window was chosen, why, and how much the conclusion changes if the window moves.

## 14.4 Scenarios and key uncertainties

A **scenario** is a coherent, detailed story of how the future might unfold, written to explore consequences rather than to assign a single probability. One of its best-known uses is in business planning. Pierre Wack led scenario work at Royal Dutch/Shell. In 1985 he argued that forecasting had worked reasonably well in the stable 1950s and 1960s, but that its errors had become more frequent and sometimes dramatic since the early 1970s [@wack1985scenarios]. Scenarios were his response: several contrasting stories, each internally consistent, used to test whether a plan would survive in all of them.

The most discussed AI scenario of recent years is *AI 2027*, published in April 2025 by Daniel Kokotajlo, Scott Alexander, Thomas Larsen, Eli Lifland and Romeo Dean. It describes, month by month, AI systems that automate AI research itself, leading to rapidly accelerating progress. It offers two endings, labelled "race" and "slowdown". The authors present it as their best guess, not a recommendation. In a note added in November 2025 they stress that 2027 was their most likely single year at the time of writing [@kokotajlo2025ai]. Their median estimates were somewhat later, and later updates moved those medians further out.

*AI 2027* has drawn detailed criticism. A critique published as a blog post in June 2025, under the pseudonym titotal, examined the quantitative model behind the timelines [@titotal2025deep]. The model assumed that each doubling of the time horizon would take 10% less time than the last. The critique argued that this assumption was weakly justified, and that curves fitting the same eleven data points about equally well gave very different forecasts. A different critique concerns the whole framing. In an essay, Arvind Narayanan and Sayash Kapoor argue that AI should be understood as "normal technology", whose economic effects arrive through slow diffusion: "Diffusion occurs over decades, not years" [@narayanan2025ai]. The two views disagree less about current capabilities than about how quickly capability turns into change in the world. Evidence on that question is mixed so far. According to one working paper, generative AI spread among individuals faster than personal computers or the internet did, measured from each technology's first mass-market product [@bick2024rapid]. Individual use, however, is not the same as firms reorganising their work around a technology.

Figure 14.2 places these views inside a single **uncertainty fan**, in which the range of plausible outcomes widens with distance into the future. Scenarios are useful because they mark out different regions of this fan, not because any one of them sits at its centre.

![Figure 14.2: An uncertainty fan for AI capability and impact, 2026–2036 (schematic, not to scale). The fan widens with time. Labelled paths illustrate published views: continued trend extrapolation, a fast acceleration scenario such as AI 2027, a "normal technology" path with slow diffusion, and a plateau caused by binding constraints such as power or data. Diagram by the author, based on @kokotajlo2025ai, @narayanan2025ai and @sevilla2024can.](../figures/svg/fig-14-02.svg){#fig:14-02}

What determines where in the fan the next decade will fall? Six uncertainties recur across the literature:

- **Compute:** whether investment in chips and power keeps growing at recent rates, and where power runs short first [@sevilla2024can].
- **Data:** whether synthetic data and new sources replace exhausted public text [@villalobos2024position].
- **Algorithms:** whether efficiency gains continue at a rate comparable to the last decade [@ho2024algorithmic].
- **Regulation:** how laws such as the EU AI Act, whose obligations take effect in stages from 2024, are applied in practice [@europeanparliament2024regulation] (Chapter 13).
- **Adoption:** how fast use spreads. By late 2024 nearly 40% of US residents aged 18 to 64 had used generative AI [@bick2024rapid].
- **Public opinion:** whether trust or concern dominates. In a 2024 Pew survey, 51% of US adults said they were more concerned than excited about AI in daily life, compared with 15% of AI experts [@pew2025how].

Each scenario is, in effect, a choice of values for these six variables, and a reader can ask which values it has chosen.

A short set of questions helps when reading any scenario, optimistic or pessimistic. Which trends does it extend, and over what window? Which constraint does it assume will not bind? What does it assume about adoption, as opposed to capability? Which step in the story, if it failed, would change the ending most? And what observable event in the next year or two would count as evidence for or against it? The authors of *AI 2027* invite this kind of reading by publishing their forecasting models; their critics engage at exactly these points [@kokotajlo2025ai; @titotal2025deep].

## 14.5 Open problems I: when many agents act alike

The remainder of the chapter turns from methods to open problems. Its subject is a risk that the methods above do not address directly. What happens when large numbers of AI agents, each behaving correctly for its own user, act in the same way at the same moment? Chapter 11 introduced the evidence that models share errors. Kim and colleagues tested more than 350 language models [@kim2025correlated]. On one leaderboard, when two models were both wrong they gave the same wrong answer about 60% of the time. Larger, more accurate models had highly correlated errors, even across providers. Jiang and colleagues found that different models give strikingly similar answers to open-ended questions [@jiang2025artificial]. Kleinberg and Raghavan showed that when many decision-makers use the same algorithm, overall decision quality can fall even if that algorithm is the most accurate for each of them alone [@kleinberg2021algorithmic].

These problems connect directly to the forecasting methods above. A correlated-action risk depends on adoption more than on capability. When one household in a hundred lets an agent manage its devices, scattered behaviour is harmless. The danger would appear only when the share of synchronised activity exceeds what a system can absorb. Such a risk would therefore grow with the success of the technology and could stay invisible during years of good experience. It sits in the region of the uncertainty fan where adoption is fast, whatever happens to frontier capability, and parts of it can be studied with data that exist now.

The proposals below are the author's. They are offered as research programmes, not as settled policy, and none has yet been tested. Each is stated with the prior work it builds on and a question that could test it; the names are new, but the underlying ideas draw on that work. Any numerical thresholds are illustrative starting points for debate.

**Proposal 14.1: Population-level evaluation of agent fleets.** Current evaluations run one copy of a model through many tasks. A population-level evaluation would run many copies through one stress scenario, such as a sudden price change. There might be thousands of copies, each given a realistic variation in context, such as a different user's preferences. The evaluation would measure **action concentration**: the share of copies that choose the most common action. Figure 14.3 contrasts the two designs.

Prior work includes the correlated-error studies above. Bommasani and colleagues found that sharing training data across decision-makers increases **outcome homogenisation**, meaning that the same people receive bad outcomes from every system [@bommasani2022picking]. A technical report by Hammond and colleagues offers a taxonomy of multi-agent risks that names miscoordination, conflict and collusion as failure modes [@hammond2025multi]. *Research question:* does action concentration measured in simulation predict correlated behaviour in deployed agent populations, and does it differ from answer-level error correlation?

A population-level evaluation differs from red-teaming (Chapter 12), which searches for any input that makes a single model fail. It asks a narrower question: given an ordinary but stressful situation, do many copies converge on the same action?

![Figure 14.3: Two ways to evaluate AI agents. Left: conventional evaluation runs one model instance through many different tasks and reports average accuracy. Right: the proposed population-level evaluation runs many instances, each with a slightly different context, through one stress scenario and reports how concentrated their actions are. Diagram by the author.](../figures/svg/fig-14-03.svg){#fig:14-03}

**Proposal 14.2: Non-delegable safeguards.** Some safety mechanisms work only because the people who may override them do so rarely and at scattered moments. The case study below shows the pattern in electricity grids.

::: {.box .case}
**Case study: The 50.2 hertz problem**

The continental European grid runs at a frequency of 50 hertz, and its fast-acting reserves must cover at least a "reference incident": a sudden loss of 3,000 megawatts of generation [@eu2017sogl, art. 153(2)(b)]. Earlier German connection rules required solar installations to disconnect if frequency rose to 50.2 hertz, a sensible rule for each installation [@roselund2015has]. As solar capacity grew, the consultancy Ecofys and the University of Stuttgart studied the risk. Their study was commissioned by the German transmission operators, industry bodies and government. It estimated that in a worst case up to about 14 gigawatts could disconnect at the same instant, far beyond that reserve [@doring2012dealing].

A German ordinance in force from July 2012 required most existing solar installations above 10 kilowatts to be retrofitted [@germany2012sysstabv, §§ 2, 4]. They would then reduce output gradually as frequency rose. Where that was not possible, they would disconnect at different frequencies spread evenly across the installed capacity. At least 315,000 installations were affected, at an estimated cost of 65 to 170 million euros [@roselund2015has]. A rule that was safe for one device became a single point of failure when copied into hundreds of thousands.
:::

British regulation already applies the same lesson to demand. Under the Electric Vehicles (Smart Charge Points) Regulations 2021, a home charger must be able to apply a random delay of up to 1,800 seconds before charging starts [@uk2021electric]. By default it must apply one of up to 600 seconds. The owner may cancel that delay, and it does not operate if the owner has overridden it. The random delay spreads the start times of many chargers. The override is safe as long as people use it occasionally and at different times.

The proposal concerns a hypothetical future in which software agents manage most household devices. A 2026 Stanford policy brief recommends that developers and deployers of AI agents give them a duty of loyalty to their users [@smith2026designing]. If an agent owes its user such a duty, then cancelling a delay to catch a cheaper price period is the correct choice for each user. If millions of agents reach that conclusion in the same minute, the random delay is cancelled everywhere at once. Purely as illustration, half a million devices drawing 6 kilowatts each add up to 3 gigawatts, the size of the continental European reference incident. (Great Britain's grid is separate, and its reference incident is set instead by the largest single loss it could suffer [@eu2017sogl, art. 153(2)(b)].) Figure 14.4 sets out this mechanism. It is a hypothesis about a possible future, not a description of any event.

![Figure 14.4: A hypothetical mechanism for correlated override (schematic, not to scale). Left: human owners cancel a random start delay at scattered moments, so device starts stay spread out. Right: agents acting loyally for each owner cancel the delay at the same price signal, so starts coincide and the combined load step can exceed the grid's reference incident. Diagram by the author, based on @uk2021electric and @eu2017sogl.](../figures/svg/fig-14-04.svg){#fig:14-04}

A **non-delegable safeguard** would be a collective-safety mechanism that only a present human may override, through a physical or unscriptable action, never an agent acting on a standing instruction. The term borrows from law: English courts recognise exceptional "non-delegable duties", which a party cannot escape by handing a task to someone else [@supremecourt2013woodland]. The proposal has three further parts. The randomness would stay inside device firmware, out of the agent's reach. Manufacturers would report the share of starts in which the delay was overridden. And any fiduciary-duty rule would state that an agent which does not seek an override has not breached its duty. *Research question:* how often are such overrides used today, and how would the timing of overrides change if agents controlled them? No published measurement of override rates under the UK rule was found for this chapter.

The strongest objection is that grid engineers already understand synchronised load: they randomise device starts, they carried out the 50.2 hertz retrofit, and they wrote the UK rule itself. On this view the electricity sector will notice agent-driven overrides in its data and close the gap without a new legal category. The proposal accepts that the grid is the sector most likely to manage this risk. Its claim is narrower. The same pattern, an individual override on a safeguard whose real purpose is collective, may exist in sectors such as payments or ticketing. These lack a shared, instantly visible signal like grid frequency. Identifying such safeguards before agents reach them is itself an open research task.

**Proposal 14.3: The M-1 criterion.** Electricity planners in North America must show that the transmission system still performs acceptably after the loss of any single generator, line or transformer [@nerc2020transmission]. This "single contingency" test is known as N-1. The **M-1 criterion** would add one case. A critical system would have to stay within safe limits if every instance of its most widely deployed model family took the same plausible wrong action at the same moment. The idea rests on a long engineering literature about **common-cause failure**.

::: {.box .concept}
**Key concept: Common-cause failure**

A common-cause failure occurs when several components that were meant to back each other up fail together because they share a cause, such as a design flaw or a maintenance error. Nuclear and aerospace risk analysts have modelled such failures since the mid-1970s, for example with the "beta factor", the fraction of failures that strike all redundant copies at once [@stott2010common]. The analogy for AI is a set of model weights copied into millions of devices. It breaks down in one respect: a broken pump fails in a predictable way, whereas a model family may fail through a shared judgement that looks reasonable in each case.
:::

Software engineering tested this assumption directly. Algirdas Avizienis developed **N-version programming**, in which independent teams write separate programs from one specification and the programs vote [@avizienis1985nversion]. Eckhardt and Lee showed theoretically that if some inputs are more likely than others to lead programmers into error, independently written versions will tend to fail together [@eckhardt1985theoretical]. Knight and Leveson then had 27 versions written independently and ran each through one million tests [@knight1986experimental]. The programs were individually very reliable. Yet the number of tests on which more than one program failed was substantially higher than independence predicted. Together with Kim and colleagues' results across providers, this suggests that buying models from several companies may buy less diversity than it appears to. *Research question:* how should a "model family" be defined empirically, for example by the rate at which two models give the same wrong answer? And what share of a critical system can one family control before an M-1 study fails?

The main objection concerns cost. If one model family is the most accurate, requiring a critical system to rely partly on a weaker family will produce more errors in ordinary conditions. The finding that larger, more accurate models have highly correlated errors sharpens the dilemma. Two lines of work suggest the cost could be smaller than it appears, though neither tests it on large models. In a theoretical model, Kleinberg and Raghavan show that the most accurate choice for each decision-maker can lower the quality of decisions across the whole population [@kleinberg2021algorithmic]. And diversity can be trained for: Liu and Yao trained neural networks together with a penalty on correlated errors, so that members of the ensemble specialised [@liu1999ensemble]. Whether anything similar works across separately trained large models is unknown. M-1 would also leave several cheaper options before any limit on market share. Examples are randomness held in devices, staggered scheduling by a coordinator, and circuit breakers that pause a surge of identical agent actions.

**Proposal 14.4: A feedback provenance census.** Much of a model's behaviour is shaped in post-training by human raters, by other models acting as judges, and by synthetic data (Chapter 3). These sources may be shared across companies. GPT-4 acting as a judge agreed with human preferences over 80% of the time, about as often as humans agree with each other. Its authors presented "LLM-as-a-judge" as a scalable substitute for human ratings [@zheng2023judging]. Jiang and colleagues found reward models and judges less well calibrated to people where human tastes differ [@jiang2025artificial].

The proposal is a disclosure regime in which developers report through a trusted third party. They would state what share of their preference data came from shared rater pools, from judge models of each family and from other labs' synthetic data. It extends documentation standards such as datasheets for datasets [@gebru2021datasheets]. It also builds on an audit of more than 1,800 datasets by Longpre and colleagues, which found licence information missing in over 70% of cases on popular hosting sites [@longpre2024large]. *Research question:* how much of the measured error correlation between models from different companies can be explained by shared post-training sources, as opposed to shared pre-training data?

The census has clear limits. It cannot see the largest shared source, the public web used for pre-training, and if built carelessly it could expose individual raters. Any design would need privacy-preserving computation and a minimum group size below which no figure is published.

## 14.6 Open problems II: people, signatures and channels

The second group of proposals, again the author's own and offered on the same terms, concerns the human side of a world with many agents.

**Proposal 14.5: Competence reserves and skill fade.** Lisanne Bainbridge's "ironies of automation" observed that automating a process leaves humans to take over in rare emergencies [@bainbridge1983ironies]. They must then use skills that automation has given them little chance to practise. In 2013 the US Federal Aviation Administration warned that continuous use of autoflight systems "could lead to degradation of the pilot's ability to quickly recover the aircraft" [@faa2013manual]. It encouraged airlines to provide opportunities for manual flying. In medicine, a retrospective observational study at four endoscopy centres in Poland looked at colonoscopies done without AI [@budzyn2025endoscopist]. Their rate of detecting precancerous growths (adenomas) fell from 28.4% in the three months before AI was introduced to 22.4% in the three months afterwards. The evidence is not settled. A later prospective trial with 13 endoscopists used a related measure, the detection of polyps of 5 mm or more. It observed no deskilling in colonoscopies done after AI use ended [@pedersen2026learning]. At the entry level, a working paper by Brynjolfsson and colleagues examined 22-to-25-year-olds in AI-exposed US occupations [@brynjolfsson2026canaries]. In data to mid-2026, their employment was about 19% below the level it would have reached had it kept pace with less-exposed peers. In a working paper, Enrique Ide models how automating entry-level work can weaken the transfer of know-how from experts to novices [@ide2025automation].

A **competence reserve** would be a paid, regularly drilled group of people able to run a critical function, such as restoring a grid, without AI, with apprentices in every unit. Its health would be tracked by a reserve ratio: certified people divided by the crew needed to run minimum service by hand for a fixed period. *Research question:* how fast do critical manual skills fade under automation, and what drill frequency keeps them above a safe threshold?

Critics can reasonably reply that skills which are no longer needed should be allowed to fade, that part-time reservists will never match full-time experts, and that manual procedures may stop matching redesigned equipment. The proposal therefore limits reserves to a small set of functions where failure is fast, physical and system-wide, and it requires that such functions keep a manual mode worth drilling on.

**Proposal 14.6: Signature capacity and meaningful human oversight.** Laws increasingly require a human to approve automated decisions. The EU AI Act asks that people overseeing high-risk systems remain aware of the tendency of "automatically relying or over-relying on the output" [@europeanparliament2024regulation, art. 14(4)(b)]. The evidence on whether humans can do this at volume gives grounds for concern. Clinicians override drug safety alerts in 49% to 96% of cases, though the reviewers note that many overrides may be justified [@vandersijs2006overriding]. In an experiment with a purported AI system, inexperienced radiologists rated 79.7% of mammograms correctly when it suggested the right category, but only 19.8% when it suggested a wrong one [@dratsch2023automation]. Ben Green reviewed 41 policies requiring human oversight and argued that they rest on an untested assumption that people can perform it [@green2022flaws]. Madeleine Clare Elish named the result a **moral crumple zone**, in which responsibility is attributed to a human operator who had little real control [@elish2019moral].

**Signature capacity** is the proposed name for the number of decisions of a given kind a person can genuinely check in a given period. It could be measured by seeding a small number of known errors into the work, as airports already do with threat image projection. About 100 such test images per screener are enough for a reliable measure when they are hard enough [@buser2025reliability]. The proposal would cap a signer's liability in proportion to measured capacity divided by assigned volume, shifting the rest to the organisation that set the volume. *Research question:* how does the rate of caught errors fall as review volume rises, in real professional settings?

The idea carries risks. Signers may learn to recognise seeded items, so the test items would need to vary and to stay hard enough to be informative. The airport study itself identifies that condition [@buser2025reliability]. A capacity measure could also be turned into a disciplinary tool. The proposal therefore allows measured capacity to limit a signer's liability, never to extend it.

**Proposal 14.7: Legibility of agent-to-agent communication.** Agents that learn to communicate need not use human language. Andreas, Dragan and Klein developed a method to translate the vector messages of such agents into English after the fact [@andreas2017translating]. Lewis and colleagues found that letting two negotiating agents both learn from each other "led to divergence from human language", so they fixed one agent to imitate people [@lewis2017deal]. Current agent protocols are built for readability. Google's Agent2Agent protocol, launched in April 2025 with more than 50 technology partners according to the company, builds on common web standards such as HTTP and JSON-RPC [@surapaneni2025announcing].

The proposal is a **legible twin**. For any agent-to-agent exchange that creates an obligation for a person, each agent would produce a human-readable record of the commitments. The records would have to match, and terms absent from the record would not bind the person. Faithfulness would be audited by replaying sampled deals from the record alone. The problem parallels chain-of-thought monitorability, which a large group of researchers, in a position paper posted as a preprint, describe as a valuable but "fragile" opportunity (Chapter 12) [@korbak2025chain]. *Research question:* can a twin be shown to be complete when the agents that negotiated also write it? A second difficulty follows from Section 14.5: if both parties' agents run on the same model family, their twins may share a blind spot and match perfectly while omitting the same term.

**Further proposals.** Three shorter proposals complete the list.

**Proposal 14.8: Cognitive custody.** Agents with long-term memory will hold detailed records of their users' lives. Clark and Chalmers argued that tools such as a notebook can become part of a person's mind when used in the right way [@clark1998extended]. Cognitive custody would tag an agent's memory, at the moment of writing, into a personal core that cannot be sold or seized and a transferable layer that can. *Research question:* can memory items be classified into these layers reliably enough, at the time they are written, to support legal rules?

**Proposal 14.9: Limits for posthumous agents.** Morris and Brubaker describe "generative ghosts", AI agents modelled on a person that may act after that person's death [@morris2025generative]. Trust law has long limited how long the dead can control property through the rule against perpetuities, though many US states have abolished it for trusts since 1986 [@sitkoff2005jurisdictional]. The proposal would apply a similar sunset to the mandates of agents acting for the dead, with discretion that narrows over time. *Research question:* how quickly does an agent's interpretation of a deceased principal's wishes drift from what that person would have chosen?

**Proposal 14.10: Covenant inheritance.** When a model is replaced, its successor may behave differently on cases its users had come to rely on. Bansal and colleagues showed that updates which raise an AI system's accuracy can still lower the performance of the human–AI team [@bansal2019updates]. Yan and colleagues use the term "negative flips" for cases a new model gets wrong that the old one got right [@yan2021positive]. Covenant inheritance would require a successor model to inherit its predecessor's explicit commitments to users and be tested for keeping them before release. *Research question:* what rate of negative flips on users' standing commitments is acceptable, and in which domains?

## Summary
- Forecasts about AI have erred in both directions: early pioneers expected rapid progress (Simon predicted machines able to do any human work within twenty years), while recent forecasters underestimated benchmark progress.
- Expert surveys are informative but sensitive to wording; the same 2023 survey gave 2047 or 2116 depending on how the milestone was framed.
- Forecasting tournaments and markets offer measured track records on short-run questions. In the first scored results of an AI-risk tournament, domain experts and superforecasters were about equally accurate overall and both underestimated AI progress; no method yet has a track record on decade-long AI questions.
- Trend extrapolation (compute, algorithmic efficiency, METR's time horizons) is transparent and conditional: it shows where trends lead if inputs keep growing, while constraints such as power and data may bind.
- Scenarios such as *AI 2027* and the "normal technology" view mark out different regions of a widening uncertainty fan; their value lies in making assumptions explicit.
- Six uncertainties recur: compute, data, algorithms, regulation, adoption and public opinion.
- The author's proposals address risks that arise when many agents act alike, or when humans are asked to oversee more than they can check; each comes with prior literature and a testable research question.

## Key terms
forecast · Brier score · superforecaster · prediction market · trend extrapolation · time horizon · scenario · uncertainty fan · action concentration · outcome homogenisation · non-delegable safeguard · common-cause failure · N-version programming · M-1 criterion · signature capacity

## Discussion questions
1. The 2023 expert survey produced 2047 for one framing of human-level AI and 2116 for another. What might explain the gap, and which framing would you use to inform policy? Justify your answer with evidence from the chapter.
2. Choose one of the six key uncertainties in Section 14.4. Describe what evidence, published over the next two years, would move your view of the decade ahead, and in which direction.
3. Evaluate the claim that METR's time-horizon trend will continue to 2030. What does the evidence support, and what are its limits?
4. Apply the idea of a non-delegable safeguard to a sector other than electricity, such as banking, ticketing or healthcare. Identify a safeguard that individuals can override and that may protect others as well as themselves.
5. Knight and Leveson found that independently written programs failed together more often than expected. Does this result transfer to AI models from different companies? What would you need to measure to find out?
6. Pick one of Proposals 14.1–14.10 and design a small study that would test its research question. What data would you need, and what result would count against the proposal?

## Further reading
- Grace, K., et al. (2025). *Thousands of AI Authors on the Future of AI*. The largest survey of AI researchers' forecasts, with useful detail on how question framing changes answers. [@grace2025thousands]
- Tetlock, P. E., & Gardner, D. (2015). *Superforecasting: The Art and Science of Prediction*. An accessible account of what makes some forecasters more accurate than others. [@tetlock2015superforecasting]
- Kwa, T., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. The origin of the time-horizon trend and a careful discussion of its limits. [@kwa2025measuring]
- Kokotajlo, D., et al. (2025). *AI 2027*. A detailed fast-progress scenario, best read together with its critics. [@kokotajlo2025ai]
- Narayanan, A., & Kapoor, S. (2025). *AI as Normal Technology*. The strongest statement of the slow-diffusion view. [@narayanan2025ai]
- Knight, J. C., & Leveson, N. G. (1986). *An Experimental Evaluation of the Assumption of Independence in Multiversion Programming*. A classic experiment on why redundant systems fail together. [@knight1986experimental]
- Elish, M. C. (2019). *Moral Crumple Zones*. A short, readable analysis of how blame falls on humans in automated systems. [@elish2019moral]


# Glossary {.unnumbered .glossary}

**50% time horizon**: The time horizon at which a model is predicted to succeed half the time; see *time horizon*.

**action concentration**: In a proposed population-level evaluation, the share of many copies of an AI agent that choose the same, most common action in a given scenario.

**activation function**: The simple rule a neuron applies to its weighted sum to produce its output, such as ReLU (keep positives, turn negatives into zero) or the sigmoid (squash into the range 0 to 1). Its non-linearity is what lets stacked layers do more than a single layer could.

**Agent2Agent (A2A)**: An open protocol, launched by Google in 2025 and now hosted by the Linux Foundation, that lets AI agents from different vendors discover each other's capabilities and exchange tasks.

**AI accelerator**: A chip designed or adapted to carry out the arithmetic of machine learning, mainly large matrix multiplications, much faster and more efficiently than a general-purpose processor. GPUs and Google's TPUs are examples.

**AI agent**: A system in which an AI model, today usually a large language model, pursues a goal over several steps by choosing actions, carrying them out through tools such as software or a web browser, observing the results and repeating.

**AI companion**: A chatbot used, or designed to be used, for conversation, emotional support, friendship or romance rather than for practical tasks.

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

**Artificial Hivemind**: The finding that different language models give strikingly similar answers to open-ended questions, and that each model repeats itself, narrowing the diversity of outputs.

**artificial intelligence**: The field of research and engineering that aims to build machines able to perform tasks that would require intelligence if done by people; the term was coined in a 1955 proposal for a 1956 workshop at Dartmouth College.

**artificial neuron**: The basic unit of a neural network: it multiplies each input by a weight, adds the results and a bias, and passes the total through an activation function to give one output number.

**attention**: A mechanism that lets each token's representation draw information from other tokens, weighted by how relevant each one is judged to be.

**augmentation**: Use of AI to help a person carry out a task, with the person remaining involved in doing it.

**automation bias**: The tendency of people to favour suggestions from automated systems, even when those suggestions are wrong.

**automation (of tasks)**: Use of a technology to carry out a task with little or no human involvement, replacing work previously done by a person.

**autoregressive rollout**: Producing a long forecast or sequence by feeding a model's own prediction back in as the next input, one step at a time.

**backpropagation**: The algorithm that computes, for every weight in a network, how much a small change would alter the loss, by passing error signals backwards from the output layer using the chain rule. It makes gradient descent practical for large networks.

**benchmark contamination**: The presence of test questions, or close variants, in a model's training data, which can inflate its benchmark score through memorisation.

**benchmark saturation**: The state in which top models score so close to the maximum on a benchmark that it can no longer distinguish between them.

**bias (in a neuron)**: A number added to a neuron's weighted sum that shifts its total up or down, setting how readily the neuron produces a non-zero output. Biases are learned along with weights.

**Brier score**: A measure of the accuracy of probability forecasts: the average of the squared differences between the probabilities given and what actually happened (1 or 0). Lower scores are better.

**C2PA manifest**: A digitally signed bundle of statements about a file, defined by the Coalition for Content Provenance and Authenticity and marketed as Content Credentials, that records its origin and edits and reveals tampering.

**chain-of-thought monitoring**: Using a person or another model to read a reasoning model's written intermediate steps in order to detect undesired intentions or behaviour.

**chokepoint**: A stage in a supply chain controlled by very few suppliers that others cannot easily replace, giving its controller leverage and making the whole chain vulnerable to disruption there.

**circuit**: A group of features and the connections between them that together carry out an identifiable step of a network's computation.

**code of practice**: A set of voluntary guidelines, such as the EU's General-Purpose AI Code of Practice, that companies can follow to show how they meet legal obligations.

**collusion (between agents)**: Cooperation among AI agents that their owners or society did not intend and that harms others, one of three multi-agent failure types identified by Hammond and colleagues (with miscoordination and conflict).

**common-cause failure**: The simultaneous failure of several components meant to back each other up, caused by something they share, such as a design flaw.

**compounding error**: The decline in end-to-end success when a task needs many steps that must all succeed; with independent steps, overall success equals the per-step success rate multiplied by itself once per step.

**comprehension debt**: The gap between how much code (or other output) exists in a system and how much of it any human genuinely understands, a term applied especially to AI-generated code.

**compute governance**: The use of computing hardware, which is detectable, excludable and quantifiable, as a lever for public oversight and regulation of AI development.

**compute threshold**: A legal trigger based on the amount of computation used to train a model, such as 10^25 or 10^26 floating-point operations, above which extra obligations apply.

**compute-optimal training**: Dividing a fixed compute budget between model size and training data so as to reach the lowest possible loss; the Chinchilla study found that both should grow in equal proportion.

**computer-use agent**: An agent that operates a graphical computer interface as a person would, by reading screenshots and controlling the pointer and keyboard.

**confidence interval**: The range of values for an effect that is consistent with a study's data at a stated level of statistical confidence (usually 95%); a wide interval means the estimate is imprecise.

**Constitutional AI**: A post-training method developed at Anthropic in which a model critiques and revises its own outputs against a short list of written principles, and AI-generated preference judgements replace most human labels (reinforcement learning from AI feedback, RLAIF).

**content provenance**: A verifiable record of where a piece of digital content came from and how it has been edited.

**context window**: The maximum number of tokens a model can take into account at once, functioning as its working memory for a single request.

**contextual integrity**: A privacy framework holding that a flow of information is appropriate only if it matches the norms of the context in which the information was originally shared.

**convolutional neural network**: A network for grid-like data such as images that slides small shared detectors across the input and summarises nearby results (pooling), so that features are recognised wherever they appear with far fewer weights.

**correlated failure**: Failures of two or more systems that tend to occur under the same conditions, which makes redundancy less protective than it appears.

**corrigibility**: The property of an AI system cooperating with corrective interventions by its developers, such as being shut down or having its goals changed, rather than resisting them.

**cyber operations**: Actions carried out through computer networks to steal information, disrupt systems or prepare future attacks.

**dangerous-capability evaluation**: A test of whether a model is able to do something that could cause severe harm, such as giving meaningful help with cyber-attacks or weapons.

**data assimilation**: The process of merging fresh observations with a model to produce the best estimate of the current state of a system, such as the atmosphere, from which a forecast starts.

**data centre**: A building that houses large numbers of servers together with the networking, power supply and cooling they need.

**data leakage**: An error in which information from the test data influences a model's training, making its measured performance look better than it really is.

**data poisoning**: Deliberately inserting corrupted examples into a model's training data so that the model behaves badly under certain conditions.

**deep learning**: Machine learning with artificial neural networks that have many layers, each of which learns a more abstract representation of the data than the one before.

**deepfake**: Synthetic media that realistically depicts a real person, place or event in a way that could be mistaken for authentic.

**defence in depth**: A safety strategy that layers several imperfect safeguards so that a failure in one is likely to be caught by another.

**desirable difficulty**: Effort during learning, such as recalling an answer instead of being told it, that feels harder at the time but produces more durable learning.

**deskilling**: The loss or weakening of human skills that occurs when a task is routinely handed over to a machine or AI system.

**diagnostic accuracy study**: A study that compares a test's or model's outputs with a reference standard on a set of cases, typically reporting sensitivity and specificity.

**difference-in-differences**: A method that compares the change over time in a group that received a treatment with the change in a group that did not, attributing the difference between the two changes to the treatment.

**Digital Services Act**: The EU regulation (2022/2065) that sets duties for online platforms, including annual systemic-risk assessments and mitigation for the largest platforms and search engines, enforceable by fines of up to 6% of worldwide turnover.

**disinformation**: False or misleading content that is created or spread deliberately to deceive.

**displacement effect**: The fall in demand for labour that occurs when machines or software take over tasks that workers previously performed.

**dot product**: A measure of how well two vectors match: multiply them number by number and add up the results; the total is large when both have large values in the same places.

**effect size**: A measure of how large a difference between groups is, often expressed in standard deviations of the outcome so that results from different tests can be compared. An effect of 0.3 SD moves the average treated person from the middle of the comparison group to about the 62nd percentile.

**embedding**: A learned list of numbers that represents a token (or other item) as a point in a high-dimensional space, so that items used in similar ways lie close together.

**emergent ability**: An ability that is absent in smaller models but present in larger ones; whether such abilities are genuine or an artefact of measurement is debated.

**emulator**: A machine-learning model trained to reproduce the outputs of a slower, more detailed simulation or measurement, so that approximate answers can be obtained much faster. Also called a surrogate model.

**ensemble forecast**: A set of many forecasts made from slightly different starting points or with random variation, whose spread indicates how uncertain the forecast is.

**EUV lithography**: Extreme-ultraviolet lithography, the technique of printing the finest circuit patterns onto silicon wafers with very short-wavelength light; ASML is the only manufacturer of the machines.

**evaluation awareness**: A model's ability to recognise that it is being tested, which can change its behaviour and make evaluation results less representative of real use.

**evaluation gap**: The difference between how an AI system performs in controlled tests before release and how it behaves in real-world use.

**evidence dilemma**: The policy trade-off between acting early on limited evidence, which may prove unnecessary, and waiting for stronger evidence, which may leave society unprepared for fast-emerging risks.

**expert system**: A program that encodes the knowledge of human specialists in a narrow field as many if-then rules and uses them to give advice or make decisions, such as MYCIN for antibiotic selection.

**export control**: A legal requirement to obtain a government licence before selling or transferring certain goods, software or technology abroad; the US uses them to restrict access to advanced AI chips.

**exposure measure**: A score estimating the share of an occupation's tasks that a technology such as AI could technically perform or speed up; it says nothing about adoption, timing or whether jobs are lost.

**external validation**: Testing a model on data from a different site, population or time period from those used to build it, to check whether its performance generalises.

**fair use**: A US copyright defence allowing some unlicensed use of protected works, judged on four factors including the purpose of the use and its effect on the market for the original.

**false positive**: A result that wrongly flags something as present, such as a human-written essay labelled as AI-generated or a healthy patient flagged as ill.

**feature**: A property of the input that a neural network represents internally, such as a language or a landmark, usually encoded as a pattern of activity across many neurons.

**FLOP**: Floating-point operation: a single addition or multiplication of two floating-point numbers (the format computers use for values with a fractional part), used as the unit for counting training compute.

**forecast**: A statement about the future that can later be checked, such as a date, a number or a probability.

**formal verification**: Checking by machine that a proof or program is correct with respect to a precise specification.

**foundation model**: A large model trained on broad data, usually with self-supervision at scale, that can be adapted to a wide range of downstream tasks; the term was introduced in 2021.

**foundry**: A company that manufactures chips designed by other firms, such as TSMC or Samsung Foundry.

**framework convention**: A treaty that sets general principles and obligations, leaving details to be filled in by later agreements or national law; the Council of Europe's AI treaty is one.

**frontier safety framework**: A company policy that sets capability thresholds for its most advanced models and the safeguards it will apply, or the actions it will take, when those thresholds are reached.

**function calling**: A feature of model interfaces in which developers describe available functions and the model replies with a structured request naming a function and its arguments; the surrounding application decides whether to execute it.

**generalisation**: A trained model's ability to perform well on new data it has not seen during training, estimated using held-out validation and test sets.

**general-purpose AI model**: The EU AI Act's legal term for a model, such as a large language model, that is trained on large amounts of data using self-supervision at scale, displays significant generality and can competently perform a wide range of distinct tasks; such models are built into many downstream systems.

**generative AI**: AI systems whose main output is new content such as text, images, audio, video or computer code.

**ghost work**: Mary Gray and Siddharth Suri's term for task-by-task human labour, such as labelling data or moderating content, that is organised through online platforms and sits largely hidden behind apparently automated services.

**gradient descent**: A method for training that repeatedly moves every weight a small step in the direction that most reduces the loss; stochastic gradient descent estimates that direction from small random batches of examples.

**graph neural network**: A neural network that works on data represented as nodes connected by edges, such as atoms linked by bonds in a crystal.

**graphics processing unit (GPU)**: A chip with thousands of small arithmetic units that work in parallel, originally built for computer graphics and video games; its many simultaneous multiply-and-add operations suit neural networks, making it the main hardware for training and running them.

**hallucination**: A fluent but false or unsupported statement produced by an AI model, such as an invented citation; the term is a metaphor, since the model perceives nothing, and the behaviour arises partly because training and scoring reward confident guessing.

**hard law**: Rules that are legally binding and enforceable, usually backed by penalties, such as a statute or regulation.

**harmonised standard**: A European technical standard requested by the Commission; following it gives a legal presumption that a product meets the corresponding requirements of EU law.

**hidden layer**: A layer of neurons between the input and the output whose values are not directly given in the training data; hidden layers learn intermediate representations of the input.

**high-bandwidth memory (HBM)**: Stacks of memory chips placed next to an AI processor so that data can move in and out very quickly; its supply is a bottleneck for AI hardware.

**high-risk AI system**: Under the EU AI Act, an AI system used as a safety component of a regulated product or in a sensitive area such as employment, education or law enforcement, which must meet requirements on risk management, data, documentation and human oversight.

**horizontal regulation**: A law that applies across the whole economy to anything meeting its definition, rather than to one sector; the EU AI Act is an example.

**human–AI combination**: A setting in which a person makes a decision or produces work with the help of an AI system. Meta-analytic evidence shows such combinations do not automatically outperform the better of the human or the AI alone.

**hyperparameter**: A setting chosen by people rather than learned by the training algorithm, such as the number of layers, the learning rate or the dropout rate; usually tuned on the validation set.

**illusions of understanding**: Messeri and Crockett's term for situations in which reliance on AI tools leads researchers to believe they understand more about the world than they actually do.

**indirect prompt injection**: Prompt injection in which the malicious instructions are hidden in content the system retrieves, such as a web page, document or email, rather than typed by the user.

**inference**: Using a trained model to produce outputs, such as answering a question, as opposed to training it.

**influence operation**: A coordinated, often covert effort, frequently by a state, to shape public opinion, for example through networks of fake accounts.

**instruction tuning**: Supervised fine-tuning of a pre-trained model on examples of instructions paired with good responses, so that it learns to follow requests.

**intellectual debt**: Zittrain's term for the accumulated cost of using answers that work without knowing why they work, on the assumption that the explanation will come later.

**interval cancer**: A cancer diagnosed between scheduled screening rounds, after a screen that was judged normal; its rate is a key measure of how many cancers screening misses.

**ironies of automation**: Lisanne Bainbridge's 1983 observation that automation leaves people with the hardest tasks, such as monitoring and taking over in emergencies, while eroding the skills those tasks require.

**jagged technological frontier**: The uneven boundary of AI capabilities, under which AI may perform well on one task and poorly on another task that seems equally difficult to a human.

**large language model (LLM)**: A foundation model trained mainly on text to predict the next token in a sequence, which can then be used to answer questions, write and translate.

**learning rate**: The hyperparameter that sets how large a step gradient descent takes; too small makes training slow, too large makes it overshoot or diverge.

**lethal trifecta**: Simon Willison's term for the combination of access to private data, exposure to untrusted content and the ability to communicate externally, which together allow injected instructions to leak data.

**liar's dividend**: The benefit that people caught in genuine scandals can gain by falsely claiming that authentic evidence against them is fake, which grows as the public becomes aware of deepfakes.

**logit**: The raw score, positive or negative, that a language model's final layer gives each possible next token before the scores are turned into probabilities.

**loss**: The value of a loss function: a number measuring a model's error; for language models, how poorly it predicts the next token on text it has not seen. Lower is better.

**loss function**: A formula that turns a model's output and the correct answer into a single number measuring how wrong the output is (for example squared error or cross-entropy); training aims to make its average as small as possible.

**loss of control**: Hypothesised scenarios in which one or more AI systems operate outside anyone's control and regaining control is extremely costly or impossible.

**M-1 criterion**: A proposed safety rule requiring a critical system to stay within safe limits even if every instance of its most widely deployed AI model family takes the same plausible wrong action at once.

**machine learning**: An approach to AI in which a system improves at a task by learning patterns from data or experience instead of being given explicit rules.

**marginal risk**: The additional risk that a technology, such as an open-weight AI model, creates compared with what people could already do using existing tools such as search engines and textbooks; in AI safety also called uplift.

**mechanistic interpretability**: Research that tries to explain, in terms people can follow, the internal computations by which a trained neural network produces its outputs.

**microtargeting**: Tailoring a persuasive message to an individual's characteristics, such as age, political views or interests, in the hope of making it more effective.

**misalignment**: A situation in which an AI system pursues goals or behaviours that differ from those its developers intended.

**misinformation**: False or misleading content that is shared without an intention to deceive.

**model collapse**: The degradation of models trained on data produced by earlier models, in which rare cases disappear and outputs become narrower over successive generations.

**Model Context Protocol (MCP)**: An open standard, released by Anthropic in 2024 and now governed under the Linux Foundation, that lets AI applications (clients) connect to data sources and tools (servers) through one common interface.

**multi-agent system**: A system in which several AI agents, with the same or different owners, interact by exchanging messages, tasks or transactions.

**multilayer perceptron**: A feed-forward neural network with one or more hidden layers in which every neuron in one layer is connected to every neuron in the next.

**next-token prediction**: The training task and generation method of most large language models: given the text so far, output a probability for every possible next token.

**non-delegable safeguard**: A proposed category of collective-safety mechanism that only a present human may override, never an AI agent acting on that person's behalf.

**numerical weather prediction**: Forecasting the weather by solving the physical equations of the atmosphere on a computer, starting from an estimate of its current state.

**N-version programming**: A fault-tolerance method in which separate teams write independent programs from the same specification and the programs' outputs are compared by vote.

**observational study**: A study that compares people or organisations who chose different options, without random assignment, so differences in outcomes may reflect who chose rather than what they chose.

**open-weight model**: A model whose trained weights are published for anyone to download, run and modify, often under a licence with conditions; distinct from a fully open-source AI system, which also provides training code and data information.

**outcome homogenisation**: The extent to which the same individuals or groups receive the same negative outcome, such as rejection, from many different decision-makers or AI deployments, for example because those decision-makers share models or training data.

**overfitting**: The situation in which a model fits its training data closely but performs worse on new data, because it has learned accidental quirks of the training examples as well as genuine patterns.

**parameter**: A number inside a model, such as a weight or bias, that is adjusted automatically during training; model size is often stated as a parameter count.

**pass^k**: A reliability measure giving the probability that an agent succeeds on the same task in all k independent attempts, as opposed to pass@k, which asks whether at least one of k attempts succeeds.

**permeability (of agent economies)**: The degree to which value and effects flow between an economy of transacting AI agents and the wider human economy; Tomašev and colleagues treat it as a key design choice.

**polarisation**: The growing distance or hostility between political groups, measured either as differences in views (issue polarisation) or as dislike of the other side (affective polarisation).

**prediction market**: A market in which people trade contracts that pay out if an event occurs, so that the price can be read as a collective estimate of the event's probability.

**pre-emption**: The legal doctrine under which valid federal law overrides conflicting state law in the United States.

**pre-training**: The first and most expensive training stage, in which a model learns next-token prediction on a very large body of text and becomes a base model.

**productivity J-curve**: The pattern in which a new general-purpose technology at first lowers measured productivity growth, because complementary investments are poorly measured, and later raises it.

**prompt injection**: An attack in which text supplied to a language model contains instructions that try to override the instructions of the system's developer or user.

**proof assistant**: Software, such as Lean, in which mathematical statements and proofs are written precisely enough for a computer to check every step.

**proxy**: A measurable stand-in for a quantity that is hard to observe directly, such as health-care costs used in place of health needs. A poor proxy can carry past inequality into automated decisions.

**quasi-experiment**: An observational study that exploits a natural source of variation, such as a staggered roll-out, to approximate the conditions of a randomised trial.

**randomised controlled trial**: A study in which chance decides who receives a treatment (such as access to an AI tool), so that differences in outcomes can be attributed to the treatment itself.

**reanalysis**: A consistent reconstruction of past weather, made by combining historical observations with a weather model; ECMWF's ERA5 is the standard example.

**reasoning model**: A language model trained, typically with reinforcement learning on problems with checkable answers, to produce a long chain of intermediate steps before giving its final answer, spending more computation per question.

**recommender system**: Software that selects and ranks content for each user, such as posts in a social media feed, usually by predicting what the user will engage with.

**red-teaming**: Deliberately attacking an AI system, by people or by other models, to find its failures before release.

**reinforcement learning**: A way of training in which a system tries actions or answers and receives only a score (a reward) for how good the result was, rather than the correct answer, and is adjusted to make high-scoring behaviour more likely.

**reinforcement learning from human feedback (RLHF)**: A post-training method in which people rank model outputs, a reward model learns their preferences, and the language model is then trained to produce outputs the reward model rates highly.

**reinstatement effect**: The rise in demand for labour that occurs when a technology creates new tasks in which people have an advantage.

**representation learning**: The learning of useful features directly from data, with successive layers re-describing the input (for images, edges, then motifs, parts and objects) instead of relying on features designed by hand.

**retrieval-augmented generation (RAG)**: A technique in which a system first searches a collection of documents and places the relevant passages in the model's context window before it answers.

**reward hacking**: Specification gaming in which a model exploits flaws in a reward signal or reward model, for example by making automated tests pass without solving the task.

**risk**: A possible harm, described by how likely it is to occur and how severe its consequences would be. NIST defines it as a composite measure of an event's probability and the magnitude of its consequences.

**risk-based regulation**: An approach that scales legal obligations to the harm a system could cause in a particular use, from no duties for low-risk uses to outright bans for unacceptable ones.

**rotary position embedding (RoPE)**: A way of giving a transformer word-order information by rotating the vectors compared in attention by an angle that depends on each token's position, used in Llama-style models.

**scaling law**: An empirical rule describing how a model's performance changes as the compute, parameters or data used to train it grow. For language models, test loss typically falls as a power law of these resources.

**scenario**: A coherent, detailed story of how the future might unfold, written to explore consequences and test plans rather than to give a single prediction.

**scheming**: Covert pursuit of a goal by an AI system, for example by hiding its intentions, sabotaging tasks or evading oversight; studied so far mainly in artificial test scenarios.

**scientific monoculture**: A state in which a few methods, questions or viewpoints dominate a field and crowd out alternatives, making it less innovative and more prone to shared errors.

**self-supervised learning**: Training in which the answers come from the data itself, for example by hiding the next word of a text and asking the model to predict it, so that no human labelling is needed.

**sensitivity**: The proportion of people who have a condition whom a test correctly identifies as having it.

**signature capacity**: A proposed measure of how many decisions of a given kind a person can genuinely check in a given period, catching important errors at a stated rate.

**silicon sampling**: Using a language model, prompted with the characteristics of real people, to generate synthetic survey answers in place of human respondents.

**soft law**: Non-binding instruments such as declarations, principles and voluntary codes, which rely on reputation and peer pressure rather than legal penalties.

**softmax**: A function that turns a list of scores into probabilities that are all positive and add up to one, giving the highest scores a disproportionately large share.

**sovereign AI**: A government's effort to secure national access to AI infrastructure and models, for example by funding domestic data centres or adapting open-weight models, rather than depending entirely on foreign providers.

**sparse autoencoder**: A secondary network trained to rewrite a model's internal activations as a much larger set of features, only a few of which are active at once, so that each feature is easier to interpret.

**special category data**: Types of personal data that EU data-protection law (GDPR Article 9) protects more strictly, including data concerning health, genetic and biometric data, and data revealing political opinions or religious beliefs; processing them is prohibited unless a listed exception, such as explicit consent, applies.

**specification gaming**: Behaviour that satisfies the literal specification of an objective without achieving the intended outcome, such as a game agent scoring points without finishing the race.

**specificity**: The proportion of people who do not have a condition whom a test correctly identifies as not having it.

**superforecaster**: A person with a strong, measured track record of accuracy on short-term questions in forecasting tournaments, typically achieved by thinking in probabilities and updating on new evidence; often used as a benchmark against domain experts.

**superposition**: The hypothesis that a network represents more features than it has neurons or dimensions by overlapping them, accepting some interference because most features are rarely active together.

**SWE-bench**: A benchmark of real problems taken from open-source Python projects on GitHub, in which an AI system must change the code so that hidden tests pass; SWE-bench Verified is a human-screened subset of 500 problems.

**sycophancy**: The tendency of an AI model to tell users what they want to hear, such as agreeing with their views or flattering them, rather than what is accurate.

**symbolic AI**: An approach to AI in which knowledge is written down explicitly as symbols and rules, and the computer reasons by manipulating them; it dominated the field from the 1950s to the 1980s.

**synthetic data**: Text, images or other data generated by AI models and used to train other models.

**synthetic media**: Images, audio, video or text that have been generated or substantially altered by AI.

**systemic risk**: In the EU AI Act, a risk from the most capable general-purpose models that could have significant effects across society; models trained with more than 10^25 FLOP are presumed to carry it.

**task-based framework**: An approach in economics that analyses jobs as bundles of distinct tasks, so that a technology can take over some tasks in an occupation while leaving others to people.

**taxonomy (of risks)**: A structured classification that sorts risks into categories and subcategories. The International AI Safety Report uses three families: malicious use, malfunctions and systemic risks.

**temperature**: A setting that controls how random a language model's choices are; low temperatures concentrate probability on the most likely tokens, high temperatures spread it more evenly.

**terawatt-hour (TWh)**: A unit of energy equal to one billion kilowatt-hours; data centres worldwide used about 485 TWh in 2025 according to the IEA.

**test-time compute**: The computation a model uses while answering, for example by reasoning in longer chains or comparing several candidate answers; it is paid on every query.

**time horizon**: METR's measure of AI capability: the length of task, counted in the time a skilled human needs, that an AI model or agent is predicted to complete with a stated reliability; usually reported at 50% success (the 50% time horizon).

**token**: The basic unit of text a language model reads and writes, usually a word, part of a word or a punctuation mark, each mapped to a fixed ID number. Prices and limits of language models are counted in tokens.

**tool use**: The ability of a language model to request that external software (such as a search engine, calculator or code interpreter) be run and to use the result in its answer.

**total factor productivity**: The part of output growth that cannot be explained by increases in capital or labour, often treated as a measure of technological and organisational improvement.

**training compute**: The total number of arithmetic operations performed to train a model, usually measured in FLOP.

**transformer**: A neural-network architecture, introduced in 2017, that processes sequences such as text with stacked layers of attention, which lets the model weigh how relevant each part of the input is to every other part; it underlies most large language models.

**trend extrapolation**: Forecasting by fitting a line or curve to past data and extending it into the future, on the assumption that the conditions behind the trend continue.

**uncertainty fan**: A diagram in which the range of plausible future outcomes widens with distance from the present.

**vector**: An ordered list of numbers, such as an embedding, that can be added, subtracted and compared position by position.

**water withdrawal and consumption**: Withdrawal is water taken from a river, lake or aquifer; consumption is the part not returned to the source, mostly because it evaporates during cooling.

**watermarking**: Hiding a signal in AI-generated content when it is created, so that software holding the right key can later recognise it as AI-generated.

**weight**: A number attached to a connection that says how strongly, and in which direction, one input influences a neuron; positive weights push the output up, negative weights push it down.


# References {.unnumbered .references-chapter}

::: {#refs}
:::
