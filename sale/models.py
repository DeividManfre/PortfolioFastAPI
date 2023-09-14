from sqlalchemy import Column, Integer, ForeignKey
from utils.db import Base


class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("car.id"))
    user_id = Column(Integer, ForeignKey("user.id"))