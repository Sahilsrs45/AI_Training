from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate
)

from config.azure_config import(
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION
)

from prompts.escalation_prompt import(
    SYSTEM_PROMPT,
    HUMAN_PROMPT
)

llm = AzureChatOpenAI(

    api_key=AZURE_OPENAI_API_KEY,

    azure_endpoint=
    AZURE_OPENAI_ENDPOINT,

    azure_deployment=
    AZURE_OPENAI_DEPLOYMENT,

    api_version=
    AZURE_OPENAI_API_VERSION
)

prompt = ChatPromptTemplate.from_messages(
[
    ("system",SYSTEM_PROMPT),
    ("human",HUMAN_PROMPT)
]
)

chain = prompt | llm

def generate_escalation(input_data):
    result = chain.invoke(input_data)
    return result.content