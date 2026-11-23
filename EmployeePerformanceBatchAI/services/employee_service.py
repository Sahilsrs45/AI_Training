import json

from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)

llm = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    deployment_name=AZURE_OPENAI_DEPLOYMENT,
    temperature=0
)

prompt = PromptTemplate(
    input_variables=[
        "employee_name",
        "department",
        "designation",
        "experience",
        "technical_skills",
        "performance_rating",
        "attendance_percentage",
        "projects_completed",
        "manager_feedback"
    ],
    template="""
You are an HR Performance Evaluator.

Employee Name: {employee_name}
Department: {department}
Designation: {designation}
Experience: {experience}
Technical Skills: {technical_skills}
Performance Rating: {performance_rating}
Attendance Percentage: {attendance_percentage}
Projects Completed: {projects_completed}
Manager Feedback: {manager_feedback}

Evaluate the employee.

Return ONLY valid JSON:

{{
    "performance_level":"",
    "strengths":[],
    "improvement_areas":[],
    "training_recommendations":[],
    "promotion_readiness":"",
    "ai_feedback":"",
    "recommended_action":""
}}
"""
)

chain = prompt | llm


def evaluate_employees(employee_list):

    batch_inputs = [
        {
            "employee_name": emp.employee_name,
            "department": emp.department,
            "designation": emp.designation,
            "experience": emp.experience,
            "technical_skills": ", ".join(emp.technical_skills),
            "performance_rating": emp.performance_rating,
            "attendance_percentage": emp.attendance_percentage,
            "projects_completed": emp.projects_completed,
            "manager_feedback": emp.manager_feedback
        }
        for emp in employee_list
    ]

    responses = chain.batch(batch_inputs)

    results = []

    for emp, response in zip(employee_list, responses):

        try:
            evaluation = json.loads(response.content)

        except Exception:
            evaluation = {
                "performance_level": "Not Available",
                "strengths": [],
                "improvement_areas": [],
                "training_recommendations": [],
                "promotion_readiness": "Unknown",
                "ai_feedback": response.content,
                "recommended_action": "Review manually"
            }

        results.append(
            {
                "employee_id": emp.employee_id,
                "employee_name": emp.employee_name,
                **evaluation
            }
        )

    return {
        "total_employees": len(employee_list),
        "results": results
    }