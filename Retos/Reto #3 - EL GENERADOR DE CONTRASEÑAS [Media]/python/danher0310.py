# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */
import string
import random

def generate_password():
  params = ""    
  print("Si introduce cualquier cosa que no sea entre 8 a 16, su rango de contraseña sera de 8")
  length = (input("introduzca un rango de su contrasena entre 8 a 16: "))  
  
  if int(length):
    if int(length) < 9 and int(length) > 16:
      length = 8
    else:
      length
  else:
    length = 8
  print("Si introduce cualquier cosa diferente a si o no, su contrasena optara por usar las mayusculas por default.")
  mayus = (input("introduzca si o no si desee tener letras mayusculas: "))
  if mayus.lower() == 'no':
    params += string.ascii_lowercase
  else:
    params += string.ascii_letters
    
  print("Si introduce cualquier cosa diferente a si o no, su contrasena optara por usar los numeros por default.")
  num = (input("introduzca si o no si desee tener letras mayusculas: "))
  if num.lower() == 'no':
    params = params
  else:
    params += string.digits
    
  print("Si introduce cualquier cosa diferente a si o no, su contrasena optara por usar los simbolos por default.")
  simb = (input("introduzca si o no si desee tener letras mayusculas: "))
  if simb.lower() == 'no':
    params = params
  else:
    params += string.punctuation
    
  newPass = ""
  for i in range(int(length)):
    randomParams = random.choice(params)
    newPass +=randomParams
  print(newPass)


generate_password()
  
  