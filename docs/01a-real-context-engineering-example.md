# Real Example: Context Engineering in a Multi-Agent Framework

This example uses **Microsoft Agent Framework (MAF)**, but the same applies to LangGraph, CrewAI, AutoGen, or any multi-agent system.

---

## How a framework passes context between agents

When you define a workflow with multiple agents, each agent gets a message object (TurnContext, thread, etc.). The framework controls what's inside it:

```
User message
    ↓
Orchestrator receives: [system_prompt + user_message + tool_schemas]
    ↓
Orchestrator decides: "Route to Research Agent"
    ↓
Research Agent receives: [its_own_system_prompt + orchestrator's_summary + tool_schemas]
    ↓                     ← framework-managed context
Research Agent returns result
    ↓
Orchestrator receives: [system_prompt + user_message + research_result + tool_schemas]
    ↓
Orchestrator synthesizes response
```

**Key:** when the orchestrator hands off to the Research Agent, it doesn't pass the entire conversation. The framework serializes a **subset** — usually the orchestrator's last message or a structured handoff object. The Research Agent never sees the original user message unless the framework (or your code) explicitly includes it.

---

## Concrete example: Code Review Workflow

Three agents:

```
Agent 1: Security Reviewer  →  system prompt: "Find security issues"
Agent 2: Performance Reviewer →  system prompt: "Find perf issues"
Agent 3: Synthesizer         →  system prompt: "Combine reviews"
```

The framework calls Agent 1 with:

```json
{
  "messages": [
    {"role": "system", "content": "You are a security reviewer..."},
    {"role": "user", "content": "Review this code: <the code>"}
  ],
  "tools": [...]
}
```

Then calls Agent 2 with the **same structure** — its own system prompt + the code. Agent 2 **never sees Agent 1's findings**. They work in parallel.

Then Agent 3 gets:

```json
{
  "messages": [
    {"role": "system", "content": "You synthesize code reviews..."},
    {"role": "user", "content": "Security findings: <agent1 output>\nPerf findings: <agent2 output>"}
  ]
}
```

**Who decided that Agent 3 sees both outputs concatenated as a single user message?** The framework did. You didn't write that serialization — the handoff/routing logic assembled it.

---

## Where context engineering comes in

Context engineering is when you **take control** of what each agent sees instead of accepting the framework's defaults:

| Default (framework manages) | Context-engineered (you manage) |
|---|---|
| Agent 3 gets raw concatenated outputs from Agents 1 & 2 | You summarize outputs into structured JSON before passing to Agent 3 |
| Each agent gets the full code file | You extract only the relevant functions for each agent's scope |
| Conversation history grows unbounded | You compress older turns into a summary to stay within token limits |
| Tool schemas are always included | You dynamically include only the tools relevant to the current step |

---

## The problem you'll hit in production

Your code review workflow works fine on 50-line files. On a 2000-line file, Agent 3 gets:

- Agent 1's output: ~800 tokens
- Agent 2's output: ~800 tokens
- The original code: ~6000 tokens
- System prompt: ~400 tokens

That's 8K+ tokens, and the synthesis quality drops because the model is drowning in context.

**Context engineering fix:** Before calling Agent 3, strip the original code (it was already reviewed), keep only the line-specific findings, and structure them:

```json
{
  "security": [
    {"line": 42, "issue": "SQL injection via string concat", "severity": "high"}
  ],
  "performance": [
    {"line": 87, "issue": "N+1 query in loop", "severity": "medium"}
  ]
}
```

Agent 3 now gets 200 tokens of structured data instead of 7600 tokens of noise. Output quality improves dramatically.

---

## The takeaway

In MAF (and LangGraph, CrewAI, etc.), the framework gives you **plumbing** — message routing, tool execution, agent lifecycle. But it makes **default choices** about what context each agent sees. Those defaults work for demos. In production, you override them — and that's context engineering.
