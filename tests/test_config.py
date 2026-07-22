"""Tests for the configuration helpers (no API keys required)."""

import config


def test_provider_of():
    assert config.provider_of("openai:gpt-4o-mini") == "openai"
    assert config.provider_of("anthropic:claude-x") == "anthropic"
    assert config.provider_of("plainmodel") == "plainmodel"


def test_required_env_vars_for_openai():
    keys = config.required_env_vars("openai:gpt-4o-mini")
    assert "TAVILY_API_KEY" in keys
    assert "OPENAI_API_KEY" in keys


def test_required_env_vars_for_anthropic():
    keys = config.required_env_vars("anthropic:claude-x")
    assert "ANTHROPIC_API_KEY" in keys
    assert "TAVILY_API_KEY" in keys


def test_validate_config_reports_missing(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    errors = config.validate_config("openai:gpt-4o-mini")
    assert any("OPENAI_API_KEY" in e for e in errors)
    assert any("TAVILY_API_KEY" in e for e in errors)
