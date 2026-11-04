from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START , END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool


@tool # -> Converts python function into a tool 
def multiply(a:int, b:int)-> int:
    "Multiply two integers"
    return a*b

tools = [multiply] # -> Creates a list of tools that can be used by our agent.

llm = ChatOpenAI(   
    model = "gpt-4o-mini",
    temperature = 0 
).bind_tools(tools) # -> Tells the LLM that which tool it can use

class AgentState(TypedDict):
    messages: Annotated[list, add_messages] # -> Annotated is used to add metadata to the messages field, indicating that it should be treated as a list of messages.
    # add_messages is a function that adds messages to the state.
    # It tells LangGraph how to update the message list: new messages should be added to the existing conversation, rather than replacing it.

def call_model(state:AgentState):
    response = llm.invoke(state["messages"]) # retrieves the conversation so far
    return {"messages":[response]} # Adds the llm response to the state.

builder = StateGraph(AgentState)

builder.add_node(START, call_model)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "llm")
builder.add_conditional_edges(
    "llm",
    tools_condition
)
builder.add_edge("tools", "llm")
graph = builder.compile()

result = graph.invoke({
    "messages": [
        HumanMessage(
            content="What is 25 multiplied by 48?"
        )
    ]
})

print(result["messages"][-1].content)


"""MULTI TOOL CALLING AGENT"""


from typing import TypedDict, Annotated

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


SYSTEM_PROMPT = """You are a helpful assistant that can perform various tasks using the tools provided.

Your responsibilities:
1. Understand the user's question.
2. Select the appropriate tool whenever necessary.
3. If multiple calculations are required, use tools in the correct order.
4. Do not invent calculation results.
5. Provide a clear final answer after receiving tool results.
6. If no tool is required, answer directly."""


@tool
def addition(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@tool
def get_weather(city: str) -> str:
    """Get simulated weather information for a city."""
    return f"The weather in {city} is sunny."


tools = [addition, multiply, get_weather]

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
).bind_tools(tools)


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


def call_model(state: AgentState):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"]
    ]

    response = llm.invoke(messages)

    return {"messages": [response]}


builder = StateGraph(AgentState)

builder.add_node("llm", call_model)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "llm")

builder.add_conditional_edges(
    "llm",
    tools_condition
)

builder.add_edge("tools", "llm")

graph = builder.compile()


result = graph.invoke({
    "messages": [
        HumanMessage(
            content="Multiply 5 and 3 and then add 2 in it, after that give me current weather in London."
        )
    ]
})

print(result["messages"][-1].content)
