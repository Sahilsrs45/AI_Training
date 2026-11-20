from crewai import Task
from agent.assessment_agent import assessment_agent

def create_assessment_task(topic,tutor_task):
    assessment_task=Task(
        
        description=(
            f"Create an assessment for the topic:{topic}."
            "Use the lesson prepared by the Python Tutor."
            "Create five Python coding questions."
            "Include two easy questions."
            "two intermediate questions,"
            "and one challenging question"
            "Provide problem statements and"
            "expected results."
            "Do not provide  complete solutions."
        ),
        expected_output=(
            "Five Python coding assignments"
            "with difficulty levels,problem statements,"
            "and expected results."
        ),
        agent=assessment_agent,
        context=[tutor_task]
        
    )
    return assessment_task