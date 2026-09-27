# LinkedIn — borrador (sep 2026)

## Headline

Technical Leader, AI Engineering @ Mercado Libre | Building with AI since 2023: LLMs in production, agentic systems, MCP | Fintech

## About

I build with AI the way a wizard practices magic: curiosity to try every new tool before it goes mainstream, creativity to push what it can do, and the technical discipline that makes it work in production.

For six years at Mercado Libre I have technically guided teams of up to 20 people and, since 2025, small expert teams amplified by AI. I have built with AI since it became commercially available. In 2023, as soon as the GPT-3.5 API made it viable, my team moved the categorization of financial transactions across Latin America from regex rules to LLMs, with every transaction anonymized before it reached a model: accuracy rose from 60% to 80% and costs fell 75%. In 2024 we brought that intelligence in-house for privacy and control: we distilled 18 billion transactions into 100K anonymized examples chosen by semantic similarity, had an LLM label them, and our own BERT-style embeddings now reach 90% accuracy on hundreds of millions of transactions a month in near real time, with no external API in the inference path. I told that story in "The New Financial Babel" on the Mercado Libre Tech blog and at PyCon Colombia 2025.

In 2025 came the next turn with agentic IDEs: Cursor, then Claude Code and Codex. Since July 2025 I lead AI engineering: spec-driven development, MCP servers, skills and plugins, and a GPU platform for tabular foundation models that turned three months of work by two senior data scientists into a single day for one, piloted by Financial Risk and Shipping teams who asked to keep building.

The discipline behind the magic:
• Determinism over prose: if a step can be a script, it does not belong in a prompt.
• No model is the source of truth: agents from different providers review each other, and every finding is checked against the code.
• Evals assert outcomes, and a test that passes without the fix proves nothing.
• Clean, hexagonal architecture is what lets agents implement a spec safely.
• Smallest intervention first: prompt optimization, then context, then RAG, then fine-tuning, each step only when the previous one falls short.

AI also goes beyond code for me: I use it to build the storytelling and impact presentations I take to senior leadership.

AI moves at a dizzying pace, and that is what I love about it: I keep up by building, putting every new model and protocol to work in my own projects first.

Focus: agentic engineering (Claude Code, Codex, MCP, skills, context engineering, RAG) · LLM and agent evaluation · tabular foundation models. Models: GPT since 3.5, Claude since 3.7, self-hosted Gemma 4.

## Experience 1 (nuevo puesto) — Technical Leader (AI Engineering) · Mercado Libre · Jul 2025 – Present

I lead small, project-based teams of expert engineers (backend, frontend, data science, data engineering). Amplified by AI, a few experts now go as far as a large team used to: that is the real impact of AI. Our standard way of building: spec-driven development on clean, hexagonal architectures, MCP and agentic IDEs (Claude Code, Codex, Cursor).

• Designed and implemented a GPU platform for tabular foundation models (TabPFN, TabICL, Mitra, TabDPT) on datasets of millions of rows: model development that took two senior data scientists three months now takes one a single day, with comparable ROC AUC, KS and F1. Its hexagonal architecture is what made spec-driven development with agents work. Financial Risk and Shipping teams piloted it and requested continued development.
• Designed a secure MCP gateway that lets AI agents operate internal services on behalf of users, with token-based identity, fail-closed authorization and prompt-injection protection.
• Leading the evolution of our multi-agent development platform from a workflow into an agent, in the sense Anthropic and OpenAI define it (the model directs its own tool use in a loop until the goal is met): deterministic code for mechanical steps, autonomous loops for open-ended ones, and one plugin for Claude Code and Codex used by hundreds of engineers. After evaluating PydanticAI and codex-rs, chose PydanticAI as the agent loop: it covered what the platform was missing and integrates natively with our Python and FastAPI backend.
• Built the team's agentic tooling (context engineering, skills, plugins and hooks) and ran experiments with autonomous agent loops and goal-driven runs, several with positive results for production use.
• Raised the bar for AI evaluation: fixed a statistical bug in a shared LLM-as-judge library, rebuilt a PII-classification benchmark free of data leakage, and made outcome-based agent evaluations the team standard.

## Experience 2 (editar el puesto actual) — Technical Leader (Machine Learning, Fintech) · Mercado Libre · Apr 2022 – Jun 2025

Technically guided a multidisciplinary team of up to 20 (ML engineers, data scientists, data engineers) building ML and GenAI solutions for Mercado Pago on clean, hexagonal architectures.

• Financial Data Enrichment: a GenAI platform that categorizes financial transactions across LATAM for Open Finance, saving $1.2M USD per month.
• 2023: moved it from regex rules to LLMs as soon as the GPT-3.5 API made it viable. I owned the anonymization, so no transaction reached a model with personal data. Accuracy from 60% to 80%, operational cost down 75%, throughput from tens of millions of transactions per quarter to tens of millions per week.
• 2024: brought it in-house for privacy and control. Normalized and anonymized 18B transactions into 5M unique descriptions, sampled 100K by semantic similarity to cover the full space, had GPT-4o-mini label them for under $10 USD, and our own BERT-style embeddings replaced the external API in the inference path; accuracy reached 90% with a further 30% cost cut, under 100 ms per transaction, hundreds of millions of transactions per month in near real time.
• Deployed async and near-real-time ML services at 100K RPM, p95 200 ms, 99.97% uptime.
• Shared the work publicly: "The New Financial Babel" (Mercado Libre Tech blog, Jul 2025) and a talk at PyCon Colombia 2025.

