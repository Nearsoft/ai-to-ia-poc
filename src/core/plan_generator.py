"""
PlanGenerator module. Does plan generation for the `Orchestrator`
(`src/core/orchestrator.py`).
"""

from typing import Dict
from src.models.chatgpt import ChatGPT, GPTTools


class PlanGenerator:
    """
    Class to perform plan generation based upon available input and metadata.

    Attributes
    ----------
    orchestrator_package :: (Dict[str, object]): Data package for the `Orchestrator`
      (`src/core/orchestrator.py), with the original prompt from the user, metadata
      of said prompt, and a list of tools to use to generate the answer.

    Methods
    -------
    _get_metadata(prompt) -> Dict[str, object]
        Generates metadata based upon the user's input, by asking ChatGPT to parse it.

    _get_plan(prompt) -> Dict[str, object]
        Generates a plan based upon the user's input, by asking ChatGPT to parse it.
    """

    def __init__(self, prompt: str):
        self.orchestrator_package = self._generate_orchestrator_package(prompt)

    @staticmethod
    def _process_prompt(prompt: str, tool: GPTTools) -> Dict[str, object]:
        """
        Uses the indicated `tool` to process the `prompt` using ChatGPT.
        """
        gpt4 = ChatGPT(tool)
        gpt4.execute(prompt)

        return gpt4.parse()

    def _generate_orchestrator_package(self, prompt: str) -> Dict[str, object]:
        """Generates a plan for the model to follow."""
        plan = {
            "original_question": prompt,
            "image": None,
            "optional_responses": [],
            "metadata": PlanGenerator._process_prompt(prompt, GPTTools.METADATA),
            "model_sequence": PlanGenerator._process_prompt(prompt, GPTTools.PLANNER),
        }

        return plan
