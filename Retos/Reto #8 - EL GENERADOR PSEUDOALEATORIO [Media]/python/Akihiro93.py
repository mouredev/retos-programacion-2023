from datetime import datetime

def ramdom ():
    Date = datetime.now()
    number_N1, number_N2, number_N3 = Date.day, Date.hour, Date.second
    result = ((number_N1 + number_N2/number_N1 - number_N2) * number_N3) / 2
    if result > 100:
        result /= 2
    return str(round(result))

print("El numero aleatorio es: ", ramdom())
