from sqlalchemy.orm import Session
from datetime import datetime
from backend.app.models.reminder import Reminder



def create_reminder(db: Session, reminder: Reminder):
    db.add(reminder)
    db.commit()
    db.refresh(reminder)

    return reminder


def get_reminders_by_user(db: Session, user_id: int):
    return (
        db.query(Reminder)
        .filter(Reminder.user_id == user_id)
        .all()
    )


def get_reminder_by_id(db: Session, reminder_id: int):
    return (
        db.query(Reminder)
        .filter(Reminder.id == reminder_id)
        .first()
    )


def update_reminder(db: Session,reminder: Reminder,title: str,description: str | None,remind_at: datetime,completed: bool):
    reminder.title = title
    reminder.description = description
    reminder.remind_at = remind_at
    reminder.completed = completed

    db.commit()
    db.refresh(reminder)

    return reminder



def delete_reminder(db: Session, reminder: Reminder):
    db.delete(reminder)
    db.commit()

    return reminder