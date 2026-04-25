from fastapi import APIRouter
import redis
from .config import REDIS_HOST, REDIS_PORT

router = APIRouter()
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@router.get("/dashboard", response_class=None)
def dashboard():
    blocked_ips = list(r.smembers("blocked_ips"))
    limits = r.hgetall("custom_limits")

    html = f"""
    <html>
    <head><title>Dashboard</title></head>
    <body>
        <h1>🚀 Rate Limiter Dashboard</h1>

        <h2>Blocked IPs</h2>
        <ul>
            {''.join(f'<li>{ip}</li>' for ip in blocked_ips)}
        </ul>

        <h2>Custom Limits</h2>
        <ul>
            {''.join(f'<li>{ip}: {limit}</li>' for ip, limit in limits.items())}
        </ul>
    </body>
    </html>
    """
    return html
