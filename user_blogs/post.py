from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.utils import get_db
from .schemas import PostCreateModel
from . import service

router = APIRouter()


@router.get("/post_list")
def all_post_list(db: Session = Depends(get_db)):
    return service.get_all_post_list(db)


@router.get("/my_posts/{user_id}")
def get_my_post_list(user_id: int, db: Session = Depends(get_db)):
    return service.get_my_post_list(user_id, db)


@router.post("/create_post", response_model=PostCreateModel, status_code=status.HTTP_201_CREATED)
def create_post(item: PostCreateModel, db: Session = Depends(get_db)):
    return service.user_create_post(db, item)


@router.get("/get_my_blog")
def get_my_blog(user_id: int, db: Session = Depends(get_db)):
    return service.get_user_blog(user_id, db)


@router.delete("/get_my_blog/{user_id}/{time}")
def update_my_blog(user_id: int, time: str, db: Session = Depends(get_db)):
    return service.delete_read_in_my_blog(user_id, time, db)