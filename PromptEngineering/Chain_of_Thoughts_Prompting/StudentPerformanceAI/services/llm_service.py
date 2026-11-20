import json

from config.setting import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_VERSION
)

from prompts.student_prompt import (
    SYSTEM_PROMPT,
    HUMAN_PROMPT
)

from models.student_model import (
    StudentPerformanceRequest,
    StudentPerformanceResponse,
    StudentPerformanceAnalysis
)

from openai import AzureOpenAI


llm = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)


def analyse_student_performance(
    request: StudentPerformanceRequest
) -> StudentPerformanceResponse:

    user_prompt = HUMAN_PROMPT.format(
        student_id=request.student_id,
        student_name=request.student_name,
        python_marks=request.python_marks,
        sql_marks=request.sql_marks,
        fastapi_marks=request.fastapi_marks
    )

    response = llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
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

    ai_text = response.choices[0].message.content

    if not ai_text:
        raise ValueError("LLM returned empty response")

    ai_analysis = StudentPerformanceAnalysis(
        **json.loads(ai_text)
    )

    return StudentPerformanceResponse(
        student_id=request.student_id,
        student_name=request.student_name,
        analysis=ai_analysis
    )