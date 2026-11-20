from crewai import Task
 
from agent.planner_agent import study_planner
 
 
def create_planner_task(topic, tutor_task):
 
    planner_task = Task(
 
        description=(
 
            f"Create a three-day beginner study plan for {topic}."
 
            "Use the lesson prepared by the Python Tutor."
 
            "Divide the study plan into exactly three days."
 
            "Day 1 should cover the basic concepts."
 
            "Day 2 should cover important operations and concepts."
 
            "Day 3 should focus on practical exercises and revision."
 
            "Include learning activities and practice exercises "
            "for each day."
 
        ),
 
        expected_output=(
 
            "A structured three-day Python study plan containing: "
 
            "1. Day 1 learning activities "
 
            "2. Day 2 learning activities "
 
            "3. Day 3 learning activities "
 
            "4. Practical exercises for each day"
 
        ),
 
        agent=study_planner,
 
        context=[tutor_task]
    )
 
    return planner_task