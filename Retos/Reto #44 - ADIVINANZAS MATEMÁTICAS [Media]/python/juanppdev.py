import random
import time

def generar_operacion(num_digitos):
    num1 = random.randint(0, 10 ** num_digitos - 1)
    num2 = random.randint(0, 9)
    operadores = ['+', '-', '*', '/']
    operador = random.choice(operadores)
    operacion = f"{num1} {operador} {num2}"
    return operacion

def jugar():
    aciertos = 0
    num_digitos = 1

    while True:
        operacion = generar_operacion(num_digitos)
        print(f"Calcula: {operacion}")

        start_time = time.time()
        respuesta = input("Respuesta: ")

        if time.time() - start_time > 3:
            print("¡Tiempo agotado! Fin del juego.")
            break

        resultado_correcto = eval(operacion)

        if float(respuesta) == resultado_correcto:
            aciertos += 1
            print("¡Correcto!\n")
        else:
            print(f"Incorrecto. La respuesta correcta era {resultado_correcto}.\n")

        if aciertos % 5 == 0:
            num_digitos += 1

    print(f"Juego finalizado. Aciertos totales: {aciertos}")

if __name__ == "__main__":
    jugar()
