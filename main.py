from utils import *

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

