import os
import pytest
from httpx import AsyncClient
from fastapi import status
from app.main import app

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_upload_success(tmp_path, monkeypatch):
    # override upload directory for tests
    monkeypatch.setenv("UPLOAD_DIR", str(tmp_path))
    file_data = b"test audio content"
    async with AsyncClient(app=app, base_url="http://test") as client:
        files = {"file": ("test.wav", file_data, "audio/wav")}
        response = await client.post("/api/upload/", files=files)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["size"] == len(file_data)
        saved = tmp_path / data["blob_name"]
        assert saved.exists()
        assert saved.read_bytes() == file_data

@pytest.mark.asyncio
async def test_upload_invalid_type():
    async with AsyncClient(app=app, base_url="http://test") as client:
        files = {"file": ("test.txt", b"text", "text/plain")}
        response = await client.post("/api/upload/", files=files)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
