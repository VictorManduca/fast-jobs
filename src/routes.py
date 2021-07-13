from fastapi import APIRouter

from src.controllers import users
from src.controllers import jobs
from src.controllers import auth

api_router = APIRouter()
api_router.include_router(users.router, prefix='/user', tags=['users'])

api_router.include_router(jobs.router, prefix='/job', tags=['jobs'])

api_router.include_router(auth.router, prefix='', tags=['auth'])
