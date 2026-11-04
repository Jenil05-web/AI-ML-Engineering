from typing import Literal, TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

# Define the state

class SupportState(TypedDict):
    query:str
    category: str
    response:str

    # Node 1 :Classify query 

def classify_query(state:SupportState):
    prompt = f"Classify the following query into one of the following categories: Billing, Technical Support, Account Management, or General Inquiry. Return only category Query: {state['query'] ,}"

    result = (prompt|llm).invoke({
        "query":state["query"]
    })

    category = result.content.strip().lower()

    if category not in ["billing", "technical", "general"]:
        category = "general"

    return {"category":category}


# Routing function
def route_query(
    state: SupportState
) -> Literal["billing", "technical", "general"]: # "Literal" means the return value must be one of the specified strings.

    return state["category"]


# Node 2 : Billing
def billing_support(state:SupportState):
    response = llm.invoke(
        f"help with this billing query:{state['query']}"
    )

    return{"response": response.content}


# Node 3 : Technical support

def technical_support(state:SupportState):
    response = llm.invoke(
        f"Help with the following technical query :{state['query']}"
    )
    return {"response":response.content}

# Node 4 : general Support

def general_support(state:SupportState):
    response = llm.invoke(
        f"Help with the above general query : {state['query']}"

    )
    return {"response": response.content}

# Build graph

builder = StateGraph(SupportState)

builder.add_node("classify",classify_query )
builder.add_node("billing", billing_support)
builder.add_node("technical", technical_support)
builder.add_node("general", general_support)

builder.add_edge(START, "classify")

builder.add_conditional_edges(
    "classify",
    route_query,{}
)

builder.add_edge("billing", END)
builder.add_edge("technical", END)
builder.add_edge("general", END)

workflow = builder.compile()

# Execute Workflow

result = workflow.invoke({
    "query": "I was charged twice for my subscription",
    "category":"",
    "response":""
})

print("Category:", result["category"])
print("Response:", result["response"])