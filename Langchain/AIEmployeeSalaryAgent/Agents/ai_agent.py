from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI
from prompts.ai_prompt import SALARY_SYSTEM_PROMPT


from config.settings import (AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINT)

from tools.ai_tool import(
    calculate_basic_salary,
    calculate_hra,
    calculate_da,
    calculate_gross_salary
    
)


def create_salary_agent():
    #step 1: connect to azure openai
    llm=AzureChatOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT,
        
    )
    
    #step 2 register four tools
    salary_tools=[calculate_basic_salary,
                  calculate_hra,
                  calculate_da,
                  calculate_gross_salary]
    
    #step 3 Create AI Agent(calling agent)
    agent=create_agent(
        model=llm,
        tools=salary_tools,
        system_prompt=SALARY_SYSTEM_PROMPT
    )
    return agent