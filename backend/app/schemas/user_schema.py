from typing import Optional
from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    email: EmailStr
    first_name: str 
    last_name: Optional[str]
    is_active: bool = True

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    id: int

class User(UserBase):

    class Config:
        orm_mode = True