"""
Module responsible for executing the plan generated by the `PlanGenerator`
(`src.core.plan_generator`).
"""


from typing import Dict
from src.models.chatgpt import ChatGPT, GPTTools


class Orchestrator:
    """
    Class responsible for executing the generated plan by calling each of the
    models in the correct order, and returning the result.

    Static Methods
    --------------
    execute_plan(plan: Dict[str, object]) -> str
        Executes the plan and returns the result.

    _assemble_prompt(tool: GPTTools, plan: Dict[str, object]) -> str
        Assembles the prompt for the given tool.
    """

    @staticmethod
    def execute_plan(plan: Dict[str, object]) -> str:
        """Executes the plan and returns the result."""
        result = None

        for tool in plan["model_sequence"]:
            if tool != GPTTools.UNINPLEMENTED:
                prompt = Orchestrator._assemble_prompt(tool, plan, result)

                gpt4 = ChatGPT(tool)
                gpt4.execute(prompt)

                result = gpt4.parse()

        return result

    @staticmethod
    def _assemble_prompt(
        tool: GPTTools, plan: Dict[str, object], result: Dict[str, object]
    ) -> str:
        """Assembles the prompt for the given tool."""
        optional_responses = (
            f"Options: {plan['optional_responses']}\n"
            if plan["optional_responses"]
            else ""
        )

        if not result:
            prompt = (
                f"{plan['original_question']} \n {optional_responses}"
                f"Metadata: {plan['metadata']}\n"
            )
        else:
            prompt = result

        return f"{tool.value.PROMPT} \n + {prompt}"
