"""Instantiation of the ChatGPT model."""

import json
import os
from enum import Enum
from typing import Any
import requests

from src.models.abstract_model import AbstractModel
from src.models.gpt_tools import (
    prompt_knowledge_retrieval,
    prompt_metadata,
    prompt_planner,
    prompt_solution_generator,
)


class GPTTools(Enum):
    """Enum for model's roles."""

    METADATA = prompt_metadata
    PLANNER = prompt_planner
    KNOWLEDGE_RETRIEVAL = prompt_knowledge_retrieval
    SOLUTION_GENERATOR = prompt_solution_generator
    UNINPLEMENTED = None


class ChatGPT(AbstractModel):
    """
    Instantiantion of the ChatGPT model. Connects to the OpenAI API for chat
    completion.

    Attributes
    ----------
    completions_url :: (str): The request url for the model.
    headers :: (Dict[str, str]): The headers for the request.
    model_id :: (str): The model id.
    name :: (str): The name of the model.
    platform :: (str): The platform the model is on.
    result :: (Dict[str, object]): The result of procesing a prompt with the model.
    tool :: (GPTTools): The tool to use for the model.

    Methods
    -------
    execute(prompt: str, result: Optional[Dict[str, object]]=None) -> None: Executes
        the model with the given `prompt` and  previous (if nany) `result`.

    parse() -> Any: Parses the result from the model, and returns the parsed result.
    """

    completions_url = "https://api.openai.com/v1/chat/completions"
    model_id = "chat_completions"
    name = "ChatGPT"
    platform = "openai"
    result = None
    tool = None

    def __init__(self, tool: GPTTools):
        """
        Constructor for the ChatGPT model.

        Parameters
        ----------
        tool :: (GPTTools): The tool to use for the model.
        """
        self.headers = {
            "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY"),
            "Content-Type": "application/json",
        }
        self.tool = tool
        self.result = None

    def execute(self, prompt: str):
        """
        Executes the model with the given prompt and result.

        Parameters
        ----------
        prompt :: (str): The prompt to execute the model with.
        result :: (Dict[str, object]): The result from the previous model's execution.
        """
        full_prompt = self.tool.value.PROMPT + "\n" + prompt
        data = {
            "model": "gpt-4",
            "messages": [{"content": full_prompt, "role": "user"}],
        }

        response = requests.post(
            self.completions_url, json=data, headers=self.headers, timeout=60
        )
        if response.status_code == 200:
            response_json = response.json()
            self.result = response_json

        print(
            f"\nResponse:\n HTTP status code: {response.status_code}\n Response: {response.json()}"
        )
        response.raise_for_status()

    def parse(self) -> Any:
        """Parses the result from the model."""
        content = self.result["choices"][0]["message"]["content"]

        match self.tool:
            case GPTTools.KNOWLEDGE_RETRIEVAL:
                # List starts right after the first '-'character.
                return content[content.find("-") :]
            case GPTTools.METADATA:
                return json.loads(content)["Metadata"]
            case GPTTools.PLANNER:
                return [
                    ChatGPT._map_module_to_tool(mn)
                    for mn in json.loads(content)["module_sequence"]
                ]
            case GPTTools.SOLUTION_GENERATOR:
                solution = content.split("The answer is ")
                self.result = f"The answer is: {solution[1]}"
                return self.result
            case _:
                return self.result

    @staticmethod
    def _map_module_to_tool(module_name: str) -> GPTTools:
        """Maps a module to its corresponding tool."""
        match module_name:
            case "Knowledge_Retrieval":
                return GPTTools.KNOWLEDGE_RETRIEVAL
            case "Solution_Generator":
                return GPTTools.SOLUTION_GENERATOR
            case _:
                return GPTTools.UNINPLEMENTED
