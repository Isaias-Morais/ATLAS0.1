
import pytest

from backend.app.ai.prompt_builder import PromptBuilder, AgenteSnapshot


def test_criar_snapshot():
    builder = PromptBuilder("AGENT.md")

    snapshot = builder.create_snapshot()

    assert isinstance(snapshot, AgenteSnapshot)
    assert isinstance(snapshot.instructions, str)
    assert isinstance(snapshot.version, str)
    assert len(snapshot.version) == 64


def test_snapshot_mantem_mesmo_hash():
    builder = PromptBuilder("AGENT.md")

    snapshot1 = builder.create_snapshot()
    snapshot2 = builder.create_snapshot()

    assert snapshot1.version == snapshot2.version
    assert snapshot1.instructions == snapshot2.instructions


def test_snapshot_e_imutavel():
    builder = PromptBuilder("AGENT.md")

    snapshot = builder.create_snapshot()

    with pytest.raises(AttributeError):
        snapshot.instructions = "Novas instruções"
