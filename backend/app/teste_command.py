from datetime import datetime, timedelta, time
import re
from datetime import timedelta
from backend.app.interpreter.interpreter import Interpreter
import unicodedata



interpreter = Interpreter()
#
# # hora = interpreter.transformar_horario(":0")
# #
# # print(hora)
# # print(type(hora))
# # print(isinstance(hora, time))
#
# # resultado = interpreter.parse_reminder_datetime(
# #     "criar lembrete estudar Python amanhã às 12h"
# # )
# #
# # print(resultado)
# # print(type(resultado))
# #
# # horario = interpreter.procurar_horario("amanhã às 99")
# #
# # print(horario)
#
# # command = interpreter.interpret('criar lembrete estudar Python amanhã às 12h')
# # print(command)
# # print(type(command))
# # print(command.type)
# # print(command.action)
# # print(command.data)
#
#

print(interpreter.extrair_id_lebrete("deletar lembrete 3"))