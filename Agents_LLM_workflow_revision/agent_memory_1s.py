"""Implementing Short term memory for the Agent"""

from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages:Annotated[list, add_messages]

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

def call_model(state:AgentState):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

builder = StateGraph(AgentState)

builder.add_node("llm", call_model)
builder.add_edge(START, "llm")
memory = InMemorySaver() # -> This creates an in-memory checkpointer that saves graph state between executions
graph = builder.compile(checkpointer=memory)

config = {
    "configuration":{
        "thread_id":"user_1" # -> ID is given because we want to save the state of the graph for a specific user. This allows us to maintain a conversation with that user across multiple invocations of the graph.
    }
}
response1 = graph.invoke({
    "messages":[
        HumanMessage(content="My name is Alex")
    ]
},
config = config)

print(response1["messages"][-1].content)

response2 = graph.invoke(
    {
        "messages": [
            HumanMessage(content="What is my name?")
        ]
    },
    config=config
)

print(response2["messages"][-1].content)

""""""

"""Managing multiple conversations using Thread IDs"""


# Conversation for User A
config_a = {
    "configurable":{
        "thread_id": "user_A"
    }
}

# Conversation for User B

config_b ={
    "configurable":{
        "thread_id": "user_B"
    }
}

# User A's first message

graph.invoke({
    "messages":[
        HumanMessage(content = "Hello, I am Alex")
    ]
},
config = config_a)

# User B's first message

graph.invoke({
    "messages":[
        HumanMessage(content="My name is John")
    ]
},
config = config_b)

# Ask for user A name

response_a = graph.invoke({"messages":[
    HumanMessage(content="What is my name ?")
]}, config = config_a)

print("User A:", response_a["messages"][-1].content)

# Ask User B question

response_b = graph.invoke({
    "messages":[
        HumanMessage(content="What is my name ?")
    ]
}, config = config_b) 

print("User B:", response_b["messages"][-1].content)
