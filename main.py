import os
# GROQ_API_KEY="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"

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
user_input = input("Ask a question: ")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ],
    model="lla192",
)

print(chat_completion.choices[0].message.content)