from fastapi import FastAPI
from backend.app.api.router import api_router

app = FastAPI(
    title="Kgoro API",
    version="0.1.0",
    description="Project Kgoro - vendor-agnostic network orchestration and monitoring platform.",
)

app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}
