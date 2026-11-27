# Review 8: Chapter 2, How Neural Networks Learn

## Verdict
Ready to print. I recomputed every worked example and all of them are correct: the neuron, the layer, softmax and cross-entropy, one-weight gradient descent and divergence, the nine-parameter backpropagation and its update, Adam's first step, vanishing gradients, the He initialisation variance, the convolution parameter counts, the matrix-multiplication operation counts, the H100 arithmetic intensity, the adversarial linearity estimate and the synapse comparison. The 2026 material on DeepSeek-V4 matches its sources. Two minor precision fixes are suggested.

## MUST change before printing
None.

## SHOULD change

### S1. The 1,202-layer ResNet was trained on CIFAR-10, not ImageNet
- Where: textbook/chapters/ch02.md:206
- Text now: "On ImageNet, the residual 34-layer network beat the residual 18-layer one, reversing the plain-network result. A 152-layer residual network helped win the 2015 competition (Section 1.7). Even a 1,202-layer network showed "no optimization difficulty", although it overfitted [@he2016deep]."
- Problem: UNCLEAR. The paragraph opens "On ImageNet", so it reads as if the 1,202-layer result was on ImageNet. In He et al. (2016) the 1,202-layer network appears in the CIFAR-10 experiments (Sec. 4.2).
- Evidence: He et al., "Deep residual learning for image recognition" (CVPR 2016), Sec. 4.2, CIFAR-10: "Exploring Over 1000 layers ... this 10^3-layer network ... no optimization difficulty".
- Change to: "... Even a 1,202-layer network, tested on the smaller CIFAR-10 dataset, showed "no optimization difficulty", although it overfitted [@he2016deep]."

### S2. "both keeping the preview's structure" is not supported for V4-Flash-0731
- Where: textbook/chapters/ch02.md:228
- Text now: "Released as a preview in April 2026, with official versions of the smaller V4-Flash on 31 July and of V4-Pro on 13 August, both keeping the preview's structure."
- Problem: UNSUPPORTED. The V4-Flash-0731 model card says the release supersedes the preview and "comes with a speculative decoding module attached". That is an addition to the structure, which the card does not describe as unchanged. DeepSeek has also since released V4.1-Flash (10 Sept 2026), which the box does not mention. That is not an error, but "official versions" implies these are the latest.
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731 (accessed 27 Nov 2026): "superseding the preview version"; "it comes with a speculative decoding module attached". https://api-docs.deepseek.com/news/news260813: DeepSeek-V4-Pro GA, 13 Aug 2026; news list includes "DeepSeek-V4.1-Flash (2026/09/10)".
- Change to: "Released as a preview in April 2026, with official versions of the smaller V4-Flash on 31 July and of V4-Pro on 13 August."

## Could not verify
- That DeepSeek-V4 keeps AdamW for the embedding, output and normalisation weights (line 228). The arXiv abstract mentions only Muon; the full paper was not read.
- The LeNet "per month / per day" discrepancy in LeCun et al. 1998 (line 3). Not re-read.
- Zech et al. (2018) figures (158,323 images; 34.2/1.2/1.0%; AUC 0.861, 0.931, 0.815; 99.95/99.98%). These match my recollection of the paper but were not re-fetched.

## Checked and confirmed
- Recomputed: z = 0.2 (and −0.3 for inputs 1,1). Layer outputs −3.4 and 1.8, giving (0, 1.8). Table 2.1: σ values 0.119/0.5/0.55/0.881, slope 0.248; tanh slope 0.961. Softmax 0.659/0.242/0.0986; losses 0.417 and 2.317. One-weight example: 0.36, −2.4, 0.3364, 0.44 → 0.0144; η = 0.5 gives 1.4 and 3.24; factor 1−8η; divergence above 0.25. Nine-parameter network: every value in Table 2.3, the updated weights, and the new loss 0.3021 (p = 0.7393). Adam: m₁ = −0.24, v₁ = 0.00576, step 0.001. 0.25^10 ≈ 9.5×10^−7. He: √(2/512) = 0.0625; 0.0256^10 ≈ 1.2×10^−16. Convolution: 1,728 weights; fully connected 150,528 × 3,211,264 ≈ 4.8×10^11. 2×1024×4096² ≈ 3.4×10^10; reuse ≈ 2,731. H100: 1,979/3.35 ≈ 590, dense ≈ 295. Adversarial: 0.007×0.01×150,528 ≈ 10.5. 1.5×10^14 / 1.6×10^12 ≈ 94. Figure 2.2: 26 parameters. AlexNet augmentation ×2,048.
- DeepSeek-V4-Pro: "1.6T parameters (49B activated)" (arXiv 2606.19348); preview 24 April 2026; GA 13 Aug 2026 (DeepSeek news page). Kimi K2: 1T total / 32B active, constant learning rate for 10T tokens, then cosine.
- Nakkiran et al.: 15% label noise; "increasing (even quadrupling) the number of train samples" can hurt. Matches.
- Classical results checked: Rosenblatt 1958; AlexNet ReLU six times faster; Glorot quotations; He 30-layer "completely stalls"; BN "14 times fewer training steps"; ResNet top-1 errors 27.94/28.54/27.88/25.03; Goyal 8,192 images / 256 GPUs / 1 hour; Adam defaults; Table 2.4 recipes; Srivastava 1.60/1.25/1.06%; Zhang et al. table values; Lee et al. "ten times less frequently", "over 4%"; Geirhos 95.9%/22.1%/63.9%; Goodfellow panda 57.7%→99.3%, 89.4%→17.9%, 0.94%→0.84%; Recht 3–15 and 11–14 points; H100 SXM 67 TF FP32, 1,979 TF sparse, 3.35 TB/s.
- Balance: the frontier-recipe box covers Meta, DeepSeek and Moonshot because they published recipes. The closed developers (OpenAI, Google, Anthropic) are not favoured. No unfair tone towards any company.
- Consistency with Chapter 1: AlexNet, ResNet, LeNet and GPT-3 figures are identical in both chapters.

## Tally
Claims checked: 72 / confirmed: 67 / wrong: 0 / outdated: 0 / imprecise or unsupported: 2 (S1, S2) / unverifiable: 3
