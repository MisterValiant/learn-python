'''
As a rule of thumb, a function should not:
1. recieve input directly ie using input
2. output data directly ie using output

to make it reusable.
'''

def emoji_converter(message):
    words=message.split(' ')

    emojis={
    ':)':'😃',
    ':(':'☹️',
    ':\'(':'😭',
    '<3':'❤️',
    ':*':'😘'
    }

    output=''

    for word in words:
        output+=emojis.get(word, word)+' '
    
    return output

message=input('>')
print(emoji_converter(message))