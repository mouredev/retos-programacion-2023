'''
Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
de un lugar ficticio al pasar un número concreto de días según estas reglas:
- La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
- Cada día que pasa:
  - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
  - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
    siguiente aumenta en un 20%.
  - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
    siguiente disminuye en un 20%.
  - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
- La función recibe el número de días de la predicción y muestra la temperatura
  y si llueve durante todos esos días.
- También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
'''
import random

def predict_weather(initial_temperature: int, initial_rain: int, days: int):
    rain_days = 0
    max_temperature = initial_temperature
    min_temperature = initial_temperature
    
    temperature = initial_temperature
    rain = initial_rain
    
    for day in range(1, days + 1):
        
        print(f"Día {day}: {temperature}º y {rain}% de lluvia")
        
        if random.randint(0, 1) == 0:
            temperature += 2
        else:
            temperature -= 2
        
        if temperature > 25:
            rain += 20
            if rain > 100:
                rain = 100
        
        if temperature < 5:
            rain -= 20
            if rain < 0:
                rain = 0
        
        if rain == 100:
            temperature -= 1
        
        if random.randint(1, 100) <= rain:
            rain_days += 1
            print("Está lloviendo!")
        
        if temperature > max_temperature:
            max_temperature = temperature
        if temperature < min_temperature:
            min_temperature = temperature
    
    print("")
    print(f"Temperatura máxima del periodo: {max_temperature}º")
    print(f"Temperatura mínima del periodo: {min_temperature}º")
    print(f"Días lluviosos del periodo: {rain_days}")
        
    

predict_weather(25, 0, 50)