# uv run -m scripts.batchCreateAudio
from lib.supabase import supabase_client
from utils.generate11LabsAudio import generate_11labs_audio_bytes
from utils.uploadAudioFile import upload_audio_file
from utils.getVoice import get_voice

def fetch_default_phrases():
    response = supabase_client.table("phrases").select("*").eq("type", "default").limit(5).execute()
    return response.data

def batch_create_audio(voice_id: str, upsert: bool = False):
    voice = get_voice(voice_id)
    provider_voice_id = voice["provider_voice_id"]
    provider_model_id = voice["provider_model_id"]
    
    phrases = fetch_default_phrases()
    for phrase in phrases:
        print(f"Text: {phrase['text']}")
        print(f"Phrase ID: {phrase['phrase_id']}")
        print(f"Voice ID: {voice_id}")
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
        except Exception as e:
            print(f"Error generating audio for phrase {phrase['phrase_id']}: {e}")
            continue

if __name__ == "__main__":
    batch_create_audio("f8e9967a-b36c-4833-94e3-059644a28f84", upsert=True)