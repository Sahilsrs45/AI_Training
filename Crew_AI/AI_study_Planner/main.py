from crewai import Crew, Process
 
# Import agents
from agent.tutor_agent import python_tutor
 
from agent.planner_agent import study_planner
 
from agent.quiz_creator_agent import quiz_creator
 
 
# Import task functions
from task.tutor_task import create_tutor_task
 
from task.planner_task import create_planner_task
 
from task.quiz_creator_task import create_quiz_task
 
 
def main():
 
    print("==========================================")
 
    print("             AI STUDY PLANNER             ")
 
    print("                  CrewAI                  ")
 
    print("==========================================")
 
    # Accept Python topic
    topic = input(
        "Enter Python topic: "
    ).strip()
 
    if not topic:
 
        print("Please enter a valid topic.")
 
        return
 
    # Step 1: Create tutor task
    tutor_task = create_tutor_task(topic)
 
    # Step 2: Create study planner task
    planner_task = create_planner_task(
        topic,
        tutor_task
    )
 
    # Step 3: Create quiz task
    quiz_task = create_quiz_task(
        topic,
        planner_task
    )
 
    # Step 4: Create the crew
    study_crew = Crew(
 
        agents=[
            python_tutor,
            study_planner,
            quiz_creator
        ],
 
        tasks=[
            tutor_task,
            planner_task,
            quiz_task
        ],
 
        process=Process.sequential,
 
        verbose=True
    )
 
    # Step 5: Execute the crew
    try:
 
        result = study_crew.kickoff()
 
        print("\n=============== PYTHON EXPLANATION ===============\n")
 
        print(tutor_task.output.raw)
 
        print("\n=============== THREE-DAY STUDY PLAN ===============\n")
 
        print(planner_task.output.raw)
 
        print("\n=============== PYTHON QUIZ ===============\n")
 
        print(quiz_task.output.raw)
 
        print("\n=============== FINAL CREW OUTPUT ===============\n")
 
        print(result.raw)
 
    except Exception as error:
 
        print(
            "Unable to generate the study plan:",
            type(error).__name__,
            str(error)
        )
 
 
if __name__ == "__main__":
 
    main()