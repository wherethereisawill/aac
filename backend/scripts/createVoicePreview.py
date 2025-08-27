# uv run -m scripts.createVoicePreview

from utils.generate11LabsAudio import generate_11labs_audio_bytes_v2
from utils.getVoice import get_voice, get_voices
from utils.uploadVoicePreview import upload_voice_preview

def create_voice_preview(voice_id: str, preview_text: str):
    try:
        voice = get_voice(voice_id)
        provider_voice_id = voice["provider_voice_id"]
        provider_model_id = voice["provider_model_id"]
        audio_bytes = generate_11labs_audio_bytes_v2(
            text=preview_text, 
            provider_voice_id=provider_voice_id,
            provider_model_id=provider_model_id
        )
        upload_voice_preview(
            audio_bytes=audio_bytes,
            voice_id=voice_id,
            upsert=True
        )
    except Exception as e:
        print(f"Error generating audio for voice {voice_id}: {e}")

if __name__ == "__main__":
    voices = get_voices()
    for voice in voices:
        voice_id = voice["voice_id"]
        name = voice["name"]
        create_voice_preview(voice_id, f"Hey, my name is {name}. What do you think of my voice?")