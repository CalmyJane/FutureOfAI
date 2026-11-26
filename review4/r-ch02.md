# Review 4: Chapter 2, How Neural Networks Learn

## Verdict

Ready to print. I found nothing that must change. The chapter explains the material clearly and the order of topics builds well. I recomputed every worked example, and all the arithmetic is correct to the stated precision:

- the single neuron;
- the activation table;
- the matrix layer;
- XOR;
- softmax and cross-entropy;
- the one-weight gradient-descent example and its divergence threshold;
- the nine-parameter backpropagation box, including the full update and the second forward pass;
- the Adam first step;
- He initialisation;
- the convolution and pooling figure;
- the parameter savings;
- the matrix-multiplication counts;
- the H100 operations-per-byte ratios;
- the adversarial ε·m·n estimate;
- the comparison of synapses with parameters.

Every quotation and every figure from a landmark paper that I could check against the source is correct. The only 2026 material, DeepSeek-V4-Pro, matches the developer's model card. The figures I inspected in the PDF (2.3, 2.4, 2.5, 2.6) agree with the text.

## MUST change before printing

None.

## SHOULD change

None that rises above taste. One optional clarification follows.

### S1 (optional). Parameter count for the August "official version" of DeepSeek-V4-Pro
- Where: textbook/chapters/ch02.md:78
- Text now: "DeepSeek-V4-Pro, for example, which its developer released as a preview in April 2026, described in a company technical report, and then in an official version in August, has 1.6 trillion parameters in total but activates 49 billion per token"
- Problem: UNCLEAR, low risk. The figures 1.6T and 49B are confirmed for the model described in the April technical report and on the Hugging Face card. Some secondary sources give slightly different figures for the 13 August checkpoint, DeepSeek-V4-Pro-0813: "1.57T … 48B active" and "about 1.7T". I could not find a primary source for those numbers. The bib entry says 0813 is "built on the preview model structure", which supports the book, so this is only a precaution.
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro (accessed 26 Nov 2026): "DeepSeek-V4-Pro with 1.6T parameters (49B activated)".
- Change to (only if the author wants to be safe): "…has 1.6 trillion parameters in total but activates 49 billion per token, according to the technical report"

## Could not verify
- That the 0813 official release keeps exactly 1.6T/49B (see S1).
- Zech et al. (2018): the account of the experiment that set the two training sites tenfold apart in pneumonia rates (line 321). The other Zech figures agree with the paper's abstract and tables as widely reported: 158,323 images, 34.2%/1.2%/1.0%, AUC 0.861, 99.95%/99.98%, 0.931 vs 0.815.
- The 1958 *New York Times* wording, which is cited as reproduced in Ananthaswamy (2024). The wording matches the commonly reproduced text.

