from crewai import Agent
from config.settings import llm


editor = Agent(
    role="Editor",
    goal="Review and improve the article",
    backstory=("You are a senior editor responsible for"
   " grammar, clarity, structure, and readability."),
    #tools=[],
    llm=llm,
    verbose=True,
    allow_delegation=False
    
)