from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database
from typing import List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="UBA API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = database.get_db()
    return next(db)

@app.get("/")
async def health_check():
    return {"status": "healthy", "message": "UBA API is running"}

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = database.get_users(db)
    return users

@app.get("/leaderboard")
def get_leaderboard(db: Session = Depends(get_db)):
    users = db.query(models.User)\
        .order_by(models.User.rank.desc())\
        .all()
    
    return [
        {
            "id": user.id,
            "name": user.name,
            "rank": round(user.rank, 1),
            "matches_played": user.matches_played,
            "wins": user.wins,
            "win_rate": f"{user.calculate_win_rate():.1f}%"
        }
        for user in users
    ]

@app.get("/matches")
def get_matches(db: Session = Depends(get_db)):
    matches = database.get_matches(db)
    return matches