import random
import time

def randon_select(level)-> list:
    operator = ['+','-','*','/']
    numbers = [random.randint(0,level-1),random.randint(0,level-1)]
    return [random.choice(operator),numbers]

def calculator(elementos: list):
    numeros = elementos[1]
    match elementos[0]:
        case '+':
            return numeros[0]+numeros[1]
        case '-':
            return numeros[0]-numeros[1]
        case '*':
            return numeros[0]*numeros[1]
        case '/':
                if numeros[1] == 0:
                    numeros[1] = random.randint(1,9)
                    return numeros[0] / numeros [1]
                else:
                    return numeros[0] / numeros[1]

while True:
    counter = 0
    level = 10
    operacion = randon_select(level)
    respuesta = calculator(operacion)
    print(f'resuelva la siguente operacion:')
    print(f'{operacion[1][0]}{operacion[0]}{operacion[1][1]}')
    print('tiene 3 segundos para responder ')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    user_answer = float(input('ingrese la respuesta '))
    if user_answer == respuesta:
        print('bien hecho')
        counter += 1
    else:
        print('respuesta erronea')
        break
    if counter == 10:
        level *= 10




