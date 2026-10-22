**token**: The basic unit of text a language model reads and writes, usually a word, part of a word or a punctuation mark, each mapped to a fixed ID number. Prices and limits of language models are counted in tokens.
**embedding**: A learned list of numbers that represents a token (or other item) as a point in a high-dimensional space, so that items used in similar ways lie close together.
**next-token prediction**: The training task and generation method of most large language models: given the text so far, output a probability for every possible next token.
**self-supervised learning**: Training in which the answers come from the data itself, for example by hiding the next word of a text and asking the model to predict it, so that no human labelling is needed.
**temperature**: A setting that controls how random a language model's choices are; low temperatures concentrate probability on the most likely tokens, high temperatures spread it more evenly.
**attention**: A mechanism that lets each token's representation draw information from other tokens, weighted by how relevant each one is judged to be.
**transformer**: The neural-network architecture, introduced in 2017, that underlies modern language models; it stacks many blocks of attention and feed-forward layers.
**context window**: The maximum number of tokens a model can take into account at once, functioning as its working memory for a single request.
**pre-training**: The first and most expensive training stage, in which a model learns next-token prediction on a very large body of text and becomes a base model.
**instruction tuning**: Supervised fine-tuning of a pre-trained model on examples of instructions paired with good responses, so that it learns to follow requests.
**reinforcement learning from human feedback (RLHF)**: A post-training method in which people rank model outputs, a reward model learns their preferences, and the language model is then trained to produce outputs the reward model rates highly.
**Constitutional AI**: A post-training method developed at Anthropic in which a model critiques and revises its own outputs against a short list of written principles, and AI-generated preference judgements replace most human labels (reinforcement learning from AI feedback, RLAIF).
**hallucination**: A fluent but false or unsupported statement produced by a language model, such as an invented citation; the term is a metaphor, since the model perceives nothing.
**retrieval-augmented generation (RAG)**: A technique in which a system first searches a collection of documents and places the relevant passages in the model's context window before it answers.
**reasoning model**: A language model trained, usually with reinforcement learning on problems with checkable answers, to produce a long chain of intermediate reasoning before giving its final answer.
