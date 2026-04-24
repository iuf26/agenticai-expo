# How Reasoning Works in LLMs — Explained Simply

⏱️ **Estimated reading time: 4 minutes**

## Contents

- [Start with what an LLM actually does](#start-with-what-an-llm-actually-does)
- [So where does "reasoning" come from?](#so-where-does-reasoning-come-from)
- [The Chain-of-Thought trick](#the-chain-of-thought-trick)
- [Reasoning models (o1, o3, DeepSeek-R1) — what changed?](#reasoning-models-o1-o3-deepseek-r1--what-changed)
- [The honest summary](#the-honest-summary)
- [References](#-references)

> Before diving into agents, tools, and skills — it helps to understand how the brain behind it all actually works.

---

## Start with what an LLM actually does

An LLM is a **next-word predictor**. That's it. Given everything that came before, it predicts the most likely next word (token). It does this one word at a time, over and over.

```
Input:  "The capital of France is"
Output: "Paris" (highest probability next token)
```

---

## So where does "reasoning" come from?

Here's the key insight: **reasoning is an emergent behavior of next-token prediction at scale.**

Nobody programmed "if someone asks a math question, do math." Instead, the model was trained on billions of examples of humans reasoning — textbooks, StackOverflow answers, research papers, step-by-step solutions. It learned the *pattern* of reasoning.

When you ask it to solve a problem, it's essentially doing:

> "Based on everything I've seen, what would a helpful, step-by-step answer look like here? What word comes next in that kind of answer?"

---

## The Chain-of-Thought trick

Early LLMs would jump straight to the answer and often get it wrong. Then researchers discovered something simple:

**If you tell the model to "think step by step," it gets dramatically better.**

Why? Because when it generates intermediate steps, each step becomes part of the context for the *next* token prediction. It's literally giving itself a scratchpad.

| Without chain-of-thought | With chain-of-thought |
|---|---|
| "What's 17 × 24?" → "408" (often wrong on harder math) | "What's 17 × 24? Let me think step by step. 17 × 20 = 340. 17 × 4 = 68. 340 + 68 = **408**" |

The model isn't "thinking" the way you do. It's generating tokens that look like thinking, and those tokens improve the quality of the tokens that follow.

---

## Reasoning models (o1, o3, DeepSeek-R1) — what changed?

Regular LLMs: trained to predict the next token from human text.

**Reasoning models**: trained with reinforcement learning to generate *internal chains of thought* before answering. They were rewarded for getting the right answer, so they learned to "think longer" on hard problems.

| Regular LLM | Reasoning Model |
|---|---|
| Reads the question → immediately starts writing the answer | Reads the question → writes a long internal "scratchpad" → then writes the answer |
| Fast, but can miss complex logic | Slower, but much better at multi-step problems |
| Like answering in a conversation | Like solving on a whiteboard first, then presenting |

---

## The honest summary

- LLMs don't "understand" or "think" the way humans do.
- They predict tokens based on patterns learned from training data.
- "Reasoning" emerges because they've seen so many examples of reasoning that they can replicate the pattern convincingly — and usefully.
- Chain-of-thought and reasoning models make this better by giving the model more "space to work" before committing to an answer.
- The bigger the model and the better the training, the more complex reasoning it can sustain — which is exactly why 2025 models can plan across 50+ tool calls while 2023 models lost the plot after 3.

> **An analogy:** Imagine you're taking an exam but you're only allowed to write one word at a time, left to right, no going back. If you jump straight to the answer, you'll mess up. But if you write out your work first, each step guides the next. That's what chain-of-thought does for an LLM — it's not smarter, it just has more room to "show its work."

---

## 📚 References

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models — Wei et al.](https://arxiv.org/abs/2201.11903)
- [OpenAI — Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/)

---

**Next:** [Section 1 — The Evolution of AI →](01-evolution-of-ai.md)
