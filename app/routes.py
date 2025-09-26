from fastapi import APIRouter
from app.services import get_ai_response
from app.models import ChatRequest, ChatResponse
from app.database import chat_collection
from bson import ObjectId

router = APIRouter()


def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc


@router.post("/", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    response_text = await get_ai_response(request.message)
    return ChatResponse(reply=response_text)


@router.get("/history")
async def get_chat_history():
    chats = await chat_collection.find().to_list(50)  # last 50 chats
    return [serialize_doc(chat) for chat in chats]
