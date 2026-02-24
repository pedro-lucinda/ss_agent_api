from langgraph.graph import StateGraph, END
from app.agents.stop_smoking_agent.state import AgentState
from app.agents.stop_smoking_agent.nodes.tooll_node import tool_node
from app.agents.stop_smoking_agent.edges.should_continue import should_continue
from app.agents.stop_smoking_agent.nodes.call_model import call_model

workflow = StateGraph(AgentState)

workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_edge("tools", "agent") 

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools", 
        "end": END,         
    },
)

workflow.set_entry_point("agent")

graph = workflow.compile()