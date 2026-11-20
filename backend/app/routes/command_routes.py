from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, raiseload
from fastapi import HTTPException
from backend.app.database.connection import get_db
from backend.app.dispatcher.dispatcher import Dispatcher
from backend.app.interpreter.interpreter import Interpreter
from backend.app.schemas.command_scherma import CommandSchema, CommandRequest
from backend.app.security.auth import get_current_user_id
from pydantic import ValidationError
from backend.app.validators.command_validator import CommandValidator

router = APIRouter(
    prefix="/commands",
    tags=["Commands"]
)

validator = CommandValidator()
interpreter = Interpreter()
dispatcher = Dispatcher()

@router.post("/")
def execute_command( text:CommandRequest,db:Session=Depends(get_db),user_id: int = Depends(get_current_user_id)):


    try:
        command: CommandSchema = interpreter.interpret(text.text)

        if command is None:
            raise HTTPException(
                status_code=400,
                detail="Não foi possível entender o comando informado."
            )

        command = validator.validate(command)

    except ValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=e.errors()
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    return dispatcher.dispatch(
        command=command,
        db=db,
        user_id=user_id
    )

