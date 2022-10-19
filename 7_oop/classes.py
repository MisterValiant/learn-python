'''
define a class using class keyword
name is capitalise (naming convention) - PascalCase
'''

class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')

'''
An object is an instance of a class
- Classes are blueprints
- Objects are instances based on that blueprint
'''

point1=Point()

# Display
point1.draw()

# Creating objects
point1.x=10
print(point1.x)

'''
point2=Point()
print(point2.x) wont work as this is a completely different new instance
'''