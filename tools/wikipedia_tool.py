"""
Wikipedia Search Tool Module

This module provides a Wikipedia search tool for the AI agent.
It allows the agent to search for factual, encyclopedia-style information.
"""

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


def get_wikipedia_tool():
    """
    Create and configure a Wikipedia search tool.
    
    This tool is designed for:
    - General knowledge questions
    - Facts about people, places, animals, concepts
    - Historical information
    - Established factual information
    
    Returns:
        WikipediaQueryRun: Configured Wikipedia search tool
    """
    tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    tool.description = (
        "Use for general knowledge, facts about people/places/animals, "
        "historical information, or when user asks 'what is X' or 'who is X'."
    )
    return tool