from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

## Enviroments variables call

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY") # bascially we got the API key from the .env file .

# Langsmith tracking used for tracing 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") # similarly we got the API key for langsmith from the .env file and set it as an environment variable. This allows us to use the langsmith tracking features in our application, which can help us monitor and analyze the performance of our language model interactions.
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_TRACING_V2"] = "true" # this means that we are enabling version 2 of langchain tracking.( basically it helps in tracing in website of langsmith)
os.environ["LANGCHAIN_PROJECT"] = "Projects"

# Creating Chatbot 

prompt = ChatPromptTemplate.from_messages([ # here ChatPromptTemplate is a class that allows us to create a prompt for our chatbot. The from_messages method is used to create a prompt template from a list of messages. Each message is a tuple that consists of a role (like "system" or "user") and the content of the message. In this case, we have two messages: one from the system that sets the context for the chatbot ("You are a helpful assistant."), and one from the user that contains the question they want to ask the chatbot ("Question:{question}"). The {question} part is a placeholder that will be replaced with the actual question input by the user when we invoke the chain later on.
    ("system", "You are a helpful assistant."),
    ("user", "Question:{question}"),
])

# streamlit framework : it is used to create a web application for the chatbot. It allows us to create an interactive interface where users can input their questions and receive responses from the chatbot. The st.title() function is used to set the title of the web application, which in this case is "Langchain Demo with OpenAI API".

st.title("Langchain OpenAI API Demo")
input_text = st.text_input("Ask a question !") # this line creates an text input field in streamlit where we can type our questions.

# Open AI LLM call 

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
output_parser = StrOutputParser() # It is used to parse the output from the language model into a string format. This is necessary because the language model may return its response in a structured format (like JSON), and we want to convert it into a simple string that can be easily displayed in the chatbot interface.

# chain it is a sequence of operations that are executed in order. In this case, the chain consists of three components: the prompt, the language model (LLM), and the output parser. The prompt is used to generate a response from the language model based on the user's input. The LLM processes the prompt and generates a response, which is then passed to the output parser to convert it into a string format that can be displayed in the chatbot interface.
chain = prompt | llm | output_parser # main line of langchain it will execute the chain of orders in an specifc format .

if input_text :
    st.write(chain.invoke({"question": input_text})) # this line means that if the user has entered some text in the input field, we will invoke the chain with the user's question. The chain will process the question through the prompt, generate a response using the language model, and then parse the output into a string format. Finally, we will display the response in the chatbot interface using st.write().
else :
    st.write("Please enter a question to get a response from the chatbot.") # this line means that if the user has not entered any text in the input field, we will display a message prompting them to enter a question in order to receive a response from the chatbot. This helps guide the user to interact with the chatbot and ensures that they understand how to use the interface effectively.