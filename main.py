from fastapi import FastAPI, Request, Body      
from fastapi.responses import HTMLResponse      
from fastapi.staticfiles import StaticFiles      
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from src.auth_key import get_auth_key
import requests
import json


import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/generate_tags")
async def generate_tags(input_data: InputData):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    key = await get_auth_key()
    story = await generate_story(input_data.text)

    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": f'Запомни, ты отлично умеешь выделять суть из текста. Вот моя история: {story}. Выдели из неё ключевые слова - это должен быть набор существительных, оформи их как хештеги, НАПРИМЕР это должно выглядеть так: \n\n#Горы, #Люди и тому подобное.   обязательно! Минимум 10 штук.'
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

    tags = json.loads(response.text)['choices'][0]['message']['content']
    return {"story": story, "tags": tags}




async def generate_story(text:str):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    key = await get_auth_key()

    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": f'Запомни - ты писатель. Сейчас я расскажу тебе короткое описание, а ты превращаешь его в увлекательную историю от первого лица длинной 1000 символов. Вот моя история: {text}.  Ответ на мой вопрос ты начинаешь сразу с истории, не нужно представляться и говорить что ты писатель!'
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
    print('\n' + story)
    return story











templates = Jinja2Templates(directory="templates")
class InputData(BaseModel):
    text: str

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
def submit(data: InputData):
    response_text = f"You entered: {data.text}"
    return {"response": response_text}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

