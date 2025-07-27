from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
import wikipedia
from langchain_community.vectorstores import FAISS

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

topics = ["Python (programming language)", "Artificial intelligence", "Internet of Things"]

def fetch_pages(topics):
    data = []
    for topic in topics:
        try:
            page = wikipedia.page(topic)
            data.append({
                "title": page.title,
                "url": page.url,
                "content": page.content
            })
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"DisambiguationError for {topic}: {e.options[:3]}")
        except wikipedia.exceptions.PageError:
            print(f"PageError: {topic} not found")
    return data

wiki_data = fetch_pages(topics)

documents = []
for item in wiki_data:
    chunks = splitter.create_documents(item["content"])
    documents.append(chunks)

def create_vectorembedding_model(model_name):
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    return embedding_model


vectorstore_path = "vectorstore/faiss"
vectordb = FAISS.from_documents(chunks,embedding=create_vectorembedding_model("sentence-transformers/all-MiniLM-L6-v2"))
vectordb.save_local(vectorstore_path)