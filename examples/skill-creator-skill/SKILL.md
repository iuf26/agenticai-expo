---
name: skill-creator
description: Helps create well-structured agent skills following best practices for the SKILL.md format.
---

# Skill Creator

## When to Use This Skill

Activate when the user:
- Wants to create a new agent skill
- Asks "how do I write a SKILL.md?"
- Wants to improve an existing skill file

## Knowledge

### What Makes a Good Skill

A skill is a structured Markdown file that gives an AI agent specialized expertise. The best skills share these traits:

1. **Clear trigger** — The agent knows exactly when to activate it
2. **Scoped knowledge** — Domain facts the LLM doesn't have (your conventions, your APIs, your patterns)
3. **Step-by-step workflow** — Not just "help the user" but a concrete sequence of actions
4. **Defined boundaries** — What the skill should NOT do is as important as what it should do

### SKILL.md Structure

```
---
name: short-kebab-case-name
description: One sentence explaining what the skill does.
---

# Skill Title

## When to Use This Skill
List specific triggers — user phrases, file patterns, or situations.

## Knowledge
Domain-specific facts, patterns, rules the LLM needs.
Organize with subheadings for different topic areas.

## Workflow
Step-by-step instructions for how the agent should handle requests.
Be specific — "Ask the user for X" not "Gather information."

## Rules
Constraints, boundaries, and things to avoid.

## Tools Available (optional)
Which tools the skill should use and when.
```

### Common Mistakes to Avoid

- **Too vague** — "Help the user with Docker" gives the agent nothing it doesn't already know
- **Too long** — Skills are injected into context. Every token counts. Be concise.
- **No workflow** — Knowledge without a workflow means the agent has facts but no process
- **Missing boundaries** — Without rules, the agent may over-reach or hallucinate scope

### Skill File Organization

```
my-skill/
├── SKILL.md           # Required: instructions, knowledge, workflow
├── references/        # Optional: API docs, specs, examples
├── scripts/           # Optional: helper scripts the skill can call
└── assets/            # Optional: templates, schemas
```

Most skills only need the SKILL.md file. Add extra folders only when the skill needs reference material the LLM wouldn't otherwise have.

## Workflow

When the user wants to create a skill:
1. Ask what domain or task the skill should cover
2. Ask for a concrete example: "What would you ask the agent to do?"
3. Draft the SKILL.md with frontmatter, triggers, knowledge, workflow, and rules
4. Review with the user — is the knowledge accurate? Is the workflow right?
5. Suggest where to place it:
   - `.github/copilot/skills/<name>/SKILL.md` for GitHub Copilot
   - `.agents/skills/<name>/SKILL.md` for cross-client compatibility
6. Test it: ask the agent a question that should trigger the skill

## Rules

- Always include the YAML frontmatter (`name` and `description`)
- Keep skills focused on ONE domain — split broad topics into separate skills
- Write knowledge sections with facts the LLM doesn't already know well
- Prefer concrete examples over abstract instructions
- Don't duplicate what the LLM already knows (e.g., don't explain what Python is)

## References

- [Agent Skills Specification](https://agentskills.io/home)
- [Compatible Clients](https://agentskills.io/clients)
- [GitHub — Custom Instructions for Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
