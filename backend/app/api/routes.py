from sys import prefix
from fastapi import APIRouter
from . import user_api

api_router = APIRouter()
api_router.include_router(user_api.router, prefix="/users", tags=["tags"])