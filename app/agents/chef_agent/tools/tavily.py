import os
from langchain.tools import tool
from langchain_tavily import TavilySearch

search = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def search_tool(query: str):
    """
    Search the web for information using Tavily API.

    :param query: The search query string
    :return: Search results related to the query
    """
    return search.invoke(query)