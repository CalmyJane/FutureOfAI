# Evidence log: Chapter 2 (How Neural Networks Learn)

All sources checked on 2026-10-22. Bibliographic metadata checked against Crossref (api.crossref.org) unless stated otherwise.

| Key | Claim supported | Exact number / quote | URL checked | Evidence type |
|---|---|---|---|---|
| lefkowitz2019professors | July 1958 ONR demonstration; IBM 704; after 50 trials learned to distinguish cards marked left vs right; NYT headline | "After 50 trials, the computer taught itself to distinguish cards marked on the left from cards marked on the right" (paraphrased in text) | https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon | news (university news office; used for event) |
| newyorktimes1958new | NYT report, 8 July 1958, p. 25: "walk, talk, see, write, reproduce itself and be conscious of its existence" | quote as given; original not accessed directly (paywalled archive); wording confirmed via Ananthaswamy 2024 sample and Cornell Chronicle headline | https://cdn.penguin.co.uk/dam-assets/books/9780241586488/9780241586488-sample.pdf | news (historical event) |
| ananthaswamy2024why | Secondary source for NYT quote; press demonstration was the day before the NYT story; Further reading | "The Navy revealed the embryo of an electronic computer today that it expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence." Published Allen Lane / Dutton 2024, ISBN 978-0-241-58648-8 | https://cdn.penguin.co.uk/dam-assets/books/9780241586488/9780241586488-sample.pdf | book (popular science) |
| lecun1998gradient | LeNet-5 cheque reading; ~60,000 trainable parameters; 345,308 connections; train error 0.35% vs test 0.95%; authors at AT&T Labs-Research | "It is deployed commercially and reads several million checks per day" (abstract); "reading millions of checks per month in several banks across the United States" (Sec. I); "345 308 connections, but only 60 000 trainable free parameters"; "test error rate stabilizes ... at 0.95%. The error rate on the training set reaches 0.35%" | https://gwern.net/doc/ai/nn/cnn/1998-lecun.pdf ; DOI 10.1109/5.726791 | peer-reviewed |
| mcculloch1943logical | Idealised neurons described with logic because of "all-or-none" character; fixed connections | "Because of the 'all-or-none' character of nervous activity, neural events and the relations among them can be treated by means of propositional logic." (abstract, p. 115) | https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf (1990 reprint); DOI 10.1007/BF02478259 | peer-reviewed |
| rosenblatt1958perceptron | Perceptron stores information in connections | "the information is contained in connections or associations rather than topographic representations" (p. 387) | https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf ; DOI 10.1037/h0042519 | peer-reviewed |
| goodfellow2016deep | ReLU default recommendation (ch. 6); XOR solution (sec. 6.1); Minsky XOR critique and backlash (ch. 6 history); universal approximation caveat (sec. 6.4.1); backprop cost same order as forward pass (sec. 6.5); history: Linnainmaa 1976, Werbos 1981, independent rediscovery (sec. 6.6); generalisation vs optimisation (sec. 5.2); hyperparameters definition (sec. 5.3); early stopping (sec. 7.8); GPUs (sec. 12.1.2) | "In modern neural networks, the default recommendation is to use the rectified linear unit"; "We are not guaranteed, however, that the training algorithm will be able to learn that function"; early stopping "is probably the most commonly used form of regularization in deep learning"; "the number of computations for the gradient computation is of the same order as the number of computations for the forward computation"; XOR solution W = all ones, c = [0, −1], w = [1, −2] | https://www.deeplearningbook.org/contents/mlp.html ; /ml.html ; /regularization.html ; /applications.html | textbook (MIT Press) |
| minsky1969perceptrons | Book proved limits of single-layer perceptrons (e.g. XOR) | MIT Press, Cambridge MA, 1969 | https://mlanthology.org/misc/1969/minsky1969misc-perceptrons ; library catalogue records | book (scholarly monograph) |
| cybenko1989approximation | Single hidden layer of sigmoid units can approximate any continuous function | title and metadata confirmed; result as standardly stated (on compact domains) | DOI 10.1007/BF02551274 | peer-reviewed |
| krizhevsky2012imagenet | AlexNet 60 million parameters, 650,000 neurons; 1.2M training / 50k validation / 150k test images; dropout used; 5–6 days on two GTX 580 GPUs | "60 million parameters and 650,000 neurons"; "roughly 1.2 million training images, 50,000 validation images, and 150,000 testing images"; "between five and six days to train on two GTX 580 3GB GPUs"; "can be improved simply by waiting for faster GPUs and bigger datasets to become available" (p. 2) | https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf | peer-reviewed (conference) |
| brown2020language | GPT-3 has 175 billion parameters | "GPT-3, an autoregressive language model with 175 billion parameters" | https://arxiv.org/abs/2005.14165 ; NeurIPS 2020 proceedings page (pp. 1877–1901) | peer-reviewed (conference) |
| lecun2015deep | Weights as "knobs" (p. 436); hundreds of millions of weights and labelled examples (p. 436); hilly landscape (p. 437); SGD "surprisingly quickly" (pp. 436–437); poor local minima "rarely a problem", saddle points (p. 438); layer hierarchy edges→motifs→parts→objects, "not designed by human engineers" (p. 436); ConvNet four key ideas (p. 439); simple/complex cells, neocognitron (p. 439); chain-rule figure (Fig. 1) | quotes as given; page numbers checked against PDF page breaks | https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf ; DOI 10.1038/nature14539 | peer-reviewed (review) |
| rumelhart1986learning | Backprop popularised; hidden units come to represent features | "internal 'hidden' units which are not part of the input or output come to represent important features of the task domain" (abstract, p. 533) | https://inspirehep.net/api/literature/2171919 (abstract record); DOI 10.1038/323533a0 | peer-reviewed |
| zhang2017understanding | Networks can fit random labels and even random noise | "easily fit a random labeling of the training data" | https://arxiv.org/abs/1611.03530 (published ICLR 2017) | peer-reviewed (conference) |
| belkin2019reconciling | Double-descent curve | "increasing model capacity beyond the point of interpolation results in improved performance" | DOI 10.1073/pnas.1903070116 (abstract via Semantic Scholar) | peer-reviewed |
| srivastava2014dropout | Dropout randomly drops units during training to reduce overfitting | "The key idea is to randomly drop units (along with their connections) from the neural network during training." | https://jmlr.org/papers/v15/srivastava14a.html | peer-reviewed |
| zeiler2014visualizing | Visualised features by layer: layer 2 corners/edge-colour conjunctions; layer 3 textures; layer 4 dog faces; layer 5 whole objects (keyboards, dogs) | "Layer 2 responds to corners and other edge/color conjunctions. Layer 3 ... similar textures (e.g. mesh patterns ...). Layer 4 ... dog faces ... Layer 5 shows entire objects ... e.g. keyboards" | https://arxiv.org/abs/1311.2901 ; DOI 10.1007/978-3-319-10590-1_53 | peer-reviewed (conference) |
| szegedy2014intriguing | Semantic information spread across units; imperceptible perturbation causes misclassification | "it is the space, rather than the individual units, that contains the semantic information"; "imperceptible perturbation" | https://arxiv.org/abs/1312.6199 | peer-reviewed (conference, ICLR 2014; bib updated at fact-check) |
| hubel1962receptive | Simple and complex cells in cat visual cortex (inspiration for CNNs) | metadata confirmed; CNN-inspiration link stated in LeCun et al. 2015, p. 439 | DOI 10.1113/jphysiol.1962.sp006837 | peer-reviewed |
| fukushima1980neocognitron | Neocognitron as root of ConvNets | metadata confirmed; "ConvNets have their roots in the neocognitron" (LeCun et al. 2015, p. 439) | DOI 10.1007/BF00344251 | peer-reviewed |
| raina2009large | GPU training cut time for 4-layer, 100M-parameter model from weeks to ~a day | "from several weeks to around a single day" (abstract). NOTE: abstract speed-up factor differs between versions (55x vs 70x), so no factor is quoted | https://mlanthology.org/icml/2009/raina2009icml-large/ ; DOI 10.1145/1553374.1553486 | peer-reviewed (conference) |
| goodfellow2015explaining | Panda 57.7% → gibbon 99.3% after imperceptible perturbation | "panda" 57.7% confidence; "gibbon" 99.3% confidence (Fig. 1, GoogLeNet on ImageNet) | https://arxiv.org/pdf/1412.6572v3 (ICLR 2015) | peer-reviewed (conference) |
| geirhos2020shortcut | Definition of shortcut learning | "Shortcuts are decision rules that perform well on standard benchmarks but fail to transfer to more challenging testing conditions" (p. 665) | DOI 10.1038/s42256-020-00257-z | peer-reviewed (perspective) |
| kirkpatrick2017overcoming | Catastrophic forgetting widely thought inevitable; EWC slows learning on important weights | "it has been widely thought that catastrophic forgetting is an inevitable feature of connectionist models" (p. 3521) | DOI 10.1073/pnas.1611835114 | peer-reviewed |
| zech2018variable | Pneumonia CNNs; 158,323 radiographs; prevalence 34.2% / 1.2% / 1.0%; hospital sorting AUC 0.861; hospital ID 99.95% / 99.98%; internal AUC 0.931 vs external 0.815 | "CNNs robustly identified hospital system and department within a hospital, which ... may confound predictions" | DOI 10.1371/journal.pmed.1002683 | peer-reviewed |
| azevedo2009equal | Adult male human brain ~86 billion neurons | "86.1 +/- 8.1 billion NeuN-positive cells" | PubMed 19226510; DOI 10.1002/cne.21974 | peer-reviewed |
| beniaguev2021single | A 5–8 layer temporally convolutional DNN needed to capture I/O of a detailed model of a layer-5 cortical pyramidal neuron | "A temporally convolutional DNN with five to eight layers was required" | PubMed 34380016; DOI 10.1016/j.neuron.2021.07.002 | peer-reviewed |
| lillicrap2020backpropagation | Backprop historically viewed as biologically problematic; feedback connections may approximate error signals | "historically it has been viewed as biologically problematic" (p. 335) | PubMed 32303713; DOI 10.1038/s41583-020-0277-3 | peer-reviewed (review) |
| yamins2014performance | Performance-optimised networks predict IT and V4 neural responses | "its top output layer turns out to be highly predictive of IT spiking responses"; "intermediate layers are highly predictive of neural responses in the V4 cortex" | PubMed 24812127; DOI 10.1073/pnas.1403112111 | peer-reviewed |
| nielsen2015neural | Further reading | "Michael A. Nielsen, 'Neural Networks and Deep Learning', Determination Press, 2015" | http://neuralnetworksanddeeplearning.com/about.html | book (online) |

