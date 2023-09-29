import string

def columna_excel(columna: str) -> str:

    list_alphabet = (list(string.ascii_uppercase))
    numero_columnas = 0
    for indice in columna.upper():
            valor_letra = (list_alphabet.index(indice) + 1) 
            numero_columnas = numero_columnas * 26 + valor_letra
            
    return numero_columnas       

print(columna_excel("A"))
print(columna_excel("z"))
print(columna_excel("AA"))
print(columna_excel("CA"))
print(columna_excel("DDD"))

