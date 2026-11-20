from crewai import Agent
from config.settings import llm
from tools.sql_tools import execute_employee_sql

sql_executor=Agent(
    role="SQL Executor",
    goal="Execute approved SQL and explain the results",
    backstory=(
        "You are an employee analytics specialist"
        "who creates readable business reports."
    ),
    tools=[execute_employee_sql],
    llm=llm,
    verbose=True,
    allow_delegation=False
)