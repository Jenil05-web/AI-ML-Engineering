from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

with open("OSR_us_000_0010_8k.wav", "rb") as audio_file:
    transcription = client.audio.transcriptions.create( # This is used for audio transcription. It takes an audio file as input and returns the transcribed text.
        model = "gpt-4o-mini-transcribe",
        file = audio_file
    )

    print("Transcription:", transcription.text)