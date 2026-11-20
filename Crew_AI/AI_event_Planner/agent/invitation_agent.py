from crewai import Agent
 
from config.setting import llm
 
 
invitation_writer = Agent(
 
    role="College Event Invitation Writer",
 
    goal=(
        "Write a short, friendly and attractive invitation "
        "using the event details, theme and planned activities."
    ),
 
    backstory=(
        "You are a professional invitation writer. "
        "You specialize in creating friendly and engaging "
        "event invitations for college students. "
        "Your writing is simple, attractive and informative."
    ),
 
    llm=llm,
 
    verbose=True,
 
    allow_delegation=False
)