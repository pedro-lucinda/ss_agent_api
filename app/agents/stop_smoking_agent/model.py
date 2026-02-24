from langchain_openai import ChatOpenAI
from app.agents.stop_smoking_agent.prompt import chat_prompt
from app.agents.stop_smoking_agent.tools import tools

model = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_tokens=1000)

model_react=chat_prompt|model.bind_tools(tools)