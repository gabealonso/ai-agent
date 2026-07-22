"""Tests for the agent builder. The live build is skipped without API keys."""

import os

import pytest

from agents.ai_agent import create_agent, generate_thread_id


def test_generate_thread_id_is_unique():
    ids = {generate_thread_id() for _ in range(100)}
    assert len(ids) == 100


@pytest.mark.skipif(
    not (os.getenv("OPENAI_API_KEY") and os.getenv("TAVILY_API_KEY")),
    reason="needs OPENAI_API_KEY and TAVILY_API_KEY to build the live agent",
)
def test_create_agent_builds():
    agent = create_agent()
    assert agent is not None
