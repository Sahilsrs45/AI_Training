from crewai import Task
 
from agent.idea_agent import idea_generator
 
 
def create_idea_task(event_name, event_date, audience):
 
    idea_task = Task(
 
        description=(
 
            f"Suggest one simple event theme for "
            f"the event: {event_name}."
 
            f"The event date is {event_date}."
 
            f"The target audience is {audience}."
 
            "Suggest one creative and engaging theme "
            "suitable for the target audience."
 
            "Explain the theme briefly."
 
            "Do not suggest multiple themes."
 
        ),
 
        expected_output=(
 
            "One suitable event theme with "
            "a short explanation."
 
        ),
 
        agent=idea_generator
    )
 
    return idea_task