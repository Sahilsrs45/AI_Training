from openai import AzureOpenAI

from config.settings import (AZURE_OPENAI_API_KEY,
                             AZURE_OPENAI_ENDPOINT,
                             AZURE_OPENAI_API_VERSION,
                             AZURE_OPENAI_DEPLOYMENT)
from models.request_model import LearnerProgressRequest
from models.analysis_model import LearnerProgressAnalysis
from models.response_model import LearnerProgressResponse
from prompts.one_shot_prompt import (SYSTEM_PROMPT,HUMAN_PROMPT)
import json

#step1
llm=AzureOpenAI(api_key=AZURE_OPENAI_API_KEY,
                azure_endpoint=AZURE_OPENAI_ENDPOINT,
                azure_deployment=AZURE_OPENAI_DEPLOYMENT,
                api_version=AZURE_OPENAI_API_VERSION)

#step 2
def analyze_learner_progress(request:LearnerProgressRequest)->LearnerProgressResponse:
    user_prompt=HUMAN_PROMPT.format(
            learner_id=request.learner_id,
            learner_name=request.learner_name,
            training_program=request.training_program,
            topics_completed=request.topics_completed,
            assignments_assigned=request.assignments_assigned,
            assignments_completed=request.assignments_completed,
            attendance_percentage=request.attendance_percentage,
            coding_assesment_score=request.coding_assesment_score,
            trainer_feedback=request.trainer_feedback
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

    ai_data = json.loads(ai_text)

    ai_analysis = LearnerProgressAnalysis(**ai_data)

    
    recommended_practice = [
        f"Practice more on {topic}"
        for topic in ai_data["weak_topics"]
    ]

    recommended_practice.append(
        "Complete pending assignments"
    )

    next_learning_plan = (
        f"Focus on improving {', '.join(ai_data['weak_topics'])} "
        f"and continue advancing in {request.training_program}."
    )

    trainer_recommendation = (
        f"Learner is at {ai_data['learning_level']} level. "
        f"Additional hands-on coding practice and project work "
        f"are recommended."
    )

    ai_summary = (
        f"{request.learner_name} has achieved "
        f"{ai_data['completion_percentage']}% completion with a "
        f"readiness score of {ai_data['readiness_score']}. "
        f"The learner demonstrates strengths in "
        f"{', '.join(ai_data['strong_topics'])} and should focus "
        f"on improving {', '.join(ai_data['weak_topics'])}."
    )
    
    return LearnerProgressResponse(
             learner_id=request.learner_id,
             learner_name=request.learner_name,
             analysis=ai_analysis,
             recommended_practice=recommended_practice,
             next_learning_plan=next_learning_plan,
             trainer_recommendation=trainer_recommendation,
             ai_summary=ai_summary
    )





















