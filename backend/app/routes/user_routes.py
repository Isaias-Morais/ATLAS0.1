from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.database.connection import get_db
from backend.app.schemas.user_schema import (UserCreate,
                                             UserResponse,
                                             UserUpdate
                                             )
from backend.app.services.user_service import (create_user_service,
                                               get_user_service,
                                               get_all_users_service,
                                               update_user_service,
                                               delete_user_service
                                               )


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/",response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user_service(
        db=db,
        name=user.name,
        email=user.email,
        password=user.password
    )


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_service(
        db=db,
        user_id=user_id
    )


@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return get_all_users_service(db)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    return update_user_service(
        db=db,
        user_id=user_id,
        name=user.name,
        email=user.email
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    delete_user_service(
        db=db,
        user_id=user_id
    )


