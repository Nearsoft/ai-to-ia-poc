"""
Run the NanoChameleon demo.
"""

from dotenv import load_dotenv
from src.core.plan_generator import PlanGenerator
from src.core.orchestrator import Orchestrator

load_dotenv()

if __name__ == "__main__":
    PROMPT = (
        "Question: What is Jupiter's volume in cubic kilometers?\n"
        "Options: (A) 1,431,281,810,739,360 cubic kilometers"
        "  (B) 2,039,471,207,872,154 cubic kilometers"
    )

    plan = PlanGenerator(PROMPT).plan
    orchestrator = Orchestrator(plan)
