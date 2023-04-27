import os
import requests
from abstract_model import AbstractModel


class ChatGTP(AbstractModel):
    def __init__(self):
        self.model_id = "chatgpt"
        self.name = "ChatGPT"
        self.platform = "openai"

        self.reqUrl = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY"),
            "Content-Type": "application/json",
        }

    def execute(self, prompt, result=None):
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"content": prompt, "role": "user"}],
        }
        response = requests.post(self.reqUrl, headers=self.headers, json=data)
        if response.status_code == 200:
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"].strip()

        else:
            print("Error: ", response.status_code, response.text)
            raise Exception("Error: ", response.status_code, response.text)

    def parse(self, result):
        return result
