from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
 
from config.settings import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)
from prompts.ai_prompt import (HUMAN_PROMPT, SYSTEM_PROMPT)
from models.trainer_model import (TrainerRequest, TrainerResponse)
 
# creaing llm
llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT
)
 
# Structured output
structure__llm = llm.with_structured_output(
    TrainerResponse
)
 
# creating the prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("user", HUMAN_PROMPT)
    ]
)
# create the langchain
chain = prompt | structure__llm
 
 
# initializing the function
def analyze_trainer(request: TrainerRequest) -> TrainerResponse:
 
    result = chain.invoke({
        "trainer_name": request.trainer_name,
        "learner_name": request.learner_name,
        "trainer_rating": request.trainer_rating,
        "trainer_feedback": request.trainer_feedback,
        "trainer_topic": request.trainer_topic
    })
 
    return result