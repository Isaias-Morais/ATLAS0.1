from pydantic import BaseModel


class CommandSchema(BaseModel):
    type: str
    action: str
    data: dict | None = None