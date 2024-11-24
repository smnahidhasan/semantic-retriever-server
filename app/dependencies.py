# app/dependencies.py
from fastapi import Header, HTTPException
from typing import Optional

async def verify_api_key(x_api_key: Optional[str] = Header(None)):
    """Dependency to verify API key in headers."""
    if not x_api_key:
        raise HTTPException(status_code=400, detail="X-API-Key header is missing")
    # In production, compare with securely stored API keys
    if x_api_key != "your_secure_api_key":
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

async def get_db():
    """Database dependency - placeholder for actual DB connection."""
    # Replace with actual database connection logic
    db = {"connected": True}
    try:
        yield db
    finally:
        # Close database connection
        db.clear()
