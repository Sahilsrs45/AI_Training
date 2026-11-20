from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (AZURE_OPENAI_API_KEY,
                             AZURE_OPENAI_API_VERSION,
                             AZURE_OPENAI_DEPLOYMENT,
                             AZURE_OPENAI_ENDPOINT)

from models.request_model import IncidentRequest
from models.response_model import IncidentResponse
from models.analysis_model import IncidentAnalysis

from prompts.incident_prompt import (SYSTEM_PROMPT,HUMAN_PROMPT)

llm=AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION
)


prompt=ChatPromptTemplate.from_messages([
    ("system",SYSTEM_PROMPT),
    ("user",HUMAN_PROMPT)
])


structured_llm=llm.with_structured_output(
    IncidentAnalysis
)

incident_chain=prompt | structured_llm



def analyze_incident(data):
    result = incident_chain.invoke({

        "employee_id": data["employee_id"],
        "employee_name": data["employee_name"],
        "department": data["department"],
        "issue": data["issue"]

    })

    return result