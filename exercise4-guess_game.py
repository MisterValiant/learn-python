counter=0

while counter<3:
    guess=int(input('Guess: '))

    if (guess==9):
        print('You win')
        break
    else:
        print(str(2-counter)+' attempts left') 

    counter+=1
else:
    print('You lose')
    
'''
Can you else with while-loop
'''