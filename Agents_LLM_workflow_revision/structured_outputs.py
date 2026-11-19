from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

# Define the expected output structure

class TopicInfo(BaseModel):
    topic: str = Field(description="Name of the topic")
    description: str = Field(
    description = "Brief explaination of the topic" )
    difficulty:str = Field(
        description="Difficulty level : Beginner, Intermediate, or Advanced"
    )

    """Field() allows us to provide additional information and rules about that field.
    First write topic :str , description :str etc. to every other state or structrue then if you will look closely we have added 
    Field(), inside field we will write another condition or additional information
    """

    # Initialize the LLM

llm = ChatOpenAI(
        model = "gpt-4o-mini",
        temperature = 0
 )

    # Bind the structured output schema
structured_llm = llm.with_structured_output(TopicInfo)

# Ask the LLM a question
response = structured_llm.invoke(
    "Explain Langgraph and mention its difficulty level"
)

print(response)
print("\nTopic:", response.topic)
print("Description:", response.description)
print("Difficulty:", response.difficulty)

