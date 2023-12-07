
def palabra_100_puntos():
    print('''
Reglas: Para ganar debe ingresar una palabra y que la suma de sus
letras sea de 100 puntos. La letra 'a' equivale a 1 punto y la 'z' 
a 27 puntos.No distingue mayusculas de minusculas! ¡A divertirse!
''')
    palabra = input("Ingrese una palabra: ")
    play = True
    while play:
        puntos = 0
        for letra in palabra:
            punto = ord(letra.upper()) - 64
            if punto in range(1,28):
                puntos +=  punto
        if puntos == 100:
            print("¡Has logrado escribir una palabra de 100 puntos!")
            print("¡Felicitaciones!")
            break
        else:
            print(f'Tu palabra sumó {puntos} puntos')
            print('¿Deseas intentarlo nuevamente? (S/N)')
            if input()[0].upper() == "S":
                palabra = input("Ingrese una palabra: ")
            else:
                print("¡Gracias por participar!")
                break

palabra_100_puntos()
