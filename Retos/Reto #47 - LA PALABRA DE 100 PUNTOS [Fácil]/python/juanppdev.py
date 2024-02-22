def calcular_puntos(palabra):
    """
    Calcula los puntos de una palabra según los valores asignados a cada letra.
    """
    puntos = 0
    for letra in palabra:
        # Asumiendo que estamos trabajando con el alfabeto español de 27 letras
        valor_letra = ord(letra.upper()) - ord('A') + 1
        puntos += valor_letra
    return puntos

def main():
    """
    Función principal del programa.
    """
    while True:
        palabra = input("Introduce una palabra: ")
        puntos = calcular_puntos(palabra)
        
        print(f"La palabra '{palabra}' tiene {puntos} puntos.")

        if puntos >= 100:
            print("¡Felicidades! Has alcanzado o superado los 100 puntos. El programa ha finalizado.")
            break

if __name__ == "__main__":
    main()
