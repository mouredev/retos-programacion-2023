for valueNumber in range(1, 101):
  valueString = ''

  if valueNumber % 3 == 0:
    valueString += 'Fizz'

  if valueNumber % 5 == 0:
    valueString += 'Buzz'

  print(valueString or valueNumber)
