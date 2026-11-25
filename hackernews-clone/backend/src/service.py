import redis.asyncio as redis
from src.cache_service import get_cache, set_cache
from src.scraper.scraper import news_scraper


async def get_stories_service(
    page:int,
    redis_client:redis):
    url=f"https://news.ycombinator.com/?p={page}"
    posts = await get_cache(f"stories:{page}",redis_client)
    if posts is None:
        print("no redis_fetch")
        posts = await news_scraper(url)
        await set_cache(f"stories:{page}",300,posts,redis_client)
    
    return {"page": page,
            "posts": posts}
    
