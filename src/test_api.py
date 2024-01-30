# Test local endpoints in container
import requests
import os
import logging
from urllib.parse import urljoin
from dotenv import load_dotenv
load_dotenv()

URL = "http://localhost:8000/"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = os.environ.get("MODEL")

logger = logging.getLogger(__name__)



def test_health():
    response = requests.get(urljoin(URL, "health"))
    print(f"\n/health response:\n{response}\n")
    assert response.status_code == 200



def test_models():
    response = requests.get(urljoin(URL, "v1/models"))
    print(f"\n/v1/models response:\n{response.json()}\n")
    assert response.status_code == 200
    assert response.json()["object"] == "list"
    assert response.json()["data"][0]["id"] == MODEL


def test_completions():
    headers = {
        "Content-Type": "application/json",
        "Authorization": OPENAI_API_KEY
    }

    data = {
        "model": MODEL,
        "prompt": "Say this is a test",
        "max_tokens": 7,
        "temperature": 0
    }

    response = requests.post(urljoin(URL, "v1/completions"), headers=headers, json=data)
    print(f"\n/v1/completions response:\n{response.json()}\n")
    
    assert response.status_code == 200
    

def test_chat_completions():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }

    response = requests.post(urljoin(URL, "v1/chat/completions"), headers=headers, json=data)
    print(f"\n/v1/chat/completions response:\n{response.json()}\n")

    assert response.status_code == 200
