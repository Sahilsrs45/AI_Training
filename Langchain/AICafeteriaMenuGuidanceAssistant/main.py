from fastapi import FastAPI

from models.menu_model import (
    CafeteriaRequest,
    CafeteriaResponse
)

from services.menu_service import cafeteria_analysis


app = FastAPI(
    title="AI Cafeteria Recommendation System",
    version="1.0.1"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Cafeteria Recommendation System"
    }


@app.post(
    "/api/v1/cafeteria",
    response_model=CafeteriaResponse
)
def analyze_cafeteria(request: CafeteriaRequest):

    response = cafeteria_analysis(request)

    return response