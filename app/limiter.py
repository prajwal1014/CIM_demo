import redis
from fastapi import Request
from fastapi.responses import JSONResponse
from .config import REDIS_HOST, REDIS_PORT, DEFAULT_RATE_LIMIT, WINDOW

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

async def rate_limiter(request: Request, call_next):
    ip = request.client.host

    # 🚫 Check blocked IP
    if r.sismember("blocked_ips", ip):
        return JSONResponse(status_code=403, content={"message": "IP blocked"})

    # 🔢 Get custom limit
    custom_limit = r.hget("custom_limits", ip)
    limit = int(custom_limit) if custom_limit else DEFAULT_RATE_LIMIT

    key = f"rate:{ip}"
    count = r.incr(key)

    if count == 1:
        r.expire(key, WINDOW)

    if count > limit:
        return JSONResponse(status_code=429, content={"message": "Rate limit exceeded"})

    return await call_next(request)
