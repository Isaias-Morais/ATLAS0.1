from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.app.models.reminder import Reminder
from backend.app.repositories.reminder_repository import create_reminder, get_reminder_by_id, update_reminder, \
    delete_reminder, get_reminders_by_user
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



def get_reminder_service(
    db: Session,
    reminder_id: int,
    user_id: int
):
    reminder = get_reminder_by_id(
        db=db,
        reminder_id=reminder_id
    )

    if reminder is None:
        raise HTTPException(
            status_code=404,
            detail="Lembrete não encontrado"
        )

    if reminder.user_id != user_id:
        raise HTTPException(
            status_code=404,
            detail="Lembrete não encontrado"
        )

    return reminder


def get_reminder_ALL_service(
    db: Session,
    user_id: int
):
    reminder = get_reminders_by_user(
        db=db,
        user_id=user_id
    )

    if reminder is None:
        raise HTTPException(
            status_code=404,
            detail="nenhum lembrete encontrado"
        )


    return reminder

def update_reminder_service(db: Session,reminder_id: int,user_id: int,title: str,description: str | None,remind_at: datetime,completed: bool):
    reminder = get_reminder_by_id(
        db=db,
        reminder_id=reminder_id
    )

    if reminder is None or reminder.user_id != user_id:
        raise HTTPException(
            status_code=404,
            detail="Lembrete não encontrado"
        )

    return update_reminder(
        db=db,
        reminder=reminder,
        title=title,
        description=description,
        remind_at=remind_at,
        completed=completed
    )



def delete_reminder_service(db: Session,reminder_id: int,user_id: int):
    reminder = get_reminder_by_id(
        db=db,
        reminder_id=reminder_id
    )

    if reminder is None or reminder.user_id != user_id:
        raise HTTPException(
            status_code=404,
            detail="Lembrete não encontrado"
        )

    delete_reminder(
        db=db,
        reminder=reminder
    )