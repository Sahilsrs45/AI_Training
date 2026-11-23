from langchain_openai import AzureChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

from config.settings import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)

from models.cafeteria_model import EscalationResponse

from prompts.escalation_prompt import (
    SYSTEMPROMPT,
    HUMANPROMPT
)


llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)

structured_llm = llm.with_structured_output(
    EscalationResponse
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEMPROMPT),
        ("human", HUMANPROMPT)
    ]
)

chain = prompt | structured_llm


def generate_escalation(
    order_id,
    employee_id,
    food_items,
    elapsed_minutes,
    priority,
    recipient
):

    result = chain.invoke({
        "order_id": order_id,
        "employee_id": employee_id,
        "food_items": food_items,
        "elapsed_minutes": elapsed_minutes,
        "priority": priority,
        "recipient": recipient
    })

    return result