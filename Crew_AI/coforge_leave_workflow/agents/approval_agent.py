from crewai import Agent
from config.settings import llm

approval_agent=Agent(
    role="Leave Approval Recommendation Specialist",
    goal=(
        "Generate an accurate leave approval "
        "or rejection recommendation"
    ),
    backstory=(
        "You are an HR approval recommendation"
        "specialist.You review employee"
        "Verifiacction results and HR policy"
        "analysis before generating a final"
        "recommendation with a clear reason."
        "You never modify employee records"
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)