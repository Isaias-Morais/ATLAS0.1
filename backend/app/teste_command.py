from backend.app.schemas.command import CommandSchema


command = CommandSchema(
    type="lembrete",
    action="criar",
    data={
        "title": "Estudar Python",
        "remind_at": "2026-09-05T15:00:00"
    }
)

print(command)
print(command.data)