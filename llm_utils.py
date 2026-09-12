import os
from dotenv import load_dotenv
from openai import OpenAI


def load_api_key(key_name="OPENAI_API_KEY"):
    load_dotenv(override=True)
    api_key = os.getenv(key_name)
    if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
        print("API key looks good so far")
    else:
        print("There might be a problem with your API key? Please visit the troubleshooting notebook!")
    return api_key


def get_llm_client(api_key=None, base_url=None):
    client = OpenAI(api_key=api_key, base_url=base_url)
    return client
