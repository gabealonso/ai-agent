"""
AI Agent Configuration Module

Builds a LangGraph ReAct agent with Wikipedia and Tavily search tools and a
checkpointer for conversational memory. Each conversation is keyed by a
`thread_id` (see `generate_thread_id`): pass it in the invoke config and the
checkpointer keeps that thread's history automatically.
"""

import uuid

from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

import config
from tools.tavily_tool import create_tavily_tool
from tools.wikipedia_tool import create_wikipedia_tool


def create_agent(model_name: str = None, max_results: int = None):
    """
    Create and configure the AI agent with Wikipedia and Tavily search tools.

    @param model_name - Model in "provider:model" form; defaults to config.DEFAULT_MODEL.
    @param max_results - Max Tavily results; defaults to config.TAVILY_MAX_RESULTS.
    @returns The compiled LangGraph agent (memory handled by its checkpointer).
    """
    model_name = model_name or config.DEFAULT_MODEL
    max_results = max_results or config.TAVILY_MAX_RESULTS

    model = init_chat_model(model_name)
    tools = [
        create_tavily_tool(max_results=max_results),
        create_wikipedia_tool(max_results=config.WIKIPEDIA_MAX_RESULTS),
    ]

    # MemorySaver keeps each thread's history in-process for the session.
    checkpointer = MemorySaver()

    return create_react_agent(
        model,
        tools=tools,
        prompt=config.SYSTEM_PROMPT,
        checkpointer=checkpointer,
    )


def generate_thread_id() -> str:
    """
    Generate a unique conversation thread id.

    @returns A new UUID string to key a conversation's memory.
    """
    return str(uuid.uuid4())
