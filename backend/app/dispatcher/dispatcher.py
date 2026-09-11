from sqlalchemy.orm import session

from backend.app.models import user
from backend.app.schemas.command_scherma import CommandSchema
from backend.app.services.reminder_service import create_reminder_service

class Dispatcher:

    def __init__(self, reminder_service=None):
        self.reminder_service = reminder_service

    def dispatch(self,db:session, command:CommandSchema,user_id:int):

        if command.type == "lembrete":

            match command.action:

                case "criar":
                    return create_reminder_service(
                        db=db,
                        user_id=user_id,
                        command=command
                    )


                case "listar":
                    print("Listar lembretes")

                case "atualizar":
                    print("Atualizar lembrete")

                case "deletar":
                    print("Deletar lembrete")

