# uba_app

# backend
Database Models:
  User: Stores player information, including rank and location
  Match: Records game results and maintains relationships between players

Core Features:
  User registration with unique IDs
  Match logging with ELO ranking updates
  Leaderboard filtering by location
  Player statistics tracking

API Endpoints:
  /users/: Create new users
  /matches/: Log matches and update rankings
  /leaderboard/: Get ranked players with location filters
  /users/{user_id}/stats: Get player statistics


ELO Ranking System:
  Implemented using standard ELO formula
  K-factor of 32 for ranking adjustments
  Real-time updates after each match

# frontend
User Dashboard (already implemented)
  Current rank display
  Win rate statistics
  Total matches played
  Rank progress chart

Match Logging Interface
  Form to input opponent and scores
  Score validation (0-15 range)
  Success/error messages
  Match rules display

Leaderboard View
  Global rankings display
  Filtering by ZIP and city
  Player cards with rank and stats
  Responsive layout

Profile Management
  Personal information editing
  Location settings
  Bio section
  Form validation
  Success messages
