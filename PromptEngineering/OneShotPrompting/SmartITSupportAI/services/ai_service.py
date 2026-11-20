import json
from config.settings import (AZURE_OPENAI_API_KEY,
                             AZURE_OPENAI_API_VERSION
                             ,AZURE_OPENAI_DEPLOYMENT,
                            AZURE_OPENAI_ENDPOINT)

from models.analysis_model import ITSupportAnalysis
from models.request_model import ITSupportRequest
from models.response_model import ITSupportResponse

from prompts.one_shot_prompt import (HUMAN_PROMPT,SYSTEM_PROMPT)
from openai import AzureOpenAI

#step1 
llm=AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
                azure_endpoint=AZURE_OPENAI_ENDPOINT,
                azure_deployment=AZURE_OPENAI_DEPLOYMENT,
                api_version=AZURE_OPENAI_API_VERSION)



def analyze_ticket(request:ITSupportRequest)->ITSupportResponse:
    
    user_prompt=HUMAN_PROMPT.format(
        ticket_id=request.ticket_id,
        employee_id=request.employee_id,
        employee_name=request.employee_name,
        department=request.department,
        issue_description=request.issue_description,
        affected_system=request.affected_system
            
    )
    
    #step 3 call llm
    response=llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            
            {"role":"system",
             "content":SYSTEM_PROMPT
                
            },
            {
                "role":"user",
                "content":user_prompt
                
            }
        ],response_format={"type":"json_object"}
    )
    
    #extract ai response
    ai_text=response.choices[0].message.content
    
    if not ai_text:
        raise ValueError("LLM return empty response")
    
    ai_data=json.loads(ai_text)
    
    ai_analysis=ITSupportAnalysis(**ai_data)
    
    
    #recommended actions
    recommended_actions=[
        f"Perform the following action:{step}"
        for step in ai_analysis.troubleshooting_steps
    ]
    
    #Escalating logic
    escalation_required=(
        ai_analysis.priority_level in ["High","Critical"]
    )
    
    if escalation_required:
        recommended_actions.append(
            "Escalate the ticket to the IT support team"
        )
    else:
        recommended_actions.append(
            "Monitor the issue and contact IT support if its persists."
        )
        
        
    #summary
    ai_summary=(
        f"Ticket {request.ticket_id} reported by "
        f"{request.employee_name} is categorized as "
        f"{ai_analysis.issue_category } with"
        f"{ai_analysis.priority_level} priority"
        f"The suspected root cause is "
        f"{ai_analysis.suspected_root_cause}."
    )    
    
    
    return ITSupportResponse(
        ticket_id=request.ticket_id,
        ticket_status=request.ticket_status,
        analysis=ai_analysis,
        recommended_actions=recommended_actions,
        escalated_required=escalation_required,
        ai_summary=ai_summary
    )