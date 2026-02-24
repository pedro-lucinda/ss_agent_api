from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest
from app.agents.utils.streaming_events import _stream_events
router = APIRouter()


@router.post("/chef-agent/chat")
async def chef_agent_stream(body: ChatRequest):
    return StreamingResponse(
        _stream_events(body.message),
        media_type="text/event-stream",
    )