# Hola mundo
print("Hola mundo")

# definicion de variables
string: str = "String"
numero_entero: int = 14
numero_decinal: float = 14.14
booleano: bool = True

# Constrante
CONSTANTE: str = "Suscribete"

# Usa un if, else if y else.
if numero_entero > 20:
    print("mayor que 20")
elif numero_entero < 10:
    print("menor que 10")
else:
    print("nuestro numero se encuentra entre 10 y 20")
# Crea diferentes
# funciones (con/sin parámetros
# y con/sin retorno).


def imprime_separador() -> None:
    print("**" * 20)


def imprime_separador_personalizado(separador: str) -> str:
    return separador * 20


# Crea estructuras como un array,
# lista,
# tupla,
# set y
# diccionario.

lista = [1, 2, 3, "esto es un string"]
tupla = (0, "Parte dos")
diccionario = {}
set = set()

# Usa un for, foreach y un while.
imprime_separador()

for i in range(len(lista)):
    print(i)

imprime_separador()

for elemento in lista:
    print(elemento)

imprime_separador()

i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1

print(imprime_separador_personalizado("++"))

# * - Crea una clase.


class Usuario:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y mi edad es de {self.edad}")


u1 = Usuario("Javier", 20)
u1.saludar()

# * - Muestra el control de excepciones.

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
