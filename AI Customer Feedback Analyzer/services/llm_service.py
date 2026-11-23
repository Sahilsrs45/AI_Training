from langchain_openai import AzureChatOpenAI

from langchain_core.prompts import (
    ChatPromptTemplate
)

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_VERSION
)

from prompts.feedback_prompt import (
    SYSTEMPROMPT,
    HUMANPROMPT
)

from models.feedback_model import (
    FeedbackRequest,
    FeedbackResponse
)

llm = AzureChatOpenAI(

    api_key=AZURE_OPENAI_API_KEY,

    azure_endpoint=AZURE_OPENAI_ENDPOINT,

    azure_deployment=AZURE_OPENAI_DEPLOYMENT,

    api_version=AZURE_OPENAI_API_VERSION
)

structured_llm = llm.with_structured_output(
    FeedbackResponse
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEMPROMPT),
        ("human", HUMANPROMPT)
    ]
)

chain = prompt | structured_llm


def analyze_feedback(
    request: FeedbackRequest
):

    result = chain.invoke({

        "customer_id":
        request.customer_id,

        "customer_name":
        request.customer_name,

        "order_id":
        request.order_id,

        "rating":
        request.rating,

        "feedback":
        request.feedback
    })

    return result