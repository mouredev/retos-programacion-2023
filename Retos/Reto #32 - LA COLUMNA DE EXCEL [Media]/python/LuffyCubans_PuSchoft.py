# Calcular el número de Columnas en Excel

def numero_columna(columna):
    resultado = 0
    
    for i in range(len(columna)):
        valor_letra = ord(columna[i]) - ord('A') + 1
        resultado = resultado * 26 + valor_letra
        
    return resultado

# Hacer que el usuario ingrese el número de columnas a calcular
cantidad_columnas = int(input("Ingrese la cantidad de columnas por favor: "))

columnas = []
for i in range(cantidad_columnas):
    # Ingresar el número de columnas uno x uno
    columna = input(f"Ingrese el nombre de la columna {i+1}: ")
    columnas.append(columna)

for columna in columnas:
    numero = numero_columna(columna)
    # Mostrar el resultado final
    print(f"La columna {columna} tiene un valor numérico de: {numero}")

# https://puschoft.blogspot.com
# Ciudad de Manzanillo , Cuba