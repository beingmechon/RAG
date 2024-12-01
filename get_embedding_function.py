import getpass
import os

# os.unsetenv("OPENAI_API_KEY")

# from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings
# from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_aws.embeddings.bedrock import BedrockEmbeddings
from langchain_huggingface.embeddings.huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

EMBEDDING_MODEL = "openai"

def get_embedding_function(embedding_model):

    if embedding_model == "aws_bedrock":
        embeddings = BedrockEmbeddings(credentials_profile_name="default", region_name="us-east-1")

    elif embedding_model == "openai":
        while not os.getenv("OPENAI_API_KEY"):
            print("Please add your OpenAI API key in the environment below or add key to the .env file.")
            os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
                
        embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    elif embedding_model == "huggingface":
        embeddings = HuggingFaceEmbeddings("sentence-transformers/all-mpnet-base-v2")

    elif embedding_model == "ollama":
        embeddings = OllamaEmbeddings(model="nomic-embed-text")

    else:
        print("Unknown embedding model")

    return embeddings
