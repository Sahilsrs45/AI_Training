from fastapi import APIRouter
from models.training_model import (
    TrainingRequest,
    TrainingResponse
)

from service.training_service import (
    training_analysis
)


router=APIRouter(
    prefix="/trainig",
    tags=["Training Support"]
)


@router.post("/ask",response_model=TrainingResponse)
def ask_question(request:TrainingRequest):
    response=training_analysis(request)
    
    return response