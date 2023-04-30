"""
Abstract class for models. All models must inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional


class AbstractModel(ABC):
    """
    Abstract class for models with a minimal set of attributes and methods that
    the `Orchestrator` (`src.core.orchestrator`) will expect to be available.

    Attributes
    ----------
    name :: (str): The name of the model.
    platform :: (str): The platform the model is on.

    Methods
    -------
    run(prompt: str, result: Optional[Dict[str, object]]=None) -> None: Executes
        the model with the given `prompt` and  previous (if nany) `result`.

    parse() -> Dict[str, object]: Parses the result from the model, and returns the
        parsed result.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "name")
            and callable(subclass.name)
            and hasattr(subclass, "platform")
            and callable(subclass.platform)
            and hasattr(subclass, "run")
            and callable(subclass.run)
            and hasattr(subclass, "parse")
            and callable(subclass.parse)
            or NotImplemented
        )

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

    @staticmethod
    @abstractmethod
    def run(payload: Dict[str, object] = None):
        """
        Run the model. Model dependent.

        Parameters
        ----------
        payload :: (Dict[str, object]): Payload to run the model with.
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def parse(result) -> Dict[str, object]:
        """
        Parse the result of the models run and return the parsed result.
        Model dependent.

        Parameters
        ----------
        result :: (Dict[str, object]): Payload to run the model with.
        """
        raise NotImplementedError
