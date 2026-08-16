from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.connection import get_db
from backend.app.schemas.auth_schema import LoginRequest, TokenResponse
from backend.app.services.auth_service import login_service
from backend.app.security.auth import get_current_user_id


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=TokenResponse)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    return login_service(
        db=db,
        email=credentials.email,
        password=credentials.password
    )


@router.get("/me")
def get_me(
    user_id: int = Depends(get_current_user_id)
):
    return {
        "user_id": user_id
    }