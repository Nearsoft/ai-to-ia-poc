"""
Abstract class for models. All models must inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import Dict

class AbstractModel(ABC):
    """
    Abstract class for models with a minimal set of attributes and methods that
    the `Orchestrator` (`src/core/orchestrator.py`) will expect to be available.

    Attributes
    ----------
    id :: (str): Unique, platfomr dependent identifier for the model.
    name :: (str): Human readable identifier for the model.
    platform :: (str): Origin platform for the model.

    Methods
    -------
    execute :: (None): Execute the model. Model dependent.
    parse :: (dict): Parse the results from model execution and return them.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "model_id")
            and callable(subclass.model_id)
            and hasattr(subclass, "name")
            and callable(subclass.name)
            and hasattr(subclass, "platform")
            and callable(subclass.platform)
            and hasattr(subclass, "tool")
            and callable(subclass.tool)
            and hasattr(subclass, "execute")
            and callable(subclass.execute)
            and hasattr(subclass, "parse")
            and callable(subclass.parse)
            or NotImplemented
        )

    @property
    @abstractmethod
    def model_id(self):
        """str: Unique, platform dependent identifier for the model."""
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self):
        """str: Human readable identifier for the model."""
        raise NotImplementedError

    @property
    @abstractmethod
    def platform(self):
        """str: Origin platform for the model."""
        raise NotImplementedError
    
    @property
    @abstractmethod
    def tool(self):
        """str: Role that the model should assume."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, prompt: str, result: Dict[str, object]):
        """
        Execute the model. Model dependent.

        Parameters
        ----------
        result :: (Dict[str, object]): Result from the previous model's execution.
        """
        raise NotImplementedError

    @abstractmethod
    def parse(self) -> Dict[str, object]:
        """
        Parse the result of the model execution and return a dictionary with
        the following structu‚re:

        {
            "output" (str): The output of the model execution.
            "metadata" (Dict): The metadata for the execution. Model dependent.
        }
        """
        raise NotImplementedError
