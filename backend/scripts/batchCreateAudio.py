# uv run -m scripts.batchCreateAudio
from lib.supabase import supabase_client
from utils.generateAudio import generate_audio_bytes
from utils.uploadAudioFile import upload_audio_file
import pprint

def fetch_default_phrases():
    response = supabase_client.table("phrases").select("*").eq("type", "default").limit(80).execute()
    return response.data

def batch_create_audio(voice_id: str, upsert: bool = False):
    phrases = fetch_default_phrases()
    for phrase in phrases:
        print(f"Text: {phrase['text']}")
        print(f"Phrase ID: {phrase['phrase_id']}")
        print(f"Voice ID: {voice_id}")
        try:
            audio_bytes = generate_audio_bytes(phrase["text"], voice_id)
            upload_audio_file(audio_bytes, phrase["phrase_id"], upsert)
        except Exception as e:
            print(f"Error generating audio for phrase {phrase['phrase_id']}: {e}")
            continue

if __name__ == "__main__":
    batch_create_audio("JBFqnCBsd6RMkjVDRZzb", upsert=True)