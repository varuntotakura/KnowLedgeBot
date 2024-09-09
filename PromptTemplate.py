from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json

with open('credentials.json', 'r') as file:
    data = json.load(file)

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    groq_api_key = data['groq_api'],
    temperature=0.2
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
print(chain.invoke(
    {
        "input_language": "English",
        "output_language": "Telugu",
        "input": "I love programming.",
    }
).content
)