## Author-computed arithmetic (no citation needed)
- Neuron: 0.5×2 + (−1)×1 + 0.2 = 0.2; inputs (1,1) → −0.3 → ReLU 0; sigmoid(0.2) = 0.5498.
- XOR network: h1 = ReLU(x1+x2), h2 = ReLU(x1+x2−1), y = h1 − 2·h2 (matches Goodfellow et al. 2016, sec. 6.1).
- Figure 2.2 parameter count: 3×4 + 4×2 = 20 weights, 4 + 2 = 6 biases, 26 total.
- Cross-entropy: −ln 0.9 = 0.105; −ln 0.1 = 2.303; −ln 0.01 = 4.605.
- Gradient-descent example: w=0.2, x=2, t=1 → loss 0.36; w=0.21 → 0.3364; exact slope 2(wx−t)x = −2.4; lr 0.1 → w=0.44, loss 0.0144; lr 0.5 → w=1.4, loss 3.24.
- Chain-rule box: x=1, w1=2, w2=0.5, t=2 → h=2, y=1, L=1; dL/dy=−2, dL/dw2=−4, dL/dh=−1, dL/dw1=−1; after lr 0.1 step: w2=0.9, w1=2.1, y=1.89.

## Claims dropped
- Raina et al. (2009) speed-up factor (70x vs 55x across abstract versions): not quoted.
- "Far more than a child needs" (data-efficiency comparison): no source verified; cut.

