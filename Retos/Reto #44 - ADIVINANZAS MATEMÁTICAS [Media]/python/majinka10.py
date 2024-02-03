import selectors, sys, random

# Esta funcion es un input con un contador de tiempo. Si no se
# ingresa un valor durante el tiempo devuelve None, en caso
# contrario devuelve el valor ingresado.
# https://es.stackoverflow.com/questions/236436/limitar-tiempo-para-input-python-3-7
def timed_input(prompt="", timeout=3):
    sel = selectors.DefaultSelector()
    sel.register(sys.stdin, selectors.EVENT_READ, input)

    respuesta = None
    print(prompt, end="")
    events = sel.select(timeout=timeout)
    if events:
        respuesta = input()
    return respuesta

# Defino los posibles operadores para las operaciones.
operadores = ['+', '-', '*', '/']

# Inicializo algunas variables
max_one, max_two = 9, 9 # El maximo de cifras para cada uno de los operadores
aciertos = 0 # Contabiliza la cantidad de aciertos que lleva el usuario
aumentado = False # Una bandera en caso de que el usuario ingrese un valor
# al azar para saltar a la siguiente pregunta. Esto impide que se aumente el
# posible número de cifras sin acertar respuestas.

while True:
    # Operadores y operandos aleatorios.
    operador = random.choice(operadores)
    operando_one = random.choice(range(0, int(max_one)))
    operando_two = random.choice(range(0, int(max_two)))

    print ("Tienes 3 segundos para responder")

    # 'Switch case' para hacer la operacion y encontrar el resultado 
    # correcto antes de hacer la pregunta.
    if operador == '+':
        resultado = operando_one + operando_two
    elif operador == '-': 
        resultado = operando_one - operando_two
    elif operador == '*':
        resultado = operando_one * operando_two
    elif operador == '/':
        while operando_two == 0:
            operando_two = random.choice(range(0, int(max_one)))
        resultado = operando_one / operando_two

    print(f"¿Cuánto es {operando_one} {operador} {operando_two}?")

    us_input = timed_input()

    # Si el usuario no responde en el tiempo designado se rompe el ciclo.
    if us_input == None:
        print(f"Tiempo agotado! Acertaste {aciertos} cálculos.")
        break
    # Si el usuario acierta, aumenta los aciertos en 1 y vuelve a la bandera
    # false, lo que permite aumentar el posible número de cifras.
    elif float(us_input) == resultado:
        aciertos += 1
        aumentado = False
        print("Correcto!")
    else:
        print("Fallaste, respuesta correcta:", resultado)
    
    # Lógica para aumentar el posible número de cifras.
    if aciertos % 5 == 0 and not aumentado:
        max_one = str(max_one)
        max_two = str(max_two)
        if len(str(max_one)) == len(str(max_two)):
            max_one += '9'
            aumentado = True
        elif len(str(max_one)) > len(str(max_two)):
            max_two += '9'
            aumentado = True