import os
from dotenv import load_dotenv

from crewai import LLM

load_dotenv

AZURE_ENDPOINT=os.getenv("OPENAI_ENDPOINT")
OPENAI_DEPLOYMENT=os.getenv("OPENAI_DEPLOYMENT")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
OPENAI_API_VERSION=os.getenv("OPENAI_API_VERSION")
if not all([AZURE_ENDPOINT,
            OPENAI_DEPLOYMENT,
            OPENAI_API_KEY,OPENAI_API_VERSION
    
]):
    raise ValueError(
        "Azure OpenAI configuration is missing"
    )
    
    
#configure azuure openai env variable
os.environ["AZURE_ENDPOINT"]=AZURE_ENDPOINT
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY
os.environ["OPENAI_DEPLOYMENT"]=OPENAI_DEPLOYMENT
os.environ["OPENAI_API_VERSION"]=OPENAI_API_VERSION


#create CrewAI LLM
llm=LLM(
    model=f"azure/{OPENAI_DEPLOYMENT}",
    endpoint=AZURE_ENDPOINT,
    api_key=OPENAI_API_KEY,
    api_version=OPENAI_API_VERSION
    
)    