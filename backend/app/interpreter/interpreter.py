from backend.app.schemas.command import CommandSchema


class Interpreter:

    def interpret(self, text):

        match text:

            case "criar lembrete":
                return CommandSchema(
                    type="lembrete",
                    action="criar"
                )

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