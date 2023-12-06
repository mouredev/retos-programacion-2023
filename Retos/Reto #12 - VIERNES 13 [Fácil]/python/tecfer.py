'''
 Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 - La función recibirá el mes y el año y retornará verdadero o falso.
'''
import datetime

def friday_13(month, year) ->bool :
    try:
        return datetime.date(year, month, 13).isoweekday() == 5
    except:
        return False
    
def main():

    print(friday_13(6,2023))
    print(friday_13(4,2023))
    print(friday_13(10,2023))
    print(friday_13(1,2023))

if __name__ == '__main__':
    main()