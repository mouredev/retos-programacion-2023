rango = range(0,100)

for numero in rango:
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 5 == 0 :
        print("buzz")
    elif numero % 3 == 0:
        print('fizz')
    else:
        print(numero)