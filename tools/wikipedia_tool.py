from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

def get_wikipedia_tool():
    return WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())