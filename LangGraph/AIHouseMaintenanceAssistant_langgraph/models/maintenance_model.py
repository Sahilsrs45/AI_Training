from pydantic import BaseModel, Field

class MaintenanceRequest(BaseModel):

    question: str = Field(min_length = 3)


class MaintenanceAnswer(BaseModel):

    answer: str


class MaintenanceResponse(BaseModel):

    question: str
    answer: str
