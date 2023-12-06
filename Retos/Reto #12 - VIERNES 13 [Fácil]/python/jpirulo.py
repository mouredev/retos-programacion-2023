import datetime


class Viernes13:
    def __init__(self, mes, año):
        if not 1 <= mes <= 12:
            raise ValueError("El mes ingresado es inválido")
        if not 1900 <= año <= 2100:
            raise ValueError("El año ingresado es inválido")

        self.mes = mes
        self.año = año

    def es_viernes_13(self):
        dia = datetime.date(self.año, self.mes, 13)
        if dia.weekday() == 4:
            return True
        else:
            return dia.strftime("%A")


try:
    mes = int(input("Ingrese el mes (1-12): "))
    año = int(input("Ingrese el año: "))
    viernes_13 = Viernes13(mes, año)
    resultado = viernes_13.es_viernes_13()
    if resultado == True:
        print("¡El 13 del mes y año indicados es un viernes 13!")
    else:
        print(f"El 13 del mes y año indicados corresponde a un {resultado}.")
except ValueError as error:
    print(f"Error: {error}")
