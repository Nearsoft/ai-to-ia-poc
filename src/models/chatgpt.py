"""Instantiation of the ChatGPT model."""
import os
from enum import Enum

import requests

from src.models.abstract_model import AbstractModel
from src.models.gpt_tools import prompt_metadata

class GPTTools(Enum):
    """Enum for model's roles."""
    # PLANNER = prompt_prompt planner
    # KNOWLEDGE_RETRIEVAL = prompt_knowledge_retrieval
    # QUERY_GENERATOR = prompt_query_generator
    # SOLUTION_GENERATOR = prompt_solution_enerator
    METADATA = prompt_metadata

class ChatGPT(AbstractModel):
    """
    Instantiantion of the ChatGPT model. Connects to the OpenAI API for chat 
    completion.

    Attributes
    ----------
    model_id :: (str): The model id.
    name :: (str): The name of the model.
    platform :: (str): The platform the model is on.
    completions_url :: (str): The request url for the model.
    headers :: (Dict[str, str]): The headers for the request.

    Methods
    -------
    execute(prompt, result=None)
        Executes the model with the given prompt and result.
    parse(result)
        Parses the result from the model.
    """

    completions_url = "https://api.openai.com/v1/chat/completions"
    model_id = "chat_completions"
    name = "ChatGPT"
    platform = "openai"
    result = None
    tool = None

    def __init__(self, tool: GPTTools):
        self.headers = {
            "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY"),
            "Content-Type": "application/json",
        }
        self.tool = tool
        self.base_prompt = self.tool.value.prompt

    def execute(self, prompt, result=None):
        """
        Executes the model with the given prompt and result.

        Parameters
        ----------
        prompt :: (str): The prompt to execute the model with.
        result :: (Dict[str, object]): The result from the previous model's execution.
        """

        data = {
            "model": "gpt-4",
            "messages": [{"content": self.base_prompt+ "\n" + prompt, "role": "user"}],
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