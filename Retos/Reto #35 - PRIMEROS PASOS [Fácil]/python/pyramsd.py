# imprimir en consola
print("Hola, mundo!")


# Tipos de variables
var_string = "Belive"
var_int = 18
var_float = 24.7
var_bool = False


# Constantes
CONSTANTE = 3.1416


# Uso de if, else if y else
if var_int > CONSTANTE:
    print("var_int es mayor")
elif var_int == CONSTANTE:
    print("var_int y CONSTANTE son iguales")
else:
    print("CONSTANTE es menor a var_int")


# Estructura de datos
array = [1, 2, 3, 44, 4, 5]
lista = ["Manuel", "Shakira", "Pique", "Ibai", "Moure"]
tupla = (12, 23, 34, 45)
set = {56, 67, 78, 89, 90}
diccionario = {"nombre": "Sergio", "apellido": "Ruiz", "edad": 18}


# Bucles for
for nombre in lista:
    print(nombre)

for k in diccionario:
    print(f"{k}: {diccionario[k]}")


# Bucles while
iter = 0
while iter < len(array):
    print(array[iter])
    iter += 1


# Funciones:
# Sin parámetros y sin retorno
def imprir_en_consola():
    print("L-gante que lo keee")

# Sin parámetros y con retorno, para llamarla: print(funcion())
def mi_edad():
    return var_int

# Con parámetros y con retorno, para llamarla: print(funcion())
def es_mayor(a, b):
    return a > b

# Con parámetros y sin retorno
def multiplicar(a, b):
    print(f"Producto {a * b}")

imprir_en_consola()
print(mi_edad())
print(es_mayor(5, 3))
multiplicar(5, 8)


# Clase
class Vehiculo:
    def __init__(self, marca, asientos):
        self.marca = marca
        self.asientos = asientos
    
    def coche(self):
        print(f"Datos del coche:\n\tMarca: {self.marca}\
              \n\tAsientos: {self.asientos}")

coche1 = Vehiculo("R8", 2)
coche1.coche()


# Control de excepciones
numero = input("Esto es un input: ")
try:
    numero + 1
except TypeError as e:
    print(f"Error: {e}")
