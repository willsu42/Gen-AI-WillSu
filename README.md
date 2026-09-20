# Gen-AI-WillSu

**Yu-Chen (Will) Su** — applied Generative AI projects and coursework: multi-agent systems, RAG-style tool use, LLM evaluation/guardrails, MCP integrations, and full-stack AI apps.

## Skills demonstrated

| Area | Tools / Frameworks |
|---|---|
| Agent orchestration | LangGraph, AutoGen, CrewAI |
| Tool use & retrieval | Tavily/Brave search, Semantic Scholar API, n8n, HTTP/XML pipelines |
| LLM ops | LLM-as-judge evaluation, safety guardrails, Groq, prompt engineering |
| Protocols & dev tooling | Model Context Protocol (MCP), Chrome DevTools MCP |
| Voice | Text-to-speech / speech-to-text pipelines |
| Full-stack | Next.js, TypeScript, Tailwind, Radix UI, PostgreSQL, Vercel |

## Capstone / team project

| Project | Description | Stack |
|---|---|---|
| [Sentinel — NCEI Threat Intelligence Platform](https://github.com/IS492-SP26/team-project-deepfakes) | Team capstone: a living archive that tracks deepfake ("nudify") incidents with structured metadata — attack vector, model used, bypass method — for researchers and policy advocates. Scrapers feed an LLM parsing layer that extracts structured incidents into a searchable dashboard. | Python scrapers, Llama 3, PostgreSQL, Next.js, deployed on Vercel |

## Course assignments

| Project | Description | Stack |
|---|---|---|
| [Multi-Agent Research System](Assignment-3-building-multi-agent-systems-willsu42-1/) | A deep-research assistant for HCI topics: multiple AutoGen agents plan, search the web and academic papers, cite sources, and pass output through input/output safety guardrails and an LLM-as-judge evaluator. Ships with both a CLI and a Streamlit UI. | AutoGen, Tavily/Brave, Semantic Scholar, Streamlit |
| [n8n AI Research Agent](Assignment2-n8n_AI_Agent/) | A scheduled n8n workflow that pulls new papers from the arXiv API, parses the XML feed, summarizes them with a Groq-hosted LLM chain, and logs results to Slack and Google Sheets. | n8n, Groq, arXiv API |
| [Be a Video Director](Assignment1-VideoDirector/) | An AI-assisted video essay on a CHI 2024 paper about generative AI and design fixation, built end-to-end with an AI content pipeline: research/summarization, scripting, slides, avatar narration, and editing. | ChatGPT, NotebookLM, HeyGen, ElevenLabs |

## Labs

| Lab | Description | Stack |
|---|---|---|
| [Lab 7 — Multi-Agent Systems: AutoGen vs. CrewAI](lab-7-multi-agent-systems-willsu42/) | Same problem class, two architectures side by side: a conversational AutoGen GroupChat for product planning, and a task-based CrewAI crew for trip planning, comparing communication and orchestration styles. | AutoGen, CrewAI |
| [Lab 6 — Chrome DevTools MCP](lab-6-mcp-chrome-devtools-willsu42/) | Connects an AI agent to a live browser via the Chrome DevTools MCP server so it can inspect console errors, network traffic, DOM state, and performance metrics to debug a real running app instead of guessing from static code. | Model Context Protocol, Chrome DevTools |
| [Lab 5 — LLM Evaluation & Guardrailing](lab-5-eval-guardrailing-willsu42/) | Hands-on notebook on evaluating LLM outputs and building safety guardrails around them. | LLM-as-judge, safety evaluation |
| [Lab 4 — TTS/STT Voice Assistant](lab-4-tts-stt-willsu42/) | A voice assistant built by chaining speech-to-text and text-to-speech models into a conversational loop. | TTS, STT |
| [Lab 3 — Building Agents with LangGraph](lab-3-building-agent-with-langgraph-willsu42/) | Graph-based agent orchestration fundamentals using LangGraph. | LangGraph |
| [Lab 2 — Full-Stack Dev](lab-2-fullstack-dev-willsu42/) | A full-stack web app scaffold covering modern front-end fundamentals. | Next.js, TypeScript, Tailwind, Radix UI |

## Repo structure

```
Gen-AI-WillSu/
├── team-project-deepfakes/                              # separate repo, capstone (linked above)
├── Assignment-3-building-multi-agent-systems-willsu42-1/
├── Assignment2-n8n_AI_Agent/
├── Assignment1-VideoDirector/
├── lab-2-fullstack-dev-willsu42/
├── lab-3-building-agent-with-langgraph-willsu42/
├── lab-4-tts-stt-willsu42/
├── lab-5-eval-guardrailing-willsu42/
├── lab-6-mcp-chrome-devtools-willsu42/
└── lab-7-multi-agent-systems-willsu42/
```
