import json
from backend.app.schemas.ai_interpretation_schema import Interpretation_AI
from pydantic import ValidationError


# Classe que transforma e valida a resposta bruta (texto) vinda da IA
class IAResponseParser:

    # Recebe a string da IA e devolve um objeto estruturado e validado
    def parse(self, response: str) -> Interpretation_AI:

        # Tenta converter o texto recebido em um dicionário Python
        try:
            json_data = json.loads(response)
        # Se a IA mandou um texto que não é JSON válido, repassa o erro para cima
        except json.JSONDecodeError as e:
            raise

        # Tenta encaixar e validar os dados no molde (schema) esperado pelo sistema
        try:
            schema_valido = Interpretation_AI.model_validate(json_data)
        # Se faltar algum campo obrigatório ou o tipo estiver errado, repassa o erro
        except ValidationError as e:
            raise

        # Devolve os dados prontos e seguros para o resto do código usar
        return schema_valido


"""
AIResponseParser:

Responsável por processar as respostas recebidas dos provedores de IA.

- Converte a resposta JSON em dados Python.
- Valida os dados utilizando o schema Interpretation_AI.
- Retorna uma interpretação validada.
- Propaga erros de JSON e validação para a camada responsável pelo tratamento.

Não executa comandos nem decide quais ações podem ser realizadas.
"""