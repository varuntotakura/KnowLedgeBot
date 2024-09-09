from langchain_groq import ChatGroq
import json

with open('credentials.json', 'r') as file:
    data = json.load(file)

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    groq_api_key = data['groq_api'],
    temperature=0.2,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2,
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that answers questions as explaining to a five year old.",
    ),
    ("human", "Explain about earth"),
]
ai_msg = llm.invoke(messages)
# print(ai_msg)

print(ai_msg.content)

