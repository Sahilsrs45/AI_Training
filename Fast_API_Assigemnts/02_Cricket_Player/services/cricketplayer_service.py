
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from models.cricketplayer_model import CricketPlayer
from config.logger import logger


# 1. Register a new cricket player
def add_player(db: Session, data):

    try:

        player = CricketPlayer(**data.model_dump())

        db.add(player)
        db.commit()
        db.refresh(player)

        logger.info(
            "Player registered successfully. Player ID: %s",
            player.player_id
        )

        return player

    except IntegrityError:

        db.rollback()

        logger.warning(
            "Duplicate player ID: %s",
            data.player_id
        )

        raise

    except SQLAlchemyError:

        db.rollback()

        logger.exception(
            "Database error while registering player"
        )

        raise


# 2. List all players with pagination
def get_all_players(db: Session, skip: int, limit: int):

    query = (
        select(CricketPlayer)
        .order_by(CricketPlayer.player_id)
        .offset(skip)
        .limit(limit)
    )

    return db.scalars(query).all()


# 3. Find player by ID
def get_player_by_id(db: Session, player_id: int):

    player = db.get(CricketPlayer, player_id)

    if player is None:

        logger.warning(
            "Player not found. Player ID: %s",
            player_id
        )

    return player


# 4. Update player match statistics
def update_player(db: Session, player_id: int, data):

    player = db.get(CricketPlayer, player_id)

    if player is None:

        logger.warning(
            "Update failed. Player not found: %s",
            player_id
        )

        return None

    update_data = data.model_dump(exclude_unset=True)

    if not update_data:

        logger.warning(
            "Update requested without statistics"
        )

        return None

    try:

        for key, value in update_data.items():

            setattr(player, key, value)

        db.commit()
        db.refresh(player)

        logger.info(
            "Player statistics updated. Player ID: %s",
            player_id
        )

        return player

    except IntegrityError:

        db.rollback()

        logger.exception(
            "Integrity error while updating player"
        )

        raise

    except SQLAlchemyError:

        db.rollback()

        logger.exception(
            "Database error while updating player"
        )

        raise


# 5. Delete a player
def delete_player(db: Session, player_id: int):

    player = db.get(CricketPlayer, player_id)

    if player is None:

        logger.warning(
            "Delete failed. Player not found: %s",
            player_id
        )

        return False

    try:

        db.delete(player)
        db.commit()

        logger.info(
            "Player deleted successfully. Player ID: %s",
            player_id
        )

        return True

    except SQLAlchemyError:

        db.rollback()

        logger.exception(
            "Database error while deleting player"
        )

        raise


# 6. Filter players by team
def get_players_by_team(db: Session, team_name: str):

    query = (
        select(CricketPlayer)
        .where(
            func.lower(CricketPlayer.team_name)
            == team_name.lower()
        )
        .order_by(CricketPlayer.player_id)
    )

    return db.scalars(query).all()


# 7. List all-rounders with at least 10 wickets
def get_all_rounders(db: Session):

    query = (
        select(CricketPlayer)
        .where(
            CricketPlayer.role == "All-Rounder",
            CricketPlayer.wickets_taken >= 10
        )
        .order_by(CricketPlayer.wickets_taken.desc())
    )

    return db.scalars(query).all()


# 8. Return top five run scorers
def get_top_five_scorers(db: Session):

    query = (
        select(CricketPlayer)
        .order_by(
            CricketPlayer.total_runs.desc(),
            CricketPlayer.player_id.asc()
        )
        .limit(5)
    )

    return db.scalars(query).all()


# 9. Calculate batting strike rate
def calculate_strike_rate(db: Session):

    query = (
        select(CricketPlayer)
        .order_by(CricketPlayer.player_id)
    )

    players = db.scalars(query).all()

    result = []

    for player in players:

        if player.balls_faced == 0:

            strike_rate = None

            logger.warning(
                "Strike rate unavailable for player ID %s: "
                "zero balls faced",
                player.player_id
            )

        else:

            strike_rate = round(
                (player.total_runs / player.balls_faced) * 100,
                2
            )

        result.append({

            "player_id": player.player_id,

            "player_name": player.player_name,

            "total_runs": player.total_runs,

            "balls_faced": player.balls_faced,

            "strike_rate": strike_rate

        })

    return result


# 10. Calculate total runs and wickets for each team
def get_team_statistics(db: Session):

    query = (
        select(
            CricketPlayer.team_name,
            func.sum(CricketPlayer.total_runs).label(
                "total_runs"
            ),
            func.sum(CricketPlayer.wickets_taken).label(
                "total_wickets"
            )
        )
        .group_by(CricketPlayer.team_name)
        .order_by(CricketPlayer.team_name)
    )

    results = db.execute(query).all()

    return [

        {
            "team_name": row.team_name,
            "total_runs": row.total_runs,
            "total_wickets": row.total_wickets
        }

        for row in results

    ]
