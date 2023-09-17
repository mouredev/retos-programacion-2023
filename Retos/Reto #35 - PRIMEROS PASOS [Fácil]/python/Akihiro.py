# Hola mundo
print("Hola mundo")

# Variables
texto = ""
numero_entero = 0
numero_decimal = 1.0
boolean = True

# Constantes
CONSTAN = 11

# if, else if, else
if CONSTAN > 20:
    print("Numero mayor a 20")
elif CONSTAN == 21:
    print("Numero igual a 21")
else:
    print("No es ninguno")

# Array, lista, tupla, set, diccionario
array = [1, 2, 3, 4, 5]
Lista = ["hola", 1, 1.1, True]
tupla = (1, "hola", 1.1)
set = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
diccionario = {
    "Texto" : "texto",
    "Numero_entero" : 1,
    "Numero_decimal" : 1.1,
    "Booleano" : True
}

# Bucles
## For, también es foreach
for i in Lista:
    print("Dato lista: ", i)
## While
count = 0
while count < 10:
    print("Numero: ", count)
    count += 1

# Funciones
## sin parámetros y sin retorno
def func1 ():
    print("No retorno")
## solo con retorno
def func2 ():
    return 1
print(func2())
## con parámetros, sin retorno
def func3 (num1, num2):
    print(num1, num2)
func3(3, 5)
## con parámetros y con retorno
def func4 (num1, num2):
    return num1, num2
print(func4(2, 3))

# Clase
class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre # propiedad privada
        self.edad = edad # propiedad publica

class Estudiante(Persona): # Herencia
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad) #inicializar propiedades heredadas
        self.__grado = grado

    @property # forma de retornar una variable privada
    def nombre(self):
        return self.__nombre

    def __privada (self):
        print("Estoy oculto")

clase = Estudiante("Nombre", 12, 5)
print(clase)

# Excepciones
clase2 = Estudiante("Nombre", 12, 5)
try:
    CONSTAN = 12
    clase2.__nombre = 12
    clase2.__privada()
    print(clase2.nombre)
except AttributeError as e:
    print("hay errores")
else:
    print("Si no hay errores me ejecuto")
finally:
    print("Siempre me ejecuto")