from pathlib import Path

from app.clients.hugging_face import client

MODEL_NAME = "Wan-AI/Wan2.2-TI2V-5B"

def generate_video(prompt:str, output_path:Path | Path, )-> Path:
    video = client.text_to_video(prompt,
                                 model = MODEL_NAME,
                                 
                                 )

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(video)

    return output_path 

    