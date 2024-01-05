### Reto 3 ###

"""
  Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
  Podrás configurar generar contraseñas con los siguientes parámetros:
  - Longitud: Entre 8 y 16.
  - Con o sin letras mayúsculas.
  - Con o sin números.
  - Con o sin símbolos.
  (Pudiendo combinar todos estos parámetros entre ellos)
"""
import random

def characters (numbers=False,symbol=False):
  cont=random.randint(8,16)
  contraseña=""
  character=list (range(97,123))
  if numbers:
    character+=list (range(48,58))
  if symbol:
    character+= list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))
  for i in range (cont):
   contraseña+=chr(random.choice(character))
  print (f"La contrseña tiene {cont} dígitos")
  return contraseña


print (characters())
print (characters(numbers=True))
print (characters(symbol=True))
print (characters(numbers=True,symbol=True))
