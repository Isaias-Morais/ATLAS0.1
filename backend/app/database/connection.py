import os
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


def get_db():
    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()