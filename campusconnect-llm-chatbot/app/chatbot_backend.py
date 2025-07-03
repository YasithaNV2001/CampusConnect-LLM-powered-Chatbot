import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Azure OpenAI Configuration
openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"

deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")

def ask_bot(user_input):
    try:
        # Load prompt template
        with open("prompts/academic_assistant_prompt.txt", "r") as f:
            system_prompt = f.read()

        response = openai.ChatCompletion.create(
            engine=deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"
