# Reto 0: El Famoso Fizz Buzz

for i in range(1,101):
    mod3 = i % 3
    mod5 = i % 5
    if mod3 == 0 and mod5 == 0: 
        print("fizzbuzz")
    elif mod3 == 0:
        print("fizz")
    elif mod5 == 0:
        print("buzz")
    else:
        print(i)
