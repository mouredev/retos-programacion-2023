# 
# La última semana de 2021 comenzamos la actividad de retos de programación,
# con la intención de resolver un ejercicio cada semana para mejorar
# nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
# 
# Crea un programa que calcule los puntos de una palabra.
# - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
#   español de 27 letras, la A vale 1 y la Z 27.
# - El programa muestra el valor de los puntos de cada palabra introducida.
# - El programa finaliza si logras introducir una palabra de 100 puntos.
# - Puedes usar la terminal para interactuar con el usuario y solicitarle
#   cada palabra.
# 

def calcular_puntos(palabra):
    puntos = 0
    dicionario_letras = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
        "K": 11, "L": 12, "M": 13, "N": 14, "Ñ": 15, "O": 16, "P": 17, "Q": 18, "R": 19,
        "S": 20, "T": 21, "U": 22, "V": 23, "W": 24, "X": 25, "Y": 26, "Z": 27
    }

    for l in palabra.upper():
        puntos += dicionario_letras[l]

    return puntos

def juegar():
    puntos = 0

    while puntos != 100:
        puntos = calcular_puntos(input("Escribe una palabra:\n"))
        print("Tu palabra vale {0} puntos".format(puntos))

    print("Fin de Juego!")

juegar()
