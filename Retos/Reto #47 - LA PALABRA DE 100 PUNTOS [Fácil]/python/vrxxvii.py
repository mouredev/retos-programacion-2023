
# La palabra de 100 puntos

def calcular_puntos_palabra(palabra):
    puntos = 0
    for letra in palabra.upper():
        if 'A' <= letra <= 'Z':
            puntos += ord(letra) - ord('A') + 1
        elif letra == 'Ñ':
            puntos += 15  # Asignando un valor a la Ñ, que no está en el rango A-Z
    return puntos

def main():
    print("Programa para calcular los puntos de una palabra.")
    print("Cada letra tiene un valor asignado (A=1, B=2, ..., Z=27, Ñ=15).")
    print("Introduce una palabra para calcular sus puntos. El programa finaliza si logras 100 puntos.")

    while True:
        palabra = input("Introduce una palabra: ")
        puntos = calcular_puntos_palabra(palabra)
        print(f"La palabra '{palabra}' tiene {puntos} puntos.")

        if puntos >= 100:
            print("¡Felicidades! Lograste una palabra de 100 o más puntos.")
            break

if __name__ == "__main__":
    main()
