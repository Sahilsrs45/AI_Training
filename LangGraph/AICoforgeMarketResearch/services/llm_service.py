from langchain_openai import AzureChatOpenAI

from config.settings import (AZURE_OPENAI_API_KEY,
                             AZURE_OPENAI_API_VERSION,
                             AZURE_OPENAI_DEPLOYMENT,
                             AZURE_OPENAI_ENDPOINT)

def create_llm():
    llm=AzureChatOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT
        
    )
    return llm

