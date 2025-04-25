import os

async def upload_blob(data: bytes, blob_name: str) -> str:
    """
    Save audio file bytes to local directory and return its URL path.
    """
    upload_dir = os.getenv("UPLOAD_DIR", "uploads")
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, blob_name)
    with open(file_path, "wb") as f:
        f.write(data)
    base_url = os.getenv("BASE_URL", "http://localhost:8000")
    return f"{base_url}/uploads/{blob_name}"
