

```markdown
# 🧠 Wikipedia Chatbot using RAG (Retrieval-Augmented Generation)

This project is an intelligent chatbot that answers questions using content retrieved from **Wikipedia**. It uses **Retrieval-Augmented Generation (RAG)** to improve the accuracy and relevance of answers by combining retrieval and generation.

---

## 🔧 Features

- 🧠 **RAG-based architecture** (Retriever + LLM)
- 📄 Vector store powered by FAISS
- 🧩 Local embedding using `sentence-transformers`
- 🗂️ Context-aware prompt generation
- 🔁 Memory support for persistent chat history
- 🤖 LLM powered by `Groq` + `LLaMA3`

---

## 📂 Project Structure

```

📁 Wikipedia-chatbot-rag
├── create\_memory\_for\_llm.py    # Step 1: Builds the vector DB and embeddings
├── connect\_memory\_to\_llm.py    # Step 2: Connects memory to the LLM
├── main.py                     # Step 3: Starts the chatbot
└── README.md                   # You’re reading it!

````

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Abdulraheem232/Wikipedia-chatbot-rag.git
cd Wikipedia-chatbot-rag
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file and add your Groq API key:

```
API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the Chatbot (in order)

1. **Build the vector memory**

```bash
python create_memory_for_llm.py
```

2. **Connect the memory to the LLM**

```bash
python connect_memory_to_llm.py
```

3. **Start the chatbot**

```bash
python main.py
```

---

## 🧰 Technologies Used

* [LangChain](https://www.langchain.com/)
* [HuggingFace Transformers](https://huggingface.co/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Groq API](https://groq.com/)
* [Python 3.10+](https://www.python.org/)

---

## 🤝 Contributions

Pull requests are welcome. If you’d like to contribute, fork the repo and submit a PR.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* LangChain documentation
* HuggingFace models
* Wikipedia API
* Groq for LLaMA3 support

```

---

```
