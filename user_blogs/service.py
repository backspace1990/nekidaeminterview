from .models import Post
from user.models import User, Subscribe
from fastapi import HTTPException, status


def get_all_post_list(db):
    return db.query(Post).all()


def get_my_post_list(user_id, db):
    controller = db.query(User).filter(User.id == user_id).first()
    if controller is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="My_user_id Not Found in User_id")

    return db.query(Post).filter(Post.user_id == user_id).all()


def get_user_blog(user_id, db):
    controller = db.query(Subscribe).filter(Subscribe.user_id == user_id).first()
    if controller is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Your user_id Not Found in Table "
                                                                          "Subscribe User_id")
    return db.query(Subscribe, Post).filter(Subscribe.user_subscriber_id == Post.user_id).all()


def user_create_post(db, item):
    controller = db.query(User).filter(User.id == item.user_id).first()
    if controller is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publisher_id Not Found in User_id!"
                                                                          "To make a Post, you need to register")
    new_post = Post(**item.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def delete_read_in_my_blog(user_id, created_at, db):
    controller = db.query(Subscribe).filter(Subscribe.user_id == user_id).first()
    if controller is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Your user_id Not Found in Table "
                                                                          "Subscribe User_id")
    return db.query(Subscribe, Post).filter(Subscribe.user_subscriber_id == Post.user_id).\
        filter(Post.created_at != created_at).all()


"""
def create_and_read_my_blog(email, db):
    controller1 = db.query()
"""
