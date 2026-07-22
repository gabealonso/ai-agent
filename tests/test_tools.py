"""Tests for the search tools (no API keys required)."""

import pytest

from tools.tavily_tool import create_tavily_tool
from tools.wikipedia_tool import create_wikipedia_tool


def test_wikipedia_tool_metadata():
    tool = create_wikipedia_tool()
    assert tool.name == "wikipedia_search"
    assert tool.description  # non-empty description guides tool selection


def test_tavily_requires_api_key(monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    with pytest.raises(ValueError):
        create_tavily_tool()
