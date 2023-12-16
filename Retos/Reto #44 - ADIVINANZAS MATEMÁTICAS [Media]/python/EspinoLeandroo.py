import random
import time

def obtener_operacion_aleatoria():
    operaciones = ['+', '-', '*', '/']
    return random.choice(operaciones)

def calcular_resultado(operando1, operando2, operacion):
    if operacion == '+':
        return operando1 + operando2
    elif operacion == '-':
        return operando1 - operando2
    elif operacion == '*':
        return operando1 * operando2
    elif operacion == '/':
        return operando1 // operando2
    else:
        raise ValueError("Operación no válida")

def main():
    puntaje = 0
    operando_cifras = 1

    for pregunta in range(1, 21):
        operando1 = random.randint(0, 10 ** operando_cifras - 1)
        operando2 = random.randint(1, 10)
        operacion = obtener_operacion_aleatoria()

        print(f'Pregunta {pregunta}: {operando1} {operacion} {operando2}')

        tiempo_inicio = time.time()

        respuesta_usuario = input('Tu respuesta: ')

        tiempo_transcurrido = time.time() - tiempo_inicio

        resultado = calcular_resultado(operando1, operando2, operacion)
        
        if tiempo_transcurrido <= 3:
            if respuesta_usuario == str(resultado):
                print('¡Correcto!')
                puntaje += 1
            else:
                 print(f'Incorrecto. El resultado era: {resultado}')
        else:
            if respuesta_usuario == str(resultado):
                print(f'Correcto, pero tardaste {tiempo_transcurrido:.2f} segundos')
                puntaje += 1
            else:
                print(f'Incorrecto y tardaste {tiempo_transcurrido:.2f} segundos')
            break

        if pregunta % 5 == 0:
            operando_cifras += 1

    print(f'Juego terminado. Puntaje final: {puntaje}')

if __name__ == "__main__":
    main()
