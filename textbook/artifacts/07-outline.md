# Outline: Understanding AI: Technology, Trends and the Decade Ahead

Fourteen chapters in five parts plus front and back matter. Each chapter is 5,500–6,500 words of body text, excluding boxes, the end-of-chapter apparatus and references. Every chapter has a job no other chapter does. The cross-references listed are the only places a topic may be treated in depth; elsewhere, refer to it in one sentence.

## Front matter
- **Preface** (~1,200 words; written by the orchestrator): who the book is for, how to use it in a course (week plan), how evidence is labelled, and what "as of October 2026" means.

## Part I: How AI Works

### Chapter 1: What We Mean by "AI": Definitions and a Short History
- **Job:** a shared vocabulary and the historical arc, so that later trends make sense.
- **Must cover:**
  - definitions (AI, machine learning, deep learning, generative AI, foundation models, agents), with OECD and EU AI Act definitions;
  - symbolic AI and expert systems;
  - the AI winters;
  - statistical machine learning;
  - the deep learning breakthrough (ImageNet / AlexNet 2012);
  - AlphaGo (2016);
  - the transformer (2017);
  - GPT-3 (2020);
  - ChatGPT (Nov 2022) and adoption speed;
  - reasoning models (2024–25);
  - agents (2025–26);
  - why "AI" is a moving target (the "AI effect").
- **Anchors:**
  - Turing 1950;
  - McCarthy et al. 1955 (Dartmouth proposal);
  - Krizhevsky, Sutskever & Hinton 2012;
  - Silver et al. 2016;
  - Vaswani et al. 2017;
  - Brown et al. 2020;
  - OECD AI definition (2023/2024);
  - Stanford AI Index (latest).
- **Figures:**
  - a timeline of milestones, 1950–2026;
  - a nested diagram (AI ⊃ ML ⊃ deep learning ⊃ generative models / LLMs).

### Chapter 2: How Neural Networks Learn
- **Job:** an intuitive, correct explanation of neural networks with no maths beyond school level.
- **Must cover:**
  - an artificial neuron (weighted sum, activation);
  - layers and the multilayer perceptron;
  - learning as error reduction;
  - loss functions;
  - gradient descent (the hill/valley intuition);
  - backpropagation in words;
  - training, validation and test data;
  - overfitting and generalisation;
  - parameters vs. hyperparameters;
  - representation learning (features learned in layers);
  - convolutional networks briefly;
  - GPUs and why parallel hardware matters;
  - what networks are bad at;
  - the biological analogy and its limits.
  - **Going deeper box:** the chain rule and backpropagation in one page.
- **Anchors:**
  - McCulloch & Pitts 1943;
  - Rosenblatt 1958;
  - Rumelhart, Hinton & Williams 1986;
  - LeCun et al. 1998 / LeCun, Bengio & Hinton 2015 (Nature review);
  - Goodfellow, Bengio & Courville 2016 (textbook).
- **Figures:**
  - a single neuron;
  - a small network with layers;
  - a gradient-descent valley;
  - an overfitting curve (training vs. validation error).

### Chapter 3: How Large Language Models Work
- **Job:** the core technical chapter on LLMs: digestible, accurate and current.
- **Must cover:**
  - tokens and tokenisation (worked example);
  - embeddings (words as points in space);
  - next-token prediction;
  - attention and the transformer, explained intuitively;
  - context windows;
  - pre-training on web-scale text;
  - sampling and temperature;
  - post-training: instruction tuning, RLHF, Constitutional AI / RLAIF;
  - why LLMs "hallucinate";
  - multimodal models;
  - reasoning / "thinking" models and test-time compute (o1 2024, DeepSeek-R1 2025);
  - retrieval-augmented generation;
  - open- vs. closed-weight models (brief; full treatment in ch. 7);
  - what we do and don't understand (pointer to interpretability, ch. 12).
- **Anchors:**
  - Vaswani et al. 2017;
  - Radford et al. 2018/2019;
  - Brown et al. 2020;
  - Ouyang et al. 2022 (InstructGPT);
  - Bai et al. 2022 (Constitutional AI);
  - Mikolov et al. 2013;
  - Lewis et al. 2020 (RAG);
  - OpenAI 2024 (o1 system card);
  - DeepSeek-AI 2025 (R1, arXiv / Nature);
  - Ji et al. 2023 (hallucination survey).
- **Figures:**
  - tokenisation of a sentence;
  - an embedding-space sketch;
  - transformer / attention schematic;
  - the training pipeline (pre-training → instruction tuning → RLHF).

### Chapter 4: Scaling, Compute and the Limits of Progress
- **Job:** why AI improved so fast, and what may slow it.
- **Must cover:**
  - scaling laws (Kaplan 2020; Chinchilla / Hoffmann 2022);
  - training-compute trends;
  - cost trends;
  - data limits ("running out of data");
  - synthetic data and model collapse;
  - algorithmic efficiency gains;
  - inference cost declines;
  - test-time scaling;
  - emergence and its critique (Wei 2022 vs. Schaeffer 2023);
  - benchmarks, saturation and contamination;
  - how capabilities are measured, including METR's task time-horizon metric.
- **Anchors:**
  - Kaplan et al. 2020;
  - Hoffmann et al. 2022;
  - Sevilla et al. 2022 (compute trends) / Epoch AI data;
  - Villalobos et al. 2024 (data);
  - Shumailov et al. 2024 (Nature, model collapse);
  - Wei et al. 2022;
  - Schaeffer et al. 2023;
  - Kwa et al. 2025 (METR time horizons);
  - Stanford AI Index 2025/2026.
- **Figures:**
  - a schematic log-log scaling curve (labelled schematic);
  - a training-compute trend chart (exact cited data points only);
  - a benchmark saturation chart (cited data) or a METR horizon chart (cited data).

## Part II: The Frontier: Technology Trends

### Chapter 5: From Chatbots to Agents
- **Job:** the shift to agentic systems: what they are and how reliable they are.
- **Must cover:**
  - definition of an agent (model + tools + loop + memory);
  - tool use and function calling;
  - protocols (Model Context Protocol, Agent2Agent);
  - computer-use agents;
  - coding agents and software engineering (SWE-bench);
  - agentic commerce and payments (AP2, x402: brief);
  - reliability, compounding errors;
  - security: prompt injection;
  - evaluation of agents;
  - multi-agent systems and their specific risks (Hammond et al. 2025);
  - economic agents (Hadfield & Koh 2025; Tomašev et al. 2025).
- **Anchors:**
  - Yao et al. 2023 (ReAct);
  - Schick et al. 2023 (Toolformer);
  - Jimenez et al. 2024 (SWE-bench);
  - Anthropic 2024 MCP announcement;
  - Greshake et al. 2023 (prompt injection);
  - METR 2025;
  - Hammond et al. 2025;
  - the agent papers already verified in the previous version.
- **Figures:**
  - the agent loop (perceive–plan–act–observe);
  - a tool-use sequence diagram;
  - error compounding over steps (simple computed curve, labelled as arithmetic).

### Chapter 6: AI for Science, Mathematics and Engineering
- **Job:** AI as a research tool and its limits.
- **Must cover:**
  - protein structure prediction (AlphaFold 2021; 2024 Nobel Prize in Chemistry), at a high level only;
  - weather forecasting (GraphCast / GenCast);
  - materials (GNoME and its critique);
  - mathematics (AlphaProof / AlphaGeometry 2024; IMO gold-level 2025; AlphaEvolve 2025);
  - autonomous "AI scientist" systems (Sakana / Nature 2026; Kosmos);
  - AI-assisted coding in research;
  - reproducibility;
  - "illusions of understanding" (Messeri & Crockett 2024);
  - intellectual debt (Zittrain).
  - **Strict:** no detailed biology, pathogen, toxin, drug-resistance or weapon content; protein work at the level of "predicts 3D structure".
- **Anchors:**
  - Jumper et al. 2021;
  - Nobel 2024 press release;
  - Lam et al. 2023 (GraphCast, Science);
  - Price et al. 2024/2025 (GenCast, Nature);
  - Merchant et al. 2023;
  - Cheetham & Seshadri 2024;
  - Trinh et al. 2024 (AlphaGeometry);
  - DeepMind 2025 IMO;
  - Lu et al. 2026 (Nature AI Scientist);
  - Messeri & Crockett 2024.
- **Figures:**
  - a "where AI enters the scientific cycle" diagram;
  - a weather-forecast skill comparison (cited) or a math-milestones timeline.

