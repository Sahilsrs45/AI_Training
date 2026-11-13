from openai import OpenAI
from prompts.ai_prompt import (SYSTEM_PROMPT,HUMAN_PROMPT)
import json
from models.ai_model import (EmployeeFeedbackRequest,EmployeeFeedbackResponse)
from config.setting import(AZURE_OPENAI_API_KEY,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINT)
#step 1 create llm
llm=OpenAI(api_key=AZURE_OPENAI_API_KEY,
           base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)


#step 2: define the service function
def analyze_employee_feedback(
    requests:EmployeeFeedbackRequest
)->EmployeeFeedbackResponse:
    user_prompt=HUMAN_PROMPT.format(
        employee_name=requests.employee_name,
        reviewer_name=requests.reviewer_name,
        project_name=requests.project_name,
        performance_rating=requests.performance_rating,
        feedback=requests.feedback
    )
    
    # step 3
    response=llm.responses.create(model=AZURE_OPENAI_DEPLOYMENT,instructions=SYSTEM_PROMPT,
                                  input=user_prompt)
    
    
    #step 4 : extract the generated response
    ai_text=response.output_text
    
    print("ai response :",repr(ai_text))
    #step 5 : converts json string into dictionary
    ai_data=json.loads(ai_text)
    
    #step 6 return pydantic response
    return EmployeeFeedbackResponse.model_validate(ai_data)
