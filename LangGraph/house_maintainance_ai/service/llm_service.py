from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (AZURE_OPENAI_API_KEY,
                             AZURE_OPENAI_API_VERSION,
                             AZURE_OPENAI_DEPLOYMENT,
                             AZURE_OPENAI_ENDPOINT)

from prompts.maintenance_prompt import (HUMAN_PROMPT,SYSTEM_PROMPT)

from models.request_model import MaintenanceRequest
from models.response_model import MaintenanceResponse

llm=AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT
)

structured_llm=llm.with_structured_output(MaintenanceResponse)


prompt=ChatPromptTemplate.from_messages(
    [
        ("system",SYSTEM_PROMPT),
        ("user",HUMAN_PROMPT)
    ]
)

chain=prompt | structured_llm

def analyze_maintenance(request:MaintenanceRequest)->MaintenanceResponse:
    
    result=chain.invoke({
        "question":request.question
    })
    
    return MaintenanceResponse(
        question=request.question,
        answer=result.answer
    )