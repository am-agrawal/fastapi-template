from fastapi import FastAPI
from core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="FastAPI backend application",
    debug=settings.DEBUG
)

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