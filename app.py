from fastapi import FastAPI
from core.config import settings

from api.user import router as user_router


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="FastAPI backend application",
    debug=settings.DEBUG
)

app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    """Root endpoint."""
    return {
        "message": "Welcome to the FastAPI application!",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}