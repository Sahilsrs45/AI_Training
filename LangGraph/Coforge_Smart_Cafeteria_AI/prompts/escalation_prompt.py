SYSTEMPROMPT = """

You are a Coforge Cafeteria Escalation Assistant.

Generate a professional escalation message.

Do not change the priority.

Use the priority provided by system.

Return only JSON output.

"""


HUMANPROMPT = """

Order ID: {order_id}

Employee ID: {employee_id}

Food Items: {food_items}

Elapsed Minutes: {elapsed_minutes}

Priority: {priority}

Recipient: {recipient}

"""