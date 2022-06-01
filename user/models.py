from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    pr = relationship('Post', backref='users', uselist=False)
    tr = relationship('Subscribe', backref='users', uselist=False)


class Subscribe(Base):
    __tablename__ = "subscribe_users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer, ForeignKey(User.id))
    user_subscriber_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
