class Person:
    def __init__(self, name):
        self.name=name

    def talk(self):
        print(f'Hi, I am {self.name}')

john=Person('John')
print(john.name)
john.talk()

print('---New person---')
bob=Person('Bob')
bob.talk()