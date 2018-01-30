class Animal():
    def __init__(self, name, dangerous=False):
        self.dangerous = dangerous
        self.name = name

class Human():
    def is_dangerous(self, animal):
        if animal.dangerous:
            print('Animal {} is dangerous'.format(animal.name))
        else:
            print('Animal {} isn`t dangerous'.format(animal.name))

snake = Animal('Змея',dangerous=True)
dog = Animal('Собака',dangerous=False)
man = Human()
man.is_dangerous(snake)
man.is_dangerous(dog)