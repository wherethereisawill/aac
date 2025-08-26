# uv run -m lib.supabase

import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_SECRET_KEY")
supabase_client: Client = create_client(url, key)

if __name__ == "__main__":
    print(supabase_client.storage.from_("audio").get_public_url("test.mp3"))