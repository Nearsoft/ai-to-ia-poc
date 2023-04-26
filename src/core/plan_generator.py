
from metadata import Metadata

class PlanGenerator:
    def __init__(self, metadata):
        self.metadata = metadata
        self.plan = self.generate_plan()

    def generate_plan(self):
        plan = {
            "original_question": "", 
            "image": None,
            "optional_responses": [],
            "metadata": self.metadata,
            "model_sequence": []
        }
        return plan