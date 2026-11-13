import json
from backend.app.schemas.ai_interpretation_schema import Interpretation_AI
from pydantic import ValidationError

class IAResponseParser:

    def parse(self, response:str) -> Interpretation_AI:

        try:
            json_data = json.loads(response)
        except json.JSONDecodeError as e:
            raise

        try:
            schema_valido = Interpretation_AI.model_validate(json_data)
        except ValidationError as e:
            raise
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



