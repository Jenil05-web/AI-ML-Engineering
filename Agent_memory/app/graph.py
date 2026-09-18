from langgraph.graph import StateGraph , START , END , MessagesState
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
import os

llm = ChatOpenAI(
    model = "gpt-3.5-turbo",
    temperature=0
)

def chatbot(state:MessagesState):
    response = llm.invoke(
        state["messages"]

    )
    return {
        "messages":[response]
    }
    

builder = StateGraph(MessagesState)
builder.add_node("chatbot", chatbot)

builder.add_edge(START, "chatbot")

builder.add_edge("chatbot", END)
checkpointer = MemorySaver()

graph = builder.compile(
    checkpointer=checkpointer
)


