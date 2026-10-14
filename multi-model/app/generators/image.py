from pathlib import Path
from app.clients.hugging_face import client

MODEL_NAME = "black-forest-labs/FLUX.1-schnell"

def generate_image(prompt:str, output_path:str | Path)->Path:
    image =client.text_to_image(
        prompt,
        model = MODEL_NAME,
    )

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)

    return output_path
