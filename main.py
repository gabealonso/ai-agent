from agents.wikipedia_agent import build_agent_executor

def main():
    agent_executor = build_agent_executor()
    question = "Who is Lionel Messi?"

    response = agent_executor.invoke({
        "messages": [{"role": "user", "content": question}]
    })

    print("Agent response:\n")
    for msg in response["messages"]:
        role = msg.__class__.__name__.replace("Message", "").upper()
        print(f"{role}: {msg.content}")

if __name__ == "__main__":
    main()
