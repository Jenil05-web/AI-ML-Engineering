"""Long Term Memory for Agents"""

from langgraph.store.memory import InMemoryStore
from dotenv import load_dotenv

load_dotenv()

store = InMemoryStore() # -> This creates an in-memory checkpointer that saves graph state between executions ( Long term memory for agents)

user_namespace = ("users", "user_123", "memories")

# Save Information to the store
store.put(
    user_namespace,
    "user_profile",
    {
        "name":"Alex",
        "programming_language":"Python",
        "goal":"Become an AI Engineer"
    }
)
 
memory = store.get(
    user_namespace,
    "user_profile"
)

print(memory.value)

thread_a  = "conversation 1"
thread_b = "conversation 2"

memory_a  = store.get(user_namespace, "user_profile")
memory_b = store.get(user_namespace, "user_profile")

print("Thread A:", memory_a.value)
print("Thread B:", memory_b.value)



