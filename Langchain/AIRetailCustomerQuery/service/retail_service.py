from prompts.prompt import (
    SYSTEM_PROMPT,
    HUMAN_PROMPT
)

from model.retail_model import (
    CustomerRequest,
    CustomerResponse
)

from config.setting import (
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
    api_version=AZURE_OPENAI_API_VERSION
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("user", HUMAN_PROMPT)
    ]
)

structured_llm = llm.with_structured_output(
    CustomerResponse
)

chain = prompt | structured_llm


def customer_assistance(request: CustomerRequest):

    response = chain.invoke(
        {
            "customer_id": request.customer_id,
            "customer_name": request.customer_name,
            "product_name": request.product_name,
            "query": request.query
        }
    )

    return response