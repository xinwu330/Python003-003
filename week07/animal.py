from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, name, category, body_type, personality):
        pass