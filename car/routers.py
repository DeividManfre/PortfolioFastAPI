from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .schemas import CarCreate, CarUpdate, CarInDB, CarListResponse, CarResponse
from .controller import create_car, get_car, get_cars, update_car, delete_car
from utils.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cars/", response_model=CarResponse)
async def create_car_handler(car: CarCreate, db: Session = Depends(get_db)):
    return create_car(db, car)

@router.get("/cars/{car_id}", response_model=CarResponse)
async def read_car(car_id: int, db: Session = Depends(get_db)):
    car = get_car(db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.get("/cars/", response_model=CarListResponse)
async def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cars = get_cars(db, skip, limit)
    return {"cars": cars}

@router.put("/cars/{car_id}", response_model=CarResponse)
async def update_car_handler(car_id: int, car_update: CarUpdate, db: Session = Depends(get_db)):
    car = update_car(db, car_id, car_update)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.delete("/cars/{car_id}", response_model=dict)
async def delete_car_handler(car_id: int, db: Session = Depends(get_db)):
    car = get_car(db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    delete_car(db, car_id)
    return {"message": "Car deleted"}
