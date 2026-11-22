# Third review: Chapter 2 — How Neural Networks Learn

## Verdict
Ready after the MUST fix below. The chapter is technically sound: every worked example (forward pass, softmax and cross-entropy, one-weight gradient descent and its divergence threshold, the nine-parameter backpropagation table and update, the Adam first step, He-initialisation variance, convolution, parameter counts, arithmetic intensity) recomputes exactly in python, the equations and notation are consistent, and the explanations of SGD, momentum, Adam/AdamW, initialisation, normalisation, residual connections, dropout and universal approximation are correct as an ML expert would judge them. Every historical attribution, quotation and benchmark number I checked against the original papers (LeNet-5, AlexNet, ResNet, Transformer, Zhang et al., Zech et al., Geirhos et al., Goodfellow et al. 2015, etc.) matches, including page pinpoints. The one blocking item is currency: the chapter twice presents DeepSeek-V4 as a "preview" release, but DeepSeek issued the official (GA) DeepSeek-V4-Pro on 13 August 2026, before the book's stated end-October cut-off. A handful of small precision points are listed as SHOULD.

## MUST change before printing

### M1. DeepSeek-V4 is no longer a "preview"
- Where: textbook/chapters/ch02.md:78 and ch02.md:228
- Text now (78): "DeepSeek-V4-Pro, for example, which its developer released in 2026 as a "preview version" described in a company technical report, has 1.6 trillion parameters in total but activates 49 billion per token [@deepseekai2026deepseekv4]."
- Text now (228): "**DeepSeek-V4 (DeepSeek, 2026).** A preview release that uses Muon for the majority of its modules while keeping AdamW for a few, such as the embedding and output layers and the normalisation weights [@deepseekai2026deepseekv4]."
- Problem: OUTDATED. The preview of April 2026 was superseded by official releases: DeepSeek-V4-Flash-0731 (31 July 2026) and DeepSeek-V4-Pro-0813 (13 August 2026). The GA model is "built on the DeepSeek-V4-Pro (Preview) model structure", so the parameter counts and training recipe in the text still apply, but calling it a preview release misdescribes the model's status as of the book's end-October cut-off.
- Evidence: https://api-docs.deepseek.com/news/news260813 ("DeepSeek-V4-Pro GA Release ... We're launching DeepSeek-V4-Pro today!"); https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813 (README: "DeepSeek-V4-Pro-0813 is the official release of DeepSeek-V4-Pro, superseding the preview version ... It is built on the DeepSeek-V4-Pro (Preview) model structure, with a DSpark speculative decoding module attached"). The preview report is at https://arxiv.org/abs/2606.19348 ("We present a preview version of DeepSeek-V4 series ... DeepSeek-V4-Pro with 1.6T parameters (49B activated)"; sec. 2.4 and the V4-Pro training paragraph: "We employ the Muon optimizer for the majority of parameters, but use the AdamW optimizer for the embedding module, the prediction head module, and the weights of all RMSNorm modules").
- Change to (78): "DeepSeek-V4-Pro, for example, which its developer released as a preview in April 2026, described in a company technical report, and then in an official version in August, has 1.6 trillion parameters in total but activates 49 billion per token [@deepseekai2026deepseekv4]."
- Change to (228): "**DeepSeek-V4 (DeepSeek, 2026).** Released as a preview in April 2026 and in official versions in July and August, with the same structure. It uses Muon for the majority of its modules while keeping AdamW for a few, such as the embedding and output layers and the normalisation weights [@deepseekai2026deepseekv4]."
- Bib: no change needed for the recipe (it rests on the preview report). Optionally add a bib entry for the GA notice: DeepSeek, "DeepSeek-V4-Pro GA Release", DeepSeek API Docs news, 13 August 2026, https://api-docs.deepseek.com/news/news260813, and cite it after "in August".

## SHOULD change (real but not blocking)

