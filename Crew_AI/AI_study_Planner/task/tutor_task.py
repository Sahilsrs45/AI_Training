from crewai import Task
 
from agent.tutor_agent import python_tutor
 
 
def create_tutor_task(topic):
 
    tutor_task = Task(
 
        description=(
 
            f"Teach the Python topic: {topic}."
 
            "The learner is a complete fresher."
 
            "Explain the concept in simple English."
 
            "Explain the meaning and purpose of the topic."
 
            "Provide exactly one small practical Python example."
 
            "Explain the example clearly."
 
        ),
 
        expected_output=(
 
            "A structured Python lesson containing: "
 
            "1. Topic introduction "
 
            "2. Meaning and purpose "
 
            "3. Important concepts "
 
            "4. One small Python example "
 
            "5. Explanation of the example"
 
        ),
 
        agent=python_tutor
    )
 
    return tutor_task