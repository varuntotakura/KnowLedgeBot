from langchain_groq import ChatGroq
import json
import chromadb

client = chromadb.Client()
collection = client.create_collection(name = "DB_Collection")

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