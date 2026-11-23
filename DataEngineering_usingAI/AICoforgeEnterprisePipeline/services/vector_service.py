from pathlib import Path
 
from langchain_openai import AzureOpenAIEmbeddings
from langchain_chroma import Chroma
 
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_ENDPOINT,
    AZURE_EMBEDDING_DEPLOYMENT
)
 
Path("vector_store").mkdir(exist_ok=True)
 
 
embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_EMBEDDING_DEPLOYMENT
)
 
vector_db = Chroma(
    collection_name="coforge_hr_knowledge",
    embedding_function=embeddings,
    persist_directory="./vector_store"
)
 
 
def add_documents(documents, ids):
    vector_db.add_documents(
        documents=documents,
        ids=ids
    )
 
 
def delete_document(document_id):
    existing = vector_db.get(
        where={"document_id": document_id}
    )
 
    ids = existing["ids"]
    if ids:
        vector_db.delete(ids=ids)
    return len(ids)
 
 
def search_documents(question, k=3):
    results = vector_db.similarity_search(
        question,
        k=k
    )
 
    return [
        {
            "context": doc.page_content,
            "metadata": doc.metadata
        }
        for doc in results
    ]
 