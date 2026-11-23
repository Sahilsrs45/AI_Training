from prompts.prompt import (
    SYSTEM_PROMPT,
    HUMAN_PROMPT
)

from models.training_model import (
    TrainingRequest,
    TrainingResponse
)

from config.settings import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI


llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION,
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("user", HUMAN_PROMPT)
    ]
)

structured_llm = llm.with_structured_output(
    TrainingResponse
)

chain = prompt | structured_llm


def training_analysis(request: TrainingRequest):

    response = chain.invoke(
        {
            "employee_id": request.employee_id,
            "employee_name": request.employee_name,
            "topic": request.topic,
            "question": request.question
        }
    )

    return response