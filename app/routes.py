# app/routes.py
from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, List
from .dependencies import verify_api_key, get_db

# Create two separate routers
router = APIRouter()
health_router = APIRouter()

# Health check endpoint - separate router without version prefix
@health_router.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}

# API endpoints with authentication
@router.get("/items", dependencies=[Depends(verify_api_key)])
async def get_items(db: dict = Depends(get_db)) -> List[Dict]:
    """Get all items endpoint."""
    return [{"id": 1, "name": "Example Item"}]