# Glossary: Chapter 5

**AI agent**: A system in which a model pursues a goal by choosing actions, carrying them out through tools, observing the results and repeating. It is usually built from a model, a set of tools, a control loop and some form of memory.
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
