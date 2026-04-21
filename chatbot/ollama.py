from langchain_openai import ChatOpenAI
from langchain_ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]= "true"
os.environ["LANGCHAIN_PROJECT"]= "Ollama API Demo"
os.environ["OLLAMA_KEY"] = os.getenv("OLLAMA_KEY")
# creating chatbot

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question:{question}"),
])

st.title("Ollama API Demo")
input_text = st.text_input("Ask a question !")

llm = Ollama(model="llama2", temperature=0)
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text :
    st.write(chain.invoke({"question": input_text}))
else :
    st.write("Please enter a question to get a response from the chatbot.")