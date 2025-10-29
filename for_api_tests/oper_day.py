import uuid
import pprint
import requests
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('TOKEN')


def test_get_oper_day():
    response = requests.get(
        url='http://10.50.50.24:9975/1.0.0/get-oper-day',
        headers={
            'Accept': 'application/json',
            'Accept-Language': 'en',
            'requestId': f'{uuid.uuid4()}',
            'Authorization': f'Bearer {TOKEN}'
        }
    )
    assert response.status_code == 200
    pprint.pprint(response.headers)
    pprint.pprint(response.json())
    pprint.pprint(response.text)
