import json
import requests

url = "http://localhost:11434/api/chat"

payload = {
    "model": "enterprise-assistant",
    "messages": [
        {"role": "system", "content": "You are a concise enterprise assistant."},
        {"role": "user", "content": "What is our primary directive?"},
    ],
    "stream": False,
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print("API Response Success!\n")
    print(data["message"]["content"])
else:
    print(f"Error: {response.status_code} - {response.text}")