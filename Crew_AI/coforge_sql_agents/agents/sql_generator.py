from crewai import Agent
from config.settings import llm
from tools.sql_tools import execute_employee_sql

sql_generator=Agent(
    role="SQL Generator",
    goal="Convert natural language into MYSQL SELECT queries",
    backstory=(
        "You are a SQL developer who creates "
        "simple employees analytics queries."
    ),
    tools=[execute_employee_sql],
    llm=llm,
    verbose=True,
    allowed_delegation=False
)