from app.config import HF_TOKEN
import os
import requests

def get_sentiment(input_text):
    API_URL = "https://router.huggingface.co/hf-inference/models/nlptown/bert-base-multilingual-uncased-sentiment"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": input,
    }) 
    return output






    # try:
    #     response = requests.post(API_URL, headers=headers, json={"inputs": input_text}, timeout=10)
    #     response.raise_for_status()
    #     output = response.json()
        
    #     if isinstance(output, dict) and "error" in output:
    #         return [{"label": "error", "score": 0}]
    #     return output

    # except requests.RequestException:
    #     return [{"label": "error", "score": 0}]
    

  