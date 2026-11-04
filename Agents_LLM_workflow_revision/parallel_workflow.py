"""parallel workflows execute multiple independent tasks at the same time."""

from typing import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph , START, END
from IPython.display import Image, display
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature = 0
     )

# Define Shared State for the paraller workflow

class ParallelState(TypedDict):
    topic : str
    explaination : str
    pros_cons = str
    applications = str

# Task 1 : Explain the Topic

def generate_explaination(state:ParallelState):
    response = llm.invoke(
        f"Explain the following topic in brief {state['topic']}"
    )
    return {"explaination": response.content}

# Task 2 : Generate Pros and Cons

def generate_pros_cons(state:ParallelState):
    response = llm.invoke(
        f"Generate pros and cons for the following topic {state['topic']}"

    )    
    return{"pros_cons": response.content}

# Task 3 : Generate Applications

def generate_applications(state:ParallelState):
    response = llm.invoke(
        f"Explain real-world applications of {state['topic']}."
    )
    return {"applications": response.content}

# Build The Graph or the actual workflow

builder = StateGraph(ParallelState)

builder.add_node("explaination", generate_explaination)
builder.add_node("pros_cons", generate_pros_cons)
builder.add_node("applications", generate_applications)

# Parallel execution

builder.add_edge(START, "explaination")
builder.add_edge(START, "pros_cons")
builder.add_edge(START, "applications")
"""Multiple edges from START allow the three nodes to execute in the same graph superstep."""

builder.add_edge("explaination", END)
builder.add_edge("pros_cons", END)
builder.add_edge("applications", END)

workflow = builder.compile()

mermaid_code = workflow.to_mermaid()
print(mermaid_code)

result = workflow.invoke({
    "topic":"Retrieval augmented generation",
    "explaination":"",
    "pros_cons":"",
    "applications":""})

print(workflow.get_graph().draw_mermaid())

