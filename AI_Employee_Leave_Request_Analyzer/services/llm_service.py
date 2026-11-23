from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from config.settings import *
from models.leave_model import LeaveRequest, LeaveResponse
from prompts.leave_prompt import SYSTEMPROMPT, HUMANPROMPT

llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)

structured_llm = llm.with_structured_output(LeaveResponse)
prompt = ChatPromptTemplate.from_messages([('system', SYSTEMPROMPT), ('human', HUMANPROMPT)])
chain = prompt | structured_llm

def analyze_leave(request: LeaveRequest):
    return chain.invoke({
        'employee_id': request.employee_id,
        'employee_name': request.employee_name,
        'leave_type': request.leave_type,
        'number_of_days': request.number_of_days,
        'reason': request.reason
    })
