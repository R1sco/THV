import os
import logging
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv

# Load .env file explicitly
load_dotenv()

# API key security setup
API_KEY = os.getenv("API_KEY", "")
logging.info(f"Loaded API_KEY: {API_KEY[:5]}...{API_KEY[-5:] if API_KEY else 'MISSING'}")
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def get_api_key(api_key_header_value: str = Security(api_key_header)):
    """Dependensi untuk memvalidasi API Key di header X-API-Key"""
    if api_key_header_value == API_KEY:
        return api_key_header_value
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or missing API Key")
