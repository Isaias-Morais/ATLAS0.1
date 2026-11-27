from backend.app.schemas.command_scherma import CommandSchema, CreateReminderData, DeleteReminderData, \
    UpdateReminderData, ListReminderData, MusicCommandData
from backend.app.schemas.command_scherma import CreateReminderData,DeleteReminderData,UpdateReminderData,ListReminderData


class CommandValidator:

    def __init__(self):
        self.schemas = {
            ("lembrete", "criar"): CreateReminderData,
            ("lembrete", "deletar"): DeleteReminderData,
            ("lembrete", "atualizar"): UpdateReminderData,
            ("lembrete", "listar"): ListReminderData,
            ("musica", "buscar"):MusicCommandData,
            ("musica", "tocar"):MusicCommandData,
            ("musica", "parar"):MusicCommandData
            }


    def validate(self, command: CommandSchema) -> CommandSchema:
        key = (command.type, command.action)

        schema = self.schemas.get(key)

        if schema is None:
            raise ValueError("Operação não possui schema de validação.")

        if command.data is None:
            data = {}
        else:
            data = command.data.model_dump(exclude_none=True)

        validated_data = schema.model_validate(data)

        return CommandSchema(
            type=command.type,
            action=command.action,
            data=validated_data.model_dump(exclude_none=True) or None
        )

