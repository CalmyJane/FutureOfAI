# Glossary: Chapter 5

**AI agent**: A system in which a language model pursues a goal by choosing actions, carrying them out through tools, observing the results and repeating, with some form of memory between steps.
**workflow (agentic)**: A system in which language models and tools are combined along fixed, programmer-defined steps, as opposed to an agent that chooses its own steps.
**ReAct**: An agent design in which a language model alternates written reasoning (thoughts), tool calls (actions) and the returned results (observations).
**tool use**: The ability of a language model to request that external software (such as a search engine, calculator or code interpreter) be run and to use the result in its answer.
**function calling**: A feature of model interfaces in which developers describe available functions and the model replies with a structured request naming a function and its arguments; the surrounding application decides whether to execute it.
**Model Context Protocol (MCP)**: An open standard, released by Anthropic in 2024 and now governed under the Linux Foundation, that lets AI applications (clients) connect to data sources and tools (servers) through one common interface.
**Agent2Agent (A2A)**: An open protocol, launched by Google in 2025 and now hosted by the Linux Foundation, that lets AI agents from different vendors discover each other's capabilities and exchange tasks.
**computer-use agent**: An agent that operates a graphical computer interface as a person would, by reading screenshots and controlling the pointer and keyboard.
**SWE-bench**: A benchmark of real problems taken from open-source Python projects on GitHub, in which an AI system must change the code so that hidden tests pass; SWE-bench Verified is a human-screened subset of 500 problems.
**compounding error**: The decline in end-to-end success when a task needs many steps that must all succeed; with independent steps, overall success equals the per-step success rate multiplied by itself once per step.
**pass^k**: A reliability measure giving the probability that an agent succeeds on the same task in all k independent attempts, as opposed to pass@k, which asks whether at least one of k attempts succeeds.
**prompt injection**: An attack in which text supplied to a language model contains instructions that try to override the instructions of the system's developer or user.
**indirect prompt injection**: Prompt injection in which the malicious instructions are hidden in content the system retrieves, such as a web page, document or email, rather than typed by the user.
**lethal trifecta**: Simon Willison's term for the combination of access to private data, exposure to untrusted content and the ability to communicate externally, which together allow injected instructions to leak data.
**multi-agent system**: A system in which several AI agents, with the same or different owners, interact by exchanging messages, tasks or transactions.
**collusion (between agents)**: Cooperation among AI agents that their owners or society did not intend and that harms others, one of three multi-agent failure types identified by Hammond and colleagues (with miscoordination and conflict).
**permeability (of agent economies)**: The degree to which value and effects flow between an economy of transacting AI agents and the wider human economy; Tomašev and colleagues treat it as a key design choice.
**plan-then-execute**: An agent design in which the full list of actions is fixed from the user's request before any external data is read, so that retrieved content cannot change which actions run.
**context engineering**: The practice of deciding which information enters a model's limited context window at each step, using techniques such as compaction (summarising a long transcript), structured notes kept outside the window and sub-agents.
**JSON-RPC**: A widely used format for remote procedure calls, in which requests and responses are JSON objects naming a method, its parameters and an identifier; MCP and A2A use it.
**Agent Card**: In the A2A protocol, a machine-readable JSON document, typically published at a standard web address, that describes an agent's identity, endpoint, authentication requirements and skills.
**OSWorld**: A benchmark of 369 tasks in real operating systems used to measure computer-use agents; OSWorld-Verified is a corrected edition released in 2025.
**pass@k**: The probability that at least one of k attempts at a task succeeds; it suits settings where a test or a person can pick out the successful attempt.
**τ-bench**: A benchmark of simulated customer-service conversations (retail, airline and, in τ²-bench, telecom and banking) in which an agent must use tools and follow a written policy; it introduced the pass^k measure.
**adaptive attack**: An attack on a security defence that is deliberately tailored to the defence's design, as opposed to a fixed set of previously known attack inputs.
**mandate (AP2)**: In the Agent Payments Protocol, a cryptographically signed record of what a user authorised, such as the conditions for a purchase or a specific cart and price.
**x402**: An open protocol that uses the HTTP status code 402 "Payment Required" to let a client, including an AI agent, pay for a web resource within the same request.
**time horizon (50%)**: METR's measure of agent capability: the length of software task, timed on skilled humans, that an agent completes with 50% predicted success.
