from fastapi import FastAPI, Request
from app.limiter import rate_limiter
from app.admin import router as admin_router

app = FastAPI()

# Middleware
app.middleware("http")(rate_limiter)

# Admin routes
app.include_router(admin_router, prefix="/admin")

@app.get("/")
def home():
    return {"message": "Cloud Rate Limiter Running 🚀"}
