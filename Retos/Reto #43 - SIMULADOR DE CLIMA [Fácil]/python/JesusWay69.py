import os
os.system('clear')
import random 
def weather_station (days:int,temperature:int,perc_rain:int):
    temp_max = temperature
    temp_min = temperature
    rain_prob_acc = 0.0
    rainy_days = 0

    for i in range (1 , days):
        rain_prob = random.random()
        two_degrees_up = random.random()
        two_degrees_down = random.random()
        if rain_prob < perc_rain/100:
            print ("el dia " , i , "sí llovió y la temperatura fue de ", temperature , " grados")
            temperature = temperature - 1
            rainy_days = rainy_days + 1
        else:
            print ("el dia " , i , "no llovió y la temperatura fue de ", temperature , " grados")

    if two_degrees_up > 0.9:  temperature += 2
    if two_degrees_down < 0.1: temperature -= 2
    if temperature > 25: rain_prob -= 0.2
    if temperature < 5: rain_prob += 0.2
    if temperature < temp_min: temp_min=temperature
    if temperature > temp_min: temp_min=temperature    
      
    print("Llovió un total de " , rainy_days , " días")
    print("La temperatura máxima fue de " , temp_max , " grados")
    print("La temperatura mínima fue de " , temp_min , " grados")
    



weather_station (31,24,20)