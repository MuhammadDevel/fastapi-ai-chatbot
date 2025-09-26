from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Chatbot with FastAPI")

app.include_router(router, prefix="/chat", tags=["Chatbot"])
