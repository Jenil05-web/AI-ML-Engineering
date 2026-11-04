"""Tools are simple python functions which holds certain capabilities. They can be used to perform specific tasks or operations within a workflow."""
# Tool calling with Python 

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import ToolMessage

# Define a tool using @tool decorator 
# The @tool decorator converts a Python function into a LangChain tool.
@tool
def multiply(a:int, b:int)->int:
    "Multiply two numbers"
    return a*b

# Bind the tool into LLM

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

llm_with_tools = llm.bind_tools([multiply])
# bind_tools is a method that allows you to integrate the defined tools into the LLM, enabling it to utilize these tools during its operations.
# bind_tools tells the LLM that it can use the multiply tool when needed.( Just Informs !)
response = llm_with_tools.invoke(
    "Multiply 5 and 10 using the multiply tool."
)
print(response.tool_calls)

tools = [multiply] # create a list of tools. 
# it is a list of python functions that can be used to perform specific tasks or operations within a workflow.

tool_results = []

for tool_call in response.tool_calls:
    selected_tool = multiply
    result = selected_tool.invoke(tool_call["args"]) # contains the arguments selected by the LLM, such as {"a": 25, "b": 48}

tool_results.append(
        ToolMessage(
            content=str(result),
            tool_call_id=tool_call["id"]
        )
    )

final_response = llm.invoke(
    [
        ("human", "What is 25 multiplied by 48?"),
        response,
        *tool_results
    ]
)

print(final_response.content)
