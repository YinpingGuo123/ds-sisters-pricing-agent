"""LangGraph workflow definition.

SHARED FILE — coordinate with the team before changing.

The flow is deliberately linear for now:

    START -> intake -> pricing -> quotation -> END

Later we may add conditional routing (clarification loops, repricing, validation
failure paths, human review / escalation). Those branches would attach here, but
they are intentionally not implemented yet — the linear version is what we need
to develop the three agents in parallel.
"""

from langgraph.graph import END, START, StateGraph

from pricing_agent.agents.intake import intake_node
from pricing_agent.agents.pricing import pricing_node
from pricing_agent.agents.quotation import quotation_node
from pricing_agent.state import QuotationState


def build_graph():
    """Build and compile the quotation workflow graph."""
    builder = StateGraph(QuotationState)

    builder.add_node("intake", intake_node)
    builder.add_node("pricing", pricing_node)
    builder.add_node("quotation", quotation_node)

    builder.add_edge(START, "intake")
    builder.add_edge("intake", "pricing")
    builder.add_edge("pricing", "quotation")
    builder.add_edge("quotation", END)

    return builder.compile()
