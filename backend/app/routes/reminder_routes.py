from datetime import datetime

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.security.auth import get_current_user_id
from backend.app.database.connection import get_db
from backend.app.schemas.reminder_schema import ReminderCreate, ReminderResponse,ReminderUpdate
from backend.app.services.reminder_service import create_reminder_service, get_reminder_service, \
    update_reminder_service, delete_reminder_service, get_reminder_ALL_service

router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"]
)


@router.post("/create",response_model=ReminderResponse,status_code=201)
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


@router.get("/get/{reminder_id}",response_model=ReminderResponse)
def get_reminder(
    reminder_id: int,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    return get_reminder_service(
        db=db,
        reminder_id=reminder_id,
        user_id=user_id
    )


@router.put("/update/{reminder_id}",response_model=ReminderResponse)
def update_reminder(
    reminder_id: int,
    reminder: ReminderUpdate,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    return update_reminder_service(
        db=db,
        reminder_id=reminder_id,
        user_id=user_id,
        title=reminder.title,
        description=reminder.description,
        remind_at=reminder.remind_at,
        completed=reminder.completed
    )


@router.delete("/delete/{reminder_id}",status_code=204)
def delete_reminder(
    reminder_id: int,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    delete_reminder_service(
        db=db,
        reminder_id=reminder_id,
        user_id=user_id
    )


@router.get(
    "/get_all",
    response_model=list[ReminderResponse]
)
def get_reminders(
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    return get_reminder_ALL_service(
        db=db,
        user_id=user_id
    )