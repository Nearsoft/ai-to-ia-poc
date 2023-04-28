"""
Run the NanoChameleon demo.
"""
import json
from dotenv import load_dotenv
from src.core.input_parser import Parser
from src.core.orchestrator import Orchestrator
from src.models.gpt_tools import prompt_metadata

load_dotenv()

if __name__ == "__main__":

    #Create Metadata object
        
    metadata_object = Parser(prompt_metadata.prompt).get_metadata()

    orchestrator = Orchestrator(metadata_object)
