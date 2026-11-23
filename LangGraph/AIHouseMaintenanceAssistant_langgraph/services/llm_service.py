from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from config.settings import (AZURE_OPENAI_ENDPOINT,AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_DEPLOYMENT)
from models.maintenance_model import (MaintenanceRequest,MaintenanceAnswer)
from prompts.maintenance_prompt import (SYSTEMPROMPT,HUMANPROMPT)

llm = AzureChatOpenAI(
   api_key= AZURE_OPENAI_API_KEY,
   azure_endpoint=AZURE_OPENAI_ENDPOINT,
   azure_deployment=AZURE_OPENAI_DEPLOYMENT,
   api_version=AZURE_OPENAI_API_VERSION,
   temperature=0
)

structured_llm = llm.with_structured_output(
    MaintenanceAnswer
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system" ,SYSTEMPROMPT
        ),
        (
            "human",HUMANPROMPT
        )

    ]
)

chain = prompt | structured_llm

def answer_question(request:MaintenanceRequest) -> MaintenanceAnswer:

    result = chain.invoke({
        "question": request.question
    })

    return result
