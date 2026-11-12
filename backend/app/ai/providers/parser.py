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



