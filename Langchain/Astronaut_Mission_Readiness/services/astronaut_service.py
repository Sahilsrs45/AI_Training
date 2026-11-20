from langchain_openai import AzureChatOpenAI

from models.astronaut_model import (
    AstronautRequest,
    AstronautAnalysis,
    AstronautResponse
)

from prompts.astronaut_prompt import astronaut_prompt

from config.settings import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)


llm = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    temperature=0
)


def analyze_astronaut(
    astronaut: AstronautRequest
) -> AstronautResponse:

    age_eligible = 21 <= astronaut.age <= 60

    training_eligible = (
        astronaut.training_hours >= 1000
    )

    medical_eligible = (
        astronaut.medical_clearance
    )

    experience_eligible = (
        astronaut.previous_missions >= 1
    )

    failed_checks = []

    if not age_eligible:
        failed_checks.append("Age Criteria Failed")

    if not training_eligible:
        failed_checks.append("Training Criteria Failed")

    if not medical_eligible:
        failed_checks.append("Medical Clearance Failed")

    if not experience_eligible:
        failed_checks.append("Experience Criteria Failed")

    if len(failed_checks) == 0:

        readiness_status = "READY"
        risk_level = "LOW"

    else:

        readiness_status = "NOT_READY"

        if len(failed_checks) == 1:
            risk_level = "MEDIUM"
        else:
            risk_level = "HIGH"

    analysis = AstronautAnalysis(
        age_eligible=age_eligible,
        training_eligible=training_eligible,
        medical_eligible=medical_eligible,
        experience_eligible=experience_eligible,
        failed_checks=failed_checks,
        risk_level=risk_level
    )

    chain = astronaut_prompt | llm

    result = chain.invoke({

        "astronaut_id": astronaut.astronaut_id,
        "astronaut_name": astronaut.astronaut_name,
        "age": astronaut.age,
        "training_hours": astronaut.training_hours,
        "medical_clearance": astronaut.medical_clearance,
        "previous_missions": astronaut.previous_missions,
        "mission_type": astronaut.mission_type,

        "age_eligible": analysis.age_eligible,
        "training_eligible": analysis.training_eligible,
        "medical_eligible": analysis.medical_eligible,
        "experience_eligible": analysis.experience_eligible,

        "failed_checks": analysis.failed_checks,
        "risk_level": analysis.risk_level,
        "readiness_status": readiness_status
    })

    ai_response = result.content

    try:

        reason = ai_response.split(
            "Recommendation:"
        )[0].replace(
            "Reason:",
            ""
        ).strip()

        recommendation = ai_response.split(
            "Recommendation:"
        )[1].strip()

    except:

        reason = ai_response
        recommendation = (
            "Continue training and medical preparation."
        )

    return AstronautResponse(

        astronaut_id=astronaut.astronaut_id,

        astronaut_name=astronaut.astronaut_name,

        mission_type=astronaut.mission_type,

        readiness_status=readiness_status,

        risk_level=risk_level,

        reason=reason,

        recommendation=recommendation
    )