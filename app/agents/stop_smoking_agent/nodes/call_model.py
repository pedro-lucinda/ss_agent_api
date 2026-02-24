from app.agents.stop_smoking_agent.state import AgentState
from app.agents.stop_smoking_agent.model import model_react

def call_model(state: AgentState):
    """Invoke the model with the current conversation state."""
    response = model_react.invoke({"history": state["messages"]})
    return {"messages": [response]}