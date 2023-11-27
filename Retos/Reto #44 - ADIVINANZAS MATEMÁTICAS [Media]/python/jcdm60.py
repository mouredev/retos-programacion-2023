# Reto #44: Adivinanzas matemáticas
#### Dificultad: Media | Publicación: 13/11/23 | Corrección: 20/11/23

## Enunciado

#
# Crea un juego interactivo por terminal en el que tendrás que adivinar 
# el resultado de diferentes
# operaciones matemáticas aleatorias (suma, resta, multiplicación 
# o división de dos números enteros).
# - Tendrás 3 segundos para responder correctamente.
# - El juego finaliza si no se logra responder en ese tiempo.
# - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
# - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
#   de la operación (cada vez en un operando):
#   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
#   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
#   - Preguntas 11 a 15: XX operación YY
#   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
#

import random
import time

class GuessingGame:
    def __init__(self):
        self.level = 1
        self.correct_guesses = 0
        self.time_limit = 3
        
    def set_time_limit(self):
        try:
            self.time_limit = float(input("Ingrese el limite de tiempo de espera para las respuesta (en segundos): "))
        except ValueError:
            print("Límite invalido, usaré el límite por defecto de 3 segundos")

    def generate_operation(self):
        if self.level <= 5:
            x = random.randint(0, 9)
            y = random.randint(1, 9)
        elif self.level <= 10:
            x = random.randint(0, 99)
            y = random.randint(1, 9)
        elif self.level <= 15:
            x = random.randint(0, 99)
            y = random.randint(1, 99)
        else:
            x = random.randint(0, 999)
            y = random.randint(1, 99)

        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)

        operation = f"{x} {operator} {y}"
        result = eval(operation) if operator != '/' or y != 0 else x

        return operation, result

    def play(self):
        self.set_time_limit()
        
        while self.level <= 20:
            print(f"\nPregunta {self.level}:")
            operation, correct_result = self.generate_operation()
            print(f"Cuál es el resultado de: {operation}?")

            start_time = time.time()
            user_answer = input("Respuesta: ")

            if time.time() - start_time > self.time_limit:
                print("Tiempo agotado!")
                break

            try:
                user_answer = eval(user_answer)
            except (ValueError, ZeroDivisionError):
                print("Respuesta no válida")
                continue

            if round(user_answer, 2) == round(correct_result, 2):
                print("Correcto!")
                self.correct_guesses += 1
            else:
                print(f"Incorrecto. La respuesta correcta era: {correct_result}.")

            if self.correct_guesses % 5 == 0:
                print(f"\nUsted obtuvo {self.correct_guesses} respuestas correctas! Vamos a aumentar el número de dígitos!")

            self.level += 1

        print(f"\nFin del juego. Total de respuestas correctas: {self.correct_guesses}")

if __name__ == "__main__":
    game = GuessingGame()
    game.play()
