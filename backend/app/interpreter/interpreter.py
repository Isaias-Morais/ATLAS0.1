from sqlalchemy.ext.asyncio import result

from backend.app.schemas.command_scherma import CommandSchema
from datetime import datetime, timedelta, time
from datetime import timedelta
import re
import unicodedata


class Interpreter:


    def parse_reminder_datetime(self,text: str):

        dia = self.identificar_dia(text)
        horario = self.procurar_horario(text)
        horario = self.transformar_horario(horario)
        data_e_hora = self.montar_data_hora(comando=dia, hora=horario)

        if not data_e_hora:
            return "O horário informado é inválido."

        return data_e_hora


    def interpret(self, text: str):

        text = self.texto_formatado(text)

        if text.startswith("criar lembrete "):
            remind_at = self.parse_reminder_datetime(text)

            title = self.extrair_titulos_lembretes(text)

            return CommandSchema(
                type="lembrete",
                action="criar",
                data={
                    "title": title,
                    "remind_at": remind_at
                }
            )


        if text.startswith("deletar lembrete"):
            reminder_id = self.extrair_id_lebrete(text)

            if reminder_id is None:
                raise ValueError("O ID do lembrete é obrigatório.")

            return CommandSchema(
                type="lembrete",
                action="deletar",
                data={
                    "reminder_id": reminder_id
                }
            )


        match text:


            case "atualizar lembrete":
                return CommandSchema(
                    type="lembrete",
                    action="atualizar"
                )

            case "listar lembrete":
                return CommandSchema(
                    type="lembrete",
                    action="listar"
                )

        return None

    def procurar_horario(self,texto: str):

        resultado = re.search(r"\d{1,2}(:\d{1,2})?", texto)

        if not resultado:
            return None
        return resultado.group()


    def transformar_horario(self,texto: str):

        if not texto:
            return None

        if not (':' in texto):
            hora = int(texto)
            minutos = 0

        else:
            partes = texto.split(':')

            if not partes[0].isdigit() or not partes[1].isdigit() :
                return None

            hora = int(partes[0])
            minutos = int(partes[1])

        if hora < 0 or hora > 23:
            return None
        if minutos < 0 or minutos > 59:
            return None

        hora_completa = time(hour=hora, minute=minutos)

        return hora_completa



    @staticmethod
    def texto_formatado(texto: str):
        texto_sem_acento = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
        texto_limpo = texto_sem_acento.lower()
        return texto_limpo


    def identificar_dia(self,texto: str):

        texto_limpo = Interpreter.texto_formatado(texto)

        if 'depois' in texto_limpo and 'amanha' in texto_limpo:
            return 2

        if 'amanha' in texto_limpo:
            return 1

        if 'hoje' in texto_limpo:
            return 0

        return None

    def montar_data_hora(self,comando: int | None, hora: time|None):

        hoje = datetime.now()

        if not comando:
            comando = 0

        data = hoje + timedelta(days=comando)

        if not hora:
            raise ValueError("O horário informado é inválido.")

        data = data.replace(hour=hora.hour, minute=hora.minute, second=0, microsecond=0)

        return data


    def extrair_titulos_lembretes(self,texto: str):

        texto = Interpreter.texto_formatado(texto)

        texto = texto.removeprefix("criar lembrete ").strip()

        resultado = re.search(r"hoje|amanha|depois de amanhã", texto)

        if not resultado:
            return None

        return texto[:resultado.start()]

    def extrair_id_lebrete(self,texto: str):
        resultado = re.search(r"\d+", texto)
        if not resultado:
            return None
        return int(resultado.group())

