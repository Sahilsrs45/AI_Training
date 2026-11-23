from pydantic import BaseModel, Field
from typing import Literal


class TrainingRequest(BaseModel):

    employee_id: int = Field(..., gt=0)

    employee_name: str = Field(..., min_length=2)

    topic: Literal["Python", "FastAPI", "LangChain"]

    question: str = Field(..., min_length=10)


class TrainingAnalysis(BaseModel):

    category: Literal["Concept", "Coding", "Career", "Other"]

    difficulty: Literal["Beginner", "Intermediate", "Advanced"]

    priority: Literal["Low", "Medium", "High"]

    summary: str


class TrainingResponse(BaseModel):

    answer: str

    recommended_action: str

    status: str