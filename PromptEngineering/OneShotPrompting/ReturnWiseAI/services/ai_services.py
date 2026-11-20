import json
 
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)
 
from models.analysis_model import RetrunAnalysis
from models.request_model import ReturnRequest
from models.response_model import ReturnResponse
 
from prompts.one_shot_prompt import (
    HUMAN_PROMPT,
    SYSTEM_PROMPT
)
 
from openai import AzureOpenAI
 
 
# step 1: create llm
 
llm = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)
 
 
def analyze_return(request: ReturnRequest) -> ReturnResponse:
 
    user_prompt = HUMAN_PROMPT.format(
        request_id=request.request_id,
        order_id=request.order_id,
        product_category=request.product_category,
        days_since_delivery=request.days_since_delivery,
        item_price_inr=request.item_price_inr,
        reason=request.reason,
        evidence_provided=request.evidence_provided,
        customer_description=request.customer_description
    )
 
    # step 2: call llm
 
    response = llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        response_format={"type": "json_object"}
    )
 
    # extract ai response
 
    ai_text = response.choices[0].message.content
 
    if not ai_text:
        raise ValueError("LLM returned empty response")
 
    
 
    ai_analysis = RetrunAnalysis(**json.loads(ai_text))
 
    # recommended actions
 
    recommended_actions = [
        f"Perform the following action: {step}"
        for step in ai_analysis.missing_information
    ]
 
    recommended_actions.append(
        "Forward the return request to a human support agent for review."
    )
 
    # human review logic
 
    human_review_required = True
 
    # customer message draft
 
    customer_message_draft = (
        f"Dear Customer, we have received your return request "
        f"{request.request_id}. "
        f"Our support team will review the provided information "
        f"and update you regarding the next steps. "
        f"No return or refund decision has been made yet."
    )
 
    return ReturnResponse(
        request_id=request.request_id,
        analysis=ai_analysis,
        recommended_next_steps=recommended_actions,
        human_review_required=human_review_required,
        customer_message_draft=customer_message_draft
    )