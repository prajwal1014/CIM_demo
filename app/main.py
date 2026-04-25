from fastapi import FastAPI
from app.limiter import rate_limiter
from app.admin import router as admin_router
from app.dashboard import router as dashboard_router

app = FastAPI()

# Apply global rate limiting middleware
app.middleware("http")(rate_limiter)

# Include admin routes
app.include_router(admin_router, prefix="/admin")

# Include dashboard route
app.include_router(dashboard_router)

# Root endpoint
@app.get("/")
def home():
    return {"message": "Cloud Rate Limiter Running 🚀"}
