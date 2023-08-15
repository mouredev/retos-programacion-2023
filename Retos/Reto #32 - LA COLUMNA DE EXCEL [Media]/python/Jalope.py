"""
Consideraremos las columnas como un sistema numérico en base 26. Para pasar a base 10, debemos realizar la operación 
    Dado un número de columna c con n dígitos, donde c_i es el dígito en la posición i-ésima, el número decimal d 
    equivalente se calcula como:
        sum_{i=0}^{n-1} c_i * 26^i
"""
#creamos el diccionario que hace corresponder a cada letra de la A a la Z su valor decimal: A=1, B=2,...,Z=26
alp_pos_map = {chr(i): i - 64 for i in range(65, 91)}

def excelCol_To_decimal(col: str)-> int:
    decimal_value = 0
    #potencia en base 26
    power = 1 

    #Iteramos el string de entrada en orden inverso
    for char in reversed(col):
        decimal_value += alp_pos_map[char]*power
        power *= 26
    return decimal_value
#{Q: d=(sum i: 0<=i<=n:col[i]*2^i)}