## Fact-check (2026-10-22)

Independent check of all numbers, dates, quotations, attributions, worked arithmetic and bibliography (about 120 claims checked). Sources re-read: Penguin sample of Ananthaswamy 2024 (prologue), Cornell Chronicle 2019, Rosenblatt 1958 PDF, LeCun et al. 1998 PDF, LeCun et al. 2015 PDF, Krizhevsky et al. 2012 PDF, Szegedy et al. arXiv v4, Goodfellow et al. 2015 arXiv v3, deeplearningbook.org chapters 1, 5, 6, 7, 12, Europe PMC abstracts (Zech, Kirkpatrick, Lillicrap, Beniaguev, Yamins), Crossref metadata for every DOI, ML Anthology (Raina).

### Writer's flags
1. NYT 1958 quote: original (nytimes.com archive, Wayback) blocked (403 / connection reset). Verified against a reliable reproduction: Ananthaswamy 2024 prologue quotes the opening paragraph verbatim, with date (8 July 1958) and page (25); Cornell Chronicle confirms the headline. The original sentence's subject is "the embryo of an electronic computer", not "the machine's successors", so the sentence was rewritten to quote the original wording and the citation now reads "[@newyorktimes1958new, p. 25; as reproduced in @ananthaswamy2024why]".
2. LeCun et al. 1998: confirmed 60,000 trainable parameters, 345,308 connections (text "more than 340,000" correct), training error 0.35% after 19 passes, test error 0.95%, MNIST 60,000 training / 10,000 test images, "several million checks per day", "millions of checks per month in several banks across the United States", AT&T Labs-Research. No change needed.
3. Goodfellow et al. section numbers: ReLU default recommendation is in sec. 6.1 (was "ch. 6"; made precise); Minsky-Papert "backlash" is in ch. 1, sec. 1.2.1, not ch. 6 (corrected); sec. 6.1 (XOR solution), 6.4.1 (universal approximation, "We are not guaranteed"), 6.5 (backprop cost "of the same order" as forward), 6.6 (Linnainmaa 1976, Werbos 1981, rediscovery), 5.2 (generalisation vs optimisation), 5.3 (hyperparameters), 7.8 (early stopping quote), 12.1.2 (GPU implementations) all confirmed.
4. Szegedy et al.: changed bib from @misc arXiv preprint to @inproceedings, ICLR 2014 (Banff); confirmed via Goodfellow et al. 2015 reference list ("ICLR, abs/1312.6199, 2014"). Text "a widely cited preprint" -> "a widely cited study".

