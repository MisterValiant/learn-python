'''
Errors are handles with try and except

Some exceptions:
ValueError - catch exceptions for int
ZeroDivisionError - cannot be zero
'''

try:
    age=int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')

try:
    divisor=int(input('Enter a divisor: '))
    number=1/divisor
    print(number)
except ZeroDivisionError:
    print('Divisor cannot be zero')