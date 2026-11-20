from langchain_core.messages import AIMessage
 
from agent.agent import create_hospital_agent
 
from models.request_model import HospitalRequest
from models.response_model import HospitalResponse

 
agent = create_hospital_agent()
 
 
def manage_hospital_request(
    request: HospitalRequest
) -> HospitalResponse:
 
    question = f"""
    User Role: {request.user_role}
 
    Question: {request.message}
    """
 
    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })
 
    tools_used = []
 
    # Identify which tools were called
 
    for message in result["messages"]:
 
        if isinstance(message, AIMessage):
 
            for tool_call in message.tool_calls:
 
                tools_used.append(tool_call["name"])
 
                print("Tool Called:", tool_call["name"])
                print("Arguments:", tool_call["args"])
 
 
    answer = result["messages"][-1].content
 
    return HospitalResponse(
        status="success",
        response=str(answer),
        tools_used=tools_used,
        data=None
    )