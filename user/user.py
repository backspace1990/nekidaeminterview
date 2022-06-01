from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from .schemas import UserModel, UserUpdateBase, SubscribeModel

user_route = APIRouter()
user_subscribe_route = APIRouter()


@user_route.get("/user_list")
def user_lists(db: Session = Depends(get_db)):
    return service.get_users_lists(db)


@user_route.post("/users_create", response_model=UserModel, status_code=status.HTTP_201_CREATED)
def user_create(item: UserModel, db: Session = Depends(get_db)):
    return service.create_user(db, item)


@user_route.put("/user_update/{id}", response_model=UserModel, status_code=status.HTTP_200_OK)
def user_update(id: int, item: UserUpdateBase, db: Session = Depends(get_db)):
    return service.update_user(id, item, db)


@user_route.delete("/user_delete/{id}")
def user_delete(id: int, db: Session = Depends(get_db)):
    return service.delete_user(id, db)


@user_subscribe_route.get("/users_subscribe_lists")
def users_subscribe_lists(db: Session = Depends(get_db)):
    return service.get_users_subscribe_lists(db)


@user_subscribe_route.post("/create_users_new_subscribe", response_model=SubscribeModel,
                           status_code=status.HTTP_201_CREATED)
def create_new_subscribe_users(item: SubscribeModel, db: Session = Depends(get_db)):
    return service.create_new_user_subscribe_user(db, item)


@user_subscribe_route.delete("/delete_subscribe/{id}")
def delete_subscribe_users(id: int, db: Session = Depends(get_db)):
    return service.delete_subscribe_user(id, db)
