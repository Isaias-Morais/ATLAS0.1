from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.app.models.reminder import Reminder
from backend.app.repositories.reminder_repository import create_reminder
from backend.app.repositories.user_repository import get_user_by_id


def create_reminder_service(
    db: Session,
    user_id: int,
    title: str,
    description: str | None,
    remind_at: datetime
):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    reminder = Reminder(
        user_id=user_id,
        title=title,
        description=description,
        remind_at=remind_at
    )

    return create_reminder(db, reminder)