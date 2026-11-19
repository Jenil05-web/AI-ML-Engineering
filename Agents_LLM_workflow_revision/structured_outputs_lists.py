from typing import List
from pydantic import BaseModel , Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv

class TopicAnalysis(BaseModel):
    topic : str = Field(
        description="Name of the programming Language"
    )
    advantages : List[str] = Field( # here we used List[str], try to compare the syntax with previous one which we have written in first file ( structrued_outputs.py)
        description = "List of advantages"
    )
    disadvantages : List[str] = Field(
        description="List of disadvantages"
    )
    use_cases: List[str] = Field(
        description = "List of common use case"
    )

llm = ChatOpenAI(
        model = "gpt-4o-mini",
        temperature=0
    )

structured_llm = llm.with_structured_output(TopicAnalysis)
response = structured_llm.invoke("Analyze Python, Provide its advantages, disadvantages, and use cases.")
print(response)
print("\n Advantages")
print("\n Disadvantages")
print("\n use_cases")


