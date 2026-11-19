from typing import TypedDict
from langgraph.graph import StateGraph, START
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command

# Define workflow state
class AgentState(TypedDict):
    email:str 
    decision : str
    statuts:str


def human_review(state: AgentState):
    decision = interrupt({ # it is used to interrupt the agent , here is where the workflow pauses for permission
        "question": "Do you approve sending this email",
        "email": state["email"]
    })

    if decision == "approve":
        return Command(
            update={"decision":"approved"},
            goto = "send_email" 

        )

    return Command(
        update = {"decision" == "rejected"},
        goto="cancel_email"

    )

# Send email if approved

def send_email(state:AgentState):
    print('Sending email ..')
    print(state["email"])

    return {"status": "sent"}

# Cancel if rejected

def cancel_email(state:AgentState):
    print("Email was not sent")
    return{"status": "cancelled"}

builder = StateGraph(AgentState)
builder.add_node("human_review", human_review)
builder.add_node("send_email", send_email)
builder.add_node("cancel_email", cancel_email)
builder.add_edge(START, "human_review")

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# 7. Start the workflow
config = {
    "configurable": {
        "thread_id": "email_1"
    }
}

result = graph.invoke(
    {
        "email": "Hello! This is a test email.",
        "decision": "",
        "status": ""
    },
    config=config
)

print(result)


print("Paused Workflow :", result)

decision = input("Approve this email (yes/no):")

if decision.lower() =="yes":
    human_decision = "approve"
else:
    human_decision = "reject"

    #  Resume the interrupted workflow
result = graph.invoke(
    Command(resume=human_decision),
    config=config
)

print("Final result:", result)
