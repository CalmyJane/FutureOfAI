# Review 7: Chapter 2 (textbook/chapters/ch02.md)

## Verdict
Ready to print. I recomputed every worked example and found no errors. The quotations and figures I checked match their sources. The 2026 material on DeepSeek-V4 matches the company's report and release notes. The exposition is clear and builds step by step, and the debate box is balanced. I found nothing that must change, and no non-taste item worth listing as SHOULD.

## MUST change before printing
None.

## SHOULD change
None.

## Could not verify
- *The New York Times*, 8 July 1958, p. 25 (line 3). The text cites the quotation as reproduced in Ananthaswamy 2024. The wording matches the widely reproduced text ("the embryo of an electronic computer ... will be able to walk, talk, see, write, reproduce itself and be conscious of its existence"). I did not see the page number in the original.
- Zech et al. 2018: the hospital-identification accuracies of 99.95% (NIH) and 99.98% (Mount Sinai) and their order (line 321). The paper is open access, but I did not open it in this round. The other figures in the box (158,323 images; 34.2%/1.2%/1.0%; AUC 0.861, 0.931 and 0.815) match the paper's abstract as I know it.
- The DeepSeek-V4-Flash official release on 31 July (line 228). The DeepSeek API news list has no item dated 31 July; the cited source for that date is the Hugging Face model card, which I did not open. The V4-Pro GA on 13 August 2026 and the preview in April 2026 are confirmed.

## Checked and confirmed
- Arithmetic, all recomputed in Python:
  - Figure 2.1: 0.2 and −0.3.
  - Table 2.1: every value and slope (sigmoid slope 0.2475 at 0.2; tanh slope 0.961).
  - The 26-parameter MLP.
  - The matrix-layer example: −3.4 and 1.8, giving (0, 1.8).
  - Table 2.2, XOR.
  - Softmax of (2, 1, 0.1): 0.659, 0.242 and 0.0986, with losses 0.417 and 2.317.
  - The one-weight example: slope −2.4, 0.3364, 0.44/0.88/0.0144, divergence at η = 0.5 (1.4 and 3.24), threshold 0.25.
  - Table 2.3 and the update in the nine-parameter box: new loss 0.3021, p = 0.7393, z = 1.0423.
  - Adam's first step: m₁ = −0.24, v₁ = 0.00576, step 0.001.
  - 0.25^10 ≈ 9.5×10^−7.
  - He initialisation: √(2/512) = 0.0625; 0.0256^10 ≈ 1.2×10^−16.
  - Convolution: 1,728 weights; 150,528 × 3,211,264 ≈ 4.8×10^11.
  - 2×1,024×4,096² ≈ 3.4×10^10; data reuse 2×4,096/3 ≈ 2,730.
  - H100: 1,979/3.35 ≈ 590 (dense ≈ 295).
  - Adversarial total: 0.007×0.01×150,528 ≈ 10.5.
  - 1.5×10^14 / 1.6×10^12 ≈ 94, so "about a hundred".
- DeepSeek-V4: arXiv 2606.19348 (submitted 26 April 2026), "DeepSeek-V4-Pro with 1.6T parameters (49B activated)", with Muon as the main optimiser; V4-Pro GA on 13 August 2026 (api-docs.deepseek.com/news/news260813).
- The AlexNet, ResNet and Transformer recipes in Table 2.4. The ResNet top-1 errors in Figure 2.4 (27.94/28.54 plain; 27.88/25.03 residual). The "16 to 30 layers" and the 1,202-layer network.
- Glorot & Bengio: the "successfully trained" and "unsuited for deep networks with random initialization" quotations. He et al.: a 30-layer network "completely stalls" under Glorot initialisation.
- Batch normalisation's "14 times fewer training steps". Santurkar et al.: "has little to do with the success" and "significantly smoother". The AdamW quotation. Adam's defaults and the "trust region" passage.
- Goyal et al.: 8,192 images, 256 GPUs, one hour, five warm-up epochs. Transformer warm-up over 4,000 steps.
- Zhang et al. 2017, Table 2.5: values and quotation. Nakkiran et al.: 15% label noise and "even quadrupling" the data. Lee et al.: "ten times less frequently" and "over 4%".
- Geirhos 2019: 95.9%, 22.1% and 63.9% "Indian elephant". Goodfellow et al. 2015: panda 57.7%, gibbon 99.3%, ε 0.007, 89.4%→17.9% and 0.94%→0.84%. Recht et al.: drops of 3–15 and 11–14 points.
- Dropout: 0.5/0.8 retention and MNIST 1.60/1.25/1.06%. LeNet-5: 0.35%/0.95% error and about 60,000 parameters. AlexNet: augmentation factor 2,048, the six-times-faster ReLU result and the "waiting for faster GPUs" quotation.
- Raina et al. 2009: a 100-million-parameter network, training time cut from weeks to about a day. H100 SXM specifications (67 TF FP32; 1,979 TF FP16 with sparsity; 3.35 TB/s).
- About 86 billion neurons (Azevedo 2009). 0.15×10^15 neocortical synapses (Pakkenberg 2003). The Beniaguev et al. 5–8 layers and the NMDA result.
- Kimi K2: about 1T total and 32B active parameters, a constant learning rate for 10T tokens, then cosine decay, and Muon with an attention-logit safeguard.
- Internal consistency with Chapter 1: AlexNet's 60M parameters on two GPUs for 5–6 days, ResNet's 152 layers and the 2006 layer-wise pre-training match. The cross-references (Sections 1.7, 2.2–2.7, 7.1 on number formats, Chapters 3, 4 and 12) point to the right places.

## Tally
Claims checked: 80 / confirmed: 77 / wrong: 0 / outdated: 0 (3 could not be verified)
