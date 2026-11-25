from fastapi import APIRouter, Query, Request
from src.service import get_stories_service

router = APIRouter(prefix="/v1")

@router.get("/")
async def get_stories(
    request:Request,
    page:int = Query(default=1,ge=1)):
    redis_client = request.app.state.redis
    return await get_stories_service(page,redis_client)
    
