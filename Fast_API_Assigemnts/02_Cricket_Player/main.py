
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi import Request

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from config.database import Base, engine, get_db
from config.logger import logger

from models.cricketplayer_model import CricketPlayer

from schemas.cricketplayer_schema import (
    CricketPlayerCreate,
    CricketPlayerUpdate,
    CricketPlayerResponse,
    StrikeRateResponse,
    TeamStatisticsResponse
)

from services import cricketplayer_service as service


# Create database tables
Base.metadata.create_all(bind=engine)


# FastAPI application
app = FastAPI(
    title="Cricket Player Statistics API",
    description="API for managing cricket player statistics",
    version="1.0.0"
)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(
        "Unexpected error on %s %s",
        request.method,
        request.url.path
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error. Please try again later."
        }
    )


# Common database error handler
def handle_database_error():

    logger.exception(
        "Unexpected database operation failure"
    )

    raise HTTPException(
        status_code=500,
        detail="Internal server error. Please try again later."
    )


# 1. Register a new cricket player
@app.post(
    "/players/",
    response_model=CricketPlayerResponse,
    status_code=201
)
def create_player(
    data: CricketPlayerCreate,
    db: Session = Depends(get_db)
):

    try:

        return service.add_player(db, data)

    except IntegrityError:

        raise HTTPException(
            status_code=409,
            detail="Player ID already exists"
        )

    except SQLAlchemyError:

        handle_database_error()


# 2. List all players with pagination
@app.get(
    "/players/",
    response_model=list[CricketPlayerResponse]
)
def get_all_players(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):

    try:

        return service.get_all_players(
            db,
            skip,
            limit
        )

    except SQLAlchemyError:

        handle_database_error()


# 6. Filter players by team
@app.get(
    "/players/team/{team_name}",
    response_model=list[CricketPlayerResponse]
)
def filter_players_by_team(
    team_name: str,
    db: Session = Depends(get_db)
):

    try:

        return service.get_players_by_team(
            db,
            team_name
        )

    except SQLAlchemyError:

        handle_database_error()


# 7. All-rounders with at least 10 wickets
@app.get(
    "/players/all-rounders",
    response_model=list[CricketPlayerResponse]
)
def get_all_rounders(
    db: Session = Depends(get_db)
):

    try:

        return service.get_all_rounders(db)

    except SQLAlchemyError:

        handle_database_error()


# 8. Top five run scorers
@app.get(
    "/players/top-five",
    response_model=list[CricketPlayerResponse]
)
def get_top_five_scorers(
    db: Session = Depends(get_db)
):

    try:

        return service.get_top_five_scorers(db)

    except SQLAlchemyError:

        handle_database_error()


# 9. Calculate batting strike rate
@app.get(
    "/players/strike-rates",
    response_model=list[StrikeRateResponse]
)
def get_strike_rates(
    db: Session = Depends(get_db)
):

    try:

        return service.calculate_strike_rate(db)

    except SQLAlchemyError:

        handle_database_error()


# 10. Total runs and wickets by team
@app.get(
    "/players/team-statistics",
    response_model=list[TeamStatisticsResponse]
)
def get_team_statistics(
    db: Session = Depends(get_db)
):

    try:

        return service.get_team_statistics(db)

    except SQLAlchemyError:

        handle_database_error()


# 3. Find player by ID
@app.get(
    "/players/{player_id}",
    response_model=CricketPlayerResponse
)
def get_player(
    player_id: int,
    db: Session = Depends(get_db)
):

    try:

        player = service.get_player_by_id(
            db,
            player_id
        )

        if player is None:

            raise HTTPException(
                status_code=404,
                detail="Player not found"
            )

        return player

    except SQLAlchemyError:

        handle_database_error()


# 4. Update player statistics
@app.put(
    "/players/{player_id}",
    response_model=CricketPlayerResponse
)
def update_player(
    player_id: int,
    data: CricketPlayerUpdate,
    db: Session = Depends(get_db)
):

    if not data.model_dump(exclude_unset=True):

        raise HTTPException(
            status_code=422,
            detail="Provide at least one statistic to update"
        )

    try:

        player = service.update_player(
            db,
            player_id,
            data
        )

        if player is None:

            raise HTTPException(
                status_code=404,
                detail="Player not found"
            )

        return player

    except SQLAlchemyError:

        handle_database_error()


# 5. Delete a player
@app.delete("/players/{player_id}")
def delete_player(
    player_id: int,
    db: Session = Depends(get_db)
):

    try:

        result = service.delete_player(
            db,
            player_id
        )

        if not result:

            raise HTTPException(
                status_code=404,
                detail="Player not found"
            )

        return {
            "message": "Player deleted successfully",
            "player_id": player_id
        }

    except SQLAlchemyError:

        handle_database_error()


# Root endpoint
@app.get("/")
def home():

    return {
        "message": "Cricket Player Statistics API is running"
    }
