from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from core.db import Base
from datetime import datetime
from user.models import User


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, nullable=False)
    content = Column(String(140), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id))
    created_at = Column(DateTime, default=datetime.now)
