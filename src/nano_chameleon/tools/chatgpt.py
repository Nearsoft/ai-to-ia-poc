"""Instantiation of the ChatGPT model."""

import json
import os
from enum import Enum
from typing import Dict
import requests

from src.nano_chameleon.tools.abstract_model import AbstractModel
from src.nano_chameleon.tools.gpt_prompts import (
    prompt_knowledge_retrieval,
    prompt_metadata,
    prompt_planner,
    prompt_solution_generator,
)


COMPLETIONS_URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY"),
    "Content-Type": "application/json",
}
MODEL_ID = "chat_completions"


class GPTPrompts(Enum):
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
    run(prompt: str, payload: Dict[str, object]) -> : Executes
        the model with the given `prompt` and  previous (if nany) `result`.

    parse() -> Any: Parses the result from the model, and returns the parsed result.
    """

    @staticmethod
    def run(payload: Dict[str, object], tool: GPTPrompts) -> None:
        """
        Runs GPT-4 with the given payload and tool.

        Parameters
        ----------
        `payload`: (Dict[str, object]): The prompt to execute the model with.
        `tool`: (GPTPrompts): Tool to use.
        """
        data = {
            "model": "gpt-4",
            "messages": [{"content": tool.value.assemble_prompt(payload), "role": "user"}],
        }

        response = requests.post(COMPLETIONS_URL, json=data, headers=HEADERS, timeout=15)
        if response.status_code == 200:
            response_json = response.json()
            result = response_json

            return ChatGPT.parse(result, tool)

        print(
            f"\nResponse:\n HTTP status code: {response.status_code}\n Response: {response.json()}"
        )
        response.raise_for_status()

    def parse(self, result: str) -> Dict[str, object]:
        """Parses the result from the model."""
        content = result["choices"][0]["message"]["content"]

        match self.tool:
            case GPTPrompts.KNOWLEDGE_RETRIEVAL:
                # List starts right after the first '-'character.
                return content[content.find("-") :]
            case GPTPrompts.METADATA:
                return json.loads(content)["Metadata"]
            case GPTPrompts.PLANNER:
                return [
                    ChatGPT._map_module_to_tool(mn)
                    for mn in json.loads(content)["module_sequence"]
                ]
            case GPTPrompts.SOLUTION_GENERATOR:
                return json.loads(content)["Answer"]
            case _:
                return result

    @staticmethod
    def _map_module_to_tool(module_name: str) -> GPTPrompts:
        """Maps a module to its corresponding tool."""
        match module_name:
            case "Knowledge_Retrieval":
                return GPTPrompts.KNOWLEDGE_RETRIEVAL
            case "Solution_Generator":
                return GPTPrompts.SOLUTION_GENERATOR
            case _:
                return GPTPrompts.UNINPLEMENTED
