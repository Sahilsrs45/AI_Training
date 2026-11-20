from crewai import Agent
from config.settings import llm
from tool.tools import check_leave_balance

leave_verifier=Agent(
    role="Leave Verification Specialist",
    goal=(
        "Verify employees information and"
        "available leave balance"
    ),
    backstory=(
        "You are an employee leave verification."
        "Specialist working in the HR department"
        "You verify employee information using"
        "the employee leave balance tool."
    
    ),
    tools=[check_leave_balance],
    llm=llm,
    verbose=True,
    allow_delegation=False
)