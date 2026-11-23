from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import START, END

from data.menu import MENU

from services.llm_service import generate_escalation


class CafeteriaState(TypedDict):

    employee_id: str
    employee_name: str

    items: list

    order_id: str
    invoice_number: str

    subtotal: float
    gst: float
    total_amount: float

    elapsed_minutes: int

    status: str

    priority: str

    escalated_to: str

    message: str


def validate_order_node(state: CafeteriaState):

    for item in state["items"]:

        if item["food_name"] not in MENU:
            raise ValueError(
                f"{item['food_name']} not available in menu"
            )

    return {}


def generate_invoice_node(state: CafeteriaState):

    subtotal = 0

    for item in state["items"]:

        price = MENU[item["food_name"]]

        subtotal += (
            price * item["quantity"]
        )

    gst = subtotal * 0.05

    total_amount = subtotal + gst

    return {

        "subtotal": subtotal,

        "gst": gst,

        "total_amount": total_amount,

        "status": "Order Placed"
    }


def check_delay_node(state: CafeteriaState):

    elapsed = state["elapsed_minutes"]

    if elapsed <= 20:

        priority = "NORMAL"

        recipient = "None"

    elif elapsed <= 30:

        priority = "HIGH"

        recipient = "Cafeteria Supervisor"

    else:

        priority = "CRITICAL"

        recipient = "Cafeteria Manager"

    return {

        "priority": priority,

        "escalated_to": recipient
    }


def delay_condition(state: CafeteriaState):

    if state["priority"] == "NORMAL":

        return "confirm"

    return "escalate"


def confirm_order_node(state: CafeteriaState):

    return {

        "message": "Order is on time."
    }


def escalate_order_node(state: CafeteriaState):

    result = generate_escalation(
        state["order_id"],
        state["employee_id"],
        state["items"],
        state["elapsed_minutes"],
        state["priority"],
        state["escalated_to"]
    )

    return {

        "message": result.escalation_message
    }


workflow = StateGraph(CafeteriaState)

workflow.add_node(
    "validate_order_node",
    validate_order_node
)

workflow.add_node(
    "generate_invoice_node",
    generate_invoice_node
)

workflow.add_node(
    "check_delay_node",
    check_delay_node
)

workflow.add_node(
    "confirm_order_node",
    confirm_order_node
)

workflow.add_node(
    "escalate_order_node",
    escalate_order_node
)

workflow.add_edge(
    START,
    "validate_order_node"
)

workflow.add_edge(
    "validate_order_node",
    "generate_invoice_node"
)

workflow.add_edge(
    "generate_invoice_node",
    "check_delay_node"
)

workflow.add_conditional_edges(
    "check_delay_node",
    delay_condition,
    {
        "confirm": "confirm_order_node",
        "escalate": "escalate_order_node"
    }
)

workflow.add_edge(
    "confirm_order_node",
    END
)

workflow.add_edge(
    "escalate_order_node",
    END
)

workflow_graph = workflow.compile()