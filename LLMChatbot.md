# SEQATO LLM Awareness – Month 1 Projects

## 🧠 Overview of Tools & Technologies

### 🔹 LLMs (Large Language Models)
Used for tasks such as chat, summarization, Q&A, and more.

---

### 🔧 Technologies Involved

- **Streamlit** → Frontend (UI)
- **FastAPI** → Backend (API layer)
- **Ollama** → Local LLM engine (e.g., LLaMA2, Mistral)
- **Python** → Core Programming Language

---

### ✅ Tool Descriptions

#### 1. **Streamlit**
Streamlit is an open-source Python framework for building simple, interactive web apps—especially useful for data science and machine learning.

- Easily turns Python scripts into shareable web apps.
- Common UI elements: `st.write()`, `st.button()`, `st.file_uploader()`.
- Used for:
  - Chat App interface
  - Document Summarization UI

#### 2. **FastAPI**
FastAPI is a modern, high-performance Python framework for building APIs with type hints.

- Fast and easy to build scalable REST APIs.
- Used as backend for the LLM Chat App to:
  - Receive chat input from Streamlit
  - Query Ollama for LLM response
  - Return result to frontend

#### 3. **Ollama**
Ollama lets you run LLMs locally without internet-based APIs like OpenAI.

- Supports open-source models like **Llama2**, **Mistral**, **Llava**.
- No external costs and ensures full data privacy.
- Accessed via simple REST API.

#### 4. **Python**
A versatile, beginner-friendly language powering all components of the program:

- Backend logic (FastAPI)
- Frontend UI (Streamlit)
- LLM inference (Ollama or Hugging Face)
- PDF handling and NLP tasks

---

## 📌 Project 1 — Local LLM Chat App

### 🛠 Tools Used
- Python  
- Streamlit  
- FastAPI  
- Ollama  

### ⚙️ How to Run

```bash
# Run backend API
uvicorn server:app --reload

# Run Streamlit frontend
streamlit run app.py
