
from sqlalchemy import Column, Integer, String

from config.database import Base


class CricketPlayer(Base):

    __tablename__ = "CricketPlayer"

    player_id = Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=True
    )

    player_name = Column(
        String(100),
        nullable=False
    )

    team_name = Column(
        String(100),
        nullable=False
    )

    role = Column(
        String(30),
        nullable=False
    )

    matches_played = Column(
        Integer,
        nullable=False
    )

    total_runs = Column(
        Integer,
        nullable=False
    )

    wickets_taken = Column(
        Integer,
        nullable=False
    )

    balls_faced = Column(
        Integer,
        nullable=False
    )

    catches = Column(
        Integer,
        nullable=False
    )
