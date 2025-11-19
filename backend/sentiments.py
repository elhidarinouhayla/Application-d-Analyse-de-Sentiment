
import os
import requests
from config import HF_API_URL, HF_API_KEY 

if not HF_API_URL:
    raise ValueError("hadak li maytsmach makhedamch")


API_URL = "https://router.huggingface.co/hf-inference/models/nlptown/bert-base-multilingual-uncased-sentiment"

headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
    }


def get_sentiment(text):
    
    payload = {input: text}

    # def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


text = get_sentiment("i loooove manal")
print(text)    

    