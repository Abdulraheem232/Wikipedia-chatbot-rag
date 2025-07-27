from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq 
from langchain_core.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import os
import dotenv

dotenv.load_dotenv()

model_name = "llama3-8b-8192"

def load_llm(model_name):
    model = ChatGroq(model_name=model_name,api_key=os.environ["API_KEY"])
    return model

chat_prompt_insturctions = """Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context

Context: {context}
Question: {input}

Start the answer directly. No small talk please."""

def create_prompt_template():
    prompt_template = PromptTemplate(
        input_variables=["context", "input"],
        template=chat_prompt_insturctions
    )
    return prompt_template

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = FAISS.load_local("vectorstore/faiss",embeddings=embedding_model,allow_dangerous_deserialization=True)


# Create the document chain
document_chain = create_stuff_documents_chain(
    llm=load_llm(model_name),
    prompt=create_prompt_template(),
    
)

# Create the retrieval chain
retriever = vector_db.as_retriever()
chain = create_retrieval_chain(retriever, document_chain)

