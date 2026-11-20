from fastapi import FastAPI

from models.order_model import (
    OrderRequest
)

from services.order_service import (
    MENU,
    orders,
    validate_order,
    create_order
)

from services.invoice_service import (
    generate_invoice
)

from graphs.cafeteria_graph import (
    workflow_graph
)

app = FastAPI(
    title="Coforge Smart Cafeteria AI"
)


@app.get("/health")
def health():

    return {
        "status":"UP"
    }


@app.get("/menu")
def get_menu():

    return MENU


@app.post("/order")
def place_order(
    request:OrderRequest
):

    validate_order(
        request.model_dump()
    )

    order = create_order(
        request.model_dump()
    )

    invoice = generate_invoice(
        order
    )

    return {

        **order,
        **invoice
    }


@app.get("/order/{order_id}")
def get_order(order_id:str):

    return orders.get(
        order_id
    )


@app.post(
"/order/{order_id}/check-delay"
)
def check_delay(
    order_id:str,
    elapsed_minutes:int
):

    if order_id not in orders:

        return {
            "message":
            "Order not found"
        }

    order = orders[order_id]

    result = workflow_graph.invoke(
        {
            "order_id":order_id,
            "employee_id":
            order["employee_id"],
            "elapsed_minutes":
            elapsed_minutes
        }
    )

    return result