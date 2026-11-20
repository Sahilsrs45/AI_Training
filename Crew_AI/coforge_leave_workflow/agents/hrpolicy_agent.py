from crewai import Agent
from config.settings import llm

hr_policy_agent=Agent(
    role="HR Policy Analyst",
    goal=(
        "Evaluate employee leave requests"
        "according to comapany HR policies"
    ),
    backstory=(
        "You are an HR policy specialist."
        "You check employee leave eligibility"
        "using verified employee information"
        "and company leave policies."
        "You never invent leave balances."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)