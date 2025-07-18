"""
DuckDuckGo Web Search Tool Module

This module provides a DuckDuckGo web search tool for the AI agent.
It allows the agent to search for current, real-time information from the web.
"""

from langchain_community.tools import DuckDuckGoSearchRun


def get_duckduckgo_tool():
    """
    Create and configure a DuckDuckGo web search tool.
    
    This tool is designed for:
    - Current weather conditions and forecasts
    - Recent news and current events
    - Real-time information (stock prices, sports scores, etc.)
    - Time-sensitive data that changes frequently
    
    Returns:
        DuckDuckGoSearchRun: Configured web search tool
    """
    tool = DuckDuckGoSearchRun()
    tool.description = (
        "Use for current weather, recent news, real-time information, "
        "or time-sensitive data."
    )
    return tool 