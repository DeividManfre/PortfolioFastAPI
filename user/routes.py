from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserUpdate, UserInDB, UserListResponse
from .controller import create_user, get_user, get_users, update_user, get_user, delete_user
from utils.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserInDB)
async def create_user_handler(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users/{user_id}", response_model=UserInDB)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/", response_model=UserListResponse)
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip, limit)
    return {"users": users}

@router.put("/users/{user_id}", response_model=UserInDB)
async def update_user_handler(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = update_user(db, user_id, user_update)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}", response_model=dict)
async def delete_user_handler(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, user_id)
    return {"message": "User deleted"}
