from config.settings import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION
)

from prompts.menu_prompts import (
    SYSTEM_PROMPT,
    HUMAN_PROMPT
)

from models.menu_model import (
    CafeteriaRequest,
    CafeteriaResponse
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI


llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("user", HUMAN_PROMPT)
    ]
)

structured_llm = llm.with_structured_output(
    CafeteriaResponse
)

chain = prompt | structured_llm


def cafeteria_analysis(request: CafeteriaRequest):

    response = chain.invoke(
        {
            "employee_id": request.employee_id,
            "employee_name": request.employee_name,
            "food_preference": request.food_preference,
            "budget": request.budget,
            "question": request.question
        }
    )

    return response