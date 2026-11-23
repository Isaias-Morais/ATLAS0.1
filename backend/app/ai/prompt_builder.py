import hashlib
import os
import time
from dataclasses import dataclass

from google.genai._gaos.types.agents import agent

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


class PromptBuilder:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.cache = {}


    def carregar_md(self, ttl_segundos: int = 10) -> str:
        agora = time.time()

        # Se está no cache e ainda não passou o tempo de validade, retorna direto da RAM
        if self.nome_arquivo in self.cache:
            conteudo, ultima_verificacao, mtime_salvo = self.cache[self.nome_arquivo]
            if agora - ultima_verificacao < ttl_segundos:
                return conteudo

        # Só chega aqui a cada 10 segundos
        caminho = os.path.join(BASE_DIR, self.nome_arquivo)
        mtime_atual = os.path.getmtime(caminho)

        # Se já tinha no cache e o arquivo não mudou, apenas renova o relógio
        if self.nome_arquivo in self.cache and self.cache[self.nome_arquivo][2] == mtime_atual:
            conteudo = self.cache[self.nome_arquivo][0]
            self.cache[self.nome_arquivo] = (conteudo, agora, mtime_atual)
            return conteudo

        # Lê do disco apenas se for a 1ª vez ou se o arquivo realmente mudou
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()

        self.cache[self.nome_arquivo] = (conteudo, agora, mtime_atual)
        return conteudo


    def create_snapshot(self):

        #carrega aqv.md
        arquivo_md = self.carregar_md()

        #transforma texto em byte
        arquivo_md_utf = arquivo_md.encode("utf-8")
        version = hashlib.sha256(arquivo_md_utf).hexdigest()

        #armazena nop dataclass
        agente_snap = AgenteSnapshot(instructions=arquivo_md, version=version)

        #retorna
        return agente_snap




#cria classe q serve para armazena dados
@dataclass(frozen=True)
class AgenteSnapshot:
    instructions: str
    version:str




