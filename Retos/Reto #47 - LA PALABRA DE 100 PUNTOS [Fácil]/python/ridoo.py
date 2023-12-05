''' /*
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */ '''

def validacion(palabra):
    while True: 
        if palabra.isalpha():
            palabra = palabra.lower()
            return palabra
        else:
            palabra = input('Ingrese una palabra valida sin numeros ni caracteres especiales: ')
            
def valor_por_caracter(caracter):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    for i, letra in enumerate(abecedario):
        if letra == caracter:
            valor = i + 1
            return valor
        else:
            pass
        

def calcular_puntos(palabra, objetivo):
    ganador = False
    
    palabra = validacion(palabra)
    acumulador = 0
    for caracter in palabra:
        acumulador += valor_por_caracter(caracter)
            
    if acumulador == objetivo:
        print(f'Lo lograste... Llegaste a {objetivo} puntos con tan solo una palabra')
        ganador = True
        return ganador
    elif acumulador < objetivo:
        print(f'Te faltaron {objetivo - acumulador} puntos para llegar al objetivo... vuelve a intentar')
    elif acumulador > objetivo:
        print(f'Sobrepasaste al objetivo por {acumulador - objetivo} puntos... vuelve a intentar')
        
    
# Presentación del juego
print("Bienvenido a mi juego.")
print("Cada letra tiene un valor asignado según el abecedario.")
print("El objetivo es formar palabras y acumular puntos hasta llegar a 100.")
print("Intenta llegar exactamente a 100 puntos con una sola palabra")
print("Si quieres finalizar el juego, ingresa el numero 0 en la opcion 'palabra'")
print("Comencemos...\n")

objetivo = 100
while True:
    palabra = input('Ingresa una palabra: ')
    
    if palabra == '0':
        print('Muchas gracias por utilizar mi programa')
        break
    
    ganador = calcular_puntos(palabra, objetivo)
    
    if ganador:
        print('Ganaste el juego')
        break
