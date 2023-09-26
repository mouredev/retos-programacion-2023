"""
 * Como cada año, el día 256 se celebra el "Día de la Programación".
 * En nuestra comunidad siempre hacemos una gran fiesta donde repartiremos 
 * 256 regalos para seguir aprendiendo programación:
 * https:#diadelaprogramacion.com
 *
 * Para seguir ayudando, te propongo este reto:
 * Mostrar la sintaxis de los principales elementos de un lenguaje
 * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
 *
 * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
 * y comenta cada bloque para identificar con qué se corresponde:
 * - Haz un "Hola, mundo!"
 * - Crea variables de tipo String, numéricas (enteras y decimales)
 *   y Booleanas (o cualquier tipo de dato primitivo).
 * - Crea una constante.
 * - Usa un if, else if y else.
 * - Crea estructuras como un array, lista, tuple, set y diccionario.
 * - Usa un for, foreach y un while.
 * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
 * - Crea una clase.
 * - Muestra el control de excepciones.
 *
 * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
 * de sintaxis básica de muchos lenguajes.
 *
 * ¡Muchas gracias!
"""

# Hola, mundo!

print("Hola, mundo!")


# Variables de tipo String, numéricas (enteras y decimales) y Booleanas

my_string = "Hola, mundo!"
my_integer = 23
my_decimal = 3.14
my_boolean = True


# Constante

# no existen las constantes como tal, pero se escriben en mayúsculas para
# entender que son o deberían tratarse como constantes

MY_NAME = "nlarrea"


# if, else if y else

if 2 > 4:
    print("2 es mayor que 4")
elif 2 < 4:
    print("2 es menor que 4")
else:
    print("2 y 4 son iguales")


# Estructuras tipo Array, lista, tuple, set y diccionario

mi_array = [1, 2, 3, 4, 5]          # Equivalente a lista
mi_set = {1, 1, 2, 3, 4, 4, 4, 5}   # elimina los valores repetidos
mi_tuple = (1, 2, 3, 4, 5)
mi_diccionario = {
    "nombre": "Naia",
    "edad": 25
}

print(type(mi_array))               # <class 'list'>
print(type(mi_set))                 # <class 'set'>
print(type(mi_tuple))               # <class 'tuple'>
print(type(mi_diccionario))         # <class 'dict'>


# Bucles for, foreach y while
for i in range(10):
    print(f"Iteración {i} del bucle for")

print("Shopping list:")
fruits = ["apple", "banana", "pineapple", "pear"]
for idx, fruit in enumerate(fruits):
    print(f"{idx + 1} - {fruit}")

i = 0
while (i < 10):
    print(f"Iteración {i} del bucle while")
    i += 1


# Funciones (con/sin parámetros y con/sin retorno)

def sin_params_ni_retorno():
    print("Saludos!")

def con_params_sin_retorno(name):
    print(f"Saludos {name}")

def sin_params_con_retorno():
    return 5 + 7

def con_params_con_retorno(numOne, numTwo):
    numThree = numOne + numTwo
    return numOne + numTwo + numThree

# llamadas a las funciones:
sin_params_ni_retorno()           # se imprime: Saludos!
con_params_sin_retorno("Naia")    # se imprime: Saludos Naia
sin_params_con_retorno()          # obtiene un: 12
con_params_con_retorno(2, 10)     # obtiene un: 24


# Crea una clase

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! My name is {self.name}")

    def compareAges(self, age):
        difference = abs(age - self.age)

        if age < self.age:
            print(f"You are {difference} year(s) older than me!")
        elif (age < self.age):
            print(f"I am {difference} year(s) older than you!")
        else:
            print("We are the same age!")

        return difference

# crear instancias de la clase
me = Person("Naia", 25)
another_person = Person("Cristina", 29)

print(me.name)          # Naia
print(me.age)           # 25
me.introduce()          # imprime: Hi! My name is Naia
me.compareAges(8)
# imprime: I am 17 year(s) older than you!
# se obtiene: 17

print(another_person.name)      # Cristina
# ...


# Muestra el control de excepciones

try:
    this_throws_an_error = 250 / 0
except Exception as error:
    print(f"{type(error).__name__}: {error}")
    # ZeroDivisionError: division by zero

try:
    raise TypeError("Se ha lanzado un error de tipo TypeError!")
except TypeError as error:
    print(error)
    # Se ha lanzado un error de tipo TypeError!

# Se pueden usar varios 'except' para gestionar diferentes errores
while True:
    try:
        user_ans = input("Enter a number between 0 and 5: ")
        assert(user_ans.isnumeric()), "You should enter a number!"

        user_ans = int(user_ans)
        
        if user_ans < 0 or user_ans > 5:
            raise ValueError("You should enter a number between 0 and 5!")
        
    except AssertionError as error:
        print(error)
        # You should enter a number!

    except ValueError as error:
        print(f"{type(error).__name__}: {error}")
        # ValueError: You should enter a number between 0 and 5!
    
    else:
        # Solo entra en el 'else' si el usuario introduce un valor entre 0 y 5
        break