import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_ENDPOINT=os.getenv("OPENAI_ENDPOINT")
OPENAI_MODEL_NAME=os.getenv("OPENAI_MODEL_NAME")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
OPENAI_API_VERSION=os.getenv("OPENAI_API_VERSION")