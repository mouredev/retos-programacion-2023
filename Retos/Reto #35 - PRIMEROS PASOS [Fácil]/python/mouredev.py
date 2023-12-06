# Hola mundo
print("¡Hola, Python!")

# Variables
my_variable = "Esto es una variable"
my_variable = "Aquí asigno un nuevo valor a la variables"

# Tipos de datos primitivos
my_string: str = "Mi cadena de texto"
my_int: int = 1
my_float: float = 1.5
my_bool: bool = True

# Constantes
MY_CONSTANT = "No existen las constantes. Simplemente se nombran variables en mayúscula."

# Control de flujo
if my_int == 1:
    print("my_int vale 1")
elif my_int == 2:
    print("my_int vale 2")
else:
    print("my_int no vale ni 1 ni 2")

# Estructuras
my_list: list = [my_string, my_int, my_float, my_bool]
my_tuple: tuple = (my_string, my_int, my_float, my_bool)
my_set: set = set([my_string, my_int, my_float, my_bool, my_string])
my_dictionary: dict = {"str": my_string, "int": my_int, "float": my_float, "bool": my_bool}

# Bucles
for index in range(10):
    print(index)

for item in my_list:
    print(item)

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# Funciones
def my_function():
    print("Función simple")

def my_function_with_return() -> str:
    return "Función con retorno"

def my_function_with_parm(param: int):
    print(f"Función con un parámetro de valor {param}")

my_function()
print(my_function_with_return())
my_function_with_parm(256)

# Clases
class MyClass():

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"¡Hola, {self.name}!")

my_class = MyClass("MoureDev")
print(my_class.name)
my_class.hello()

# Excepciones
try:
    print(0 / 0)
except:
    print("Se ha producido una excepción")
finally:
    print("Siempre se ejecuta el finally")