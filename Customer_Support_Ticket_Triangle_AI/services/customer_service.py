import json
from openai import OpenAI
from prompts.customer_prompt import SYSTEM_PROMPT,HUMAN_PROMPT
from models.customer_model import CustomerSupportRequest,CustomerSupportResponse
from config.setting import (AZURE_OPENAI_API_KEY,AZURE_OPENAI_ENDPOINT,AZURE_OPENAI_DEPLOYMENT)

#step 1
llm=OpenAI(
    api_key="AZURE_OPENAI_API_KEY",
    base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)
#step 2
def analyze_ticket(requests:CustomerSupportRequest)->CustomerSupportResponse:
    user_prompt=HUMAN_PROMPT.format(
        ticket_id=requests.ticket_id,
        employee_name=requests.employee_name,
        department=requests.department,
        issue_description=requests.issue_description,
     )
    
    #step 3
    response=llm.responses.create(model=AZURE_OPENAI_DEPLOYMENT,
                                  instructions=SYSTEM_PROMPT,
                                  input=user_prompt)
    #step 4 extract the generated response
    ai_text=response.output_text
    
    print("aicontent :",ai_text)
    #step 5 convert json string to dictionary
    ai_data=json.loads(ai_text)
     
    #step 6
    return CustomerSupportResponse.model_validate(ai_data)