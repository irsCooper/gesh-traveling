import requests
import json

async def get_auth_key():
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload = 'scope=GIGACHAT_API_PERS'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': 'cb9759e3-16a3-4c8f-8080-500ed5da0c33',
        'Authorization': 'Basic Y2I5NzU5ZTMtMTZhMy00YzhmLTgwODAtNTAwZWQ1ZGEwYzMzOmQ4MDkxOTU4LTczZmYtNDYwYy1iYWU4LWI3NmI5ZjA3YWRiMQ=='
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return json.loads(response.text)['access_token']