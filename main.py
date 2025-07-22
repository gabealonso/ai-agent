"""
AI Agent Chat Application

This is a conversational interface to chat with an AI agent that can search
using both Wikipedia and Tavily, with conversational memory.
"""

import os
import uuid
from dotenv import load_dotenv
from agents.ai_agent import create_agent, generate_thread_id

# Load environment variables
load_dotenv()


def setup_environment():
    """
    Setup environment variables and validate required API keys.
    """
    # Check for required API keys
    required_keys = ["TAVILY_API_KEY"]
    optional_keys = ["OPENAI_API_KEY"]
    
    missing_required = []
    missing_optional = []
    
    for key in required_keys:
        if not os.getenv(key):
            missing_required.append(key)
    
    for key in optional_keys:
        if not os.getenv(key):
            missing_optional.append(key)
    
    if missing_required:
        print(f"⚠️ Missing required environment variables: {', '.join(missing_required)}")
        print("These are required for the agent to function:")
        for key in missing_required:
            if key == "TAVILY_API_KEY":
                print(f"  {key}=your-tavily-api-key")
        return False
    
    if missing_optional:
        print(f"⚠️ Missing optional environment variables: {', '.join(missing_optional)}")
        print("These are optional but recommended for better performance:")
        for key in missing_optional:
            if key == "OPENAI_API_KEY":
                print(f"  {key}=your-openai-api-key")
        print("The agent will work without these keys, but may have limited functionality.")
    
    return True


def format_message(message):
    """
    Format a message for display.
    
    Args:
        message: The message object from LangChain
        
    Returns:
        str: Formatted message string
    """
    # Handle different message types
    if hasattr(message, 'content'):
        # For AIMessage, HumanMessage, etc.
        return str(message.content)
    elif hasattr(message, 'pretty_print'):
        # For messages that support pretty_print
        return str(message)
    elif isinstance(message, dict):
        # For dictionary messages
        return message.get('content', str(message))
    else:
        # Fallback
        return str(message)


def chat_with_agent(agent_executor, memory):
    """
    Chat with the AI agent in a natural conversation.
    
    Args:
        agent_executor: The configured agent executor
        memory: The conversation buffer memory
    """
    print("Chat with Albert 1.0")
    print("=" * 40)
    print("Type 'quit' to exit, 'new' to start a new conversation")
    print("=" * 40)
    print()
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            # Check for new conversation command
            if user_input.lower() == 'new':
                # Clear memory for new conversation
                memory.clear()
                print("New conversation started.")
                print()
                continue
            
            # Validate input
            if not user_input:
                print("Please enter a message.")
                continue
            
            # Get response from agent (memory is handled automatically)
            response = agent_executor.invoke({"input": user_input})
            
            # Display agent's response
            if "output" in response:
                print(f"Agent: {response['output']}")
            else:
                print("Agent: I'm sorry, I didn't get a response. Could you try again?")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.")


def main():
    """
    Main application entry point.
    """
    print("Starting AI Agent...")
    
    # Setup environment
    if not setup_environment():
        return
    
    try:
        # Create the agent
        agent_executor, memory = create_agent()
        print("Agent is ready to chat!")
        print()
        
        # Start the conversation
        chat_with_agent(agent_executor, memory)
        
    except Exception as e:
        print(f"Failed to start agent: {e}")
        print("Please check your configuration and try again.")


if __name__ == "__main__":
    main() 