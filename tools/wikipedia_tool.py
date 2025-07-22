"""
Wikipedia Search Tool

This module provides a Wikipedia search tool for detailed, factual information
about people, places, historical events, and concepts.
"""

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


def create_wikipedia_tool(max_results=3):
    """
    Create a Wikipedia search tool with custom configuration.
    
    Args:
        max_results (int): Maximum number of search results (default: 3)
    
    Returns:
        WikipediaQueryRun: Configured Wikipedia search tool
    """
    # Create the Wikipedia API wrapper
    api_wrapper = WikipediaAPIWrapper()
    
    # Create the Wikipedia tool
    wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
    
    # Set a descriptive name and description for the tool
    wikipedia_tool.name = "wikipedia_search"
    wikipedia_tool.description = (
        "Use this tool to search for DETAILED, FACTUAL, and EDUCATIONAL information from Wikipedia. "
        "SPECIFICALLY use this tool for: "
        "- Biographies of historical figures and famous people "
        "- Historical events and their detailed explanations "
        "- Scientific concepts, theories, and definitions "
        "- Geographical information about countries, cities, and landmarks "
        "- Detailed explanations of complex topics and concepts "
        "- Information about books, movies, and cultural works "
        "- Academic subjects and educational content "
        "- Detailed information about animals, plants, and natural phenomena "
        "- Information about organizations, companies, and institutions "
        "- Detailed explanations of technologies and inventions "
        "This tool provides comprehensive, well-researched information from Wikipedia articles. "
        "Use this for learning, education, and detailed factual information."
    )
    
    return wikipedia_tool


def create_default_wikipedia_tool():
    """
    Create a Wikipedia tool with default settings.
    
    Returns:
        WikipediaQueryRun: Default Wikipedia search tool
    """
    return create_wikipedia_tool() 