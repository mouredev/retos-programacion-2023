# Hola mundo
print("Hola, mundo!")

# Variables
variable_string = "Variable de tipo str"
variable_entero = 4
variable_flotante = 8.34
variable_booleana = True

# Constante
CONSTANTE = "Sigue siendo variable pero las mayusculas se usan como constantes"

# if | else if | else
if variable_booleana:
    print("Su valor es true")
elif variable_flotante > 10:
    print("Su valor es mayor a 10")
else:
    print("Ningunas de las condiciones anteriores se cumplieron")

# Estructuras
lista: list = [0, 1, 2, "tres"]
tupla: tuple = (0, 1, 2, "dos + 1")
conjunto: set = {0, 1, 2, "tres"}
diccionario: dict = {"clave_1": "valor_1", "clave_2": "valor_2"}

# for | foreach | while
for i in range(5):
    print(i)

for elemento in lista:
    print(elemento)

i = 0
while i < 5:
    print(i)
    i += 1

# Funciones
def funcion_con_parametros(parametro_1: str, parametro_2: float):
    print(f"Pasaste: {parametro_1} y {parametro_2}")

def funcion_sin_parametros():
    print("Solo necesitas llamar esta funcion")

def funcion_con_retorno(valor: int) -> int:
    return valor + 1

funcion_con_parametros("Hola", 3.3)
funcion_sin_parametros()
print(funcion_con_retorno(3))

# Clases
class MiClase:
    def __init__(self, id: str):
        self.id = id

    def show_id(self):
        print(self.id)

print(MiClase("Marco").show_id())

# Control de excepciones
try:
    print(3 / 0)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
finally:
    print("Esta parte se ejecuta con o sin error")
