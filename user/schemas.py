from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserUpdateBase(BaseModel):
    username: str
    email: str


class SubscribeModel(BaseModel):
    user_id: int
    user_subscriber_id: int

    class Config:
        orm_mode = True


class SubscribeUpdateModel(SubscribeModel):
    user_subscriber_email: str
