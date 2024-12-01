from langchain_community.document_loaders import JSONLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
# from langchain_community.document_loaders import PyPDFDirectoryLoader

from glob import glob
from pathlib import Path

def document_loaders(data_path):
    files = glob(data_path, recursive=True)

    docs = []

    for file in files:
        if file.endswith(".json"):
            loader = JSONLoader(file_path=file, jq_schema='.', text_content=False)
        elif file.endswith(".pdf"):
            loader = PyPDFLoader(file)
        elif file.endswith(".txt"):
            loader = TextLoader(file)
        elif file.endswith(".md"):
            loader = UnstructuredMarkdownLoader(file)
        else:
            print("Unknown file type: " + file)

        doc = loader.load()
        docs.append(doc)

    return  docs



if __name__ == "__main__":
    DATA_PATH = "./data/*/*"

    docs = document_loaders(data_path=DATA_PATH)
    print(len(docs))
    print(docs)
    print

