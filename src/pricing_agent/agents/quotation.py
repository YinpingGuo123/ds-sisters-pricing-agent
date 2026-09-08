"""Quotation agent — PLACEHOLDER.

Owner: Jenny

Reads:  state["intake_result"], state["pricing_result"]
Writes: state["quotation_result"]

Responsibility: review and validate the intake and pricing results, then produce
the final quotation — or flag the case for human review.

Nothing is implemented yet. Replace the body below with your own logic; you own
the shape of the ``quotation_result`` payload, so you should not need to edit
state.py to do it.
"""

from pricing_agent.state import QuotationState


def quotation_node(state: QuotationState) -> dict:
    """Return a partial state update containing only ``quotation_result``."""
    return {
        "quotation_result": {
            "status": "not_implemented",
            "saw_intake": state.get("intake_result") is not None,
            "saw_pricing": state.get("pricing_result") is not None,
        }
    }
