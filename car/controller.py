from sqlalchemy.orm import Session
from .models import Car
from .schemas import CarCreate, CarUpdate, CarInDB

def create_car(db: Session, car: CarCreate) -> CarInDB:
    _car = Car(**car.dict())
    db.add(_car)
    db.commit()
    db.refresh(_car)
    return _car

def get_car(db: Session, car_id: int) -> CarInDB:
    return db.query(Car).filter(Car.id == car_id).first()

def get_cars(db: Session, skip: int = 0, limit: int = 100) -> list[CarInDB]:
    return db.query(Car).offset(skip).limit(limit).all()

def update_car(db: Session, car_id: int, car_update: CarUpdate) -> CarInDB:
    _car = get_car(db, car_id)
    for field, value in car_update.dict(exclude_unset=True).items():
        setattr(_car, field, value)
    db.commit()
    db.refresh(_car)
    return _car

def delete_car(db: Session, car_id: int) -> None:
    _car = get_car(db, car_id)
    db.delete(_car)
    db.commit()