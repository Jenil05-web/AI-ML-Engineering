from langchain_openai import ChatOpenAI
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
load_dotenv()

"""A linear, step-by-step pipeline where tasks execute in a strict, predefined order. 
   The output of one step directly serves as the input for the next."""
# Initialize llm

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

# Define Workflow : 

class WorkflowState(TypedDict):
    topic: str
    research:str
    summary:str

def research_topic(state:WorkflowState):
    response = llm.invoke(
        f"Explain the following topic in breif {state['topic']}"
    )
    return {"research": response.content}

def summarize_research(state:WorkflowState):
    response = llm.invoke(
        f"Summarize this research into 5 key points: {state['research']}"

    )
    return {"summary": response.content}

builder = StateGraph(WorkflowState)
builder.add_node("research", research_topic)
builder.add_node("summarizer", summarize_research)

builder.add_edge(START, "research")
builder.add_edge("research", "summarizer")
builder.add_edge("summarizer", END)

# Compile the workflow 
workflow = builder.compile()

# Execute the Workflow
result = workflow.invoke({
    "topic":"Retrieval augmented generation",
    "research":"",
    "summary":""
})

print("\nFINAL SUMMARY:\n")
print(result["summary"])

    