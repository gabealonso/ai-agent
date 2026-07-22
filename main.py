"""
AI Agent Chat Application

A conversational interface to chat with an AI agent that can search using both
Wikipedia and Tavily, with per-conversation memory (LangGraph checkpointer).
"""

import os

from dotenv import load_dotenv

import config
from agents.ai_agent import create_agent, generate_thread_id

# Load environment variables
load_dotenv()


def setup_environment() -> bool:
    """
    Validate that the environment has the keys required for the default model.

    @returns True when everything required is present, False otherwise.
    """
    missing = [key for key in config.required_env_vars() if not os.getenv(key)]
    if missing:
        print(f"⚠️ Missing required environment variables: {', '.join(missing)}")
        print("Add them to your .env file (see .env.example). The agent needs:")
        for key in missing:
            print(f"  {key}=your-{key.lower().replace('_', '-')}")
        return False
    return True


def chat_with_agent(agent) -> None:
    """
    Run the interactive chat loop against the agent.

    @param agent - The compiled LangGraph agent.
    """
    print("Chat with Albert 1.0")
    print("=" * 40)
    print("Type 'quit' to exit, 'new' to start a new conversation")
    print("=" * 40)
    print()

    thread_id = generate_thread_id()

    while True:
        try:
            user_input = input(config.CHAT_PROMPT).strip()

            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            if user_input.lower() == "new":
                # A fresh thread id starts a new, empty conversation.
                thread_id = generate_thread_id()
                print("New conversation started.")
                print()
                continue

            if not user_input:
                print("Please enter a message.")
                continue

            # The checkpointer keeps this thread's history, so we only send the
            # new message; prior turns are recalled by thread_id.
            result = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]},
                config={"configurable": {"thread_id": thread_id}},
            )
            answer = result["messages"][-1].content
            print(f"{config.AGENT_PROMPT}{answer}")
            print()

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as error:
            print(f"\nError: {error}")
            print("Please try again.")


def main() -> None:
    """
    Application entry point: validate the environment, build the agent, chat.
    """
    print("Starting AI Agent...")

    if not setup_environment():
        return

    try:
        agent = create_agent()
        print("Agent is ready to chat!")
        print()
        chat_with_agent(agent)
    except Exception as error:
        print(f"Failed to start agent: {error}")
        print("Please check your configuration and try again.")


if __name__ == "__main__":
    main()
