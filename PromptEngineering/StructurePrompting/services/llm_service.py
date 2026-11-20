from openai import AzureOpenAI
from models.structure_model import LearnerRequest,LearnerResponse,LearnerAnalysis
import json
from prompts.structure_prompt import HUMAN_Prompt,SYSTEM_PROMPT

from config.setting import (AZURE_OPENAI_API_DEPLOYMENT,
                            AZURE_OPENAI_API_KEY,
                            AZURE_OPENAI_API_VERSION,
                            AZURE_OPENAI_ENDPOINT)

llm=AzureOpenAI(api_key=AZURE_OPENAI_API_KEY,
                api_version=AZURE_OPENAI_API_VERSION,
                azure_deployment=AZURE_OPENAI_API_DEPLOYMENT,
                azure_endpoint=AZURE_OPENAI_ENDPOINT)

#average score
def calculluate_average_score(request:LearnerRequest)->float:
    average=(request.pythonScore + request.sqlScore + request.fastApiScore)/3
    return round(average,2)

# performance level
def calculate_performance(average_score:float)->str:
    if average_score >=85:
        return "Excellent"
    elif average_score>=70:
        return "Good"
    elif average_score>=50:
        return "Needs Improvement"
    else:
        return "Critical"
    
#Strong and weak subject
def identify_technologies(request: LearnerRequest):
   python = request.pythonScore
   sql = request.sqlScore
   fastapi = request.fastApiScore
   if python >= sql and python >= fastapi:
       strongest = "Python"
   elif sql >= python and sql >= fastapi:
       strongest = "SQL"
   else:
       strongest = "FastAPI"
   if python <= sql and python <= fastapi:
       weakest = "Python"
   elif sql <= python and sql <= fastapi:
       weakest = "SQL"
   else:
       weakest = "FastAPI"
   return strongest, weakest


#assignment completion %
def calculate_assignment_percentage(request:LearnerRequest)->float:
    percentage=(request.assignemtsCompleted/request.totalAssignemts)*100
    return round(percentage,2)

#

def analyzer(request: LearnerRequest) -> LearnerResponse:

    average_score = calculluate_average_score(request)

    performance = calculate_performance(
        average_score
    )

    strongest, weakest = identify_technologies(
        request
    )

    completion_percentage = (
        calculate_assignment_percentage(
            request
        )
    )

    user_prompt = HUMAN_Prompt.format(
        learnerName=request.learnerName,
        department=request.department,
        pythonScore=request.pythonScore,
        sqlScore=request.sqlScore,
        fastApiScore=request.fastApiScore,
        attendancePercentage=request.attendancePercentage,
        assignemtsCompleted=request.assignemtsCompleted,
        totalAssignemts=request.totalAssignemts,
        averageScore=average_score,
        performance=performance,
        strongestTechnology=strongest,
        weakestTechnology=weakest,
        completionPercentage=completion_percentage
    )

    response = llm.chat.completions.create(
        model=AZURE_OPENAI_API_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    result = response.choices[0].message.content

    if not result:
        raise ValueError(
            "LLM returned an empty response"
        )

    data = json.loads(result)

    ai_analysis = LearnerAnalysis(**data)

    return LearnerResponse(
        learnerName=request.learnerName,
        department=request.department,
        analysis=ai_analysis,
        finalRecommendation=data["finalRecommendation"]
    )

