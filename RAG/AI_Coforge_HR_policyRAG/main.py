from fastapi import FastAPI
 
from model.rag_model import (
    RAGRequest,
    RAGResponse
)
 
from service.ingestion_service import (
    create_vector_store
)
 
from service.rag_service import (
    ask_hr_policy
)
 
 
app = FastAPI(
    title="Coforge HR Policy RAG Assistant",
    version="1.0"
)
 
 
@app.post("/api/hr/ingest")
def ingest_documents():
    return create_vector_store()
 
 
@app.post("/api/hr/ask", response_model=RAGResponse)
def ask_question(request: RAGRequest):
    return ask_hr_policy(request.question)
 
 
@app.get("/")
def home():
    return {
        "message": "HR Policy RAG Assistant is running. Use /docs for API documentation."
    }
 
 
@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "application": "HR Policy RAG"
    }
 