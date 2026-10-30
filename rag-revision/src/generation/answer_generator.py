from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def generate_answer(query, documents):
    llm = ChatOpenAI(
        model = "gpt-4o-mini",
        temperature=0
    )

    context = "\n".join(
    
    )

    prompt = ChatPromptTemplate.from_template(
        """
    Answer the question using only the provided context.

    If the answer is not available in the context,
    say that you don't know.

    Context:
    {context}

    Question:
    {question}"""
    )

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": query
    })

    return response.content

