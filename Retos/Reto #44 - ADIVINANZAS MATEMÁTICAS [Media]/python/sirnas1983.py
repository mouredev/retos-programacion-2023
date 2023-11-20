import random
import time

def operacion_aleatoria(tupla):
    a,b = tupla
    op = random.randint(1,4)
    if op == 1:
        res = a + b 
        signo = '+' 
    elif op == 2:
        res =  a - b
        signo = '-' 
    elif op == 3:
        res =  a * b
        signo = 'x' 
    else:
        if b == 0:
            b = 1
        res =  a // b
        signo = '//'
    return res, f"{a} {signo} {b} = "

def operandos_aleatorios(nivel):
    exp = nivel//2 + 1
    a = random.randint(1,10**exp) - 1 
    if nivel%2==0:
        b = random.randint(1,10**(exp -1)) - 1
    else:
        b = random.randint(1,10**exp) - 1
    return a, b

def juego_matematicas():
    jugar = input("¿Quieres jugar? s/n: ").lower() == "s"
    tiempo = 5
    nivel = 1
    correctas = 0
    while jugar:
        if correctas == 0:
            print("¿Preparado?")
            print("Nota: En las divisiones ingresar la parte entera unicamente")
        time.sleep(0.7)
        resp, texto = operacion_aleatoria(operandos_aleatorios(nivel))
        print(texto)
        cronom_on = time.time()
        guess = float(input("respuesta: "))
        cronom_off = time.time()
        vuelta = cronom_off - cronom_on
        if vuelta > tiempo:
            print(f"Tiempo agotado, tienes {tiempo} seg. para contestar correctamente")
            jugar = False
        elif guess == resp:
            print("¡Respuesta correcta!")
            correctas += 1
            if correctas % 5 == 0 and correctas < 16:
                nivel += 1
                print(f"¡¡Felicidades, pasaste al nivel {nivel}!!")
        else: 
            print("Respuesta incorrecta")
            print(f"La respuesta correcta era {resp}")
            jugar = False
        if not jugar:
            print("Gracias por participar")
            print(f"Usted logro {correctas} respuestas correctas")
            
juego_matematicas()
