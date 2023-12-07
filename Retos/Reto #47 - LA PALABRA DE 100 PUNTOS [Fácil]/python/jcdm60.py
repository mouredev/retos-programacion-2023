# Reto #47: La palabra de 100 puntos
#### Dificultad: Fácil | Publicación: 04/12/23 | Corrección: 11/12/23

## Enunciado

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

class PointsCalculator:
    def calculate_points(self, word):
        total_points = 0
        for letter in word:
            value_of_letter = ord(letter.upper()) - 64
            if 1 <= value_of_letter <= 26:  
                total_points += value_of_letter
        return total_points

def main():
    calculator = PointsCalculator()
    while True:
        word = input("Introduce una palabra: ")
        points = calculator.calculate_points(word)
        print(f"La palabra '{word}' tiene {points} puntos.")

        if points >= 100:
            print("Has alcanzado o superado los 100 puntos!")
            break

if __name__ == "__main__":
    main()
