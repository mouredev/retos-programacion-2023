"""
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
"""

points = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'Ñ': 15, 'O': 16, 'P': 17, 'Q': 18, 'R': 19, 'S': 20, 'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25, 'Y': 26, 'Z': 27}

sentence_points = 0

while sentence_points != 100:
    sentence = input("Introduce una frase: ")

    for letter in sentence:
        letter = letter.upper()
        if letter in points:
            sentence_points += points[letter]
    
    if sentence_points != 100:
        print(f"Puntos de la frase: {sentence_points}. ¡Intenta nuevamente! \n")
        sentence_points = 0
    else:
        print("¡Lo lograste!")
