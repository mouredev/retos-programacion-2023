#
# Reto #43: Simulador de clima
# Dificultad: Fácil | Publicación: 30/10/23 | Corrección: 13/11/23
#-----------------------------------------------------------------
# ENUNCIADO DEL EJERCICIO
#-----------------------------------------------------------------
# /*
#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
#  * - Cada día que pasa:
#  *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#  *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
#  *     siguiente aumenta en un 20%.
#  *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
#  *     siguiente disminuye en un 20%.
#  *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
#  * - La función recibe el número de días de la predicción y muestra la temperatura
#  *   y si llueve durante todos esos días.
#  * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
#  */
#-----------------------------------------------------------------

import random


print ("Pushodev")
print ("https://github.com/PushoDev")

def simular_clima_interactivo():
    # Solicitar entrada del usuario
    dias = int(input("Ingrese el número de días para la predicción: "))
    temp_inicial = float(input("Ingrese la temperatura inicial: "))
    prob_lluvia_inicial = float(input("Ingrese la probabilidad inicial de lluvia (0-1): "))

    # Inicializar variables
    temperatura = temp_inicial
    prob_lluvia = prob_lluvia_inicial
    llueve = False
    dias_lluvia = 0
    temperaturas = []

    # Simular condiciones climáticas
    for _ in range(dias):
        # 10% de posibilidades de cambio de temperatura
        if random.random() < 0.1:
            cambio_temperatura = random.choice([-2, 2])
            temperatura += cambio_temperatura

        # Ajustar probabilidad de lluvia según la temperatura
        if temperatura > 25:
            prob_lluvia += 0.2
        elif temperatura < 5:
            prob_lluvia -= 0.2

        # Verificar si llueve
        llueve = random.random() < prob_lluvia

        # Ajustar temperatura si llueve
        if llueve:
            temperatura -= 1

        # Registrar datos del día
        temperaturas.append(temperatura)

        # Contar días de lluvia
        if llueve:
            dias_lluvia += 1

    # Mostrar resultados
    temp_maxima = max(temperaturas)
    temp_minima = min(temperaturas)

    print(f"\nPredicción para los próximos {dias} días:")
    print(f"Temperatura máxima: {temp_maxima}°C")
    print(f"Temperatura mínima: {temp_minima}°C")
    print(f"Días de lluvia: {dias_lluvia}")
    print("Detalles por día:")
    for i, temp in enumerate(temperaturas, start=1):
        print(f"Día {i}: {temp}°C {'(lluvia)' if llueve else ''}")

# Ejecutar la simulación interactiva
simular_clima_interactivo()

print("Gracias por participar ...")
