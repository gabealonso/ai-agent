"""
AI Agent Configuration Module

This module configures and creates an AI agent with Wikipedia and Tavily search capabilities.
The agent uses LangChain with various language models and includes conversation memory.
"""

import os
import uuid
from langchain.chat_models import init_chat_model
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

# Import our custom tools
from tools.tavily_tool import create_tavily_tool
from tools.wikipedia_tool import create_wikipedia_tool

# Load environment variables
load_dotenv()


def create_agent(model_name="openai:gpt-4o-mini", max_results=5):
    """
    Create and configure the AI agent with both Wikipedia and Tavily search capabilities.
    
    Args:
        model_name (str): The language model to use (default: "openai:gpt-4o-mini")
        max_results (int): Maximum number of search results (default: 5)
    
    Returns:
        tuple: (agent_executor, memory) - The configured agent and memory saver
        
    Raises:
        ValueError: If required API keys are not set
    """
    # Initialize the language model
    model = init_chat_model(model_name)
    
    # Create both search tools
    tavily_tool = create_tavily_tool(max_results=max_results)
    wikipedia_tool = create_wikipedia_tool()
    
    # Combine tools - the agent will choose which one to use based on the query
    tools = [tavily_tool, wikipedia_tool]
    
    # Create prompt template for the agent
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful AI assistant with access to Wikipedia and Tavily search tools. 

IMPORTANT INSTRUCTIONS:
1. Always remember information the user shares with you (name, age, location, preferences, etc.)
2. When asked about the user's personal information, respond with what they told you
3. Use Wikipedia for detailed, factual information about people, places, historical events, and concepts
4. Use Tavily for current information, weather, news, and real-time data
5. Be conversational and friendly in your responses
6. If you don't need to search for information, just respond conversationally

Remember: The user's name, age, location, and other personal details they share are important to remember throughout the conversation."""),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    # Create the agent with memory
    agent = create_openai_functions_agent(model, tools, prompt)
    
    # Create memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    # Create agent executor with memory
    agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=False)
    
    return agent_executor, memory


def create_agent_with_custom_tools(model_name="openai:gpt-4o-mini", tools=None):
    """
    Create an agent with custom tools.
    
    Args:
        model_name (str): The language model to use
        tools (list): List of custom tools to use
    
    Returns:
        tuple: (agent_executor, memory) - The configured agent and memory saver
    """
    # Initialize the language model
    model = init_chat_model(model_name)
    
    # Use default tools if none provided
    if tools is None:
        tavily_tool = create_tavily_tool()
        wikipedia_tool = create_wikipedia_tool()
        tools = [tavily_tool, wikipedia_tool]
    
    # Create prompt template for the agent
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful AI assistant with access to search tools. Always remember information the user shares with you and be conversational."""),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    # Create the agent with memory
    agent = create_openai_functions_agent(model, tools, prompt)
    
    # Create memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    # Create agent executor with memory
    agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=False)
    
    return agent_executor, memory


def generate_thread_id():
    """
    Generate a unique thread ID using UUID.
    
    Returns:
        str: A unique thread ID
    """
    return str(uuid.uuid4()) 