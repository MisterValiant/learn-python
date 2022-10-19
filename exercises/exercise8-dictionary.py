'''Map numbers to text equivalent using a dictionary'''

phone_number=input('Enter phone numnber: ')

conversion={
    0:'Zero',
    1:'One',
    2:'Two',
    3:'Three',
    4:'Four',
    5:'Five',
    6:'Six',
    7:'Seven',
    8:'Eight',
    9:'Nine'
}

output=''

for item in phone_number:
    output+=conversion.get(int(item), "!") + ' '

print(output)

'''
Learning outcome:
can read each char in a string with a for loop
'''