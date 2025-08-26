# uv run -m utils.uploadAudioFile
from lib.supabase import supabase_client

def upload_audio_file(audio_bytes: bytes, phrase_id: str, upsert: bool = False):
    filename = f"{phrase_id}.mp3"
    path = filename
    
    try:
        supabase_client.storage.from_("audio").upload(
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
    
def get_bytes_from_file(file_path: str) -> bytes:
    with open(file_path, "rb") as file_handle:
        return file_handle.read()
    
if __name__ == "__main__":
    audio_bytes = get_bytes_from_file("/Users/willnorris/Documents/Projects/aac/backend/files/test.mp3")
    upload_audio_file(audio_bytes, "test")