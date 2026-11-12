
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from sqlalchemy.exc import SQLAlchemyError

from models.trainingfeedback_model import TrainingFeedback
from schemas.trainingfeedback_schema import TrainingFeedbackCreate
from config.logger import logger


# 1. Submit new feedback
def create_feedback(db: Session, feedback_data: TrainingFeedbackCreate):

    try:
        feedback = TrainingFeedback(**feedback_data.model_dump())

        db.add(feedback)
        db.commit()
        db.refresh(feedback)

        logger.info(
            "Feedback created successfully. ID: %s",
            feedback.feedback_id
        )

        return feedback

    except SQLAlchemyError:
        db.rollback()
        logger.exception("Database error while creating feedback")
        raise


# 2. Get all feedback with pagination
def get_all_feedback(db: Session, skip: int = 0, limit: int = 10):

    try:
        feedback_list = (
            db.query(TrainingFeedback)
            .offset(skip)
            .limit(limit)
            .all()
        )

        return feedback_list

    except SQLAlchemyError:
        logger.exception("Database error while retrieving feedback")
        raise


# 3. Get feedback by ID
def get_feedback_by_id(db: Session, feedback_id: int):

    try:
        feedback = db.get(TrainingFeedback, feedback_id)

        if feedback is None:
            logger.warning("Feedback ID %s not found", feedback_id)

        return feedback

    except SQLAlchemyError:
        logger.exception("Database error while retrieving feedback by ID")
        raise


# 4. Update existing feedback
def update_feedback(db: Session, feedback_id: int, update_data: dict):

    try:
        feedback = db.get(TrainingFeedback, feedback_id)

        if feedback is None:
            logger.warning("Cannot update. Feedback ID %s not found", feedback_id)
            return None

        for field, value in update_data.items():
            setattr(feedback, field, value)

        db.commit()
        db.refresh(feedback)

        logger.info("Feedback ID %s updated successfully", feedback_id)

        return feedback

    except SQLAlchemyError:
        db.rollback()
        logger.exception("Database error while updating feedback")
        raise


# 5. Delete feedback
def delete_feedback(db: Session, feedback_id: int):

    try:
        feedback = db.get(TrainingFeedback, feedback_id)

        if feedback is None:
            logger.warning("Cannot delete. Feedback ID %s not found", feedback_id)
            return None

        db.delete(feedback)
        db.commit()

        logger.info("Feedback ID %s deleted successfully", feedback_id)

        return feedback_id

    except SQLAlchemyError:
        db.rollback()
        logger.exception("Database error while deleting feedback")
        raise


# 6. Filter feedback by trainer name
def get_feedback_by_trainer(db: Session, trainer_name: str):

    try:
        feedback_list = (
            db.query(TrainingFeedback)
            .filter(
                func.lower(TrainingFeedback.trainer_name)
                == trainer_name.lower()
            )
            .all()
        )

        return feedback_list

    except SQLAlchemyError:
        logger.exception("Database error while filtering by trainer")
        raise


# 7. Filter feedback by course name
def get_feedback_by_course(db: Session, course_name: str):

    try:
        feedback_list = (
            db.query(TrainingFeedback)
            .filter(
                func.lower(TrainingFeedback.course_name)
                == course_name.lower()
            )
            .all()
        )

        return feedback_list

    except SQLAlchemyError:
        logger.exception("Database error while filtering by course")
        raise


# 8. Calculate average trainer rating for each trainer
def get_trainer_average_ratings(db: Session):

    try:
        results = (
            db.query(
                TrainingFeedback.trainer_name,
                func.avg(TrainingFeedback.trainer_rating).label(
                    "average_trainer_rating"
                )
            )
            .group_by(TrainingFeedback.trainer_name)
            .all()
        )

        return [
            {
                "trainer_name": row.trainer_name,
                "average_trainer_rating": round(
                    float(row.average_trainer_rating), 2
                )
            }
            for row in results
        ]

    except SQLAlchemyError:
        logger.exception("Database error while calculating trainer averages")
        raise


# 9. Find low-rated sessions
# A session is low-rated if ANY one of its three ratings is 2 or below.
def get_low_rated_feedback(db: Session):

    try:
        feedback_list = (
            db.query(TrainingFeedback)
            .filter(
                or_(
                    TrainingFeedback.content_rating <= 2,
                    TrainingFeedback.trainer_rating <= 2,
                    TrainingFeedback.hands_on_rating <= 2
                )
            )
            .all()
        )

        return feedback_list

    except SQLAlchemyError:
        logger.exception("Database error while finding low-rated feedback")
        raise


# 10. Calculate recommendation percentage for a course
def get_recommendation_percentage(db: Session, course_name: str):

    try:
        total_feedback = (
            db.query(func.count(TrainingFeedback.feedback_id))
            .filter(
                func.lower(TrainingFeedback.course_name)
                == course_name.lower()
            )
            .scalar()
        )

        recommended_count = (
            db.query(func.count(TrainingFeedback.feedback_id))
            .filter(
                func.lower(TrainingFeedback.course_name)
                == course_name.lower(),
                TrainingFeedback.would_recommend.is_(True)
            )
            .scalar()
        )

        # Avoid division by zero
        if total_feedback == 0:
            percentage = 0.0
        else:
            percentage = (recommended_count / total_feedback) * 100

        return {
            "course_name": course_name,
            "total_feedback": total_feedback,
            "recommended_count": recommended_count,
            "recommendation_percentage": round(percentage, 2)
        }

    except SQLAlchemyError:
        logger.exception(
            "Database error while calculating recommendation percentage"
        )
        raise
