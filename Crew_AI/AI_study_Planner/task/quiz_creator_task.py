from crewai import Task
 
from agent.quiz_creator_agent import quiz_creator
 
 
def create_quiz_task(topic, planner_task):
 
    quiz_task = Task(
 
        description=(
 
            f"Create exactly five easy beginner-level "
            f"practice questions about {topic}."
 
            "Use the three-day study plan prepared by "
            "the Study Planner."
 
            "Create questions based on the concepts covered "
            "in the study plan."
 
            "All five questions must be beginner-friendly."
 
            "Number the questions from 1 to 5."
 
            "Do not provide answers, solutions or hints."
 
        ),
 
        expected_output=(
 
            "Exactly five numbered beginner-level Python "
            "practice questions without answers or solutions."
 
        ),
 
        agent=quiz_creator,
 
        context=[planner_task]
    )
 
    return quiz_task