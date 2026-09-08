"""Contract test for the workflow skeleton.

This does not test anyone's business logic — it tests that the three agents
still fit together. If a change to state.py or graph.py breaks the contract the
other owners rely on, this test fails loudly.
"""

from pricing_agent.graph import build_graph


def test_graph_runs_end_to_end():
    """The graph starts with only raw_request and every node fills in its key."""
    graph = build_graph()

    final_state = graph.invoke({"raw_request": "test RFQ"})

    assert final_state["raw_request"] == "test RFQ"
    assert final_state["intake_result"] is not None
    assert final_state["pricing_result"] is not None
    assert final_state["quotation_result"] is not None


def test_state_flows_between_nodes():
    """Each node actually sees what the previous ones wrote, in order."""
    graph = build_graph()

    final_state = graph.invoke({"raw_request": "test RFQ"})

    assert final_state["intake_result"]["saw_raw_request"] is True
    assert final_state["pricing_result"]["saw_intake"] is True
    assert final_state["quotation_result"]["saw_intake"] is True
    assert final_state["quotation_result"]["saw_pricing"] is True
