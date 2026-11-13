from openai import OpenAI
from prompts.ai_prompt import (SYSTEM_PROMPT, HUMAN_PROMPT)
from models.ai_model import (
    RequestAIforText,
    ResponseAIforText
)
from config.setting import (
    AZURE_OPENAI_API_KEY,
   # AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)
 
# Step 1. Create LLM client outside the function
# Create LLM client outside the function
llm = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)
 
# Step 2. Define the service function
 
 
def generate_ai_response(requests: RequestAIforText) -> RequestAIforText:
 
    # Prepare the human prompt
    user_prompt = HUMAN_PROMPT.format(requestfromAI=requests.requestfromAI)
 
    # Step 3. Invoke the LLM
    response = llm.responses.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_prompt
    )
 
    # Step 4. Extract the generated response
    ai_text = response.output_text
 
    # Step 5. Return the pydantic response
    return ResponseAIforText(
        responsefromAI=ai_text
    )