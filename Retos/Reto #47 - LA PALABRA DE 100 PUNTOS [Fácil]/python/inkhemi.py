def pointsPerWord():
    letterPoints = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
                    "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                    "k": 11, "l": 12, "m": 13, "n": 14, "ñ": 15,
                    "o": 16, "p": 17, "q": 18, "r": 19, "s": 20,
                    "t": 21, "u": 22, "v": 23, "w": 24, "x": 25,
                    "y": 26, "z": 27
                    }

    print("Intenta escribir una palabra de 100 puntos. \nCada palabra tiene una cantidad de puntos según su lugar en el alfabeto.")
    print("Escribe 0 para salir")

    while True:
        points = 0
        word = input("Ingresa una palabra sin utilizar tildes: ").lower()
        if word == "0":
            print("Saliste con éxito")
            break

        try:
            for letter in word:
                points += letterPoints[letter]

            if points == 100:
                print("Lograste escribir una palabra de 100 puntos. \nHas ganado")
                break
            print(f"La palabra tiene {points} puntos")
        except KeyError:
            print("Argumento incorrecto")


if __name__ == "__main__":
    pointsPerWord()
