import boto3
from langchain_community.embeddings import BedrockEmbeddings ## Bedrock
from langchain.text_splitter import RecursiveCharacterTextSplitter ## Text Splitter
from langchain_community.document_loaders import PyPDFLoader ## Pdf Loader
from langchain_community.vectorstores import FAISS ## import FAISS
import streamlit as st
import os
import uuid


## s3_client
s3_client = boto3.client("s3")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Define Helper Functions
def get_unique_id():
    return str(uuid.uuid4())

# Main Function for Streamlit Application
## main method
def main():
    st.write("Hello world")
    uploaded_file = st.file_uploader("Choose a file", "pdf")
    if uploaded_file is not None:
        request_id = get_unique_id()
        st.write(f"Request Id: {request_id}")
        saved_file_name = f"{request_id}.pdf"
        with open(saved_file_name, mode="wb") as w:
            w.write(uploaded_file.getvalue())
        
        loader = PyPDFLoader(saved_file_name)
        pages = loader.load_and_split()

        st.write(f"Total Pages: {len(pages)}")

        ## Split Text
        splitted_docs = split_text(pages, 1000, 200)
        st.write(f"Splitted Docs length: {len(splitted_docs)}")
        st.write("===================")
        st.write(splitted_docs[0])
        st.write("===================")
        st.write(splitted_docs[1])



if __name__ == "__main__":
    main()