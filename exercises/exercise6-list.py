'''Find the largest number in a list'''

numbers=[1,4,6,2,3]
highest=-999

for item in numbers:
    if item>highest:
        highest=item

print(f'Largest number in the list is {highest}')