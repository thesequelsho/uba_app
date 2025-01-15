from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./uba.db"  # Using SQLite for MVP
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    city = Column(String)
    rank = Column(Float, default=1000.0)  # Starting ELO rating
    matches_played = Column(Integer, default=0)
    wins = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    def calculate_win_rate(self):
        if self.matches_played == 0:
            return 0.0
        return (self.wins / self.matches_played) * 100

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    player1_id = Column(Integer, ForeignKey("users.id"))
    player2_id = Column(Integer, ForeignKey("users.id"))
    player1_score = Column(Integer)
    player2_score = Column(Integer)
    played_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)