from fastapi import FastAPI
from user.models import Base as base_user
from user.routes import router as router_user
from utils.db import engine
from car.models import Base as base_car
from car.routers import router as router_car

base_user.metadata.create_all(bind=engine)
base_car.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(router_user)
app.include_router(router_car)
