from crewai import Agent
from config.settings import llm

writer = Agent(
    role="Content Writer",
    goal="Write a professional article based on research findings",
    backstory=("You are a skilled content writer who transforms"
    "research into engaging and informative articles."),
    # tools=[],
    llm=llm,
    verbose=True,
    allow_delegation=False
)