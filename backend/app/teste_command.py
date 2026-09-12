from datetime import datetime, timedelta, time
import re
from datetime import timedelta

import unicodedata

def procurar_horario(texto:str):

    resultado = re.search(r"\d\d:\d\d" , texto)

    if not resultado:
       return None
    return resultado.group()




def transformar_horario(texto:str):

    if not texto:
        return None

    partes = texto.split(':')

    hora = int(partes[0])
    minutos = int(partes[1])


    hora_completa = time(hour=hora, minute=minutos)

    return hora_completa




def identificar_dia(texto:str):

    texto_sem_acento = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')

    texto_limpo = texto_sem_acento.lower()

    if 'depois' in texto_limpo and 'amanha' in texto_limpo:
        return 2

    if 'amanha' in texto_limpo:
        return 1

    if 'hoje' in texto_limpo:
        return 0

    return None


def montar_data_hora(comando:int|None,hora:time):

    hoje = datetime.now()

    if not comando:
        comando = 0

    data = hoje + timedelta(days=comando)

    data = data.replace(hour=hora.hour, minute=hora.minute)

    return data

texto = 'faco isso amanha as 14:01'

hora_str = procurar_horario(texto)

hora = transformar_horario(hora_str)

comando = identificar_dia(texto)


print(montar_data_hora(comando,hora))
