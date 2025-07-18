"""
AI Agent Configuration Module

This module configures and creates the main AI agent with Wikipedia and DuckDuckGo search capabilities.
The agent uses LangGraph with GPT-4o-mini model and includes conversation memory.
"""

import os
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools.wikipedia_tool import get_wikipedia_tool
from tools.duckduckgo_tool import get_duckduckgo_tool
from pydantic import SecretStr
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def build_agent_executor():
    """
    Build and configure the AI agent executor.
    
    This function:
    1. Initializes Wikipedia and DuckDuckGo search tools
    2. Configures the GPT-4o-mini model with appropriate settings
    3. Creates a LangGraph agent with tool binding
    4. Returns the configured agent executor
    
    Returns:
        AgentExecutor: Configured agent ready for conversation
        
    Raises:
        ValueError: If OPENAI_API_KEY environment variable is not set
    """
    # Initialize search tools
    wikipedia_tool = get_wikipedia_tool()
    duckduckgo_tool = get_duckduckgo_tool()
    tools = [wikipedia_tool, duckduckgo_tool]

    # Validate API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Environment variable OPENAI_API_KEY is not defined")

    # Configure the language model
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # Fast and cost-effective model
        temperature=0,        # Deterministic responses
        api_key=SecretStr(api_key)
    )

    # Bind tools to the language model
    llm_with_tools = llm.bind_tools(tools)

    # Create the agent executor
    agent_executor = create_react_agent(llm_with_tools, tools)

    return agent_executor
