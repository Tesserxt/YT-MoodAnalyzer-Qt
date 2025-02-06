import requests
import pprint
import json
from db import Database


class HuggingFaceInferenceApi:
    
    def __init__(self):
        self.__api_key = None
    
    def set_api_key(self, key):
        self.__api_key = key

    def get_api_key(self):
        return self.__api_key

    def run_analysis(self, data, existing=None):
        '''
        existing=None: replace None with file_name to get existing data
        '''

        if existing:
            try:
                with open(existing, "r") as file:
                    return json.load(file)
            except FileNotFoundError:
                return {"error": f"File '{existing}' not found"}
            except json.JSONDecodeError:
                return {"error": f"Invalid JSON format in '{existing}'"}

        else:
            API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
            headers = {"Authorization": f"Bearer {self.get_api_key()}"}
            payload = data
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

    