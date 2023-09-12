from pydantic import BaseModel
from typing import List
from datetime import date
from enum import Enum

class CompleteEnum(str, Enum):
    Sim = 'S'
    Não = 'N'

class CarCreate(BaseModel):
    brand: str
    model: str
    complete: CompleteEnum
    year: date
    color_id: int
    name_brand_id: int
    license_plate: int

class CarUpdate(BaseModel):
    brand: str
    model: str
    complete: CompleteEnum
    year: date
    color_id: int
    name_brand_id: int
    license_plate: int

class CarInDB(CarCreate):
    id: int

class CarResponse(BaseModel):
    id: int
    brand: str
    model: str
    complete: CompleteEnum
    year: date
    color_id: int
    name_brand_id: int
    license_plate: int

class CarListResponse(BaseModel):
    cars: List[CarResponse]