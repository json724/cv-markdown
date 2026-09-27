# JAISON ANDRES GONZALEZ DE LA TORRE

**AI Engineering Technical Leader | Agentic Systems, MCP, Spec-Driven Development | ML for Fintech**

Colombia | jaison.gonzalezd@gmail.com | +57 300 7354355 | linkedin.com/in/json724

Languages: Spanish (native); English (advanced technical reading, spoken English in active training)

## Summary

Technical leader with 13 years in data and machine learning, the last 6 at Mercado Libre, technically guiding teams of up to 20 people. I have built with AI since it became commercially available: in 2023 I put LLMs into production to categorize financial transactions across Latin America, and in 2024 distilled them into in-house embeddings serving hundreds of millions of transactions a month in near real time. Since July 2025 I lead AI engineering: spec-driven development on clean, hexagonal architectures, MCP servers and agentic workflows, including a platform that turned three months of modeling work into a single day. Hands-on with OpenAI and Anthropic models since GPT-3.5 and Claude 3.7, and with self-hosted small models behind agent harnesses. I also use AI beyond code, to build the storytelling and impact presentations I take to senior leadership. Curiosity for new tools, paired with the technical discipline that makes them work in production.

## Experience

### AI Engineering Technical Leader | Mercado Libre

Jul 2025 - Present | Colombia

- Technically guide a team of up to 20 through the transition from classic ML to AI engineering, adopting spec-driven development, clean (hexagonal) architecture, the Model Context Protocol (MCP) and agentic IDEs (Claude Code, Codex, Cursor) as our standard way of building.
- Designed and implemented a GPU platform for tabular foundation models (TabPFN, TabICL, Mitra, TabDPT) on datasets of millions of rows: model development that took two senior data scientists three months now takes one a single day, with comparable ROC AUC, KS and F1. Its hexagonal architecture is what made spec-driven development with agents work. Financial Risk and Shipping teams piloted it and requested continued development.
- Designed a secure MCP gateway that lets AI agents operate internal services on behalf of users, with token-based identity, fail-closed authorization and prompt-injection protection.
- Leading the evolution of a multi-agent development platform, used by hundreds of engineers through one plugin for Claude Code and Codex, from a workflow into an agent: deterministic code for mechanical steps and a PydanticAI agent loop for open-ended ones, chosen over codex-rs because it covered the missing loop and integrates natively with our FastAPI backend.
- Built the team's agentic tooling (context engineering, skills, plugins and hooks) and ran experiments with autonomous agent loops and goal-driven runs, several with positive results for production use.
- Raised the bar for AI evaluation: fixed a statistical bug in a shared LLM-as-judge library, rebuilt a PII-classification benchmark free of data leakage, and made outcome-based agent evaluations the team standard.
- Designed a GPU capacity allocation system and led guardrails for its AI recommender after data showed the agent, not the users, was over-sizing hardware requests.

### Machine Learning Technical Leader, Fintech | Mercado Libre

Jan 2022 - Jun 2025 | Colombia

- Technically guided a multidisciplinary team of up to 20 (ML engineers, data scientists, data engineers) building ML and GenAI solutions for Mercado Pago on clean, hexagonal architectures.
- Financial Data Enrichment, a GenAI platform that categorizes financial transactions across LATAM for Open Finance and saves $1.2M USD per month. In 2023, as soon as the GPT-3.5 API made it viable, moved it from regex rules to LLMs, owning the anonymization so no transaction reached a model with personal data: accuracy from 60% to 80%, operational cost down 75%, throughput from tens of millions of transactions per quarter to tens of millions per week.
- Brought it in-house for privacy and control (2024): normalized and anonymized 18B transactions into 5M unique descriptions, sampled 100K by semantic similarity for GPT-4o-mini labeling (under $10 USD) and trained our own BERT-style embeddings; accuracy reached 90% with a further 30% cost cut, under 100 ms per transaction and hundreds of millions of transactions per month in near real time.
- Deployed async and near-real-time ML systems with 99.97% uptime, p95 latency of 200 ms and 100K RPM capacity.

### Senior Machine Learning Engineer | Mercado Libre

Oct 2020 - Dec 2021 | Colombia

- Developed and productionized ML solutions for logistics optimization, reducing estimation errors by 30% and generating $3.2M USD in monthly billing savings.
- Optimized data pipelines, reducing ETL execution time and cost by 8x.

### Earlier Experience

- Senior Data Engineer | Global Hitss (Claro Colombia) | Nov 2019 - Oct 2020: measured the impact of prepaid campaigns, reducing end-user contact by 32% without affecting conversion.
- Business Intelligence Analyst | Tigo Colombia | Jun 2015 - Nov 2019: demand forecasting and regression models that raised customer-service agent productivity by 27%.
- Quality Analyst | Tigo Colombia | Jul 2013 - Jun 2015.

## Talks and Writing

- "The New Financial Babel: Teaching AI to Speak Money in LATAM", Mercado Libre Tech blog on Medium (Jul 2025).
- "Fine-tuning with LLMs: Control and Privacy in Financial NLP", PyCon Colombia 2025, Medellin, co-presented with Jonny Jimenez (2025.pycon.co/#/talks/22).

## Independent AI Work (Continuous Learning)

- Agent-first income-tax engine: hexagonal / DDD backend with an explainable calculation pipeline, exposed to AI agents through a remote MCP server secured with OAuth 2.1, user consent and audit trails.
- Personal knowledge base on Andrej Karpathy's LLM Wiki pattern (about 100 pages), kept consistent by a deterministic linter wired into agent hooks; tested a specialized classifier for routing content against a blind gold set (917 documents for USD 0.05).
- Operating manual for my coding agents across Claude Code and Codex: every claim labeled verified, deduced or assumed, and conclusions re-derived by an independent path before delivery.

## Skills

- AI and Agentic Engineering: Claude Code, Codex, Cursor, Model Context Protocol (MCP), skills and plugins, prompt optimization, context engineering, RAG, fine-tuning of BERT-style transformers, autonomous agent loops, multi-agent orchestration, cross-model review, spec-driven development, agent hooks, LLM evaluation (LLM-as-judge, scenario evals, golden fixtures), prompt-injection defense, PydanticAI, AI-assisted storytelling and executive presentations.
- Models: OpenAI GPT (GPT-3.5 to GPT-6 Astra), Anthropic Claude (Claude 3.7 Sonnet to current Opus, Sonnet and Haiku), Google Gemini, self-hosted small models (Gemma 4 26B MoE and E4B), GLM-5.3; Claude Code harness running on self-hosted models.
- Machine Learning and Data: tabular foundation models (TabPFN, TabICL, Mitra, TabDPT), GPU serving, Python, Pandas, NumPy, TensorFlow, PyTorch, deep learning, statistical and predictive models, SQL, NoSQL, ETL/ELT, BigQuery, Teradata.
- Backend and Architecture: FastAPI, asyncio, Pydantic, SQLAlchemy, REST, gRPC, hexagonal architecture, domain-driven design, idempotency, state machines, eventual consistency, security hardening; Kubernetes, Docker, GCP, AWS, Terraform, Kafka, Redis, DynamoDB.

## Certifications

Generative AI Leader, Google (Jul 2026); Ignite: Dev to Technical Lead, Lidr (May 2022); Deep Learning Specialization, Coursera (Aug 2021); Data Science for All (DS4A) Colombia, Graduated with Honors, Correlation One and MinTIC (Dec 2019).

## Education

BSc Electronic Engineering | Universidad del Norte, Barranquilla | 2008 - 2013 | Full academic scholarship
