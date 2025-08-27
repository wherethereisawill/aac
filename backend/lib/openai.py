# uv run -m lib.openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_client = OpenAI()

if __name__ == "__main__":
    print(openai_client.models.list())