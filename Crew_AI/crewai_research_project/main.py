from crewai import Crew,Process
from agents.researcher_agent import researcher
from agents.writer_agent import writer
from agents.editor_agent import editor

from tasks.tasks import create_tasks

questions=input("Provide the topic that you want to research:")
tasks=create_tasks(questions)

crew=Crew(
    agents=[editor,writer,researcher],
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)

result=crew.kickoff()
print("\n Final Agent Response")
print(result.raw)