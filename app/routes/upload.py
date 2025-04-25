from fastapi import APIRouter, File, UploadFile, HTTPException, status, Depends, Security
from fastapi_throttle import RateLimiter
from app.schemas.upload import UploadResponse
from app.services.blob import upload_blob
from app.security import get_api_key
import os
import uuid
from datetime import datetime

router = APIRouter()

@router.post(
    "/",
    response_model=UploadResponse,
    dependencies=[Depends(RateLimiter(times=5, seconds=60))],
)
async def upload_audio(
    file: UploadFile = File(...),
    api_key: str = Security(get_api_key),
):
    # Read raw data and compute file size
    data = await file.read()
    size = len(data)
    if not file.content_type.startswith("audio/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type"
        )
    ext = os.path.splitext(file.filename)[1]
    blob_name = f"{uuid.uuid4()}{ext}"
    try:
        url = await upload_blob(data, blob_name)
        created_at = datetime.utcnow()
        return UploadResponse(url=url, blob_name=blob_name, size=size, created_at=created_at)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
