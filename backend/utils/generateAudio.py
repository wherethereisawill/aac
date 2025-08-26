# uv run -m utils.generateAudio
from lib.elevenlabs import elevenlabs_client
import os

def generate_audio_bytes(text: str, voice_id: str) -> bytes:
    audio_bytes = b""
    try:
        for chunk in elevenlabs_client.text_to_speech.convert(
            voice_id=voice_id,
            output_format="mp3_44100_128",
            text=text,
            model_id="eleven_multilingual_v2"
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
    audio_bytes = generate_audio_bytes("Repair (flip over)", "JBFqnCBsd6RMkjVDRZzb")
    save_audio_to_file(audio_bytes, "test.mp3")