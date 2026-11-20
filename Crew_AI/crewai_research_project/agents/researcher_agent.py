from crewai import Agent
from config.settings import llm

researcher = Agent(
    role="Senior Researcher",
    goal="Find accurate and latest information about the given topic",
    backstory=("You are an expert researcher who gathers"
    "detailed and fact-based information from reliable sources."
    ),
    # tools=[],
    llm=llm,
    verbose=True,
    allow_delegation=False
    
)