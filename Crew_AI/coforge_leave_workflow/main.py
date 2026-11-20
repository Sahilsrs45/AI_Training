from crewai import Crew, Process
 
 
from agents.leave_verification_agent import leave_verifier
from agents.hrpolicy_agent import hr_policy_agent
from agents.approval_agent import approval_agent
from task.task import create_tasks
 
emp_id = int(input("Enter Employee ID: "))
req_day = int(input("Enter Leave Days: "))
 
if req_day <= 0:
    raise ValueError("leave days must be positive")
 
tasks = create_tasks(emp_id, req_day)
 
crew = Crew(
    agents=[
        leave_verifier,
        hr_policy_agent,
        approval_agent
    ],
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)
 
result = crew.kickoff()
 
print("\nFINAL LEAVE WORKFLOW RESULT")
print(result.raw)
 