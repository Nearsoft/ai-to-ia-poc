"""
PlanGenerator module. Does plan generation for the `Orchestrator`
(`src/core/orchestrator.py`).
"""

import re
from typing import Dict, List
from src.models.chatgpt import ChatGPT, GPTTools


class PlanGenerator:
    """
    Class to perform plan generation based upon available input and metadata.

    Static Methods
    --------------
    generate_plan(prompt: str) -> Dict[str, object]
        Generates a plan based upon the user's input, by asking ChatGPT to parse it.

    _process_prompt(prompt: str, tool: GPTTools) -> Dict[str, object]
        Generates metadata based upon the user's input, by asking ChatGPT to parse it.
    """

    @staticmethod
    def generate_plan(prompt: str) -> Dict[str, object]:
        """
        Generates a plan for the model to follow.

        Parameters
        ----------
        prompt :: (str): The user's input.
        """
        metadata = PlanGenerator._process_prompt(prompt, GPTTools.METADATA)
        optional_responses = PlanGenerator._get_options_from_prompt(prompt)
        model_sequence = PlanGenerator._process_prompt(
            prompt + f"\nMetadata: {metadata}\n", GPTTools.PLANNER
        )

        return {
            "original_question": prompt,
            "image": None,  # Image handling will be added in a future release.
            "optional_responses": optional_responses,
            "metadata": metadata,
            "model_sequence": model_sequence,
        }

    @staticmethod
    def _process_prompt(prompt: str, tool: GPTTools) -> Dict[str, object]:
        """
        Uses the indicated `tool` to process the `prompt` using ChatGPT.

        Parameters
        ----------
        prompt :: (str): Prompt for the given tool, might be user input or might contain
            metadata as well.
        tool :: (GPTTools): The tool to use for processing the `prompt`.
        """
        gpt4 = ChatGPT(tool)
        gpt4.execute(prompt)

        return gpt4.parse()

    @staticmethod
    def _get_options_from_prompt(prompt: str) -> List[str]:
        """
        Gets the options from the `prompt`. Returns `[]` if there are no options.

        Parameters
        ----------
        prompt :: (str): User inputed prompt.
        """
        options: List[str] = []

        # Find and split the options from the rest of the prompt.
        options_string = prompt.split("Options: ")

        if len(options_string) > 1:
            options_list: List[str] = re.split(
                r"\(([a-z]|[A-Z]|[0-9])\)", options_string[1]
            )[1:]

            # We take the options_list and pair each option with its answer
            for i in range(0, len(options_list), 2):
                options.append(
                    options_list[i].strip() + " " + options_list[i + 1].strip()
                )

        return options
