class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print('My name is {}...'.format(self.name))
        print('My friend is {}...'.format(friend))


p = Person('Bob', 'Male')
p('Alice')