# uv run -m utils.generate11LabsAudio
from lib.elevenlabs import elevenlabs_client
from utils.getVoice import get_voice
import os

def generate_11labs_audio_bytes(text: str, provider_voice_id: str, provider_model_id: str) -> bytes:
    audio_bytes = b""
    try:
        for chunk in elevenlabs_client.text_to_speech.convert(
            voice_id=provider_voice_id,
            output_format="mp3_44100_128",
            text=text,
            model_id=provider_model_id
        ):
            audio_bytes += chunk
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
    voice = get_voice("d9ed509b-e830-4ca2-b7f2-21bbb5c9e54d")
    provider_voice_id = voice["provider_voice_id"]
    provider_model_id = voice["provider_model_id"]

    audio_bytes = generate_11labs_audio_bytes(
        text="This is a test", 
        provider_voice_id=provider_voice_id,
        provider_model_id=provider_model_id
    )
    save_audio_to_file(audio_bytes, "test.mp3")