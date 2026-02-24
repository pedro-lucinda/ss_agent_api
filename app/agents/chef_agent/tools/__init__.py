from .tavily import search_tool

tools=[search_tool]

tools_by_name={ tool.name:tool for tool in tools}