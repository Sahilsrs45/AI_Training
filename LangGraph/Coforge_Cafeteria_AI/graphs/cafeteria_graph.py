from typing import TypedDict
from langgraph.graph import (
    StateGraph,
    START,
    END
)

class CafeteriaState(TypedDict):

    order_id:str
    employee_id:str

    elapsed_minutes:int

    priority:str
    recipient:str

    escalation_message:str


def check_delay(state):

    elapsed = state[
        "elapsed_minutes"
    ]

    if elapsed <= 20:
        return "confirm"

    return "escalate"


def confirm_order_node(state):

    return {

        "priority":"NORMAL",

        "recipient":"None",

        "escalation_message":
        "Order within expected delivery time"
    }


def escalate_order_node(state):

    elapsed = state[
        "elapsed_minutes"
    ]

    if elapsed <= 30:

        return {

            "priority":"HIGH",

            "recipient":
            "Cafeteria Supervisor"
        }

    return {

        "priority":"CRITICAL",

        "recipient":
        "Cafeteria Manager"
    }


workflow = StateGraph(
    CafeteriaState
)

workflow.add_node(
    "confirm",
    confirm_order_node
)

workflow.add_node(
    "escalate",
    escalate_order_node
)

workflow.add_conditional_edges(
    START,
    check_delay,
    {
        "confirm":"confirm",
        "escalate":"escalate"
    }
)

workflow.add_edge(
    "confirm",
    END
)

workflow.add_edge(
    "escalate",
    END
)

workflow_graph = workflow.compile()