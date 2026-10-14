from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

previous_response_id = None

while True:
    audio_path = input("Audio file path (or 'exit'): ").strip()

    if audio_path.lower() == "exit":
        break

    # Speech to Text :

    with open(audio_path,"rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model = "gpt-4o-mini-transcribe",
            file = audio_file
        )

        user_text = transcription.text
        print("You:", user_text)

        # Text -> AI response , linked to previous turn
        response = client.responses.create(
            model = "gpt-4o-mini",
            instructions="You are an helpful assistant. Please provide a concise and informative response to the user's query.",
            input = user_text,
            previous_response_id = previous_response_id
        )

        answer = response.output_text
        print("AI:", answer)

        previous_response_id = response.id

        # AI response -> Speech
        with client.audio.speech.with_streaming_response.create(
            model = "gpt-4o-mini-tts",
            voice = "marin",
            input = answer
        ) as speech_response:
            output_audio_path = "response_audio.wav"
            with open(output_audio_path, "wb") as audio_file:
                for chunk in speech_response.iter_bytes():
                    audio_file.write(chunk)

            print(f"AI response saved as '{output_audio_path}'.")