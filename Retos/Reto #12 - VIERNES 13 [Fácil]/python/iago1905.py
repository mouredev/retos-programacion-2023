def viernes_trece(year, month):
    if month < 1 or month > 12:
        return "Mes incorrecto  (1-12)"
    else:
        import datetime
        fecha = datetime.date(year, month, 13)
        if fecha.weekday() == 4:
            return "¡VIERNES 13!"
        else:
            return "No es viernes 13"

print(viernes_trece(2016, 4))

print(viernes_trece(2023, 10))