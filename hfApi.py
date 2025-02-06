import requests
import pprint

from db import Database


class HuggingFaceInferenceApi:
    
    def __init__(self):
        self.__api_key = None
    
    def set_api_key(self, key):
        self.__api_key = key

    def get_api_key(self):
        return self.__api_key

    def run_analysis(self):
        API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
        headers = {"Authorization": f"Bearer {self.get_api_key()}"}
        d = Database()
        payload = d.get_filter_data()
        response = requests.post(API_URL, headers=headers, json=payload)
        print(response.json())

    