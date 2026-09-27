# JAISON ANDRES GONZALEZ DE LA TORRE

**Technical Leader, AI Engineering | Agentic Systems, LLMs in Production, MCP | Fintech**

Colombia | jaison.gonzalezd@gmail.com | +57 300 7354355 | linkedin.com/in/json724

Languages: Spanish (native); English (advanced technical reading, spoken English in active training)

## Summary

AI engineering leader with 13 years in data and machine learning, 6 at Mercado Libre. I have shipped large language models (LLMs) to production since 2023, as soon as the GPT-3.5 API made it viable, and today I lead small expert teams that, amplified by AI agents, deliver what used to take large ones. I pair curiosity for every new model and tool with the discipline that makes them work in production: clean architecture, deterministic contracts around LLMs and evaluations that measure outcomes.

## Selected Impact

- 3 months to 1 day: my GPU platform for tabular foundation models lets one senior data scientist build in a day the models that took two seniors three months, with comparable ROC AUC, KS and F1.
- $1.2M USD saved per month by Financial Data Enrichment, the GenAI platform that categorizes financial transactions across LATAM: accuracy from 60% to 90% on hundreds of millions of transactions a month.
- Hundreds of engineers build with the multi-agent development plugin I lead for Claude Code and Codex.
- $3.2M USD per month in logistics billing savings from ML estimation models.
- 100K requests per minute, p95 latency of 200 ms and 99.97% uptime on near-real-time ML systems built for scalability.

## Experience

### Technical Leader (AI Engineering) | Mercado Libre

Jul 2025 - Present | Colombia

- Lead small, project-based teams of expert engineers (backend, frontend, data science, data engineering) through the shift from classic ML to AI engineering: spec-driven development on hexagonal architectures, MCP and agentic IDEs (Claude Code, Codex, Cursor).
- Built a GPU platform for tabular foundation models (TabPFN, TabICL, Mitra, TabDPT) that serves datasets of millions of rows synchronously and asynchronously through distributed job queues; its hexagonal design is what made spec-driven development with agents work. Financial Risk and Shipping piloted it and asked to scale it.
- Leading a multi-agent development platform, one plugin for Claude Code and Codex used by hundreds of engineers, from workflow to agent: deterministic code for mechanical steps and a PydanticAI agent loop for open-ended ones, chosen over codex-rs for its native fit with our FastAPI backend.
- Designed a secure MCP gateway that lets AI agents act on internal microservices on behalf of users, with token-based identity, fail-closed authorization and prompt-injection protection.
- Made AI evaluation trustworthy: fixed a statistical bug in a shared LLM-as-judge library that skewed A/B tests, rebuilt a leaky PII benchmark and made outcome-based agent evals the team standard; added guardrails to an AI hardware recommender once data showed the agent, not the users, was over-sizing requests.
- Push the frontier into production: context engineering, skills and hooks for the team's agents, and experiments with autonomous agent loops and goal-driven runs, several with positive results for production use.

### Technical Leader (Machine Learning, Fintech) | Mercado Libre

Apr 2022 - Jun 2025 | Colombia

- Technical leadership and mentoring of a team of up to 20 (ML engineers, data scientists, data engineers) building ML and GenAI for Mercado Pago on clean, hexagonal architectures, communicating strategy and outcomes to senior stakeholders.
- Put LLMs in production in 2023, as soon as the GPT-3.5 API made it viable: Financial Data Enrichment moved from regex rules to LLMs, with accuracy from 60% to 80%, 75% lower cost and throughput from tens of millions of transactions per quarter to tens of millions per week. I owned the anonymization, so no transaction reached a model with personal data.
- Brought it in-house in 2024 for privacy and control: distilled 18B transactions into 5M unique descriptions and 100K examples sampled by semantic similarity, labeled by GPT-4o-mini for under $10 USD, to train our own BERT-style embeddings: 90% accuracy, a further 30% cost cut and under 100 ms per transaction.
- Ran distributed, observable near-real-time ML systems at 100K RPM, p95 200 ms and 99.97% uptime.

### Senior Machine Learning Engineer | Mercado Libre

Oct 2020 - Mar 2022 | Colombia

- ML estimation models for logistics that cut errors by 30% and saved $3.2M USD per month in billing; data pipelines 8x faster and cheaper.

### Senior Data Engineer | Global Hitss (Claro Colombia)

Nov 2019 - Oct 2020 | Bogota, Colombia

- Near-real-time campaign analytics that cut end-user contact by 32% without affecting conversion.

### Business Intelligence Analyst | Tigo Colombia

Jun 2015 - Nov 2019 | Colombia

- Customer-service demand forecasting that raised agent productivity by 27%. Previously Quality Analyst (Jul 2013 - Jun 2015).

## Talks and Writing

- "The New Financial Babel: Teaching AI to Speak Money in LATAM", Mercado Libre Tech blog on Medium (Jul 2025).
- "Fine-tuning with LLMs: Control and Privacy in Financial NLP", PyCon Colombia 2025, Medellin, co-presented with Jonny Jimenez (2025.pycon.co/#/talks/22).

## Independent AI Work (Continuous Learning)

- Agent-first income-tax engine: hexagonal / DDD backend with an explainable calculation pipeline, exposed to AI agents through a remote MCP server secured with OAuth 2.1, user consent and audit trails.
- Personal knowledge base on Andrej Karpathy's LLM Wiki pattern, kept consistent by a deterministic linter wired into agent hooks; tested a specialized routing classifier against a blind gold set (917 documents for USD 0.05).
- Operating manual for my coding agents in Claude Code and Codex: every claim labeled verified, deduced or assumed, and conclusions re-derived by an independent path before delivery.
- Model lab: OpenAI GPT from GPT-3.5 to GPT-6 Astra, Anthropic Claude from 3.7 Sonnet to current Opus, Sonnet and Haiku, self-hosted Gemma 4 (26B MoE and E4B) and GLM-5.3, including the Claude Code harness on self-hosted models.

## Skills

- AI and Agentic Engineering: Claude Code, Codex, Cursor, Model Context Protocol (MCP), PydanticAI (agent loops and tool orchestration, the patterns LangGraph provides), spec-driven development, context engineering, prompt engineering and optimization, retrieval-augmented generation (RAG) and vector databases, skills, plugins and hooks, multi-agent orchestration, autonomous agent loops, cross-model review, LLM and agent evaluation (LLM-as-judge, scenario evals, golden fixtures), prompt-injection defense, fine-tuning of BERT-style transformers, AI-assisted storytelling for executive presentations.
- Machine Learning and Data: MLOps and LLMOps, tabular foundation models (TabPFN, TabICL, Mitra, TabDPT), GPU serving, NLP, embeddings, deep learning, statistical and predictive models, Python, PyTorch, SQL, BigQuery, ETL/ELT.
- Backend and Architecture: system design, distributed systems, microservices and APIs, observability, CI/CD, FastAPI, asyncio, Pydantic, SQLAlchemy, hexagonal architecture, domain-driven design, scalability, idempotency, state machines, eventual consistency, security hardening; Kubernetes, Docker, GCP, AWS, Terraform, Kafka.

## Certifications

Generative AI Leader, Google (Jul 2026); Ignite: Dev to Technical Lead, Lidr (May 2022); Deep Learning Specialization, Coursera (Aug 2021); Data Science for All (DS4A) Colombia, Graduated with Honors, Correlation One and MinTIC (Dec 2019).

## Education

BSc Electronic Engineering | Universidad del Norte, Barranquilla | 2008 - 2013 | Full academic scholarship
