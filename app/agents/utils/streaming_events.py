import json
from langchain_core.messages import HumanMessage
from app.agents.stop_smoking_agent.workflow import graph


async def _stream_events(message_text: str):
    """
    Stream LLM output token-by-token using LangGraph's "messages" stream mode.
    Yields SSE events: each event is one token (or message chunk) from the agent node.
    See: https://docs.langchain.com/oss/python/langgraph/streaming#messages
    """
    async for message_chunk, metadata in graph.astream(
        {"messages": [HumanMessage(content=message_text)]},
        stream_mode="messages",
    ):
        if not getattr(message_chunk, "content", None):
            continue
        payload = {
            "content": message_chunk.content,
            "node": metadata.get("langgraph_node"),
        }
        yield f"data: {json.dumps(payload)}\n\n"
