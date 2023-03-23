# Reto 0 - El Famoso Fizz Buzz
for i in range(1,101):
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    else:
        print(i)
