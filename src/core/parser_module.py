import json
from models.chatgtp import ChatGTP
from core.metadata import Metadata


class Parser:
    def __init__(self, prompt):
        self.prompt = prompt

    def get_metadata(self):
        generated_metadata = ChatGTP().execute(self.prompt)
        params = json.loads("{" + generated_metadata.split("{")[1])
        metadata_object = Metadata(**params)
        return metadata_object
