from animal import Animal

class Cat(Animal):
    
    meow = 'meowww...meoww'

    def __init__(self, name, category, body_type, personality):
        self.name = name
        self.category = category
        self.body_type = body_type
        self.personality = personality
        self.is_ferocious = (body_type == '中等' or body_type == '大型') and category == '食肉' and personality == '凶猛'
        self.is_pet = not self.is_ferocious


    