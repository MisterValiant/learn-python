'''
Enter weight
Choose between kg or lbs using K/k and L/l
Output conversion
'''

weight=float(input('Enter weight: '))
choice=input('(K)g or (L)bs: ').lower()

if (choice=='l'):
    print('Weight in kg: ' + str(weight/2.2046))
elif(choice=='k'):
    print('Weight in lbs: ' + str(weight*2.2046))
else:
    print('Wrong choice! Try again.')