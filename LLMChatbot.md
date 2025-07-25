# 🗨️ Local LLM Chat App

This project is part of the SEQATO LLM Awareness & Portfolio Development Program.

It demonstrates a full-stack application that enables real-time interaction with a locally running Large Language Model (LLM) using **Streamlit (frontend)**, **FastAPI (backend)**, and **Ollama (local LLM engine)**.

---

## 🧠 LLMs (Large Language Models)

Large Language Models (LLMs) are AI models trained to understand and generate human-like text. They can answer questions, summarize content, assist in coding, and more.

---

## 🛠️ Technologies Involved

| Tool         | Role                    |
|--------------|--------------------------|
| **Streamlit** | Frontend (UI)            |
| **FastAPI**   | Backend (API layer)      |
| **Ollama**    | Local LLM engine         |
| **Python**    | Core programming language|

---

### 🔍 Tool Descriptions

#### ✅ Streamlit
Streamlit is an open-source Python framework for building interactive web apps quickly. It's especially used in data science and ML projects. It allows developers to create web UIs using simple Python commands like `st.write()`, `st.button()`, and `st.file_uploader()`.

In this project, **Streamlit is used to create the frontend UI** for the chat application, allowing users to input messages and view LLM-generated responses in a web browser without complex frontend development.

---

#### ✅ FastAPI
FastAPI is a fast and easy-to-use web framework for building APIs with Python 3.6+ using type hints.

In this project, **FastAPI serves as the backend server** that:
- Accepts chat input from Streamlit
- Sends the message to the Ollama LLM
- Returns the generated response back to Streamlit

---

#### ✅ Ollama
Ollama is a platform that enables users to run **Large Language Models locally** (offline). It supports open-source models like:
- **LLaMA2**
- **Mistral**
- **LLaVA** (for multi-modal)

Ollama exposes a local API that allows interaction with these models — no internet required, ensuring full privacy and zero API cost.

---

#### ✅ Python
Python is used for:
- Building both the **backend (FastAPI)** and **frontend (Streamlit)**
- Handling communication with Ollama
- Managing application logic

It’s a top choice for LLM development due to its simplicity and strong library ecosystem.

---

## 🔄 Workflow

1. 💬 **User sends a message via Streamlit UI**
2. 🚀 **Streamlit calls the FastAPI backend (`/chat` endpoint)**
3. 🧠 **FastAPI sends the message to Ollama LLM (e.g., LLaMA2)**
4. 🤖 **Ollama returns a generated response**
5. 🌐 **Frontend displays the LLM response to the user**
