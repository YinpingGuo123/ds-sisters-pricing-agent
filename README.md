# ds-sisters-pricing-agent

A small multi-agent quotation workflow built for an AI course. A customer RFQ
goes through three specialized agents and comes out as a quotation.

This is an MVP for learning, not a production system.

## Workflow

```
START -> intake -> pricing -> quotation -> END
```

The graph is strictly linear for now. Conditional routing (clarification loops,
repricing, validation failures, human escalation) may be added later.

## Who owns what

Each of us owns one agent. Work only in your own file unless we agree otherwise.

| Agent | Responsibility | Your file | Owner |
| --- | --- | --- | --- |
| Intake | Extract and normalize the RFQ into a structured result | `src/pricing_agent/agents/intake.py` | Yinping |
| Pricing | Apply pricing logic to the intake result | `src/pricing_agent/agents/pricing.py` | Rea |
| Quotation | Validate and produce the final quotation, or flag for review | `src/pricing_agent/agents/quotation.py` | Jenny |

> Naming note: the package `pricing_agent` is the **whole workflow**. The pricing
> agent specifically is `agents/pricing.py`.

## Tools

Tools and helper functions live in `src/pricing_agent/tools/`, one module per
agent, named to match `agents/`:

| Your agent | Your tools file |
| --- | --- |
| Intake | `src/pricing_agent/tools/intake.py` |
| Pricing | `src/pricing_agent/tools/pricing.py` |
| Quotation | `src/pricing_agent/tools/quotation.py` |

**These files do not exist yet — create yours when you have something to put in
it.** Same filename as your agent means same owner, so there is no extra rule to
remember.

### Not everything should be an LLM tool

- A **tool** is exposed to the model, which decides whether and how to call it.
- A **helper** is a plain function your node calls directly in Python.

Default to plain helpers. Deterministic logic — pricing math, validation rules —
should not go through the model: it stays reproducible, and it is the part of
this project actually worth unit-testing. Expose a real tool only when the model
genuinely needs to choose, such as looking up an unfamiliar product mentioned in
free-text RFQ.

If two agents end up needing the same tool (customer lookup is the likely one),
put it in `tools/shared.py` and treat it as a shared file — see below.

## Shared files — coordinate with the team before changing

These are the files all three of us depend on. Changing them can break the other
two, so raise it in the group chat first and merge it as its own small PR.

| File | What it does |
| --- | --- |
| `src/pricing_agent/state.py` | The `QuotationState` contract passed between agents |
| `src/pricing_agent/graph.py` | Wires the three nodes into the LangGraph flow |
| `src/pricing_agent/config.py` | Loads `.env`, resolves which model each agent uses |
| `src/pricing_agent/tools/shared.py` | Tools used by more than one agent (does not exist yet) |
| `pyproject.toml` | Dependencies |

They are not frozen — the contract will need to evolve once we pick the domain.
Just agree the change first.

## Setup

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
Copy-Item .env.example .env
```

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

The `pip install -e ".[dev]"` step is **required** — the package lives under
`src/`, so without it every import fails with `ModuleNotFoundError`.

Then fill in your own values in `.env` (it is gitignored — never commit it).
Set `DEFAULT_MODEL` to use one model everywhere, or set `INTAKE_MODEL` /
`PRICING_MODEL` / `QUOTATION_MODEL` to give an agent its own.

## Run

```bash
python -m pricing_agent
```

Runs the whole graph on `data/test_cases/sample_rfq.json` and prints the final
state. Every agent currently returns `{"status": "not_implemented"}` — that is
expected; it proves the wiring works before any logic exists.

## Test

```bash
pytest
```

`tests/test_graph.py` checks that the three agents still fit together;
`tests/test_config.py` checks the model fallback.

## Working together

Branch off `main`, one branch per agent:

- `feature/intake-agent`
- `feature/pricing-agent`
- `feature/quotation-agent`

Open a Pull Request before merging to `main`, and have one teammate look at it.
Keep PRs small.

Before changing anything in **Shared files** above, or adding a dependency, or
committing a notebook, check with the team first.

## Status

The industry, dataset, and detailed schemas are still being decided. See
[data/README.md](data/README.md) for how data is organized and what comes next.
