from langgraph.graph import StateGraph, END
from app.agents.chef_agent.state import AgentState
from app.agents.chef_agent.model import model_react
from app.agents.chef_agent.nodes.tooll_node import tool_node
from app.agents.chef_agent.edges.should_continue import should_continue
from app.agents.chef_agent.nodes.call_model import call_model

# Define a new graph
workflow = StateGraph(AgentState)

# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

# Add edges between nodes
workflow.add_edge("tools", "agent")  # After tools, always go back to agent

# Add conditional logic
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",  # If tools needed, go to tools node
        "end": END,          # If done, end the conversation
    },
)

# Set entry point
workflow.set_entry_point("agent")

# Compile the graph
graph = workflow.compile()