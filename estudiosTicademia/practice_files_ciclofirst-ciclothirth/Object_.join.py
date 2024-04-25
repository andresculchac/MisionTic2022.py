numlist = ['1', '2', '3', '4', '5', '6', '7']
separator = '->'
numListContinuation = ['8', '9', '10', '11', '12', '13']
stringlist = 'i am humble'
stringempty = ' '

print('List before Join():', numlist)
print('List after Join():' , separator.join(numlist))
print(stringlist.join(separator))
print(stringempty.join(numlist))


# .join with lists
words = ['Hello','can','we', 'play', 'today', '!']

sentence = ' '.join(words)
print(sentence)
for i in words:
    print(i)