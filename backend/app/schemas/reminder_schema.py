from datetime import datetime
from pydantic import BaseModel


class ReminderCreate(BaseModel):
    title: str
    description: str | None = None
    remind_at: datetime


class ReminderResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str | None
    remind_at: datetime
    completed: bool
    created_at: datetime



class ReminderUpdate(BaseModel):
    title: str
    description: str | None = None
    remind_at: datetime
    completed: bool