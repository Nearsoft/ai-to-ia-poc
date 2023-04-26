import abc

class AbstractModel(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'plataform') and 
                callable(subclass.plataform) and 
                hasattr(subclass, 'name') and 
                callable(subclass.name) and 
                hasattr(subclass, 'id') and 
                callable(subclass.id) and 
                hasattr(subclass, 'initialize') and 
                callable(subclass.initialize) and 
                hasattr(subclass, 'execute') and 
                callable(subclass.execute) and 
                hasattr(subclass, 'parse') and 
                callable(subclass.parse) or 
                NotImplemented)
        
    @property
    @abc.abstractmethod
    def plataform(self):
        raise NotImplementedError
    
    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplementedError
    
    @property
    @abc.abstractmethod
    def id(self):
        raise NotImplementedError

    @abc.abstractmethod
    def initialize(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def execute(self, result):
        raise NotImplementedError
    
    @abc.abstractmethod
    def parse(self):
        raise NotImplementedError
    


