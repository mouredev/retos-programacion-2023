'''
Crea un juego interactivo por terminal en el que tendrás que adivinar 
el resultado de diferentes
operaciones matemáticas aleatorias (suma, resta, multiplicación 
o división de dos números enteros).
- Tendrás 3 segundos para responder correctamente.
- El juego finaliza si no se logra responder en ese tiempo.
- Al finalizar el juego debes mostrar cuántos cálculos has acertado.
- Cada 5 aciertos debes aumentar en uno el posible número de cifras 
  de la operación (cada vez en un operando):
  - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
  - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
  - Preguntas 11 a 15: XX operación YY
  - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
  ...
'''
import random
import threading

def read_answer_with_timeout():
    
    def on_timeout():
        print("\nTIEMOUT! Press enter")
        global still_playing
        still_playing = False
    
    timer = threading.Timer(3, on_timeout)
    timer.start()
    
    try:
        answer = input(f"{a} {operations[operation]} {b} = ")
    finally:
        timer.cancel()
    return answer


operations = ['+', '-', '*', '/']
a_length = 1
b_length = 1

correct_answers = 0
still_playing = True

while still_playing:
    if correct_answers > 0 and correct_answers % 5 == 0 and correct_answers % 10 != 0:
        a_length += 1
    if correct_answers > 0 and correct_answers % 10 == 0:
        b_length += 1
        
    a = random.randint(0, 10 ** a_length - 1)
    b = random.randint(0, 10 ** b_length - 1)
    operation = random.randint(0, 0)

    if operation == 0:
        answer = a + b
    elif operation == 1:
        answer = a - b
    elif operation == 2:
        answer = a * b
    else:
        answer = a / b

    user_answer = read_answer_with_timeout()
    
    if not still_playing:
        break
    elif user_answer == str(answer):
        print('CORRECT!')
        correct_answers += 1
    else:
        print('INCORRECT!')
        still_playing = False
        
print(f'Game Over, {correct_answers} correct answers!')
    