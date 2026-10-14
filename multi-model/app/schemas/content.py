from pydantic import BaseModel

class ContentPlan(BaseModel):
    description : str
    image_prompt : str
    video_prompt: str

    