from fastapi import FastAPI
from api.chat import router as chat_router
from api.image import router as image_router

app = FastAPI(title="CallMissed Backend Chatbot API")

app.include_router(chat_router)
app.include_router(image_router)

@app.get("/")
def root():
    return {"message": "Backend Chatbot API is running successfully!"}