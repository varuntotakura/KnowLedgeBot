import streamlit as st
from utils import llm, collection

# Initialize Streamlit app
st.title("📝 Conversational Chat with File Analysis (Llama via ChatGroq)")

# Initialize session state for chat history and file
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []
if 'uploaded_file' not in st.session_state:
    st.session_state['uploaded_file'] = None

# File uploader for articles
uploaded_file = st.file_uploader("Upload an article", type=("txt", "md", "pdf"))

# Set uploaded file in session state to retain context
if uploaded_file is not None:
    st.session_state['uploaded_file'] = uploaded_file
    article = uploaded_file.read().decode()
    st.session_state['conversation'].append({"role": "system", "content": f"Here's an article:\n\n{article}"})

# Input field for user question
question = st.text_input(
    "Ask a question about the article",
    placeholder="What would you like to know?",
    disabled=st.session_state['uploaded_file'] is None,
)

# Handle the file and question processing
if st.session_state['uploaded_file'] and question:
    article = st.session_state['uploaded_file'].read().decode()

    # Combine the article and user's current question into the prompt
    prompt = f"{article}\n\n{question}\nAnswer:"

    # Send the prompt to the Llama model via ChatGroq and get a response
    response = llm.generate(prompt)

    # Append the user's question and the model's answer to the conversation history
    st.session_state['conversation'].append({"role": "user", "content": question})
    st.session_state['conversation'].append({"role": "assistant", "content": response})

    # Store article and embeddings in ChromaDB
    doc_id = collection.add_document([article], metadata={"source": "uploaded_file"})

# Display the conversation history
if st.session_state['conversation']:
    st.write("### Conversation History")
    for message in st.session_state['conversation']:
        if message["role"] == "user":
            st.write(f"**You:** {message['content']}")
        else:
            st.write(f"**Assistant:** {message['content']}")

# Optionally clear conversation history
if st.button('Clear conversation'):
    st.session_state['conversation'] = []
