from backend.app.schemas.command import CommandSchema


class Dispatcher:

    def dispatcher(self, command:CommandSchema):

        if command.type == "lembrete":

            match command.action:
                case "criar":
                    print("Criar lembrete")

                case "listar":
                    print("Listar lembretes")

                case "atualizar":
                    print("Atualizar lembrete")

                case "deletar":
                    print("Deletar lembrete")