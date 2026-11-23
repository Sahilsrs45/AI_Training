from fastapi import APIRouter, HTTPException
from models.request_model import (
   KnowledgeRequest,
   SearchRequest
)
from services.document_service import (
   ingest_document,
   ingest_all_documents,
   remove_document
)
from services.vector_service import search_documents
from services.rag_service import ask_hr_question

router = APIRouter(
   prefix="/knowledge",
   tags=["HR Knowledge Pipeline"]
)

@router.post("/ingest-all")
def ingest_all():
   return ingest_all_documents()

@router.post("/ingest/{filename}")
def ingest_single(filename: str):
   try:
       return ingest_document(filename)
   except FileNotFoundError:
       raise HTTPException(
           status_code=404,
           detail="Document not found"
       )
   except ValueError as error:
       raise HTTPException(
           status_code=400,
           detail=str(error)
       )

@router.delete("/{filename}")
def delete_policy(filename: str):
   return remove_document(filename)

@router.post("/search")
def search_policy(request: SearchRequest):
   return search_documents(
       request.question,
       request.k
   )

@router.post("/ask")
def ask_policy(request: KnowledgeRequest):
   return ask_hr_question(
       request.question
   )