import requests
import json

url = "http://localhost:8000/generate_story"
data = {"text": "я ездил на розу хутор"}

response = requests.post(url, json=data)

if response.status_code == 200:
    story = response.json()['story']
    print(story)
else:
    print(f"Ошибка: {response.status_code} - {response.text}")
