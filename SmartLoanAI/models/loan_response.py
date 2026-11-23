from pydantic import BaseModel

class LoanResponse(BaseModel):
    customer_name:str
    loan_amount:float
    processing_fee:float
    discount_amount:float
    gst:float
    additional_tax:float
    upfront_charges:float
    monthly_emi:float
    total_interest:float
    total_emi_repayment:float
    overall_customer_outflow:float
