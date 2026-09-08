"""Pricing agent — PLACEHOLDER.

Owner: Rea

Reads:  state["intake_result"]
Writes: state["pricing_result"]

Responsibility: consume the structured intake result, apply pricing logic and
reference data, and produce a structured pricing result.

Naming note: this file is the pricing *node*. The package ``pricing_agent`` is
the whole three-agent workflow, not this module.

Nothing is implemented yet. Replace the body below with your own logic; you own
the shape of the ``pricing_result`` payload, so you should not need to edit
state.py to do it.
"""

from pricing_agent.state import QuotationState


def pricing_node(state: QuotationState) -> dict:
    """Return a partial state update containing only ``pricing_result``."""
    return {
        "pricing_result": {
            "status": "not_implemented",
            "saw_intake": state.get("intake_result") is not None,
        }
    }
