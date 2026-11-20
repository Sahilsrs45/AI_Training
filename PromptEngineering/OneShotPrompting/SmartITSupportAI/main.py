from fastapi import FastAPI
from models.response_model import ITSupportResponse
from models.request_model import ITSupportRequest
from services.ai_service import analyze_ticket

app=FastAPI(title="Ticket Analysis",
            version="1.0.1")

@app.get("/")
def home():
    return{
        "message":"Welcome to ticket analysis"
    }
    
@app.post("/api/tickets/analze" ,response_model=ITSupportResponse)
def anlyze_ticket_query(request:ITSupportRequest):
    response=analyze_ticket(request)    
    return response