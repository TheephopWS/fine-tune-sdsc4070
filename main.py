import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
model = "ministral-8b-2410"

client = Mistral(api_key=MISTRAL_API_KEY)

response = client.chat.complete(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)

print(response.choices[0].message.content)