### S1. Glorot and Bengio's reason for rejecting the sigmoid is not the slope argument
- Where: ch02.md:186
- Text now: "With sigmoid units, whose slope is at most 0.25 (Table 2.1), the slopes alone multiply the signal over ten layers by at most 0.25^10^ ≈ 0.00000095. This is the **vanishing gradient problem** [...]. Glorot and Bengio found that logistic sigmoid units are "unsuited for deep networks with random initialization", and proposed..."
- Problem: the quotation is exact, but placed right after the slope argument it reads as Glorot and Bengio's reason. Their stated reason is different: "because of its mean value, which can drive especially the top hidden layer into saturation" (abstract, https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf).
- Change to: "Glorot and Bengio found that logistic sigmoid units are "unsuited for deep networks with random initialization" because their non-zero mean output drives the top hidden layer into saturation, and proposed..."

### S2. "Each transformer block contains two sub-layers" holds only for encoder blocks and decoder-only models
- Where: ch02.md:196 and ch02.md:206
- Text now: "Each transformer block contains two sub-layers, an attention layer and a small fully connected network" and "Every transformer block uses residual connections around both of its sub-layers [@vaswani2017attention]."
- Problem: in the cited original design, each decoder block has three sub-layers (self-attention, encoder–decoder attention, feed-forward), each with a residual connection (Vaswani et al. 2017, sec. 3.1). This is true of the decoder-only language models of Chapter 3.
- Change to (196): "Each block of a transformer language model contains two sub-layers, an attention layer and a small fully connected network (Chapter 3)". Change to (206): "Every transformer block uses a residual connection around each of its sub-layers [@vaswani2017attention]."

### S3. Pinpoint for the saddle-point sentence
- Where: ch02.md:112, "[@lecun2015deep, p. 438]"
- Problem: "rarely a problem" is on p. 438, but "almost all of them have very similar values of the objective function" runs onto p. 439 (checked against the page breaks of the Nature PDF).
- Change to: "[@lecun2015deep, pp. 438–439]".

### S4. Reasoning-model claim rests on a 2016 Go paper
- Where: ch02.md:82
- Text now: "it is how game-playing systems and today's reasoning models are trained (Chapters 1 and 3) [@silver2016mastering]."
- Problem: Silver et al. 2016 supports game playing only. The reasoning-model half is unsupported by the cited source.
- Change to: "it is how game-playing systems were trained [@silver2016mastering] and, in a different form, today's reasoning models (Chapters 1 and 3)."

