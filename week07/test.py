from animal import *
from zoo import *
from dog import *
from cat import *

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')


    # Test
    # print(have_cat)

    # dog1 = Dog('大黄狗 1', '食肉', '中', '温顺')
    # z.add_animal(dog1)
    # have_dog = hasattr(z, 'Dog')
    # print(have_dog)

    # z.add_animal(cat1)

    # print(z.__dict__)
    
    # cat2 = Cat('大花猫 2', '食肉', '小', '温顺')
    # z.add_animal(cat2)
    
    # print(z.__dict__)