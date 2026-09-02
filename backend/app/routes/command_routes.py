from fastapi import APIRouter, Depends

from backend.app.dispatcher.dispatcher import Dispatcher
from backend.app.schemas.command import CommandSchema
from backend.app.security.auth import get_current_user_id

router = APIRouter(
    prefix="/commands",
    tags=["Commands"]
)

dispatcher = Dispatcher()

@router.post("/")
def execute_command(command:CommandSchema,user_id: int = Depends(get_current_user_id)):
    return dispatcher.dispatcher(command)