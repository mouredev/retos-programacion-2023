"""
Crea una función que reciba una expresión matemática (String)
y compruebe si es correcta. Retornará true o false.
- Para que una expresión matemática sea correcta debe poseer un número, 
  una operación y otro número separados por espacios.
Tantos números y operaciones como queramos.
- Números positivos, negativos, enteros o decimales.
- Operaciones soportadas: + - * / % 
"""
import re

def exp_math(ecuacion):
#iniciar variables y trocear ecuación
    simbolos = ("+", "-", "*", "/", "%")
    elementos=ecuacion.split(" ")
    x = 0
    
#Si no da la talla o no hay suficientes elementos, no continuamos
    if len(elementos) < 3 or len(elementos)%2 == 0:
        return False

#recorre la lista para diferenciar números de simbolos (número símbolo número ...)
    while x < len(elementos):
        if x==0 or x%2 == 0:
            if elementos[x].replace(".","").isdigit() == False:
                return False
        else:
            if not(elementos[x] in simbolos) :
                return False
        x = x + 1
    return True

print(exp_math("1 + 2")) #True
print(exp_math("1 x 2")) #False
print(exp_math("1 + ")) #False
print(exp_math("+ 2")) #False
print(exp_math("1 + 2 - 3 + 4 * 5 / 6 % 7")) #True
print(exp_math("1+2")) #False
print(exp_math("1,5 + 2")) #False
print(exp_math("1 + 0.2")) #True
