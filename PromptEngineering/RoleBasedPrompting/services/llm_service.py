from config.settings import (AZURE_OPENAI_API_DEPLOYMENT,AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_ENDPOINT)
from models.model_role_based import (PythonAIRequest,PythonAIResponse)
from prompts.prompt_role_based import (SYSTEM_PROMPT,HUMAN_PROMPT)
from openai import OpenAI
import json


#STEP 1
llm = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)
def analyze_python_role_based(request:PythonAIRequest)->PythonAIResponse:
    
    user_prompt=HUMAN_PROMPT.format(
        learner_name=request.learner_name,
        question=request.question,
        experience_level=request.experience_level
    )
    
    response=llm.responses.parse(
        model=AZURE_OPENAI_API_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_prompt,
        text_format=PythonAIResponse)
    ai_text=response.output_text
    print("Response :",ai_text)
    
    parse_data=json.loads(ai_text)
    
    return PythonAIResponse(
        **parse_data
    )
     