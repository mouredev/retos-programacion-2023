# Hola Mundo
print("Hola mundo!")

# Variable tipo String
nombre= "Solobino"

# Variable numerica entera
edad = 2

# Variable numerica decimal
peso = 13.5

# variable booleana
perro = True

# Constante
RAZA = "pitbull"

# Uso de if, else if, y else
if edad <=2:
    print("cachorro")
elif edad > 2 and edad < 10:
    print("perro Adulto")
else:
    print("perro Viejito")

# creacion de una Lista
marcas_autos: list = ["Ford","Nissan","Toyota","Mazda","SEAT"]

# creacion de una Tupla
razas_perro: tuple = ("Beagle","pitbull","Poodle")

# creacion de un Set
paises: set = {"Mexico", "España", "Colombia", "Brazil", "Argentina"}

# creacion de un Diccionario
calificaciones: dict = {"Gerardo" : 90, "Luis" : 85, "Alejandro" : 100, "Andres" : 98}

# La sentencia for
for raza in razas_perro:
    print(raza)

# La sentencia while
indice = 0
while indice < len(marcas_autos):
    print(marcas_autos[indice])
    indice += 1

# Funcion sin parametros
def imprimir_hola_mundo():
    print("Hola mundo")

# Funcion con parametros
def imprimir_nombre_edad(nombre: str, edad: int):
    print(f"Nombre: {nombre}, Edad: {edad}")

# Funcion con parametros con retorno
def imprime_nombre(nombre: str) -> str:
    return nombre

# Creacion de una Clase
class Vehiculo():
    
    def __init__(self, color, marca, ruedas):
        self.color = color
        self.marca = marca
        self.ruedas = ruedas

# Control de excepciones
buscar_indice = 5
try:
    print(marcas_autos[buscar_indice])
except IndexError:
    print("El indice que buscas no existe")










