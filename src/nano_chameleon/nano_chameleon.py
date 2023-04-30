"""
The `NanoChameleon` module implements a tool to query LLMs and other ML models
for question answering.

Currently, it oly uses GPT-4, and only allows text input. Future versions will be 
multimodal, and will extend the set of tools the chameleon can use to include Bing Search,
and models from Hugging Face.
"""

import re
from typing import Dict, List
from src.nano_chameleon.tools.chatgpt import ChatGPT, GPTPrompts

class NanoChameleon:
    """
    Class that implements a tool to query LLMs and other ML models
    for question answering.

    Static Methods
    --------------
    _generate_payload:
        Params:
        user_prompt: str) -> Dict[str, object]`: Generates the initial
        payload the `NanoChameleon` will use to correctly answer the user's question.

    """

    @staticmethod
    def run(user_prompt: str) -> str:
        """
        Runs the NanoChameleon demo.

        Parameters
        ----------
        `user_prompt` (str): The user's input.
        """
        initial_payload = NanoChameleon._assemble_payload(user_prompt)
        print(f"\nInitial payload: {initial_payload}")

        print(NanoChameleon._run(initial_payload))

    @staticmethod
    def _assemble_payload(user_prompt: str) -> Dict[str, object]:
        """
        Assembles the initial payload the `NanoChameleon` will use to correctly
        answer the user's question.

        Parameters
        ----------
        `user_prompt` (str): The user's input.
        """
        payload = {}

        # Get the basics from the user's input.
        for line in user_prompt.splitlines():
            parts = line.split(":")

            parts[0].strip().lower()
            parts[1].strip()

            payload[parts[0]]: parts[1]

        # Add the `metadata` for the question and the `module_sequence` to run.
        payload['image'] = False  # Image handling will be added in a future release.
        payload['metadata'] = NanoChameleon._process_payload(payload, GPTPrompts.METADATA)
        payload['module_sequence'] = NanoChameleon._process_payload(payload, GPTPrompts.PLANNER)

        return payload

    @staticmethod
    def _process_payload(payload: str, tool: GPTPrompts) -> Dict[str, object]:
        """
        Uses the indicated `tool` to process the `prompt` using ChatGPT.

        Parameters
        ----------
        prompt :: (str): Prompt for the given tool, might be user input or might contain
            metadata as well.
        tool :: (GPTTools): The tool to use for processing the `prompt`.
        """
        gpt4 = ChatGPT(tool, payload)
        gpt4.run()


        return gpt4.parse()

    @staticmethod
    def _run(payload: Dict[str, object]) -> str:
        """
        Runs the NanoChameleon demo.

        Parameters
        ----------
        `payload` (Dict[str, object]): The payload to run.
        """
        for tool in payload["model_sequence"]:
            if tool != GPTPrompts.UNINPLEMENTED:
                gpt4.run(tool, payload)

                result = gpt4.parse()

        return result
        for module in payload['module_sequence']:
            module.run(payload)
            payload = module.parse()
