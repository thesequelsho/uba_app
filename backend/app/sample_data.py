from . import models
import random
from datetime import datetime, timedelta

def create_sample_data():
    db = models.SessionLocal()

    # Sample cities
    cities = ["Chicago", "New York", "Los Angeles", "Miami", "Houston"]
    
    # Create sample users
    sample_users = [
        ("John Doe", "john@example.com", "Chicago"),
        ("Jane Smith", "jane@example.com", "New York"),
        ("Mike Johnson", "mike@example.com", "Los Angeles"),
        ("Sarah Williams", "sarah@example.com", "Miami"),
        ("Tom Brown", "tom@example.com", "Houston")
    ]

    users = []
    for name, email, city in sample_users:
        user = models.User(
            name=name,
            email=email,
            city=city,
            rank=1000.0  # Starting ELO rating
        )
        db.add(user)
        users.append(user)
    
    db.commit()

    # Create sample matches
    for _ in range(20):  # Create 20 sample matches
        player1, player2 = random.sample(users, 2)
        
        # Generate realistic scores (games to 15)
        if random.random() < 0.7:  # 70% chance player1 wins
            score1, score2 = 15, random.randint(8, 13)
        else:
            score1, score2 = random.randint(8, 13), 15

        match = models.Match(
            player1_id=player1.id,
            player2_id=player2.id,
            player1_score=score1,
            player2_score=score2,
            played_at=datetime.now() - timedelta(days=random.randint(0, 30))
        )
        
        db.add(match)
        
        # Update player stats
        player1.matches_played += 1
        player2.matches_played += 1
        
        if score1 > score2:
            player1.wins += 1
        else:
            player2.wins += 1

        # Update ELO ratings
        k_factor = 32
        expected_score1 = 1 / (1 + 10 ** ((player2.rank - player1.rank) / 400))
        actual_score = 1 if score1 > score2 else 0
        
        rank_change = k_factor * (actual_score - expected_score1)
        player1.rank += rank_change
        player2.rank -= rank_change

    db.commit()
    db.close()

if __name__ == "__main__":
    print("Creating sample data...")
    create_sample_data()
    print("Sample data created successfully!")