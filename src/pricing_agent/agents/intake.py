"""Intake agent — PLACEHOLDER.

Owner: Yinping

Reads:  state["raw_request"]
Writes: state["intake_result"]

Responsibility: take the customer's raw RFQ text, extract and normalize the
information the pricing agent will need, and produce a structured intake result.
May later look up or enrich customer/product information.

Nothing is implemented yet. Replace the body below with your own logic; you own
the shape of the ``intake_result`` payload, so you should not need to edit
state.py to do it.
"""

from pricing_agent.state import QuotationState


def intake_node(state: QuotationState) -> dict:
    """Return a partial state update containing only ``intake_result``."""
    return {
        "intake_result": {
            "status": "not_implemented",
            "saw_raw_request": bool(state.get("raw_request")),
        }
    }
