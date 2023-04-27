import os
import requests
import json
from core.metadata import Metadata
from core.orchestrator import Orchestrator
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    
    # Get metadata from prompt
    file_path = os.path.abspath('src/demos/prompt_metadata.py')
    with open(file_path, 'r') as f:
        prompt = f.read().split('prompt = """')[1].split('"""')[0]
    #TODO: call_chatgpt(prompt)
    #params=json.loads(generated_text[12:])
    #metadata_object = Metadata(**params)