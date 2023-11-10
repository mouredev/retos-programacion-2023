import random

def simular_condiciones_climaticas(dias_prediccion):
    temperatura_actual = float(input("Introduce la temperatura inicial: "))
    probabilidad_lluvia_actual = float(input("Introduce la probabilidad de lluvia inicial (%): "))
    
    temperatura_maxima = temperatura_actual
    temperatura_minima = temperatura_actual
    dias_lluvia = 0
    
    for dia in range(1, dias_prediccion + 1):
        # Determinar si la temperatura aumenta o disminuye en 2 grados
        cambio_temperatura = random.choice([-2, 2])
        temperatura_actual += cambio_temperatura
        
        # Actualizar probabilidad de lluvia
        if temperatura_actual > 25:
            probabilidad_lluvia_actual += 20
        if temperatura_actual < 5:
            probabilidad_lluvia_actual -= 20
        
        probabilidad_lluvia_actual = max(0, min(100, probabilidad_lluvia_actual))
        
        # Determinar si llueve en este día
        llueve = random.randint(1, 100) <= probabilidad_lluvia_actual
        
        if llueve:
            temperatura_actual -= 1
            dias_lluvia += 1
        
        # Actualizar temperatura máxima y mínima
        temperatura_maxima = max(temperatura_actual, temperatura_maxima)
        temperatura_minima = min(temperatura_actual, temperatura_minima)
        
        # Mostrar información del día
        print(f"Día {dia}: Temperatura: {temperatura_actual}°C, Probabilidad de lluvia: {probabilidad_lluvia_actual}%")
    
    print(f"Temperatura máxima: {temperatura_maxima}°C")
    print(f"Temperatura mínima: {temperatura_minima}°C")
    print(f"Días de lluvia: {dias_lluvia}")

# Llama a la función con el número de días de predicción
dias_prediccion = int(input("Introduce el número de días de predicción: "))
simular_condiciones_climaticas(dias_prediccion)
