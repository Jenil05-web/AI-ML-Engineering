from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app = FastAPI( # basically we created or set up an FastAPI application instance and we have provided some metadata for the API such as the title, version, and description. This information can be useful for documentation purposes and helps users understand what the API is about when they access it.
    # for example it is similar to restapi whrere we write , const app = express() and then we set up our routes and endpoints. Similarly, here we are creating an instance of FastAPI which will allow us to define our API routes and handle incoming requests. 
    title="Langhchain ServerAPI",
    version="1.0",
    description = "This is a simple API for Langchain ServerAPI"
)

add_routes( # here add_routes is of langserve library which is used to add routes to our FastAPI application. It takes three arguments: the FastAPI app instance, the chain of operations that we want to execute when a request is made to this route, and the path for the route. In this case, we are adding a route at "/openai" that will execute the chain consisting of the prompt and the ChatOpenAI language model when a request is made to this endpoint.
    app, # the FastAPI app instance that we created earlier. This is where we will be adding our API routes.
    ChatOpenAI(),
    path="/openai"

)

model = ChatOpenAI() # define model that we want to use for our API. In this case, we are using the ChatOpenAI model from the langchain_openai library, which allows us to interact with OpenAI's language models.

llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write a essay about topic {topic} in 100 words")
prompt2 = ChatPromptTemplate.from_template("Write a poem about topic {topic} for a 5 year old")

add_routes( # this is where langchain and langserve combine to create API endpoints for our application.
# The add_routes function is used to define the routes for our FastAPI application, and it takes three arguments: the FastAPI app instance, the chain of operations that we want to execute when a request is made to this route, and the path for the route.
    # In this case, we are adding two routes: one at "/essay" that will execute the chain consisting of prompt1 and the ChatOpenAI model, and another at "/poem" that will execute the chain consisting of prompt2 and the Ollama language model. This allows us to create API endpoints that can generate essays and poems based on user input.
    app,
    prompt1 | model,
    path="/essay"

)
add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)

if __name__ == "__main__": # this means that if we run this script directly (instead of importing it as a module), we will start the FastAPI server using uvicorn. The uvicorn.run() function is used to run the FastAPI application, and we specify the host and port where the server will be accessible. In this case, the server will be running on localhost at port 8000, which means we can access our API endpoints at http://localhost:8000/openai, http://localhost:8000/essay, and http://localhost:8000/poem.
    uvicorn.run(app,host="localhost",port=8000) # port 8000 default port defined for fastapi application.


# The Server (api.py)(File 1): You built the "Brain." By using FastAPI and LangServe, you told your computer: "Listen on Port 8000. If anyone sends a POST request to /essay/invoke, take their topic, run it through my LangChain, and send back an essay."

#The Client.py (File 2): You built the "Face." You used Streamlit to get the user's input, but instead of doing the AI work itself, it acts as a messenger. It packages that input into a JSON "envelope" and sends it to the URL you created in File 1.

#The Connection: The second file consumes the service that the first file provides.