from .models import User, Subscribe
from fastapi import HTTPException, status


def get_users_lists(db):
    return db.query(User).all()


def create_user(db, item):
    new_user = User(**item.dict())
    controller1 = db.query(User).filter(User.username == item.username).first()
    if controller1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New_User_name already exists"
                                                                            "Please register with new username")
    controller2 = db.query(User).filter(User.email == item.email).first()
    if controller2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New_User_email already exists"
                                                                            "Please register with new mail")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(id, item, db):
    item_to_update = db.query(User).filter(User.id == id).first()
    item_to_update.username = item.username
    item_to_update.email = item.email
    db.commit()
    return item_to_update


def delete_user(id, db):
    user_to_delete = db.query(User).filter(User.id == id).first()

    if user_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    db.delete(user_to_delete)
    db.commit()
    return user_to_delete


def get_users_subscribe_lists(db):
    return db.query(Subscribe).all()


def create_new_user_subscribe_user(db, item):
    user_in_listUser = db.query(User).filter(User.id == item.user_id).first()
    subscribe_in_listUser = db.query(User).filter(User.id == item.user_subscriber_id).first()
    if user_in_listUser is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User_id Not Found in UserLists")

    if subscribe_in_listUser is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User_Subscribe_id Not Found in UserLists")

    new_subscribe = Subscribe(**item.dict())
    db.add(new_subscribe)
    db.commit()
    db.refresh(new_subscribe)
    return new_subscribe


def delete_subscribe_user(id, db):
    first_param = db.query(Subscribe).filter(Subscribe.id == id).first()

    if first_param is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    db.delete(first_param)
    db.commit()
    return first_param
