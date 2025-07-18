# import os
# from langchain_openai import ChatOpenAI
# from langgraph.prebuilt import create_react_agent
# from langgraph.checkpoint.memory import MemorySaver
# from tools.wikipedia_tool import get_wikipedia_tool
# from pydantic import SecretStr
# from dotenv import load_dotenv
# load_dotenv()

# def build_agent_executor():
#     tool = get_wikipedia_tool()
#     tools = [tool]

#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         raise ValueError("environment variable OPENAI_API_KEY is not defined")

#     llm = ChatOpenAI(
#         model="gpt-4o-mini",
#         temperature=0,
#         api_key=SecretStr(api_key)
#     )

#     llm_with_tools = llm.bind_tools(tools)

#     memory = MemorySaver()

#     agent_executor = create_react_agent(llm_with_tools, tools, checkpointer=memory)

#     return agent_executor

import os
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools.wikipedia_tool import get_wikipedia_tool
from pydantic import SecretStr
from dotenv import load_dotenv

load_dotenv()

def build_agent_executor():
    tool = get_wikipedia_tool()
    tools = [tool]

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("environment variable OPENAI_API_KEY is not defined")

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=SecretStr(api_key)
    )

    llm_with_tools = llm.bind_tools(tools)

    agent_executor = create_react_agent(llm_with_tools, tools)

    return agent_executor
