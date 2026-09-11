from pydantic import BaseModel
from datetime import datetime


class ReminderCommandData(BaseModel):
    title: str
    description: str | None = None
    remind_at: datetime | None = None


class CommandSchema(BaseModel):
    type: str
    action: str
    data: ReminderCommandData | None = None


class CommandRequest(BaseModel):
    text:str


