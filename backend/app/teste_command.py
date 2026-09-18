from datetime import datetime, timedelta, time
import re
from datetime import timedelta
from backend.app.interpreter.interpreter import Interpreter
import unicodedata


def extrair_titulos_lembretes(texto: str):

    texto = Interpreter.texto_formatado(texto)

    texto = texto.removeprefix("criar lembrete ").strip()

    resultado = re.search(r"hoje|amanha|depois de amanhã", texto)

    if not resultado:
        return None

    return texto[:resultado.start()]




interpreter = Interpreter()

hora = interpreter.transformar_horario("14:99")

print(hora)
print(type(hora))
print(isinstance(hora, time))