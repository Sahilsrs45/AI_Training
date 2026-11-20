from crewai import Agent
 
from config.setting import llm
 
 
idea_generator = Agent(
 
    role="College Event Idea Generator",
 
    goal=(
        "Suggest one creative and simple event theme "
        "based on the event name, date and target audience."
    ),
 
    backstory=(
        "You are an experienced college event organizer. "
        "You specialize in generating creative, engaging "
        "and budget-friendly event ideas for students. "
        "You understand student interests and preferences."
    ),
 
    llm=llm,
 
    verbose=True,
 
    allow_delegation=False
)