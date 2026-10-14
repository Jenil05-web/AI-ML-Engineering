from app.clients.hugging_face import client
from app.schemas.content import ContentPlan

MODEL_NAME = "openai/gpt-oss-20b"

def create_content_plan(topic:str)-> ContentPlan :
    prompt = f"""
Create  a content plan for the topic : {topic}
Return only JSON with this exact this fields :
{{
"description": "A short description of the concept",
    "image_prompt": "A detailed prompt for an image generation model",
    "video_prompt": "A detailed prompt for a video generation model"
}}"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content": prompt}],
        max_tokens = 500,
    )

    content  = response.choices[0].message.content

    return ContentPlan.model_validate_json(content)

