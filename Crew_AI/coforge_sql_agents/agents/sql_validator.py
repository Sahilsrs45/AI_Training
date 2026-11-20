from crewai import Agent
from config.settings import llm
from tools.sql_tools import execute_employee_sql


sql_validator=Agent(
    role="SQL Validator",
    goal="Review generated SQL for correctness and safety",
    backstory=(
        "You are a database reviewer."
        "You only approve safe SELECT queries."
    ),
    tools=[execute_employee_sql],
    llm=llm,
    verbose=True,
    allow_delegation=False
) 