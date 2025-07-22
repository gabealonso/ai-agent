"""
Tavily Search Tool

This module provides a Tavily search tool for current information,
weather, news, stock prices, and real-time data.
"""

from langchain_tavily import TavilySearch
import os


def create_tavily_tool(max_results=5):
    """
    Create a Tavily search tool with custom configuration.
    
    Args:
        max_results (int): Maximum number of search results (default: 5)
    
    Returns:
        TavilySearch: Configured Tavily search tool
    """
    # Check if Tavily API key is available
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY environment variable is required")
    
    # Create the Tavily search tool
    search_tool = TavilySearch(max_results=max_results)
    
    # Set a descriptive name and description for the tool
    search_tool.name = "tavily_search"
    search_tool.description = (
        "Use this tool to search for CURRENT and REAL-TIME information from the web. "
        "SPECIFICALLY use this tool for: "
        "- Current weather conditions and forecasts "
        "- Breaking news and recent events "
        "- Live information and time-sensitive data "
        "- Current stock prices and financial data "
        "- Recent sports scores and results "
        "- Current traffic conditions "
        "- Live event information "
        "- Recent product releases or updates "
        "- Current political events and elections "
        "- Recent natural disasters or emergencies "
        "This tool provides the most up-to-date information available on the web. "
        f"Returns up to {max_results} current search results from Tavily."
    )
    
    return search_tool


def create_default_tavily_tool():
    """
    Create a Tavily tool with default settings.
    
    Returns:
        TavilySearch: Default Tavily search tool
    """
    return create_tavily_tool() 