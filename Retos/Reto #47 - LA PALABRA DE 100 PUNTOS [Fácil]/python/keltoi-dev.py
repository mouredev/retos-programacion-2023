"""/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */"""

print("Bienvenido al juego de palabras!!!")
print("Tienes que escribir una palabra que sume 100 puntos.")
print("La palabra debe existir en el diccionario.\n")

palabra = input("Introduce una palabra: ").lower()
puntos = 0

for letra in palabra:
    valor = ord(letra)
    if letra == "ñ":
        puntos += valor - 226
    elif valor > 96 and valor < 110:
        puntos += valor - 96
    elif valor > 110 and valor < 123:
        puntos += valor -95
    else:
        print("La palabra tiene caracteres que no son letras.")

if puntos == 100:
    print("Ganaste!!! Ingresaste un aplabra de 100 puntos.")
else:
    print(f"Haz ingresado una palabra que suma {puntos} puntos")
