from datetime import datetime

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.security.auth import get_current_user_id
from backend.app.database.connection import get_db
from backend.app.schemas.reminder_schema import ReminderCreate, ReminderResponse
from backend.app.services.reminder_service import create_reminder_service


router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"]
)


@router.post("/",response_model=ReminderResponse,status_code=201)
def create_reminder(
    reminder: ReminderCreate,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    return create_reminder_service(
        db=db,
        user_id=user_id,
        title=reminder.title,
        description=reminder.description,
        remind_at=reminder.remind_at
    )