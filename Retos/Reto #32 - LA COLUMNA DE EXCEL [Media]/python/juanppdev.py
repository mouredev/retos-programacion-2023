def excel_column_to_number(column_name):
    column_name = column_name.upper() # Convertir a mayúsculas para asegurarnos de manejar todas las letras en mayúsculas
    result = 0

    for char in column_name:
        result = result * 26 + (ord(char) - ord('A')) + 1

    return result

print(excel_column_to_number('A'))
print(excel_column_to_number('B'))
print(excel_column_to_number('F'))
print(excel_column_to_number('M'))
print(excel_column_to_number('P'))
print(excel_column_to_number('Q'))
print(excel_column_to_number('Z'))
print(excel_column_to_number('AA'))
print(excel_column_to_number('DD'))
print(excel_column_to_number('NN'))
print(excel_column_to_number('ZZ'))
