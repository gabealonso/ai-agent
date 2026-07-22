"""
Configuration for the AI Agent.

Only settings that are actually used by the app live here, so this file is the
single source of truth for the agent's behavior. Import it wherever a value is
needed instead of hardcoding.
"""

import os
from typing import List

# --- Model ---------------------------------------------------------------

# Default model, in the "provider:model" form understood by init_chat_model.
DEFAULT_MODEL = "openai:gpt-4o-mini"

# Models known to work out of the box (langchain-openai is installed). Other
# providers also work with init_chat_model, but need their own package and API
# key — e.g. `pip install langchain-anthropic` + ANTHROPIC_API_KEY for
# "anthropic:...", or langchain-google-genai + GOOGLE_API_KEY for "google:...".
AVAILABLE_MODELS = [
    "openai:gpt-4o-mini",
    "openai:gpt-4o",
    "openai:gpt-3.5-turbo",
]

# Maps a model's provider prefix to the API key it needs.
PROVIDER_ENV_KEYS = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "google": "GOOGLE_API_KEY",
}

# --- Search --------------------------------------------------------------

TAVILY_MAX_RESULTS = 5
WIKIPEDIA_MAX_RESULTS = 3

# --- Agent behavior ------------------------------------------------------

SYSTEM_PROMPT = """You are a helpful AI assistant with access to Wikipedia and Tavily search tools.

IMPORTANT INSTRUCTIONS:
1. Always remember information the user shares with you (name, age, location, preferences, etc.)
2. When asked about the user's personal information, respond with what they told you
3. Use Wikipedia for detailed, factual information about people, places, historical events, and concepts
4. Use Tavily for current information, weather, news, and real-time data
5. Be conversational and friendly in your responses
6. If you don't need to search for information, just respond conversationally

Remember: The user's name, age, location, and other personal details they share are important to remember throughout the conversation."""

# --- Chat display --------------------------------------------------------

CHAT_PROMPT = "You: "
AGENT_PROMPT = "Agent: "


def provider_of(model_name: str) -> str:
    """
    Return the provider prefix of a "provider:model" name.

    @param model_name - A model name such as "openai:gpt-4o-mini".
    @returns The provider part ("openai"), or the whole string if there is no prefix.
    """
    return model_name.split(":", 1)[0]


def required_env_vars(model_name: str = DEFAULT_MODEL) -> List[str]:
    """
    Return the environment variables required to run with the given model.

    Tavily is always needed (the search tool); the model's provider key depends
    on which model is selected.

    @param model_name - The model the agent will use.
    @returns The list of required environment variable names.
    """
    keys = ["TAVILY_API_KEY"]
    provider_key = PROVIDER_ENV_KEYS.get(provider_of(model_name))
    if provider_key:
        keys.append(provider_key)
    return keys


def validate_config(model_name: str = DEFAULT_MODEL) -> List[str]:
    """
    Validate that the environment is ready to run with the given model.

    @param model_name - The model the agent will use.
    @returns A list of human-readable error strings (empty when everything is set).
    """
    errors = []
    for var in required_env_vars(model_name):
        if not os.getenv(var):
            errors.append(f"Missing required environment variable: {var}")
    if TAVILY_MAX_RESULTS <= 0:
        errors.append("TAVILY_MAX_RESULTS must be greater than 0")
    if WIKIPEDIA_MAX_RESULTS <= 0:
        errors.append("WIKIPEDIA_MAX_RESULTS must be greater than 0")
    return errors
