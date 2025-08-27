# uv run -m utils.getVoice
from lib.supabase import supabase_client
import pprint

def get_voice(voice_id: str):
    response = supabase_client.table("voices").select("*").eq("voice_id", voice_id).execute()
    provider_model_id = response.data[0]["provider_model_id"]
    provider = response.data[0]["provider"]
    provider_voice_id = response.data[0]["provider_voice_id"]
    return {
        "provider_model_id": provider_model_id,
        "provider": provider,
        "provider_voice_id": provider_voice_id
    }

def get_voices():
    response = supabase_client.table("voices").select("*").execute()
    return response.data

if __name__ == "__main__":
    voice = get_voice("d9ed509b-e830-4ca2-b7f2-21bbb5c9e54d")
    pprint.pprint(voice)