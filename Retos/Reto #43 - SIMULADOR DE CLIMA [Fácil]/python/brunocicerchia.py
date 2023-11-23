import random
    
def nextDay(days, temp, rain):
    minTemp = 100
    maxTemp = 0
    rainCount = 0
    # For que recorre los dias elegidos por el usuario
    for i in range(days):
        print("Day: " + str(i+1))
        
        # 10% de probabilidad de que la temperatura cambie 2 grados
        if random.randint(0,100) < 10:
            if random.randint(0,100) < 50:
                temp = temp - 2
            else:
                temp = temp + 2
                
        # Si la temperatua es mayor a 25 grados aumenta la probabilidad de lluvia
        if temp > 25:
            # Validacion para no superar el 100% de lluvia
            if rain < 80:
                rain = rain + 20
            else:
                rain = 100
        
        # Si la temperatura es menor a 5 grados disminuye la probabilidad de lluvia
        if temp < 5:
            if rain < 20:
                rain = 0
            else:
                rain = rain - 20
        
        # Si llueve la temperatura disminuye 1 grado y se suma un dia de lluvia
        if rain == 100:
            rainCount = rainCount + 1
            print("Rainy day")
            
        # Checkeo si la temperatura es minima o maxima
            
        if temp < minTemp:
            minTemp = temp
        
        if temp > maxTemp:
            maxTemp = temp
        
        print("Temperature: " + str(temp))
        print("Rain probability: " + str(rain))
            
        print("")
    
    print("Rainy days: " + str(rainCount))
    print("Min temperature: " + str(minTemp))
    print("Max temperature: " + str(maxTemp))
    

def main():
    temp = int(input("Insert temperature: "))
    rain = int(input("Insert rain probability(%): "))
    nextDay(int(input("Insert days: ")), temp, rain)
    
if __name__ == "__main__":
    main()