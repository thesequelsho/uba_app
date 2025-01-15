# Note: Handles all match-related API endpoints
from fastapi import APIRouter
router = APIRouter()

# backend/app/routes/matches.py
@router.post("/matches/")
async def create_match(match_data: MatchCreate, db: Session):
    # 1. Validate match data
    validate_match(match_data)

    # 2. Create match record
    new_match = create_match_record(db, match_data)

    # 3. Update player rankings
    update_player_rankings(db, match_data)

    # 4. Send notifications (if any)
    notify_players(match_data)

    return {"success": True, "new_rankings": updated_rankings}