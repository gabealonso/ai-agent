"""
AI Agent Main Application

This is the main entry point for the AI agent application.
It provides an interactive chat interface with conversation memory and smart tool selection.
"""

import uuid
import warnings
import sys
import os
from agents.ai_agent import build_agent_executor

# Suppress RuntimeWarnings (mainly from DuckDuckGo)
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Global conversation memory
conversation_memory = []


def get_system_prompt():
    """
    Get the system prompt for the AI agent.
    
    Returns:
        list: List containing the system message with instructions
    """
    return [
        {
            "role": "system",
            "content": (
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
        }
    ]


def extract_user_name_from_history():
    """
    Extract user name from conversation history.
    
    Returns:
        str or None: The user's name if found, None otherwise
    """
    for msg in conversation_memory:
        if msg["role"] == "user":
            content = msg["content"].lower()
            if "my name is" in content:
                return content.split("my name is")[-1].strip().split()[0]
            elif "i'm" in content:
                parts = content.split("i'm")
                if len(parts) > 1:
                    return parts[1].strip().split()[0]
            elif "i am" in content:
                parts = content.split("i am")
                if len(parts) > 1:
                    return parts[1].strip().split()[0]
    return None


def enhance_user_input(user_input, user_name):
    """
    Enhance user input with context and tool selection guidance.
    
    Args:
        user_input (str): The original user input
        user_name (str or None): The user's name if known
        
    Returns:
        str: Enhanced input with context and guidance
    """
    # Add name context if asking about name
    if user_name and ("what is my name" in user_input.lower() or "what's my name" in user_input.lower()):
        return f"The user's name is {user_name}. Current question: {user_input}"
    
    # Add tool selection guidance for specific types of questions
    elif any(word in user_input.lower() for word in ["weather", "current", "today", "latest", "recent", "now"]):
        return f"IMPORTANT: This is a time-sensitive question. Use DuckDuckGo web search for current information. Question: {user_input}"
    elif any(word in user_input.lower() for word in ["what is", "who is", "tell me about", "define", "explain"]):
        return f"IMPORTANT: This is a general knowledge question. Use Wikipedia for factual information. Question: {user_input}"
    
    return user_input


def format_ai_response(content):
    """
    Format AI response with appropriate prefix based on content.
    
    Args:
        content (str): The AI response content
        
    Returns:
        str: Formatted response with appropriate prefix
    """
    # Check for Wikipedia tool usage
    if "wikipedia" in content.lower() or "page:" in content.lower():
        if not content.startswith("Wikipedia: "):
            return "Wikipedia: " + content
    
    # Check for web search tool usage
    elif any(pattern in content.lower() for pattern in ["search", "duckduckgo", "weather", "oct", "jan", "sep", "2023", "2020", "·", "°c", "°f"]):
        if not content.startswith("Web: "):
            return "Web: " + content
    
    return content


def run_agent_interaction(agent_executor, user_input):
    """
    Run a single interaction with the agent.
    
    Args:
        agent_executor: The configured agent executor
        user_input (str): The user's input
        
    Returns:
        bool: True if response was generated, False otherwise
    """
    try:
        # Extract user name from history
        user_name = extract_user_name_from_history()
        
        # Enhance user input with context
        enhanced_input = enhance_user_input(user_input, user_name)
        
        # Add current message to memory
        conversation_memory.append({"role": "user", "content": user_input})
        
        # Suppress warnings and run agent
        with open(os.devnull, 'w') as devnull:
            old_stderr = sys.stderr
            sys.stderr = devnull
            try:
                response = agent_executor.invoke({
                    "messages": [{"role": "user", "content": enhanced_input}],
                    "config": {"recursion_limit": 10}
                })
            finally:
                sys.stderr = old_stderr
        
        # Process and display response
        response_found = False
        for msg in response["messages"]:
            if (hasattr(msg, 'content') and msg.content and 
                msg.__class__.__name__ != "HumanMessage" and
                msg.__class__.__name__ != "SystemMessage"):
                
                formatted_response = format_ai_response(msg.content)
                print(f"\nAI: {formatted_response}")
                
                # Add AI response to memory
                conversation_memory.append({"role": "assistant", "content": msg.content})
                response_found = True
                break
        
        if not response_found:
            print("\nAI: No response generated. Please try again.")
            return False
            
        return True
        
    except Exception as e:
        print(f"\nError: {e}")
        return False


def main():
    """
    Main application entry point.
    
    Sets up the agent, initializes conversation memory, and runs the interactive chat loop.
    """
    print("Initializing AI Agent...")
    agent_executor = build_agent_executor()
    
    # Generate unique thread ID for this session
    thread_id = str(uuid.uuid4())
    print(f"Thread ID: {thread_id}")
    print("=" * 50)
    print("AI Agent is ready! Type 'quit' to exit.")
    print("=" * 50)
    
    # Initialize conversation memory with system context
    conversation_memory.extend(get_system_prompt())
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            # Validate input
            if not user_input:
                print("Please enter a message.")
                continue
            
            # Run agent interaction
            run_agent_interaction(agent_executor, user_input)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()
