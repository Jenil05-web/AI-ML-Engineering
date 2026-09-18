from tools.db_tool import get_db_tools
from llm.model import llm


tools = get_db_tools(llm)

for tool in tools:
    print(tool.name)
    print(tool.description)
    print("-" * 50)