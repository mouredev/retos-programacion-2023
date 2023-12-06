"""
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
"""

import datetime






def ask_date():
    date = {}
    date["year"] = input("Año: ")
    date["month"] = input("Mes: ")
    date["day"] = "13"
    return date

def main():

    date_given = ask_date()
    if check_date_f13(date_given):
        print("Ese mes de ese año tiene Viernes 13")
    else: 
        print("Ese mes no tiene viernes 13")
    
def check_date_f13(date_given):
    
    x_date = datetime.date(int(date_given["year"]), int(date_given["month"]), int(date_given["day"]))
    no = x_date.weekday()

    if no != 4:
        return False
    else:
        return True
        
if __name__ == "__main__":
    main()