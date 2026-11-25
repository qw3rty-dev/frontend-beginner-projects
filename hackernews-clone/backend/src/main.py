import os
from contextlib import asynccontextmanager

import redis.asyncio as redis
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import router

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")

@asynccontextmanager
async def lifespan(app:FastAPI):
    app.state.redis = redis.Redis.from_url(REDIS_URL)
    yield
    await app.state.redis.aclose()

    
app = FastAPI(lifespan=lifespan)
app.include_router(router)


origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:5501",
    "http://localhost:5501",
    "http://127.0.0.1:5502",
    "http://localhost:5502",
    ]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
)
