from pydantic import BaseModel, model_validator
from typing import Literal
from backend.app.schemas.command_scherma import CommandSchema

class Interpretation_AI(BaseModel):
    type:Literal["clarification","conversation","action"]
    message:str
    command:CommandSchema|None = None

    @model_validator(mode='after')
    def validar_interpretacao(self):
        if self.type == "action" and self.command is None:
            raise ValueError("Ação precisa de um comando")

        if (self.type == "conversation" or self.type == "clarification") and self.command is not None:
            raise ValueError("Conversa não pode ter comando")

        return self
