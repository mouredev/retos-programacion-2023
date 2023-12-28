import string
import random
longitud = 0  
def generarPassword(largo,mayus,nros,simb):
  lista_caracteres = list(string.ascii_lowercase)
  password=[]
  if mayus == 'y':
    lista_caracteres += list(string.ascii_uppercase)
  if nros == 'y':
    lista_caracteres += list(string.digits)
  if simb == 'y':
    lista_caracteres += list(string.punctuation)
  for x in range(largo):
    password.append(random.choice(lista_caracteres))
  return ''.join(password)

while longitud<7 or longitud>17:
  longitud = int(input('Longitud de la contraseña (Entre 8 y 16): '))

mayus = input('Incluye mayúsculas (y/n): ')
nros = input('Incluye números (y/n): ')
simb = input('Incluye símbolos (y/n): ')

print(generarPassword(longitud,mayus,nros,simb))