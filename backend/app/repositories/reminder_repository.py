from sqlalchemy.orm import Session

from backend.app.models.reminder import Reminder


def create_reminder(db: Session, reminder: Reminder):
    db.add(reminder)
    db.commit()
    db.refresh(reminder)

    return reminder