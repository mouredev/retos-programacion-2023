def columna(nombre:str):
    nombre=nombre.upper()
    numero=0
    for char in nombre:
        numero = numero * 26 + (ord(char) - ord('A')) + 1
    return numero

print(columna('A'))
print(columna('Z'))
print(columna('AA'))
print(columna('CA'))
print(columna('IK'))
print(columna('ZZ'))
print(columna('ABN'))