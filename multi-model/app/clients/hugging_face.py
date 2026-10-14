from huggingface_hub import InferenceClient
from config import HF_TOKEN

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto",
)