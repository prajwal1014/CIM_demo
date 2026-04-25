from fastapi import APIRouter, Request, HTTPException
import redis
from .config import REDIS_HOST, REDIS_PORT, ADMIN_TOKEN

router = APIRouter()
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def verify_admin(request: Request):
    token = request.headers.get("x-admin-token")
    if token != ADMIN_TOKEN:
        raise HTTPException(status_code=403, detail="Unauthorized")

@router.post("/block/{ip}")
def block_ip(ip: str, request: Request):
    verify_admin(request)
    r.sadd("blocked_ips", ip)
    return {"message": f"{ip} blocked"}

@router.post("/unblock/{ip}")
def unblock_ip(ip: str, request: Request):
    verify_admin(request)
    r.srem("blocked_ips", ip)
    return {"message": f"{ip} unblocked"}

@router.post("/set-limit/{ip}/{limit}")
def set_limit(ip: str, limit: int, request: Request):
    verify_admin(request)
    r.hset("custom_limits", ip, limit)
    return {"message": f"{ip} limit set to {limit}"}
