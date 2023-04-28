"""
Metadata module. Used to store metadata for use by the `PlanGenerator`
(`src/core/plan_generator.py`).
"""

import json

from src.models.chatgpt import ChatGPT, GPTTools

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

    input_type = None
    answer_type = None
    domain = None
    skill = None
    difficulty = None

    @staticmethod
    def get_metadata(prompt: str) -> 'Metadata':
        """
        Generates metadata based upon the user's input, by asking ChatGPT to parse it.
        """
        gpt4 = ChatGPT(GPTTools.METADATA)
        gpt4.execute(prompt)
        generated_metadata = gpt4.parse()
        params = json.loads("{" + generated_metadata.split("{")[1])

        return Metadata._build_metadata(**params)

    @staticmethod
    def _build_metadata(
            input_type: str,
            answer_type:str,
            domain: str,
            skill: str,
            difficulty: str
    ):
        metadata = Metadata()
        metadata.input_type = input_type
        metadata.answer_type = answer_type
        metadata.domain = domain
        metadata.skill = skill
        metadata.difficulty = difficulty

        return metadata
