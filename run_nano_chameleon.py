"""
Run the NanoChameleon demo.
"""
import os
from dotenv import load_dotenv
from src.core.plan_generator import PlanGenerator
from src.core.orchestrator import Orchestrator

load_dotenv()

def get_prompt():
    """
    Load test prompt from file.
    """
    file_path = os.path.abspath("src/demos/prompt_metadata.py")
    with open(file_path, "r", encoding='UTF-8') as f:
        prompt = f.read().split('prompt = """')[1].split('"""')[0]
    return prompt

if __name__ == "__main__":

    #Create Metadata object
    prompt_from_file = get_prompt()
    metadata_object = PlanGenerator(metadata=None).get_metadata(prompt_from_file)
    orchestrator = Orchestrator(metadata_object)
