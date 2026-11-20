from crewai import Agent
 
from config.setting import llm
 
 
activity_planner = Agent(
 
    role="College Event Activity Planner",
 
    goal=(
        "Create exactly four suitable and engaging "
        "activities based on the event theme."
    ),
 
    backstory=(
        "You are an experienced event activity planner. "
        "You specialize in designing fun, interactive "
        "and educational activities for college students. "
        "You create activities that encourage teamwork "
        "and student participation."
    ),
 
    llm=llm,
 
    verbose=True,
 
    allow_delegation=False
)