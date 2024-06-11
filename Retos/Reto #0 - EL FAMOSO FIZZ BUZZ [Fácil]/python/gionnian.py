def fizz_buzz(start: int, end:int) -> None:
  for num in range(start, end + 1):
    if (num % 3 == 0) and (num % 5 == 0):
      print("fizzbuzz")
    elif num % 3 == 0:
      print("fizz")
    elif num % 5 == 0:
      print("buzz")
    else:
      print(num)

fizz_buzz(1, 100)