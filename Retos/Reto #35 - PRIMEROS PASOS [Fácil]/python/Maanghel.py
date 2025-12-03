"""
Como cada año, el día 256 se celebra el "Día de la Programación".
En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos
    256 regalos para seguir aprendiendo programación:
    https://diadelaprogramacion.com

Para seguir ayudando, te propongo este reto:
Mostrar la sintaxis de los principales elementos de un lenguaje
    en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?

En un fichero, haz lo siguiente (si el lenguaje lo soporta),
    y comenta cada bloque para identificar con qué se corresponde:
- Haz un "Hola, mundo!"
- Crea variables de tipo String, numéricas (enteras y decimales)
    y Booleanas (o cualquier tipo de dato primitivo).
- Crea una constante.
- Usa un if, else if y else.
- Crea estructuras como un array, lista, tupla, set y diccionario.
- Usa un for, foreach y un while.
- Crea diferentes funciones (con/sin parámetros y con/sin retorno).
- Crea una clase.
- Muestra el control de excepciones.

Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
    de sintaxis básica de muchos lenguajes.

¡Muchas gracias!
"""

# Imprimir "Hola, mundo!" en Python
print("Hola, mundo!")

# Crear variables
my_string = "Hola"
my_integer = 42
my_decimal = 3.14
my_boolean = True

# Crear una constante
PI = 3.14159

# Estructura if, elif y else
if my_integer > 50:
    print("El número es mayor que 50")
elif my_integer == 50:
    print("El número es igual a 50")
else:
    print("El número es menor que 50")

# Crear estructuras de datos
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dictionary = {"key1": "value1", "key2": "value2"}

# Usar bucles
for i in range(5):
    print(i)

for item in my_list:
    print(item)

while my_integer > 0:
    my_integer -= 1
    print(my_integer)

# Crear funciones
def my_function() -> None:
    print("Esta es una función sin parámetros ni retorno")

def my_function_with_params(param1: str, param2: int) -> None:
    print(f"Parámetros recibidos: {param1}, {param2}")

def my_function_with_return() -> str:
    return "Valor de retorno"

# Crear una clase
class MyClass:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        print(f"Hola, {self.name}!")

# Control de excepciones
try:
    result = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e:
    print(f"Ocurrió un error: {e}")

# Ejemplo de uso de la clase
my_object = MyClass("Mundo")
my_object.greet()