## Roles anteriores (reemplazar la descripción actual por estas versiones cortas)

### Sr Machine Learning Engineer · Mercado Libre · Oct 2020 – Mar 2022
ML for logistics and fintech: estimation models that cut errors by 30% and saved $3.2M USD per month in billing, and data pipelines 8x faster and cheaper.

### Sr Data Engineer · Global Hitss · Nov 2019 – Oct 2020
Near-real-time data products for marketing: measured the impact of prepaid campaigns, cutting end-user contact by 32% without affecting conversion.

### Business Intelligence Analyst · Tigo Colombia · Jun 2015 – Nov 2019
Demand forecasting and regression models for customer service that raised agent productivity by 27%.

### Quality Analyst · Tigo Colombia · Jul 2013 – Jun 2015 / Computer Programming Teacher · 2010
Sin descripción; considerar ocultar el puesto de profesor (2010) para enfocar el perfil.

## Featured (sección Destacados)

• Artículo: The New Financial Babel: Teaching AI to Speak Money in LATAM — https://medium.com/mercadolibre-tech/la-nueva-babel-financiera-ense%C3%B1ar-a-la-ia-a-hablar-dinero-en-latinoam%C3%A9rica-4605235e3aac
• Charla: Fine-tuning with LLMs: Control and Privacy in Financial NLP (PyCon Colombia 2025) — https://2025.pycon.co/#/talks/22 (y subir el PDF de la presentación).
• Certificación: Generative AI Leader, Google (Jul 2026).

## Projects (sección Proyectos) — 3 entradas

### Agent-first income-tax engine (2026)
An income-tax calculation engine built to be used by AI agents, not just people. Hexagonal / DDD backend in Python (FastAPI, async SQLAlchemy) with a 6-stage explainable calculation pipeline and legal parameters versioned by year, so a new tax year needs no code changes. Exposed to agents through a remote MCP server secured with OAuth 2.1 (standard discovery and dynamic client registration), where the user's identity always comes from the token, never from the agent's input, plus user consent and audit trails.
Skills: Model Context Protocol (MCP) · FastAPI · Domain-Driven Design · OAuth

### LLM Wiki: personal knowledge base on Karpathy's pattern (2026)
A personal knowledge base of about 100 pages built on Andrej Karpathy's LLM Wiki pattern and maintained by AI agents across many sessions. To keep an LLM-written system consistent without trusting the model to remember the rules, every check lives in code: a deterministic linter wired into agent lifecycle hooks gives each figure a declared owner, marks a page stale when its inputs change, and blocks the session from closing while the change log is out of date. To study how others use the pattern, I tested a specialized classifier (Jev) for routing content: validated against a blind gold set first, then classified 917 community comments for USD 0.05 and kept the 51 with real, non-promotional experience.
Skills: Context Engineering · AI Agents · LLM Evaluation · Python

### Operating manual for coding agents (2026)
A shared rulebook for my agents in Claude Code and Codex: every claim is labeled verified, deduced or assumed; conclusions are re-derived by an independent path before delivery; and the agent attacks its own answer before handing it over. It turns agent output from plausible into auditable.
Skills: Claude Code · Codex · Prompt Engineering

### Model and harness lab (2023 – present)
Hands-on across model families to know what each one is good for: OpenAI GPT from 3.5 to GPT-6 Astra, Anthropic Claude from Claude 3.7 Sonnet to current Opus, Sonnet and Haiku, and Google Gemini. Deployed self-hosted small models (Gemma 4 26B MoE and E4B), tested GLM-5.3, and ran the Claude Code harness on self-hosted models to measure where local inference is enough and where it is not. Next on the ladder: fine-tuning an LLM (supervised fine-tuning with LoRA adapters, then preference or reward-based post-training such as DPO or GRPO), as soon as a use case needs more than prompts, context and RAG can give.
Skills: Large Language Models (LLM) · Small Language Models · Claude Code

## Skills (publicado 2026-09-27)

Top skills (Acerca de): AI Agents · Large Language Models (LLM) · Generative AI · Model Context Protocol (MCP) · Technical Leadership

Agregadas (24), asociadas a los puestos de Technical Leader: AI Agents, Large Language Models (LLM), Generative AI, Model Context Protocol (MCP), Retrieval-Augmented Generation (RAG), Natural Language Processing (NLP), Large Language Model Operations (LLMOps), MLOps, Context Engineering, Software Architecture, Domain-Driven Design (DDD), Hexagonal Architecture, FastAPI, Claude Code, Transformer Models, Fine Tuning, Model Evaluation, Google Cloud Platform (GCP), Kubernetes, Docker, Apache Kafka, Spec-Driven Development, Storytelling, Executive Presentations.

Eliminadas (21): Matlab, Microsoft Excel, Visual Basic for Applications (VBA), COPC, Customer Service, Redes informáticas, Time Management, TeamWork, Prioritize Workload, Logical Approach, Adaptability, Persuasion, Team Motivation, Analytical Reasoning, Data Extraction, Databases, Tableau, Business Intelligence (BI), Investigación y desarrollo, Management, Decision-Making.

Python: se conservó "Python (Programming Language)" (nombre estándar) con las asociaciones de la skill "Python" (9 certificados y cursos) más el puesto de IA y 2 proyectos; "Python" se eliminó. Total: 51 skills.
