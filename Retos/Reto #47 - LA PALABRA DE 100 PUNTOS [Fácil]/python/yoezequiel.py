def calcular_puntos(palabra):
    valores_letras = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "Ñ": 15,
        "O": 16,
        "P": 17,
        "Q": 18,
        "R": 19,
        "S": 20,
        "T": 21,
        "U": 22,
        "V": 23,
        "W": 24,
        "X": 25,
        "Y": 26,
        "Z": 27,
    }
    puntaje = sum(valores_letras.get(letra.upper(), 0) for letra in palabra)
    return puntaje


def main():
    total_puntos = 0
    print(
        """
        BIENVENID@ AL JUEGO DE PALABRAS
        En este emocionante desafío, tu objetivo es acumular puntos formando palabras. Cada letra tiene un valor asignado según su posición el abecedario
        Las reglas son simples:
            1. Ingresa una palabra y descubre cuántos puntos ganas.
            2. Intenta alcanzar un total de 100 puntos o más.
          """
    )
    while total_puntos < 100:
        palabra = input("Ingresa una palabra: ")
        puntos_palabra = calcular_puntos(palabra)

        print(f"Palabra: {palabra}, Puntos de la palabra: {puntos_palabra}")

        if puntos_palabra >= 100:
            print("¡Felicidades! Has alcanzado 100 puntos.")
            break


if __name__ == "__main__":
    main()
