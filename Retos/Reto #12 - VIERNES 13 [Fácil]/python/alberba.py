import datetime

def viernes_13(year: int, month: int) -> bool:
    try:
        return datetime.date(year, month, 13).weekday() == 4
    except:
        return False
    
print(viernes_13(2023, 3))
print(viernes_13(2023, 1))
print(viernes_13(2023, 13))
print(viernes_13(-2023, 1))