from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str
    email: str
    phone: int

class UserUpdate(BaseModel):
    name: str
    email: str
    phone: int

class UserInDB(UserCreate):
    id: int

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: int

class UserListResponse(BaseModel):
    users: List[UserResponse]
