from crewai import Crew, Process
 
 
# Import agents
from agent.idea_agent import idea_generator
 
from agent.activity_agent import activity_planner
 
from agent.invitation_agent import invitation_writer
 
from agent.quality_agent import quality_checker
 
 
# Import task functions
from task.idea_task import create_idea_task
 
from task.activity_task import create_activity_task
 
from task.invitation_task import create_invitation_task
 
from task.quality_task import create_quality_task
 
 
def main():
 
    print("==========================================")
 
    print("              AI EVENT PLANNER            ")
 
    print("                  CrewAI                  ")
 
    print("==========================================")
 
    # Accept event details from user
 
    event_name = input(
        "Enter event name: "
    ).strip()
 
    event_date = input(
        "Enter event date: "
    ).strip()
 
    audience = input(
        "Enter target audience: "
    ).strip()
 
 
    # Validate input
 
    if not event_name or not event_date or not audience:
 
        print("Please enter all required event details.")
 
        return
 
 
    # Step 1: Create Idea Task
 
    idea_task = create_idea_task(
        event_name,
        event_date,
        audience
    )
 
 
    # Step 2: Create Activity Task
 
    activity_task = create_activity_task(
        event_name,
        audience,
        idea_task
    )
 
 
    # Step 3: Create Invitation Task
 
    invitation_task = create_invitation_task(
        event_name,
        event_date,
        audience,
        idea_task,
        activity_task
    )
 
 
    # Step 4: Create Quality Task
 
    quality_task = create_quality_task(
        event_name,
        event_date,
        audience,
        idea_task,
        activity_task,
        invitation_task
    )
 
 
    # Step 5: Create the Crew
 
    event_crew = Crew(
 
        agents=[
            idea_generator,
            activity_planner,
            invitation_writer,
            quality_checker
        ],
 
        tasks=[
            idea_task,
            activity_task,
            invitation_task,
            quality_task
        ],
 
        process=Process.sequential,
 
        verbose=True
    )
 
 
    # Step 6: Execute the Crew
 
    try:
 
        result = event_crew.kickoff()
 
 
        print("\n================ EVENT IDEA ================\n")
 
        print(idea_task.output.raw)
 
 
        print("\n================ EVENT ACTIVITIES ================\n")
 
        print(activity_task.output.raw)
 
 
        print("\n================ EVENT INVITATION ================\n")
 
        print(invitation_task.output.raw)
 
 
        print("\n================ QUALITY CHECKLIST ================\n")
 
        print(quality_task.output.raw)
 
 
        print("\n================ FINAL CREW OUTPUT ================\n")
 
        print(result.raw)
 
 
    except Exception as error:
 
        print(
 
            "Unable to generate the event plan:",
 
            type(error).__name__,
 
            str(error)
 
        )
 
 
if __name__ == "__main__":
 
    main()