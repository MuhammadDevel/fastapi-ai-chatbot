from datetime import datetime
from app.database import chat_collection
from app.models import ChatHistory
from gradio_client import Client

client = Client("white-tiger111/chatbot")

async def get_ai_response(message: str) -> str:
    result = client.predict(input_text=message, api_name="/predict")

    # Save chat in DB
    history = ChatHistory(
        user_message=message,
        bot_reply=result,
        timestamp=datetime.utcnow()
    )
    await chat_collection.insert_one(history.dict())

    return result
