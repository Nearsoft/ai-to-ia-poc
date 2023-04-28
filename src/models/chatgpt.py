"""Instantiation of the ChatGPT model."""
import os
import requests
from enum import Enum
from src.models.abstract_model import AbstractModel
from src.models.gpt_tools import prompt_metadata

class gpt_tools(Enum):
    """Enum for the roles of the model."""
    # PLANNER = prompt planner
    # knowledge_retrieval = "Knowledge Retrieval"
    # query_generator = "Query Generator"
    # solution_generator = "Solution Generator"
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
    tool = gpt_tools.METADATA

    def __init__(self, tool: gpt_tools):
        self.completions_url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY"),
            "Content-Type": "application/json",
        }
        self.result = None
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