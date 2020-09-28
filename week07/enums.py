from enum import Enum

class Category(Enum):
    carnivore = '食肉'
    herbivore = '食草'

class BodyType(Enum):
    small = 1
    medium = 2
    large = 3

class Personality(Enum):
    docile = 1
    violent = 2