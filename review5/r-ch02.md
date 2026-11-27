# Review 5: Chapter 2 (textbook/chapters/ch02.md)

## Verdict
Technically accurate and well paced. I recomputed every worked example and all of them are correct: the neuron, the matrix layer, XOR, softmax and cross-entropy, the one-weight gradient descent, the nine-parameter backpropagation including the post-update forward pass, Adam's first step, He initialisation, convolution parameter counts, matrix-multiplication data reuse, the H100 operations-per-byte figure, the adversarial linearity estimate and the synapse comparison. The 2026 material on DeepSeek-V4 matches the company's report and release pages. There are no MUST items. **Ready to print**, with two minor SHOULD items.

## MUST change before printing
None.

## SHOULD change

### S1. DeepSeek-V4 "official versions in July and August": the July release is not in the cited sources
- Where: textbook/chapters/ch02.md:228
- Text now: "Released as a preview in April 2026 and in official versions in July and August, with the same structure. ... [@deepseekai2026deepseekv4; @deepseekai2026v4pro]"
- Problem: UNSUPPORTED (minor). The cited DeepSeek API news page covers only the V4-Pro GA release of 13 August 2026. DeepSeek's news index has no July item; its entries run from "DeepSeek-V4 Preview Release 2026/04/24" to "DeepSeek-V4-Pro GA Release 2026/08/13". The July release, DeepSeek-V4-Flash-0731, is real but documented on Hugging Face and in the press. The claim is mentioned only in the bib entry's note, so readers cannot trace it.
- Evidence: https://api-docs.deepseek.com/news/news260813 (sidebar list, accessed 27 November 2026); https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731.
- Change to: "Released as a preview in April 2026, with official versions of the smaller V4-Flash on 31 July and of V4-Pro on 13 August, both keeping the preview's structure." Add a bib entry:
  ```
  @misc{deepseekai2026v4flash0731,
    author       = {{DeepSeek-AI}},
    title        = {{DeepSeek-V4-Flash-0731}: Model Card},
    year         = {2026},
    howpublished = {Hugging Face model card, 31 July 2026 (company source)},
    url          = {https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731},
    urldate      = {2026-11-27}
  }
  ```

### S2. LeNet cheque volume: the source gives two figures
- Where: textbook/chapters/ch02.md:3
- Text now: "was reading the amounts, handwritten or printed, on millions of bank cheques a month in the United States, according to its developers [@lecun1998gradient]"
- Problem: UNCLEAR (minor; not wrong). The paper's introduction says "millions of checks per month in several banks across the United States". Its abstract says "reads several million checks per day", and its conclusion says it "has been reading millions of checks per day since then" (that is, since June 1996). The book's figure is the conservative one and is supported. A reader who checks the abstract, however, will find "per day".
- Evidence: LeCun et al. (1998), Proc. IEEE 86(11). Abstract: "It is deployed commercially and reads several million checks per day." Sec. I: "It is reading millions of checks per month in several banks across the United States." Sec. X: "it has been reading millions of checks per day since then."
- Change to: (optional) "...was reading the amounts, handwritten or printed, on millions of bank cheques in the United States (the developers' paper says per month in one place and per day in another) [@lecun1998gradient]". Or leave the text as it is.

## Could not verify
- Line 228: that V4 uses Muon for "the majority of its modules while keeping AdamW for a few, such as the embedding and output layers and the normalisation weights". The arXiv abstract (2606.19348) confirms that Muon is used. I did not read the module breakdown in the full report in this round.
- Line 227: the Kimi K2 details (a constant learning rate for the first 10 trillion tokens, and the MuonClip safeguard) are consistent with my knowledge of the report. I did not re-fetch it.

## Checked and confirmed
- **Recomputed with a script:**
  - Table 2.1: sigmoid 0.119/0.550/0.881, slope 0.248; tanh 0.197/0.964, slope 0.961.
  - Softmax: 0.659/0.242/0.0986; losses 0.417 and 2.317.
  - Backpropagation: h = (1.0, 0.5), p = 0.6225, L = 0.4741; all gradients in Table 2.3; the updated parameters; the second pass: h = (1.2265, 0.2735), z = 1.0423, p = 0.7393, L = 0.3021.
  - Gradient descent: the 0.3364 nudge; 0.44 → 0.88 → 0.0144; the factor 1 − 8η; 1.4 and 3.24; the threshold η > 0.25.
  - Adam: m₁ = −0.24, v₁ = 0.00576, step 0.001.
  - Initialisation and vanishing gradients: 0.25^10^ ≈ 9.5 × 10^−7^; √(2/512) = 0.0625; 0.0256^10^ ≈ 1.2 × 10^−16^.
  - Parameter and operation counts: 1,728 and 4.8 × 10^11^; 3.4 × 10^10^; reuse of about 2,731.
  - H100: 1,979/3.35 ≈ 590 (sparse) and ≈ 295 (dense).
  - Adversarial example: 150,528 × 0.007 × 0.01 ≈ 10.5.
  - Synapse comparison: 1.5 × 10^14^ / 1.6 × 10^12^ ≈ 94.
  - Figure 2.2: 26 parameters. AlexNet augmentation: ×2,048.
- **LeCun 1998, read in full text:** "only 60 000 trainable free parameters"; test error 0.95% and training error 0.35%.
- **DeepSeek-V4 report:** arXiv 2606.19348, submitted 26 April 2026: "DeepSeek-V4-Pro with 1.6T parameters (49B activated)", a one-million-token context, and Muon.
- **DeepSeek release dates:** V4-Pro GA on 13 August 2026 (DeepSeek API news). V4-Flash-0731 confirmed on Hugging Face and in the press.
- **H100 SXM specification:** 67 TF FP32; 1,979 TF FP16/BF16 with sparsity; 3.35 TB/s.
- **Values in published papers**, which agree with the sources as I know them:
  - Rosenblatt and the NYT of 8 July 1958;
  - the AlexNet ReLU result (six times faster);
  - batch normalisation's "14 times fewer training steps";
  - Goyal et al.: 8,192 images, 256 GPUs, one hour;
  - ResNet errors of 28.54/27.94/25.03/27.88%;
  - Table 2.4 recipes;
  - dropout MNIST errors of 1.60/1.25/1.06%;
  - Zhang et al. Table 2.5 values;
  - Zech et al.: 158,323 images, 34.2/1.2/1.0%, AUC 0.861, accuracy 99.95/99.98%, AUC 0.931/0.815;
  - Geirhos et al.: 95.9/22.1/63.9%;
  - Recht et al.: 3–15 and 11–14 points;
  - the panda/gibbon example: 57.7%, 99.3%, ε = 0.007; errors 89.4→17.9% and 0.94→0.84%;
  - Lee et al.: "ten times less frequently" and "over 4%";
  - Raina et al.: from weeks to a day;
  - Azevedo et al.: 86 billion; Pakkenberg et al.: 1.5 × 10^14^.
- **Bib keys and cross-references:** all cited keys exist in bib/ch02.bib. The cross-references to Sections 1.7, 7.1 and 3, and to Chapters 4 and 12, are correct. The DeepSeek-V4-Pro figures agree with ch03.md:439 and ch07.md:286.

## Tally
Claims checked: 71 · confirmed: 67 · wrong: 0 · outdated: 0 · unsupported/unclear (minor): 2 · could not verify: 2
