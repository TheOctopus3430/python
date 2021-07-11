class Animal(object):
    # 定义类变量
    __localtion = 'Asia'
    # 定义初始化函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 定义类方法
    @classmethod
    def set_localtion(cls, localtion):
        cls.__localtion = localtion
    # 定义类方法
    @classmethod
    def get_localtion(cls):
        return cls.__localtion


print(Animal.get_localtion())  # ==> Asia
Animal.set_localtion('Afica')
print(Animal.get_localtion())  # ==> Afric
