"""
PlanGenerator module. Does plan generation for the `Orchestrator`
(`src/core/orchestrator.py`).
"""

from typing import Dict
from src.core.metadata import Metadata
import json
from src.models.chatgpt import ChatGPT

class PlanGenerator:
    """
    Class to perform plan generation based upon available input and metadata.
    
    Attributes
    ----------
    metadata :: (Metadata): Metadata for the plan.
    plan :: (Dict[str, object]): Generated plan for the orchestrator to follow.
    """

    def __init__(self, metadata: Metadata):
        self.metadata = metadata
        self.plan = self._generate_plan()

    def get_metadata(self, prompt: str) -> Metadata:
        """
        Generates metadata based upon the user's input, by asking ChatGPT to parse it.
        """
        gpt4 = ChatGPT()
        gpt4.execute(prompt)
        generated_metadata = gpt4.parse()
        params = json.loads("{" + generated_metadata.split("{")[1])
        
        return Metadata(**params)
    
    def _generate_plan(self) -> Dict[str, object]:
        """Generates a plan for the model to follow."""
        plan = {
            "original_question": "", 
            "image": None,
            "optional_responses": [],
            "metadata": self.metadata,
            "model_sequence": []  # this is a List[AbstractModel->Model].
        }

        return plan

# TODO (jhernandez, kapioma): Should we add a `Plan` class?
