import streamlit as st
from pdf_processing import extract_pdf_text, split_text
from vector_store import create_vector_store
from qa_chain import get_qa_chain, answer_query
import openai
import os

# Explicitly set the OpenAI API key here if not done globally
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App
def main():
    st.title("PDF Query System")

    # PDF Upload
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file is not None:
        with st.spinner("Processing the PDF..."):
            # Save the uploaded file temporarily
            with open("uploaded_file.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Extract text and split into chunks
            raw_text = extract_pdf_text("uploaded_file.pdf")
            texts = split_text(raw_text)

            # Create the vector store
            document_search = create_vector_store(texts)

            # Initialize QA chain
            chain = get_qa_chain()

            # Query Input
            query = st.text_input("Ask a question about the PDF:")
            if query:
                with st.spinner("Getting the answer..."):
                    answer = answer_query(chain, document_search, query)
                    st.write(answer)

if __name__ == "__main__":
    main()
