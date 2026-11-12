
from sqlalchemy import Column, Integer, String, Date, Boolean
from config.database import Base


class TrainingFeedback(Base):

    # Database table name
    __tablename__ = "training_feedback"

    # Unique feedback ID
    feedback_id = Column(Integer, primary_key=True, index=True, autoincrement=False)

    # Learner details
    learner_name = Column(String(100), nullable=False)

    # Trainer details
    trainer_name = Column(String(100), nullable=False)

    # Course details
    course_name = Column(String(150), nullable=False)

    # Training session date
    session_date = Column(Date, nullable=False)

    # Ratings (1 to 5) - validation will be handled by Pydantic schemas
    content_rating = Column(Integer, nullable=False)
    trainer_rating = Column(Integer, nullable=False)
    hands_on_rating = Column(Integer, nullable=False)

    # Optional comments
    comments = Column(String(1000), nullable=True)

    # Recommendation status
    would_recommend = Column(Boolean, nullable=False, default=False)
