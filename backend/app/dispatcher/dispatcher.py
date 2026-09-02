from backend.app.services.reminder_service import create_reminder_service


class Dispatcher:

    def dispatch(self, command, db):

        if command["type"] == "lembrete":

            match command["action"]:
                case "criar":
                    return create_reminder_service(
                        db=db,
                        user_id=command["user_id"],
                        title=command["title"],
                        description=command["description"],
                        remind_at=command["remind_at"]
                    )

                case "listar":
                    print("Listar lembretes")

                case "atualizar":
                    print("Atualizar lembrete")

                case "deletar":
                    print("Deletar lembrete")


w