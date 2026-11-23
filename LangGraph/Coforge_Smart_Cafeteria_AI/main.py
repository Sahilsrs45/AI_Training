from fastapi import FastAPI

from data.menu import MENU

from workflow.cafeteria_workflow import workflow_graph

from models.cafeteria_model import (
    OrderRequest,
    OrderResponse,
    DelayResponse
)

app = FastAPI(
    title="Coforge Smart Cafeteria AI"
)

ORDERS = {}

order_counter = 1001
invoice_counter = 1001


@app.get("/")
def home():

    return {
        "message": "Coforge Smart Cafeteria AI"
    }


@app.get("/menu")
def get_menu():

    return MENU


@app.post("/order", response_model=OrderResponse)
def place_order(data: OrderRequest):

    global order_counter
    global invoice_counter

    order_id = f"ORD{order_counter}"

    invoice_number = f"INV{invoice_counter}"

    order_counter += 1
    invoice_counter += 1

    result = workflow_graph.invoke({

        "employee_id": data.employee_id,

        "employee_name": data.employee_name,

        "items": [item.model_dump() for item in data.items],

        "order_id": order_id,

        "invoice_number": invoice_number,

        "elapsed_minutes": 0
    })

    ORDERS[order_id] = {

        "employee_id": data.employee_id,

        "employee_name": data.employee_name,

        "items": [item.model_dump() for item in data.items],

        "order_id": order_id,

        "invoice_number": invoice_number
    }

    return OrderResponse(

        order_id=order_id,

        invoice_number=invoice_number,

        employee_id=data.employee_id,

        employee_name=data.employee_name,

        subtotal=result["subtotal"],

        gst=result["gst"],

        total_amount=result["total_amount"],

        status=result["status"]
    )


@app.get("/order/{order_id}")
def get_order(order_id: str):

    return ORDERS.get(order_id)


@app.post("/order/{order_id}/check-delay")
def check_delay(
    order_id: str,
    elapsed_minutes: int
):

    order = ORDERS[order_id]

    result = workflow_graph.invoke({

        "employee_id": order["employee_id"],

        "employee_name": order["employee_name"],

        "items": order["items"],

        "order_id": order["order_id"],

        "invoice_number": order["invoice_number"],

        "elapsed_minutes": elapsed_minutes
    })

    delay_minutes = max(
        0,
        elapsed_minutes - 20
    )

    return DelayResponse(

        order_id=order_id,

        employee_id=order["employee_id"],

        elapsed_minutes=elapsed_minutes,

        expected_minutes=20,

        delay_minutes=delay_minutes,

        priority=result["priority"],

        escalated_to=result["escalated_to"],

        message=result["message"]
    )


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }