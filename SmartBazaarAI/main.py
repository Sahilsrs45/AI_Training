from fastapi import FastAPI

from models.billing_models import (
    BillingRequest
)

from services.billing_calculator import (
    calculate_invoice
)

from services.ai_billing_service import (
    generate_bill_explanation
)

app = FastAPI(
    title="Smart Bazaar AI"
)


@app.get(
    "/api/bazaar/health"
)
def health():

    return {
        "status": "healthy"
    }


@app.get(
    "/api/bazaar/rules"
)
def rules():

    return {
        "grocery_discount": "5%",
        "household_discount": "10%",
        "personal_care_discount": "8%",
        "coupon": "SMART100",
        "loyalty_limit": 200
    }


@app.post(
    "/api/bazaar/calculate"
)
def calculate(
        request:
        BillingRequest
):

    return calculate_invoice(
        request
    )


@app.post(
    "/api/bazaar/explain"
)
def explain(
        request:
        BillingRequest
):

    invoice = calculate_invoice(
        request
    )

    explanation = (
        generate_bill_explanation(
            request.customer_name,
            request.membership_tier,
            invoice
        )
    )

    return {
        "invoice": invoice,
        "explanation":
            explanation
    }