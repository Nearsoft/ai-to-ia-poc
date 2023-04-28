"""
PlanGenerator module. Does plan generation for the `Orchestrator`
(`src/core/orchestrator.py`).
"""

from typing import Dict
from src.core.metadata import Metadata
# from src.models.chatgpt import ChatGPT, GPTTools
# from src.models.gpt_tools import prompt_plan_generator

class PlanGenerator:
    """
    Class to perform plan generation based upon available input and metadata.
    
    Attributes
    ----------
    plan :: (Dict[str, object]): Generated plan for the orchestrator to follow.
    """

    def __init__(self, metadata: Metadata):
        self.plan = self._generate_plan(metadata)

    def _generate_plan(self, metadata: Metadata) -> Dict[str, object]:
        """Generates a plan for the model to follow."""
        plan = {
            "original_question": "", 
            "image": None,
            "optional_responses": [],
            "metadata": metadata,
            "model_sequence": []  # this is a List[AbstractModel->Model].
        }

        return plan

# TODO (jhernandez, kapioma): Should we add a `Plan` class?
