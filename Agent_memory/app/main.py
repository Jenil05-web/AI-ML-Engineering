from app.graph import graph

config = {
    "configurable":{
        "thread_id": "conversation-1"
    }
}

result = graph.invoke({
    "messages":[
        {
            "role": "user",
            "content":"Hello! my name is Alex"
        }
    ]
}
, config

)

graph.invoke({
    "messages":[{
        "role": "user",
        "content": "What is my name ? I like to code in python"
    }]
}, config)
for message in result["messages"]:
    print(message)