import abc

class AbstractModel(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        raise NotImplementedError

