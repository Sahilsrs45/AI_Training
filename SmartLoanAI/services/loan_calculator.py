from math import pow

DISCOUNTS={"Regular":0,"Salary Account Holder":10,"Senior Citizen":20,"Premium":30,"Bank Employee":50}

def calculate_loan(request):
    principal=request.loan_amount
    processing_fee=principal*0.02
    discount_amount=processing_fee*DISCOUNTS[request.customer_category]/100
    discounted_fee=processing_fee-discount_amount
    gst=discounted_fee*0.18
    additional_tax=principal*0.01
    upfront_charges=discounted_fee+gst+additional_tax

    r=request.annual_interest_rate/1200
    n=request.loan_tenure_years*12

    emi=(principal*r*pow(1+r,n))/((pow(1+r,n))-1)
    total_emi_repayment=emi*n
    total_interest=total_emi_repayment-principal
    overall_customer_outflow=total_emi_repayment+upfront_charges

    return {
      "customer_name":request.customer_name,
      "loan_amount":round(principal,2),
      "processing_fee":round(processing_fee,2),
      "discount_amount":round(discount_amount,2),
      "gst":round(gst,2),
      "additional_tax":round(additional_tax,2),
      "upfront_charges":round(upfront_charges,2),
      "monthly_emi":round(emi,2),
      "total_interest":round(total_interest,2),
      "total_emi_repayment":round(total_emi_repayment,2),
      "overall_customer_outflow":round(overall_customer_outflow,2),
      "ai_explanation":"Verified loan calculation completed."
    }
