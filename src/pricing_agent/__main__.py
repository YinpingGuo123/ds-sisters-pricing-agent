"""Smoke test entry point: ``python -m pricing_agent``.

Runs the whole graph on one sample RFQ and prints the final state, so anyone can
confirm the workflow wires up correctly before any business logic exists.
"""

import json
from pathlib import Path

from pricing_agent.graph import build_graph

# data/ lives outside the package (src/pricing_agent/ -> src/ -> repo root), so
# resolve it from this file rather than the current working directory.
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
SAMPLE_RFQ = DATA_DIR / "test_cases" / "sample_rfq.json"


def main() -> None:
    sample = json.loads(SAMPLE_RFQ.read_text(encoding="utf-8"))

    graph = build_graph()
    final_state = graph.invoke({"raw_request": sample["raw_request"]})

    print(f"Ran sample: {sample['rfq_id']}\n")
    print(json.dumps(final_state, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
