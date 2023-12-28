# Reto 0

def fizz_buzz():
    for i in range(1, 101):
        fizz = i % 3 == 0
        buzz = i % 5 == 0
        if fizz and buzz: print("fizzbuzz")
        elif fizz: print("fizz")
        elif buzz: print("buzz")
        else: print(i)

fizz_buzz()
