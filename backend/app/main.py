from fastapi import FastAPI

app = FastAPI(
    title="Kgoro API",
    version="0.1.0",
    description="Project Kgoro - vendor-agnostic network orchestration and monitoring platform.",
)

@app.get("/health")
def health():
    return {"status": "ok"}
