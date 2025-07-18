import uuid
from agents.wikipedia_agent import build_agent_executor

def main():
    agent_executor = build_agent_executor()
    
    # Generate a unique thread ID
    thread_id = str(uuid.uuid4())
    print(f"Thread ID: {thread_id}")
    print("=" * 50)
    
    while True:
        # Get user input from console
        user_input = input("\nEnter your question (or 'quit' to exit): ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input:
            print("Please enter a question.")
            continue
        
        print(f"\nProcessing your question...")
        
        try:
            response = agent_executor.invoke({
                "messages": [{"role": "user", "content": user_input}],
                "config": {"configurable": {"thread_id": thread_id}}
            })

            print("\nAgent response:")
            print("-" * 30)
            for msg in response["messages"]:
                role = msg.__class__.__name__.replace("Message", "").upper()
                print(f"{role}: {msg.content}")
            print("-" * 30)
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
