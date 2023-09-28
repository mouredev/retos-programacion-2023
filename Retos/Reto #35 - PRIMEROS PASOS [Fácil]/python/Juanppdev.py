# Python
print("Hola, mundo!")

string_variable = "Hola"
int_variable = 42
float_variable = 3.14
bool_variable = True

CONSTANTE = 100

if bool_variable:
    print("Es verdadero")
elif int_variable > 50:
    print("Mayor que 50")
else:
    print("Ninguna condición se cumplió")

array = [1, 2, 3]
lista = [4, 5, 6]
tupla = (7, 8, 9)
conjunto = {10, 11, 12}
diccionario = {"clave1": "valor1", "clave2": "valor2"}

for item in array:
    print(item)

for item in lista:
    print(item)

index = 0
while index < len(tupla):
    print(tupla[index])
    index += 1

def funcion_sin_parametros():
    print("Hola desde función sin parámetros")

def funcion_con_parametros(parametro):
    print("El parámetro es:", parametro)

def funcion_con_retorno():
    return 42

class MiClase:
    def __init__(self):
        self.valor = 0

    def metodo(self):
        print("Método de la clase")

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error de división por cero")

# Continúa con más lenguajes si lo deseas
