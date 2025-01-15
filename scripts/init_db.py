# Note: Sets up database and creates sample data
from backend.app.models import Base, User, Match
from sqlalchemy import create_engine

def init_db():
    # Create database tables
    engine = create_engine("postgresql://localhost/uba_db")
    Base.metadata.create_all(engine)
    
    # Add sample data
    # (Add sample users and matches here)

if __name__ == "__main__":
    init_db()