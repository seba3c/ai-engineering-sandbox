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


def load_api_keys():
    load_dotenv(override=True)
    openai_api_key = os.getenv('OPENAI_API_KEY')
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
    google_api_key = os.getenv('GOOGLE_API_KEY')
    deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
    groq_api_key = os.getenv('GROQ_API_KEY')
    grok_api_key = os.getenv('GROK_API_KEY')
    openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

    if openai_api_key:
        print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
    else:
        print("OpenAI API Key not set")
        
    if anthropic_api_key:
        print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
    else:
        print("Anthropic API Key not set (and this is optional)")

    if google_api_key:
        print(f"Google API Key exists and begins {google_api_key[:2]}")
    else:
        print("Google API Key not set (and this is optional)")

    if deepseek_api_key:
        print(f"DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
    else:
        print("DeepSeek API Key not set (and this is optional)")

    if groq_api_key:
        print(f"Groq API Key exists and begins {groq_api_key[:4]}")
    else:
        print("Groq API Key not set (and this is optional)")

    if grok_api_key:
        print(f"Grok API Key exists and begins {grok_api_key[:4]}")
    else:
        print("Grok API Key not set (and this is optional)")

    if openrouter_api_key:
        print(f"OpenRouter API Key exists and begins {openrouter_api_key[:3]}")
    else:
        print("OpenRouter API Key not set (and this is optional)")

