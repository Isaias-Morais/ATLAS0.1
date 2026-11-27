from pydantic import BaseModel , model_validator
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




class CommandSchema(BaseModel):
    type: str
    action: str
    data: ReminderCommandData | MusicCommandData | None = None



class CommandRequest(BaseModel):
    text:str

#lista Lembrete
class ListReminderData(BaseModel):
    pass

#CRIA LEMBRETE
class CreateReminderData(BaseModel):
    title: str
    remind_at: datetime
    text: str | None = None
    description: str | None = None


# DELETAR LEMBRETE
class DeleteReminderData(BaseModel):
    reminder_id: int


# ATUALIZAR LEMBRETE
class UpdateReminderData(BaseModel):
    reminder_id: int
    title: str | None = None
    text: str | None = None
    description: str | None = None
    remind_at: datetime | None = None
    completed: bool | None = None

    @model_validator(mode="after")
    def validar_atualizacao(self):
        campos = [
            self.title,
            self.text,
            self.description,
            self.remind_at,
            self.completed
        ]

        if all(campo is None for campo in campos):
            raise ValueError("Informe pelo menos um campo para atualizar.")

        return self