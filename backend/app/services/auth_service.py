from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.app.repositories.user_repository import get_user_by_email
from backend.app.security.jwt import create_access_token
from backend.app.security.password import verify_password


def login_service(
    db: Session,
    email: str,
    password: str
):
    user = get_user_by_email(db, email)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    password_is_valid = verify_password(
        password,
        user.password_hash
    )

    if not password_is_valid:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    access_token = create_access_token(user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }