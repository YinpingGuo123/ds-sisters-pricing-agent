# Project guidance

## What this is

A 3-person AI course MVP: a quotation workflow built as three LangGraph agents
(`START -> intake -> pricing -> quotation -> END`). It is for learning, not
production.

## How to work in this repo

- Keep implementations simple and readable. Prefer obvious code over clever code.
- Avoid overengineering: no premature abstractions, no speculative flexibility,
  no infrastructure that nothing needs yet.
- **Do not implement another owner's agent unless explicitly asked.** Each of the
  three agent modules in `src/pricing_agent/agents/` has a single owner.
- Each node writes only its own state key and returns a partial dict.

## Coordinate before changing

These are shared and all three members depend on them. Flag the change first
rather than editing them as a side effect of other work:

- `src/pricing_agent/state.py` — the state contract
- `src/pricing_agent/graph.py` — the workflow wiring
- `src/pricing_agent/config.py` — env and model resolution
- `pyproject.toml` — dependencies

They are expected to evolve; they just need agreement, not protection.

## Still being decided

The industry, the dataset, and the detailed business schemas are not chosen yet.

- Do not invent a dataset or assume an industry.
- Keep result payloads loosely typed (`dict[str, Any]`) until the domain settles;
  per-agent schemas belong in the agent's own module, not in `state.py`.
- No model name is hard-coded anywhere — models come from environment variables
  via `config.py`.

## Do not add unless asked

Provider SDKs, Langfuse, Streamlit, FastAPI, Docker, CI/CD, databases, MCP.
Committed notebooks also need team agreement — they merge badly.
