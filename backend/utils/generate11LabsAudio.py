# uv run -m utils.generate11LabsAudio
from lib.elevenlabs import elevenlabs_client
from utils.getVoice import get_voice
import base64
import os

def generate_11labs_audio_bytes(text: str, provider_voice_id: str, provider_model_id: str) -> bytes:
    audio_bytes = b""
    try:
        for chunk in elevenlabs_client.text_to_speech.convert(
            voice_id=provider_voice_id,
            output_format="mp3_44100_128",
            text=text,
            model_id=provider_model_id,
            previous_text="The word I'm going to say is"
        ):
            audio_bytes += chunk
        return audio_bytes
    except Exception as e:
        raise e
    
def generate_11labs_audio_bytes_v2(text: str, provider_voice_id: str, provider_model_id: str, previous_text: str = "The word I'm going to say is", next_text: str = ".") -> bytes:
    try:
        response = elevenlabs_client.text_to_speech.convert_with_timestamps(
            voice_id=provider_voice_id,
            output_format="mp3_44100_128",
            text=text,
            model_id=provider_model_id,
            previous_text=previous_text,
            next_text=next_text,
            voice_settings={
                "speed": 0.8,
                "stability": 1.0,
                "similarity_boost": 0.8,
                "style": 0.0
            }
        )
        audio_bytes = base64.b64decode(response.audio_base_64)
        return audio_bytes
    except Exception as e:
        raise e

def save_audio_to_file(audio_bytes: bytes, filename: str, path: str = "/Users/willnorris/Documents/Projects/aac/backend/files"):
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, filename)
    with open(filepath, "wb") as f:
        f.write(audio_bytes)
    return filepath

if __name__ == "__main__":
    voice_ids = ["d9ed509b-e830-4ca2-b7f2-21bbb5c9e54d", "f8e9967a-b36c-4833-94e3-059644a28f84", "b5c062a8-4a33-49f5-907b-6da259cd74d7"]
    # voice_ids = ["d9ed509b-e830-4ca2-b7f2-21bbb5c9e54d"]
    
    for voice_id in voice_ids:
        voice = get_voice(voice_id)
        provider_voice_id = voice["provider_voice_id"]
        provider_model_id = voice["provider_model_id"]

        test_words = ["I, me, my", "is, am, are", "go", "to", "not", "she", "he", "help", "Math", "School", "Work"]
        # test_words = ["go"]

        for word in test_words:

            audio_bytes = generate_11labs_audio_bytes_v2(
                text=word, 
                provider_voice_id=provider_voice_id,
                provider_model_id=provider_model_id
            )
            save_audio_to_file(audio_bytes, f"{word}.mp3", f"/Users/willnorris/Documents/Projects/aac/backend/files/v6/{voice_id}")