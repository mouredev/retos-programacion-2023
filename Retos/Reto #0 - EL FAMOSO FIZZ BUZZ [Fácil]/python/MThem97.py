
r=range(1,101)
for number in r:
    if number % 5==0 and number % 3==0:
           print('fizzbuzz')
    if number % 3==0:
           print('fizz')
    if number % 5==0:
           print('buzz')
    else:
           print(number)




