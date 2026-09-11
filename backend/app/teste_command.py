from backend.app.interpreter.interpreter import Interpreter


interpreter = Interpreter()

command = interpreter.interpret(
    "criar lembrete estudar python amanhã às 15:00"
)

print(command)
print(command.data.title)
print(command.data.remind_at)

