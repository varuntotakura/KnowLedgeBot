from utils import *
import uuid
import chromadb

client = chromadb.PersistentClient('vectorstore')
collection = client.get_or_create_collection(name="portfolio")

# if not collection.count():
#     for _, row in df.iterrows():
#         collection.add(documents=row["Techstack"],
#                        metadatas={"links": row["Links"]},
#                        ids=[str(uuid.uuid4())])

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