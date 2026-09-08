"""Tests for the model-selection fallback in config.py."""

from pricing_agent.config import get_model


def test_per_agent_model_wins(monkeypatch):
    monkeypatch.setenv("DEFAULT_MODEL", "shared-model")
    monkeypatch.setenv("PRICING_MODEL", "pricing-specific-model")

    assert get_model("pricing") == "pricing-specific-model"


def test_falls_back_to_default_model(monkeypatch):
    monkeypatch.setenv("DEFAULT_MODEL", "shared-model")
    monkeypatch.delenv("PRICING_MODEL", raising=False)

    assert get_model("pricing") == "shared-model"


def test_returns_none_when_nothing_configured(monkeypatch):
    monkeypatch.delenv("DEFAULT_MODEL", raising=False)
    monkeypatch.delenv("INTAKE_MODEL", raising=False)

    assert get_model("intake") is None
