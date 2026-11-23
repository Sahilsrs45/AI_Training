from langchain_openai import AzureChatOpenAI
from langchain_community.vectorstores import FAISS
from config.settings import (
    OPENAI_API_KEY,
    OPENAI_API_VERSION,
    OPENAI_ENDPOINT,
    OPENAI_MODEL_NAME
)
 
from service.ingestion_service import (
    get_embeddings,
    VECTOR_PATH
)
 
from prompt.rag_prompt import (
    SYSTEM_PROMPT,
    HUMAN_PROMPT
)
 
llm = AzureChatOpenAI(
    azure_endpoint=OPENAI_ENDPOINT,
    api_key=OPENAI_API_KEY,
    api_version=OPENAI_API_VERSION,
    azure_deployment=OPENAI_MODEL_NAME
)
 
 
def ask_hr_policy(question: str):
    embeddings = get_embeddings()
 
    # Load only the trusted index created by this app
    vector_store = FAISS.load_local(
        str(VECTOR_PATH),
        embeddings,
        allow_dangerous_deserialization=True
    )
 
    # Retrieve relevant documents
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )
    
    docs = vector_store.similarity_search(question, k=3)

    print("\nQUESTION:", question)
    print("\nRETRIEVED DOCS:")

    for i, doc in enumerate(docs):
        print(f"\nDOC {i+1}")
        print(doc.page_content)
 
    documents = retriever.invoke(question)
 
    if not documents:
        return {
            "question": question,
            "answer": "Information is not available in the HR policy.",
            "sources": []
        }
 
    # Build context
    context = "\n\n".join(
        doc.page_content for doc in documents
    )
 
    user_prompt = HUMAN_PROMPT.format(
        context=context,
        question=question
    )
 
    # invoke LLM
    response = llm.invoke([
        ("system", SYSTEM_PROMPT),
        ("human", user_prompt)
    ])
 
    sources = list({
        doc.metadata.get("source", "Unknown")
        for doc in documents
    })
 
    return {
        "question": question,
        "answer": response.content,
        "sources": sources
    }