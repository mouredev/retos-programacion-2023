numbers = list(range(1,101))

for n in numbers:
  if (n % 3 == 0) and (n % 5 == 0):
    print('Fizzbuzz \n')
  elif(n % 3 == 0):
    print("Fizz \n")
  elif(n % 5 == 0):
    print("Buzz \n")
  else:
    print(n, "\n")