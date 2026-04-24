# Career in AI — What the Work Actually Looks Like

⏱️ **Estimated reading time: 5 minutes**

## Contents

- [From Chatbots to Agentic AI to Skills](#from-chatbots-to-agentic-ai-to-skills)
- [AI Is Software Engineering](#ai-is-software-engineering)
- [AI Standards](#ai-standards)
- [How to Keep Up in a Fast-Changing AI World](#how-to-keep-up-in-a-fast-changing-ai-world)
- [What Can I Try Right Now? (It's Free)](#what-can-i-try-right-now-its-free)
- [Full Learning Path](#full-learning-path)

---

## From Chatbots to Agentic AI to Skills

AI evolved in stages: LLMs → RAG → Agentic AI → Multi-Agent Systems → Agent Skills. Each stage added new capabilities — from generating text, to retrieving real data, to taking actions, to agents working together.

📖 **Read more:** [The Evolution of AI](../docs/01-evolution-of-ai.md) · [Agent Concepts, Tools & MCP](../docs/02-agent-concepts-tools-mcp.md) · [Agent Skills](../docs/03-agent-skills.md)

---

## AI Is Software Engineering

AI is built on software engineering. APIs, modular design, dependency injection, event-driven architecture, orchestration — these patterns existed long before AI agents, and they're exactly what powers them now.

Companies want engineers who can build agents, design systems, write tests, and set up evaluation pipelines. Master software engineering first — AI follows naturally.

---

## AI Standards

Standards like the **Model Context Protocol (MCP)** define how agents connect to tools and how data flows between systems. Without them, every company builds something incompatible. With them, your skills transfer across tools, platforms, and employers.

📖 **Read more:** [Agent Concepts, Tools & MCP](../docs/02-agent-concepts-tools-mcp.md) · [Staying Current & Standards](../docs/04-staying-current-and-standards.md)

---

## How to Keep Up in a Fast-Changing AI World

Follow the organizations building the standards — Anthropic, Microsoft, OpenAI, Google, Meta. Their blogs, release notes, and open-source repos are where real trends appear first. Don't chase hype. Stay hands-on.

📖 **Read more:** [Staying Current & Standards](../docs/04-staying-current-and-standards.md)

---

## What Can I Try Right Now? (It's Free)

Everything below is **free** and takes about **30 minutes** to set up.

**1. Get GitHub Copilot** — As a student, you get **Copilot Pro for free** through the GitHub Student Developer Pack.

👉 **[Set up Copilot as a student](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)** — create your account right now.

**2. Install [VS Code](https://code.visualstudio.com/)** — Copilot works as a built-in extension. Once your GitHub account has Copilot enabled, it just works.

**3. Try your first Agent Skill in 2 minutes:**

Copy the [`cv-tailor` skill](../examples/cv-tailor-skill/SKILL.md) into your own project:

```
.github/copilot/skills/cv-tailor/SKILL.md
```

Open **Copilot Chat** (`Ctrl+Shift+I`), paste a job description, and ask:

> _"Here's a job posting for a Junior Software Engineer at Microsoft. Can you help me update my CV to match it?"_

Copilot will use the skill to walk you through tailoring your CV. **That's how simple agent skills are** — a Markdown file with structured knowledge.

📖 **How skills work:** [Agent Skills](../docs/03-agent-skills.md)

**4. Try the hands-on examples in this repo:**

| Example | What It Shows | Folder |
|---|---|---|
| **CV Tailor Skill** | An agent skill that tailors your CV to a job description | [`examples/cv-tailor-skill/`](../examples/cv-tailor-skill/) |
| **Skill Creator Skill** | A skill that helps you create new skills with best practices | [`examples/skill-creator-skill/`](../examples/skill-creator-skill/) |
| **Simple Tool Calling** | An LLM agent that calls Python functions as tools | [`examples/simple-tool-calling/`](../examples/simple-tool-calling/) |
| **MCP Weather Server** | A real MCP server that Copilot can connect to | [`examples/mcp-weather-server/`](../examples/mcp-weather-server/) |

**5. Go deeper** — read [how LLMs reason](../docs/00-how-llm-reasoning-works.md), build your own MCP server, or write more skills.

---

## Full Learning Path

| # | Section | Time |
|---|---|---|
| 0 | [How LLM Reasoning Works](../docs/00-how-llm-reasoning-works.md) | 4 min |
| 1 | [The Evolution of AI](../docs/01-evolution-of-ai.md) | 6 min |
| 2 | [Agent Concepts, Tools & MCP](../docs/02-agent-concepts-tools-mcp.md) | 5 min |
| 3 | [Agent Skills](../docs/03-agent-skills.md) | 9 min |
| 4 | [Staying Current & Standards](../docs/04-staying-current-and-standards.md) | 7 min |

**Total deep-dive time: ~31 minutes** — start wherever interests you most.

---

**Back to:** [Main README →](../README.md)
