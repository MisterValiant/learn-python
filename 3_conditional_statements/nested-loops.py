'''Drawing an F with nested if statements'''

numbers=[5,2,5,2,2]

for item in numbers:
    print('x'*item)

# Using inner for-loop
print('---using inner for-loop---')

for i in numbers:
    output=''
    for j in range(i):
     output+='x'
    print(output)

'''
use range() for number of iterations in a for-loop
'''