import datetime

def is_friday_thirteen(year: int, month: int) -> bool:
    try:
        # verificamos si el año está dentro del rango válido (entre 1 y 9999). 
        # Si no es así, lanzamos una excepción ValueError
        if not 1 <= year <= 9999: 
            raise ValueError("El año debe estar en el rango entre 1 y 9999")
        # verificamos si el mes está dentro del rango válido (entre 1 y 12). 
        # Si no es así, lanzamos una excepción ValueError
        elif not 1 <= month <= 12:
            raise ValueError("El mes debe estar entre el 1 y 12")
        # Crear una instancia de la fecha para el día 13 del año y mes dados
        date_13th = datetime.date(year, month, 13)
        
        # Verificar si el día de la semana es viernes (4)
        return date_13th.weekday() == 4
    except ValueError as ve:
        return False, str(ve)
        
        # Capturar la excepción si la fecha no es válida (por ejemplo, mes fuera de rango)
        return False

# Probar la función con diferentes años y meses
print(is_friday_thirteen(2023, 10))
print(is_friday_thirteen(2023, 1))
print(is_friday_thirteen(-5, 12))
print(is_friday_thirteen(2022, 8))
print(is_friday_thirteen(2022, 2))
print(is_friday_thirteen(2023, 14))

