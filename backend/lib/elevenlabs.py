# uv run -m lib.elevenlabs

from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os

load_dotenv()

elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')

elevenlabs_client = ElevenLabs(api_key=elevenlabs_api_key)

if __name__ == "__main__":
    voices = elevenlabs_client.voices.get_shared(featured=True,reader_app_enabled=True)
    print(voices)