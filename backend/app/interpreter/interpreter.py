from backend.app.schemas.command_scherma import CommandSchema
from datetime import datetime,timedelta


class Interpreter:


    def parse_reminder_datetime(text: str):

        if "amanhã às 15:00" in text:
            tomorrow = datetime.now() + timedelta(days=1)

            return tomorrow.replace(
                hour=15,
                minute=0,
                second=0,
                microsecond=0
            )

        return None



    def interpret(self, text: str):

        text = text.lower().strip()

        if text.startswith("criar lembrete "):
            remind_at = Interpreter.parse_reminder_datetime(text)

            title = text.removeprefix("criar lembrete ").strip()

            return CommandSchema(
                type="lembrete",
                action="criar",
                data={
                    "title": title,
                    "remind_at": remind_at
                }
            )

        match text:

            case "listar lembretes":
                return CommandSchema(
                    type="lembrete",
                    action="listar"
                )

            case "atualizar lembrete":
                return CommandSchema(
                    type="lembrete",
                    action="atualizar"
                )

            case "deletar lembrete":
                return CommandSchema(
                    type="lembrete",
                    action="deletar"
                )

        return None