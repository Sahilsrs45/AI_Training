from langchain_core.messages import AIMessage
from Agents.ai_agent import create_salary_agent

from models.ai_model import SalaryRequest,SalaryResponse

agent=create_salary_agent()


def calculate_employee_salary(request:SalaryRequest)->SalaryResponse:
    question=f"""
    EMployee ID:{request.employee_id}
    Employee Name:{request.employee_name}
    Question: {request.question}
    
    """
    
    result=agent.invoke({
        "messages":[
            { "role":"user","content":question}
        ]
    })
    
    tools_used=[]
    #tells which tool to use
    for message in result["messages"]:
        if isinstance(message,AIMessage):
            for tool_call in message.tool_calls:
                tools_used.append(tool_call["name"])
                print("Tool Called:",tool_call["name"])
                print("Arguments:",tool_call["args"])
                
    answer =result["messages"][-1].content
    
    return SalaryResponse(
        employee_id=request.employee_id,
        employee_name=request.employee_name,
        answer=str(answer),
        tools_used=tools_used
    )            