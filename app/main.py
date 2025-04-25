from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.INFO)

load_dotenv()

from app.routes.upload import router as upload_router

app = FastAPI(title="THV - True Heart Voice API")

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory=os.getenv("UPLOAD_DIR", "uploads")), name="uploads")

# Tidak perlu event startup khusus untuk rate limiting karena fastapi-throttle menggunakan memory

@app.get("/health")
async def health_check():
    
    return {"status": "ok"}
app.include_router(upload_router, prefix="/api/upload", tags=["upload"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )