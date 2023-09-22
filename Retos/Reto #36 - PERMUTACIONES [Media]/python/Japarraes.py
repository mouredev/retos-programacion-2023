""" Reto Semanales'23: Crea un programa que sea capaz de generar e imprimir
    todas las permutaciones disponibles formadas por las letras de una palabra.
    - Las palabras generadas no tienen por qué existir.
    - Deben usarse todas las letras de cada permutación"""

# Solución mediante recursividad 
def permutationsRecursion(last_segment, word=''):

    # "ABC"
    # A --> BC              B --> AC                C --> AB
    #       B -->C (ABC)           A --> C (BAC)          A --> B (CAB)
    #       C -->B (ACB)           C --> A (BCA)          B --> A (CBA)
    # 

    if len(last_segment) == 0:
        print(word)

    for i in range(len(last_segment)):

        new_word = word + last_segment[i]
        newlast_segment = last_segment[0:i] + last_segment[i+1:]

        permutationsRecursion(newlast_segment, new_word)

# Python tiene funciones específicas para establecer iteraciones de elementos,
# en este caso, las letras de un string  
from itertools import permutations
def permutationsmodulo(word):

    list_combinations = list(permutations(word))

    for combination in list_combinations:
        print("".join(combination))


# MAIN PROGRAM
s = 'ABC'
# Recursividad
permutationsRecursion(s)

# Separador soluciones
print("---------------------------------------------------------")

# Función de Python
permutationsmodulo(s)