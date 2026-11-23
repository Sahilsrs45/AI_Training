from openai import AzureOpenAI

from config.settings import *

from prompts.billing_prompt import (
    SYSTEM_PROMPT,
    HUMAN_PROMPT
)

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION
)


def generate_bill_explanation(
        customer_name,
        membership_tier,
        invoice_data
):

    human_prompt = HUMAN_PROMPT.format(
        customer_name=customer_name,
        membership_tier=membership_tier,
        invoice=invoice_data
    )

    response = (
        client.chat.completions.create(
            model=
            AZURE_OPENAI_DEPLOYMENT,

            messages=[
                {
                    "role":
                    "system",
                    "content":
                    SYSTEM_PROMPT
                },
                {
                    "role":
                    "user",
                    "content":
                    human_prompt
                }
            ]
        )
    )

    return response.choices[
        0
    ].message.content