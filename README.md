# 🧠 LLM-Powered PDF Query Assistant (RAG-based)

This is a simple yet powerful PDF Question-Answering chatbot built using **LangChain**, **OpenAI LLMs**, **FAISS Vector DB**, and **Streamlit**. The app lets you upload a PDF and ask questions about its contents — providing accurate answers by combining retrieval with generation.

---

## 🔍 What It Does

- 📄 **Upload PDFs**  
  Drop in any PDF and the app will read and index its content.

- ❓ **Ask Questions**  
  Query anything from the uploaded file — it retrieves the relevant chunks and generates meaningful answers using LLM.

- ⚙️ **Powered by Retrieval-Augmented Generation (RAG)**  
  Combines vector search and generative AI to deliver contextually accurate responses.

---

## ⚙️ Tech Stack

- **Python**
- **LangChain**
- **OpenAI GPT API**
- **FAISS (Vector Search)**
- **Streamlit (Frontend UI)**
- **PyPDF2** (for PDF parsing)

---

## 🚀 How It Works

1. **PDF Parsing**  
   → Extracts text using `PyPDF2`.

2. **Text Splitting**  
   → Splits text into chunks using `LangChain`'s `CharacterTextSplitter`.

3. **Embedding & Vector Store**  
   → Embeds chunks using `OpenAI Embeddings` and stores in `FAISS`.

4. **Querying**  
   → Takes user questions, finds relevant text chunks, and answers using an LLM.

---

## 🧑‍💻 How to Run

# Clone the repository
git clone https://github.com/yourusername/LLM-PDF-Query.git
cd LLM-PDF-Query

# Set up the virtual environment
python -m venv venv
# Activate the virtual environment
# For macOS/Linux:
source venv/bin/activate
# For Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your OpenAI API key
echo OPENAI_API_KEY=your_openai_key_here > .env

# Run the Streamlit app
streamlit run main.py

 
