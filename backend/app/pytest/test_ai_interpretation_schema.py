from backend.app.schemas.ai_interpretation_schema import Interpretation_AI


def test_conversation_without_command():
    interpretation = Interpretation_AI(
        type="conversation",
        message="Python é muito usado no backend.",
        command=None
    )

    assert interpretation.type == "conversation"
    assert interpretation.command is None