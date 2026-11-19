from typing import TypedDict , Annotated

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

# Define the State

class AgentState(TypedDict):
    messages:Annotated[list,add_messages]

# Initialize the LLM

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature=0
)   

store = InMemoryStore()
user_namespace = ("users", "user_123", "memories")

# Save user information
store.put(
    user_namespace,
    "user_profile",
    {
        "name":"Alex",
        "programming_language":"Python",
        "goal": "I want to become an AI Engineer"

    }
)

# Create an LLM node
def call_model(state: AgentState, config, *, store):
    user_id = config["configurable"]["user_id"]

    user_namespace = ("users", user_id, "memories")

    memory = store.get(
        user_namespace,
        "user_profile"
    )

# Convert Retrieved memory in text
#     