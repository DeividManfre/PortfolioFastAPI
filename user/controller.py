from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, UserUpdate, UserInDB

def create_user(db: Session, user: UserCreate) -> UserInDB:
    _user = User(**user.dict())
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

def get_user(db: Session, user_id: int) -> UserInDB:
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[UserInDB]:
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_update: UserUpdate) -> UserInDB:
    _user = get_user(db, user_id)
    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(_user, field, value)
    db.commit()
    db.refresh(_user)
    return _user

def delete_user(db: Session, user_id: int) -> None:
    _user = get_user(db, user_id)
    db.delete(_user)
    db.commit()
