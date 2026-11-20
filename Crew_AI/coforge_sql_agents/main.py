from crewai import Crew,Process
from agents.sql_executor_agent import sql_executor
from agents.sql_generator import sql_generator
from agents.sql_validator import sql_validator

from tasks.tasks import create_tasks

questions=input("Ask your SQL questions:")
tasks=create_tasks(questions)

crew=Crew(
    agents=[sql_validator,sql_generator,sql_executor],
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)

result=crew.kickoff()
print("\n Final Agent Response")
print(result.raw)