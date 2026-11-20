from model.helpdesk_model import (HelpDeskRequest)
from graph.helpdesk_graph import workflow_graph


def analyze_agent(request: HelpDeskRequest):
    initial_state = {
        "employeeId": request.employeeId,
        "employeeName": request.employeeName,
        "issue": request.issue,

        "category": "",
        "priority": "",

        "resolution": [],
        "toolsCalled": [],


        "reviewStatus": "Not Reviewed",
        "reviewReason": "",

        "ticketId": None,
        "status": "Pending",

        "agentUsed": "",

        "finalResponse": {}
    }

    result = workflow_graph.invoke(initial_state)
    # print(result)
    return result["finalResponse"]
