
from datetime import date
from pydantic import BaseModel, Field, ConfigDict


# Schema for creating a new feedback record
class TrainingFeedbackCreate(BaseModel):

    feedback_id: int = Field(gt=0)
    learner_name: str = Field(min_length=2, max_length=100)
    trainer_name: str = Field(min_length=2, max_length=100)
    course_name: str = Field(min_length=2, max_length=150)

    session_date: date

    content_rating: int = Field(ge=1, le=5)
    trainer_rating: int = Field(ge=1, le=5)
    hands_on_rating: int = Field(ge=1, le=5)

    comments: str | None = Field(default=None, max_length=1000)

    would_recommend: bool


# Schema for updating an existing feedback record
class TrainingFeedbackUpdate(BaseModel):

    learner_name: str | None = Field(default=None, min_length=2, max_length=100)
    trainer_name: str | None = Field(default=None, min_length=2, max_length=100)
    course_name: str | None = Field(default=None, min_length=2, max_length=150)

    session_date: date | None = None

    content_rating: int | None = Field(default=None, ge=1, le=5)
    trainer_rating: int | None = Field(default=None, ge=1, le=5)
    hands_on_rating: int | None = Field(default=None, ge=1, le=5)

    comments: str | None = Field(default=None, max_length=1000)

    would_recommend: bool | None = None


# Schema for sending feedback details in API responses
class TrainingFeedbackResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    feedback_id: int
    learner_name: str
    trainer_name: str
    course_name: str
    session_date: date
    content_rating: int
    trainer_rating: int
    hands_on_rating: int
    comments: str | None
    would_recommend: bool


# Schema for trainer-wise average rating
class TrainerAverageResponse(BaseModel):

    trainer_name: str
    average_trainer_rating: float


# Schema for course recommendation percentage
class RecommendationPercentageResponse(BaseModel):

    course_name: str
    total_feedback: int
    recommended_count: int
    recommendation_percentage: float
