from fastapi import APIRouter

from src.controllers import users

api_router = APIRouter()
api_router.include_router(users.router, prefix='/user', tags=['users'])