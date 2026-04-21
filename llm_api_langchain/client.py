import streamlit as st
import requests

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", json={"input": {"topic": input_text}})
    return response.json()['output']

st.title("Langchain Demo with OpenAI and Llama2 API Chains")

essay_input = st.text_input("Write an essay on ", key="essay_input")
poem_input = st.text_input("Write a poem on ", key="poem_input")

if essay_input:
    st.write(get_openai_response(essay_input))

if poem_input:
    st.write(get_ollama_response(poem_input))
