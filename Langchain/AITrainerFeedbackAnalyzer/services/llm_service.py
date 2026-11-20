import json
from openai import AzureOpenAI 
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)
 
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from models.trainer_feedback_model import TrianerFeedbackRequest,TrainerFeedbackResponse
from prompts.trainer_feedback_prompt import (HUMAN_PROMPT,SYSTEM_PROMPT)
llm= AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

#structure llm
structure_llm=llm.with_structured_output(TrainerFeedbackResponse)

#create prompt
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",SYSTEM_PROMPT),
        ("human",HUMAN_PROMPT)
     ]
    
    
    
)


chain=prompt | structure_llm

#create function
def analyze_feedback(request:TrianerFeedbackRequest)->TrainerFeedbackResponse:
    result=chain.invoke(
        
        {
            "trainer_name":request.trainer_name,
            "training_topic":request.training_topic,
            "learner_name":request.learner_name,
            "rating":request.rating,
            "feedback":request.feedback
            
        }
        
    )
    return result
    
    # response_dict = json.loads(result.content)

    # return TrainerFeedbackResponse(**response_dict)

