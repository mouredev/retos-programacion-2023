word_or_number = ''
for i in range(1, 101):
    if (i % 3 == 0):
        word_or_number = 'fizzbuzz' if i % 5 == 0 else 'fizz'
    elif (i % 5 == 0):
        word_or_number = 'buzz'
    else:
        word_or_number = i
    print(word_or_number)
    