"""
Metadata module. Used to store metadata for use by the `PlanGenerator`
(`src/core/plan_generator.py`).
"""

class Metadata:
    """
    Metadata class. Contains metadata from the user's input.
    
    Attributes
    ----------
    input_type :: (str): The type of input the user provided.
    answer_type :: (str): The type of answer the user is looking for.
    domain :: (str): The domain of the question.
    skill :: (str): The skill required to answer the question.
    difficulty :: (str): The difficulty of the question.
    """

    # TODO (jhernandez): Change the types above/below to enums.
    def __init__(
            self,
            input_type: str,
            answer_type:str,
            domain: str,
            skill: str,
            difficulty: str
    ):
        self.input_type = input_type
        self.answer_type = answer_type
        self.domain = domain
        self.skill = skill
        self.difficulty = difficulty
