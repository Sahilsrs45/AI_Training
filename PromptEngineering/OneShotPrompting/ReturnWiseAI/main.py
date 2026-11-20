from fastapi import FastAPI
from models.response_model import ReturnResponse
from models.request_model import ReturnRequest
from services.ai_services import analyze_return

app=FastAPI(title="Analyze ReturnWiseAI",
            version="1.0.1")

@app.get("/")
def home():
    return{
        "message":"Welcome to analysis"
    }
    
@app.post("/api/returnwise/analze" ,response_model=ReturnResponse)
def anlyze_ticket_query(request:ReturnRequest):
    response=analyze_return(request)    
    return response