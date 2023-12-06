# Hola mundo
print("Hola, mundo!")

# Variables
string_var = "Soy Leandro"
int_var = 26
float_var = 3.14
bool_var = True

# Constante
CONSTANT = 11

# If, else if, else
if int_var > CONSTANT:
    print("int_var es mayor que CONSTANT")
elif int_var == CONSTANT:
    print("int_var es igual a CONSTANT")
else:
    print("int_var es menor que CONSTANT")

# Estructuras de datos
array = [1, 2, 3, 4, 5]
lista = ["apple", "banana", "cherry"]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
diccionario = {"nombre": "Juan", "edad": 52}

# Bucle for
for num in array:
    print(num)

for fruit in lista:
    print(fruit)

# Bucle while
counter = 0
while counter < 5:
    print("Contador:", counter)
    counter += 1

# Funciones
# con parametros y con retorno
def sum(a, b):
    return a + b

# con parametros y sin retorno
def subtraction(a, b):
    print("Resta: ", (a - b))

# sin parametros y con retorno
def pi():
    return 3.1416

# sin parametros y sin retorno
def constante():
    print(CONSTANT)

print(sum(3, 5))
subtraction(3,5)
print(pi())
constante()

# Clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "años.")

persona1 = Persona("Itzel", 26)
persona1.saludar()

# Control de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
