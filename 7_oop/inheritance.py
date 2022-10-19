class Dog:
    def walk(self):
        print('walk')

# What if we want same code in class CAT?
# DRY principle - Dont repeat yourself

#(REPEARED -> Create a parent class an inherit)
#  class Cat:
#     def walk(self):
#         print('walk')

class Mammal:
    def walk(self):
        print('walk')

# Inherit

class Dog(Mammal):
    def bark(self):
        print('bark')

# Pass is used here as python does not like leaving classes blank

class Cat(Mammal):
    pass #pass are used to mean nothing

dog1= Dog()
dog1.walk()
dog1.bark()

cat1=Cat()
cat1.walk()