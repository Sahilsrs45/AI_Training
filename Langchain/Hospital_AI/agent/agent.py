from langchain.agents import create_agent
 
from langchain_openai import AzureChatOpenAI
 
from prompts.hospital_prompt import HOSPITAL_SYSTEM_PROMPT
 
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)
 
from tools.hospital_tools import (
    register_patient,
    check_doctor_availability,
    book_appointment,
    get_patient_medical_records,
    calculate_hospital_bill
)
 
 
def create_hospital_agent():
 
    # Step 1: Connect to Azure OpenAI
 
    llm = AzureChatOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT
    )
 
    # Step 2: Register five tools
 
    hospital_tools = [
        register_patient,
        check_doctor_availability,
        book_appointment,
        get_patient_medical_records,
        calculate_hospital_bill
    ]
 
    # Step 3: Create AI Agent
 
    agent = create_agent(
        model=llm,
        tools=hospital_tools,
        system_prompt=HOSPITAL_SYSTEM_PROMPT
    )
 
    return agent