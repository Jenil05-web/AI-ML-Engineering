from typing import Literal
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv

class CustomerQuery(BaseModel):
    category: Literal[
        "Billing", 
        "Technical",
        "General"
    ] = Field(
        description="Category of the customer query"
    )

    urgency: Literal[
        "High",
        "Medium",
        "Low"
    ] = Field(
        description="Urgency of the query"
    )

    explaination : str = Field(
        description="Explaination of the query"
    )

llm = ChatOpenAI(
        model = "gpt-4o-mini",
        temperature = 0

    )

structured_llm = llm.with_structured_output(CustomerQuery)
response = structured_llm.invoke(
    "My payment was deducted twice. Please help me get a refund."
)
print(response)

print("Category:", response.category)
print("Urgency:", response.urgency)
print("Explanation:", response.explanation)
