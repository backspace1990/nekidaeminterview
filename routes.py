from fastapi import APIRouter
from user_blogs import post
from user import user


routes = APIRouter()

routes.include_router(post.router, prefix="/blog", tags=["blogs"])
routes.include_router(user.user_route, prefix="/users", tags=["users"])
routes.include_router(user.user_subscribe_route, prefix="/subscribe", tags=["subscribe"])