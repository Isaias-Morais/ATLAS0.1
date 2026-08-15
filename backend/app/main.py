from fastapi import FastAPI

from backend.app.database.base import Base
from backend.app.database.connection import engine
from backend.app.models.user import User
from backend.app.routes.user_routes import router as user_router

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "ATLAS ONLINE"}
