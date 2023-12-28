def fizzbuzz(number)->int:
  for number in range (1,101):
    if number%3==0:
      print('fizz')
    elif number%5==0:
      print('buzz')
    elif number%3==0 and number%5==0:
      print('fizzbuzz')
    else:
      print(number)  

fizzbuzz(number=range)