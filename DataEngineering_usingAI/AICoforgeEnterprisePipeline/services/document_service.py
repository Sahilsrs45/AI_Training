from pathlib import Path
import hashlib
from pypdf import PdfReader
from langchain_text_splitters import (RecursiveCharacterTextSplitter)
from langchain_core.documents import Document
from services.vector_service import (
   add_documents,
   delete_document,
   vector_db
)
POLICY_FOLDER = Path("data/policies")

def calculate_hash(file_path):
   content = Path(file_path).read_bytes()
   return hashlib.sha256(content).hexdigest()

def extract_pdf_text(file_path):
   reader = PdfReader(str(file_path))
   text = ""
   for page in reader.pages:
       text += (page.extract_text() or "") + "\n"
   return text.strip()

def ingest_document(filename):
   file_path = POLICY_FOLDER / filename
   if not file_path.is_file():
       raise FileNotFoundError(filename)
   if file_path.suffix.lower() != ".pdf":
       raise ValueError("Only PDF files are supported")
   document_id = filename
   file_hash = calculate_hash(file_path)
   existing = vector_db.get(
       where={"document_id": document_id}
   )
   if existing["ids"]:
       old_hash = existing["metadatas"][0].get(
           "file_hash"
       )
       if old_hash == file_hash:
           return {
               "status": "unchanged",
               "document": filename
           }
   text = extract_pdf_text(file_path)
   if not text:
       raise ValueError("No extractable text found")
   splitter = RecursiveCharacterTextSplitter(
       chunk_size=600,
       chunk_overlap=100
   )
   chunks = splitter.split_text(text)
   documents = []
   ids = []
   for index, chunk in enumerate(chunks):
       documents.append(
           Document(
               page_content=chunk,
               metadata={
                   "document_id": document_id,
                   "source": filename,
                   "file_hash": file_hash,
                   "chunk_index": index
               }
           )
       )
       ids.append(
           f"{document_id}_{file_hash}_{index}"
       )
   # Generate and store new vectors first.
   add_documents(documents, ids)
   # Remove old versions after the new vectors exist.
   old_ids = [
       old_id
       for old_id in existing["ids"]
       if old_id not in ids
   ]
   if old_ids:
       vector_db.delete(ids=old_ids)
   return {
       "status": "indexed",
       "document": filename,
       "chunks": len(chunks)
   }

def ingest_all_documents():
   results = []
   for file in sorted(POLICY_FOLDER.glob("*.pdf")):
       results.append(
           ingest_document(file.name)
       )
   return results

def remove_document(filename):
   count = delete_document(filename)
   return {
       "status": "deleted",
       "document": filename,
       "deleted_chunks": count
   }