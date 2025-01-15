<<<<<<< HEAD
# Underground Basketball Association (UBA)

A global ranking system for competitive basketball players outside of the NBA.

=======
# uba_app
We are building the world's first professional basketball league that ranks players solely on how hard it is to beat them in a game of 1 on 1. The higher the number the harder it is to win against them. 

Questions we want answers to: 
- Who is capable of claiming to be the best year after year?
- Where will they come from?
- Which city and/or country can hold the crown the longest?

Fans will be able to follow their favorite hometown heros and players can hold th crown in their respective cities. Should be fun to watch.  

# backend
Database Models:
- User: Stores player information, including rank and location
- Match: Records game results and maintains relationships between players

Core Features:
- User registration with unique IDs
- Match logging with ELO ranking updates
- Leaderboard filtering by location
- Player statistics tracking

API Endpoints:
- /users/: Create new users
- /matches/: Log matches and update rankings
- /leaderboard/: Get ranked players with location filters
- /users/{user_id}/stats: Get player statistics

ELO Ranking System:
- Implemented using standard ELO formula
- K-factor of 32 for ranking adjustments
- Real-time updates after each match

# frontend
User Dashboard (already implemented)
- Current rank display
- Win rate statistics
- Total matches played
- Rank progress chart

Match Logging Interface
- Form to input opponent and scores
- Score validation (0-15 range)
- Success/error messages
- Match rules display

Leaderboard View
- Global rankings display
- Filtering by ZIP and city
- Player cards with rank and stats
- Responsive layout

Profile Management
- Personal information editing
- Location settings
- Bio section
- Form validation
- Success messages
>>>>>>> origin/main
