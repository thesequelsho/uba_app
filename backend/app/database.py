from sqlalchemy.orm import Session
from . import models

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Database operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_matches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Match).offset(skip).limit(limit).all()

def create_user(db: Session, name: str, email: str, city: str):
    db_user = models.User(name=name, email=email, city=city)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user