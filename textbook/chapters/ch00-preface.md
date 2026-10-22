# Preface {.unnumbered}

This book is an introduction to artificial intelligence as it stands in October 2026: how the technology works, where it is heading, what it is already doing to work, science, media and public life, and how societies are trying to govern it. It is written for a first university course on AI and society, open to students from any discipline. It assumes no programming and no mathematics beyond school level. Students with a technical background will find the main text quick going and can use the "Going deeper" boxes and the further reading for more.

The book has two aims. The first is understanding: by the end, a reader should be able to explain in plain words how a neural network learns, what a large language model does when it answers a question, and why more computing power has so reliably produced more capable systems. The second is judgement. Public discussion of AI swings between promise and alarm, and much of it rests on anecdotes, company announcements and forecasts presented as facts. A student who has worked through this book should be able to ask of any claim about AI: what kind of evidence supports this, how strong is it, and what would change my mind?

## How the book is organised

The fourteen chapters fall into five parts.

**Part I, How AI Works (Chapters 1–4),** builds the technical foundation. Chapter 1 defines the main terms and traces the history of the field from the 1950s. Chapter 2 explains neural networks from a single artificial neuron to deep learning, using small worked examples. Chapter 3 does the same for large language models: tokens, embeddings, attention, pre-training and the later stages of training that turn a text predictor into an assistant. Chapter 4 examines scaling, the empirical regularity that has driven most recent progress, and asks where its limits lie.

**Part II, The Frontier (Chapters 5–7),** follows the main technology trends. Chapter 5 covers the move from chatbots to agents that use tools and act over many steps. Chapter 6 looks at AI in science, mathematics and engineering, where some of the best-documented successes are found. Chapter 7 turns to the physical side of AI: chips, supply chains, data centres, electricity, and the debate over openly released models.

**Part III, Society and Economy (Chapters 8–10),** examines effects on people. Chapter 8 reviews the evidence on work, productivity and the labour market. Chapter 9 covers information, media and democracy, including synthetic media, persuasion and content provenance. Chapter 10 looks at education, health and everyday life.

**Part IV, Risk, Safety and Governance (Chapters 11–13),** asks what can go wrong and what is being done about it. Chapter 11 sets out a structured view of risks, from present harms to contested long-term concerns. Chapter 12 explains the technical work on making AI systems safe: alignment training, interpretability and evaluation. Chapter 13 compares how the European Union, the United States, China, the United Kingdom and international bodies regulate AI.

**Part V, The Decade Ahead (Chapter 14),** closes the book with the methods people use to forecast AI, the main scenarios for the next ten years, and a set of open problems. It also includes a small number of proposals, clearly labelled as the author's own, for students to criticise.

Every chapter follows the same pattern. It opens with learning objectives and a documented case that shows why the topic matters. Numbered sections carry the argument. Four kinds of box interrupt the text: **Key concept** boxes define an idea precisely; **Case study** boxes examine a real event in detail; **Debate** boxes set out a contested question with the best evidence on each side and say what would settle it; and **Going deeper** boxes give technical detail, including the few equations in the book, which readers may skip without losing the thread. Each chapter ends with a summary, a list of key terms (all defined in the glossary at the back), discussion questions and annotated further reading.

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
