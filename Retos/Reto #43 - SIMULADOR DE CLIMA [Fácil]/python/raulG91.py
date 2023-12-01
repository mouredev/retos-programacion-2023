from random import randrange

def sim_weather(ini_temp,ini_rain_percentage,num_days=7):
    min_temp = ini_temp
    max_temp = ini_temp
    rain_percentage = ini_rain_percentage
    rain_days = 0
    temperature_today  =  ini_temp
    temperature_previos_day = temperature_today
    temperature_next_day = temperature_today
    
    for day in range(1,num_days + 1):
        is_raining = False
        temperature_previos_day = temperature_today
        temperature_today = temperature_next_day
        
        print("Temparature on day " + str(day)  + " is " + str(temperature_today))
        #Adjust min and max temperature
        if temperature_today < min_temp:
            min_temp = temperature_today
        elif temperature_today > max_temp:
            max_temp = temperature_today    
        #Generate a random number to check if it will rain
        random = randrange(0,100)
        if random <= rain_percentage:
            #It will rain
            is_raining = True
            rain_days +=1
            print("it will rain")
        else:
            print("it won't rain")    
        if temperature_today > 25:
         #Temparature is bigger than 25 so we increase rain percentage 20%
            rain_percentage += 20 
        if temperature_previos_day - temperature_today == 5:
           #Temperature decrease 5 degrees
           rain_percentage -= 20

        if is_raining :
            #if it's raining 100% temperature will decrease 1 degree
            temperature_next_day = temperature_today - 1 
        else:
            # there is a 10% of changing temparature
            random = randrange(0,100)
            if random <= 10:
                #Temperature will change and new random will be generated to know if it will 
                # increase or  decrease
                random = randrange(0,1)
                if random == 0:
                    temperature_next_day = temperature_today + 2
                else:
                    temperature_next_day = temperature_today - 2    
    print("Number days with rain " + str(rain_days))
    print("Max temperature expected " + str(max_temp) + " , min temperature expected " + str(min_temp))

ini_temp = int(input("Set initial temperature "))
ini_rain_percentage = int(input("Set initial rain probability "))

sim_weather(ini_temp=ini_temp, ini_rain_percentage= ini_rain_percentage)