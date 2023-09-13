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

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    complete = Column(String)
    year = Column(Date)
    color_id = Column(Integer)
    name_brand_id = Column(Integer)
    license_plate = Column(String)