# uv run -m utils.uploadVoicePreview
from lib.supabase import supabase_client
from utils.uploadAudioFile import get_bytes_from_file

def upload_voice_preview(audio_bytes: bytes, voice_id: str, upsert: bool = False):
    path = f"{voice_id}.mp3"
    
    try:
        supabase_client.storage.from_("voice_previews").upload(
            file=audio_bytes,
            path=path,
            file_options={
                "cache-control": "3600",
                "content-type": "audio/mpeg",
                "upsert": "true" if upsert else "false",
            }
        )
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    audio_bytes = get_bytes_from_file("/Users/willnorris/Documents/Projects/aac/backend/files/v6/b5c062a8-4a33-49f5-907b-6da259cd74d7/go.mp3")
    upload_voice_preview(
        audio_bytes=audio_bytes,
        voice_id="test_voice_id",
        upsert=True
    )