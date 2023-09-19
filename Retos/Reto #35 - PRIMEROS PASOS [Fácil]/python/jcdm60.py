# Reto #35: Primeros pasos
#### Dificultad: Fácil | Publicación: 28/08/23 | Corrección: 04/09/23

## Enunciado

#
# Como cada año, el día 256 se celebra el "Día de la Programación".
# En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos
# 256 regalos para seguir aprendiendo programación:
# https://diadelaprogramacion.com
#
# Para seguir ayudando, te propongo este reto:
# Mostrar la sintaxis de los principales elementos de un lenguaje
# en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
#
# En un fichero, haz lo siguiente (si el lenguaje lo soporta),
# y comenta cada bloque para identificar con qué se corresponde:
# - Haz un "Hola, mundo!"
# - Crea variables de tipo String, numéricas (enteras y decimales)
#   y Booleanas (o cualquier tipo de dato primitivo).
# - Crea una constante.
# - Usa un if, else if y else.
# - Crea estructuras como un array, lista, tupla, set y diccionario.
# - Usa un for, foreach y un while.
# - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
# - Crea una clase.
# - Muestra el control de excepciones.
#
# Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
# de sintaxis básica de muchos lenguajes.
#
# ¡Muchas gracias!
#

# Hola, mundo!
print("Hola, mundo!")

# Variables
my_string = "Hola, soy un string"
my_integer = 69
my_float = 3.14159
my_boolean = False

# Constante
PI = 3.14159

# Estructuras de datos
my_list = ["lima", "limon", "mandarina"]
my_array = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3, 4, 5, 6}
my_dictionary = {"nombre": "Juan", "edad": 30, "ciudad": "Barcelona"}

# Condiciones
my_number = 1
if my_number > 1:
    print("El número es mayor que 1")
elif my_number == 10:
    print("El número es igual a 1")
else:
    print("El número es menor que 1")

# Bucles
# For
for item in list:
    print(item)

# For Each (a través de un bucle for)
for num in my_array:
    print(num)

# While
count = 0
while count < 5:
    print("Contador:", count)
    count += 1


# Funciones
def add(a, b):
    return a + b


def hello(nombre):
    print("Hola,", nombre)


def is_even(number):
    return number % 2 == 0


# Clase
class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hola, soy", self.name)


# Control de excepciones
try:
    result = 5 / 0
except ZeroDivisionError:
    print("Error: división por cero")

