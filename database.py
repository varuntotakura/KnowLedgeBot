from utils import *

collection.add(
    documents = [
        "Document about New York",
        "Document about France",
        "Document about Italy"
    ],
    ids = ['id1', 'id2', 'id3'],
    metadatas=[
        {"url":""},
        {"url":""},
        {"url":""}
    ]
)

documents = collection.get()

results = collection.query(query_texts=['Query about Capitol'], n_results = 2)

print(results)