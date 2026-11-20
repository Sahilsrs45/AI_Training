from openai import AzureOpenAI
from config.settings import (AZURE_OPENAI_API_KEY,
                             AZURE_OPENAI_API_VERSION,
                             AZURE_OPENAI_DEPLOYMENT,
                             AZURE_OPENAI_ENDPOINT)
from models.ai_model import(StudentAnalysis,StudentRequest,StudentResponse)
from prompts.ai_prompt import (SYSTEM_PROMPT,HUMAN_PROMPT)
import json
llm=AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)
def analyze_student_profile(request:StudentRequest)->StudentResponse:
    user_prompt=HUMAN_PROMPT.format(
        student_id=request.student_id,
        student_name=request.student_name,
        course=request.course,
        semester=request.semester,
        percentage=request.percentage,
        primary_skill=request.primary_skill,
        career_goal=request.career_goal
    
        
    )
     #call llm
    response=llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role":"system",
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
        raise ValueError("LLM returns empty response") 
    
    ai_analysis=StudentAnalysis(**json.loads(ai_text)) 
    return StudentResponse(  
               student_id=request.student_id,
               student_name=request.student_name,
               prompting_technique="Onbe shot prompting",
               ai_analysis=ai_analysis)