## Checked and confirmed
- Rosenblatt's 1958 demonstration: Office of Naval Research, IBM 704, left/right cards, 50 trials (Cornell Chronicle). NYT, 8 July 1958, p. 25: "embryo of an electronic computer", "walk, talk, see, write, reproduce itself and be conscious of its existence".
- LeNet-5: about 60,000 parameters. The paper says it "is reading millions of checks per month in several banks across the United States" (sec. I), so the book's wording is supported. The abstract says "several million checks per day".
- LeNet-5 training and test error: 0.35% and 0.95%.
- Neuron example: 0.5·2 − 1·1 + 0.2 = 0.2; with inputs (1, 1) the total is −0.3.
- Table 2.1: σ(−2) = 0.119, σ(0.2) = 0.550, σ(2) = 0.881, σ′(0.2) = 0.248; tanh(0.2) = 0.197, slope 0.961; ReLU values.
- Matrix layer: −3.4 and 1.8, giving output (0, 1.8) after ReLU. XOR Table 2.2 and the geometry of the hidden coordinates. MLP parameter count: 12 + 8 + 6 = 26.
- Softmax of (2, 1, 0.1): 0.659, 0.242, 0.0986. Cross-entropy: 0.417 and 2.317.
- One-weight gradient descent: loss 0.36, slope −2.4, finite-difference check (0.3364, fall 0.0236), step to 0.44 (loss 0.0144), contraction factor 1 − 8η, divergence above η = 0.25, η = 0.5 overshooting to 1.4 (loss 3.24). Figure 2.3 values 0.488 and 0.4976.
- Backpropagation box (Table 2.3), recomputed exactly: p = 0.6225, L = 0.4741, every gradient, updated parameters (0.5378, 0.3255 / −0.5378, 0.4245 / ±0.0378 / 1.0378, −0.9811 / 0.0378), second pass h = (1.2265, 0.2735), z = 1.0423, p = 0.7393, L = 0.3021.
- Adam first step: m₁ = −0.24, v₁ = 0.00576, bias-corrected values −2.4 and 5.76, step +0.001. Defaults as given in Kingma & Ba.
- 0.25^10 ≈ 9.5 × 10^−7. He initialisation: √(2/512) = 0.0625; 0.5 × 512 × 10^−4 = 0.0256, and 0.0256^10 ≈ 1.2 × 10^−16.
- Convolution (Figure 2.5): the window over columns 2–4 gives 3; the feature map has columns 0/3/3; max pooling gives [4 2; 2 5]; a 25 → 9 fully connected layer needs 225 weights.
- Convolutional layer weights: 3 × 3 × 3 × 64 = 1,728. A fully connected equivalent needs 150,528 × 3,211,264 ≈ 4.8 × 10^11 weights.
- Matrix multiplication: 2 × 1,024 × 4,096² ≈ 3.4 × 10^10 operations; reuse 2 × 4,096/3 ≈ 2,731, matching "about 2,700".
- H100 SXM: 67 TFLOPS FP32, 1,979 TFLOPS FP16 tensor "with sparsity", 3.35 TB/s. 1,979/3.35 ≈ 591; dense 989/3.35 ≈ 295. Consistent with ch07.md:43.
- Krizhevsky et al.: ReLU reaches 25% error six times faster (CIFAR-10, four layers); full recipe in Table 2.4 (batch 128, momentum 0.9, weight decay 0.0005, learning rate 0.01 divided by 10 three times, dropout 0.5, Gaussian initialisation with σ = 0.01, local response normalisation, augmentation factor 2,048, "simply by waiting for faster GPUs…", "important for the model to learn", "not merely a regularizer").
- He et al. 2016: "16 to 30" layers; plain 56 vs 20 layers on CIFAR-10; top-1 errors 27.94 / 28.54 / 27.88 / 25.03 (Figure 2.4); 1,202 layers "no optimization difficulty"; Table 2.4 recipe. He et al. 2015: 30-layer network converges, Xavier initialisation "completely stalls".
- Vaswani et al.: 4,000 warm-up steps, inverse-square-root decay, β₂ = 0.98, batches of about 25k + 25k tokens, dropout 0.1, label smoothing 0.1.
- Goyal et al.: 8,192 images, 256 GPUs, one hour, 5-epoch warm-up. Ioffe & Szegedy: "14 times fewer training steps". Santurkar et al. quotations. Loshchilov & Hutter AdamW quotation.
- Goodfellow et al. quotations: "the default recommendation", "cannot learn", "been largely abandoned" (except in NLP), "user's familiarity with the algorithm", "The best way to make a machine learning model generalize better…", "probably the most commonly used form of regularization".
- Glorot & Bengio quotations. Cybenko and Hornik (1989). Raina et al. 2009 ("several weeks to around a single day", 100M parameters).
- Llama recipe (cosine to 10%, clipping at 1.0, pre-norm RMSNorm); Kimi K2 (1.04T/32B, constant learning rate for the first 10T tokens, then cosine, MuonClip); DeepSeek-V4 uses Muon (HF card: "We employ the Muon optimizer…"); Flash-0731 and Pro-0813 releases (bib).
- Srivastava et al.: p = 0.5 for hidden units and 0.8 for inputs; MNIST 1.60% → 1.25% → 1.06%. PaLM trained without dropout.
- Zhang et al. 2017, Table 2.5 values (Inception 1.65M: 100/89.05, 100/85.75, 100/9.78; AlexNet 1.39M: 99.90/81.22, 100/76.07, 99.82/9.86); "neither necessary nor by itself sufficient".
- Nakkiran et al.: 15% label noise, "even quadrupling" the data can hurt. Lee et al.: "ten times less frequently", "over 4% of the validation set".
- Geirhos 2020 definition of shortcuts (p. 665). Geirhos 2019: 95.9% shape for humans, 22.1% for ResNet-50, "Indian elephant" at 63.9%.
- Recht et al.: drops of 3–15 points (CIFAR-10) and 11–14 points (ImageNet). Goodfellow et al. 2015: panda 57.7% → gibbon 99.3%, ε = 0.007; adversarial error 89.4% → 17.9%, clean error 0.94% → 0.84%. ε·m·n = 0.007 × 0.01 × 150,528 ≈ 10.5.
- Kirkpatrick et al. quotation. Beniaguev et al.: 5–8 layers, one hidden layer without NMDA. Azevedo: 86 billion neurons. Pakkenberg: 0.15 × 10^15 neocortical synapses; 1.5 × 10^14 / 1.6 × 10^12 ≈ 94, so "about a hundred times". Lillicrap quotation (p. 335). Yamins et al. (IT and V4).
- Cross-references: Section 1.7 (AlexNet, ImageNet); Section 2.4 rule of thumb; Chapter 4 6N rule; Section 7.1 (8-bit formats are covered at ch07.md:34–41); ch03 refers back to Sections 2.1, 2.3, 2.5 and 2.6, and ch09, ch10 and ch12 refer to Section 2.8 for AUC. All correct. DeepSeek-V4-Pro's 1.6T/49B agrees with ch03.md:451 and ch07.md:272. DeepSeek-V3 FLOP (ch07.md:9): 6 × 37B × 14.8T ≈ 3.3 × 10^24, consistent with the 6N rule here.
- All 77 citation keys used in ch02.md exist in bib/ch02.bib.

## Tally
Claims checked: 118, of which about 45 are recomputed arithmetic · confirmed: 115 · wrong: 0 · outdated: 0 · could not verify: 3
