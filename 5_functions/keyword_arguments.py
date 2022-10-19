def greet_user(fname, mname):
    print(f'Hi there {fname} {mname}!')
    print('Welcome aboard')

print('Start')
greet_user('Teesa', 'Devi')
print('Finish')

'''
With keyword argument position does not matter
'''
print('---Keyword arg---')
greet_user(mname='Singh', fname='Sarv ')

'''
- Use keyword args for multiple parameters to improve readability
- Always use first position arg before keyword arg if using both position and key arg
'''