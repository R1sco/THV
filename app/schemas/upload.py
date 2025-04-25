from pydantic import BaseModel, Field
from datetime import datetime

class UploadResponse(BaseModel):
    url: str = Field(..., description="URL to access the uploaded audio file")
    blob_name: str = Field(..., description="Name of the saved audio file")
    size: int = Field(..., description="Size of the uploaded file in bytes")
    created_at: datetime = Field(..., description="Upload timestamp in ISO 8601 format")
