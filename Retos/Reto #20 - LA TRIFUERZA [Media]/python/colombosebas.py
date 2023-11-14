#Reto semanal 19

# ¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible!
#
# Crea un programa que dibuje una Trifuerza de "Zelda"
# formada por asteriscos.
# - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
# - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#
# Ejemplo: Trifuerza 2
#
#   *
#  ***
# *   *
#*** ***
# Ejemplo: Trifuerza 3
# creo que debería verse así
#     *
#    ***
#   *****
#  *     *
# ***   ***
#***** *****
# Ejemplo: Trifuerza 4
# creo que debería verse así
#       *
#      ***
#     *****
#    *******
#   *       *
#  ***     ***
# *****   *****
#******* *******
try:
    nivelTrifuerza = int(input('Ingrese el nivel trifuerza: '))
    altura = nivelTrifuerza * 2
    largocadena = altura
    recorrida = 1
    recorridaBase = 1
    while recorrida <= altura:
        cadena = ''
        espacios = altura - recorrida
        asteriscos = largocadena - espacios
        espacio = 1
        asterisco = 1
        while espacio <= espacios:
            cadena += ' '
            espacio += 1
        if recorrida <= nivelTrifuerza:
            while asterisco <= asteriscos:
                cadena += '*'
                asterisco += 1
        else:
            asteriscos = (recorridaBase * 2) - 1
            asterisco = 1
            while asterisco <= asteriscos:
                cadena += '*'
                asterisco += 1
            espacioMedio = (espacios * 2) + 1
            espacio = 1
            while espacio <= espacioMedio:
                cadena += ' '
                espacio += 1
            asteriscos = (recorridaBase * 2) - 1
            asterisco = 1
            while asterisco <= asteriscos:
                cadena += '*'
                asterisco += 1
            recorridaBase +=1
        print(cadena)
        recorrida +=1
        largocadena +=1
except ValueError:
    print('Debes ingresar un número entero!')
