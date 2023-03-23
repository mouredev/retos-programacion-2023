def es_multiplo(numero, multiplo):
    return numero % multiplo == 0


for numero in range(1, 101):
    if es_multiplo(numero, 3) and es_multiplo(numero, 5):
        print("fizzbuzz")
    elif es_multiplo(numero, 3):
        print("fizz")
    elif es_multiplo(numero, 5):
        print("buzz")
    else:
        print(numero)