### Corrections (old -> new)
- "the Cornell psychologist Frank Rosenblatt" -> "Frank Rosenblatt, a research psychologist at the Cornell Aeronautical Laboratory" (Cornell Chronicle; he joined the university faculty later).
- NYT sentence: "expected the machine's successors to 'walk, talk, ...'" -> "had revealed 'the embryo of an electronic computer' that it expected 'will be able to walk, talk, ...'".
- Szegedy quote "imperceptible perturbation" -> "imperceptible non-random perturbation" (exact wording, arXiv v4 p. 2; abstract says "hardly perceptible").
- [@goodfellow2016deep, ch. 6] (ReLU) -> sec. 6.1; [@goodfellow2016deep, ch. 6] (backlash) -> sec. 1.2.1.
- [@lecun2015deep, p. 437] (gradient definition) -> p. 436; "surprisingly quickly" pp. 436-437 -> p. 437.
- Krizhevsky quote completed ("... bigger datasets to become available") and locator "p. 2" -> "p. 1098" (proceedings pagination, consistent with bib pages 1097-1105).
- "The underlying mathematics, a rule from calculus called the chain rule, was developed ... from the 1960s onwards" -> chain rule is centuries old; its efficient application was developed from the 1960s (Goodfellow sec. 6.6).
- "ImageNet competition data used to train AlexNet ... 150,000 test images" -> "dataset on which AlexNet was trained and evaluated" (test images are not training data).
- Zech: ">99.9% accuracy identifying hospital system" restricted to NIH and Mount Sinai radiographs (99.95% / 99.98%; IU not reported).
- Raina: "four-layer network" -> "four-layer network (a 'deep belief network')" (as in abstract).
- Further reading: "chapters 5-8 cover everything in this chapter" -> "chapters 5-9 cover most of this chapter" (CNNs are ch. 9; GPUs ch. 12).
- Bib: szegedy2014intriguing -> @inproceedings ICLR 2014; zeiler2014visualizing: added "Part I" and LNCS volume 8689.

