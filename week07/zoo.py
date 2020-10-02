class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        name = animal.__class__.__name__
        if name not in self.animals:
            self.animals.append(name)
        else:
            raise Exception(f'{self.name} already has {animal.name}')
        setattr(self, animal.__class__.__name__, animal)