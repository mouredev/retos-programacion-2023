def exercise_1_solution():
  for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
      print("fizzbuzz")
    if number % 3 == 0:
      print("fizz")
    if number % 5 == 0:
      print("buzz")
    else:
      print(number)

if __main__ == "__name__":
  exercise_1_solution()
