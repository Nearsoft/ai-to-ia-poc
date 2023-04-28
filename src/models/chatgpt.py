"""Instantiation of the ChatGPT model."""
import os
import requests
from src.models.abstract_model import AbstractModel

class ChatGPT(AbstractModel):
    """
    Instantiantion of the ChatGPT model. Connects to the OpenAI API for chat 
    completion.

    Attributes
    ----------
    model_id :: (str): The model id.
    name :: (str): The name of the model.
    platform :: (str): The platform the model is on.
    reqUrl :: (str): The request url for the model.
    headers :: (Dict[str, str]): The headers for the request.

    Methods
    -------
    execute(prompt, result=None)
        Executes the model with the given prompt and result.
    parse(result)
        Parses the result from the model.
    """

    model_id = "chat_completions"
    name = "ChatGPT"
    platform = "openai"

    def __init__(self):
        self.completions_url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY"),
            "Content-Type": "application/json",
        }
        self.result = None

    def execute(self, prompt, result=None):
        """
        Executes the model with the given prompt and result.

        Parameters
        ----------
        prompt :: (str): The prompt to execute the model with.
        result :: (Dict[str, object]): The result from the previous model's execution.
        """
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"content": prompt, "role": "user"}],
        }
        response = requests.post(self.completions_url, json=data, headers=self.headers, timeout=15)
        if response.status_code == 200:
            response_json = response.json()
            self.result = response_json["choices"][0]["message"]["content"].strip()

        
        print(f"Response:\n HTTP status code: {response.status_code}\n Response text: {response.text}")

        response.raise_for_status()

    def parse(self):
        """Parses the result from the model."""
        return self.result