# Sequential Workflow : 
"A linear, step-by-step pipeline where tasks execute in a strict, predefined order. The output of one step directly serves as the input for the next."

In sequential workflows, execution follows a fixed path.

# Parallel Workflow :
"pattern where multiple independent tasks or sub-agents execute simultaneously, and their outputs are later aggregated or merged."

In parallel workflows, multiple branches execute together.

# Conditional Workflow
"How it Works: If condition $X$ is met, go to Module A; else if condition $Y$ is met, go to Module B."

In conditional workflows, the next step is selected based on a condition or decision.

Uses add_conditional_edges() for dynamic routing.

# Tool Calling :
Tool calling allows an LLM to request the execution of external functions or tools when it needs additional capabilities.

@tool: Converts a Python function into a LangChain tool.

bind_tools(): Makes tools available to the LLM.

# 4. LangGraph Fundamentals

State: Stores information shared across workflow nodes.

Node: A function that performs a specific task and returns state updates.

Edge: Defines the connection and execution flow between nodes.

Reducer: Defines how state updates are combined with existing state.

StateGraph: Used to construct workflows.

START and END: Represent workflow entry and exit points.

TypedDict defines the structure of agent state.

Annotated[list, add_messages] defines a message list with an append/update reducer.

state["messages"] provides access to conversation history.

Nodes return state updates using dictionaries

# Memory in AI Agents :

Short Term Memory - remembers message within an conversation
Long Term Memory - Retains information across different conversations

Short Term Memory :

memory = InMemorySaver() , it is used in langgrapgh for managing the memory of chats in conversation.

config = {
    "configurable": {
        "thread_id": "user_1"
    }
}
 Unique thread ID is given to map the conversation later on







