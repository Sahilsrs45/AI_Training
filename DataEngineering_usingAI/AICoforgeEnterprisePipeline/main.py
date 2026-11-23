from fastapi import FastAPI
 
from routers.employee_router import (
    router as employee_router
)
from routers.knowledge_router import (
    router as knowledge_router
)
app = FastAPI(
    title="Coforge Enterprise knowledge and data pipeline",
    description=(
        "Enterprise Data Engineering and RAG."
    ),
    version="1.0.1"
)
 
 
@app.get("/")
def home():
    return {
        "home"
    }
 
 
@app.get("/health")
def health():
    return {
        "status": "health"
    }
 
 
app.include_router(employee_router)
app.include_router(knowledge_router)
 