"""
Configuration file for the AI Agent

This file contains all the configurable parameters for the AI agent,
making it easy to customize behavior without modifying the core code.
"""

import os
from typing import List, Optional

# Model Configuration
DEFAULT_MODEL = "openai:gpt-4o-mini"
AVAILABLE_MODELS = {
    "openai": [
        "openai:gpt-4o-mini",
        "openai:gpt-4o",
        "openai:gpt-3.5-turbo"
    ],
    "anthropic": [
        "anthropic:claude-3-5-sonnet-20241022",
        "anthropic:claude-3-haiku-20240307"
    ],
    "google": [
        "google:gemini-1.5-flash",
        "google:gemini-1.5-pro"
    ]
}

# Search Configuration
TAVILY_MAX_RESULTS = 5
WIKIPEDIA_MAX_RESULTS = 3

# Memory Configuration
MEMORY_TYPE = "memory_saver"  # Options: "memory_saver", "sqlite"

# Chat Configuration
CHAT_PROMPT = "You: "
AGENT_PROMPT = "Agent: "
MAX_CONVERSATION_LENGTH = 100  # Maximum number of messages to keep in memory

# Tool Selection Configuration
TOOL_SELECTION_STRATEGY = "intelligent"  # Options: "intelligent", "manual"

# Wikipedia Tool Keywords (queries containing these words will prefer Wikipedia)
WIKIPEDIA_KEYWORDS = [
    "who was", "biography", "history", "definition", "what is",
    "tell me about", "explain", "concept", "theory", "scientist",
    "inventor", "artist", "writer", "philosopher", "mathematician",
    "physicist", "chemist", "biologist", "geography", "country",
    "city", "landmark", "monument", "museum", "university",
    "company", "organization", "institution", "book", "movie",
    "film", "music", "album", "song", "painting", "sculpture"
]

# Tavily Tool Keywords (queries containing these words will prefer Tavily)
TAVILY_KEYWORDS = [
    "weather", "forecast", "temperature", "news", "latest",
    "current", "today", "recent", "breaking", "live",
    "stock", "price", "market", "trading", "crypto",
    "bitcoin", "ethereum", "sports", "score", "game",
    "election", "politics", "traffic", "accident", "disaster",
    "earthquake", "hurricane", "flood", "fire", "emergency",
    "product", "release", "update", "announcement", "event"
]

# Environment Variables
REQUIRED_ENV_VARS = ["TAVILY_API_KEY"]
OPTIONAL_ENV_VARS = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]

# Logging Configuration
LOG_LEVEL = "INFO"  # Options: "DEBUG", "INFO", "WARNING", "ERROR"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Performance Configuration
REQUEST_TIMEOUT = 30  # seconds
MAX_RETRIES = 3
RETRY_DELAY = 1  # seconds

# Output Configuration
STREAM_RESPONSES = True
SHOW_TOOL_CALLS = False  # Whether to show which tool was used
SHOW_THREAD_ID = True

# Conversation Management
AUTO_CLEANUP_OLD_CONVERSATIONS = True
CONVERSATION_CLEANUP_DAYS = 7  # Remove conversations older than this many days

# Error Handling
SHOW_DETAILED_ERRORS = False  # Set to True for debugging
GRACEFUL_DEGRADATION = True  # Continue with partial results if one tool fails


def get_model_config() -> dict:
    """
    Get the current model configuration.
    
    Returns:
        dict: Model configuration
    """
    return {
        "default_model": DEFAULT_MODEL,
        "available_models": AVAILABLE_MODELS,
        "current_model": os.getenv("DEFAULT_MODEL", DEFAULT_MODEL)
    }


def get_search_config() -> dict:
    """
    Get the current search configuration.
    
    Returns:
        dict: Search configuration
    """
    return {
        "tavily_max_results": TAVILY_MAX_RESULTS,
        "wikipedia_max_results": WIKIPEDIA_MAX_RESULTS,
        "wikipedia_keywords": WIKIPEDIA_KEYWORDS,
        "tavily_keywords": TAVILY_KEYWORDS
    }


def get_chat_config() -> dict:
    """
    Get the current chat configuration.
    
    Returns:
        dict: Chat configuration
    """
    return {
        "chat_prompt": CHAT_PROMPT,
        "agent_prompt": AGENT_PROMPT,
        "max_conversation_length": MAX_CONVERSATION_LENGTH,
        "stream_responses": STREAM_RESPONSES,
        "show_tool_calls": SHOW_TOOL_CALLS,
        "show_thread_id": SHOW_THREAD_ID
    }


def validate_config() -> List[str]:
    """
    Validate the current configuration.
    
    Returns:
        List[str]: List of validation errors (empty if valid)
    """
    errors = []
    
    # Check required environment variables
    for var in REQUIRED_ENV_VARS:
        if not os.getenv(var):
            errors.append(f"Missing required environment variable: {var}")
    
    # Check model configuration
    if DEFAULT_MODEL not in [model for models in AVAILABLE_MODELS.values() for model in models]:
        errors.append(f"Default model '{DEFAULT_MODEL}' not found in available models")
    
    # Check search configuration
    if TAVILY_MAX_RESULTS <= 0:
        errors.append("TAVILY_MAX_RESULTS must be greater than 0")
    
    if WIKIPEDIA_MAX_RESULTS <= 0:
        errors.append("WIKIPEDIA_MAX_RESULTS must be greater than 0")
    
    return errors


def print_config_summary():
    """
    Print a summary of the current configuration.
    """
    print("🔧 AI Agent Configuration Summary")
    print("=" * 40)
    print(f"Default Model: {DEFAULT_MODEL}")
    print(f"Tavily Max Results: {TAVILY_MAX_RESULTS}")
    print(f"Wikipedia Max Results: {WIKIPEDIA_MAX_RESULTS}")
    print(f"Memory Type: {MEMORY_TYPE}")
    print(f"Tool Selection: {TOOL_SELECTION_STRATEGY}")
    print(f"Stream Responses: {STREAM_RESPONSES}")
    print(f"Show Tool Calls: {SHOW_TOOL_CALLS}")
    print()
    
    # Check environment variables
    print("Environment Variables:")
    for var in REQUIRED_ENV_VARS:
        status = "✅" if os.getenv(var) else "❌"
        print(f"  {status} {var}")
    
    for var in OPTIONAL_ENV_VARS:
        status = "✅" if os.getenv(var) else "⚠️"
        print(f"  {status} {var}")
    
    print()
    
    # Validation
    errors = validate_config()
    if errors:
        print("❌ Configuration Errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✅ Configuration is valid!") 