import pytest

from pydantic import ValidationError
from backend.app.validators.command_validator import CommandValidator
from backend.app.schemas.command_scherma import CommandSchema, ReminderCommandData, MusicCommandData


def test_deletar_lembrete_com_id():
    validator = CommandValidator()

    command = CommandSchema(
        type="lembrete",
        action="deletar",
        data=ReminderCommandData(reminder_id=10)
    )

    resultado = validator.validate(command)

    assert resultado.data.reminder_id == 10


def test_deletar_lembrete_sem_id():
    validator = CommandValidator()

    command = CommandSchema(
        type="lembrete",
        action="deletar",
        data=ReminderCommandData()
    )

    with pytest.raises(ValidationError):
        validator.validate(command)


def test_listar_lembretes_sem_dados():
    validator = CommandValidator()

    command = CommandSchema(
        type="lembrete",
        action="listar",
        data=None
    )

    resultado = validator.validate(command)

    assert resultado is not None


def test_buscar_musica():
    validator = CommandValidator()

    command = CommandSchema(
        type="musica",
        action="buscar",
        data=MusicCommandData(musica="Evidências")
    )

    resultado = validator.validate(command)

    assert resultado.type == "musica"
    assert resultado.action == "buscar"
    assert resultado.data.musica == "Evidências"


def test_tocar_musica():
    validator = CommandValidator()

    command = CommandSchema(
        type="musica",
        action="tocar",
        data=MusicCommandData(musica="Evidências")
    )

    resultado = validator.validate(command)

    assert resultado.type == "musica"
    assert resultado.action == "tocar"
    assert resultado.data.title == "Evidências"


def test_parar_musica():
    validator = CommandValidator()

    command = CommandSchema(
        type="musica",
        action="parar",
        data=MusicCommandData(musica="Evidências")
    )

    resultado = validator.validate(command)

    assert resultado.type == "musica"
    assert resultado.action == "parar"
    assert resultado.data.musica == "Evidências"