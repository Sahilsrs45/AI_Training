from fastapi import FastAPI
from models.astronaut_model import (
    AstronautRequest,
    AstronautResponse
)
from services.astronaut_service import analyze_astronaut


app = FastAPI(
    title="Astronaut Readiness Analyzer API",
    version="1.0.0",
    description="AI-powered Astronaut Readiness Analysis System"
)


@app.get("/")
def home():
    return {
        "message": "Astronaut Readiness Analyzer API is running"
    }


@app.post(
    "/api/v1/analyze-astronaut", response_model=AstronautResponse)
def analyze_astronaut_api(
    request: AstronautRequest
):
    return analyze_astronaut(request)

