from fastapi import FastAPI
from pydantic import BaseModel
from model import generate_response
# we have used the fastapi to connect the model.py file with the main.py file and to create a web interface for our chatbot.
app = FastAPI()
# promptrequest is premade class in fastapi which is used to define the structure of the request body that will be sent to the "/generate" endpoint. By defining this class, we can ensure that any incoming requests to the "/generate" endpoint will have a JSON body that matches this structure, and we can easily access the "prompt" field in our generate_text() function.
class PromptRequest(BaseModel): # PromptRequest is a class that inherits from BaseModel, which is a class provided by the Pydantic library. This class is used to define the structure of the request body that will be sent to the "/generate" endpoint. In this case, the PromptRequest class has a single field called "prompt" of type string. By defining this class, we can ensure that any incoming requests to the "/generate" endpoint will have a JSON body that matches this structure, and we can easily access the "prompt" field in our generate_text() function.
    # this creates a data model for the request body, which expects a JSON object with a "prompt" field of type string.
    prompt: str

@app.post("/generate")
def generate_text(request: PromptRequest): # this defines a POST endpoint at the URL "/generate". When a POST request is made to this endpoint with a JSON body that matches the PromptRequest model, the function generate_text() is called. Inside this function, we call the generate_response() function from the model.py file, passing the user's prompt as an argument. The generated response is then returned as a JSON object with a "response" field.
    response = generate_response(request.prompt)
    return {"response": response}


# FastAPI NOtes :

# @app.get("/") ""this is an endpoint that listens for GET requests at the root URL ("/"). When a GET request is made to this endpoint, the function hello_world() is called, which returns a JSON response with the message "Hello, World!".
# def hello_world():
#     return {"message": "Hello, World!"}

# similarly
# @app.get("/teacher") ""this is an endpoint that listens for GET requests at the "/teacher" URL. When a GET request is made to this endpoint, the function teacher() is called, which returns a JSON response with the message "Hello, Teacher!".
# now to run this code and to get the web interface we will write "uvicorn main:app --reload" in the terminal and then we can access the web interface at http://