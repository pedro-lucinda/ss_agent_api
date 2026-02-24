from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage,SystemMessage

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are stop smoking agent that helps users to stop smoking. You will use the tools provided to you to help the user stop smoking.

Tools:
-
"""),
    MessagesPlaceholder(variable_name="history")
])