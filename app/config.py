import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

DEFAULT_RATE_LIMIT = 5
WINDOW = 60  # seconds

ADMIN_TOKEN = "secret123"  # change later
