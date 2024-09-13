from fastapi import FastAPI, Request
from pydantic import BaseModel
from src.auth_key import get_auth_key
import requests
import json


import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/generate_story")
async def generate_story(input_data: InputData):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    key = await get_auth_key()

    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": f'Запомни - ты писатель. Сейчас я расскажу тебе короткое описание, а ты превращаешь его в увлекательную историю от первого лица длинной 1000 символов. Ответ на мой запрос ты сразу начинаешь с  повествования истории. Вот моя история: {input_data.text}'
            }
        ],
        "stream": False,
        "repetition_penalty": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {key}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    story = json.loads(response.text)['choices'][0]['message']['content']
    return {"story": story}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

