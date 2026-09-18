from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit

from database.connection import engine


db = SQLDatabase(engine)


def get_db_tools(llm):
    toolkit = SQLDatabaseToolkit(
        db=db,
        llm=llm,
    )

    return toolkit.get_tools()

"""To connect the external database with our agent or system we will wrap it into an tool so by that way we can expose it to our agent, 
and it can use our database to answer the questions. We will use SQLDatabaseToolkit to wrap our database into a tool and then we will expose it to our agent.
This logic will be used everytime whenever we are working or building something that has to be connected with our agent """
