from pydantic import BaseModel


class PostModel(BaseModel):
    title: str
    content: str
    user_id: int

    class Config:
        orm_mode = True


class PostCreateModel(PostModel):
    pass
