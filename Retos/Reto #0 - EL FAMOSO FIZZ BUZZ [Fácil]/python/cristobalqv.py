for numero in range(1,101):
    if (numero % 3 == 0) and (numero % 5 == 0):     # ESTE ES EL CASO MAS PARTICULAR, HAY QUE TRABAJARLO PRIMERO
        print('fizz buzz')
    elif (numero % 3 == 0):
        print('fizz')
    elif numero % 5 == 0:
        print('buzz')
    else:
        print(numero)

