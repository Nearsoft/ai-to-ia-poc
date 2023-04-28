"""
Metadata module. Used to store metadata for use by the `PlanGenerator`
(`src/core/plan_generator.py`).
"""

import json

from src.models.chatgpt import ChatGPT, GPTTools
from src.models.gpt_tools import prompt_metadata

class Metadata:
    """
    Metadata class. Contains metadata from the user's input.
    
    Attributes
    ----------
    input_type :: (str): The type of input the user provided.
    answer_type :: (str): The type of answer the user is looking for.
    domain :: (str): The domain of the question.
    skill :: (str): The skill required to answer the question.
    difficulty :: (str): The difficulty of the question.

    Methods
    -------
    get_multichoice_metadata(prompt: str) -> 'Metadata':
        Generates metadata based upon the user's input, by asking ChatGPT to parse it.
    """

    def __init__(
            self,
            input_type: str,
            answer_type:str,
            domain: str,
            skill: str,
            difficulty: str
    ):
        self.input_type = input_type
        self.answer_type = answer_type
        self.domain = domain
        self.skill = skill
        self.difficulty = difficulty

    def get_multichoice_metadata(self, prompt: str) -> 'Metadata':
        """
        Generates metadata based upon the user's input, by asking ChatGPT to parse it.
        """
        gpt4 = ChatGPT(GPTTools.METADATA)
        gpt4.execute(prompt)
        generated_metadata = gpt4.parse()
        params = json.loads("{" + generated_metadata.split("{")[1])
        
        return Metadata(**params)