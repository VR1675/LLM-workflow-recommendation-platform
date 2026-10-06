import json
import time

try:
    import redis
except ImportError:
    redis = None

from app.config import REDIS_HOST, REDIS_PORT, CACHE_TTL_SECONDS
from app.utils.logger import logger


class CacheService:
    def __init__(self):
        self.memory_cache = {}
        self.redis_client = None

        if redis:
            try:
                self.redis_client = redis.Redis(
                    host=REDIS_HOST,
                    port=REDIS_PORT,
                    decode_responses=True,
                    socket_connect_timeout=1
                )
                self.redis_client.ping()
                logger.info("Connected to Redis cache")
            except Exception:
                self.redis_client = None
                logger.warning("Redis unavailable. Using in-memory cache fallback.")

    def get(self, key: str):
        if self.redis_client:
            value = self.redis_client.get(key)
            if value:
                return json.loads(value)

        item = self.memory_cache.get(key)

        if not item:
            return None

        value, expires_at = item

        if time.time() > expires_at:
            del self.memory_cache[key]
            return None

        return value

    def set(self, key: str, value, ttl_seconds: int = CACHE_TTL_SECONDS):
        if self.redis_client:
            self.redis_client.setex(key, ttl_seconds, json.dumps(value))
            return

        expires_at = time.time() + ttl_seconds
        self.memory_cache[key] = (value, expires_at)