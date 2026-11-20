import json
import pytest



from backend.app.ai.providers.parser import IAResponseParser
from backend.app.schemas.ai_interpretation_schema import Interpretation_AI


def test_parse_conversation():

    response_teste = '{"type": "conversation","message": "Olá! Como posso ajudar?","command": null}'

    paser = IAResponseParser()

    response = paser.parse(response_teste)

    paser = response_teste

    assert isinstance(response, Interpretation_AI)

