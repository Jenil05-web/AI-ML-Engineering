import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

prompt = input("Describe the image you want to generate: ")

response = client.responses.create(
    model = "gpt-4o-mini",
    input = f"Generate an image of: {prompt}",
    tools = [
        {
            "type": "image_generation",
            "model": "gpt-image-1-mini"
        }
    ]
)

for output in response.output:
    if output.type=="image_generation_call":
        image_data = base64.b64decode(output.result)

        with open("generated_image.png", "wb") as file:
            file.write(image_data)

            print("Image generated and saved as 'generated_image.png'.")
            break

    else:
        print("No image generated. Please try again with a different prompt.")


    