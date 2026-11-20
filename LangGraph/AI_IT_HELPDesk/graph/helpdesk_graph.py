from langgraph.graph import StateGraph, START, END
from graph.helpdesk_state import HelpDeskState
from agent.analysis_agent import analysis_issue
from agent.resolution_agent import resolve_issue
from agent.review_agent import review_resolution

from tool.it_support_tools import create_support_ticket


# Node 4: Escalation
# def escalate_issue(state):

#     ticket_result = create_support_ticket.invoke({
#         "employeeId": state["employeeId"],
#         "issue": state["issue"],
#         "priority": state["priority"]
#     })

def escalate_issue(state):

    ticket_result = create_support_ticket.invoke({
        "id": state["employeeId"],
        "issue": state["issue"],
        "priority": state["priority"]
    })

    # extract ticket id from the simulated tool response
    # ticket_id = ticket_result.split("Ticket ID: ")[1].split(".")[0]
    ticket_id = ticket_result["ticketId"]

    return {
        "ticketId": ticket_id,
        "status": "Escalated",
        "agentUsed": "Escalation Agent"
    }


# Node 5: Generate Final response
def generate_response(state):

    status = state.get("status")

    if status != "Escalated":
        status = "Resolution Suggested"

    response = {
        "employeeId": state["employeeId"],
        "category": state["category"],
        "priority": state["priority"],
        "agentUsed": state["agentUsed"],
        "toolsCalled": state["toolsCalled"],
        "resolution": state["resolution"],
        "reviewStatus": state["reviewStatus"],
        "ticketId": state["ticketId"],
        "status": status
    }

    return {
        "status": status,
        "finalResponse": response
    }

# Conditional routing after analysis


def route_after_analysis(state):

    if state["priority"] == "Critical":
        return "escalate"
    return "resolve"

# Conditional routing after review


def route_after_review(state):
    if state["reviewStatus"] == "Approved":
        return "generate"
    return "escalate"


# create stateGraph
workflow = StateGraph(HelpDeskState)


# Register Nodes
workflow.add_node("analysis", analysis_issue)
workflow.add_node("resolve", resolve_issue)
workflow.add_node("review", review_resolution)
workflow.add_node("escalate", escalate_issue)
workflow.add_node("generate", generate_response)


# starting Edge

workflow.add_edge(START, "analysis")
# routing after issue analysis
workflow.add_conditional_edges(
    "analysis",
    route_after_analysis,
    {
        "resolve": "resolve",
        "escalate": "escalate"
    }
)
# resolution goes to quality review
workflow.add_edge("resolve", "review")
# routing after quality review
workflow.add_conditional_edges(
    "review",
    route_after_review,
    {
        "generate": "generate",
        "escalate": "escalate"
    }
)

# Escalation goes to final response
workflow.add_edge("escalate", "generate")
# End Workflow
workflow.add_edge("generate", END)

# compile the graph
workflow_graph = workflow.compile()
