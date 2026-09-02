from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.database.base import Base
from backend.app.database.connection import engine
from backend.app.models.user import User
from backend.app.models.reminder import Reminder
from backend.app.routes.user_routes import router as user_router
from backend.app.routes.reminder_routes import router as reminder_router
from backend.app.routes.auth_routes import router as auth_router
from backend.app.routes.command_routes import router as command_router

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(reminder_router)
app.include_router(auth_router)
app.include_router(command_router)


@app.get("/")
def root():
    return {"message": "ATLAS ONLINE"}
