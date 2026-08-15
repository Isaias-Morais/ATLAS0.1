from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend.app.models.user import User
from backend.app.repositories.user_repository import (create_user,
                                                      get_user_by_id,
                                                      get_all_users,
                                                      update_user,
                                                      delete_user
                                                      )
from backend.app.security.password import hash_password


def create_user_service(
    db: Session,
    name: str,
    email: str,
    password: str
):
    hashed_password = hash_password(password)

    user = User(
        name=name,
        email=email,
        password_hash=hashed_password
    )

    return create_user(db, user)


def get_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return user


def get_all_users_service(db: Session):
    return get_all_users(db)


def update_user_service(
        db: Session,
        user_id: int,
        name: str,
        email: str
):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return update_user(
        db=db,
        user=user,
        name=name,
        email=email
    )


def delete_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    delete_user(db, user)