### S5. Unsourced "historians still debate"
- Where: ch02.md:41
- Text now: "although historians still debate how much it mattered [@goodfellow2016deep, sec. 1.2.1]"
- Problem: Goodfellow et al. sec. 1.2.1 says only that the critics "caused a backlash against biologically inspired learning in general" (https://www.deeplearningbook.org/contents/intro.html); it says nothing about historians' debate. Either cite a historian (e.g. Olazaran 1996, "A sociological study of the official history of the perceptrons controversy", Social Studies of Science 26(3):611–659) or delete the clause.
- Change to: "Goodfellow and colleagues count the critique among the causes of a backlash against neural network research [@goodfellow2016deep, sec. 1.2.1]."

### S6. "best standard networks" overstates the dropout paper
- Where: ch02.md:283
- Text now: "the best standard networks without dropout had reached 1.60% error"
- Problem: Srivastava et al. 2014 (sec. 6.1.1) say networks "that do not use dropout or unsupervised pretraining achieve an error of about 1.60%"; "best" is not in the source.
- Change to: "standard networks without dropout or unsupervised pre-training reached about 1.60% error".

## Could not verify
- ch02.md:3, NYT quote: the 8 July 1958 NYT article (p. 25) is paywalled. Its wording matches the AITopics archive record of the headline and many independent reproductions, and the chapter flags it as "as reproduced in" Ananthaswamy (2024), which I could not open. Low risk.
- ch02.md:257, AlexNet quote pinpoint "p. 1098": the quote is confirmed verbatim in the NeurIPS PDF; the proceedings page number follows from the 1097–1105 page range (quote is on the paper's second page). Low risk.
- No claim that matters for printing remains unverified.

## Reader notes
1. ch02.md:5 and 78: DeepSeek-V4-Pro's "1.6 trillion adjustable numbers" appears in the opening, eight paragraphs before mixture-of-experts and active parameters are explained. A reader may compare it with GPT-3's 175 billion and draw the wrong conclusion. A forward pointer "(Section 2.2)" would help.
2. ch02.md:233: "A photograph of 1,000 × 1,000 pixels has a million input values." A colour photograph has three million (three channels), as the chapter itself notes eight lines later for 224 × 224 images. Say "A greyscale photograph" or "three million input values ... three billion weights".
3. ch02.md:227: "approximately orthogonalises each matrix update" is the one technical term in the chapter left unexplained for a lay reader. The following clause helps but "orthogonalises" will stop many readers.
4. ch02.md:120: the step from "backward pass roughly twice that" to "about three forward passes" is quick. It is right (2N + 4N = 6N), but one more clause would let readers see the 6N coming.
5. ch02.md:304: the paragraph packs implicit regularisation, double descent, interpolation threshold, epoch-wise double descent, label noise and sample non-monotonicity into seven sentences. It is accurate but is the densest paragraph in the chapter.
6. ch02.md:304: "For linear models, SGD always converges to a solution of small norm" is exactly Zhang et al.'s sentence, but the same paper adds that minimum norm "is not predictive of generalization performance". A half-sentence would keep the reader from taking it as the answer.
7. Table 2.5 labels the networks "Inception (small)" and "AlexNet (small)"; Zhang et al. call them "Inception" and "Alexnet" (CIFAR-sized variants). The added "(small)" is helpful but could note that these are not the ImageNet networks named earlier.

## Checked and confirmed
Arithmetic (python, all exact to the printed rounding): neuron z = 0.2 / −0.3; Table 2.1 (sigmoid 0.119/0.5/0.550/0.881, slope 0.248; tanh −0.964/0/0.197/0.964, slope 0.961); Fig 2.2 26 parameters; matrix layer (−3.4, 1.8) → (0, 1.8); XOR Table 2.2 and line h1 − 2h2 = 0.5; squared error 0.64/0.01; softmax 0.659/0.242/0.0986, CE 0.417/2.317, ln 10 ≈ 2.3; one-weight GD 0.4/−0.6/0.36, slope −2.4, nudge 0.3364/0.0236, step to 0.44/0.88/0.0144; factor 1 − 8η, η = 0.5 → −3, w = 1.4, loss 3.24, divergence above 0.25, curvature 8; Fig 2.3 path 0.44/0.488/0.4976 and 80% per step; Table 2.3 all 16 values; update to (0.5378, 0.3255), (−0.5378, 0.4245), biases ±0.0378, v = (1.0378, −0.9811), c = 0.0378; re-forward h = (1.2265, 0.2735), z = 1.0423, p = 0.7393, L = 0.3021; 6N/2N; momentum 1/(1−β) = 10; Adam m1 = −0.24, v1 = 0.00576, bias-corrected −2.4/5.76, step +0.001; 0.25^10 = 9.5e−7; He std √(2/512) = 0.0625, factor 0.0256, 0.0256^10 = 1.2e−16; conv feature map rows (0, 3, 3), 1,728 weights, 4.83e11 FC weights; Fig 2.5 pooling (4, 2 / 2, 5) and 225 weights; 2·1024·4096² = 3.4e10; reuse 2·4096/3 = 2,731; H100 1979/3.35 = 591, dense 295; adversarial 0.007·0.01·150,528 = 10.5; 1.5e14/1.6e12 = 94; AlexNet 32²·2 = 2,048. figs_ch02.py values match text and captions (asserts included).

Opening
- July 1958 ONR demo, IBM 704, punch cards left/right, 50 trials, Rosenblatt research psychologist at Cornell Aeronautical Laboratory — Cornell Chronicle (Lefkowitz 2019).
- NYT 8 July 1958 p. 25 headline and "embryo ... conscious of its existence" — AITopics archive record and reproductions (see Could not verify).
- LeNet-5 "60 000 trainable free parameters"; cheque system "reading millions of checks per month in several banks across the United States" (Sec. I); "handwritten and machine-printed bank checks"; AT&T Labs-Research — LeCun et al. 1998 PDF (gwern mirror). (Abstract says "per day"; the chapter's "a month" follows Sec. I and is conservative.)
- DeepSeek-V4-Pro 1.6T total / 49B active; open weights — arXiv 2606.19348, DeepSeek news 24 Apr 2026.

2.1
- Rosenblatt quote "contained in connections or associations rather than topographic representations", p. 387 — Psych. Review PDF (UIC mirror), page 2 = p. 387.
- AlexNet ReLU 4-layer net 25% CIFAR-10 training error six times faster than tanh — NeurIPS 2012 PDF.
- Goodfellow sec. 6.1 "the default recommendation"; sec. 6.3.1 "cannot learn via gradient-based methods" — deeplearningbook.org.
- Shazeer 2020: GLU variants improve over ReLU/GELU in transformers — arXiv abstract. Llama uses SwiGLU (and RMSNorm) — Llama paper sec. 2.2.
- GELU in BERT; Hendrycks & Gimpel preprint — known; arXiv entry exists.

2.2
- XOR critique caused "a backlash against biologically inspired learning" — Goodfellow sec. 1.2.1.
- Universal approximation; worst-case exponential hidden units; depth results — Goodfellow sec. 6.4.1.
- AlexNet 60 million parameters — NeurIPS PDF. GPT-3 175B — known.

2.3
- "knobs" and "tiny amount" gradient definition, p. 436; SGD "surprisingly quickly", p. 437; "poor local minima are rarely a problem", p. 438; saddle points with "very similar values", p. 439 — Nature PDF page by page.

2.4
- C ≈ 6N per training token; Cforward ≈ 2N; context-dependent term negligible for d_model > n_ctx/12 — Kaplan et al. arXiv PDF.
- Rumelhart et al. 1986 Nature 323:533–536 — Crossref.

2.5
- Glorot & Bengio: before 2006 deep nets "not successfully trained"; sigmoid "unsuited for deep networks with random initialization" — PMLR PDF.
- Goodfellow sec. 15.1.1 "largely abandoned, except in ... natural language processing"; "medium-sized datasets" — deeplearningbook.org.
- Goodfellow sec. 8.7.5 advances "obtained by changing the model family"; skip connections "mitigate the vanishing gradient problem" — deeplearningbook.org.
- Goyal et al.: up to 8,192 images, no loss of accuracy, linear scaling rule — arXiv abstract.
- Transformer: warmup_steps = 4000, inverse-sqrt decay; Adam β1 0.9, β2 0.98; ~25,000 source + 25,000 target tokens; Pdrop 0.1; label smoothing 0.1; no weight decay or init reported — arXiv PDF.
- MiniCPM introduces WSD schedule — arXiv abstract. SGDR — arXiv.
- Momentum terminal velocity — Goodfellow sec. 8.3.2. AlexNet momentum 0.9; ResNet momentum 0.9 — both PDFs.
- Goodfellow sec. 8.5.4 "depend largely on the user's familiarity with the algorithm" — deeplearningbook.org.
- AdamW: L2 and weight decay inequivalent for Adam; "substantially improves Adam's generalization performance" — arXiv abstract.
- Llama: AdamW, cosine to 10% of max, clipping 1.0, pre-normalisation "to improve the training stability", RMSNorm — arXiv PDF. Llama 3 AdamW + cosine — known/arXiv entry.
- DeepSeek-V3: AdamW, gradient clipping norm 1.0, FP8 mixed-precision framework — arXiv PDF.
- Kimi K2: 1.04T total, 32B activated; constant LR 2e-4 for first 10T tokens then cosine decay; Moonlight showed Muon "substantially outperforms AdamW" at equal compute; exploding attention logits, QK-Clip — arXiv PDF.
- DeepSeek-V4: Muon for majority; AdamW for embedding, prediction head, RMSNorm weights — arXiv PDF.
- He 2015: std √(2/n_l); 30-layer model, Xavier "completely stalls" — arXiv PDF.
- BN "14 times fewer training steps"; internal covariate shift — arXiv abstract.
- Santurkar et al.: "has little to do with the success"; "significantly smoother"; authors at MIT (Madry group) — arXiv abstract.
- Layer norm (Ba, Kiros, Hinton 2016); RMSNorm (Zhang & Sennrich 2019) cheaper — arXiv abstracts.
- ResNet: depths "sixteen to thirty"; 56- vs 20-layer CIFAR-10 plain; Table 2 top-1 (10-crop) 27.94/28.54/27.88/25.03; batch 256; LR 0.1 ÷10 on plateau; wd 0.0001; no dropout; BN after each conv; scale/crop/flip/colour augmentation; init as in [13] (He 2015); 1202-layer "no optimization difficulty", overfitting; 152-layer and 1st place ILSVRC 2015 — arXiv PDF. Fig 2.4 values match.
- AlexNet: batch 128; wd 0.0005; LR 0.01, ÷10 three times; N(0, 0.01) init; LRN; dropout in first two FC layers — NeurIPS PDF.

2.6
- ConvNet "four key ideas"; roots in neocognitron; simple/complex cells, p. 439 — Nature PDF.
- AlexNet "frequency- and orientation-selective kernels, as well as various colored blobs"; five to six days on two GTX 580 GPUs; "simply by waiting for faster GPUs" — NeurIPS PDF.
- Goodfellow sec. 9.2 sparse interactions, parameter sharing, equivariant representations — deeplearningbook.org.
- "These layers of features are not designed by human engineers", p. 436 — Nature PDF.
- Szegedy et al.: "the space, rather than the individual units" carries semantic information; "imperceptible non-random perturbation" — arXiv PDF.
- LSTM "found extremely successful" — Goodfellow sec. 10.10.1.
- H100 SXM: FP32 67 TFLOPS; FP16/BF16 Tensor 1,979 TFLOPS "with sparsity"; 3.35 TB/s — nvidia.com H100 page.
- Blackwell "new 4-bit floating point AI inference capabilities", 18 March 2024 — Nvidia press release. Rubin NVFP4 training 35 PFLOPS — Nvidia technical blog, 5 Jan 2026.
- Raina et al. 2009 ICML pp. 873–880 — Crossref.

2.7
- Goodfellow sec. 7.4 "The best way to make a machine learning model generalize better is to train it on more data"; sec. 7.8 early stopping "most commonly used form of regularization" — deeplearningbook.org.
- LeNet-5 test 0.95%, training 0.35% after 19 passes — LeCun 1998 PDF.
- AlexNet weight decay "important for the model to learn ... not merely a regularizer"; dropout "substantial overfitting"; augmentation factor 2048 "highly interdependent", "suffers from substantial overfitting" — NeurIPS PDF.
- Dropout: p = 0.5 hidden, 0.8 input; 2^n thinned networks; MNIST 1.60/1.35/1.25/1.06 — JMLR PDF.
- Zhang et al. Table 1: Inception 1,649,402 params, 100.0/89.05, 100.0/85.75, random 100.0/9.78; Alexnet 1,387,786, 99.90/81.22, 100.0/76.07, random 99.82/9.86; "neither necessary nor by itself sufficient"; "For linear models, SGD always converges to a solution with small norm" — arXiv PDF.
- Nakkiran et al.: double descent in model size and epochs; "increasing (even quadrupling) the number of train samples actually hurts" — arXiv abstract.
- Belkin et al. PNAS 116:15849–15854 — Crossref.
- Lee et al.: "ten times less frequently"; train–test overlap "affects over 4% of the validation set" — arXiv abstract.
- PaLM trained without dropout — known (JMLR paper); not fetched.

2.8
- Geirhos 2020 definition of shortcuts (abstract); cows on grass example — arXiv PDF; Nature MI 2:665–673 — Crossref.
- Geirhos 2019: humans 95.9% shape of correct decisions; ResNet-50 22.1% shape; "Indian elephant 63.9%" — arXiv PDF.
- Zech et al.: 158,323 radiographs, three systems; prevalence MSH 34.2%, NIH 1.2%, IU 1.0%; hospital-only sorting AUC 0.861; hospital ID 99.95% (NIH) and 99.98% (MSH); joint model 0.931 internal vs 0.815 at IU; 10-fold prevalence difference improved internal but not IU performance; "may confound predictions"; "cannot fully assess what other factors might be contributing"; NLP-derived labels for NIH/MSH, manual for IU — PLOS Medicine full text.
- Hanley & McNeil 1982 Radiology 143:29–36 — Crossref.
- Recht et al.: drops 3–15% CIFAR-10, 11–14% ImageNet; "slightly 'harder' images"; not adaptivity — arXiv abstract.
- Goodfellow et al. 2015: panda 57.7%, gibbon 99.3%, ε = .007; activation grows by εmn; adversarial error 89.4% → 17.9%; test error 0.94% → 0.84% — arXiv PDF.
- Ilyas et al. "non-robust features ... highly predictive, yet brittle and incomprehensible to humans" — arXiv abstract. Athalye et al. ICML 2018 — PMLR.
- Kirkpatrick et al. "widely thought that catastrophic forgetting is an inevitable feature of connectionist models", PNAS 114:3521 — arXiv abstract, Crossref.

2.9
- Beniaguev et al.: temporally convolutional DNN of five to eight layers; without NMDA a one-hidden-layer network sufficed — HUJI/ELSC summaries; Neuron 109:2727 — Crossref.
- Azevedo et al. 2009 (86 billion neurons) — Crossref for record; figure known.
- Pakkenberg et al. 2003: ≈0.15 × 10^15 neocortical synapses — PubMed/catalogue record; Exp. Gerontol. 38:95–99 — Crossref.
- Lillicrap et al. 2020 abstract: backprop "has historically been viewed as biologically problematic", p. 335 — Oxford record; Nat. Rev. Neurosci. 21:335–346 — Crossref.
- Yamins et al. PNAS 111:8619–8624 — Crossref; IT/V4 result known.

Bib entries checked against Crossref (title, first author, year, volume, pages; all match): mcculloch1943logical, rosenblatt1958perceptron, rumelhart1986learning, lecun1998gradient, lecun2015deep, cybenko1989approximation, belkin2019reconciling, zeiler2014visualizing, hubel1962receptive, fukushima1980neocognitron, raina2009large, geirhos2020shortcut, kirkpatrick2017overcoming, zech2018variable, azevedo2009equal, beniaguev2021single, lillicrap2020backpropagation, yamins2014performance, he2016deep, he2015delving, nakkiran2021deep, devlin2019bert, hanley1982meaning, hinton2006fast, hochreiter1997long, seide2011conversational, hornik1989multilayer, lee2022deduplicating, pakkenberg2003aging, schmidhuber2015deep. Checked via arXiv/PDF: deepseekai2026deepseekv4 (arXiv record gives published 26 Apr 2026, matching the bib note despite the 2606 identifier), kimiteam2025kimi, deepseekai2024deepseekv3, touvron2023llama, kaplan2020scaling, hu2024minicpm, shazeer2020glu, zhang2017understanding, szegedy2014intriguing, goodfellow2015explaining, geirhos2019imagenettrained, ilyas2019adversarial, recht2019imagenet, santurkar2018how, ba2016layer, zhang2019root, kingma2015adam, loshchilov2019decoupled, goyal2017accurate, ioffe2015batch, vaswani2017attention, krizhevsky2012imagenet, glorot2010understanding, srivastava2014dropout, nvidia2026h100, nvidia2024blackwell, aubrey2026inside, lefkowitz2019professors. No bibliographic problems found.

## Tally
Claims checked against a web source: 190. Confirmed: 187. Wrong: 0. Outdated: 1 (DeepSeek-V4 "preview", two places). Unsupported by cited source: 2 minor (S4, S5; SHOULD level). Could not verify: 2 (low risk). Arithmetic items recomputed: 42 (errors: 0). Bib entries checked: 58 (problems: 0).
