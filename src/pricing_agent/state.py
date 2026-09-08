"""Shared state passed between the three agent nodes.

SHARED FILE — coordinate with the team before changing.

Conventions (please follow these; they are what let three people work in
parallel without stepping on each other):

1. ``total=False`` means every key is optional. The graph starts with only
   ``raw_request`` and each node fills in its own key as it runs. Always read
   downstream keys with ``state.get("intake_result")``, never
   ``state["intake_result"]`` — the key may not exist yet.

2. A node returns a *partial* dict, not the whole state. LangGraph merges the
   returned dict into the state for you.

3. Each node writes **only its own key**. Intake writes ``intake_result``,
   pricing writes ``pricing_result``, quotation writes ``quotation_result``.

4. The result payloads are typed loosely as ``dict[str, Any]`` on purpose. The
   shape of each payload is owned by that agent's module, so you can design and
   change your own payload without editing this file. When your schema settles,
   define a Pydantic model (or TypedDict) inside your own agent module and use
   it there.

The business domain and data model are still being decided, so this contract is
expected to evolve — just agree the change with the team first, since all three
agents depend on it.
"""

from typing import Any, TypedDict


class QuotationState(TypedDict, total=False):
    """State flowing through START -> intake -> pricing -> quotation -> END."""

    raw_request: str
    intake_result: dict[str, Any]
    pricing_result: dict[str, Any]
    quotation_result: dict[str, Any]
