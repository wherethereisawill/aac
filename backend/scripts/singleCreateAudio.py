# uv run -m scripts.singleCreateAudio
from lib.supabase import supabase_client
from utils.generate11LabsAudio import generate_11labs_audio_bytes
from utils.uploadAudioFile import upload_audio_file
import pprint

def fetch_phrase(phrase_id: str):
    response = supabase_client.table("phrases").select("*").eq("phrase_id", phrase_id).execute()
    return response.data[0]

def single_create_audio(phrase_id: str, voice_id: str, upsert: bool = False):
    phrase = fetch_phrase(phrase_id)
    pprint.pprint(f"Text: {phrase['text']}")
    pprint.pprint(f"Phrase ID: {phrase['phrase_id']}")
    pprint.pprint(f"Voice ID: {voice_id}")
    try:
        audio_bytes = generate_11labs_audio_bytes(phrase["text"], voice_id)
        upload_audio_file(audio_bytes, phrase["phrase_id"], upsert)
    except Exception as e:
        pprint.pprint(f"Error generating audio for phrase {phrase['phrase_id']}: {e}")

if __name__ == "__main__":
    single_create_audio("160ad03e-238e-4f92-b301-6e9e30c20e12", "JBFqnCBsd6RMkjVDRZzb", upsert=True)