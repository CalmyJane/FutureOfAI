**emulator**: A machine-learning model trained to reproduce the outputs of a slower, more detailed simulation or measurement, so that approximate answers can be obtained much faster. Also called a surrogate model.
**multiple sequence alignment (MSA)**: A table that lines up the sequences of related proteins from many organisms position by position, so that positions which change together over evolution can be detected.
**Evoformer**: The main trunk of AlphaFold 2, 48 network blocks that repeatedly exchange information between a representation of the sequence alignment and a representation of every pair of residues.
**structure module**: The part of AlphaFold 2 that turns the network's internal representations into 3D coordinates, treating each residue as a rigid body that is moved into place.
**pLDDT**: AlphaFold's per-residue confidence score (predicted local distance difference test), an estimate of how accurate the local structure around each residue is likely to be.
**CASP**: The Critical Assessment of Structure Prediction, a community experiment in which protein-structure predictions are tested blind against unreleased experimental structures and scored by independent assessors.
**diffusion model**: A generative model that learns to turn random noise into a realistic sample, such as an image, a weather forecast or a set of atom positions, by removing the noise step by step; starting from different noise gives different samples.
**numerical weather prediction**: Forecasting the weather by solving the physical equations of the atmosphere on a computer, starting from an estimate of its current state.
**data assimilation**: The process of merging fresh observations with a model to produce the best estimate of the current state of a system, such as the atmosphere, from which a forecast starts.
**reanalysis**: A consistent reconstruction of past weather, made by combining historical observations with a fixed modern weather model; ECMWF's ERA5 is the standard example.
**graph neural network**: A neural network that works on data represented as nodes connected by edges, such as atoms linked by bonds in a crystal or points on a mesh covering the globe.
**root mean square error (RMSE)**: A measure of forecast error: the square root of the average squared difference between forecast and verifying values; lower is better.
**anomaly correlation coefficient (ACC)**: A measure of whether a forecast gets departures from normal weather right, from 1 (perfect) to 0 (no better than climatology).
**continuous ranked probability score (CRPS)**: A score for probabilistic forecasts that rewards a range of predicted outcomes centred on what happened and neither too narrow nor too wide.
**ensemble forecast**: A set of many forecasts made from slightly different starting points or with random variation, whose spread indicates how uncertain the forecast is.
**autoregressive rollout**: Producing a long forecast or sequence by feeding a model's own prediction back in as the next input, one step at a time.
**density functional theory (DFT)**: An approximate quantum-mechanical method for computing the energy of a material from its atomic structure; the standard way to check whether a predicted crystal is likely to be stable.
**convex hull**: In materials science, the lowest-energy combination of competing phases for a given overall composition; a compound on or below the hull is predicted to be stable.
**active learning**: A training loop in which a model chooses which new examples to have labelled (here, by DFT calculations) and is retrained on the results, round after round.
**reinforcement learning**: A way of training a system by trial and error, rewarding actions that lead to a desired outcome.
**proof assistant**: Software, such as Lean, in which mathematical statements and proofs are written precisely enough for a computer to check every step.
**formalisation**: Translating a mathematical statement or proof from ordinary language into the precise language of a proof assistant.
**test-time reinforcement learning**: AlphaProof's method of generating and learning from many variants of a hard problem while it is working on that problem.
**formal verification**: Checking by machine that a proof or program is correct with respect to a precise specification.
**AI scientist system**: An AI system that attempts to automate much of the research process, such as generating ideas, writing and running code, analysing results and drafting papers.
**comprehension debt**: The gap between how much code (or other output) exists in a system and how much of it any human genuinely understands, a term applied especially to AI-generated code.
**data leakage**: An error in which information from the test data influences a model's training, making its measured performance look better than it really is.
**illusions of understanding**: Messeri and Crockett's term for situations in which reliance on AI tools leads researchers to believe they understand more about the world than they actually do.
**scientific monoculture**: A state in which a few methods, questions or viewpoints dominate a field and crowd out alternatives, making it less innovative and more prone to shared errors.
**intellectual debt**: Zittrain's term for the accumulated cost of using answers that work without knowing why they work, on the assumption that the explanation will come later.