### Chapter 7: Chips, Data Centres, Energy and Open Models
- **Job:** the physical and industrial base of AI.
- **Must cover:**
  - GPUs and accelerators;
  - the semiconductor supply chain (TSMC, ASML, Nvidia);
  - export controls (US 2022 onward);
  - data-centre electricity (IEA 2025/2026);
  - water;
  - cost of training runs;
  - concentration among a few firms;
  - open-weight models (Llama, Mistral, Qwen, DeepSeek), with their benefits and risks;
  - the "DeepSeek moment" (Jan 2025);
  - compute governance;
  - sovereign AI and national strategies.
- **Anchors:**
  - IEA 2025 *Energy and AI* (and the April 2026 update);
  - Epoch AI on training costs;
  - Stanford AI Index;
  - US BIS export-control rules (Oct 2022, Oct 2023, Jan 2025);
  - Kapoor et al. 2024 (open foundation models);
  - Sastry et al. 2024 (compute governance);
  - de Vries 2023 (Joule).
- **Figures:**
  - data-centre electricity 2024 vs. 2030 projection (IEA numbers);
  - an AI supply-chain stack diagram (chips → cloud → models → applications).

## Part III: Society and Economy

### Chapter 8: Work, Productivity and the Economy
- **Job:** what the evidence says about AI and work.
- **Must cover:**
  - task-based frameworks (exposure measures: Eloundou et al. 2023/2024; Felten et al.);
  - experimental productivity studies:
    - Brynjolfsson, Li & Raymond 2023/2025 (customer support);
    - Noy & Zhang 2023 (Science);
    - Dell'Acqua et al. 2023 ("jagged frontier");
    - Peng et al. 2023 (Copilot);
    - METR 2025 developer RCT (slowdown);
  - adoption data (surveys; Anthropic Economic Index; Census BTOS);
  - entry-level effects (Brynjolfsson, Chandar & Chen 2025/2026);
  - macro forecasts and their spread (Acemoglu 2024 vs. Goldman Sachs);
  - inequality;
  - deskilling (Bainbridge 1983; the colonoscopy study 2025);
  - the policy response.
- **Anchors:** the studies above, plus PwC 2026, Humlum & Vestergaard (Denmark).
- **Figures:**
  - a productivity-effect comparison chart (exact study results with confidence where available);
  - exposure vs. adoption framework diagram.

### Chapter 9: Information, Media and Democracy
- **Job:** the evidence on AI and the information ecosystem.
- **Must cover:**
  - deepfakes and synthetic media;
  - the "liar's dividend";
  - the evidence from the 2024 election "super-year" (limited measurable impact; cite studies);
  - AI persuasion experiments (Hackenburg et al. 2025 *Science*; Costello et al. 2024 conspiracy dialogue, *Science*);
  - silicon sampling (Argyle 2023; Pew 2026);
  - content provenance (C2PA, watermarking, SynthID);
  - recommender systems;
  - journalism and search traffic;
  - platform governance (DSA).
- **Anchors:** the sources listed.
- **Figures:**
  - provenance pipeline diagram;
  - persuasion-effect chart (cited numbers).

### Chapter 10: Education, Health and Everyday Life
- **Job:** AI in learning, medicine and personal life.
- **Must cover:**
  - tutoring RCTs (World Bank Nigeria 2025; Harvard physics tutor RCT 2024/2025);
  - learning harms (Bastani et al. 2024/2025, PNAS);
  - cheating and assessment;
  - AI in medicine:
    - FDA-cleared AI devices count;
    - diagnostic accuracy studies;
    - the clinician + AI evidence (mixed, e.g. Goh et al. 2024 JAMA Netw Open);
    - ambient scribes;
  - companions and loneliness (OpenAI / MIT 2025 studies);
  - accessibility (translation, vision aids);
  - privacy and memory.
  - **Strict:** no hazardous biomedical detail.
- **Anchors:** the studies above; Turkle 2026 (*Artificial Intimacy*), labelled as a book.
- **Figures:**
  - an RCT results chart (cited);
  - a "where AI sits in the clinical workflow" diagram.

## Part IV: Risk, Safety and Governance

### Chapter 11: Risks and Failure Modes
- **Job:** a structured taxonomy of AI risks, with evidence of each.
- **Must cover:**
  - the taxonomy of the International AI Safety Report (Bengio et al. 2025; 2026 update if any): malicious use, malfunctions, systemic risks;
  - hallucination;
  - bias and discrimination (Buolamwini & Gebru 2018; Obermeyer et al. 2019);
  - security vulnerabilities and AI-enabled cyber operations (reported incidents, clearly sourced);
  - misuse (high level only);
  - systemic risk:
    - algorithmic monoculture (Kleinberg & Raghavan 2021);
    - outcome homogenisation (Bommasani 2022);
    - correlated errors (Kim et al. 2025);
    - Artificial Hivemind (Jiang et al. 2025);
  - automation bias (Dratsch 2023);
  - loss-of-control debate (with views across the spectrum);
  - expert risk surveys (Grace et al. 2024);
  - how to weigh risks under uncertainty.
