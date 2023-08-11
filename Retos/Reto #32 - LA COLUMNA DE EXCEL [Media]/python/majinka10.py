def columna(nombre:str):
    nombre=nombre.upper()
    letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numero=0
    for char in range(len(nombre)):
        for i in letras:
            if i == nombre[char]:
                numero = numero * 26 + (letras.index(i)) + 1
    return numero

print(columna('A'))
print(columna('Z'))
print(columna('AA'))
print(columna('CA'))
print(columna('IK'))
print(columna('ZZ'))
print(columna('ABN'))

# print(ord('Z')-ord('A'))