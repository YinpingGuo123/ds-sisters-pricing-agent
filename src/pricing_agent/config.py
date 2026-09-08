"""Environment and model configuration.

SHARED FILE — coordinate with the team before changing.

Each of us uses our own local ``.env`` (copy ``.env.example``). No model name is
hard-coded here: which model an agent uses is entirely an environment decision,
so the team can run all three agents on the same model or on different ones
without touching any code.
"""

import os

from dotenv import load_dotenv

load_dotenv()


def get_model(agent: str) -> str | None:
    """Return the model name configured for ``agent``.

    Resolution order:
      1. ``<AGENT>_MODEL``  (e.g. ``PRICING_MODEL``) — per-agent override
      2. ``DEFAULT_MODEL``  — shared across all agents
      3. ``None``           — nothing configured

    ``None`` means "not configured". There is no default model name on purpose.
    Whoever writes the first real LLM call should decide how to handle it
    (raise a clear error, or prompt the user).
    """
    return os.getenv(f"{agent.upper()}_MODEL") or os.getenv("DEFAULT_MODEL")


def get_api_key() -> str | None:
    """Return the OpenAI API key from the environment, or None if unset."""
    return os.getenv("OPENAI_API_KEY")
