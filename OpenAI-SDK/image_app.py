import base64 # it is used to convert the image bytes to text 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

with open("image.png", "rb") as file:
    image_data = base64.b64encode(file.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Describe this image and identify the main objects."
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{image_data}"
                }
            ]
        }
    ]
)

print(response.output_text)

# This file is basically used to send an image to the OpenAI API and get a description of the image along with identification of the main objects present in it.
#    The image is read from a file, converted to base64 format, and then sent as part of the request to the API. The response is printed out, which contains the description and object identification.