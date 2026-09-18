from langchain.agents import create_agent

from llm.model import llm

from tools.db_tool import get_db_tools

tools = get_db_tools(llm)

agent = create_agent(
    model= llm,
    tools = tools,
    system_prompt="""
You are a company database assistant.

Use the SQL database tools to answer questions about:
- customers
- products
- employees
- orders

Always use the database for factual company data.
Do not invent database information.
"""

)