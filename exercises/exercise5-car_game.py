'''
A car game that accepts case-insensitive commands
help - shows lists of commands
start
stop
quit
other strings do not work

Use while loop only
'''

command='stop'

while command!='quit':
    previous=command
    command=input('>').lower()

    if (command==previous ):
        print(f'Are you a spammer? Vehicle status: {command}')

    elif (command=='help'):
        print('start - to start the car\nstop - to stop the car\nquit - to exit')
    
    elif command=='start':
        print('Car started.. Ready to go!')
    
    elif command=='stop':
        print('Car stopped')
    
    elif command=='quit':
        print('Exit program')
        break
   
    else:
        print('I don\'t understand that...')

'''
triple quote can also be used to print multiline
'''