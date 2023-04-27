import os
from core.parser_module import Parser
from dotenv import load_dotenv

load_dotenv()

def get_prompt():
    file_path = os.path.abspath("src/demos/prompt_metadata.py")
    with open(file_path, "r") as f:
        prompt = f.read().split('prompt = """')[1].split('"""')[0]
    return prompt

if __name__ == "__main__":

    #Create Metadata object
    prompt = get_prompt()
    metadata_object = Parser(prompt).get_metadata()

    #TODO: Create Orchestrator object with metadata_object
    #orchestrator = Orchestrator(metadata_object)