- **Anchors:** the sources listed.
- **Figures:**
  - risk taxonomy diagram;
  - a correlated-errors illustration (cited from Kim et al.).

### Chapter 12: Making AI Safe: Alignment, Interpretability and Evaluation
- **Job:** the technical safety toolkit and its limits.
- **Must cover:**
  - the alignment problem;
  - RLHF limits;
  - specification gaming (DeepMind list; Krakovna 2020);
  - sycophancy (Sharma et al. 2024);
  - deceptive behaviours in evaluations (Apollo 2024; alignment faking, Greenblatt et al. 2024);
  - interpretability (features / sparse autoencoders, circuits; Anthropic 2024 "Scaling Monosemanticity"; 2025 tracing);
  - chain-of-thought monitorability (Korbak et al. 2025);
  - red-teaming and dangerous-capability evaluations;
  - frontier safety frameworks / responsible scaling policies;
  - AI safety institutes;
  - model welfare (brief, balanced: Long et al. 2024);
  - corrigibility (Soares et al. 2015; off-switch game).
- **Anchors:** the sources listed.
- **Figures:**
  - a "Swiss cheese" layered-defence diagram;
  - an interpretability sketch (features in activations).

### Chapter 13: Governing AI: Law, Policy and International Coordination
- **Job:** the regulatory landscape as of October 2026.
- **Must cover:**
  - EU AI Act (risk tiers, GPAI obligations, timeline 2024–2027, the GPAI Code of Practice 2025, the "digital omnibus" changes if verified);
  - US federal and state approach (executive orders 2023 / 2025, state laws such as Colorado and California SB 53 if verified);
  - China (generative-AI measures 2023, labelling rules 2025);
  - UK;
  - international:
    - Bletchley 2023, Seoul 2024, Paris 2025 summits;
    - the Council of Europe convention;
    - UN resolutions / advisory body;
    - OECD / G7 Hiroshima process;
  - standards (ISO/IEC 42001);
  - liability;
  - copyright and training data (major lawsuits and rulings, verified status);
  - compute thresholds.
- **Anchors:** primary legal texts and official sites.
- **Figures:**
  - EU AI Act risk pyramid;
  - governance timeline 2023–2026.

## Part V: The Decade Ahead

### Chapter 14: Forecasting the Next Ten Years: Methods, Scenarios and Open Problems
- **Job:** how to think rigorously about AI futures, ending with open research problems.
- **Must cover:**
  - why forecasting AI is hard;
  - the track record of past predictions;
  - expert surveys (Grace et al. 2024);
  - forecasting platforms;
  - trend extrapolation (METR, Epoch);
  - scenario methods (e.g. AI 2027, presented as one scenario among others, with critiques);
  - key uncertainties (compute, data, algorithms, regulation, adoption, public opinion);
  - **open problems and proposals (clearly labelled as the author's proposals, each with its prior literature):**
    - population-level evaluation of agent fleets and correlated action;
    - non-delegable safeguards;
    - the M-1 criterion (credit common-cause failure / N-version literature);
    - feedback provenance;
    - competence reserves and skill fade;
    - signature capacity and meaningful human oversight;
    - legibility of agent-to-agent communication;
    - a short list of further proposals (cognitive custody, posthumous agents, covenant inheritance), one paragraph each.
- **Anchors:**
  - Grace et al. 2024;
  - Tetlock & Gardner 2015;
  - Kokotajlo et al. 2025;
  - Kwa et al. 2025;
  - Avizienis 1985;
  - Knight & Leveson 1986;
  - NERC N-1;
  - the 50.2 Hz case;
  - UK smart charge regulations;
  - Elish 2019.
- **Figures:**
  - a scenario cone / uncertainty fan;
  - the "single model vs. population" evaluation diagram.

## Back matter
- **Glossary:** about 120 terms, merged from the chapters.
- **Bibliography:** APA 7, generated from `bib/*.bib` by pandoc citeproc.
- **Week plan for instructors:** in the Preface.
