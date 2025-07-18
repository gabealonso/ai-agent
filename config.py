"""
Configuration Module

This module contains all configuration settings for the AI agent application.
Centralizing configuration makes it easier to modify settings and maintain the code.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o-mini"
OPENAI_TEMPERATURE = 0

# Agent Configuration
RECURSION_LIMIT = 10
THREAD_ID_LENGTH = 36

# Tool Configuration
WIKIPEDIA_TOOL_DESCRIPTION = (
    "Use for general knowledge, facts about people/places/animals, "
    "historical information, or when user asks 'what is X' or 'who is X'."
)

DUCKDUCKGO_TOOL_DESCRIPTION = (
    "Use for current weather, recent news, real-time information, "
    "or time-sensitive data."
)

# System Prompt Configuration
SYSTEM_PROMPT = (
    "You are a helpful assistant with access to two tools: Wikipedia and DuckDuckGo web search. "
    "IMPORTANT: You must choose the MOST APPROPRIATE tool for each query. "
    "Use Wikipedia ONLY for: general knowledge, facts about people/places/animals/concepts, "
    "historical information, or when user asks 'what is X' or 'who is X'. "
    "Use DuckDuckGo ONLY for: current weather, recent news, real-time information, "
    "or time-sensitive data. NEVER use both tools for the same query. "
    "Choose ONE tool based on the type of information needed. "
    "Always remember the information the user shares with you during the conversation. "
    "When the user asks you about their name, respond with the name they previously told you."
)

# UI Configuration
SEPARATOR_LINE = "=" * 50
EXIT_COMMANDS = ['quit', 'exit', 'q']

# Name extraction patterns
NAME_PATTERNS = [
    "my name is",
    "i'm",
    "i am"
]

# Tool selection keywords
WEATHER_KEYWORDS = ["weather", "current", "today", "latest", "recent", "now"]
GENERAL_KNOWLEDGE_KEYWORDS = ["what is", "who is", "tell me about", "define", "explain"]

# Response formatting patterns
WIKIPEDIA_PATTERNS = ["wikipedia", "page:"]
WEB_SEARCH_PATTERNS = ["search", "duckduckgo", "weather", "oct", "jan", "sep", "2023", "2020", "·", "°c", "°f"] 