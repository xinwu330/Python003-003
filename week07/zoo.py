class Zoo:
    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        setattr(self, animal.__class__.__name__, animal)