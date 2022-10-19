message=input('>')
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

print(output)

'''
Learning outcome:
- split returns a list of words split with the defined char/separator
- use get to read dictionary to return a default value, as done above
if word is not found in dictionary, word is displayed as it is.
'''