from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, raiseload
from fastapi import HTTPException
from backend.app.database.connection import get_db
from backend.app.dispatcher.dispatcher import Dispatcher
from backend.app.interpreter.interpreter import Interpreter
from backend.app.schemas.command_scherma import CommandSchema, CommandRequest
from backend.app.security.auth import get_current_user_id

router = APIRouter(
    prefix="/commands",
    tags=["Commands"]
)

interpreter = Interpreter()
dispatcher = Dispatcher()

@router.post("/")
def execute_command( text:CommandRequest,db:Session=Depends(get_db),user_id: int = Depends(get_current_user_id)):

    try:
        command:CommandSchema = interpreter.interpret(text.text)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return dispatcher.dispatch(command=command,db=db,user_id=user_id)

