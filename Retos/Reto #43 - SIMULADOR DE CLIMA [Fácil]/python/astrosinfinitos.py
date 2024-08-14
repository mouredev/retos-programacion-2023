# /
#  Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
#  - Cada día que pasa:
# - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
# - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
#      siguiente aumenta en un 20%.
#    - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
#     siguiente disminuya en un 20%.
#   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
#  - La función recibe el número de días de la predicción y muestra la temperatura
#    y si llueve durante todos esos días.
#  - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
# /

import random


def obtener_tiempo():
    temperatura_inicial = int(input("Ingrese temperatura inicial: "))
    probabilidad_lluvia = int(input("Ingrese probabilidad de lluvia: "))
    estimacion_dias = int(input("Días predichos: "))
    dias_lluvia = 0
    temperatura_actual = temperatura_inicial
    temperatura_maxima = temperatura_inicial
    temperatura_minima = temperatura_inicial

    for dia in range(estimacion_dias):
        # Hay que determinar la probablidad de que lluvia durante el día de hoy
        probabilidad_lluvia = max(
            0, min(100, probabilidad_lluvia)
        )  # Mantener entre 0 y 100
        # Determinar si llueve
        llueve_hoy = random.random() <= probabilidad_lluvia / 100
        # Ajustes de temperatura
        if random.random() <= 0.1:  # 10% de probabilidad de cambio
            if random.random() < 0.5:
                temperatura_inicial -= 2
            else:
                temperatura_inicial += 2
        # Ajustar la probablidad de lluvia
        if temperatura_inicial > 25:
            probabilidad_lluvia += 20
        elif temperatura_inicial < 5:
            probabilidad_lluvia -= 20
        if probabilidad_lluvia == 100:
            dias_lluvia += 1
            temperatura_inicial -= 1
        # Mostramos el prónostico del día
        print(f"Día{dia+1}: Temperatura = {temperatura_actual} °C")
        # Actualizamos resultados
        if llueve_hoy:
            temperatura_actual -= 1  # Disminuir la temperatura si llovió
            dias_lluvia += 1

        temperatura_maxima = max(temperatura_maxima, temperatura_actual)
        temperatura_minima = min(temperatura_minima, temperatura_actual)

        # Mostrar el pronóstico para el día
        print(
            f"Día {dia}: Temperatura = {temperatura_actual}°C, Llueve = {'Hoy parece que lloverá' if llueve_hoy else 'Hoy parece que no lloverá'}"
        )

        # Nostrar el resumen final
        print(f"\nTemperatura máxima: {temperatura_maxima}°C")
        print(f"Temperatura mínima: {temperatura_minima}°C")
        print(f"Días de lluvia: {dias_lluvia}")


obtener_tiempo()
