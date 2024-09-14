import requests
import json

url = "http://localhost:8000/generate_tags"
data = {"text": "я ездила в тайгу"}

response = requests.post(url, json=data)

if response.status_code == 200:
    story = response.json()
    print(story)
else:
    print(f"Ошибка: {response.status_code} - {response.text}")
