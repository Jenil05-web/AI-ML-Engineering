from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
 # Convert Speech to text 
with open("OSR_us_000_0010_8k.wav", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model = "gpt-4o-mini-transcribe",
        file = audio_file
    )

    user_text = transcription.text
    print("You:", user_text)

    # Generate an AI response

    response = client.responses.create(
        model = "gpt-4o-mini",
        input = user_text
    )

    answer = response.output_text
    print("AI:", answer)

    # 3. Convert the response to speech

    with client.audio.speech.with_streaming_response.create(
        model = "gpt-4o-mini-tts",
        voice = "marin",
        input = answer
    ) as speech_response:
        with open("response_audio.wav", "wb") as audio_file:
            for chunk in speech_response.iter_bytes():
                audio_file.write(chunk)

