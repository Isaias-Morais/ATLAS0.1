from sqlalchemy.orm import session

from backend.app.models import user, reminder
from backend.app.schemas.command_scherma import CommandSchema
from backend.app.services.reminder_service import create_reminder_service, get_all_reminders_service, \
    delete_reminder_service,update_reminder_service


class Dispatcher:

    def __init__(self, reminder_service=None, music_service=None):
        self.reminder_service = reminder_service
        self.music_service = music_service

    def dispatch(self,db:session, command:CommandSchema,user_id:int):

        if command is None:
                return {"status": "error", "message": "Comando inválido ou não reconhecido."}

        if command.type == "lembrete":

            match command.action:

                case "criar":
                    return create_reminder_service(
                        db=db,
                        user_id=user_id,
                        title=command.data.title,
                        remind_at=command.data.remind_at,
                        description=command.data.description
                    )


                case "listar":
                    return get_all_reminders_service(
                        db=db,
                        user_id=user_id,
                    )

                case "atualizar":
                    return update_reminder_service(
                        db=db,
                        reminder_id=command.data.reminder_id,
                        user_id=user_id,
                        title=command.data.title,
                        remind_at=command.data.remind_at,
                        completed=command.data.completed,
                        description=command.data.description
                    )

                case "deletar":
                    return delete_reminder_service(
                        db=db,
                        reminder_id=command.data.reminder_id,
                        user_id=user_id
                    )

        if command.type == "musica":
            if command.action == "tocar":
                if not command.data:
                    return {
                        "status": "error",
                        "message": "Faltam os dados da música."
                    }

                if not command.data.musica and not command.data.artist:
                    return {
                        "status": "error",
                        "message": "Preciso do nome da música ou do artista."
                    }

                musica_id = self.music_service.tocar_musica_service(
                    musica=command.data.musica,
                    cantor=command.data.artist
                )

                return {
                    "tipo": "musica",
                    "mensagem": f"{command.data.musica}!",
                    "musica_id": musica_id
                }

