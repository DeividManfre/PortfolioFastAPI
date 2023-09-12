from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
from datetime import date

Base = declarative_base()

class CompleteEnum(Enum):
    Sim = 'S'
    Não = 'N'

class Car(Base):
    __tablename__ = "car"

    id: int = Column(Integer, primary_key=True, index=True)
    brand: str = Column(String)
    model: str = Column(String)
    complete: CompleteEnum = Column(String)
    year: date = Column(Date)
    color_id: int = Column(Integer)
    name_brand_id: int = Column(Integer)
    license_plate: str = Column(String)
