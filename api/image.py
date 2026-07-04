from fastapi import APIRouter, HTTPException
from schemas.models import ImageRequest, ImageResponse
from services.callmissed_client import client

router = APIRouter()

@router.post("/image", response_model=ImageResponse)
def generate_image(request: ImageRequest):
    try:
        response = client.images.generate(
            model="flux-2-klein-9b",
            prompt=request.prompt
        )

        return ImageResponse(
            image=response.data[0].b64_json
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Image generation failed."
        )