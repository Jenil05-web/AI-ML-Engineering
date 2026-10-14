
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

previous_response_id = None


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=user_input,
        previous_response_id=previous_response_id
    )
    

    print("AI:", response.output_text)
    previous_response_id = response.id