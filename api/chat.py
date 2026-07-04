from fastapi import APIRouter, HTTPException
from schemas.models import ChatRequest, ChatResponse
from services.callmissed_client import client

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        messages = []

        for msg in request.history:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })

        messages.append({
            "role": "user",
            "content": request.message
        })

        response = client.chat.completions.create(
            model="kimi-k2.7-code",
            messages=messages
        )

        return ChatResponse(
            response=response.choices[0].message.content
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to get response from CallMissed API."
        )