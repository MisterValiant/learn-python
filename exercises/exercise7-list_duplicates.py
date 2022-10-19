'''
Write a program to remove the duplicates in a list
'''

numbers=[1,1,2,2,2,3,3,3,3]
uniques=[]

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)