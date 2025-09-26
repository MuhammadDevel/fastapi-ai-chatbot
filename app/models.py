from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

class ChatHistory(BaseModel):
    user_message: str
    bot_reply: str
    timestamp: datetime
