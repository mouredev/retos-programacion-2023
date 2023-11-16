"""
/*
 * Crea un juego interactivo por terminal en el que tendrás que adivinar 
 * el resultado de diferentes
 * operaciones matemáticas aleatorias (suma, resta, multiplicación 
 * o división de dos números enteros).
 * - Tendrás 3 segundos para responder correctamente.
 * - El juego finaliza si no se logra responder en ese tiempo.
 * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
 * - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
 *   de la operación (cada vez en un operando):
 *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
 *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
 *   - Preguntas 11 a 15: XX operación YY
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 *   ...
 */
"""
from enum import Enum
import random
from inputimeout import inputimeout, TimeoutOccurred

class Operator(Enum):
    ADD = 1 
    SUBSTRACT = 2 
    MULTIPLY = 3 
    DIVIDE = 4

class ResultOperation(Enum):
    OK = 1
    ERROR_DIV_0 = 2

def get_operator():
    rand_operator =random.randint(1,4)
    return(Operator(rand_operator))

def get_number(digits):
    number = 0
    for d in range(digits):
        if d == 0:
            rand_digit = random.randint(0,9)
        else:
            rand_digit = random.randint(1,9)
        number += 10**d * rand_digit
    return number

def do_operation(digit_op1, digit_op2):
    operand_one = get_number(digit_op1)
    operand_two = get_number(digit_op2)
    operator = get_operator()
    match operator:
        case Operator.ADD:
            print(f"{operand_one} + {operand_two} = ", end="")
            return (operand_one + operand_two), ResultOperation.OK
        case Operator.SUBSTRACT:
            print(f"{operand_one} - {operand_two} = ", end="")
            return (operand_one - operand_two), ResultOperation.OK            
        case Operator.MULTIPLY:
            print(f"{operand_one} * {operand_two} = ", end="")
            return (operand_one * operand_two), ResultOperation.OK
        case Operator.DIVIDE:
            if operand_two == 0:
                return 0, ResultOperation.ERROR_DIV_0
            print(f"{operand_one} / {operand_two} = ", end="")
            return (operand_one / operand_two), ResultOperation.OK

correct_answers = 0
digit_op1 = 1
digit_op2 = 1

while True:    
    guess, isOK = do_operation(digit_op1, digit_op2)
    if isOK == ResultOperation.ERROR_DIV_0:
        continue
    try:
        result = inputimeout(prompt='', timeout=10)
    except TimeoutOccurred:
        print("Perdiste")
        break    
    if round(float(result),2) == round(float(guess),2):
        correct_answers += 1
        pack_5answer_count = int(correct_answers / 5)
        if correct_answers % 5 == 0 and not pack_5answer_count == 0:
            print("Has subido de nivel. Nivel: "+str(pack_5answer_count))
            if pack_5answer_count % 2 == 0:
                digit_op2 += 1
            else:
                digit_op1 += 1   
    else:
        print("Perdiste")
        break