### Worked arithmetic re-checked (all correct)
Neuron 0.2 / -0.3 -> 0; sigmoid(0.2) = 0.550; Figure 2.2: 12 + 8 = 20 weights + 6 biases = 26; XOR network matches Goodfellow eq. 6.4-6.6 and gives 0,1,1,0; squared errors 0.64, 0.01; cross-entropy 0.105, 2.303, 4.605; gradient example (0.36, 0.3364, slope -2.4, w 0.44, loss 0.0144; lr 0.5 -> 1.4, loss 3.24; lr 0.1 contracts error by factor 0.2 per step, so converges to 0.5 as stated); chain-rule box (h 2, y 1, L 1; gradients -2, -4, -1, -1; w2 0.9, w1 2.1, y 1.89); 2 x 3 = 6; 1,000 x 1,000 inputs x 1,000 neurons = 10^9 weights. Figure specs 2.1-2.4 consistent with text; no figure data changed.

### Remaining uncertainties
- NYT 1958 article not seen in the original; wording rests on Ananthaswamy 2024 (verbatim, with date and page) and the Cornell Chronicle headline.
- Szegedy et al. ICLR 2014 venue confirmed via a secondary reference list (OpenReview/dblp blocked); this is the well-known venue.
- Zeiler & Fergus layer descriptions and the Geirhos p. 665 quote rest on the writer's log (Crossref metadata confirmed; full text not re-read).

## Revision (2026-10-22, after reader panel)

Panel points (Mia) and global fixes applied; no new sources.
- XOR: new Table 2.1 (inputs, target, h1 = sum, h2 = ReLU(sum - 1), output h1 - 2h2) plus a paragraph explaining linear separability: (1,0) and (0,1) both map to hidden point (1,0), the 0 cases to (0,0) and (2,1); the line h1 - 2h2 = 0.5 separates them (checked: 1 > 0.5; 0 < 0.5; 0 < 0.5). Follows Goodfellow et al. sec. 6.1. Caption carries "Calculation by the author".
- Gradient step sign: text now says gradient descent moves opposite to the slope; step = -learning rate x slope = -0.1 x (-2.4) = +0.24 (weight 0.2 -> 0.44); lr 0.5: -0.5 x (-2.4) = +1.2 (weight -> 1.4). Arithmetic unchanged from fact-check.
- Double descent: now explicitly about model size, not training time (Figure 2.4's x-axis); test error falls, rises to the interpolation threshold, then falls again (Belkin et al. 2019). Q5 no longer ties the Zhang puzzle to Figure 2.4 but to the classical account in Section 2.5. Figure 2.4 spec unchanged.
- Universal approximation: "continuous function" explained in plain words (no sudden jumps); main sentence now "imitate any smooth input-output rule".
- Cross-entropy: loss defined as -ln(probability), a unitless number like squared error; 0.9 -> ~0.1 (-ln 0.9 = 0.105), 0.1 -> ~2.3 (-ln 0.1), 0.01 -> ~4.6 (-ln 0.01); each tenfold drop adds ~2.3.
- Name lists lightened: backprop history (Linnainmaa, Werbos sentence removed; still cites Goodfellow sec. 6.6 for multiple discovery); CNN history (Hubel and Wiesel, Fukushima names removed; citations kept).
- Repetitions: "the standard textbook" (4x) replaced by one introduction of Goodfellow, Bengio and Courville's *Deep Learning* and later "Goodfellow and colleagues"; "LeCun, Bengio and Hinton" (5x) reduced to one full introduction ("a widely cited 2015 review") and "the 2015 review"; Further reading "The standard graduate textbook" -> "A widely used graduate textbook".
- Analogy-limit formula: kept one explicit sentence (fog analogy, which Q2 uses); mixing desk, firm, factory and GPU limits folded into the sentences.
- Saddle-point sentence split into four; added LeCun et al. p. 438 point that saddle points have very similar objective values, so it matters little which one training settles near (checked against the Nature PDF).
- Cross-references: §2.6 paragraph-final references to Ch. 12 and Ch. 3 removed (one kept, to Ch. 4/7). "Its abstract notes" -> "It notes".
- Citations: duplicate goodfellow2015explaining in the adversarial paragraph removed.
- Body word count: 6,021 -> 6,247. pandoc --citeproc: no warnings.

## Consistency pass (2026-10-22, cross-chapter audit)
- §2.3 fog analogy: "breaks down in instructive ways" → "Real training differs from the walk in fog in three respects." (only remaining "breaks down" is discussion question 2 about the fog analogy).
- §2.6: "one pattern stands out" signpost removed.
- Debate closer "What would settle it" → "Evidence that could resolve it" (varied across chapters). No new sources.
