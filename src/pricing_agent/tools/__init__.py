# Tools and helper functions used by the agents.
#
# Convention: one module per agent, named to match agents/. The owner of
# agents/pricing.py owns tools/pricing.py.
#
#     tools/intake.py      Yinping
#     tools/pricing.py     Rea
#     tools/quotation.py   Jenny
#
# None of them exist yet — create yours when you have something to put in it.
#
# Do not re-export anything here. If this file imported everyone's tools, every
# feature branch would have to modify it and we would get merge conflicts on
# every PR. Import directly from the module instead, e.g.
# `from pricing_agent.tools.pricing import calculate_price`.
#
# If two agents end up needing the same tool, put it in tools/shared.py and
# treat it as a shared file — coordinate with the team before changing it.
