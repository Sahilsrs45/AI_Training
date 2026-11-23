from config.settings import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION
)

from prompts.helpdesk_prompt import (
    SYSTEM_PROMPT,
    HUMAN_PROMPT
)

from models.helpdesk_model import (
    HelpdeskRequest,
    HelpdeskResponse
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI


llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("user", HUMAN_PROMPT)
    ]
)

structured_llm = llm.with_structured_output(
    HelpdeskResponse
)

chain = prompt | structured_llm


def helpdesk_analysis(request: HelpdeskRequest):

    response = chain.invoke(
        {
            "employee_id": request.employee_id,
            "employee_name": request.employee_name,
            "issue_type": request.issue_type,
            "issue_description": request.issue_description
        }
    )

    return response