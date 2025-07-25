import streamlit as st
import requests

st.title("Local LLM Chatbot")
user_input = st.text_input("Enter your message:")

if st.button("Send"):
    response = requests.post("http://localhost:8000/chat", json={"message": user_input})
    st.write("Bot:", response.json()["response"])