from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    first_name: str | None
    last_name: Optional[str]
    is_active: bool = True

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    id: int

class User(UserBase):

    class Config:
        orm_mode = True