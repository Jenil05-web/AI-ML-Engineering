from agents.db_agent import agent

question = "What products do we sell?"

result = agent.invoke({
    "messages": [
        {"role": "user", "content": question}
    ]
})

print(result["messages"][-1].content)