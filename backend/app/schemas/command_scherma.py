from pydantic import BaseModel
from datetime import datetime


class ReminderCommandData(BaseModel):
    title: str | None = None
    text: str | None = None
    description: str | None = None
    remind_at: datetime | None = None
    reminder_id: int|None = None
    completed: bool | None = None


class MusicCommandData(BaseModel):
    musica: str | None = None
    artist: str | None = None
    title: str | None = None



class CommandSchema(BaseModel):
    type: str
    action: str
    data: ReminderCommandData | MusicCommandData | None = None



class CommandRequest(BaseModel):
    text:str


