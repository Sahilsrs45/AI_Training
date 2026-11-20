import json
import uuid
from datetime import datetime

orders = {}
with open(
    "config/menu.json",
    "r"
) as file:
    MENU = json.load(file)


def validate_order(data):

    for item in data["items"]:

        if item["food_name"] not in MENU:

            raise ValueError(
                f"{item['food_name']} not available"
            )

    return data


def create_order(data):

    order_id = (
        "ORD" +
        str(
            len(orders)+1001
        )
    )

    invoice_number = (
        "INV" +
        str(
            len(orders)+1001
        )
    )

    orders[order_id] = {
        **data,
        "order_id": order_id,
        "invoice_number":invoice_number,
        "status":"Order Placed",
        "created_at":datetime.now()
    }

    return orders[order_id]