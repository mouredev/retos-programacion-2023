import random
import threading
import queue
import os

operations = {
    1: "+",
    2: "-",
    3: "*",
    4: "/"
}


def get_input(input_queue):
    input_queue.put(float(input("Respuesta: ")))


input_queue = queue.Queue()


def operations_game():
    '''
    Juego de resolución de operaciones matemáticas básicas con limite de tiempo de 3 segundos.
    '''

    digits_1 = 1
    digits_2 = 1
    questions = 0
    cont = 0

    while True:
        op = random.randint(1, 4)
        number_1 = random.randint(0, int("9" * digits_1))
        number_2 = random.randint(0, int("9" * digits_2))

        if op == 1:
            result = number_1 + number_2
        elif op == 2:
            result = number_1 - number_2
        elif op == 3:
            result = number_1 * number_2
        else:
            if number_2 == 0:  # Si el divisor es 0, se cambia por 1 para evitar errores
                number_2 += 1
            result = number_1 / number_2

        print(f"{number_1} {operations[op]} {number_2} = ?")
        input_thread = threading.Thread(target=get_input, args=(input_queue,))
        input_thread.start()
        input_thread.join(timeout=3)

        if input_thread.is_alive():
            print("\nTiempo agotado!")
            break

        answer = input_queue.get()

        if answer == result:
            print("Correcto!\n")
        else:
            break

        questions += 1
        cont += 1
        if cont == 5:
            if digits_1 == digits_2:
                digits_1 += 1
            else:
                digits_2 += 1
            cont = 0

    print(f"Fin del juego \nRespuestas correctas: {questions}")
    # Se usa os._exit(0) para terminar el programa cuando se acaba el tiempo
    os._exit(0)


operations_game()
