import streamlit as st
from augmentation import prompt_creation_and_api_calls

st.set_page_config(page_title="RAG Demo", layout="centered")

st.title("RAG: Retrieval-Augmented Generation Demo")
st.write("Type your query below. The system will retrieve relevant documents and generate an answer.")

query = st.text_input("Enter your query:", "")

if st.button("Generate Answer"):
    if not query.strip():
        st.warning("Please enter a query!")
    else:
        with st.spinner("Processing..."):
            answer = prompt_creation_and_api_calls(query)
        st.subheader("Generated Answer")
        st.write(answer)
