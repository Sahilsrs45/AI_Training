import json

with open(
    "config/menu.json","r"
) as file:
    MENU=json.load(file)


def generate_invoice(order):

    subtotal = 0

    for item in order["items"]:

        subtotal += (
            MENU[item["food_name"]]
            *
            item["quantity"]
        )

    gst = subtotal * 0.05

    total = subtotal + gst

    return {

        "subtotal": round(subtotal,2),

        "gst": round(gst,2),

        "total_amount": round(total,2)
    }
    