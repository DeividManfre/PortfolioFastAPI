from pydantic import BaseModel
from typing import List

class SaleCreate(BaseModel):
    user_id: int
    car_id: int

class SaleUpdate(BaseModel):
    user_id: int
    car_id: int

class SaleInDB(SaleCreate):
    id: int

class SaleResponse(BaseModel):
    id: int
    user_id: int
    car_id: int

class SaleListResponse(BaseModel):
    items: List[SaleResponse]