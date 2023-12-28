from datetime import datetime
while True:
    try:
        dia_input = int(input("Dia: "))
        mes_input = int(input("Mes: "))
        año_input = int(input("Año: "))
    except:
        print("ERROR: se debe introducir números")
        continue
    else:
        break

def viernes_trece (año, mes, dia):
    fecha = datetime(año, mes, dia)
    dia_es = fecha.strftime("%A")
    if dia_es == "Friday":
        print(True)
    else:
        print(False)

viernes_trece(año_input,mes_input, dia_input)