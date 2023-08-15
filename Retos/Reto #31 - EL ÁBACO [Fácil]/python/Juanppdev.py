
def abacotostring(abaco):
    resultado = 0

    for i in range(len(abaco)):
        cuenta = abaco[i].split("---")[0].count("0")
        if i == 0:
            resultado += cuenta * 1000000
        else:
            resultado +=  cuenta * (10 ** (6 - i))
        
    return resultado

abaco = ["0---00000000",
         "000---000000",
         "---000000000",
         "00---0000000",
         "0000000---00",
         "000000000---",
         "---000000000"]

resultado = abacotostring(abaco)
print(resultado)

"""
Explicacion:

1. Primero, definimos la función leer_abaco, que toma el ábaco como entrada.
2. Creamos dos listas: unidades que contiene las representaciones numéricas para las unidades, y millones para los millones.
3. Inicializamos resultado en 0, que almacenará el número total representado por el ábaco.
4. Luego, recorremos cada elemento del ábaco usando un bucle for.
5. Usamos el método split("---") para separar la parte de la cuenta y eliminar los guiones, luego contamos cuántas "O" hay en la cuenta usando count("O").
6. Dependiendo del índice i, multiplicamos el valor de la cuenta por la cantidad correspondiente (unidades o millones) y lo agregamos al resultado.
7. Finalmente, retornamos el resultado total.
8. Al llamar a la función con el ábaco proporcionado, obtenemos el resultado 1.302.790, que es el número representado por el ábaco.
"""