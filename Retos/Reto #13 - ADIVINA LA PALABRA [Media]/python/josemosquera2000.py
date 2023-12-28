'''''/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */'''

import random
def adivinar_palabra():
    palabras = ["Martes", "Python", "Jugar", "Abeja", "Arbusto", "JavaScript", "Patio"]
    aleatorio = random.choice(palabras).lower()
    # Calcular cuántos caracteres se deben reemplazar
    caracteres_reemplazar = max(int(len(aleatorio) * 0.57), 1)

    # Obtener una lista de índices aleatorios para reemplazar
    indices_reemplazar = random.sample(range(len(aleatorio)), caracteres_reemplazar)

    # Crear una lista de caracteres con los caracteres reemplazados
    palabra_lista = list(aleatorio)
    for i in indices_reemplazar:
        palabra_lista[i] = '_'

    # Convertir la lista de caracteres de vuelta a una cadena



    contador=0
    intentos_maximos = 7
    intentos_realizados = 0
        
    while intentos_realizados < intentos_maximos:
        print(" ".join(palabra_lista))
        letra_ingresada = input("Ingresa una letra o la palabra completa a adivinar: ").lower()
            
        if len(letra_ingresada) == 1:
            if letra_ingresada in aleatorio:
                for i in range(len(aleatorio)):
                    if aleatorio[i] == letra_ingresada:
                        palabra_lista[i] = letra_ingresada
                        intentos_realizados+=1
                if "_" not in palabra_lista:
                    print("¡Ganaste!")
                    print(f"La palabra era {aleatorio}.")
                    print(f"Intentos realizados: {intentos_realizados}")
                    return
            else:
                    intentos_realizados += 1
                    intentos_restantes = intentos_maximos - intentos_realizados
                    print(f"La letra {letra_ingresada} no está en la palabra. Intentos restantes: {intentos_restantes}")
        else:
            if letra_ingresada == aleatorio:
                print("¡Ganaste!")
                print(f"La palabra era {aleatorio}.")
                print(f"Intentos realizados: {intentos_realizados}")
                return               
            else:
                intentos_realizados += 1
                intentos_restantes = intentos_maximos - intentos_realizados
                print(f"La palabra ingresada no es correcta. Intentos restantes: {intentos_restantes}")
        
    print("¡Perdiste!")
    print(f"La palabra era {aleatorio}.")

adivinar_palabra()
