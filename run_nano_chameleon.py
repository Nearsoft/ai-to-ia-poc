"""
Run the NanoChameleon demo.
"""

from dotenv import load_dotenv
from src.core.metadata import Metadata
from src.core.orchestrator import Orchestrator

load_dotenv()

if __name__ == "__main__":
    prompt = {
        "question": (
            "Is the following statement about our solar system true or false?"
            " Jupiter's volume is more than ten times as large as Saturn's volume."
        ),
        "options": "(A) True (B) False"
    }

    # Create Metadata object
    metadata_object = Metadata(prompt_metadata.prompt).get_metadata(QUESTION, OPTIONS)
    orchestrator = Orchestrator(metadata_object)
