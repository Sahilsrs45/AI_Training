from langchain.agents import create_agent
from config.settings import llm
from tool.it_support_tools import it_tools

resolution_agent = create_agent(
    model=llm,
    tools=it_tools,
    system_prompt="""
    You are an IT Helpdesk Resolution Agent.

    Your responsibility is to analyze the issue 
    and select the most appropriate and IT support tool.

    Rules:
    1. Use tools whenever a relevant tool is available
    2. Do not call unrelated tools.
    3. Do not create tickets directly.
        Ticket Creation is handled by the escalation node. 
    4. Never request or reveal passwords.
    5. Do not claim an issue is fixed unless verified.
    6. Provide clear troubleshooting steps.
    7. If no solution is available, explain that escalation 
        may be required. 
    """
)


def resolve_issue(state):

    user_message = f"""
    Employee ID: {state["employeeId"]}
    Category: {state["category"]}
    Priority: {state["priority"]}
    Issue: {state["issue"]}

    Select an appropriate tool and suggest a solution.
    """

    result = resolution_agent.invoke({
        "messages": [
            {"role": "user", "content": user_message}
        ]
    })

    tools_called = []

    for message in result["messages"]:
        if hasattr(message, "tool_calls"):
            for tool_call in message.tool_calls:
                tools_called.append(tool_call["name"])

    final_message = result["messages"][-1]

    content = final_message.content

    if isinstance(content, str):
        resolution_text = content
    else:
        resolution_text = str(content)

    return {
        "resolution": [resolution_text],
        "toolsCalled": tools_called,
        "agentUsed": "Resolution Agent"
    }
