from crewai import Crew,Process
from agent.tutor_agent import python_tutor
from agent.assessment_agent import assessment_agent
from task.tutor_task import create_tutor_task
from task.assessment_task import assessment_agent,create_assessment_task


def main():
    print("==========================================")
    print("         MULTI AGENT AI PYTHON TUTOR       ")
    print("                CrewAI")
    print("==========================================")
    
    topic=input(
        "Enter Python topic:"
    ).strip()
    
    if not topic:
        print("Please enter a valid topic.")
        return
    
    #Step 1 Create task
    tutor_task=create_tutor_task(topic)
    
    #step 2 create assessment task
    assessment_task=create_assessment_task(
        topic,
        tutor_task
    )
    #step 3 : Create the crew
    python_crew=Crew(
        agents=[python_tutor,assessment_agent],
        tasks=[tutor_task,assessment_task],
        process=Process.sequential,
        verbose=True
    )
    
    
    #step 4 Execute the crew
    try:
        result=python_crew.kickoff()
        
        print("\n================PYTHON LESSON============\n")
        print(tutor_task.output.raw)
        print("n\==============PYTHON ASSESSMENT===========\n")
        print(assessment_task.output.raw)
        
        print("\n===============FINAL CREW OUTPUT=============\n")
        print(result.raw)
    except Exception as error:
        print(
            "Unable to generate the lesson:",
            type(error).__name__
        )    
if __name__=="__main__":
    main()        