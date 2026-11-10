
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal


# Base schema
class CricketPlayerBase(BaseModel):

    player_name: str = Field(
        min_length=2,
        max_length=100
    )

    team_name: str = Field(
        min_length=2,
        max_length=100
    )

    role: Literal[
        "Batter",
        "Bowler",
        "All-Rounder",
        "Wicketkeeper"
    ]

    matches_played: int = Field(ge=0)

    total_runs: int = Field(ge=0)

    wickets_taken: int = Field(ge=0)

    balls_faced: int = Field(ge=0)

    catches: int = Field(ge=0)


# Create schema
class CricketPlayerCreate(CricketPlayerBase):

    pass


# Update schema
class CricketPlayerUpdate(BaseModel):

    matches_played: int | None = Field(
        default=None,
        ge=0
    )

    total_runs: int | None = Field(
        default=None,
        ge=0
    )

    wickets_taken: int | None = Field(
        default=None,
        ge=0
    )

    balls_faced: int | None = Field(
        default=None,
        ge=0
    )

    catches: int | None = Field(
        default=None,
        ge=0
    )


# Response schema
class CricketPlayerResponse(CricketPlayerBase):

    player_id: int

    model_config = ConfigDict(from_attributes=True)


# Strike rate response
class StrikeRateResponse(BaseModel):

    player_id: int

    player_name: str

    total_runs: int

    balls_faced: int

    strike_rate: float | None


# Team statistics response
class TeamStatisticsResponse(BaseModel):

    team_name: str

    total_runs: int

    total_wickets: int
