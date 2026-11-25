import asyncio
import json
from typing import Any

import redis.asyncio as redis
from redis.exceptions import RedisError


async def set_cache(key:str, ttl: int, value: Any, redis_client:redis.Redis):
    try:
        json_value = json.dumps(value)
        await asyncio.wait_for(redis_client.set(key, json_value, ex=ttl),timeout=1.0)
        print(f"Log: Added {key} to redis")
    except (TimeoutError,RedisError) as e:
        print(f"Log: Redis_error {e}")

        
async def get_cache(key:str,redis_client:redis.Redis):
    try:
        cache = await asyncio.wait_for(redis_client.get(key),timeout=1.0)
        if cache is None:
            return None
        print("Log: Fetching from Redis")
        return json.loads(cache)
    
    except (TimeoutError, RedisError) as e:
        print(f"Log: Redis_error {e}")
