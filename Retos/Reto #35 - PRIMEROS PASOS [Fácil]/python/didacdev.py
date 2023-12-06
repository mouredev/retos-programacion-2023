# Hola mundo
print("Hola mundo")

# Variables
saludo = "Hola mundo"  # String
edad = 27  # Integer
altura = 1.75  # Float
programador = True  # Boolean

# Constantes
PI = 3.1416

# Condicionales
if programador:
    print("Eres programador")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad y no eres programador")

# Listas, tuplas, conjuntos y diccionarios
marcas = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour"]  # Listas
letras = ("a", "b", "c")  # Tuplas
numeros = {1, 2, 3, 4, 5}  # Conjuntos
datos = {"nombre": "Paco", "apellido": "Soria", "edad": 40}  # Diccionarios

# Bucles
for numero in range(1, 6):
    print(numero)

for numero in numeros:
    print(numero)

while edad < 18:
    print("Eres menor de edad")
    edad += 1


# Funciones
def get_edad() -> int:
    return 27


def add_year():
    edad += 1


def saludar(nombre: str):
    print("Hola " + nombre)


def saludar2(nombre: str) -> str:
    return "Hola " + nombre


# Clases
class Persona:
    # Constructor
    def __init__(self, nombre: str, apellido: str, edad: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


# Excepciones
try:
    print("Hola")
except:
    print("Ha ocurrido un error")
