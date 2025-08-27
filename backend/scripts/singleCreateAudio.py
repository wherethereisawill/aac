# uv run -m scripts.singleCreateAudio
from lib.supabase import supabase_client
from utils.generate11LabsAudio import generate_11labs_audio_bytes
from utils.uploadAudioFile import upload_audio_file
from utils.getVoice import get_voice
import pprint

def fetch_phrase(phrase_id: str):
    response = supabase_client.table("phrases").select("*").eq("phrase_id", phrase_id).execute()
    return response.data[0]

def single_create_audio(phrase_id: str, voice_id: str, upsert: bool = False):
    voice = get_voice(voice_id)
    provider_voice_id = voice["provider_voice_id"]
    provider_model_id = voice["provider_model_id"]
    
    phrase = fetch_phrase(phrase_id)
    text = phrase["text"]
    phrase_id = phrase["phrase_id"]
    try:
            audio_bytes = generate_11labs_audio_bytes(
                text=phrase["text"], 
                provider_voice_id=provider_voice_id,
                provider_model_id=provider_model_id
            )
            
            upload_audio_file(
                audio_bytes=audio_bytes,
                phrase_id=phrase["phrase_id"],
                voice_id=voice_id,
                upsert=upsert
            )
            pprint.pprint(f"Audio successfully uploaded")
            pprint.pprint(f"Text: {text}")
            pprint.pprint(f"Phrase ID: {phrase_id}")
            pprint.pprint(f"Voice ID: {voice_id}")
    except Exception as e:
        pprint.pprint(f"Error generating audio for phrase {phrase['phrase_id']}: {e}")

if __name__ == "__main__":
    single_create_audio("4afab421-e2f5-4fed-87f3-3afa339569da", "f8e9967a-b36c-4833-94e3-059644a28f84", upsert=True)