
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from config.database import engine, Base, get_db
from config.logger import logger

# Import the model so SQLAlchemy registers its table
from models.trainingfeedback_model import TrainingFeedback

from schemas.trainingfeedback_schema import (
    TrainingFeedbackCreate,
    TrainingFeedbackUpdate,
    TrainingFeedbackResponse,
    TrainerAverageResponse,
    RecommendationPercentageResponse
)

from services import trainingfeedback_service as service


# Create FastAPI application
app = FastAPI(
    title="Corporate Training Feedback API",
    description="API for managing corporate training feedback",
    version="1.0.0"
)


# Create database tables
@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
    logger.info("Training Feedback API started")

# --------------------------------------------------
# 1. SUBMIT NEW FEEDBACK
# --------------------------------------------------

@app.post(
    "/feedback",
    response_model=TrainingFeedbackResponse,
    status_code=201
)
def create_feedback(
    feedback_data: TrainingFeedbackCreate,
    db: Session = Depends(get_db)
):
    try:
        return service.create_feedback(db, feedback_data)

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Feedback ID already exists"
        )

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while creating feedback"
        )

    except Exception:
        logger.exception("Unexpected error while creating feedback")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# 2. GET ALL FEEDBACK WITH PAGINATION
# --------------------------------------------------

@app.get(
    "/feedback",
    response_model=list[TrainingFeedbackResponse]
)
def get_all_feedback(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    try:
        return service.get_all_feedback(db, skip, limit)

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while retrieving feedback"
        )

    except Exception:
        logger.exception("Unexpected error while retrieving feedback")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# 3. FILTER FEEDBACK BY TRAINER NAME
# --------------------------------------------------

@app.get(
    "/feedback/trainer/{trainer_name}",
    response_model=list[TrainingFeedbackResponse]
)
def get_feedback_by_trainer(
    trainer_name: str,
    db: Session = Depends(get_db)
):
    try:
        return service.get_feedback_by_trainer(db, trainer_name)

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while filtering by trainer"
        )

    except Exception:
        logger.exception("Unexpected error while filtering by trainer")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# 4. FILTER FEEDBACK BY COURSE NAME
# --------------------------------------------------

@app.get(
    "/feedback/course/{course_name}",
    response_model=list[TrainingFeedbackResponse]
)
def get_feedback_by_course(
    course_name: str,
    db: Session = Depends(get_db)
):
    try:
        return service.get_feedback_by_course(db, course_name)

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while filtering by course"
        )

    except Exception:
        logger.exception("Unexpected error while filtering by course")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# 5. GET AVERAGE TRAINER RATINGS
# --------------------------------------------------

@app.get(
    "/feedback/trainer-averages",
    response_model=list[TrainerAverageResponse]
)
def get_trainer_average_ratings(
    db: Session = Depends(get_db)
):
    try:
        return service.get_trainer_average_ratings(db)

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while calculating trainer averages"
        )

    except Exception:
        logger.exception("Unexpected error calculating trainer averages")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# 6. GET LOW-RATED SESSIONS
# --------------------------------------------------

@app.get(
    "/feedback/low-rated",
    response_model=list[TrainingFeedbackResponse]
)
def get_low_rated_feedback(
    db: Session = Depends(get_db)
):
    try:
        return service.get_low_rated_feedback(db)

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while finding low-rated feedback"
        )

    except Exception:
        logger.exception("Unexpected error finding low-rated feedback")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# 7. GET COURSE RECOMMENDATION PERCENTAGE
# --------------------------------------------------

@app.get(
    "/feedback/recommendation/{course_name}",
    response_model=RecommendationPercentageResponse
)
def get_recommendation_percentage(
    course_name: str,
    db: Session = Depends(get_db)
):
    try:
        return service.get_recommendation_percentage(db, course_name)

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while calculating recommendation percentage"
        )

    except Exception:
        logger.exception("Unexpected error calculating recommendation percentage")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# 8. GET FEEDBACK BY ID
# --------------------------------------------------

@app.get(
    "/feedback/{feedback_id}",
    response_model=TrainingFeedbackResponse
)
def get_feedback_by_id(
    feedback_id: int,
    db: Session = Depends(get_db)
):
    try:
        feedback = service.get_feedback_by_id(db, feedback_id)

        if feedback is None:
            raise HTTPException(
                status_code=404,
                detail="Feedback not found"
            )

        return feedback

    except HTTPException:
        raise

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while retrieving feedback"
        )

    except Exception:
        logger.exception("Unexpected error retrieving feedback")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# 9. UPDATE EXISTING FEEDBACK
# --------------------------------------------------

@app.patch(
    "/feedback/{feedback_id}",
    response_model=TrainingFeedbackResponse
)
def update_feedback(
    feedback_id: int,
    update_data: TrainingFeedbackUpdate,
    db: Session = Depends(get_db)
):
    try:
        update_dict = update_data.model_dump(exclude_unset=True)

        if not update_dict:
            raise HTTPException(
                status_code=422,
                detail="Provide at least one field to update"
            )

        feedback = service.update_feedback(
            db,
            feedback_id,
            update_dict
        )

        if feedback is None:
            raise HTTPException(
                status_code=404,
                detail="Feedback not found"
            )

        return feedback

    except HTTPException:
        raise

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while updating feedback"
        )

    except Exception:
        logger.exception("Unexpected error updating feedback")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# 10. DELETE FEEDBACK
# --------------------------------------------------

@app.delete("/feedback/{feedback_id}")
def delete_feedback(
    feedback_id: int,
    db: Session = Depends(get_db)
):
    try:
        deleted_id = service.delete_feedback(db, feedback_id)

        if deleted_id is None:
            raise HTTPException(
                status_code=404,
                detail="Feedback not found"
            )

        return {
            "message": "Feedback deleted successfully",
            "feedback_id": deleted_id
        }

    except HTTPException:
        raise

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while deleting feedback"
        )

    except Exception:
        logger.exception("Unexpected error deleting feedback")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# --------------------------------------------------
# ROOT ENDPOINT
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to Corporate Training Feedback API",
        "documentation": "/docs"
    }
