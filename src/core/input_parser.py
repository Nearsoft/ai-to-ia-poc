"""Module for parsing the user's input."""

import json
from src.core.metadata import Metadata
from src.models.chatgpt import ChatGPT, gpt_tools

class Parser:
    """
    Class to parse the user's input and generate metadata.
    """
    def __init__(self, prompt):
        self.prompt = prompt

    def get_metadata(self):
        """
        Generates metadata based upon the user's input, by asking ChatGPT to parse it.
        """
        gpt4 = ChatGPT(gpt_tools.METADATA)
        gpt4.execute(self.prompt)
        generated_metadata = gpt4.parse()

        params = json.loads(generated_metadata)['Metadata']
        return Metadata(**params)
