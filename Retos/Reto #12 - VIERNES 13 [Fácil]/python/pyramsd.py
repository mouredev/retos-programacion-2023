import datetime

def frienes_trece(year, month):
    try: 

        date = datetime.date(year, month, 13)
        date_str = date.strftime(f"%A %d de %B del %Y")

        if date.weekday() == 4:
            print(f"{date_str}: {True}")
        else:
            print(f"{date_str}: {False}")
    except ValueError:
        print("[-] ERROR: El mes debe ser un entero entre 1 y 12")

year = int(input("Año: "))
month = int(input("Mes: "))

frienes_trece(year, month)
