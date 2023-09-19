'''
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
'''

# hola mundo
print('Hola, mundo!')

# creación de variables
var_string = 'esto es un string'
var_entero = 3
var_decimal = 2.8
var_boolean = True # o False

# esto es una constante, aunque en python no existen como tal
VAR_CONSTANTE = 'constante'

# if, else if, else
condicion = 1
if(condicion > 1):
  print('la condición es mayor que uno')
elif(condicion < 1):
  print('la condición es menor que uno')
else:
  print('ninguna de las anteriores')
  
# estructuras de datos
lista = ['manzana', 'fresa', 'pera', 'platano']
tupla = ('manzana', 'fresa', 'pera', 'platano')
set = {'manzana', 'fresa', 'pera', 'platano'}
dict = {
  'marca': 'Seat',
  'modelo': 'Ibiza',
  'year': 2021
}

# bucles
for x in range(6):
  print(x)
  
for fruta in lista:
  print(fruta)

i = 1
while i < 6:
  print(i)
  i += 1

def some_func():
  print('Esto es una función.')

some_func()

def suma(a: int, b: int) -> int:
  sum = a + b
  return sum

print('Suma: ', suma(3, 5))

class Coche:
  marca = 'Seat'
  modelo = 'Ibiza'
  
coche = Coche()
print(coche.marca, coche.modelo)

try:
  print(0 / 0)
except:
  print('Se ha producido una excepción!')
finally:
  print('Siempre se ejecuta el finally despues del try/except')