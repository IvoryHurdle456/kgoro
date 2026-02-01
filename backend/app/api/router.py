from fastapi import APIRouter
from backend.app.api.routes.devices import router as devices_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(devices_router)