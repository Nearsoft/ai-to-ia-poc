"""
Run the NanoChameleon demo.
"""
import os
from dotenv import load_dotenv
from src.core.plan_generator import PlanGenerator
from src.core.orchestrator import Orchestrator
from src.demos.prompt_metadata import get_prompt

load_dotenv()

if __name__ == "__main__":
    question = "Is the following statement about our solar system true or false? Jupiter's volume is more than ten times as large as Saturn's volume."
    options = "(A) true (B) false"
    metadata = '{"input_type": "text", "answer_type": "multiple_choice", "domain": "technology", "skill": "Compare", "difficulty": "1"}'
 
    #Create Metadata object
    prompt_from_file = get_prompt(question, options, metadata)
    metadata_object = PlanGenerator(metadata=None).get_metadata(prompt_from_file)

    orchestrator = Orchestrator(metadata_object)
